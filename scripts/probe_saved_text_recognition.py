"""Four fixed-input OCR controls before layout parsing; no table/video rerun.

Use the SAME mobile detector and saved detection parameters. Change only the
recognition model in the second pair. Original native evidence is immutable.
This is diagnosis, not automatic text repair or source-content acceptance.
"""
from __future__ import annotations
import argparse
import importlib.metadata
import json
import shutil
import time
from pathlib import Path
from mp4_analysis.thin.video import file_hash


def compact(text):
    """Only whitespace normalization; never erase punctuation or identifiers."""
    return ''.join(text.split())


def validate_source(source, frames):
    source = Path(source).resolve()
    report = json.loads((source/'report.json').read_text(encoding='utf-8'))
    if report.get('parser_attempts') != 57 or report.get('pending_parser_inputs') != 0:
        raise ValueError('expected completed 57-input baseline')
    if not frames or len(frames) != len(set(frames)):
        raise ValueError('choose unique source frame indices')
    jobs = {j['id']: j for j in report['items']}
    selected = []
    for index in frames:
        job = jobs.get(f'frame_{index:08d}')
        if job is None or job.get('kind') != 'source_frame':
            raise ValueError('frame is not an existing source-frame job')
        image = (source/job['input_image']).resolve()
        native = (source/job['directory']).resolve()
        if not image.is_relative_to(source) or not native.is_relative_to(source):
            raise ValueError('nonlocal source resource')
        cache = json.loads((native/'adapter.json').read_text(encoding='utf-8'))
        if cache.get('errors') or not cache.get('files'):
            raise ValueError('unsuccessful native evidence')
        if file_hash(image) != cache['signature']['input_sha256']:
            raise ValueError('source image changed')
        for name, digest in cache['files'].items():
            p = (native/name).resolve()
            if not p.is_relative_to(native) or file_hash(p) != digest:
                raise ValueError('native resource changed or nonlocal')
        payload = json.loads((native/cache['native_json']).read_text(encoding='utf-8'))
        payload = payload.get('res', payload)
        selected.append((job, image, native, payload))
    return selected


def run(source, output, evidence, frames=(2920, 2950)):
    source, output = Path(source).resolve(), Path(output).resolve()
    if source == output or source in output.parents or output in source.parents:
        raise ValueError('source and output must be disjoint')
    if output.exists():
        raise FileExistsError(output)
    selected = validate_source(source, frames)
    versions = {p: importlib.metadata.version(p) for p in ('paddleocr', 'paddlex', 'paddlepaddle')}
    if versions != {'paddleocr': '3.7.0', 'paddlex': '3.7.2', 'paddlepaddle': '3.2.2'}:
        raise ValueError('fixed-version experiment only')
    clauses = json.loads(Path(evidence).read_text(encoding='utf-8'))['limit_clauses']['records']
    before = {str(p.relative_to(source)): file_hash(p) for p in (source/'native').rglob('*') if p.is_file()}
    output.mkdir(parents=True)
    summary = {'versions': versions, 'planned': len(selected)*2, 'cases': [],
               'pending': len(selected)*2, 'source_evidence_sha256': file_hash(Path(evidence)),
               'content_acceptance': 'NOT_ACCEPTED', 'inference_stage': 'GeneralOCR before layout',
               'full_video_rerun': False, 'native_files_count': len(before)}
    began = time.monotonic()
    try:
        from paddleocr import PaddleOCR
        for model in ('mobile', 'server'):
            params = selected[0][3]['overall_ocr_res']['text_det_params']
            options = dict(text_detection_model_name='PP-OCRv5_mobile_det',
                text_recognition_model_name=f'PP-OCRv5_{model}_rec',
                use_doc_orientation_classify=False, use_doc_unwarping=False,
                use_textline_orientation=False, device='cpu', cpu_threads=2,
                enable_mkldnn=True, text_det_limit_side_len=params['limit_side_len'],
                text_det_limit_type=params['limit_type'], text_det_thresh=params['thresh'],
                text_det_box_thresh=params['box_thresh'], text_det_unclip_ratio=params['unclip_ratio'],
                text_rec_score_thresh=0.0)
            init = time.monotonic()
            engine = PaddleOCR(**options)
            init_seconds = time.monotonic()-init
            for job, image, native, payload in selected:
                name = job['id']+'_'+model
                dest = output/name; dest.mkdir()
                shutil.copy2(image, dest/'input.png')
                shutil.copy2(native/payload_path(native), dest/'baseline_layout.json')
                start = time.monotonic()
                result = next(iter(engine.predict(str(image))))
                result.save_to_json(str(dest/'raw_ocr.json'))
                raw = json.loads((dest/'raw_ocr.json').read_text(encoding='utf-8'))
                raw = raw.get('res', raw)
                # Do not call this raw output the same as PP-Structure's mutable overall_ocr_res.
                text = '\n'.join(raw['rec_texts'])
                (dest/'observed_text.txt').write_text(text, encoding='utf-8')
                hits = [c['id'] for c in clauses if compact(c['expected_text']) in compact(text)]
                item = {'id': name, 'frame': job['frame'], 'source_sha256': file_hash(image),
                    'options': options, 'text_det_params': raw.get('text_det_params'),
                    'rec_text_count': len(raw['rec_texts']), 'exact_anchor_hits': hits,
                    'elapsed_seconds': round(time.monotonic()-start, 4),
                    'model_initialization_seconds': round(init_seconds, 4),
                    'raw_ocr_sha256': file_hash(dest/'raw_ocr.json'),
                    'full_clause_acceptance': False}
                summary['cases'].append(item)
                summary['pending'] = summary['planned']-len(summary['cases'])
                (output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
                print(json.dumps(item, ensure_ascii=False), flush=True)
            del engine
    finally:
        after = {str(p.relative_to(source)): file_hash(p) for p in (source/'native').rglob('*') if p.is_file()}
        summary['native_files_unchanged'] = before == after
        summary['elapsed_seconds'] = round(time.monotonic()-began, 4)
        (output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    if before != after:
        raise RuntimeError('native evidence changed')
    return summary


def payload_path(native):
    return json.loads((native/'adapter.json').read_text(encoding='utf-8'))['native_json']


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('-o', '--output', required=True, type=Path)
    p.add_argument('--evidence', type=Path, default=Path('docs/step11_evidence.json'))
    p.add_argument('--frame', type=int, action='append')
    a = p.parse_args()
    run(a.source, a.output, a.evidence, a.frame or (2920, 2950))
