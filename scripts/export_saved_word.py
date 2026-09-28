"""Output-only recovery; consumes one native cache or the report's existing jobs."""
import argparse
import json
from pathlib import Path
from mp4_analysis.thin.output import export_saved_word


def main():
    parser = argparse.ArgumentParser(description='只重导出已有原生结果，不运行OCR、不替换原文件')
    parser.add_argument('source', type=Path, help='单个 native/job 目录，或带 report.json 的运行目录')
    parser.add_argument('-o', '--output', required=True, type=Path, help='新的派生输出目录')
    args = parser.parse_args()
    report_path = args.source/'report.json'
    if not report_path.exists():
        print(json.dumps(export_saved_word(args.source, args.output), ensure_ascii=False))
        return
    if args.output.exists():
        parser.error('输出已存在，请使用新目录；不会覆盖先前结果')
    report = json.loads(report_path.read_text(encoding='utf-8'))
    if report.get('pending_parser_inputs') or report.get('status') != 'REVIEW_REQUIRED':
        parser.error('本批量入口只接受处理完毕、待核验的运行')
    items = []
    for item in report['items']:
        try:
            source = (args.source/item['directory']).resolve()
            if not source.is_relative_to(args.source.resolve()/'native'):
                raise ValueError('source job is outside native directory')
            if Path(item['id']).name != item['id']:
                raise ValueError('invalid job ID')
            result = export_saved_word(source, args.output/item['id'])
            items.append({'id': item['id'], 'result': result})
        except Exception as exc:
            items.append({'id': item['id'], 'error': f'{type(exc).__name__}: {exc}'})
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output/'export_summary.json').write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'{len(items)}/{len(report["items"])} {item["id"]}: {"ERROR" if "error" in items[-1] else "REVIEW_REQUIRED"}', flush=True)
    if any('error' in item for item in items):
        parser.exit(1, '部分重导出失败，见 export_summary.json；原生结果未改动\n')


if __name__ == '__main__':
    main()
