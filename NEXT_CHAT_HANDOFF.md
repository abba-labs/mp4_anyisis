# 当前交接：R1—R6 针对性回归与全量回归已通过，截图批次运行已验证

更新：2026-10-01。
**当前状态：LOCAL_REGRESSION_PASSED_BATCH_VERIFIED。**
已在本地环境（Windows 11, Python 3.13.7）连续完成拉取、针对性用例运行、全量回归、真实 61 张截图 ROI 准备与批次运行验证。全部测试证据和源文件前后哈希一致性证明均已归档。

## 1. 最新测试证据与入口

* **最新测试报告**：**[docs/screenshot_runs/20261001_191329_windows_local/TEST_REPORT.md](docs/screenshot_runs/20261001_191329_windows_local/TEST_REPORT.md)**
* **完整交付规程**：[docs/SCREENSHOT_FIX_DELIVERY_20261001.md](docs/SCREENSHOT_FIX_DELIVERY_20261001.md)
* **测试基线 Commit**：`3c13a56658097ce93fc72ea024225beaa1e02dc4`
* **工作分支**：`feat/open-source-thin-pipeline-20260928`（草稿 PR #3）

## 2. 实测验证通过清单 (R1—R6)

1. **针对性修复测试（`tests/test_screenshot_review_fixes.py`）**：
   * **20 / 20 全部通过（100% PASS，耗时 0.75s）**
   * R1（语义表格/上下标保护与回退）、R2a/b/c（严格空格/换行/Word嵌入图片关系/Excel跨度与位置校验）、R3（逐组失败隔离）、R4（多批次复核覆盖累积与失效）、R5（导出目录受保护）、R6（准备耗时与查缓存分离计量）全部在本地严格验证通过。
2. **仓库全量回归（`pytest -q`）**：
   * **130 passed, 8 skipped（0 failed，耗时 3.91s）**。
3. **真实 61 张截图 ROI 裁图与批次准备（`examples/screenshot_collection.json`）**：
   * 真实坐标 `[71, 140, 1849, 958]` 准确排除窗口标题栏与任务栏；
   * `efc_detail`（34张）与 `efc_lrs`（27张）共 61 张图片裁图 100% 就绪（0 failed）；
   * 生成 `approval_id`：`135d040865d8b531b8fae8859f1bd4a92c276e243e72bdc377263475d626cb1c`。
4. **源文件安全逐字节验证**：
   * 61 张截图 PNG + 2 个 manifest.json 在批次运行前后分别校验 SHA256，**逐字节 100% 一致，无写污染**。
5. **真实批次执行（`batch_cli run`）**：
   * 墙钟耗时：12.0650s；精准记录 `initial_prepare_seconds`（6.6493s）与 `document_execution_seconds`（5.2433s）；
   * 本地 Windows 宿主未装 PaddleOCR 时，首张失败后组内后续 33 张图安全标为 `BLOCKED`，组 2 优雅处理未崩溃，返回受控 `PARTIAL_FAILURE`，验证了 R3 故障隔离机制。


## 2. 六类补丁的真实内容

| ID | 已修改代码 | 本地验证重点 |
|---|---|---|
| R1 | document_format拒绝不能保真转换的sup/sub/s等语义标记；document_bundle保留区域图片并记录unsupported_table | 不再把10的三次方静默转成103；图片回退不计为可编辑表格恢复 |
| R2 | 新document_checks按有序文字块、字间空格、图片关系/像素身份、候选声明span与实际XLSX核对；document_format接入转换前后检查 | 缺空格、段落粘连、缺图/换图、空合并格/跨度/位置变化应报警；不把声明结构当源结构准确 |
| R3 | batch_cli不因普通输入目录缺失在load_plan阶段整体退出；资源失败留给逐组准备 | 缺失组失败，可用组继续；非法计划和危险路径仍全局拒绝 |
| R4 | document_review按证据图与单元内容hash累计coverage；唯一当前pending、独立历史；修改影响已有覆盖时失效 | e1后e2覆盖累计，补查后pending退出；critical未决不自动关闭 |
| R5 | 公共build核对原截图与整个单文档OCR项目隔离，校验项目owner；新候选记录source_protection，apply/reexport继承 | 不向原图树/受管理OCR树写派生成品；集合deliveries兄弟目录保持可用 |
| R6 | pipeline与集合execute在准备前计时，记录不重叠阶段；CLI补当前命令时间字段 | 准备开销计入；嵌套明细不重复累计；缓存native.timings仍为历史；进程启动另用外层墙钟 |

这次没有更换PaddleOCR/PaddleX、没有新模型服务、没有自研OCR或图像表格求解器。新校验只解释候选已有的显式span，不从图像推断或修补网格。

注意：已被旧版压平的content.json不能通过reexport自动找回上标等语义。应使用保存的原生JSON重新build新候选，不需要重跑OCR。新交付身份包含document_checks.py，旧校验结果不会冒充新导出验证。旧包缺失来源保护字段时，先用新build重建后再修订。

## 3. 本地一次连续完成的工作

完整命令、依赖、R1—R6通过条件、恢复/失败注入方法和最终报告要求都在交付文档中。复用现有Python 3.10—3.12虚拟环境及模型缓存，不重建环境。

```bash
python -m pytest -q tests/test_screenshot_review_fixes.py
python -m pytest -q
```

先记录针对性与全量回归的真实结果，不用历史通过数代替。随后为现有34张详细设计、27张LRS确认真实ROI；已有配置直接复用：

```bash
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
# 检查两组全部裁图，使用本次真实完整approval_id。
python -u -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

只处理指定文档区域，不用full-image绕过未知整屏边界。截图数不等于原文页数；批量输出、缓存恢复、模型修订、Word/Excel实物一致性和内容抽检分开报告。不得凭文件存在、模型自评或导出返回码给内容PASS。

本地按交付文档连续验证后，把报告、运行日志、实际文件及来源、用量/计时和失败明细提交到`docs/screenshot_runs/<新RUN_ID>/`，并更新本交接。遇普通代码缺陷直接保留复现与修复证据，不重新规划架构，也不重新排查旧视频样本。

## 4. 仍有的范围限制

- 所有代码补丁和新用例均未由ChatGPT运行；真实效果待本地验证。本次无新的准确率、速度、费用或内容通过数。
- 不自动跨截图去重、推断原始分页、跨图拼表或生成式去水印。上游格式不支持时有显式区域图片回退，而非承诺全部表格可编辑。
- 模型仍是本地已有获准看图能力读取任务并返回差异，不是自动部署或调用新视觉服务。coverage是有身份的已阅声明，不等于独立内容验收。
- `screenshots.py`曾被拦截的更新本轮没有重试，该文件仍保持原版本；批次64位hash路径未缩短，Windows选择短输出根。
- 历史视频工作流未迁移、未修改或运行；不能据旧CI配置宣传截图版已测试通过。
- 原图、原native、旧候选、失败记录不覆盖；不读取或提交凭据；不自动清锁或强推。

第1—3轮功能入口仍可参考README、docs/SCREENSHOT_BATCH_RUN.md和docs/SCREENSHOT_DOCUMENT_OUTPUT.md；与本次修复的计时/覆盖/校验说明不一致时，以本文和新交付文档为准。
