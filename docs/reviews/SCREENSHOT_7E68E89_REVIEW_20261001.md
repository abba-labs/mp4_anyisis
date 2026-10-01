# 截图首版源码复核：主体已接线，尚不能宣布全部完成

日期：2026-10-01。
审查代码固定为 `7e68e89076640f27354f2aa6ad8c1edc24ecf0b7`。
仓库：`abba-labs/mp4_anyisis`；分支：`feat/open-source-thin-pipeline-20260928`；PR #3 保持草稿，main 不改。

## 结论与证据边界

**源码复核结论：REQUIRES_FIXES；运行验收结论：NOT_RUN。**

三个开发轮次确实交付了区域准备、OCR调度、文档组装、修订导入、多组运行及缓存恢复的代码，不是只有任务说明。但“入口都有了”不能推导为“功能已经可靠完成”。本次定位了6类适配/收尾问题，另有明确范围限制。不能把它们推给OCR模型，亦不需要重新搭建框架。

方法：通过已连接GitHub查询实际PR head，固定提交后逐段追踪截图、单组/多组入口、缓存、组装、导出、修订、重导出及文件工具的调用关系。核对当前文件列表和交接。下面的触发例都是**源码可推导的反例或检查缺口，不是已经运行的测试结果**。

本次没有执行仓库测试、GUI、当前61张截图OCR、视觉模型、Word/Excel生成或渲染，也没有取得它们的运行通过数据。只额外读取历史已挂载原生JSON的字段形状，不作为截图版运行或准确性证据。容器源文件下载未成功，未声称完成全仓编译。未调用第三方代码审阅服务，未外发私有源码。本次只写审阅记录与根交接提示，**没有修复生产代码**。

## 已能由源码确认的主链路

| 环节 | 已存在的实现 | 不能据此宣称 |
|---|---|---|
| 区域输入 | `screenshots.region_box/prepare_screenshots` 要求显式区域；Pillow先裁剪；取消/越界不回退整屏 | 61张实际边界已人工确认、所有窗口位置相同 |
| OCR | `pipeline.run`验证裁图hash后调用已有NativeParser；默认不新增视觉服务 | 实际识别准确率、吞吐已验证 |
| 模型输入 | run任务和bundle证据来自文档裁图；没有自动模型请求 | 模型已自动完成全组复核 |
| 缓存 | `native_cache`对源hash、ROI、裁图、模型指纹及parser/patch实现做匹配，并验证输出文件 | 已实际完成跨批次恢复测试；模型权重文件本身已逐个hash锁定 |
| 文档及修订 | 有整份HTML/Word、表格集、裁图图片、差异导入和独立重导出入口 | 原始分页、跨屏去重、跨图表格结构都已恢复 |

主要来源：[screenshots.py](../../src/mp4_analysis/thin/screenshots.py)、[pipeline.py](../../src/mp4_analysis/thin/pipeline.py)、[native_cache.py](../../src/mp4_analysis/thin/native_cache.py)、[document_bundle.py](../../src/mp4_analysis/thin/document_bundle.py)。这些相对链接的实际固定版本以文末链接为准。

## R1：表格允许上/下标等标记，却在中间表示中丢掉语义

**优先级：高；类型：条件触发的数据损失。**

位置：`document_format.py` 的 `table_model`、`_cell_text`、`table_html`。

`table_model`允许 `sup`、`sub`、`s` 等节点；`_cell_text`只对br/p保存换行，对其他节点递归取普通字符；新表格又仅将这些字符进行HTML转义，不携带原有上下标信息。

源码反例：若原生单元格为 `<td>10<sup>3</sup></td>`，中间值会变成普通字符串 `103`，重导出的候选不再表示10的三次方。原始OCR即便给了正确的上标标记，我们的适配也会把含义改变。这里没有宣称当前61张一定包含这种标记。

修复方向：优先沿用成熟转换器支持的安全内联结构；暂时不能无损保留的标签，应明确拒绝该单元格/表格的可编辑转换，保留区域图并标未决，而非无声当成普通文本。不要自研公式/表格算法，也不要根据常识补表达式。

完成依据：相应带格式的受支持输入，输出仍保留语义；不支持时有可见失败/回退记录，不出现悄悄变成另一数值的情况。

