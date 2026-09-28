"""Adapter contracts: fakes for orchestration, real codec/SCANS tests separately."""
import json
import sys
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import zipfile

import pytest
from PIL import Image

from mp4_analysis.thin.video import extract_video, image_hash, stitch_preview
from mp4_analysis.thin.parser import NativeParser
from mp4_analysis.thin.output import write_index, inspect_workbook


@pytest.fixture
def movie(monkeypatch, tmp_path):
    source=tmp_path/'recording.mp4';source.write_bytes(b'fixture, not an encoded video')
    def install(values, times=None):
        frames=[]
        for i,value in enumerate(values):
            image=Image.new('RGB',(80,60),'white')
            image.putpixel((30,30),(value,0,0))
            frames.append(SimpleNamespace(pts=i if times is None else times[i],time_base=Fraction(1,30),
                                          to_image=lambda img=image:img.copy()))
        class Container:
            streams=SimpleNamespace(video=[object()])
            def __enter__(self):return self
            def __exit__(self,*args):pass
            def decode(self,stream):return iter(frames)
        monkeypatch.setitem(sys.modules,'av',SimpleNamespace(open=lambda path:Container()))
        return source
    return install


def test_one_pixel_change_is_kept(movie,tmp_path):
    report=extract_video(movie([0,0,1,1,2]),tmp_path/'frames')
    assert [f['frame_index'] for f in report['frames']]==[0,2,4]
    assert report['identical_observations']==2
    assert report['selection_complete']
    assert not report['content_completeness_verified']


def test_rapid_pages_and_last_frame_are_kept(movie,tmp_path):
    report=extract_video(movie([2,3,4]),tmp_path/'frames')
    assert len(report['frames'])==3
    assert report['frames'][-1]['start_time']==pytest.approx(2/30)


def test_reverse_visit_is_not_removed(movie,tmp_path):
    report=extract_video(movie([1,2,1]),tmp_path/'frames')
    assert len(report['frames'])==3


def test_vfr_uses_presentation_timestamps(movie,tmp_path):
    report=extract_video(movie([1,2,3],[0,7,60]),tmp_path/'frames')
    assert [r['start_time'] for r in report['frames']]==[0,7/30,2]


def test_sampling_is_explicitly_incomplete_and_flushes_tail(movie,tmp_path):
    report=extract_video(movie([1,2,3]),tmp_path/'frames',sample_seconds=1)
    assert not report['selection_complete']
    assert [f['frame_index'] for f in report['frames']]==[0,2]


def test_cap_never_claims_full_coverage(movie,tmp_path):
    report=extract_video(movie([1,2,3]),tmp_path/'frames',max_frames=1)
    assert len(report['frames'])==1
    assert not report['selection_complete']


@pytest.mark.parametrize('options',[{'sample_seconds':-1},{'sample_seconds':float('nan')},
    {'start':-1},{'end':0},{'max_frames':0},{'roi':(0,0,200,100)}])
def test_invalid_selection_rejected(movie,tmp_path,options):
    with pytest.raises(ValueError):extract_video(movie([1,2]),tmp_path/'frames',**options)


def test_roi_mapping_is_explicit(movie,tmp_path):
    report=extract_video(movie([1,2]),tmp_path/'frames',roi=(10,20,40,30))
    f=report['frames'][0]
    assert f['source_offset']==[10,20] and (f['width'],f['height'])==(40,30)


@pytest.fixture
def upstream(monkeypatch,tmp_path):
    calls=[]
    raw={'parsing_res_list':[{'block_label':'table','block_bbox':[1,1,70,50],
        'block_content':'0x2800 | 0x2808 | 0 | 0'}], 'table_res_list':[{'pred_html':'<table></table>'}],
         'overall_ocr_res':{'rec_scores':[0.99,0.4]}}
    class Result:
        def save_to_json(self,save_path):
            Path(save_path,'source_res.json').write_text(json.dumps(raw))
        def save_to_markdown(self,save_path):Path(save_path,'source.md').write_text('0x2800 | 0x2808 | 0 | 0')
        def save_to_html(self,save_path):Path(save_path,'source.html').write_text('<table></table>')
        def save_to_xlsx(self,save_path):pass
        def save_to_word(self,save_path):raise RuntimeError('native exporter unavailable')
    class Engine:
        def __init__(self,**options):calls.append(options)
        def predict(self,path):
            calls.append(path);yield Result()
    monkeypatch.setitem(sys.modules,'paddleocr',SimpleNamespace(PPStructureV3=Engine))
    image=tmp_path/'source.png';Image.new('RGB',(80,60),'white').save(image)
    return image,calls


