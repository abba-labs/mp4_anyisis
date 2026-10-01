"""Build a source-linked acceptance ledger; never infer accuracy from execution."""
import argparse
import html
import json
import os
from pathlib import Path
from mp4_analysis.thin.utils import file_hash

GATES = ('coverage', 'text', 'tables', 'images', 'office')
STATES = {'PASS', 'FAIL', 'NOT_REVIEWED', 'NOT_APPLICABLE'}


def unit_state(unit):
    gates = unit['gates']
    if set(gates) != set(GATES) or any(v not in STATES for v in gates.values()):
        raise ValueError('invalid review gates')
    if 'FAIL' in gates.values():
        return 'FAIL'
    if 'NOT_REVIEWED' in gates.values():
        return 'NOT_REVIEWED'
    if gates['coverage'] != 'PASS' or gates['office'] != 'PASS' or not unit.get('acceptance_evidence'):
        raise ValueError('accepted unit requires coverage, Office review and explicit evidence')
    return 'PASS'


def build(source, ledger, output):
    source, ledger, output = Path(source).resolve(), Path(ledger).resolve(), Path(output).resolve()
    if source == output or source in output.parents or output in source.parents:
        raise ValueError('source and review output must be disjoint')
    if output.exists():
        raise FileExistsError(output)
    spec = json.loads(ledger.read_text(encoding='utf-8'))
    report = json.loads((source/'report.json').read_text(encoding='utf-8'))
    manifest = json.loads((source/'video.json').read_text(encoding='utf-8'))
    if manifest['source_sha256'] != spec['source_sha256']:
        raise ValueError('review ledger belongs to another video')
    frames = {f['frame_index']: f for f in manifest['frames']}
    units = spec['units']
    if not units or len({u['id'] for u in units}) != len(units):
        raise ValueError('review unit IDs must be nonempty and unique')
    def local(name):
        path = (source/name).resolve()
        if not path.is_relative_to(source) or not path.is_file():
            raise ValueError(f'missing or nonlocal evidence: {name}')
        return path
    rows = []
    for unit in units:
        state = unit_state(unit)
        anchors = []
        for index in unit['source_frames']:
            frame = frames[index]
            relative = 'frames/'+frame['image']
            if file_hash(local(relative)) != frame['file_sha256']:
                raise ValueError('source frame changed')
            anchors.append({'frame_index': index, 'pts': frame['start_time'],
                            'file': relative, 'sha256': frame['file_sha256']})
        if not anchors:
            raise ValueError('each unit requires independent source evidence')
        outputs = []
        for item in report['items']:
            if not set(unit['source_frames']).intersection(f['frame_index'] for f in item.get('source_frames', [item['frame']])):
                continue
            for name, digest in item.get('native', {}).get('files', {}).items():
                relative = item['directory']+'/'+name
                if file_hash(local(relative)) != digest:
                    raise ValueError('native output changed')
                if Path(name).suffix in {'.md', '.docx', '.xlsx'}:
                    outputs.append({'job_id': item['id'], 'file': relative, 'sha256': digest})
        rows.append(dict(unit, status=state, source_evidence=anchors, candidate_outputs=outputs))
    states = [r['status'] for r in rows]
    result = {'scope': spec['scope'], 'ledger_sha256': file_hash(ledger),
              'units': rows, 'accepted': states.count('PASS'), 'failed': states.count('FAIL'),
              'not_reviewed': states.count('NOT_REVIEWED'), 'total_units': len(rows),
              'project_completion_percent': None, 'full_video_coverage_verified': False,
              'execution': {'processed': report['parser_attempts'], 'pending': report['pending_parser_inputs']},
              'note': 'Anchor frames route review work; they do not prove exhaustive source coverage. No automatic acceptance.'}
    output.mkdir(parents=True)
    (output/'review.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    def link(relative, title):
        url = os.path.relpath(source/relative, output).replace(os.sep, '/')
        return '<a href="'+html.escape(url, quote=True)+'">'+html.escape(title)+'</a>'
    body = ['<!doctype html><meta charset="utf-8"><html lang="zh-CN"><title>源内容验收台账</title>',
            '<style>body{max-width:1100px;margin:24px auto;font:16px sans-serif;line-height:1.6}section{border-top:1px solid;padding:14px 0}a{margin-right:12px}code{overflow-wrap:anywhere}</style>',
            '<h1>源内容验收台账（不是项目完成百分比）</h1>',
            f'<p>{len(rows)}个一级资料单元；完整通过{result["accepted"]}，已知失败{result["failed"]}，未完成核对{result["not_reviewed"]}。</p>',
            '<p>源目录与前置资料形成的第一版清单。锚点仅供定位，短暂页面、逐字/逐格与全视频覆盖仍需核验；文件存在不自动变绿。链接依赖已保存工件。</p>']
    for row in rows:
        body += ['<section><h2>'+html.escape(row['id']+' '+row['title']+' — '+row['status'])+'</h2>',
                 '<p>'+html.escape(row['reason'])+'</p>',
                 '<p>'+html.escape(json.dumps(row['gates'], ensure_ascii=False))+'</p>',
                 '<p>源画面：'+''.join(link(a['file'],str(a['frame_index'])) for a in row['source_evidence'])+'</p>',
                 '<details><summary>对应原生产物（待核对，未修改）</summary>'+''.join(link(a['file'],a['job_id']+Path(a['file']).suffix) for a in row['candidate_outputs'])+'</details></section>']
    (output/'index.html').write_text(''.join(body)+'</html>', encoding='utf-8')
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('--ledger', type=Path, default=Path('tests/fixtures/sarc_review_units_v1.json'))
    p.add_argument('-o', '--output', type=Path, required=True)
    a = p.parse_args()
    build(a.source, a.ledger, a.output)
