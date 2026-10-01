"""Saved OCR -> document -> reviewed document; separate export-only retries."""
from __future__ import annotations

import argparse
import json
import signal


def main():
    parser = argparse.ArgumentParser(description='截图文档组织、修订、重导出；不运行OCR或模型')
    actions = parser.add_subparsers(dest='action', required=True)
    build = actions.add_parser('build', help='从截图run_directory组织文档')
    build.add_argument('run_directory')
    apply = actions.add_parser('apply', help='校验视觉意见，产生独立修订版本')
    apply.add_argument('bundle_directory')
    apply.add_argument('response_file')
    apply.add_argument('--accept-changes', required=True, metavar='RESPONSE_SHA256')
    reexport = actions.add_parser('reexport', help='从冻结初稿或修订稿重试导出，不重复OCR/模型')
    reexport.add_argument('bundle_directory')
    inspect = actions.add_parser('inspect-review', help='只显示复核意见的数量及批准hash')
    inspect.add_argument('response_file')
    for command in (build, apply, reexport):
        command.add_argument('-o','--output',required=True,help='新的独立目录，不能覆盖已有版本')
        command.add_argument('--no-docx',action='store_true',help='不调用Pandoc')
        command.add_argument('--no-xlsx',action='store_true',help='只保留HTML表格')
        command.add_argument('--pandoc',default='pandoc',help='已有Pandoc 3.1.11.1')
        command.add_argument('--export-timeout',type=int,default=180)
    args = parser.parse_args()
    if hasattr(signal,'SIGTERM'):
        def terminate(*_):
            raise KeyboardInterrupt
        signal.signal(signal.SIGTERM,terminate)
    try:
        if args.action == 'inspect-review':
            from .document_review import response_summary
            result = response_summary(args.response_file)
        else:
            if args.export_timeout <= 0:
                parser.error('--export-timeout必须为正整数')
            options = dict(word=not args.no_docx,xlsx=not args.no_xlsx,
                           pandoc=args.pandoc,timeout=args.export_timeout)
            if args.action == 'build':
                from .document_bundle import build_document
                result = build_document(args.run_directory,args.output,**options)
            elif args.action == 'reexport':
                from .document_reexport import reexport_bundle
                result = reexport_bundle(args.bundle_directory,args.output,**options)
            else:
                from .document_review import apply_review
                result = apply_review(args.bundle_directory,args.response_file,args.output,
                                      accept_changes=args.accept_changes,**options)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        if result.get('status') == 'EXPORT_ERROR':
            parser.exit(2,'候选与错误已保留；使用reexport和新的输出目录重试导出。\n')
    except KeyboardInterrupt:
        parser.exit(130,'已中断；原候选不修改，未完成尝试保留。\n')
    except Exception as exc:
        parser.exit(1,f'失败：{exc}\n')


if __name__ == '__main__':
    main()
