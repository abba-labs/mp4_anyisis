"""Resume the saved 57-job experiment without changing its input plan.

This is an experiment runner, not a new pipeline or a content-acceptance gate.
The immutable original ZIP must be kept alongside the resumed output.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys
import time
import traceback

from mp4_analysis.thin.video import file_hash, prepare_reconstructions
from mp4_analysis.thin.parser import NativeParser
from mp4_analysis.thin.pipeline import run


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def checked_path(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if path == root or root not in path.parents:
        raise ValueError(f'unsafe artifact member: {relative}')
    return path


def validate_saved(root, evidence, fingerprint):
    """Read-only validation. Reject mismatches BEFORE NativeParser can clear a target."""
    root = Path(root).resolve()
    manifest = load(root/'video.json')
    plan = load(root/'reconstruction.json')
    report = load(root/'report.json')
    completed = evidence['completed_cache_job_ids']
    pending = evidence['pending_job_ids_in_plan_order']
    if fingerprint != evidence['parser_identity']['fingerprint']:
        raise ValueError('parser fingerprint changed; refusing destructive cache misses')
    if [j['id'] for j in plan['jobs']] != completed + pending:
        raise ValueError('saved job order changed')
    if [j['id'] for j in report['items']] != completed:
        raise ValueError('saved report completed jobs differ')
    if manifest['signature'] != {'source_sha256': evidence['source']['sha256'],
                                'options': evidence['source']['options'], 'schema': 1}:
        raise ValueError('video signature changed')
    hashes = {}
    for frame in manifest['frames']:
        path = checked_path(root, 'frames/'+frame['image'])
        if file_hash(path) != frame['file_sha256']:
            raise ValueError(f'frame hash mismatch: {path.name}')
    for name, digest in plan['derived_files'].items():
        if file_hash(checked_path(root, name)) != digest:
            raise ValueError(f'composite hash mismatch: {name}')
    for job in plan['jobs'][:len(completed)]:
        target = checked_path(root, 'native/'+job['id'])
        adapter = load(target/'adapter.json')
        expected = {'input_sha256': file_hash(checked_path(root, job['input_image'])),
                    'parser': fingerprint, 'word': True}
        if adapter.get('signature') != expected or adapter.get('errors') or not adapter.get('files'):
            raise ValueError(f'invalid successful cache: {job["id"]}')
        for name, digest in adapter['files'].items():
            path = checked_path(target, name)
            if file_hash(path) != digest:
                raise ValueError(f'export hash mismatch: {job["id"]}/{name}')
            hashes[str(path.relative_to(root))] = digest
        hashes[str((target/'adapter.json').relative_to(root))] = file_hash(target/'adapter.json')
    return plan, hashes


def main():
    import cv2
    root = Path(sys.argv[1]).resolve()
    evidence = load('docs/handoff_evidence_2026-09-28.json')
    source = Path(evidence['source']['repository_path'])
    if file_hash(source) != evidence['source']['sha256']:
        raise ValueError('source MP4 hash changed')
    if sys.version_info[:2] != (3, 11) or cv2.__version__ != evidence['reconstruction']['opencv_version_string']:
        raise ValueError('Python/OpenCV environment differs from the saved run')
    cv2.setNumThreads(2)
    parser = NativeParser(ocr_models='mobile', threads=2)
    plan, old_hashes = validate_saved(root, evidence, parser.fingerprint)
    reconstruction = prepare_reconstructions(load(root/'video.json'), root)
    if not reconstruction.get('cache_hit') or reconstruction['jobs'] != plan['jobs']:
        raise ValueError('reconstruction did not reuse the exact saved job plan')
    preflight = {'source_sha256': file_hash(source), 'parser_fingerprint': parser.fingerprint,
                 'versions': parser.versions, 'reconstruction_cache_hit': True,
                 'successful_cache_entries_validated': len(evidence['completed_cache_job_ids']),
                 'planned_job_ids': [j['id'] for j in plan['jobs']]}
    (root.parent/'resume_preflight.json').write_text(json.dumps(preflight, indent=2), encoding='utf-8')
    print('PREFLIGHT', json.dumps(preflight), flush=True)
    begun = time.monotonic()
    error = None
    try:
        report = run(source, root, sample_seconds=1.0, reconstruct=True,
                     ocr_models='mobile', word=True, parser=parser)
    except BaseException:
        error = traceback.format_exc()
        print(error, flush=True)
        report = load(root/'report.json')
    preserved = all(file_hash(checked_path(root, name)) == digest for name, digest in old_hashes.items())
    items = report.get('items', [])
    cache_ids = [i['id'] for i in items if i.get('native', {}).get('cache_hit')]
    failed = [i['id'] for i in items if i.get('error') or i.get('native', {}).get('errors')]
    reset_matches = []
    anchor = 'ADC数字控制器不能早于模拟ADC解复位'
    for item in items:
        native = item.get('native', {})
        if not native.get('native_json'):
            continue
        raw = load(root/item['directory']/native['native_json'])
        data = raw.get('res', raw)
        for block in data.get('parsing_res_list', []):
            if anchor in ''.join(str(block.get('block_content', '')).split()):
                reset_matches.append({'job_id': item['id'], 'bbox': block.get('block_bbox'),
                                      'text': block['block_content']})
    summary = {'source_run_id': evidence['workflow_run_id'], 'source_artifact_id': evidence['artifact']['id'],
               'elapsed_seconds': round(time.monotonic()-begun, 3), 'error': error,
               'status': report['status'], 'planned': len(plan['jobs']),
               'processed': len(items), 'failed_job_ids': failed,
               'pending': report['pending_parser_inputs'], 'cache_hit_job_ids': cache_ids,
               'new_successes': len(items)-len(cache_ids)-len(failed),
               'old_native_files_unchanged': preserved,
               'outputs': {ext: len(list(root.rglob('*.'+ext))) for ext in ['docx','xlsx','md']},
               'reset_anchor_matches': reset_matches,
               'content_completeness_verified': False, 'office_visual_acceptance_completed': False}
    (root.parent/'resume_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print('RESUME_SUMMARY', json.dumps(summary, ensure_ascii=False), flush=True)
    if error or failed or summary['pending'] or not preserved or cache_ids != evidence['completed_cache_job_ids']:
        raise RuntimeError('resume execution/integrity incomplete; inspect preserved evidence')


if __name__ == '__main__':
    main()
