"""Bounded OCR controls before layout parsing; no table/video rerun.

Select --recognizer mobile to run the first two controls without loading a
second model. --preflight checks saved inputs and installed versions but NEVER
runs inference. Original native evidence remains immutable.
"""
from __future__ import annotations
import argparse
import importlib.metadata
import json
import shutil
import sys
import time
from pathlib import Path
from mp4_analysis.thin.video import file_hash

REQUIRED_VERSIONS = {'paddleocr': '3.7.0', 'paddlex': '3.7.2', 'paddlepaddle': '3.2.2'}
# Match pyproject.toml; interpreter identity is provenance, not a 3.11-only gate.
PYTHON_REQUIREMENT = '>=3.10,<3.13'
BASELINE_PYTHON = '3.11.16'


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
        if cache.get('native_json') not in cache['files']:
            raise ValueError('native JSON is not in the hashed manifest')
        payload = json.loads((native/cache['native_json']).read_text(encoding='utf-8'))
        payload = payload.get('res', payload)
        selected.append((job, image, native, payload))
    return selected


def validate_recognizers(recognizers):
    models = tuple(recognizers)
    if not models or len(models) != len(set(models)) or any(m not in {'mobile', 'server'} for m in models):
        raise ValueError('select unique mobile/server recognizers')
    return models


def runtime_status():
    """Metadata only. Do not import Paddle or download models in a preflight."""
    versions = {}
    for name in REQUIRED_VERSIONS:
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = 'not-installed'
    python_version = sys.version.split()[0]
    python_supported = (3, 10) <= sys.version_info[:2] < (3, 13)
    baseline_python_match = python_version == BASELINE_PYTHON
    warnings = []
    if not python_supported:
        warnings.append(f'Python is outside the project requirement {PYTHON_REQUIREMENT}.')
    elif not baseline_python_match:
        warnings.append('Python differs from the historical baseline; use before/after '
                        'runs in this same environment, not a cross-version causal claim.')
    return {'python': python_version, 'versions': versions,
            'python_requirement': PYTHON_REQUIREMENT, 'python_supported': python_supported,
            'baseline_python': BASELINE_PYTHON, 'baseline_python_match': baseline_python_match,
            'ready': python_supported and versions == REQUIRED_VERSIONS,
            'warnings': warnings, 'model_cache_checked': False,
            'dependencies_import_checked': False,
            'note': 'Metadata readiness and a matching Python version do not prove '
                    'full environment equivalence, model availability or successful inference.'}


def preflight(source, frames=(2920, 2950), recognizers=('mobile', 'server')):
    models = validate_recognizers(recognizers)
    selected = validate_source(source, frames)
    settings = [(p['overall_ocr_res']['text_det_params'],
                 p['overall_ocr_res']['text_rec_score_thresh']) for _, _, _, p in selected]
    if any(s != settings[0] for s in settings):
        raise ValueError('selected frames have different saved OCR parameters')
    runtime = runtime_status()
    return {'status': 'RUNTIME_READY' if runtime['ready'] else 'BLOCKED_RUNTIME',
            'inference_performed': False, 'executed': 0, 'planned': len(selected)*len(models),
            'pending': len(selected)*len(models), 'recognizers': list(models),
            'runtime': runtime, 'source_validation_scope': 'selected frames and their native exports only',
            'inputs': [{'id': j['id'], 'sha256': file_hash(im)} for j, im, _, _ in selected],
            'text_det_params': settings[0][0], 'text_rec_score_thresh': settings[0][1]}


def verify_returned_settings(raw, expected):
    """Do not count a differently configured OCR run as a matched control."""
    if (raw.get('text_det_params') != expected['text_det_params']
            or raw.get('text_rec_score_thresh') != expected['text_rec_score_thresh']):
        raise ValueError('returned OCR parameters differ from saved baseline; raw result retained')


def run(source, output, evidence, frames=(2920, 2950), *, recognizers=('mobile', 'server')):
    source, output = Path(source).resolve(), Path(output).resolve()
    if source == output or source in output.parents or output in source.parents:
        raise ValueError('source and output must be disjoint')
    if output.exists():
        raise FileExistsError(output)
    models = validate_recognizers(recognizers)
    check = preflight(source, frames, models)
    if not check['runtime']['ready']:
        raise RuntimeError('supported Python >=3.10,<3.13 / pinned Paddle runtime unavailable; run --preflight for details')
    selected = validate_source(source, frames)
    clauses = json.loads(Path(evidence).read_text(encoding='utf-8'))['limit_clauses']['records']
    before = {str(p.relative_to(source)): file_hash(p) for p in (source/'native').rglob('*') if p.is_file()}
    output.mkdir(parents=True)
    summary = {'versions': check['runtime']['versions'], 'python': check['runtime']['python'],
               'runtime': check['runtime'],
               'planned': check['planned'], 'cases': [], 'pending': check['planned'],
               'recognizers': list(models), 'source_evidence_sha256': file_hash(Path(evidence)),
               'content_acceptance': 'NOT_ACCEPTED', 'inference_stage': 'GeneralOCR before layout',
               'full_video_rerun': False, 'native_files_count': len(before), 'error': None}
    began = time.monotonic()
    try:
        from paddleocr import PaddleOCR
        for model in models:
            params = check['text_det_params']
            options = dict(text_detection_model_name='PP-OCRv5_mobile_det',
                text_recognition_model_name=f'PP-OCRv5_{model}_rec',
                use_doc_orientation_classify=False, use_doc_unwarping=False,
                use_textline_orientation=False, device='cpu', cpu_threads=2,
                enable_mkldnn=True, text_det_limit_side_len=params['limit_side_len'],
                text_det_limit_type=params['limit_type'], text_det_thresh=params['thresh'],
                text_det_box_thresh=params['box_thresh'], text_det_unclip_ratio=params['unclip_ratio'],
                text_rec_score_thresh=check['text_rec_score_thresh'])
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
                verify_returned_settings(raw, check)
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
    except BaseException as exc:
        summary['error'] = f'{type(exc).__name__}: {exc}'
        raise
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


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('-o', '--output', type=Path)
    p.add_argument('--evidence', type=Path, default=Path('docs/step11_evidence.json'))
    p.add_argument('--frame', type=int, action='append')
    p.add_argument('--recognizer', choices=('mobile', 'server'), action='append')
    p.add_argument('--preflight', action='store_true', help='validate saved inputs/runtime; never run inference')
    a = p.parse_args()
    frames, models = a.frame or (2920, 2950), a.recognizer or ('mobile', 'server')
    if a.preflight:
        result = preflight(a.source, frames, models)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result['runtime']['ready'] else 2
    if a.output is None:
        p.error('--output is required for inference')
    run(a.source, a.output, a.evidence, frames, recognizers=models)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
