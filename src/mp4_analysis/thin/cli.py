"""Command line interface for screenshot document extraction."""
import argparse
from .pipeline import run


def main():
    parser = argparse.ArgumentParser(description='截图目录 -> 原生文档解析 (PP-StructureV3)')
    parser.add_argument('input_dir', help='包含截图 PNG 的目录路径')
    parser.add_argument('-o', '--output', required=True, help='解析结果输出目录')
    parser.add_argument('--word', action='store_true', help='同步导出原生 Word 文件')
    parser.add_argument('--device', default='cpu', help='推理设备 (cpu / gpu)')
    parser.add_argument('--threads', type=int, default=2, help='CPU 推理线程数')
    parser.add_argument('--no-mkldnn', action='store_true', help='关闭 CPU MKLDNN 加速')
    parser.add_argument('--table-mode', choices=['default', 'cells'], default='default',
                        help='表格解析模式')
    parser.add_argument('--ocr-models', choices=['server', 'mobile'], default='server',
                        help='OCR 模型类型 (server 高精度 / mobile 轻量)')
    args = parser.parse_args()
    try:
        run(args.input_dir, args.output, word=args.word,
            device=args.device, threads=args.threads, mkldnn=not args.no_mkldnn,
            table_mode=args.table_mode, ocr_models=args.ocr_models)
    except Exception as exc:
        parser.exit(1, f'失败：{exc}\n')

if __name__ == '__main__':
    main()
