"""Thin output adapters for the existing Pandoc and PaddleX converters.

Unsupported semantic formatting becomes an explicit source-image fallback in
bundle assembly. Export checks do not infer source accuracy or repair geometry.
"""
from __future__ import annotations

import html
import importlib.metadata
import math
import shutil
import subprocess
from pathlib import Path

from .document_checks import check_docx, check_worksheet, declared_cells, literal_text
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
    """Accept only literal cells and explicit spans supported without guessing.

    In particular sup/sub/deletions and styled inline text are NOT flattened.
    The caller retains a source crop and records unsupported_table instead.
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
               'b', 'strong', 'i', 'em', 'span', 'p', 'br', 'u', 'code'}
    for el in table.iter():
        if not isinstance(el.tag, str) or el.tag not in allowed:
            raise ValueError('Semantic/unsupported table markup cannot be flattened: '+str(el.tag))
        if any(k.lower().startswith('on') or k.lower() in {'src', 'href', 'srcset'} for k in el.attrib):
            raise ValueError('Active or linked table content is not supported')
        # CSS can encode the same semantics as sup/sub/strike. Do not silently
        # discard it on literal text nodes, or semantic styles on table cells.
        style = el.get('style', '').lower()
        if style and (el.tag not in {'table', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th'}
                      or any(k in style for k in ('vertical-align', 'text-decoration', 'display', 'visibility'))):
            raise ValueError('Styled table text requires source-image review')
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
    result = {'rows': canonical, 'cells': cells,
              'caption': ''.join(_cell_text(c) for c in table.xpath('./caption')),
              'geometry_source': 'native_html_explicit_spans', 'geometry_verified': False}
    declared_cells(result)  # Validate explicit contracts; no geometry inference.
    return result


def _literal_html(text):
    # HTML/Pandoc may collapse ordinary repeated spaces. Encode them explicitly;
    # verification permits NBSP/space equivalence, never separator deletion.
    return html.escape(literal_text(text)).replace(' ', '&#160;').replace('\n', '<br>')


def table_html(table, name='Table'):
    cells = {c['id']: c for c in table['cells']}
    parts = [f'<table name="{html.escape(name, quote=True)}">']
    if table.get('caption'):
        parts.append('<caption>' + _literal_html(table['caption']) + '</caption>')
    parts.append('<tbody>')
    for row in table['rows']:
        parts.append('<tr>')
        for cid in row:
            c = cells[cid]
            parts.append(f'<td rowspan="{c["rowspan"]}" colspan="{c["colspan"]}" class="TYPE_STRING">'
                         + _literal_html(c['text']) + '</td>')
        parts.append('</tr>')
    parts.append('</tbody></table>')
    return ''.join(parts)


def render_html(document):
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
            if block['kind'] == 'table':
                parts.append(table_html(block['table'], block['id']))
            elif block['kind'] == 'image':
                parts.append(f'<p><img src="{html.escape(block["image"], quote=True)}" alt="Document image"></p>')
            else:
                tag = 'h2' if block.get('label') in {'doc_title', 'paragraph_title', 'title'} else 'p'
                parts.append(f'<{tag} id="{block["id"]}">' + _literal_html(block.get('text', '')) + f'</{tag}>')
        parts.append('</section>')
    parts.append('</body></html>')
    return ''.join(parts)


def export_bundle(root, document, *, word=True, xlsx=True, pandoc='pandoc', timeout=180):
    """Retain candidates on failure. A consistent export is still unaccepted."""
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or timeout <= 0:
        raise ValueError('Export timeout must be finite and positive')
    root = Path(root)
    checks, errors, table_index = {}, [], []
    markup = render_html(document)
    (root / 'document.html').write_text(markup, encoding='utf-8')
    (root / 'document.md').write_text(markup[markup.index('<body>')+6:markup.rindex('</body>')]+'\n', encoding='utf-8')
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
                errors.append({'stage': 'word', 'message': 'Frozen blocks, word separators, tables or image resources changed'})
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
            try:
                if len(wb.worksheets) != 1:
                    raise ValueError('Expected one native-converted sheet')
                ws = wb.worksheets[0]
                # Compare BEFORE any local formatting: candidate -> converter,
                # not merely converter -> saved file. Literal formula text stays data.
                conversion = check_worksheet(ws, table)
                for row in ws:
                    for cell in row:
                        if isinstance(cell, MergedCell):
                            continue
                        if cell.value is not None:
                            cell.data_type = 's'
                            cell.number_format = '@'
                            cell.alignment = Alignment(vertical='top', wrap_text=True)
                for col in ws.column_dimensions.values():
                    col.width = min(42, max(10, col.width or 10))
                path = folder / (filename + '.xlsx')
                wb.save(path)
            finally:
                wb.close()
            saved = load_workbook(path, data_only=False, keep_links=False)
            try:
                if len(saved.worksheets) != 1:
                    raise ValueError('Saved workbook sheet count changed')
                stored = check_worksheet(saved.worksheets[0], table)
            finally:
                saved.close()
            entry['xlsx'] = f'tables/{filename}.xlsx'
            same = conversion['status'] == stored['status'] == 'CONSISTENT'
            checks[block['id']] = {'status': 'CONSISTENT' if same else 'EXPORT_MISMATCH',
                'xlsx': entry['xlsx'], 'sha256': file_hash(path),
                'candidate_to_converter': conversion, 'candidate_to_saved': stored,
                'source_geometry_verified': False, 'source_accuracy_verified': False}
            if not same:
                errors.append({'stage': 'xlsx', 'block_id': block['id'],
                               'message': 'Candidate text/positions/explicit spans differ from converter or saved workbook'})
        except Exception as exc:
            errors.append({'stage': 'xlsx', 'block_id': block['id'], 'message': f'{type(exc).__name__}: {exc}'})
    write_json(root / 'table_index.json', table_index)
    result = {'schema': 2, 'status': 'EXPORT_ERROR' if errors else 'REVIEW_REQUIRED',
              'candidate_sha256': json_hash(document), 'checks': checks, 'errors': errors,
              'word_requested': word, 'xlsx_requested': xlsx, 'table_count': len(blocks),
              'inference_performed': False, 'accuracy_verified': False, 'layout_rendered': False}
    write_json(root / 'export_report.json', result)
    return result
