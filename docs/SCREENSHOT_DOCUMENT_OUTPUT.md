# 截图整文档输出与可重放修订（第2轮实现）

2026-10-01。开发进入提交：d3f22ead7a69eadac496d58c5758c5dbe774495b。
本轮只编写与提交代码，没有运行测试、OCR、GUI、模型、Office导出或渲染。下面是已实现的入口和数据契约，不是实测通过记录。

## 1. 现在的操作链路

选框／裁图确认 → 原有PP-StructureV3 → 保存截图OCR运行 → 组织整份文档包 → 本地获准模型看裁图并提交差异JSON → 批量批准该JSON → 生成独立修订文档包。

一个文档包包括：整份Word、HTML、带原始HTML块的Markdown、独立表格HTML/Excel、图像、仅指定区域的证据PNG、结构化正文、稳定修改目标和未决清单。是否产生Word/Excel以实际export_report.json为准。没有输出文件不算已交付。

不引入新OCR后端、表格求解器、网络服务或Agent平台。未部署视觉模型，文件导入器不会自动调用API；本地Agent通过已经获准的看图工具读取任务、填写真实差异。模型意见、程序应用成功和资料准确性分别记录。

## 2. 成熟能力的复用

- 图像：Pillow只从已确认的文档裁图中切出图像块，不从整屏重新取图。
- 表格HTML：lxml读取上游已有的行与rowspan/colspan；物理单元格按源HTML分配ID，不推断网格、不求解行列。
- Word：沿用已有Pandoc 3.1.11.1，以HTML直接转换DOCX，避免技术标识符被Markdown扩展重新解释。不复制粘贴OOXML段落来合并文件。
- Excel：调用已安装PaddleX 3.7.2的`paddlex.inference.utils.io.tablepyxl.document_to_workbook`，即上游XlsxWriter所用的现成转换器；openpyxl用于文字类型、基本可读格式和存盘回读，不用于重新求解表格。每张表独立Excel，`table_index.json`关联正文位置和源裁图。
- 所有单元格按文字导出，不执行截图中的公式，不把地址、前导零或`=`字符串转换成计算公式。

固定上游源码依据：
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/utils/io/writers.py
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/utils/io/tablepyxl.py
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/utils/io/style.py
https://pandoc.org/MANUAL.html

只补缺少的依赖，复用现有环境；新安装可使用`python -m pip install -e ".[parser,document]"`。已安装环境不要为此重建。Pandoc为外部可执行程序，继续使用原有版本。Python范围不变。

## 3. 已有OCR结果：不重新识别，直接组织文档

`RUN_DIRECTORY`取第一轮OCR控制台输出的`run_directory`，或由`latest_result.json`的run字段定位；它形如`工作根/batches/批次/runs/运行`。命令不会调用OCR。

```bash
python -m mp4_analysis.thin.document_cli build RUN_DIRECTORY -o work/deliveries/efc_tool_v1
```

新文档目录必须与源批次隔离，不能是其子目录或父目录，也不能已存在。构建读取run/report.json、crop_approval.json和batch/manifest.json；检查批准ID、逐图哈希、模型身份和native文件哈希。

支持在有失败项的已保存运行上生成部分候选：未完成OCR的裁图作为明确的原图回退保留，未准备成功的截图显示缺口，全部问题写入unresolved.json。这不是自动补回未识别文字。

不具备某个导出器时，基础HTML和content.json仍会保留，export_report.json记录错误，CLI返回2。后续可从同一OCR结果生成另一版本，无需再次OCR。明确不需要某类格式时可选：

```bash
python -m mp4_analysis.thin.document_cli build RUN_DIRECTORY -o work/deliveries/efc_html_v1 --no-docx --no-xlsx
```

## 4. 一条命令：OCR完成后直接组织整文档

在已经确认本批裁图后：

```bash
python -m mp4_analysis.thin.cli screenshots/efc详细设计文档 -o work/efc_ocr --roi-config work/regions/efc.json --accept-crops APPROVAL_ID --document-output work/deliveries/efc_tool_v1
```

不必打开`--word`；该旧选项只额外逐截图导出上游Word，而`--document-output`在最后组织整份Word。

若OCR流程返回部分失败，主命令会保留运行记录并退出；用第3节build命令从该已保存运行组织部分候选。不会为导出再次重跑识别。多组入口与统一断点恢复在第3轮收尾。

## 5. 文档包结构

```text
efc_tool_v1/
  content.json                 # 权威结构化候选正文、表格及来源；不是原生OCR
  document.html                # 可直接查看的整文档候选
  document.md                  # 保留HTML结构的Markdown，不用于重新生成Word
  document.docx                # Pandoc实际生成成功时存在
  evidence/                    # 只包含已经批准的文档裁图，无整屏原图
  images/                      # 从上述裁图再次切出的原像素图像块
  tables/                      # table_0001.html及成功导出的xlsx
  table_index.json             # 表ID → 文件、裁图、区域、结构身份
  review_tasks.json            # 真实裁图+稳定block/cell ID+原值+hash
  unresolved.json              # 来源/结构/识别/覆盖未决
  export_report.json           # 实际文件回读结果、导出错误，不是源准确率
  bundle.json                  # 所有包内文件哈希、content身份与bundle身份
```

