# MP4 Analysis — 开源引擎薄适配版（开发中）

> **新对话/新执行者请先读 [NEXT_CHAT_HANDOFF.md](NEXT_CHAT_HANDOFF.md)**：包含当前状态、全部阶段的失败教训、研究方法、源码阅读顺序、原视频与工件位置、精确缓存恢复步骤和下一步验收任务。关键运行快照见 [docs/handoff_evidence_2026-09-28.json](docs/handoff_evidence_2026-09-28.json)。当前代码在 `feat/open-source-thin-pipeline-20260928` / 草稿 PR #3，不在 main。旧 `TASKS.md`、`REFACTOR_PLAN.md` 已标明历史状态，请勿按旧的大框架计划重新开发。

三个模块、一条本地流水线，不做插件平台、数据库或模型自研。

| 模块 | 复用 | 本仓库负责 |
|---|---|---|
| video.py | PyAV/FFmpeg；OpenCV SCANS 的公开 detail 接口 | 读取画面、PTS时间、分组调用、来源映射、失败回退 |
| parser.py | PP-StructureV3 | 一个引擎入口、原生输出、缓存、错误记录 |
| output.py | 引擎原生 Markdown/HTML/XLSX/DOCX | 结果清单、来源链接、简易检查 |

`pipeline.py` 顺序连接三者，`src/mp4_analysis/thin/` 是 CLI 入口。旧代码保留作对照，旧二进制成品不代表新流程输出。

## 安装

建议 Python 3.11。依赖固定 OpenCV contrib 4.10.0.84、PaddlePaddle 3.2.2、PaddleOCR 3.7.0、PaddleX 3.7.2，不需要为拼接升级 OpenCV 或再安装一套相冲突的 OpenCV 包。

```bash
python -m pip install -e ".[parser,dev]"
python -m pip check
python -m pytest -q
```

首次运行需下载上游模型，后续复用模型缓存。录屏在运行机器上推理，不调用云端识别API。离线使用须预先准备模型与依赖；Windows 原生安装尚未验收。

## 先小范围试跑

```bash
mp4-analysis "MP4/ET6601_SRC_LRS设计文档.mp4" -o output/sarc_preview --start 15 --end 19 --sample-seconds 1 --max-frames 4 --word
```

这只是选定片段的抽样，不代表整段视频已提取完整。

默认不做时间抽样，只合并连续像素完全一致的画面：

```bash
mp4-analysis "MP4/ET6601_SRC_LRS设计文档.mp4" -o output/sarc_full
```

默认模式可能很慢，不能因逐帧读取就认定资料恢复完整。同配置重跑可复用帧和成功解析结果；缓存校验输入、配置、版本及输出文件哈希。换视频或抽帧参数时须换输出目录。

## 实验性滚屏重建

```bash
mp4-analysis "MP4/ET6601_SRC_LRS设计文档.mp4" -o output/sarc_reconstructed --sample-seconds 1 --reconstruct --ocr-models mobile --word
```

- `--reconstruct` 对全部选中画面分组调用原生 SCANS，并非只处理开头8张。
- 使用 OpenCV 自带的特征、仿射匹配/估计/调整、仿射投影、GraphCut 接缝和无混色组合；没有本地配准求解器或生成式补画。
- 通过公开 detail 接口获取输入成员及原生变换，兼容固定的 4.10 Python 绑定，不再依赖缺失的 `Stitcher.component()/cameras()`。
- 记录输入图像像素到合成画布的映射；若使用 ROI，原视频坐标还需加回 `source_offset`。映射来自原生 warper，不直接将 camera.R 当成画布坐标。
- 排除输入、明显变形、超过画布大小限制或原生异常时，回退到保留的原画面。
- 合成图作为明确标记的未核验派生输入交给解析器，原帧仍保留。几何检查不等于接缝内容正确；重叠分组仍可能重复文字。
- `--ocr-models mobile` 是显式选择上游轻量OCR模型，默认仍为 server；速度和准确性必须实测。
- `--sample-seconds 1` 可能漏掉短暂出现的内容，不能据此宣称全视频覆盖。
- `--scans` 仍只是额外尝试开头最多8张画面的预览，不等同于 `--reconstruct`。

## 输出

```text
output/
  video.json          # 视频哈希、帧号/时间、ROI偏移
  frames/             # 原画面；指定ROI时为该区域
  reconstruction.json # 使用 --reconstruct 时的分组、拒绝原因、来源映射
  reconstructed/      # 未核验的原生拼接候选
  native/             # 每个解析输入的原生JSON/Markdown/图片/表格/可选Word
  index.html
  index.md
  report.json         # 已处理/待处理输入、错误、缓存和未核验状态
```

Word按解析输入导出，不是一份已经整合验收的“完整版”。保留原生HTML/JSON，以核对表格的行、列及合并单元格。公式识别、图表转数据和印章识别默认关闭，图像证据保留。不进行语义改写、编辑距离删字或重复单元格过滤。

## 尚未完成

完整且高效的视频内容覆盖、所有跨屏图表的可靠整合、密集表格正确性、整片Office成品验收。回归测试通过、文件生成成功、帧数和模型置信度，都不能代替内容验收。只能处理合法授权录屏中实际可见的内容。

## 上游依据

- https://pyav.org/docs/stable/
- https://github.com/opencv/opencv/blob/4.10.0/modules/stitching/src/stitcher.cpp
- https://github.com/opencv/opencv/blob/4.10.0/samples/python/stitching_detailed.py
- https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html

各轮实测范围与失败记录见 `docs/thin_pipeline_step*_2026-09-28.md`。不将测试执行成功混同于内容验收。
