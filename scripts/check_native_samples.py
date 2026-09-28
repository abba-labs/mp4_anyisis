"""Small source-anchored acceptance check, separate from execution success.

Usage: python scripts/check_native_samples.py /path/to/validation/thin
No OCR or model calls. No modification/evaluation of Office files.
"""
from pathlib import Path
import json
import re
import sys
import zipfile
from xml.etree import ElementTree as ET


def sheet_cells(path):
    ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(path) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            strings = [''.join(n.itertext()) for n in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si', ns)]
        sheet = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        values = {}
        for cell in sheet.findall('.//s:sheetData/s:row/s:c', ns):
            if cell.find('s:f', ns) is not None:
                values[cell.attrib['r']] = '[FORMULA_REQUIRES_REVIEW]'
                continue
            inline, value = cell.find('s:is', ns), cell.find('s:v', ns)
            text = ''.join(inline.itertext()) if inline is not None else (value.text or '' if value is not None else '')
            if cell.attrib.get('t') == 's':
                text = strings[int(text)]
            values[cell.attrib['r']] = text
        dim = sheet.find('s:dimension', ns)
        return values, dim.attrib.get('ref') if dim is not None else None


def check(root):
    fixture = json.loads((Path(__file__).resolve().parents[1]/'tests/fixtures/native_acceptance.json').read_text(encoding='utf-8'))
    checks = []
    for name in ['sarc_requirement', 'sarc_diagram']:
        files = list((root/name).rglob('*_res.json'))
        item = {'sample': name, 'passed': False}
        if files:
            data = json.loads(files[0].read_text(encoding='utf-8')); data = data.get('res', data)
            blocks = data.get('parsing_res_list', [])
            if 'text' in fixture[name]:
                text = ''.join(str(b.get('block_content', '')) for b in blocks)
                item['passed'] = fixture[name]['text'] in re.sub(r'\s+', '', text)
            else:
                item['passed'] = any(b.get('block_label') == fixture[name]['label'] for b in blocks)
                item['full_figure_verified'] = False
        else:
            item['reason'] = 'native result missing'
        checks.append(item)
    books = list((root/'memorymap').rglob('*.xlsx'))
    item = {'sample': 'memorymap', 'passed': False, 'mismatches': []}
    if books:
        cells, dimension = sheet_cells(books[0]); item['dimension'] = dimension
        end_column = re.sub('[^A-Z]', '', (dimension or '').split(':')[-1])
        columns = 0
        for letter in end_column:
            columns = columns * 26 + ord(letter) - ord('A') + 1
        if columns < fixture['memorymap']['required_columns']:
            item['mismatches'].append({'reason': 'missing columns', 'expected_minimum': 17, 'actual': columns})
        for address, expected in fixture['memorymap']['cells'].items():
            actual = cells.get(address, '')
            if re.sub(r'\s+', '', actual) != re.sub(r'\s+', '', expected):
                item['mismatches'].append({'cell': address, 'expected': expected, 'actual': actual})
        item['passed'] = not item['mismatches']
    else:
        item['reason'] = 'xlsx missing'
    checks.append(item)
    return {'execution_success_is_not_acceptance': True, 'full_video_verified': False,
            'anchor_checks_passed': all(c['passed'] for c in checks), 'checks': checks}


if __name__ == '__main__':
    root = Path(sys.argv[1]); result = check(root)
    (root/'anchor_acceptance.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['anchor_checks_passed'] else 1)
