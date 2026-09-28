"""Isolated Docling candidate; never rewrite text, repair cells or change production."""
from __future__ import annotations
import argparse
import hashlib
import importlib.metadata
import json
import re
import time
import traceback
from pathlib import Path


def evaluate_table(data, fixture):
    """Check native logical slots, not only shape or words elsewhere in a table.

    Docling cell boxes can describe text rather than drawn cell boundaries, so
    full-cell IoU is diagnostic only, not an interchangeable geometry contract.
    Native row/column offsets and text must satisfy the unchanged source slots.
    """
    rows, cols = data.get('num_rows', 0), data.get('num_cols', 0)
    cells = data.get('table_cells', [])
    invalid = []
    for i, cell in enumerate(cells):
        offsets = [cell.get(k) for k in ('start_row_offset_idx', 'end_row_offset_idx',
                                        'start_col_offset_idx', 'end_col_offset_idx')]
        if (not all(isinstance(v, int) and not isinstance(v, bool) for v in offsets)
                or not (0 <= offsets[0] < offsets[1] <= rows)
                or not (0 <= offsets[2] < offsets[3] <= cols)):
            invalid.append(i)
    checks = []
    normalize = lambda text: re.sub(r'\s+', '', text)
    for address, expected in fixture['cells'].items():
        match = re.fullmatch(r'([A-Z]+)([1-9][0-9]*)', address)
        if not match:
            raise ValueError('invalid fixture address')
        col = 0
        for char in match[1]:
            col = 26 * col + ord(char) - 64
        row, col = int(match[2]) - 1, col - 1
        owners = [cell for i, cell in enumerate(cells) if i not in invalid
                  and cell['start_row_offset_idx'] <= row < cell['end_row_offset_idx']
                  and cell['start_col_offset_idx'] <= col < cell['end_col_offset_idx']]
        actual = owners[0].get('text', '') if len(owners) == 1 else None
        checks.append({'cell': address, 'expected': expected, 'actual': actual,
                       'owners': len(owners), 'passed': isinstance(actual, str)
                       and normalize(actual) == normalize(expected)})
    width_ok = cols == fixture['required_columns']
    return {'rows': rows, 'columns': cols, 'width_ok': width_ok,
            'invalid_native_cells': invalid, 'anchors': checks,
            'matched_anchors': sum(c['passed'] for c in checks),
            'acceptance_passed': bool(cells and checks) and width_ok and not invalid
                                 and all(c['passed'] for c in checks),
            'complete_table_verified': False}


def source_frame(path, index):
    import av
    with av.open(str(path)) as video:
        for i, frame in enumerate(video.decode(video.streams.video[0])):
            if i == index:
                return frame.to_image().convert('RGB'), float(frame.time)
    raise RuntimeError(f'missing source frame {index}')


def run(output):
    import torch
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import (PdfPipelineOptions, RapidOcrOptions,
        TableStructureOptions, TableFormerMode, AcceleratorOptions, AcceleratorDevice)
    from docling.document_converter import DocumentConverter, ImageFormatOption
    torch.set_num_threads(2)
    output.mkdir(parents=True, exist_ok=True)
    fixture = json.loads(Path('tests/fixtures/native_acceptance.json').read_text(encoding='utf-8'))
    options = PdfPipelineOptions()
    options.do_ocr = True
    options.do_table_structure = True
    options.ocr_options = RapidOcrOptions(force_full_page_ocr=True, lang=['chinese'],
        backend='onnxruntime', rapidocr_params={'EngineConfig.onnxruntime.intra_op_num_threads': 2,
                                               'EngineConfig.onnxruntime.inter_op_num_threads': 2})
    options.table_structure_options = TableStructureOptions(mode=TableFormerMode.ACCURATE)
    options.accelerator_options = AcceleratorOptions(num_threads=2, device=AcceleratorDevice.CPU)
    options.generate_page_images = True
    options.generate_picture_images = True
    options.document_timeout = 150
    converter = DocumentConverter(allowed_formats=[InputFormat.IMAGE],
        format_options={InputFormat.IMAGE: ImageFormatOption(pipeline_options=options)})
    versions = {}
    for name in ['docling', 'docling-slim', 'docling-core', 'docling-ibm-models', 'rapidocr', 'onnxruntime', 'torch']:
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            pass
    (output/'options.json').write_text(options.model_dump_json(indent=2), encoding='utf-8')
    (output/'versions.json').write_text(json.dumps(versions, indent=2), encoding='utf-8')
    summary = []
    cases = [('memorymap_full', 'memorymap', None),
             ('memorymap_viewport', 'memorymap', (18, 0, 1660, 675)),
             ('sarc_requirement', 'sarc_requirement', None),
             ('sarc_diagram', 'sarc_diagram', None)]
    for name, kind, roi in cases:
        target = output/name
        target.mkdir(exist_ok=True)
        source = Path('MP4')/fixture[kind]['video']
        image, timestamp = source_frame(source, fixture[kind]['frame'])
        image.save(target/'source_full.png')
        if roi:
            image = image.crop(roi)
        image.save(target/'input.png')
        item = {'sample': name, 'source_video': str(source),
                'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                'frame': fixture[kind]['frame'], 'timestamp': timestamp, 'roi': roi,
                'full_video_verified': False, 'acceptance_passed': False}
        started = time.monotonic()
        try:
            result = converter.convert(target/'input.png')
            doc = result.document
            (target/'native.json').write_text(doc.model_dump_json(indent=2), encoding='utf-8')
            (target/'native.html').write_text(doc.export_to_html(), encoding='utf-8')
            (target/'native.md').write_text(doc.export_to_markdown(), encoding='utf-8')
            item['conversion_status'] = str(result.status)
            item['tables'] = []
            for i, table in enumerate(doc.tables):
                raw = table.data.model_dump(mode='json')
                (target/f'table_{i}.json').write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding='utf-8')
                (target/f'table_{i}.html').write_text(table.export_to_html(doc=doc), encoding='utf-8')
                check = evaluate_table(raw, fixture['memorymap']) if kind == 'memorymap' else {'rows': raw['num_rows'], 'columns': raw['num_cols']}
                item['tables'].append(check)
            for i, picture in enumerate(doc.pictures):
                img = picture.get_image(doc)
                if img is not None:
                    img.save(target/f'picture_{i}.png')
            item['pictures'] = len(doc.pictures)
            if kind == 'memorymap':
                item['acceptance_passed'] = any(x['acceptance_passed'] for x in item['tables'])
            elif kind == 'sarc_requirement':
                text = re.sub(r'\s+', '', doc.export_to_markdown())
                item['text_anchor_passed'] = fixture[kind]['text'] in text
                item['acceptance_passed'] = item['text_anchor_passed']
            else:
                item['note'] = 'Image detection is not full cross-screen figure recovery.'
            item['status'] = 'ran'
        except Exception:
            item.update(status='failed', error=traceback.format_exc())
        item['seconds'] = round(time.monotonic()-started, 4)
        summary.append(item)
        (output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
        print('CASE', json.dumps(item, ensure_ascii=False), flush=True)
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    results = run(args.output)
    if any(x['status'] != 'ran' for x in results):
        raise SystemExit('Native candidate execution failed; see summary.json')
