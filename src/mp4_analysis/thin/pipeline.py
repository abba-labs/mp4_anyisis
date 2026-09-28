"""One local synchronous pipeline connecting three concrete modules."""
from __future__ import annotations

import json
from pathlib import Path

from .video import extract_video, file_hash, stitch_preview, prepare_reconstructions
from .parser import NativeParser
from .output import inspect_workbook, write_index


def run(source, output, *, sample_seconds=0.0, start=0.0, end=None,
        max_frames=None, roi=None, word=False, scans=False, device='cpu', threads=2,
        parser=None, mkldnn=True, table_mode='default', reconstruct=False, ocr_models='server'):
    roi = list(roi) if roi is not None else None
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    frames_dir = output/'frames'
    manifest_path = output/'video.json'
    config = dict(sample_seconds=sample_seconds,start=start,end=end,max_frames=max_frames,roi=roi)
    signature = {'source_sha256':file_hash(Path(source)), 'options':config, 'schema':1}
    previous = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else None
    if previous is not None and previous.get('signature') != signature:
        raise ValueError('output belongs to a different input/config; use another output directory')
    if previous and all((frames_dir/f['image']).is_file() and file_hash(frames_dir/f['image']) == f['file_sha256'] for f in previous['frames']):
        manifest = previous
    else:
        manifest = extract_video(source,frames_dir,**config)
        manifest['signature']=signature
        for frame in manifest['frames']:
            frame['file_sha256']=file_hash(frames_dir/frame['image'])
        manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    parser = parser if parser is not None else NativeParser(device=device, threads=threads, mkldnn=mkldnn, table_mode=table_mode, ocr_models=ocr_models)
    reconstruction = prepare_reconstructions(manifest, output) if reconstruct else None
    jobs = reconstruction['jobs'] if reconstruction else [
        {'id':f"frame_{f['frame_index']:08d}", 'input_image':f"frames/{f['image']}",
         'frame':f, 'source_frames':[f], 'kind':'source_frame'} for f in manifest['frames']]
    items=[]
    try:
        for job in jobs:
            frame = job['frame']
            relative = f"native/{job['id']}"
            item=dict(job, directory=relative)
            try:
                item['native']=parser.parse(output/job['input_image'],output/relative,word=word)
                item['workbooks']=[inspect_workbook(output/relative/name) for name in item['native']['files'] if name.endswith('.xlsx')]
            except Exception as exc:
                item['error']=f'{type(exc).__name__}: {exc}'
            items.append(item)
            print(f"{len(items)}/{len(jobs)} input={frame['frame_index']} "
                  f"{'ERROR' if item.get('error') else item['native']['labels']}",flush=True)
            # Missing engine/dependencies will not improve by retrying every frame.
            if item.get('error') and parser.engine is None:
                break
    finally:
        # Even an interrupted native call leaves an honest partial index.
        write_index(output,manifest,items,reconstruction=reconstruction)
    stitch=None
    if scans and len(manifest['frames'])>=2:
        selected=manifest['frames'][:8]
        stitch=stitch_preview([frames_dir/f['image'] for f in selected],output/'stitch_preview.png')
        stitch['input_frame_indices']=[f['frame_index'] for f in selected]
    report=write_index(output,manifest,items,stitch=stitch,reconstruction=reconstruction)
    if len(items)!=len(jobs) or report['status'] in {'PARTIAL_FAILURE','NO_CONTENT'}:
        raise RuntimeError('pipeline incomplete; see report.json')
    return report
