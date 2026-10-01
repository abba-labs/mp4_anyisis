"""Read-only provenance audit, NOT an OCR accuracy score or a text repair.

PaddleX 3.7.2 standardized_data mutates overall_ocr_res. Empty text with a
retained nonzero score must not be described as an unmodified recognizer result.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
from mp4_analysis.thin.utils import file_hash


def inspect_payload(data):
    data = data.get('res', data)
    ocr = data.get('overall_ocr_res', {})
    texts, scores, boxes = (ocr.get(k, []) for k in ('rec_texts','rec_scores','rec_boxes'))
    if not (len(texts) == len(scores) == len(boxes)):
        raise ValueError('unaligned OCR text/score/box arrays')
    findings = []
    for index, (text, score, box) in enumerate(zip(texts, scores, boxes)):
        if not isinstance(text, str) or not math.isfinite(float(score)):
            raise ValueError('invalid OCR text or score')
        if text == '' and float(score) > 0:
            findings.append({'ocr_index': index, 'bbox': box, 'retained_score': float(score),
                'kind': 'empty_text_retained_score', 'stage': 'post_layout',
                'recognizer_failure_proven': False, 'missing_source_content_proven': False})
    return findings


def run(source):
    source = Path(source).resolve()
    report = json.loads((source/'report.json').read_text(encoding='utf-8'))
    results = []
    checked = 0
    for job in report['items']:
        native = (source/job['directory']).resolve()
        image = (source/job['input_image']).resolve()
        if not native.is_relative_to(source) or not image.is_relative_to(source):
            raise ValueError('nonlocal source path')
        adapter = json.loads((native/'adapter.json').read_text(encoding='utf-8'))
        if adapter.get('errors') or not adapter.get('files'):
            raise ValueError('unsuccessful native cache')
        if file_hash(image) != adapter['signature']['input_sha256']:
            raise ValueError('changed source image')
        for name, digest in adapter['files'].items():
            p = (native/name).resolve()
            if not p.is_relative_to(native) or file_hash(p) != digest:
                raise ValueError('changed or nonlocal native file')
            checked += 1
        name = adapter['native_json']
        if name not in adapter['files']:
            raise ValueError('unhashed native JSON')
        findings = inspect_payload(json.loads((native/name).read_text(encoding='utf-8')))
        results.append({'job_id': job['id'], 'input_image': job['input_image'],
            'input_sha256': adapter['signature']['input_sha256'],
            'native_json': job['directory']+'/'+name,
            'native_json_sha256': adapter['files'][name], 'findings': findings})
    return {'scope': 'post-layout evidence audit; not pre-layout OCR capture',
        'jobs_checked': len(results), 'hashed_native_exports_checked': checked,
        'jobs_with_observations': sum(bool(r['findings']) for r in results),
        'observations': sum(len(r['findings']) for r in results), 'items': results,
        'new_inference': False, 'content_acceptance': 'NOT_EVALUATED',
        'limitations': ['Observations include possible legitimate supersession, not a lost-line count.',
            'Use a same-input GeneralOCR capture before layout to distinguish recognition from mutation.']}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('-o','--output',type=Path,required=True)
    a = p.parse_args()
    if a.output.resolve() == a.source.resolve() or a.source.resolve() in a.output.resolve().parents:
        p.error('write the audit outside the immutable source cache')
    result = run(a.source)
    with a.output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
