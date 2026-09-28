"""Small source index, integrity checks and links to UNMODIFIED native outputs."""
from __future__ import annotations

import html
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


def inspect_workbook(path):
    """Read OOXML only; do not evaluate formulas or convert model confidence to accuracy."""
    ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(path) as archive:
        sheets = []
        for name in archive.namelist():
            if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
                root = ET.fromstring(archive.read(name))
                sheets.append({'part': name, 'rows':len(root.findall('.//s:row', ns)),
                               'cells':len(root.findall('.//s:c', ns)),
                               'formulas':len(root.findall('.//s:f', ns)),
                               'merges':len(root.findall('.//s:mergeCell', ns))})
    return {'sheets':sheets, 'formula_review_required':any(s['formulas'] for s in sheets)}


def write_index(output, manifest, items, *, stitch=None, reconstruction=None):
    output = Path(output)
    errors = [item for item in items if item.get('error') or item.get('native', {}).get('errors')]
    expected = reconstruction['parser_inputs'] if reconstruction else len(manifest.get('frames', items))
    pending = max(0, expected-len(items))
    report = {'status':'NO_CONTENT' if not items else 'PARTIAL_FAILURE' if errors or pending else 'REVIEW_REQUIRED',
              'source':manifest, 'parser_attempts':len(items),
              'expected_parser_inputs':expected, 'pending_parser_inputs':pending,
              'cache_hits':sum(item.get('native', {}).get('cache_hit', False) for item in items),
              'items':items, 'stitch_preview':stitch, 'reconstruction':reconstruction,
              'accuracy_verified':False, 'content_completeness_verified':False,
              'limitations':['Frames are observations, not original document pages.',
                 'No semantic rewriting or text-similarity deletion.',
                 'SCANS composites, when requested, remain unverified; no cross-batch content deduplication.',
                 'Sampled or capped runs cannot establish coverage.',
                 'Native model outputs, including table row/column assignments, require review.']}
    (output/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    lines = ['# 录屏资料提取索引（待核验）', '',
             '原生结果按画面保存；帧数不是原文页数。实验拼接只生成待核验候选，不代表图表完整恢复。', '']
    cards = []
    for item in items:
        frame = item['frame']
        title = f"画面 {frame['frame_index']} · {frame['start_time']:.3f} 秒"
        lines += [f'## {title}', '']
        links=[]
        for name in item.get('native', {}).get('files', {}):
            if Path(name).suffix.lower() in {'.md','.html','.xlsx','.docx','.json'}:
                relative = f"{item['directory']}/{name}"
                lines.append(f'- [{name}](<{relative}>)')
                links.append(f'<a href="{html.escape(relative,quote=True)}">{html.escape(name)}</a>')
        source_links = []
        for source in item.get('source_frames', [frame]):
            source_links.append(f'<a href="frames/{html.escape(source["image"],quote=True)}">{source["frame_index"]}</a>')
        preview = item.get('input_image', f'frames/{frame["image"]}')
        if item.get('kind') == 'unverified_composite':
            links.append('实验拼接：几何及文字完整性未核验')
        issue = item.get('error') or item.get('native', {}).get('errors')
        if issue:
            lines.append(f'错误：{issue}')
        cards.append(f'<section><h2>{html.escape(title)}</h2><p>{" · ".join(links)}</p>'
                     f'<p>{html.escape(str(issue or "待对照原画面核验"))}</p>'
                     f'<p>源帧：{" · ".join(source_links)}</p>'
                     f'<img loading="lazy" src="{html.escape(preview,quote=True)}" alt="解析输入（源帧或未核验拼接）"></section>')
    (output/'index.md').write_text('\n'.join(lines),encoding='utf-8')
    (output/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8">'
        '<title>录屏资料提取 · 待核验</title><style>body{max-width:1100px;margin:24px auto;font:16px sans-serif;line-height:1.6}img{max-width:100%}section{border-top:1px solid #ccc;padding:12px}</style>'
        '<h1>录屏资料提取 · 待核验</h1><p>保留原画面及引擎原生结果；本索引不代表完整性或准确率验收。</p>'
        +''.join(cards)+'</html>',encoding='utf-8')
    return report
