"""Output-only adapters: safe HTML, existing Pandoc and PaddleX table export.

No OCR, inferred table geometry, OOXML splicing or network requests. Export
checks compare actual files with the frozen candidate, NOT with source truth.
"""
from __future__ import annotations

import hashlib
import html
import importlib.metadata
import math
import shutil
import subprocess
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from .utils import file_hash, json_hash, write_json


def local_file(root, relative, digest=None):
    """Resolve only a regular, non-symlink file below a trusted directory."""
    root = Path(root).resolve()
    if not isinstance(relative, str) or not relative:
        raise ValueError('Resource name must be a nonempty string')
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts or '\\' in relative or ':' in relative:
        raise ValueError(f'Unsafe resource name: {relative!r}')
    path = root
    for part in rel.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f'Symlink resource: {relative}')
    if not path.is_file() or not path.resolve().is_relative_to(root):
        raise ValueError(f'Missing local resource: {relative}')
    if digest is not None and file_hash(path) != digest:
        raise ValueError(f'Resource changed: {relative}')
    return path


def checked_bbox(box, size):
    if not isinstance(box, (list, tuple)) or len(box) != 4:
        raise ValueError('Expected a four-coordinate crop-pixel box')
    if any(isinstance(x, bool) or not isinstance(x, (float, int)) or not math.isfinite(x) for x in box):
        raise ValueError('Box coordinates must be finite numbers')
    l, t, r, b = box
    if not (0 <= l < r <= size[0] and 0 <= t < b <= size[1]):
        raise ValueError('Box is empty or outside the approved document crop')
    return [math.floor(l), math.floor(t), math.ceil(r), math.ceil(b)]


def _cell_text(element):
    """Preserve explicit line boundaries while reading literal inline text."""
    pieces = [element.text or '']
    for child in element:
        if child.tag == 'br':
            pieces.append('\n')
        else:
            if child.tag == 'p' and pieces and not pieces[-1].endswith('\n'):
                pieces.append('\n')
            pieces.append(_cell_text(child))
            if child.tag == 'p':
                pieces.append('\n')
        pieces.append(child.tail or '')
    return ''.join(pieces)


def table_model(markup, block_id):
    """Read upstream HTML physical cells without solving a table grid.

    Canonical rows preserve order and explicit spans. Cells become td for the
    pinned upstream exporter, which otherwise reorders mixed th/td. Raw HTML
    stays in the native cache. No remote/active markup or formulas are accepted.
    """
    from lxml import html as LH
    if not isinstance(markup, str) or len(markup) > 4_000_000:
        raise ValueError('Invalid or oversized table HTML')
    node = LH.fromstring(markup, parser=LH.HTMLParser(no_network=True))
    tables = ([node] if node.tag == 'table' else []) + node.xpath('.//table')
    if len(tables) != 1:
        raise ValueError('Expected exactly one non-nested native table')
    table = tables[0]
    allowed = {'table', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th', 'caption',
               'b', 'strong', 'i', 'em', 'span', 'p', 'br', 'sup', 'sub', 'u', 's', 'code'}
    for el in table.iter():
        if not isinstance(el.tag, str) or el.tag not in allowed:
            raise ValueError('Unsupported table markup; retain source crop for review')
        if any(k.lower().startswith('on') or k.lower() in {'src', 'href', 'srcset'} for k in el.attrib):
            raise ValueError('Active or linked table content is not supported')
    rows = table.xpath('./thead/tr | ./tbody/tr | ./tfoot/tr | ./tr')
    if not rows or len(rows) > 10000:
        raise ValueError('Empty or oversized table')
    canonical, cells = [], []
    for row in rows:
        entries = []
        for el in row:
            if not isinstance(el.tag, str) or el.tag not in {'td', 'th'}:
                raise ValueError('Unsupported non-cell child in table row')
            spans = {}
            for key in ('rowspan', 'colspan'):
                value = el.get(key, '1')
                if not value.isdigit() or not 1 <= int(value) <= 1000:
                    raise ValueError('Unsupported cell span')
                spans[key] = int(value)
            text = _cell_text(el)
            cell = {'id': f'{block_id}.c{len(cells)+1:04d}', 'text': text,
                    'before_hash': json_hash(text), **spans}
            cells.append(cell)
            entries.append(cell['id'])
        canonical.append(entries)
    if not cells or len(cells) > 100000:
        raise ValueError('Empty or oversized cell list')
    caption = ''.join(_cell_text(c) for c in table.xpath('./caption'))
    return {'rows': canonical, 'cells': cells, 'caption': caption,
            'geometry_source': 'native_html_explicit_spans', 'geometry_verified': False}


