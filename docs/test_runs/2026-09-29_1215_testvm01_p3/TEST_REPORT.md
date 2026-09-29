# 2950 帧 PP-Structure 重组丢字：根因确认与最小修复验证（P0-followup）

- RUN_ID（本报告）: `2026-09-29_1215_testvm01_p3`
- 日期: 2026-09-29（CST）
- 分支: `feat/open-source-thin-pipeline-20260928`
- 状态: **根因已用同次调用轨迹确认，最小修复已验证**

## 1. 结论

1. **根因确认**：2950 帧 LIMIT.08 首行丢失不是识别问题，而是上游
`paddlex==3.7.2` 的 PP-StructureV3 重组函数
`_LayoutParsingPipelineV2.standardized_data` 中 "hurdles" 循环
（`pipeline_v2.py:427`）把**旁观者行**的文字置空且从不恢复。
同次调用轨迹（p0，10 个写入事件）完整复现了历史症状。
2. **最小修复**：仓库新增版本限定的进程内 guard
（`src/mp4_analysis/thin/_layout_parsing_patch.py`），只拦截 hurdles
置空对旁观者行（`ocr_idx!= overall_ocr_idx`）的写入；跨栏行自身的
置空/替换/追加原样放行。不改模型、不改上游源码、不按帧/关键字特判、
不手工补字。
3. **验证**：同一 2950 输入，修复前 `idx=6 score=0.9919 text=''`，
修复后同框同分同索引 `text='LRS.SARC.LIMIT.SPECADC数字控制器的使能信号需要早于控制器内的'`；
guard 在同次调用中精确拦截了 p0 轨迹里的 3 次旁观者置空；
2920 邻帧回归零拦截（行为与未修复一致）；Word 实读+渲染确认首行回到正文。

## 2. 固定环境

- Python 3.11.16（uv 独立构建，复用 `.venv-test`）
- `paddleocr==3.7.0` / `paddlex==3.7.2` / `paddlepaddle==3.2.2`
- `opencv-contrib-python==4.10.0.84` / `av==16.0.1` / `python-docx==1.2.0`
- `numpy==2.3.5` / `pillow==12.3.0`，`pip check` 通过
- 输入：`work/test_machine_baseline/restored/sarc/frames/frame_00002950.png`
SHA256 `d2fe16ef0d8c919e3ed9d48cce4d9920f3e95c420a26bc5e1a28802953b86770`
- 配置：`NativeParser(device="cpu", threads=2, mkldnn=True, table_mode="default", ocr_models="mobile")`
- `no_proxy/NO_PROXY=localhost,127.0.0.1`（已收敛）

## 3. 根因：hurdles 循环误伤旁观者行（同次轨迹确认）

上游逻辑（`pipeline_v2.py` 约 400–476 行）：当一行 OCR 横跨多个版面框，
对每个相交裁剪区先把**所有**与裁剪区交叠 IoU>0.8 的 OCR 行文字置空
（第 427 行），再对裁剪图重识别；只有跨栏行自身会被替换/追加恢复，
旁观者行永不恢复。

p0 同次观测（`docs/test_runs/2026-09-29_1055_testvm01_p0/trace/trace_events.json`，
10 个事件）的关键序列：

| # | 位置 | 动作 |
|---|------|------|
| 1 |:427 | 跨栏行 idx8（box `[212,166,361,266]`）处理版面框 3，裁剪区 `[212,166,361,169.3]`；**旁观者 idx6（首行，IoU 0.901）被置空** |
| 2 |:455 | idx8 被裁剪重识别替换为 `"——"`（149×3px 细条，分数 0.602，垃圾） |
| 3 |:427 | 同一跨栏行处理版面框 7；**旁观者 idx10（`2022年12月22日`，IoU 1.0）被置空** |
| 4 |:469 | 第二裁剪区重识别为空，追加空条目 |
| 5 |:427 | 跨栏行 idx9（box `[567,162,714,262]`）处理版面框 3；**idx6 再次被置空（IoU 0.955）** |
| 6 |:455 | idx9 被替换为 `"上"`（147×7px 细条，分数 0.606，垃圾） |
| 7–8 |:469/:509 | 追加空条目；版面框回退重识别把 `2022年12月22日` 追加回来（idx50） |

最终 `overall_ocr_res`：`idx=6 score=0.9919 box=[197,146,1082,169] text=''`
——与历史问题报告的签名（框/分保留、文字为空）完全一致；md 里首行缺失、
续行 `其他使能信号（比如vcen等）打开；` 保留为孤立片段。

## 4. 最小修复

新增 `src/mp4_analysis/thin/_layout_parsing_patch.py`：

- 进程内包装 `_LayoutParsingPipelineV2.standardized_data`（与 paddleocr
自身 `_patch_layout_parsing` 同模式），调用期间把
`overall_ocr_res["rec_texts"]` 换成 `_GuardedRecTexts`，调用结束换回普通 list。
- `_GuardedRecTexts.__setitem__` 仅当以下**全部**成立时否决写入（保留原文）：
写入值 `""`、调用方为 `standardized_data`、写入目标是循环变量
（`index == ocr_idx`，以此区分:427 置空点和:455 替换点）、
且 `ocr_idx!= overall_ocr_idx`（旁观者，非跨栏行自身）。
- **版本限定**：仅当 `paddlex==3.7.2` 时生效，否则记 warning 跳过；
幂等；`get_last_guard_report()` 供诊断读取每次调用的否决明细。
- `NativeParser.__init__` 中惰性安装（`import` 失败/版本不符不崩），
安装状态计入 `fingerprint`（`bystander_guard`），旧缓存自动失效。

