# 指定区域截图 OCR（开发中）

先读 [NEXT_CHAT_HANDOFF.md](NEXT_CHAT_HANDOFF.md)。输入为截图目录，不支持视频提取/拼接；保留`mp4_analysis`包名和旧命令别名仅为安装兼容。

**2026-10-01，第2轮：指定区域输入、批量OCR、整文档输出、外部视觉差异导入与修订重导出已编码。没有在ChatGPT侧运行测试、OCR、视觉模型、Office导出或渲染验收。**

当前链路：截图目录 → 显式区域配置 → Pillow裁剪 → 全组预览／批准 → PP-StructureV3 → 整份Word／HTML、表格与图像 → 外部模型复核意见 → 校验应用 → 独立修订稿。

## 复用的成熟能力

- ShareX负责截图采集，本项目不开发截图软件。
- OpenCV `selectROI`负责鼠标框选，Pillow负责批量裁剪。
- 现有PaddleOCR／PaddleX PP-StructureV3负责唯一默认解析后端。
- Pandoc负责HTML→Word；PaddleX已有tablepyxl导出器负责HTML→Excel，openpyxl负责基础格式和回读。没有自研表格网格求解。
- 本地已有获准看图能力负责视觉意见；程序只处理任务和差异文件，不自行上传图片或部署模型服务。

缺少区域、取消选框、越界或尺寸变化时，不退回整屏OCR。原截图不修改，处理与交付只携带文档裁图。原始OCR与修订候选分开保存。

## 环境

复用已有Python 3.10—3.12环境；不为新功能重装已可用的OCR。新安装才需要：

```bash
python -m pip install -e ".[parser,document]"
```

已有依赖齐全，只需更新命令别名时：

```bash
python -m pip install --no-deps -e .
```

也可直接运行下列`python -m`入口，不依赖别名注册。将python替换为现有虚拟环境解释器。整份Word继续使用已有Pandoc 3.1.11.1；表格Excel导出复用PaddleX 3.7.2。基础截图准备不会初始化OCR。

## 1. 一组截图选一次区域

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o work/efc_ocr --select-region work/regions/efc.json
```

拖动矩形，Enter确认，C取消。默认使用manifest第一张；可用`--reference-image 实际文件名.png`换一张选框。程序把预览坐标换回原图像素，不缩小实际OCR裁图。

打开打印的preview.html查看整组边缘和顺序，取得完整approval_id。分辨率相同不证明窗口位置相同。无桌面的处理机可读取采集电脑保存的JSON，不为选框改变OCR环境。

## 2. 批量OCR并在末尾生成整份文档

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o work/efc_ocr --roi-config work/regions/efc.json --accept-crops APPROVAL_ID --document-output work/deliveries/efc_tool_v1
```

APPROVAL_ID来自本批实际预览。`--document-output`必须是与输入/OCR工作目录隔离的新目录。结果目录已存在时不会覆盖，可另取v2。

默认server，显式可选`--ocr-models mobile`或`mixed`。不据模型名称承诺准确率。`--word`／`--native-word`仅额外逐截图导出原生Word，一般无需打开；整文档使用末尾的`--document-output`。

不加`--document-output`则仅运行OCR。部分输入失败时保留逐图终态和成功缓存。改变输入、ROI或模型配置不冒称同一次旧运行。

## 3. 已有OCR结果，不重跑，直接打包

RUN_DIRECTORY来自OCR输出或latest_result.json定位：

```bash
python -m mp4_analysis.thin.document_cli build RUN_DIRECTORY -o work/deliveries/efc_tool_v1
```

支持从已保存的部分运行生成部分候选，失败项和未识别内容明确保留，不称完整恢复。

缺导出程序时会保留content.json、HTML等和错误记录，CLI返回2。明确只需基础格式可使用`--no-docx --no-xlsx`，不代表已生成Office。

## 4. 模型复核意见导入与新稿导出

完整任务契约、示例JSON和边界见 [SCREENSHOT_DOCUMENT_OUTPUT.md](docs/SCREENSHOT_DOCUMENT_OUTPUT.md)。本地获准模型读取包内review_tasks.json和evidence裁图，只输出有来源的差异，不接收expected_text抄答案，不直接修改包文件。

```bash
# 只查看真实意见文件的修改数量与批准hash。
python -m mp4_analysis.thin.document_cli inspect-review work/reviews/efc_changes.json

# 审查后一次批准整批差异，产生独立修订稿，不改原生结果或工具初稿。
python -m mp4_analysis.thin.document_cli apply work/deliveries/efc_tool_v1 work/reviews/efc_changes.json -o work/deliveries/efc_reviewed_v1 --accept-changes RESPONSE_SHA256
```

支持文字修正、单元格文字修正、有证据的漏段插入、派生正文中的叠加文字排除及结构/图像问题标记。禁止模型改表格跨度或任意执行指令。全部校验先在隔离副本完成；任一前置值、版本或来源不一致则拒绝应用，不写半份修订到原稿。

这不是自动调用视觉API的入口。模型名、独立读取、Token和费用须按实际记录；未知就写未知，不凭任务文件生成冒称已复核。

## 例外截图与已裁好的输入

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" --select-region work/regions/efc.json --override-image ACTUAL_SCREENSHOT.png
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o work/efc_ocr --roi-config work/regions/efc.json --prepare-only
```

配置变更后重新预览，使用新approval_id。ShareX已经只截文档时，可显式`--full-image`代替区域JSON，也先准备预览。不能以此绕过未设置的整屏区域。

每组文档独立区域、独立输出；不把`screenshots/`父目录下多份文档默默混合。Windows使用短工作根。ROI为原图像素[left,top,right,bottom]，右下不含；同组default配合按文件名overrides。标题、正文、表格和图像都属于文档内容，不按text标签误删图表。矩形裁剪不能解决正文内部水印遮挡。

## 输出

OCR工作根中：latest.json定位裁图批次，latest_result.json定位OCR运行；batches/<batch>/manifest.json绑定来源与ROI，frames只有裁图，runs/<execution>/保存report.json、原生输出及失败尝试。

文档交付目录中：

```text
content.json                 # 冻结的结构化候选，不是原生OCR
bundle.json                  # 文件哈希及版本身份
review_tasks.json            # block/cell/evidence ID、原值和hash
unresolved.json              # 来源/识别/覆盖/结构未决
export_report.json           # 真实文件一致性及导出错误
 document.html
 document.md                 # 保留原始HTML块的Markdown
 document.docx               # 导出成功时才存在
 evidence/                   # 文档区域证据PNG，绝不含整屏原图
 images/                     # 从裁图取得的原像素图像块
 tables/                     # 每表HTML及实际生成的Excel
 table_index.json            # 表格与来源/输出文件映射
```

上面文件均在交付根下，缩进空格不代表另有子目录。修订包另有原始review_response.json、applied_changes.json和父包身份。未成功的构建保存在单独.failed-*目录，不冒充成功版本。

## 当前边界

按截图和原生块列表顺序组织，不推断原始分页、不自动跨页去重或合并表格。上游内容或结构无法安全解释时保留裁图并标未决。Word实际正文/物理单元格及Excel存盘一致性检查已经编码，但不代表本轮运行过，更不证明源识别正确或布局渲染合格。

第3轮收尾：多文档批量入口、逐页增量复用、异常恢复、短路径与交付说明统一。61张实际效果仍由本地测试。历史工作流仍有旧视频引用，本轮未改动或手动触发；历史报告不再指挥截图流程。