def table_html(table, name='Table'):
    cells = {c['id']: c for c in table['cells']}
    parts = [f'<table name="{html.escape(name, quote=True)}">']
    if table.get('caption'):
        parts.append('<caption>' + html.escape(table['caption']) + '</caption>')
    parts.append('<tbody>')
    for row in table['rows']:
        parts.append('<tr>')
        for cid in row:
            c = cells[cid]
            parts.append(f'<td rowspan="{c["rowspan"]}" colspan="{c["colspan"]}" class="TYPE_STRING">'
                         + html.escape(c['text']).replace('\n', '<br>') + '</td>')
        parts.append('</tr>')
    parts.append('</tbody></table>')
    return ''.join(parts)


def render_html(document):
    """Build a literal, local-only HTML candidate; no text-similarity deletion."""
    parts = ['<!doctype html><html><head><meta charset="utf-8"><title>Document candidate</title>',
             '<style>body{max-width:1100px;margin:24px auto;font-family:sans-serif;line-height:1.5}'
             'table{border-collapse:collapse;width:100%}td{border:1px solid #999;padding:5px;white-space:normal}'
             'img{max-width:100%;height:auto}section{margin-bottom:2em}p{white-space:pre-wrap}</style>',
             '</head><body>']
    for unit in document['units']:
        parts.append(f'<section id="{unit["id"]}">')
        for block in unit['blocks']:
            if block.get('excluded'):
                continue
            kind = block['kind']
            if kind == 'table':
                parts.append(table_html(block['table'], block['id']))
            elif kind == 'image':
                parts.append(f'<p><img src="{block["image"]}" alt="Document image"></p>')
            else:
                tag = 'h2' if block.get('label') in {'doc_title', 'paragraph_title', 'title'} else 'p'
                parts.append(f'<{tag} id="{block["id"]}">' + html.escape(block.get('text', '')).replace('\n', '<br>') + f'</{tag}>')
        parts.append('</section>')
    parts.append('</body></html>')
    return ''.join(parts)


def _compact(text):
    return ''.join(text.split())


def _expected(document):
    body, tables = [], []
    for unit in document['units']:
        for block in unit['blocks']:
            if block.get('excluded'):
                continue
            if block['kind'] == 'table':
                table = block['table']
                if table.get('caption'):
                    body.append(table['caption'])
                values = {c['id']: c['text'] for c in table['cells']}
                ordered = [values[cid] for row in table['rows'] for cid in row]
                body.extend(ordered)
                tables.append([_compact(v) for v in ordered])
            elif block['kind'] != 'image':
                body.append(block.get('text', ''))
    return _compact(''.join(body)), tables


def check_docx(path, document):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read('word/document.xml'))
    body = root.find('w:body', ns)
    if body is None:
        raise ValueError('DOCX has no document body')
    observed = _compact(''.join(x.text or '' for x in body.findall('.//w:t', ns)))
    actual_tables = []
    for tbl in body.findall('.//w:tbl', ns):
        values = []
        for row in tbl.findall('./w:tr', ns):
            for cell in row.findall('./w:tc', ns):
                merge = cell.find('./w:tcPr/w:vMerge', ns)
                if merge is not None and merge.get('{'+ns['w']+'}val') != 'restart':
                    continue
                values.append(_compact(''.join(t.text or '' for t in cell.findall('.//w:t', ns))))
        actual_tables.append(values)
    expected, tables = _expected(document)
    same = observed == expected and actual_tables == tables
    return {'status': 'CONSISTENT' if same else 'EXPORT_MISMATCH',
            'body_equal_ignoring_whitespace': observed == expected,
            'physical_cell_text_equal': actual_tables == tables,
            'expected_text_sha256': hashlib.sha256(expected.encode()).hexdigest(),
            'actual_text_sha256': hashlib.sha256(observed.encode()).hexdigest(),
            'file_sha256': file_hash(path), 'source_accuracy_verified': False,
            'layout_rendered': False, 'merge_geometry_verified': False}


