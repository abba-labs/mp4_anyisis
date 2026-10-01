"""One local synchronous pipeline connecting parser and output modules."""
from __future__ import annotations

import json
from pathlib import Path

from .utils import file_hash, load_screenshots
from .parser import NativeParser
from .output import inspect_workbook, write_index


def run(source, output, *, word=False, device='cpu', threads=2,
        parser=None, mkldnn=True, table_mode='default', ocr_models='server'):
    source = Path(source).resolve()
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    frames_dir = output / 'frames'
    manifest_path = output / 'manifest.json'

    if not source.is_dir():
        raise ValueError(f"Source must be a directory of screenshots: {source}")

    manifest = load_screenshots(source, frames_dir)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

    parser = parser if parser is not None else NativeParser(
        device=device, threads=threads, mkldnn=mkldnn, table_mode=table_mode, ocr_models=ocr_models
    )

    jobs = [
        {
            'id': f"frame_{f['frame_index']:08d}",
            'input_image': f"frames/{f['image']}",
            'frame': f,
            'source_frames': [f],
            'kind': 'source_frame'
        }
        for f in manifest['frames']
    ]

    items = []
    try:
        for job in jobs:
            frame = job['frame']
            relative = f"native/{job['id']}"
            item = dict(job, directory=relative)
            try:
                item['native'] = parser.parse(output / job['input_image'], output / relative, word=word)
                item['workbooks'] = [
                    inspect_workbook(output / relative / name)
                    for name in item['native']['files']
                    if name.endswith('.xlsx')
                ]
            except Exception as exc:
                item['error'] = f'{type(exc).__name__}: {exc}'
            items.append(item)
            print(
                f"{len(items)}/{len(jobs)} input={frame['frame_index']} "
                f"{'ERROR' if item.get('error') else item['native']['labels']}",
                flush=True
            )
            if item.get('error') and parser.engine is None:
                break
    finally:
        write_index(output, manifest, items)

    report = write_index(output, manifest, items)
    if len(items) != len(jobs) or report['status'] in {'PARTIAL_FAILURE', 'NO_CONTENT'}:
        raise RuntimeError('pipeline incomplete; see report.json')
    return report

