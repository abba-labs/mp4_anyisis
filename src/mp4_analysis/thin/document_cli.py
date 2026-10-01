"""Saved OCR -> document bundle -> reviewed bundle, without inference."""
from __future__ import annotations

import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='已确认裁图的OCR结果 -> 整份文档 -> 有来源的修订稿；不运行OCR或模型')
    actions = parser.add_subparsers(dest='action', required=True)
    build = actions.add_parser('build', help='从截图run_directory组织文档、表格和图片')
    build.add_argument('run_directory')
    apply = actions.add_parser('apply', help='校验外部视觉复核差异，产生独立新版本')
    apply.add_argument('bundle_directory')
    apply.add_argument('response_file')
    apply.add_argument('--accept-changes', required=True, metavar='RESPONSE_SHA256',
                       help='明确批准已查看的复核JSON文件SHA256；不是内容验收声明')
    inspect = actions.add_parser('inspect-review', help='只读取复核文件，显示修改数量及批准所需hash')
    inspect.add_argument('response_file')
    for command in (build, apply):
        command.add_argument('-o', '--output', required=True, help='新的独立文档目录；不能覆盖已有版本')
        command.add_argument('--no-docx', action='store_true', help='只输出HTML/Markdown等，不调用Pandoc')
        command.add_argument('--no-xlsx', action='store_true', help='保留HTML表格，不调用上游Excel导出')
        command.add_argument('--pandoc', default='pandoc', help='已有Pandoc 3.1.11.1可执行文件')
        command.add_argument('--export-timeout', type=int, default=180, help='单次外部导出限时，秒')
    args = parser.parse_args()
    try:
        if args.action == 'inspect-review':
            from .document_review import response_summary
            result = response_summary(args.response_file)
        else:
            if args.export_timeout <= 0:
                parser.error('--export-timeout必须为正整数')
            options = dict(word=not args.no_docx, xlsx=not args.no_xlsx,
                           pandoc=args.pandoc, timeout=args.export_timeout)
            if args.action == 'build':
                from .document_bundle import build_document
                result = build_document(args.run_directory, args.output, **options)
            else:
                from .document_review import apply_review
                result = apply_review(args.bundle_directory, args.response_file, args.output,
                                      accept_changes=args.accept_changes, **options)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if result.get('status') == 'EXPORT_ERROR':
            parser.exit(2, '候选与失败记录已保存；部分导出失败，不能标为已交付通过。\n')
    except KeyboardInterrupt:
        parser.exit(130, '已中断；原始结果不修改，新目录中的记录保留。\n')
    except Exception as exc:
        parser.exit(1, f'失败：{exc}\n')


if __name__ == '__main__':
    main()
