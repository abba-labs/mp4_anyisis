# 当前交接：截图指定区域开发，第2轮代码已提交

更新：2026-10-01。用户要求由ChatGPT直接开发，三轮收敛；**测试、真实OCR、模型调用和成品验收留给本地，本轮不执行。** 不把小开发再下发给本地，也不恢复局部标点／旧视频实验。

仓库：abba-labs/mp4_anyisis；工作分支：feat/open-source-thin-pipeline-20260928；PR #3保持草稿。本轮进入head为`d3f22ead7a69eadac496d58c5758c5dbe774495b`。本轮源码、接口与README截至`a2fcbf47f571977e6b9739770af775cd664d1a3e`，随后为本交接提交。继续前重新查询实际head，避免覆盖其他修改。main保持不动、不强推、不自动合并或修改PR元数据。

**本轮没有运行测试、GUI、OCR、视觉模型、Word/Excel生成或渲染。** 所有提交标skip-ci，未修改/手动触发工作流。状态是“实现已落库，运行效果未验证”，没有新的准确率、速度或61张内容通过数。

## 1. 两轮已经编码的能力

| 范围 | 当前代码状态 |
|---|---|
| 显式文档区域 | OpenCV现成选框，Pillow批量裁剪，整组默认/单图覆盖，预览确认；缺配置/越界不退回整屏 |
| 输入可靠性 | 源manifest顺序、源hash/ROI/裁图hash身份、批次批准、原图不改；OCR只读已确认裁图 |
| OCR运行 | 复用现有PP-StructureV3；逐图状态、成功缓存、失败尝试和未处理项保留 |
| 整份文档组织（本轮） | 按已保存run/report及native块列表生成冻结content.json、整份HTML/Word、HTML块Markdown、表格集与图片集 |
| 成熟导出复用（本轮） | Word用已有Pandoc 3.1.11.1；Excel用PaddleX 3.7.2自身tablepyxl转换器，不自写网格求解；openpyxl用于文字类型、基本格式及回读 |
| 稳定模型任务（本轮） | review_tasks.json提供block/cell/evidence ID、原值/hash和仅文档裁图；不初始化或调用视觉模型 |
| 修订应用（本轮） | 从外部JSON导入意见，核对候选版本、原值/hash、来源及bbox；明确批准整份响应hash后写独立新版本 |
| 修订操作（本轮） | 文字/单元格文字替换、有证据的漏段插入、派生正文叠加文字排除；表结构/图像只能标未决，不随意改变跨度/生成补图 |
| 实物一致性（本轮编码） | Word回读正文/物理单元格，Excel转换与存盘前后比较；记录EXPORT_MISMATCH/EXPORT_ERROR，不以文件存在产生PASS |
| 自包含来源与版本（本轮） | bundle.json封装文件哈希；相对路径图像均来自批准裁图；原生目录不写入，旧候选不覆盖，新版本有父包身份/完整差异 |

两组源截图仍为34张详细设计、27张LRS，共61张；图片数不等于原始完整页数。本轮没有更改输入集合或原始证据。

## 2. 新增和修改的代码

新增输出层文件（不是新增逻辑平台）：

- `src/mp4_analysis/thin/document_format.py`：安全表格HTML/文字提取，HTML呈现，Pandoc及上游Excel转换，实际文件一致性检查。
- `src/mp4_analysis/thin/document_bundle.py`：读取批准run、验证来源、按顺序组织内容、仅裁图证据、稳定任务与包哈希。
- `src/mp4_analysis/thin/document_review.py`：复核JSON读取、重复键/版本/来源/前置值/操作校验，批准响应后生成独立reviewed包。
- `src/mp4_analysis/thin/document_cli.py`：`build`、`inspect-review`、`apply`入口，不进行OCR。

修改：

- `cli.py`增加`--document-output`及可选禁用Office格式开关；OCR成功后最终统一组织文档，不要求逐图`--word`。
- `pyproject.toml`增加`screenshot-document`命令和明确的`document`IO依赖；PyAV未重新引入。
- README更新为两轮实际接口；详细说明见`docs/SCREENSHOT_DOCUMENT_OUTPUT.md`。

第1轮`screenshots.py`、`utils.py`、`pipeline.py`和现有NativeParser继续复用，本轮未重新设计框架。

## 3. 已编码入口（留给本地执行，未在本轮运行）

先按README为每份截图目录选区域、准备全部裁图预览，取得准确approval_id。ROI仍使用原图[left,top,right,bottom]，右下不含。不同布局需覆盖，不预填未经确认的61张坐标。

