"""Bounded same-engine experiment on saved inputs; never edits the 57-job cache.

Compare upstream cell-geometry HTML mode on three existing inputs, plus the
original source frame as a default-mode control. This is not a production
fallback and does not certify table correctness.
"""
import argparse
import json
import shutil
import time
import traceback
from pathlib import Path

from mp4_analysis.thin.parser import NativeParser
from mp4_analysis.thin.output import export_saved_word
from mp4_analysis.thin.video import file_hash

BASE_FINGERPRINT = '878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb'
CASES = [('group_000078_a', 'cells'), ('group_000018_b', 'cells'),
         ('frame_00000452', 'cells'), ('frame_00002373', 'default')]


def run_saved_probe(source, output):
    source, output = Path(source).resolve(), Path(output).resolve()
    if source == output or source in output.parents or output in source.parents:
        raise ValueError('source and experiment output must be disjoint')
    if output.exists():
        raise FileExistsError('experiment output already exists')
    report = json.loads((source/'report.json').read_text(encoding='utf-8'))
    if report.get('pending_parser_inputs') or report.get('parser_attempts') != 57:
        raise ValueError('expected completed 57-input baseline')
    baseline = NativeParser(ocr_models='mobile', threads=2)
    if baseline.fingerprint != BASE_FINGERPRINT:
        raise ValueError('baseline parser fingerprint mismatch; no inference performed')
    before = {str(p.relative_to(source)): file_hash(p)
              for p in (source/'native').rglob('*') if p.is_file()}
    for item in report['items']:
        directory = source/item['directory']
        if not directory.resolve().is_relative_to(source/'native'):
            raise ValueError('native directory escapes source')
        cache = json.loads((directory/'adapter.json').read_text(encoding='utf-8'))
        if cache.get('errors') or cache['signature']['parser'] != BASE_FINGERPRINT:
            raise ValueError('invalid baseline cache')
        if file_hash(source/item['input_image']) != cache['signature']['input_sha256']:
            raise ValueError('baseline input image changed')
        for name, digest in cache['files'].items():
            path = (directory/name).resolve()
            if not path.is_relative_to(directory) or file_hash(path) != digest:
                raise ValueError('baseline native resource changed')
    output.mkdir(parents=True)
    jobs = {j['id']: j for j in report['items']}
    cells = NativeParser(ocr_models='mobile', threads=2, table_mode='cells')
    records = []
    summary = {'cases': records, 'planned': len(CASES), 'content_acceptance': 'REVIEW_REQUIRED',
               'baseline_fingerprint': baseline.fingerprint, 'cells_fingerprint': cells.fingerprint,
               'baseline_native_files': len(before), 'native_outputs_modified': False}
    try:
        for job_id, mode in CASES:
            started = time.monotonic()
            entry = {'job_id': job_id, 'mode': mode}
            records.append(entry)
            job = jobs.get(job_id)
            image = source/(job['input_image'] if job else f'frames/{job_id}.png')
            entry['input_sha256'] = file_hash(image)
            entry['source_job'] = job
            saved_image = output/'inputs'/image.name
            saved_image.parent.mkdir(exist_ok=True)
            shutil.copy2(image, saved_image)
            if job:
                shutil.copytree(source/job['directory'], output/'baseline'/job_id)
            parser = cells if mode == 'cells' else baseline
            if parser.engine is None:
                parser.engine = cells.engine or baseline.engine
            native = output/'native'/f'{job_id}_{mode}'
            try:
                entry['native'] = parser.parse(image, native, word=True)
                try:
                    entry['word'] = export_saved_word(native, output/'word'/f'{job_id}_{mode}')
                except Exception:
                    entry['word_error'] = traceback.format_exc()
            except Exception:
                entry['error'] = traceback.format_exc()
            entry['elapsed_seconds'] = round(time.monotonic()-started, 3)
            summary['pending'] = len(CASES)-len(records)
            (output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
            print(json.dumps(entry, ensure_ascii=False), flush=True)
    finally:
        after = {str(p.relative_to(source)): file_hash(p)
                 for p in (source/'native').rglob('*') if p.is_file()}
        summary['native_outputs_modified'] = before != after
        summary['pending'] = len(CASES)-len(records)
        (output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    if before != after:
        raise RuntimeError('baseline changed during isolated experiment')
    if any('error' in entry for entry in records):
        raise RuntimeError('native experiment failed; inspect preserved summary')
    return summary


if __name__ == '__main__':
    arguments = argparse.ArgumentParser(description=__doc__)
    arguments.add_argument('source', type=Path)
    arguments.add_argument('-o', '--output', type=Path, required=True)
    args = arguments.parse_args()
    run_saved_probe(args.source, args.output)
