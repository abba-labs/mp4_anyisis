"""Screenshot CLI: choose a document region, preview the batch, then run OCR."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import run
from .screenshots import select_region


def main():
    command = argparse.ArgumentParser(
        description='指定文档区域截图 -> 批量裁剪预览 -> 原生OCR（不接收视频）',
        epilog='默认先生成裁图预览；确认后加 --accept-crops <approval_id> 才运行OCR。')
    command.add_argument('input_dir', help='一份文档的PNG截图目录，可包含manifest.json')
    command.add_argument('-o', '--output', help='独立输出目录，不能在输入目录内')
    region = command.add_mutually_exclusive_group()
    region.add_argument('--roi-config', help='已有区域JSON配置，支持单图覆盖')
    region.add_argument('--full-image', action='store_true',
                        help='明确确认所有输入已只包含所需文档区域；不再裁剪')
    region.add_argument('--select-region', metavar='SAVE_JSON',
                        help='调用OpenCV鼠标框选并保存配置；不启动OCR')
    command.add_argument('--reference-image', help='整组选框使用的PNG文件名；默认清单第一张')
    command.add_argument('--override-image', help='为指定PNG单独选框，更新--select-region指定的已有配置')
    command.add_argument('--prepare-only', action='store_true', help='只生成全组裁图、来源清单及预览')
    command.add_argument('--accept-crops', metavar='APPROVAL_ID',
                         help='确认当前裁剪预览的完整approval_id，开始/恢复OCR')
    command.add_argument('--word', '--native-word', dest='word', action='store_true',
                         help='另外导出每张截图的原生Word；不是整文档合并输出')
    command.add_argument('--device', default='cpu', help='推理设备，例如cpu或gpu:0')
    command.add_argument('--threads', type=int, default=2, help='CPU推理线程数')
    command.add_argument('--no-mkldnn', action='store_true', help='关闭CPU MKLDNN')
    command.add_argument('--table-mode', choices=['default', 'cells'], default='default')
    command.add_argument('--ocr-models', choices=['server', 'mobile', 'mixed'], default='server')
    args = command.parse_args()
    if args.threads < 1:
        command.error('--threads必须为正整数')
    if (args.reference_image or args.override_image) and not args.select_region:
        command.error('--reference-image/--override-image只能与--select-region一起使用')
    if args.reference_image and args.override_image:
        command.error('整组选框与单图覆盖不能同时执行')
    if args.accept_crops and (args.prepare_only or args.select_region):
        command.error('请先完成选框/预览，再使用--accept-crops')
    if not args.output and not args.select_region:
        command.error('批量准备/识别需要-o输出目录')
    if not (args.roi_config or args.full_image or args.select_region):
        command.error('必须指定--roi-config、--select-region或显式--full-image；不自动识别整屏')
    try:
        config = args.roi_config
        if args.select_region:
            config = select_region(args.input_dir, args.select_region,
                                   filename=args.override_image or args.reference_image,
                                   override=bool(args.override_image))
            print(f'区域已保存：{Path(args.select_region).resolve()}', flush=True)
            if not args.output:
                return
        report = run(
            args.input_dir, args.output, roi_config=config, full_image=args.full_image,
            prepare_only=args.prepare_only or bool(args.select_region), accept_crops=args.accept_crops,
            word=args.word, device=args.device, threads=args.threads,
            mkldnn=not args.no_mkldnn, table_mode=args.table_mode, ocr_models=args.ocr_models,
        )
        if report['status'] == 'CROPS_PREPARED':
            print(json.dumps({
                'status': report['status'], 'ready': report['ready'], 'failed': report['failed'],
                'preview': str(Path(report['batch_directory']) / 'preview.html'),
                'approval_id': report['approval_id'], 'ocr_executed': False,
            }, ensure_ascii=False, indent=2))
            print('查看全部裁图后，用相同输入、输出和区域配置重运行，并添加：')
            print(f'--accept-crops {report["approval_id"]}')
            if report['failed']:
                print('部分截图准备失败；修正区域/清单后重新预览，或明确接受当前部分批次。')
        else:
            print(json.dumps({key: report.get(key) for key in
                              ('status', 'counts', 'cache_hits', 'elapsed_seconds', 'run_directory')},
                             ensure_ascii=False, indent=2))
    except KeyboardInterrupt:
        command.exit(130, '已中断；已完成结果和记录保留。\n')
    except Exception as exc:
        command.exit(1, f'失败：{exc}\n')


if __name__ == '__main__':
    main()