图片链接都是包内相对路径，不依赖测试机临时目录。原native保持原位且不修改，证据包不复制原始整屏。每张截图按输入清单序排列，内部沿用native块列表顺序；不自动推断原文页号，不将相似文字去重，不跨截图硬合并表格。

上游HTML超出支持范围或原生结果失效时，保留已批准裁图作为回退，同时记录未决。不要将图像回退称为可编辑表格恢复成功。包含上游小字、错字、图像接缝问题的候选仍需本地验收。

## 6. 给本地视觉模型的任务

让模型读取文档包的review_tasks.json及其中引用的evidence PNG，按完整裁图逐块查漏，不只核对已有OCR目标。所有bbox均为裁图坐标[left,top,right,bottom]，右下不含；不是桌面坐标或原始整屏坐标。

表格的cell ID按上游物理单元格顺序分配，任务中bbox只精确到整个表格，明确标`table_region_not_individual_cell`。不能把这当作已经计算出的单元格像素框。

模型输出一个外部JSON，不直接改content.json。示例只说明格式，字符串占位必须从真实任务/看图结果取得，不得照示例伪造：

```json
{
  "schema": 1,
  "base_content_sha256": "从review_tasks.json复制实际值",
  "reviewer": {
    "mode": "agent_image_tool",
    "name": "实际模型名，不可得时明确unknown",
    "billing_mode": "UNMETERED_SUBSCRIPTION"
  },
  "reviewed_evidence_ids": ["screenshot_0001.crop"],
  "changes": [
    {
      "issue_id": "review-001",
      "operation": "replace_text",
      "target_id": "从任务复制实际目标ID",
      "before": "任务中的完整原值",
      "target_before_hash": "任务中对应before_hash",
      "text": "实际查看裁图后提出的完整替换文本",
      "critical": true,
      "reason": "具体源证据和差异说明",
      "evidence_refs": [
        {"evidence_id": "screenshot_0001.crop", "image_sha256": "实际证据哈希", "bbox": [10, 10, 200, 40]}
      ]
    }
  ],
  "unresolved": []
}
```

示例bbox不是现有截图坐标，必须实际定位后填写。`base_content_sha256`是程序规范JSON的身份，不是随意重新排版后content.json字节哈希。

支持的操作：

| 操作 | 作用及边界 |
|---|---|
| replace_text | 替换一段真实文字；必须原值与hash一致 |
| replace_cell | 只修改单元格文字，不修改行列、跨度或合并 |
| restore_fragment | 在同截图指定块之后插入有源证据的漏段；不能从答案抄写 |
| exclude_overlay | 仅从派生正文排除一个有证据的叠加文字块，原始块仍保留在content.json与变更日志；不删除图表 |
| flag_structure / flag_image | 标记结构或图像未决，不自动生成几何修复或补图 |

restore_fragment需target_id指向块；before/target_before_hash绑定该块原text，没有text的图表块则绑定完整块JSON及规范hash。禁止同一响应多次修改同一目标；先合并成一个最终建议。所有修改都检查证据ID、源图hash、裁图边界和目标所属截图。

`critical`默认true。寄存器、地址、位宽、下划线、极性、否定词等不靠命名规律补写。独立读取可作为`independent_read`附加记录，但程序不能证明一次新上下文真的执行过，不据此自动通过。关键修改保留待源验收项；没有复核的证据范围也保留未决。不要把期望答案给修正模型。

## 7. 一次批准整份意见，并生成新版本

```bash
python -m mp4_analysis.thin.document_cli inspect-review work/reviews/efc_changes.json
```

输出复核文件的准确SHA256、修改数量等，只读取、不应用。查看该文件后，一次批准整批意见：

```bash
python -m mp4_analysis.thin.document_cli apply work/deliveries/efc_tool_v1 work/reviews/efc_changes.json -o work/deliveries/efc_reviewed_v1 --accept-changes RESPONSE_SHA256
```

前置值、版本、文件hash或来源不匹配时整次拒绝，不把半份修改写入原稿。成功的新版本包含review_response.json原始字节、applied_changes.json前后值、父版本身份及重新导出的Word/表格。失败构建另留`.failed-*`目录，不覆盖历史产物。

这是“文件任务＋结果导入”，不是无人值守模型服务。不要伪造API次数/Token/金额。源图或表格有疑点也可保留候选继续后续截图，不要求模型不停自我修正到100%。

## 8. 一致性检查与明确未完成项

代码中已经加入生产时的回读检查，本轮未执行：

- Word从实际word/document.xml读正文和物理单元格，与冻结候选比对；保留标点、大小写、下划线，忽略排版空白。
- Excel先核对转换后非空单元格文字，再比较存盘前后坐标、值、数据类型和合并范围；空字符串与空XML存储可等价，但不凭此认定空格几何正确。
- 不一致写EXPORT_MISMATCH／EXPORT_ERROR，不把“文件存在”当通过。
- 上述不是源内容准确率，不证明文字来源正确、表格网格正确或图像完整；Word页渲染和密集表验收仍需本地进行。
- 本轮没有自动模型调用、自动跨页去重／表格合并，也没有对61张截图产生新的准确率或耗时数据。
- 剩余第3轮：多文档批量入口、增量复用和断点恢复、短路径与边界统一收尾、本地执行说明。仍不恢复视频流程。
