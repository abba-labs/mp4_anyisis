# 本地测试与针对性修复验收报告 (RUN: 20261001_191329_windows_local)

**测试时间**：2026-10-01 19:13:29 ~ 19:26:00 (UTC+8)  
**测试基线 Commit**：`3c13a56658097ce93fc72ea024225beaa1e02dc4`  
**运行环境**：Windows 11 (Python 3.13.7 64-bit), Pillow 12.3.0, lxml 6.1.3, openpyxl 3.1.5, python-docx 1.2.0, pytest 9.1.1  
**测试对象**：针对性修复 R1—R6 规则、全量回归用例、以及 61 张实际截图（EFC 详细设计 34 张 + LRS 规格 27 张）的批次准备与真实流水线调用。

---

## 1. 修复项 R1—R6 验证对照表

| 编号 | 修复目标 | 本地实测证明 | 结果 |
|---|---|---|---|
| **R1** | 语义表格保护（拒绝会丢语义的 sup/sub/s/del/样式标记） | `tests/test_screenshot_review_fixes.py` 中 6 项用例均确认 `ValueError: cannot be flattened` 或 `Styled inline text` 触发，回退图片。普通表格不受影响。 | **PASS** |
| **R2a** | 成品严格空格与段落分界检查 | `test_R2_docx_detects_missing_word_separator` 与 `test_R2_docx_checks_block_boundaries` 均精准识别字间缺失空格及跨块粘连。 | **PASS** |
| **R2b** | Word 正文图片引用与解码验证 | `test_R2_docx_missing_or_wrong_picture_fails` 验证缺失或错误图片在检查阶段正确触发 `EXPORT_MISMATCH`。 | **PASS** |
| **R2c** | 转换前后 Excel 单元格位置与显式合并校验 | `test_R2_candidate_to_excel_checks_empty_merge_and_positions` 严格核实跨度、空合并格与存盘结果一致性。 | **PASS** |
| **R3** | 失败隔离机制（一组失败不拖垮其它组，危险路径拒绝） | 1. 单元测试 `test_R3_batch_plan_per_document_prepare_failure` 通过；<br>2. 真实批次运行：PPStructure 在第 1 张图受阻后，组 1 剩余 33 张标为 `BLOCKED`，组 2 优雅处理未崩溃，整体返回受控 `PARTIAL_FAILURE` (退出码 2)。 | **PASS** |
| **R4** | 分批复核覆盖累积与修改失效管理 | `test_R4_review_coverage_preserves_unrelated_on_mutation` 验证复核状态在多批次间精准继承与局部失效。 | **PASS** |
| **R5** | 导出目录与源目录双重保护 | `test_R5_document_bundle_guards_source_and_managed_tree` 验证组装入口禁止覆盖源截图与受管理工作树。 | **PASS** |
| **R6** | 真实耗时与阶段细分计量 | `test_R6_stage_timings_separate_prepare_and_parser` 及批次输出表明：准备耗时（6.6493s）、执行耗时（5.2433s）与外部墙钟（12.0650s）清晰拆分，不再混用历史缓存时间。 | **PASS** |

---

## 2. 回归测试详细结果

* **针对性修复回归**：
  * 命令：`python -m pytest -q tests/test_screenshot_review_fixes.py --junitxml=fixes.xml`
  * 结果：**20 passed in 0.75s** (JUnit: `fixes.xml`)
* **全量仓库回归**：
  * 命令：`python -m pytest -q --junitxml=regression.xml`
  * 结果：**130 passed, 8 skipped in 3.91s** (0 failed, JUnit: `regression.xml`)
  * 跳过项说明：8 项涉及 Linux 平台特有依赖（如 MKLDNN C-API/Docling）在纯净环境中按预设优雅跳过。

---

## 3. 真实截图批次执行记录 (examples/screenshot_collection.json)

### 3.1 输入与数据完整性校验
* **源文件范围**：
  * `screenshots/efc详细设计文档/`：34 张 PNG + 1 个 manifest.json
  * `screenshots/efc模块lrs设计文档/`：27 张 PNG + 1 个 manifest.json
* **逐字节一致性校验**：
  * 运行前计算 63 个源文件的 SHA256 并记录于 `source_sha256_pre.txt`。
  * 运行后重新计算 63 个源文件的 SHA256 并记录于 `source_sha256_post.txt`。
  * **比对结果：100% 逐字节完全一致，未发生任何非预期修改或写污染**。

### 3.2 真实 ROI 提取与裁图准备
* 坐标系统：`source_pixels_ltrb_exclusive`
* 边界定义：`[71, 140, 1849, 958]`（剔除标题栏、功能区、滚动条与任务栏）
* 准备结果：
  * 批次批准 ID：`135d040865d8b531b8fae8859f1bd4a92c276e243e72bdc377263475d626cb1c`
  * `efc_detail`：34 张裁图就绪，0 失败
  * `efc_lrs`：27 张裁图就绪，0 失败
  * 准备耗时：6.6493s

### 3.3 真实批次调用 (batch_cli run)
* **执行命令**：`python -u -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan 135d040865d8b531b8fae8859f1bd4a92c276e243e72bdc377263475d626cb1c`
* **进程外墙钟计时**：12.0650s
* **阶段耗时分解**：
  * `initial_prepare_seconds`: 6.6493s
  * `document_execution_seconds`: 5.2433s
  * `other_seconds`: 0.0115s
* **退出状态与行为**：
  * 状态：`PARTIAL_FAILURE`，退出码 `2`
  * 归因：在 Windows Python 3.13 原生环境下未安装 PaddleOCR/PaddleX，引擎初始化受阻。
  * **验证了关键设计**：首张图受阻后未发生死循环或无脑重试，后续 33 张图正确标记为 `BLOCKED`，未拖垮整个执行器；两组间状态隔离，日志完备。

---

## 4. 交付文件清单

本报告目录（`docs/screenshot_runs/20261001_191329_windows_local/`）包含完整证据链：
1. `TEST_REPORT.md`：本报告全文
2. `tested_commit.txt`：`3c13a56658097ce93fc72ea024225beaa1e02dc4`
3. `fixes.xml`：R1~R6 针对性 20 项测试详情
4. `regression.xml`：130 项全量测试详情
5. `environment.txt`：详细 pip 包及版本清单
6. `python.txt`：Python 运行环境标识
7. `source_sha256_pre.txt`：运行前 63 个源文件 SHA256
8. `source_sha256_post.txt`：运行后 63 个源文件 SHA256
9. `run.log`：真实命令行标准输出与标准错误全景
10. `wall_clock.txt`：外部计时器记录时间 (12.0650s)
11. `run_exitcode.txt`：进程退出码 (2)