def test_native_result_and_export_are_not_rewritten(upstream,tmp_path):
    image,calls=upstream
    meta=NativeParser().parse(image,tmp_path/'native')
    assert meta['labels']=={'table':1} and meta['table_count']==1
    assert meta['low_confidence_observations']==1
    assert (tmp_path/'native/source.md').read_text()=='0x2800 | 0x2808 | 0 | 0'
    assert not meta['verified']


def test_cache_avoids_model_and_checks_output_hashes(upstream,tmp_path):
    image,calls=upstream
    parser=NativeParser();parser.parse(image,tmp_path/'native')
    count=len(calls)
    assert NativeParser().parse(image,tmp_path/'native')['cache_hit']
    assert len(calls)==count
    (tmp_path/'native/source.md').write_text('corrupt')
    assert not parser.parse(image,tmp_path/'native')['cache_hit']
    assert len(calls)>count


def test_export_failure_is_visible_and_not_cached_as_success(upstream,tmp_path):
    image,calls=upstream
    meta=NativeParser().parse(image,tmp_path/'native',word=True)
    assert meta['errors'][0]['stage']=='save_to_word'
    assert (tmp_path/'native/source_res.json').is_file()


def test_engine_change_invalidates_cache(upstream,tmp_path):
    image,calls=upstream
    NativeParser(threads=1).parse(image,tmp_path/'native')
    assert not NativeParser(threads=2).parse(image,tmp_path/'native')['cache_hit']


def test_blank_images_stitch_failure_preserves_inputs(tmp_path):
    pytest.importorskip('cv2')
    images=[]
    for i in range(2):
        path=tmp_path/f'{i}.png';Image.new('RGB',(300,200),'white').save(path);images.append(path)
    result=stitch_preview(images,tmp_path/'stitched.png')
    assert result['status']=='rejected'
    assert all(p.is_file() for p in images)
    assert not result['verified']


def test_index_is_not_accuracy_claim_and_escapes_text(tmp_path):
    report=write_index(tmp_path,{'source':'a'},[{'frame':{'frame_index':0,'start_time':0,'image':'x.png'},
        'directory':'native/f0','error':'<script>alert(1)</script>'}])
    assert report['status']=='PARTIAL_FAILURE'
    assert not report['accuracy_verified']
    page=(tmp_path/'index.html').read_text()
    assert '<script>' not in page and '&lt;script&gt;' in page


def test_excel_inspection_never_evaluates_formula(tmp_path):
    path=tmp_path/'book.xlsx'
    with zipfile.ZipFile(path,'w') as z:
        z.writestr('xl/worksheets/sheet1.xml','<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1"><f>1+1</f><v>2</v></c></row></sheetData></worksheet>')
    result=inspect_workbook(path)
    assert result['formula_review_required']
    assert result['sheets'][0]['cells']==1


def test_real_codec_roundtrip_preserves_three_quick_screens(tmp_path):
    av=pytest.importorskip('av',reason='remote integration job installs pinned PyAV')
    import cv2
    import numpy as np
    source=tmp_path/'quick.avi'
    writer=cv2.VideoWriter(str(source),cv2.VideoWriter_fourcc(*'FFV1'),30,(160,120))
    assert writer.isOpened()
    for value in (0,80,160):writer.write(np.full((120,160,3),value,dtype=np.uint8))
    writer.release()
    result=extract_video(source,tmp_path/'frames')
    assert result['selected_frames']==3 and result['selection_complete']
