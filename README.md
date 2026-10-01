# 指定区域截图 OCR（首版实现，待本地验证）

先读 [NEXT_CHAT_HANDOFF.md](NEXT_CHAT_HANDOFF.md)。只接收截图目录，不恢复MP4提取或滚动拼接。`mp4_analysis`包名和旧命令别名仅为兼容安装。

**2026-10-01：三轮主要代码已提交。ChatGPT没有运行测试、GUI、OCR、模型或Office生成/渲染；这是实现交付，不是61张截图验收通过。**

截图目录 → 指定区域 → 批量裁剪预览/确认 → 现有OCR → 整份文档候选 → 外部视觉意见 → 有来源的独立修订稿。

## 复用，不造新引擎

ShareX负责采集；OpenCV selectROI选框；Pillow裁剪；PP-StructureV3是唯一默认解析后端；Pandoc输出Word，PaddleX已有表格转换器输出Excel。新增代码只负责输入边界、任务顺序、缓存、文件组织与修订记录，没有新OCR、表格求解器、网页编辑平台或模型服务。

缺ROI、取消、越界时不退回整屏；原PNG不修改。OCR和模型任务只接收批准的文档裁图。区域内水印遮挡、模糊字不能靠裁剪补好；未决项单列，不自动PASS。

## 环境

复用已有Python 3.10—3.12环境，不重装已可用的OCR。新环境才需要：

```bash
python -m pip install -e ".[parser,document]"
```

已有依赖齐全，仅注册新命令别名：

```bash
python -m pip install --no-deps -e .
```

下文也可直接使用`python -m`，python须指向现有虚拟环境。最终Word使用已有Pandoc 3.1.11.1，Excel使用PaddleX 3.7.2自身转换能力。

## 推荐：两组文档连续处理

完整说明见 [多文档运行与恢复](docs/SCREENSHOT_BATCH_RUN.md)，现成计划为 [examples/screenshot_collection.json](examples/screenshot_collection.json)。它对应已有的34张详细设计和27张LRS，不包含虚构ROI。

### 1. 每组只选一次文档区域

在有桌面的电脑执行，已有配置就跳过本步：

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" --select-region "work/regions/efc_detail.json"
python -m mp4_analysis.thin.cli "screenshots/efc模块lrs设计文档" --select-region "work/regions/efc_lrs.json"
```

拖框后Enter确认，C取消；程序映射回原图像素，不缩小实际OCR裁图。无桌面的处理机读取采集电脑保存的JSON。例外截图使用`--override-image 实际文件名.png`更新该组ROI。

### 2. 整组预览，再一次确认运行

```bash
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
```

打开输出的`collection_preview.html`，检查两组全部裁图、边缘及错误项；将打印的完整approval_id代入下一条命令：

```bash
python -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

集合配置的相对路径以JSON所在目录为准。输入或ROI或计划变化必须重新prepare/确认；相同计划直接重复run会检查并复用成功缓存。每份文档独立输出，错误不隐瞒、不混组。集合的`index.html`链接各组OCR结果和实际文档。

OCR模型默认server，计划可显式设mobile或mixed。`ocr.word=false`不逐截图生成Word，`export.word=true`在最后输出整文档。首次模型是否已缓存、各阶段耗时、准确度均以本地实际运行为准。

## 单份文档入口仍保留

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o work/efc_ocr --roi-config work/regions/efc_detail.json --prepare-only
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o work/efc_ocr --roi-config work/regions/efc_detail.json --accept-crops ACTUAL_CROP_APPROVAL_ID --document-output work/deliveries/efc_tool_v1
```

第二条使用单组preview.html的approval_id，不是集合accept-plan。`--document-output`必须为新独立目录。`--word/--native-word`仅额外生成每截图原生Word，一般不需开启。

已经只含文档的ShareX截图可明确用`--full-image`，但仍需预览确认。分辨率相同不证明窗口位置相同，必须检查整组区域；不能用full-image跳过应有的选框。

## 已有结果：直接组织或重导出，不重跑OCR

RUN_DIRECTORY取打印路径或单组latest_result.json：

```bash
python -m mp4_analysis.thin.document_cli build RUN_DIRECTORY -o work/deliveries/efc_tool_v1
python -m mp4_analysis.thin.document_cli reexport ACTUAL_BUNDLE_DIRECTORY -o work/deliveries/efc_export_v2
```

build可从部分运行生成有缺口标记的候选；reexport保留冻结正文，从初稿或修订稿重试Office导出。旧版本不覆盖，无模型调用。Word/Excel失败保留HTML/content及错误报告，退出码2；显式只需基本格式时可加`--no-docx --no-xlsx`。

## 外部模型复核：任务文件、差异文件、独立新稿

[完整任务格式](docs/SCREENSHOT_DOCUMENT_OUTPUT.md)。已有获准模型读取文档包的review_tasks.json及evidence裁图，不读区域外像素、不获得expected_text抄答案；只输出有来源的差异和未决项。

```bash
python -m mp4_analysis.thin.document_cli inspect-review work/reviews/efc_changes.json
python -m mp4_analysis.thin.document_cli apply work/deliveries/efc_tool_v1 work/reviews/efc_changes.json -o work/deliveries/efc_reviewed_v1 --accept-changes ACTUAL_RESPONSE_SHA256
```

版本/原值/hash/来源不匹配则拒绝应用。支持文本和单元格文字修订、漏段恢复、派生正文叠加文字排除；不允许模型直接改跨度、删整表、生成补图或执行命令。关键字段仍需源内容验收。

程序不自动调用视觉API或采购服务。模型身份、调用用量和费用按实际记录；未知保留unknown/UNMETERED_SUBSCRIPTION。

## 增量、恢复及路径

只在同一文档项目内复用原图hash、ROI、裁图hash/尺寸、模型参数及原生解析实现完全匹配的成功缓存。复制前后核对所有文件哈希，不用文件大小或相似文字判定相同。重新排序或补页不要求未变页面重做OCR，改变ROI/内容仍产生新批准批次。

损坏/失败缓存先移到failed_attempts；历史调用状态保存在attempts。每次report的墙钟时间属于当前调用，缓存里的native.timings属于历史，不相加冒充此次推理。Ctrl+C/SIGTERM尽量落盘；强杀/断电后检查残留锁，程序不擅自解锁。

新run目录缩短为`runs/r_<16位定位符>`，完整身份仍存文件核查；兼容旧长run目录，不重命名旧数据。**批次层仍是64位hash**：该层的缩短改动本轮被平台安全检查拦截，screenshots.py未改；请用短输出根（例如`D:/ocr/efc`），不保证任意长路径均兼容。

## 实际交付内容

集合`index.html`提供统一索引；每个文档包独立包含：

```text
content.json
bundle.json
review_tasks.json
unresolved.json
export_report.json
document.html
document.md
document.docx             # 按实际导出结果
evidence/                 # 仅批准裁图
images/
tables/                   # 每表HTML及实际生成的XLSX
table_index.json
```

修订版另有review_response.json、applied_changes.json；重导出版有reexport_origin.json。存在文档候选不证明内容正确，未支持的原生结构保留裁图并记未决；不推断原始分页、不自动跨截图合并表格或模糊去重。

## 未执行验证与遗留边界

三轮均按要求只开发，未运行实际61张OCR、模型、Word/Excel生成或渲染。区域外排除、增量复用、排序、错误恢复、导出一致性和内容准确率均待本地验证。历史工作流仍有视频参数，未获准修改/启动，不能称CI已经迁移完成。旧视频报告只作历史，不再指挥当前截图流程。
