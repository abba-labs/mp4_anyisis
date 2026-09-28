# MP4 Analysis — 开源引擎薄适配版（开发中）

三个模块、一条本地流水线，不做插件平台、数据库或模型自研。

| 模块 | 复用 | 本仓库负责 |
|---|---|---|
| video.py | PyAV/FFmpeg；可选 OpenCV SCANS | 画面读取、PTS时间点、来源索引、原画面保存 |
| parser.py | PP-StructureV3 | 一个引擎入口、原生输出、缓存、错误记录 |
| output.py | 引擎原生 Markdown/HTML/XLSX/DOCX | 结果清单、来源链接、简易检查 |

`pipeline.py` 顺序连接以上三者。`src/mp4_analysis/thin/` 是新入口。
旧 `pipeline.py`、`document/` 等保留便于对照，不再由 CLI 调用。旧二进制成品不代表新流程输出。

## 安装

建议 Python 3.11（开发环境固定 CPU PaddlePaddle 3.2.2、PaddleOCR 3.7.0）。

```bash
python -m pip install -e ".[parser,dev]"
python -m pytest -q
```

首次运行需下载上游模型；后续可复用本地模型缓存。敏感录屏只在运行机器上推理，不调用云端识别API。
离线部署需先按 PaddleOCR 官方说明准备模型及依赖。本版本尚未验证 Windows 原生安装。

## 先小范围试跑

```bash
mp4-analysis "MP4/ET6601_SRC_LRS设计文档.mp4" -o output/sarc_preview --start 15 --end 19 --sample-seconds 1 --max-frames 4 --word
```

这只是选定片段的抽样，不代表整段视频已提取完整。

默认完整模式不做时间抽样，只合并连续像素完全一致的画面：

```bash
mp4-analysis "MP4/ET6601_SRC_LRS设计文档.mp4" -o output/sarc_full
```

**完整模式可能很慢。** 视频压缩噪声和滚动会使大量画面不完全一致，CPU逐帧解析成本很高；当前先保真，不通过模糊删除换速度。
同配置重跑复用帧文件和原生解析缓存；缓存校验输入、引擎版本、配置和输出文件哈希。
换视频/抽帧参数必须换输出目录，避免混入旧产物。

## 输出

```text
output/
  video.json          # 原视频哈希、每个画面的帧号/时间/坐标偏移
  frames/             # 原画面（使用 --roi 时为指定区域）
  native/frame_*/      # 引擎原生 JSON、Markdown、图片、表格及可选Word
  index.html          # 时间点、原画面及各类结果链接
  index.md
  report.json         # 失败项、缓存使用、未核验状态
```

不重新编写Word排版器；Word按画面导出，不拼凑一份“完整版”。公式识别、图表转数据和印章识别默认关闭，图像证据保留。无语义改写、无编辑距离删字、无重复单元格过滤。
表格来自模型，行列或合并单元格仍可能有误，原生HTML/JSON必须一同核对。

## 当前边界（重要）

- 已接入的是画面解析；**尚未完成跨屏长表格、长图的自动合并**。
- `--scans` 直接调用 OpenCV SCANS，最多取首8张选定画面尝试拼接，只生成未核验预览；失败保留原图。
- SCANS高层接口没有输出逐帧坐标变换，本版本不假装已有精确拼接溯源，也不把预览偷偷交给OCR替代原图。
- 帧数不是原文页数；模型置信度不是准确率；没有人工对照，不标记完整恢复。
- 没有“任意视频100%恢复”承诺。只能处理合法授权的录屏中实际可见内容。

## 上游依据

- https://pyav.org/docs/stable/
- https://docs.opencv.org/4.x/d8/d19/tutorial_stitcher.html
- https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html
- https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.7.0

详见 `docs/thin_pipeline_validation_2026-09-28.md` 的实际测试范围，不将测试执行成功混同于内容验收。