## R2：成品一致性检查存在三类盲区

**优先级：高；类型：校验覆盖缺口，不是已观察到当前Word丢图。**

位置：`document_format.py` 的 `_compact`、`_expected`、`check_docx` 和 `export_bundle`。

### R2a：删除所有空白后比较，会掩盖有意义的空格错误

当前 `_compact` 为 `''.join(text.split())`。因此 `A B` 与 `AB`、`Flash Power Switch` 与 `FlashPowerSwitch` 都会落到同一比较值。正文还拼成一串后比较，不能证明段落边界正确。

源码反例：冻结候选有单词间空格，而实际Word少了空格，当前正文比较仍可能一致。技术标识符、命令参数和英文术语中的空格不能都视为排版噪声。

修复方向：区分段落/换行等允许规范化的排版信息与需保留的字间空格；至少为技术字段及单元格提供保留字符边界的比较。不能通过进一步删除符号来提高通过率。

### R2b：没有验证Word图片引用及资源

`_expected`跳过image块；`check_docx`只读取`word/document.xml`中的文字与表格，不检查drawing引用、relationships、media文件或图片集合。

源码反例：相同文字/表格但缺少图片的DOCX，不会因缺图被这一检查拒绝。不能把`CONSISTENT`解释成完整文档一致。当前返回`layout_rendered:false`、`merge_geometry_verified:false`等边界是正确的，但并不能补上缺图报警。

修复方向：用现成DOCX/OOXML读取能力核对期望图片与实际引用、资源存在及必要身份；区分非视觉完整性检查与之后本地的实际渲染检查。

### R2c：Excel结构检查主要覆盖存盘前后，而非候选到转换器输出

`expected_merges`在`document_to_workbook`转换完成后才取值，随后与重新打开的文件比较；另一个候选到转换后检查只比较非空单元格文本序列。

所以，如果转换阶段就改变合并范围或空行/空格位置，而非空文本顺序未变，存盘检查仍可能一致。这不是新的表格识别结论，也不能被标作原始表结构正确。

修复方向：在现成转换器边界对照候选的显式行/单元格跨度与转换结果；不能确认时标结构未核对。无需编写新的图像网格求解器。

## R3：单组目录缺失会在多组运行之前中止全部任务

**优先级：中；类型：失败隔离不完整。**

位置：`batch_cli.load_plan` 与 `_prepare/execute`。

`load_plan`遍历所有文档并执行`if not source.is_dir(): raise ValueError(...)`，发生在`execute`之前。虽然`_prepare`能把每组错误记录为`PREPARE_FAILED`，目录缺失/挂载暂时不可用却到不了该分支。

源码反例：计划里有两个路径格式合法的组，一组目录临时不存在，另一组可用；实际会在读取计划时整体退出，可用组也不会准备或执行。这应与“计划JSON错误、危险/冲突路径”这种必须整体拒绝的情况区分。

修复方向：保留语法、路径隔离和安全检查的全局拒绝；把普通输入资源可用性放到每组准备阶段记录。其他独立组继续，总状态明确部分失败。

## R4：分批视觉复核的当前状态会丢失/积累错误的待复核项

**优先级：中；类型：修订状态不一致。**

位置：`document_review.apply_review`。

每次应用都深拷贝旧`unresolved`，但将`reviewed_evidence_ids_reported`直接替换为本次响应中的ID；然后对本次未列出的所有证据追加`source_review_pending`。旧pending没有被解析/合并，已补查项目也没有转为已解决历史记录。

源码反例：两页e1/e2。首轮仅报已复核e1，则追加e2待复核；第二轮针对新候选复核e2，则旧e2待复核仍在，还新追加e1待复核。即使第二轮列出e1/e2，旧pending也不会自动退出当前未决列表。

修复方向：用稳定问题/证据ID维护当前未决与历史记录；对源hash不变且未被新内容修改影响的已有复核记录保留；只对实际补查完成项关闭pending。关键字段独立验收和模型自报已看过仍必须分开，不能借状态整理自动给内容PASS。

## R5：独立文档build入口没有完整继承输入目录隔离约束

**优先级：中；类型：入口约束不一致。**

