"""Native stitching orchestration; routing is not semantic coverage."""
import json
from pathlib import Path
import pytest
from PIL import Image
from mp4_analysis.thin import video
from mp4_analysis.thin.parser import NativeParser


def fixture_manifest(tmp_path, count=19):
    frames=[]
    (tmp_path/'frames').mkdir(exist_ok=True)
    for i in range(count):
        path=tmp_path/'frames'/f'{i}.png'
        Image.new('RGB',(40,40),(i,0,0)).save(path)
        frames.append({'frame_index':i,'image':path.name,'start_time':float(i),
                       'end_time':float(i),'coordinate_system':'source_frame_pixels'})
    return {'frames':frames,'selection_complete':False}


def test_native_subset_is_rejected(monkeypatch,tmp_path):
    import cv2
    import numpy as np
    manifest=fixture_manifest(tmp_path,3)
    class Subset:
        def setCompositingResol(self,v): pass
        def stitch(self,images): return cv2.Stitcher_OK,np.zeros((40,40,3),np.uint8)
        def component(self): return [0,2]
    monkeypatch.setattr(cv2,'Stitcher_create',lambda _:Subset())
    result=video.stitch_preview([tmp_path/'frames'/f['image'] for f in manifest['frames']],tmp_path/'x.png')
    assert result['status']=='rejected'
    assert result['included_input_indices']==[0,2]
    assert not (tmp_path/'x.png').exists()


def test_entire_timeline_including_tail_is_routed(monkeypatch,tmp_path):
    manifest=fixture_manifest(tmp_path)
    calls=[]
    def stitch(paths,target):
        calls.append(paths)
        if len(calls)==2:return {'status':'rejected'}
        target.parent.mkdir(exist_ok=True)
        Image.new('RGB',(40,80),'white').save(target)
        return {'status':'candidate','image':str(target),'verified':False}
    monkeypatch.setattr(video,'stitch_preview',stitch)
    result=video.prepare_reconstructions(manifest,tmp_path)
    assert len(calls)==3
    assert result['candidate_count']==2
    assert result['all_selected_frames_routed']
    assert not result['content_completeness_verified']
    assert {f['frame_index'] for j in result['jobs'] for f in j['source_frames']}==set(range(19))
    assert all((tmp_path/'frames'/f['image']).exists() for f in manifest['frames'])
    assert any(j['kind']=='source_frame' for j in result['jobs'])
    assert video.prepare_reconstructions(manifest,tmp_path)['cache_hit']
    assert len(calls)==3
    (tmp_path/result['jobs'][0]['input_image']).write_bytes(b'broken')
    assert not video.prepare_reconstructions(manifest,tmp_path)['cache_hit']
    assert len(calls)==6


def test_all_failures_keep_every_original(monkeypatch,tmp_path):
    manifest=fixture_manifest(tmp_path,10)
    monkeypatch.setattr(video,'stitch_preview',lambda *_:{'status':'rejected'})
    result=video.prepare_reconstructions(manifest,tmp_path)
    assert result['candidate_count']==0 and len(result['jobs'])==10
    assert result['unrouted_selected_frames']==[]


@pytest.mark.parametrize('count',[0,1,2,8,9,14,15])
def test_boundary_batch_sizes_have_no_unrouted_frames(monkeypatch,tmp_path,count):
    manifest=fixture_manifest(tmp_path,count)
    monkeypatch.setattr(video,'stitch_preview',lambda *_:{'status':'rejected'})
    result=video.prepare_reconstructions(manifest,tmp_path)
    assert len(result['jobs'])==count and result['all_selected_frames_routed']


def test_invalid_batching_rejected(tmp_path):
    manifest=fixture_manifest(tmp_path,2)
    for options in ({'group_size':1},{'group_size':9},{'overlap':8},{'overlap':-1}):
        with pytest.raises(ValueError): video.prepare_reconstructions(manifest,tmp_path,**options)


def test_mobile_uses_upstream_models_and_distinct_cache_key():
    default=NativeParser();mobile=NativeParser(ocr_models='mobile')
    assert mobile.options['text_detection_model_name']=='PP-OCRv5_mobile_det'
    assert mobile.options['text_recognition_model_name']=='PP-OCRv5_mobile_rec'
    assert default.fingerprint!=mobile.fingerprint
    assert 'text_detection_model_name' not in default.options
    with pytest.raises(ValueError): NativeParser(ocr_models='unknown')


def test_actual_scans_on_overlapping_canvas(tmp_path):
    import cv2
    import numpy as np
    rng=np.random.default_rng(71)
    canvas=rng.integers(0,256,(1000,600,3),dtype=np.uint8)
    # Native image features and SCANS, no mock of registration/composition.
    paths=[]
    for i,offset in enumerate([0,250,400]):
        path=tmp_path/f'{i}.png';Image.fromarray(canvas[offset:offset+600]).save(path);paths.append(path)
    result=video.stitch_preview(paths,tmp_path/'result.png')
    assert result['status']=='candidate'
    assert sorted(result['included_input_indices'])==[0,1,2]
    assert not result['verified']
    assert Image.open(tmp_path/'result.png').height>900