```bash
# OCR完成后，在最后生成整文档包；一般不需要--word逐截图导出。
python -m mp4_analysis.thin.cli screenshots/efc详细设计文档 -o work/efc_ocr --roi-config work/regions/efc.json --accept-crops APPROVAL_ID --document-output work/deliveries/efc_tool_v1

# 已有OCR结果，直接组织文档，不重新识别。
python -m mp4_analysis.thin.document_cli build RUN_DIRECTORY -o work/deliveries/efc_tool_v1

# 本地获准看图模型填写真实差异文件后，查看hash/数量。
python -m mp4_analysis.thin.document_cli inspect-review work/reviews/efc_changes.json

# 一次批准整个响应，生成新的reviewed稿并重导出；不改原native或初稿。
python -m mp4_analysis.thin.document_cli apply work/deliveries/efc_tool_v1 work/reviews/efc_changes.json -o work/deliveries/efc_reviewed_v1 --accept-changes RESPONSE_SHA256
```

RUN_DIRECTORY取现有OCR打印的run_directory或latest_result.json。文档输出必须是新的独立目录；不直接复用已有v1。Word/Excel失败仍保留HTML/content/错误记录，CLI返回2；明确只要基础格式时使用document_cli的`--no-docx --no-xlsx`。

主OCR命令遇部分失败时保留运行并退出；可以用独立build命令从该run生成带缺口的候选，不先重跑成功页面。输入失败、识别未完成或不支持的结构明确进入unresolved；原图回退不算可编辑内容识别成功。

任务内容、操作JSON样例、回读界限和字段解释集中在`docs/SCREENSHOT_DOCUMENT_OUTPUT.md`，不重读整段历史。

## 4. 区域和准确性边界

所有模型证据是批准的文档裁图；图像块也仅从这些裁图的合法bbox裁出。文档包不包含原始整屏图片。模型返回只当数据，不执行其指令，不外发到新服务，不读取/打印凭据。

稳定cell ID基于原生HTML物理单元格，并非重新求解出来的网格。复核任务中cell bbox精度为表格区域，不伪造精确单元格框。模型不能通过导入文件直接更改rowspan/colspan、任意删除图表或把图形补画完整。

关键字段修改保留待源验收项，独立读取记录只是附带证据，代码不声称已证实新上下文的实际执行。程序从不据格式正确、模型自信或两次回答相同自动设置内容PASS。

Word回读比较保留标点、下划线和大小写，但忽略排版空白；Excel存盘前后坐标/值/类型/合并比较不等于源表正确。HTML转表非空文字也检查，空格几何不靠猜测补足。版式、图片完整性及所有61张真实OCR仍由本地验证。

当前按截图顺序及native块列表组织，不自动推断原始分页、不作模糊相似度去重、不跨图硬合并表格。复杂表格用原图回退并保留问题，不能把候选文件生成当全部内容恢复。

## 5. 第3轮剩余固定范围（由ChatGPT直接继续实现）

1. **多文档批量入口和统一产物索引。** 两组或多组截图各自ROI与输出，顺序执行并独立记录失败，不默默混合来源。
2. **增量和断点恢复。** 新批次里未变页面可按完整输入/模型/代码身份复用已成功OCR；失败、改变ROI/源图及导出重试保留旧尝试，不能以旧缓存冒充新运行。
3. **运行目录、短路径和来源边界收尾。** 统一裁图/OCR/文档/修订入口的身份与冲突规则，缩短Windows深路径；确认目录和响应文件不会覆盖用户原图。
4. **整包交付说明与迁移残留清单。** 最终给本地明确连续执行命令、未运行验证项、源码/交接位置。测试不由ChatGPT运行，不再用新方案和测试数替代实现。

保留两轮已实现接口，不扩张为自动识别任意窗口、截图软件、OCR模型训练、表格求解器、数据库、队列或Agent平台。旧视频相关工作流迁移仍属此前未获准修改的范围，本轮不擅自改变权限或工作流；在交付清单明确列出，而非宣称CI全部迁移通过。

## 6. Git和本次交付事实

本轮仅改源代码、依赖声明、README、输出使用说明和本交接；没有测试报告、模型返回或真实Office成品。提交信息带skip-ci。不以库文档支持某功能冒充本项目已实测。

开始/提交前核对远端实际head，只改本轮文件，冲突时先读新内容再整合。main与PR元数据不改，不强推，不删除旧原生证据、失败报告或未验收成品。历史第1轮完整交接保留在d3f22ead7a69eadac496d58c5758c5dbe774495b。

**下一轮直接完成第3轮开发收尾，不重新询问需求，不把实现工作转回本地。**
