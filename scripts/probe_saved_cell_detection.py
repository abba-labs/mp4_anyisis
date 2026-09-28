"""Five detector-only controls on saved evidence; no OCR, table repair or tuning.

The tighter rectangle is a MANUAL diagnostic ROI, not production auto-cropping.
Compare the same native model/threshold before considering any pipeline change.
"""
import argparse
import importlib.metadata
import json
import time
from pathlib import Path

from PIL import Image
from mp4_analysis.thin.video import file_hash


def run(source, output):
    source, output = Path(source).resolve(), Path(output).resolve()
    if source == output or source in output.parents or output in source.parents:
        raise ValueError('source and output must be disjoint')
    if output.exists():
        raise FileExistsError(output)
    versions = {p: importlib.metadata.version(p) for p in ('paddleocr', 'paddlex', 'paddlepaddle')}
    if versions != {'paddleocr': '3.7.0', 'paddlex': '3.7.2', 'paddlepaddle': '3.2.2'}:
        raise ValueError('fixed-version experiment only')
    report = json.loads((source/'report.json').read_text(encoding='utf-8'))
    if report.get('parser_attempts') != 57 or report.get('pending_parser_inputs') != 0:
        raise ValueError('expected completed 57-input baseline')
    jobs = {j['id']: j for j in report['items']}
    g18 = jobs['group_000018_b']
    frame = next(f for f in g18['source_frames'] if f['frame_index'] == 675)
    paths = [source/g18['input_image'], source/'frames'/frame['image'],
             source/jobs['frame_00000452']['input_image']]
    cache = json.loads((source/g18['directory']/'adapter.json').read_text())
    cache452 = json.loads((source/jobs['frame_00000452']['directory']/'adapter.json').read_text())
    for path, digest in zip(paths, [cache['signature']['input_sha256'], frame['file_sha256'],
                                    cache452['signature']['input_sha256']]):
        if file_hash(path) != digest:
            raise ValueError('saved input hash mismatch')
    before = {str(p.relative_to(source)): file_hash(p)
              for p in (source/'native').rglob('*') if p.is_file()}
    cases = [('composite_native_bbox', paths[0], [117,396,1166,529]),
             ('source675_native_bbox', paths[1], [117,396,1166,529]),
             ('composite_manual_tight', paths[0], [117,396,1166,510]),
             ('source675_manual_tight', paths[1], [117,396,1166,510]),
             ('frame452_native_bbox', paths[2], [118,118,1166,227])]
    output.mkdir(parents=True)
    summary = {'versions': versions, 'planned': len(cases), 'cases': [], 'ocr_performed': False,
               'content_acceptance': 'NOT_EVALUATED', 'manual_rois_not_production': True,
               'baseline_files': len(before), 'pending': len(cases)}
    from paddleocr import TableClassification, TableCellsDetection
    from paddlex.inference.pipelines.table_recognition.pipeline_v2 import _TableRecognitionPipelineV2
    classifier = TableClassification(device='cpu', cpu_threads=2, enable_mkldnn=True)
    detectors = {}
    begun = time.monotonic()
    try:
        for name, path, box in cases:
            dest = output/name; dest.mkdir()
            image = dest/'input.png'
            with Image.open(path) as im:
                im.convert('RGB').crop(box).save(image)
            classified = next(iter(classifier.predict(str(image))))
            classified.save_to_json(str(dest/'classification.json'))
            label = classified['label_names'][0]
            if label not in {'wired_table', 'wireless_table'}:
                raise ValueError(f'unexpected table class: {label}')
            model = f'RT-DETR-L_{label}_cell_det'
            if model not in detectors:
                detectors[model] = TableCellsDetection(model_name=model, device='cpu',
                                                       cpu_threads=2, enable_mkldnn=True)
            result = next(iter(detectors[model].predict(str(image), threshold=0.3)))
            result.save_to_json(str(dest/'detection.json'))
            boxes = result['boxes']
            coords = [list(map(float, b['coordinate'])) for b in boxes]
            scores = [float(b['score']) for b in boxes]
            kept, kept_scores = ([], [])
            if coords:
                kept, kept_scores = _TableRecognitionPipelineV2.cells_det_results_nms(
                    None, coords, scores, cells_det_threshold=0.3)
            summary['cases'].append({'name': name, 'source_image': str(path.relative_to(source)),
                'source_sha256': file_hash(path), 'crop': box, 'crop_sha256': file_hash(image),
                'table_class': label, 'model': model, 'threshold': 0.3,
                'raw_count': len(coords), 'nms_count': len(kept),
                'native_nms_boxes': kept, 'native_nms_scores': kept_scores})
            summary['pending'] = len(cases)-len(summary['cases'])
            (output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))
            print(json.dumps(summary['cases'][-1]), flush=True)
    finally:
        after = {str(p.relative_to(source)): file_hash(p)
                 for p in (source/'native').rglob('*') if p.is_file()}
        summary['baseline_unchanged'] = before == after
        summary['elapsed_seconds'] = round(time.monotonic()-begun, 3)
        (output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    if before != after:
        raise RuntimeError('baseline changed')
    return summary


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('-o', '--output', type=Path, required=True)
    a = p.parse_args()
    run(a.source, a.output)