约束遵守情况：未修改 site-packages；未换模型；未按 frame/index/文字特判；
未手工补 LIMIT.08；未从验收文本生成输出；未重写 OCR/版面引擎。

## 5. 验证

### 5.1 同图修复前后对比（p0 broken vs p3 fixed）

| 检查项 | 修复前（p0） | 修复后（p3） |
|---|---|---|
| `overall_ocr_res` idx6（box `[197,146,1082,169]`，score 0.9919） | `text=''` | `text='LRS.SARC.LIMIT.SPECADC数字控制器的使能信号需要早于控制器内的'` |
| 首行核心子串在 md | 否 | **是** |
| 续行 `其他使能信号` 在 md | 是（孤立） | 是 |
| 首行核心子串在 `overall_ocr_res` 出现次数 | 0 | 1（无重复） |
| 入口→出口被置空行数 | 2（idx6、idx10） | 0 |

### 5.2 guard 拦截明细（p3，`trace/guard_report.json`）

9 个写入事件，**否决 3 次**，与 p0 轨迹的旁观者置空一一对应：

- `idx=6` 首行 ×2（两次被不同跨栏行的裁剪区误伤）
- `idx=10` `2022年12月22日` ×1

跨栏行自身的置空/替换/追加（`——`/`上`/空条目）全部放行——那是上游既有
行为（见 §6），本次不碰。

### 5.3 2920 邻帧回归（`2026-09-29_1215_testvm01_2920/`）

- 同配置跑 2920：`errors=[]`，LIMIT.01–08 八条全在 md，无丢失。
- guard 上报：3 个事件，**否决 0 次** → 本帧无旁观者误伤，修复前后行为一致。
- 唯一入口→出口置空：idx14 时间戳水印 `26-09-27-20:14`（跨栏行自身路径，
guard 不干预；与修复无关，属上游既有行为）。

### 5.4 Word 生成与实读/渲染校验（p2 `word_2950/`）

- `NativeParser.parse(word=True)`：`errors=[]`，生成 `frame_00002950.docx`。
- python-docx 实读：8 段；首行核心子串 ✓；续行 ✓；
`LIMIT.SPEC` 出现 1 次（无重复）。
- libreoffice 转 PDF + pdftoppm 渲染首頁確認：
`LRS.SARC.LIMIT.SPECADC数字控制器的使能信号需要早于控制器内的——上`
位于正文正确位置（07 条之后、日期之前）。见 `word_2950/render/page-1.png`。

### 5.5 单测与回归

- 新增 `tests/test_hurdle_bystander_patch.py`（9 项，无模型）：
旁观者否决、跨栏行自身放行、替换点（含空裁剪文本）放行、非
`standardized_data` 调用方放行、numpy 索引转 int 且上报 JSON 可序列化、
版本限定/幂等/版本不符跳过。
- 全量：`168 passed, 7 skipped`（7 skipped 为既有跳过）。

## 6. 已知遗留（非本次范围，上游既有行为）

- md/Word 里首行后粘着 `——上`：上游 hurdles 对 3–7px 高的细长裁剪条
重识别产生的垃圾（`——` 0.602 / `上` 0.606），修复前已存在。
消除它需要改写上游 hurdles 重识别策略，超出“最小修复”范围，另行评估。

## 7. 运行目录索引

- `2026-09-29_1055_testvm01_p0/` — broken 基线：同次轨迹 10 事件、
`text=''` 的最终 JSON（根因证据）
- `2026-09-29_1205_testvm01_p1/` — fixed 首次验证（JSON/md 正确；
超大快照已清理，guard 明细缺失为诊断脚本时序 bug，p3 已补齐）
- `2026-09-29_1215_testvm01_p2/` — fixed 中间尝试（int64 序列化问题已修；
含 `word_2950/`：docx/pdf/渲染 png）
- `2026-09-29_1215_testvm01_p3/` — **fixed 完整验证**（本报告主体：
guard_report.json、裁剪快照、trace_analysis.json）
- `2026-09-29_1215_testvm01_2920/` — 2920 邻帧回归
- 诊断脚本：`work/p0_2950_observe/observe_2950.py`
（`P0_RUN_ID`/`P0_FRAME`/`P0_EXPECTED_SHA`/`P0_GUARD_ONLY` 环境变量控制）

## 8. 复现命令

```bash
cd ~/workspace/repos/mp4_anyisis
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONUNBUFFERED=1 \
PADDLE_PDX_MODEL_SOURCE=HF no_proxy=localhost,127.0.0.1 NO_PROXY=localhost,127.0.0.1
# 修复验证（2950）
P0_GUARD_ONLY=1 P0_RUN_ID=<新RUN_ID> P0_FRAME=2950 \
.venv-test/bin/python work/p0_2950_observe/observe_2950.py
# 单测
.venv-test/bin/python -m pytest tests/ -q
```
