# 指定区域截图 OCR（开发中）

先读 [NEXT_CHAT_HANDOFF.md](NEXT_CHAT_HANDOFF.md)。输入已经改为截图目录，视频提取/拼接不再是生产入口。保留原包名 `mp4_analysis` 和旧命令别名仅为兼容安装，不表示仍支持MP4。

**2026-10-01：区域输入与批量OCR接线已经编码并提交；本轮未运行测试、OCR、GUI或成品验收。整份文档总装与修订应用尚待后续实现，不把单图原生输出称为整文档交付。**

## 当前实际链路

截图目录 → 显式区域配置 → Pillow批量裁剪 → 全组预览 → 确认本批裁图 → PP-StructureV3逐图解析 → 原生文件、状态及仅裁图的复核任务。

- 选框复用OpenCV `selectROI`，不自研截图或图形编辑器。
- 裁剪复用Pillow；OCR复用已有PaddleOCR/PaddleX，不新增解析后端。
- 没有区域配置就报错；取消、越界、尺寸变化不会退回整屏OCR。
- 原截图不改。输出预览及模型复核任务只有文档裁图，不复制整屏到交付目录。
- 原图、清单顺序或区域变化会生成新批次；同大小不同内容也会变更身份。
- 原生缓存按模型/参数/实现身份分开；失败记录和成功缓存保留。

## 环境

复用已经可用的Python 3.10—3.12环境。新安装才需要：

```bash
python -m pip install -e ".[parser]"
```

已有依赖齐全时，仅更新可编辑安装及命令别名：

```bash
python -m pip install --no-deps -e .
```

可以使用 `screenshot-analysis`，也可以直接 `python -m mp4_analysis.thin.cli`，避免依赖新别名是否已注册。请将 `python` 替换为测试机现有虚拟环境的解释器，不要求重建环境。本项目不再直接依赖PyAV；OpenCV保留用于现成区域选择及解析依赖。

## 1. 桌面上选一次区域，并生成整组裁图预览

在仓库根目录执行，选框窗口中拖动矩形，按Enter确认，按C取消：

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o "work/efc_detail" --select-region "work/regions/efc_detail.json"
```

该命令只保存区域并准备裁图，不初始化Paddle、不进行OCR。默认以源manifest的第一张截图选框；可用 `--reference-image` 指定本组其他截图。预览缩小时，程序将坐标映射回原图，不缩小实际OCR裁图。

打开控制台打印的 `preview.html`，检查全组内容和边缘；记下其中的 `approval_id`。相同分辨率不证明窗口位置相同，不能跳过整组预览。

没有桌面GUI的机器：在有桌面的采集电脑保存区域JSON，再在处理电脑使用相同配置和截图；不要为选框重装OCR环境。

## 2. 确认本批裁图后，连续运行OCR

将下面的 `APPROVAL_ID` 替换为预览页面实际给出的完整值：

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o "work/efc_detail" --roi-config "work/regions/efc_detail.json" --accept-crops APPROVAL_ID
```

默认server模型；需要明确选择时使用 `--ocr-models mobile` 或 `--ocr-models mixed`。保留上游模型，不据模型名称承诺准确率。

`--word`（别名 `--native-word`）仅额外保存每张截图的原生Word，可能增加耗时；当前不是整份文档合并功能。默认保存原生JSON、Markdown、HTML/XLSX及引擎图像资源，按实际模型输出而定。

同配置重新运行会检查并复用完整成功缓存；只处理失败或未完成的输入。中断保留状态和成功结果。不同配置位于独立结果目录，不能把旧输出当成新模型实际运行。

## 3. 例外截图与已经裁好的输入

为一张位置不同的截图设置覆盖区域，使用它的实际文件名：

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" --select-region "work/regions/efc_detail.json" --override-image "ACTUAL_SCREENSHOT.png"
```

修改后重新生成全组预览，再使用新的approval_id，不复用旧批准：

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o "work/efc_detail" --roi-config "work/regions/efc_detail.json" --prepare-only
```

ShareX已经只截取文档内容时，可以显式使用 `--full-image` 代替区域JSON。它也先准备预览，确认后才能OCR，不能把它用于跳过未配置的整屏截图。

两组文档分别选择区域、使用独立输出目录。选择上层 `screenshots/` 不会默默递归混合两份文档，而是明确提示选择文档子目录。Windows建议使用较短输出根目录，例如 `D:/ocr/efc`。

## 区域配置格式

JSON由选框命令生成。`schema=1`、`coordinate_system=source_pixels_ltrb_exclusive`；`default` 包含 `image_size=[width,height]` 和 `box=[left,top,right,bottom]`，右/下边界不包含。`overrides` 按完整截图文件名保存同形状配置。

不提供未经确认的现有截图坐标。尺寸不一致必须单图覆盖；程序不自动缩放ROI，也不通过裁剪外填黑边掩盖越界。正文、表格、标题和图像都属于区域内内容，不按text标签过滤图表。区域内水印遮挡不能靠矩形裁剪无损去除，无法辨读的原文需标未决。

## 输出与状态

```text
work/efc_detail/
  .screenshot_project.json       # 绑定源文档，拒绝复用别人的输出目录
  latest.json                   # 当前裁图批次
  preview.html                  # 当前批次预览入口
  latest_result.json            # 当前OCR结果位置
  batches/<batch_id>/
    manifest.json               # 源hash、ROI、裁图hash、逐图准备状态
    preview.html                # 只展示文档裁图
    frames/                     # 名称兼容，实际内容只有裁图
    runs/<execution_id>/
      crop_approval.json
      report.json               # 每张图的终态/未完成状态、计时、缓存命中
      index.html
      index.md
      review_tasks.json         # 仅裁图+来源引用，没有自动模型调用
      native/                   # 上游原生输出
      failed_attempts/          # 被重新执行前保留的失败产物
```

`PARSED_UNVERIFIED`只代表引擎完成，不代表内容正确；`REVIEW_REQUIRED`仍需本地核对。坏图、非法区域、失败和未处理项不会自动变成PASS。

源manifest存在时严格按index读取，检查文件集合及声明尺寸；不存在时自然排序并标明未验证页序。PNG编码无损不代表阅读器显示的小字一定足够清晰。一张截图也不一定是一整页。

## 当前边界

本轮未运行测试或OCR。整份Word/表格集总装、结构化视觉意见的校验应用和修订稿重导出属于接下来的开发范围；61张实际效果由本地验证。现存历史工作流仍有视频参数，本轮未修改或启动工作流；历史报告保留，不再照旧视频指令执行。

上游参考：Pillow Image.crop、OpenCV selectROI、PaddleOCR PP-StructureV3；既有Pandoc适配继续保留给后续文档总装复用。没有新截图软件、OCR引擎或表格求解器。
