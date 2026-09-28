"""Isolated upstream comparison. Evaluation never changes OCR or table values."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import re
import time
import traceback
from pathlib import Path

SOURCE_BOXES = {'A3': [18, 57, 133, 75], 'D3': [315, 57, 381, 75],
                'E3': [381, 57, 485, 75], 'F3': [485, 57, 588, 75],
                'P21': [1408, 384, 1555, 402], 'P23': [1408, 420, 1555, 438]}


def valid_box(box):
    return (isinstance(box, (list, tuple)) and len(box) == 4
            and all(isinstance(v, (int, float)) and not isinstance(v, bool)
                    and math.isfinite(v) for v in box)
            and box[0] < box[2] and box[1] < box[3])


def iou(a, b):
    if not valid_box(a) or not valid_box(b):
        return 0.0
    area = max(0, min(a[2], b[2])-max(a[0], b[0])) * max(0, min(a[3], b[3])-max(a[1], b[1]))
    return area / ((a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - area)


def assess_geometry(tables, anchors, columns):
    """Require actual positive-area cells, not just a nominal matrix width.

    This fixture addresses table zero. A different table may not satisfy its
    anchors. Repeated boxes for genuinely merged cells are allowed.
    """
    invalid = []
    for ti, table in enumerate(tables):
        for ri, row in enumerate(table['cells']):
            for ci, cell in enumerate(row):
                if not valid_box(cell.get('bbox')):
                    invalid.append({'table': ti, 'row': ri+1, 'column': ci+1})
    checks = []
    rows = tables[0]['cells'] if tables else []
    for address, box in anchors.items():
        match = re.fullmatch(r'([A-Z]+)([1-9][0-9]*)', address)
        if not match or not valid_box(box):
            raise ValueError('invalid source annotation')
        col = 0
        for letter in match[1]:
            col = col*26 + ord(letter)-64
        row = int(match[2])-1
        actual = rows[row][col-1].get('bbox') if row < len(rows) and col <= len(rows[row]) else None
        score = iou(box, actual)
        checks.append({'cell': address, 'iou': round(score, 4), 'passed': score >= .75, 'actual_bbox': actual})
    shape_ok = bool(rows) and all(len(row) == columns for row in rows)
    return {'geometry_passed': bool(checks) and shape_ok and not invalid and all(c['passed'] for c in checks),
            'matrix_width_ok': shape_ok, 'invalid_cells': invalid, 'anchors': checks,
            'complete_table_verified': False}


def run_probe(output):
    # Optional dependencies stay out of the production install and unit tests.
    import av
    from PIL import Image as PILImage
    from img2table.document import Image
    from img2table.ocr import RapidOCR
    from rapidocr import LangRec
    from scripts.check_native_samples import sheet_cells

    class ObservedOCR(RapidOCR):
        """Record native OCR observations without changing the return value."""
        def of(self, document):
            result = super().of(document)
            self.records = result.records if result else {}
            return result

    output.mkdir(parents=True, exist_ok=True)
    video = Path('MP4/GameViewer_96iLJ4Cokv.mp4')
    with av.open(str(video)) as cap:
        for index, frame in enumerate(cap.decode(cap.streams.video[0])):
            if index == 60:
                full = frame.to_image().convert('RGB')
                break
        else:
            raise RuntimeError('source frame not found')
    full.save(output/'source.png')
    source_hash = hashlib.sha256(video.read_bytes()).hexdigest()
    fixture = json.loads(Path('tests/fixtures/native_acceptance.json').read_text(encoding='utf-8'))['memorymap']
    ocr = ObservedOCR(params={'Rec.lang_type': LangRec.CH,
          'EngineConfig.onnxruntime.intra_op_num_threads': 2,
          'EngineConfig.onnxruntime.inter_op_num_threads': 2})
    summary = []
    # Cropping and gamma/scale are input experiments only, NOT production rules.
    for name, scale, gamma, implicit in [('default', 1, 1, False), ('gamma2', 1, 2, False),
                                          ('scale2', 2, 1, False), ('implicit', 1, 1, True)]:
        folder = output/name
        folder.mkdir(exist_ok=True)
        started = time.monotonic()
        item = {'name': name, 'source_video_sha256': source_hash, 'frame': 60,
                'crop': [18, 0, 1660, 675], 'scale': scale, 'gamma': gamma,
                'implicit_columns': implicit, 'full_video_verified': False}
        try:
            image = full.crop((18, 0, 1660, 675))
            if gamma != 1:
                image = image.point([round(255*(v/255)**gamma) for v in range(256)]*3)
            if scale != 1:
                image = image.resize((image.width*scale, image.height*scale), PILImage.Resampling.LANCZOS)
            path = folder/'source.png'
            image.save(path)
            doc = Image(src=str(path), detect_rotation=False)
            options = dict(ocr=ocr, implicit_rows=False, implicit_columns=implicit,
                           borderless_tables=False, min_confidence=50)
            tables = doc.extract_tables(**options)
            structures = []
            for table in tables:
                rows = [[{'bbox': [c.bbox.x1/scale+18, c.bbox.y1/scale,
                                   c.bbox.x2/scale+18, c.bbox.y2/scale], 'value': c.value}
                         for c in row] for row in table.content.values()]
                structures.append({'cells': rows})
            (folder/'tables.json').write_text(json.dumps(structures, ensure_ascii=False, indent=2), encoding='utf-8')
            (folder/'raw_ocr.json').write_text(json.dumps(ocr.records, ensure_ascii=False, indent=2), encoding='utf-8')
            item['geometry'] = assess_geometry(structures, SOURCE_BOXES, fixture['required_columns'])
            item['shapes'] = [[len(t['cells']), max(map(len, t['cells']), default=0)] for t in structures]
            doc.to_xlsx(dest=str(folder/'native.xlsx'), **options)
            cells, item['dimension'] = sheet_cells(folder/'native.xlsx')
            item['mismatches'] = [{'cell': cell, 'expected': expected, 'actual': cells.get(cell, '')}
                                 for cell, expected in fixture['cells'].items()
                                 if re.sub(r'\s+', '', cells.get(cell, '')) != re.sub(r'\s+', '', expected)]
            item['matched_anchors'] = len(fixture['cells'])-len(item['mismatches'])
            item['acceptance_passed'] = item['geometry']['geometry_passed'] and not item['mismatches']
            item['status'] = 'ran'
        except Exception:
            item.update(status='failed', acceptance_passed=False, error=traceback.format_exc())
        item['seconds'] = round(time.monotonic()-started, 4)
        summary.append(item)
        (output/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
        print(json.dumps({k: v for k, v in item.items() if k != 'geometry'}, ensure_ascii=False), flush=True)
    if any(x['status'] != 'ran' for x in summary):
        raise RuntimeError('candidate execution failed; inspect summary.json')
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    run_probe(args.output)