位置：`document_bundle.build_document`；对照`cli.main`。

主CLI的`--document-output`检查与原截图目录、整个OCR输出目录均不相交。独立`build_document`只检查与当前batch目录不相交，没有核对manifest中的原截图目录，也没有保护整个OCR项目目录。

源码反例：使用独立build，将新的目标指定为`原截图目录/derived`，它与OCR batch不相交，会进入创建目标父目录/文件的逻辑，违反“输入目录只读”的接口约定。这里不声称它一定覆盖已有PNG：目标存在检查会保护已有目标；问题是仍能把派生文件写入原输入树，或把产物混入受管理的OCR工作树。

修复方向：将主CLI已实现的来源/工作目录隔离检查下沉到公共组装函数，独立调用与主CLI采用相同规则；保留多组入口现有的合法deliveries目录。不增加新的目录框架。

## R6：计时字段不能代表从命令开始的完整墙钟时间

**优先级：中；类型：计量范围与说明不一致。**

位置：`pipeline.run`、`batch_cli.execute`、根交接的计时口径。

单组`run`在`prepare_screenshots`完成后才设置`started`；多组`execute`在最初的`_prepare`完成后才设置`begun`。但准备阶段会读原图、校验、裁剪、编码PNG并生成预览。批准后的run还会重新准备一次；集合第一次准备不在其elapsed里，单组准备也不在OCR elapsed里。

源码推论：这些字段可作为特定子阶段耗时，但不能直接叫命令全程耗时或拿来比较包含准备的端到端流程。本次没有测量其漏记了多少秒。

修复方向：在入口计时并单列prepare/OCR/cache/export等阶段；保持原生缓存timings为历史信息的现有区分，不把缓存时间冒充新推理。最终报告写清各字段起止边界。

## 范围限制：不是新发现的算法故障，也不能冒称已经解决

- 模型复核目前是文件任务和差异导入，仍要由已有获准Agent/视觉通道执行。它不是无人值守视觉API；这一点符合既定首版范围，不要求换服务。
- 输出按截图/原生块顺序组织，不自动判断完整页、重叠去重或跨图拼表。若实际输入是连续滚动的部分页，不能把一份有重复的拼接候选称为原文还原。
- 表格结构问题可flag，不能靠导入JSON随意重写几何。现成工具转换不是源结构正确性的证明。
- 区域裁剪排除范围外像素，但不能去除正文内水印或补回不可见内容。没有目视核定61张ROI，就不能宣称全部边界正确。
- `screenshots.py`此前被拦截的更新仍未应用；本次只读取原文件，没有重试或绕过。64位batch目录不是核心链路失败的证据；使用短输出根仍是现有限制。
- 历史视频工作流仍未迁移；此项保留原授权边界，不借此次复核去更改工作流或PR元数据。

## 收尾方式：一个适配修复包，不再扩大方案

优先处理R1/R2的数据保留与检查；同时完成R3/R4的多组和复核状态、R5公共目录约束、R6真实计时。复用既有Pillow、PaddleOCR/PaddleX、Pandoc、lxml及Office读取库，原则上不新增解析后端或服务。

源码修复由ChatGPT承担；本地执行验证和实际61张成品检查，保持用户既定分工。不是要求用户逐个标点接力，也不先修上游所有OCR错误。此报告本身不将任何R项变成已修复。

## 固定源码与官方语义参考

以下链接均固定本次审查提交，后续分支更新不改变本次结论的来源：

- [区域输入](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/screenshots.py)
- [单组运行](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/pipeline.py)
- [多组入口](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/batch_cli.py)
- [缓存](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/native_cache.py)
- [文档格式与检查](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/document_format.py)
- [文档组装](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/document_bundle.py)
- [修订应用](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/document_review.py)
- [重导出](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/document_reexport.py)
- [主CLI](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/src/mp4_analysis/thin/cli.py)
- Python str.split无参数时处理所有空白：[官方说明](https://docs.python.org/3/library/stdtypes.html#str.split)。
- Pandoc提供现成结构转换，但官方不保证所有格式无损互转：[官方手册](https://pandoc.org/MANUAL.html)。本项目的R1损失发生在调用Pandoc前，不应归咎于Pandoc。
