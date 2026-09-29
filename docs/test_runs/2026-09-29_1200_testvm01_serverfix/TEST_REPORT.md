# TEST_REPORT: 2.4 约束章节 server 对照与 Word 交付

**RUN**: `2026-09-29_1200_testvm01_serverfix`
**日期**: 2026-09-29
**任务包**: A（约束章节闭环）

## 目标

1. 运行 server 识别器对照，验证第07条 `vcen` 下划线与第01条标点问题是否可解
2. 生成 2.4 约束说明 Word（8 条完整）
3. 逐条核对并记录真实通过/失败

## 执行步骤

### 1. Server 识别探针（mobile-det + server-rec）

- 脚本：`scripts/probe_saved_text_recognition.py`
- 输入：2920/2950（SHA256 已校验）
- 结果目录：`docs/test_runs/2026-09-29_1140_testvm01_server_rec/`
- **结论**：
  - 01条标点：server 修复（`：`→`；`），与源图一致
  - 07条 `vcen`：server 仍失败（无下划线）
  - 08条首行：server 识别完整

### 2. Server 全量流水线（server-det + server-rec）

- 配置：`NativeParser(ocr_models='server')`，含旁观者保护
- 输出：`native_2920/`, `native_2950/`
- **结论**：不如 mobile-det + server-rec
  - 01条仍为 `：`（检测框差异导致）
  - 06条出现 `huaTMCU`（比 mobile 的 `ETNCU` 更差）
  - 08条碎片化更严重
- **决策**：最终 Word 采用 mobile 全量输出（已验证旁观者保护）

### 3. 源图目视验证

- 01条源图：`；`清晰可见（`/tmp/punct_check4.png`）
- 07条源图：`vc_en` 下划线清晰可见（`/tmp/vcen_check3.png`）
- **结论**：两处均为模型识别局限，非源图质量问题

### 4. 2.4 Word 生成

- 输出：`word_24/section_2_4_constraints.docx`
- 来源：2920（01-07）+ 2950（08），mobile 全量 + 旁观者保护
- 派生清理（有证据，见核对记录）：
  - 08条 `——上`（hurdles 垃圾，score 0.60/0.61）
  - 08条 `2022年12月22日`（日期污染）
  - 05条时间戳污染
  - 独立水印/时间戳行
- 未改写：`vcen`（未手工补字）、01条 `：`（未改写）、06条 `ETNCU`（已标注）

## 8条核对结果

| 条款 | 状态 | 说明 |
|------|------|------|
| 01 | FAIL（已知） | 源图`；`，识别为`：`；探针证实 server-rec 可修复，未经全量验证 |
| 02 | PASS | 与期望完全一致 |
| 03 | PASS | 与期望完全一致 |
| 04 | PASS | 与期望完全一致 |
| 05 | PASS（清理后） | 时间戳污染已排除，正文完整 |
| 06 | FAIL（已知） | 水印`ETNCU`嵌入，已标注未改写 |
| 07 | FAIL（已知） | `vcen`下划线缺失，双模型均失败，源图可见 |
| 08 | PASS（清理后） | 首行恢复，`——上`/日期已排除，续行核对；`vcen`同07 |

**完全通过**：3/8（02, 03, 04）
**清理后通过**：2/8（05, 08）
**已知失败**：3/8（01, 06, 07）

## 残留风险

1. 01条标点：需验证 mobile-det + server-rec 全量组合（未做）
2. 06条水印嵌入：需位置证据的精细排除（未做）
3. 07/08条 `vc_en`：模型能力缺口，无开源方案（需用户决策是否接受）

## 文件清单

- `native_2920/`：server 全量输出（2920）
- `native_2950/`：server 全量输出（2950）
- `word_24/section_2_4_constraints.docx`：2.4 Word
- `word_24/section_2_4_constraints.pdf`：渲染 PDF
- `word_24/page-1.png`：渲染检查图
- `TEST_REPORT.md`：本报告
