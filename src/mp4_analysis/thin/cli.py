"""Small command line interface; explicit sampling and limits for preview runs."""
import argparse
from .pipeline import run


def main():
    parser=argparse.ArgumentParser(description='视频 → 开源文档解析 → 原生结果与来源索引（待核验）')
    parser.add_argument('video')
    parser.add_argument('-o','--output',required=True)
    parser.add_argument('--sample-seconds',type=float,default=0.0,help='0保留所有像素不同的连续画面；大于0为显式抽样，可能漏内容')
    parser.add_argument('--start',type=float,default=0.0)
    parser.add_argument('--end',type=float)
    parser.add_argument('--max-frames',type=int,help='仅用于有限范围试跑，不是全片验收')
    parser.add_argument('--roi',type=int,nargs=4,metavar=('X','Y','W','H'))
    parser.add_argument('--word',action='store_true',help='请求引擎原生Word导出，失败会记录')
    parser.add_argument('--scans',action='store_true',help='额外生成OpenCV SCANS实验预览，不替代原画面')
    parser.add_argument('--device',default='cpu')
    parser.add_argument('--threads',type=int,default=2)
    parser.add_argument('--no-mkldnn', action='store_true', help='显式关闭CPU加速，仅用于兼容性排障')
    parser.add_argument('--table-mode', choices=['default', 'cells'], default='default',
                        help='使用上游默认表格结构或单元格几何模式；不代表内容验收通过')
    parser.add_argument('--reconstruct',action='store_true',help='实验：全时段分组调用SCANS，保留源帧；拼接不代表内容已验收')
    parser.add_argument('--ocr-models',choices=['server','mobile'],default='server',help='选择上游OCR模型；mobile仅用于显式性能对比')
    args=parser.parse_args()
    try:
        run(args.video,args.output,sample_seconds=args.sample_seconds,start=args.start,
            end=args.end,max_frames=args.max_frames,roi=args.roi,word=args.word,
            scans=args.scans,device=args.device,threads=args.threads,mkldnn=not args.no_mkldnn,table_mode=args.table_mode,reconstruct=args.reconstruct,ocr_models=args.ocr_models)
    except Exception as exc:
        parser.exit(1,f'失败：{exc}\n')

if __name__=='__main__':
    main()