def export_bundle(root, document, *, word=True, xlsx=True, pandoc='pandoc', timeout=180):
    """Retain HTML/content when optional exporters fail; never mark PASS."""
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or timeout <= 0:
        raise ValueError('Export timeout must be finite and positive')
    root = Path(root)
    checks, errors, table_index = {}, [], []
    markup = render_html(document)
    (root / 'document.html').write_text(markup, encoding='utf-8')
    # Markdown's raw HTML blocks retain table spans and literal identifiers.
    # HTML is authoritative for DOCX; Markdown is not reparsed during export.
    body_markup = markup[markup.index('<body>')+6:markup.rindex('</body>')]
    (root / 'document.md').write_text(body_markup + '\n', encoding='utf-8')
    if word:
        try:
            executable = shutil.which(pandoc)
            if executable is None:
                raise RuntimeError('Pandoc executable is required for document.docx')
            version = subprocess.run([executable, '--version'], capture_output=True, check=True,
                                     text=True, timeout=timeout).stdout.splitlines()[0]
            if version != 'pandoc 3.1.11.1':
                raise RuntimeError(f'Expected existing Pandoc 3.1.11.1, found {version}')
            result = subprocess.run([executable, '--from=html', '--to=docx', 'document.html',
                                     '--resource-path=.', '-o', 'document.docx'], cwd=root,
                                    capture_output=True, text=True, check=True, timeout=timeout)
            checks['docx'] = check_docx(root / 'document.docx', document)
            checks['docx']['converter'] = version
            if result.stderr.strip():
                errors.append({'stage': 'word', 'message': result.stderr.strip()})
            if checks['docx']['status'] != 'CONSISTENT':
                errors.append({'stage': 'word', 'message': 'Export changed frozen candidate text/cells'})
        except Exception as exc:
            errors.append({'stage': 'word', 'message': f'{type(exc).__name__}: {exc}'})
    blocks = [b for u in document['units'] for b in u['blocks'] if b['kind'] == 'table' and not b.get('excluded')]
    for index, block in enumerate(blocks, 1):
        folder = root / 'tables'
        folder.mkdir(exist_ok=True)
        filename = f'table_{index:04d}'
        table = block['table']
        table_markup = '<html><body>' + table_html(table, f'T{index:04d}') + '</body></html>'
        (folder / (filename + '.html')).write_text(table_markup, encoding='utf-8')
        entry = {'block_id': block['id'], 'html': f'tables/{filename}.html',
                 'evidence_id': block.get('evidence_id'), 'bbox': block.get('bbox'),
                 'table_model_sha256': json_hash(table), 'xlsx': None}
        table_index.append(entry)
        if not xlsx:
            continue
        try:
            if importlib.metadata.version('paddlex') != '3.7.2':
                raise RuntimeError('Existing table exporter requires PaddleX 3.7.2')
            from paddlex.inference.utils.io.tablepyxl import document_to_workbook
            from openpyxl import load_workbook
            from openpyxl.cell.cell import MergedCell
            from openpyxl.styles import Alignment
            wb = document_to_workbook(table_markup)
            if len(wb.worksheets) != 1:
                raise ValueError('Expected one native-converted sheet')
            ws = wb.worksheets[0]
            for row in ws:
                for cell in row:
                    if isinstance(cell, MergedCell):
                        continue
                    if cell.value is not None:
                        cell.data_type = 's'  # Literal screenshot text, never Excel formulas.
                        cell.number_format = '@'
                        cell.alignment = Alignment(vertical='top', wrap_text=True)
            for col in ws.column_dimensions.values():
                col.width = min(42, max(10, col.width or 10))
            path = folder / (filename + '.xlsx')
            # OOXML may serialize an empty string as an empty cell. Treat only
            # this storage distinction as equivalent; other characters stay exact.
            expected_cells = [(c.coordinate, c.value, c.data_type) for row in ws for c in row
                              if not isinstance(c, MergedCell) and c.value not in (None, '')]
            expected_merges = sorted(str(r) for r in ws.merged_cells.ranges)
            model_values = [_compact(c['text']) for c in table['cells'] if _compact(c['text'])]
            converted_values = [_compact(str(v)) for _, v, _ in expected_cells if _compact(str(v))]
            wb.save(path)
            wb.close()
            saved = load_workbook(path, data_only=False, keep_links=False)
            try:
                observed_ws = saved.worksheets[0]
                observed_cells = [(c.coordinate, c.value, c.data_type) for row in observed_ws for c in row
                                  if not isinstance(c, MergedCell) and c.value not in (None, '')]
                observed_merges = sorted(str(r) for r in observed_ws.merged_cells.ranges)
                same = (expected_cells == observed_cells and expected_merges == observed_merges
                        and model_values == converted_values)
            finally:
                saved.close()
            entry['xlsx'] = f'tables/{filename}.xlsx'
            checks[block['id']] = {'status': 'CONSISTENT' if same else 'EXPORT_MISMATCH',
                'xlsx': entry['xlsx'], 'sha256': file_hash(path),
                'saved_cells_and_merges_equal': expected_cells == observed_cells and expected_merges == observed_merges,
                'html_nonempty_cell_text_equal': model_values == converted_values,
                'source_geometry_verified': False, 'source_accuracy_verified': False}
            if not same:
                errors.append({'stage': 'xlsx', 'block_id': block['id'], 'message': 'Table conversion changed cell text or saved geometry'})
        except Exception as exc:
            errors.append({'stage': 'xlsx', 'block_id': block['id'], 'message': f'{type(exc).__name__}: {exc}'})
    write_json(root / 'table_index.json', table_index)
    result = {'schema': 1, 'status': 'EXPORT_ERROR' if errors else 'REVIEW_REQUIRED',
              'candidate_sha256': json_hash(document), 'checks': checks, 'errors': errors,
              'word_requested': word, 'xlsx_requested': xlsx, 'table_count': len(blocks),
              'inference_performed': False, 'accuracy_verified': False, 'layout_rendered': False}
    write_json(root / 'export_report.json', result)
    return result
