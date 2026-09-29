# 测试报告：2920 / 2950 两帧 mobile GeneralOCR 实测与重组前后对照

- 运行 ID：`2026-09-29_1018_testvm01`
- 日期：2026-09-29（CST）
- 分支：`feat/open-source-thin-pipeline-20260928`（基线 commit `3d1e2df`）
- 依据：`docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md` §测试目标与验收口径

## 结论先行

1. **帧 2920 LIMIT.07 的两处 `vc_en`→`vcen`：不是重组引入的。** 本次实测的首轮 GeneralOCR（raw）里已经是 `vcen`
   （两处分数 0.989 / 0.980），存量 `overall_ocr_res` 原样保留，重组未改动。这是首次 OCR 的识别结果，不是重组改写。
2. **帧 2950 LIMIT.08 首行丢失：发生在重组/后处理阶段，不是首次 OCR 识别失败。** 同模型、同参数、同输入 PNG 下，
   本次实测 raw 在框 `[197,146,1082,169]` 以分数 0.992 正确识别出
   `LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的`；
   而存量 `overall_ocr_res` 同框分数 0.9919、文字却被置空；重组后的 markdown 里整条 LIMIT.08 缺失。
   识别本身是对的，文字是在重组阶段丢的。
3. **帧 2950 LIMIT.07 续行缺“行”字（`进配置`）：** raw 里已经缺字（s=0.981），属首次 OCR 问题，重组未改动。
4. 2920 的 LIMIT.05—08、2950 的 LIMIT.07：raw 与存量文字逐字一致，重组仅做了按阅读顺序合并行，
   附带把水印碎片（ETNCU/BTMCU/ETMC/CTWCU、日期串）并入了条款段落，未丢失条款文字。
5. 本次只跑了 mobile recognizer（2 帧实测通过），按交接文档“只有证据需要时才跑 server”，不盲跑。

## 运行信息

- 输入：工件 `full-recording-resumed-validation`（Actions run `36439891744` / artifact `10978920126`，
  未过期，ZIP SHA256 与交接文档一致），解压于 `work/test_machine_baseline/restored/sarc`；
  两帧 PNG SHA256 与交接文档一致；57 项基线 `report.json`（57 完成、0 待处理）未动。
- 本次运行目录（机器侧）：`work/test_machine_mobile_01`（唯一新目录，未覆盖旧目录）。
- Python：3.11.16（uv 官方 standalone 构建；Ubuntu 24.04 apt 源无 python3.11，
  与原环境补丁版本 3.11.16 一致，差异已记录）。
- 虚拟环境：`.venv-test`，约束 `work/test_machine_baseline/constraints_linux_py311.txt`（104 条 pin），
  `pip check` 通过。关键版本：paddleocr 3.7.0、paddlex 3.7.2、paddlepaddle 3.2.2、
  opencv-contrib-python 4.10.0.84、av 16.0.1、python-docx 1.2.0、numpy 2.3.5、pillow 12.3.0。
- 环境变量：`OMP_NUM_THREADS=1`、`OPENBLAS_NUM_THREADS=1`、`PYTHONUNBUFFERED=1`、`PADDLE_PDX_MODEL_SOURCE=HF`。
- 模型：`PP-OCRv5_mobile_det` / `PP-OCRv5_mobile_rec`（首次从 HuggingFace 公开源下载）。

实际执行命令（仓库根目录）：

```bash
PY="$PWD/.venv-test/bin/python"
SOURCE="$PWD/work/test_machine_baseline/restored/sarc"
RUN="$PWD/work/test_machine_mobile_01"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONUNBUFFERED=1
export PADDLE_PDX_MODEL_SOURCE=HF
"$PY" scripts/probe_saved_text_recognition.py "$SOURCE" --recognizer mobile --preflight
"$PY" -u scripts/probe_saved_text_recognition.py "$SOURCE" --recognizer mobile \
  --evidence docs/step11_evidence.json -o "$RUN/results/mobile"
```

## 运行结果

- 预检：exit 0，`status=RUNTIME_READY`，`planned=2`（见 `logs/preflight.json`）。
- 实测：exit 0，`planned=2`，两个唯一 case，`pending=0`，`error=null`，`native_files_unchanged=true`
  （见 `results/mobile/summary.json`）。
  - `frame_00002920_mobile`：32 条文本，推理 7.793s（含模型初始化 22.5s）
  - `frame_00002950_mobile`：48 条文本，推理 4.166s
- 检测参数三处一致（本次 raw / 存量 `overall_ocr_res` / 交接文档要求）：
  `limit_side_len=736`、`limit_type=min`、`thresh=0.3`、`max_side_limit=4000`、
  `box_thresh=0.6`、`unclip_ratio=1.5`，`text_rec_score_thresh=0.0`。
- 两份 `raw_ocr.json` 已落盘（`results/mobile/frame_00002920_mobile/`、`frame_00002950_mobile/`），
  另有 `observed_text.txt`、`baseline_layout.json`。
- 57 项基线不受影响：本次只读了工件输入，未重跑全片，未改生产代码。

### 首次尝试失败说明（已处理，不影响结论）

第 1 次实测在模型下载阶段失败：`huggingface_hub` 底层 httpx 无法解析 `no_proxy` 中的括号 IPv6 条目
（如 `[::1]`），报 `InvalidURL: Invalid port: ':1]'`，导致 PaddleX 判定无可用模型源。
处理：仅把 `no_proxy`/`NO_PROXY` 收敛为 `localhost,127.0.0.1`（代理本身未动），重试通过；
第 1 次残留的 `results/mobile`（仅含报错 summary）已清除后重跑。
完整 traceback 见 `logs/mobile.attempt1_download_failed.log`。日志已脱敏，不含任何凭证。

## 逐条对照（摘要）

详见 `comparisons/frame_00002920_LIMIT.md`、`comparisons/frame_00002950_LIMIT.md`
（raw=本次实测首轮 GeneralOCR；stored=工件内存量 overall_ocr_res；md=重组后 markdown）。

| 帧 / 条款 | raw → stored | stored → md | 结论 |
|---|---|---|---|
| 2920 LIMIT.05 | 三行逐字一致 | 按序合并（“需要最”+“小间隔”→“需要最小间隔”正确），混入水印 | 无丢失 |
| 2920 LIMIT.06 | 两行逐字一致 | 合并两行，混入水印 ETNCU/BTMCU | 无丢失 |
| 2920 LIMIT.07 | 两处已是 `vcen`，逐字一致 | 合并两行，混入水印 | `vc_en`→`vcen` 在首次 OCR；重组无丢失 |
| 2920 LIMIT.08 | 首行逐字一致（s≈0.993） | 保留首行，混入水印 ETNC | 无丢失 |
| 2950 LIMIT.07 | 一致（`进配置` 缺“行”，s=0.981） | 合并两行，混入水印 ETNGI/CTWCU | 缺字在首次 OCR；重组无丢失 |
| 2950 LIMIT.08 | **首行被置空**（同框 s=0.9919，raw s=0.992 有文字） | 整条缺失 | **重组阶段丢失** |

## 关键证据：2950 LIMIT.08 首行

- raw（本次）：`#6 [197,146,1082,169] s=0.992`
  `LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的`
- stored：`#6 [197,146,1082,169] s=0.9919` 文字为空
- raw 续行 `#40 [238,585,673,612] s=0.987`：`其他使能信号（比如vcen等）打开；`（stored #40 保留文字，但 md 未收录）
- md：无 LIMIT.08 段落

同模型、同检测参数、同输入文件下复测可正确识别，因此可排除“首次识别失败”。
建议后续：先捕获同一次局部 PP-Structure 重组前后轨迹（为何 #6 保留框与分数却置空文字），
再考虑最小修复；不换模型、不重设计框架。

## 文件清单

- `TEST_REPORT.md`（本文件）、`run_metadata.json`、`SHA256SUMS.txt`
- `logs/`：预检 JSON/stderr/exitcode、实测日志（含第 1 次失败日志）/exitcode、pip freeze 环境
- `results/mobile/summary.json`、两帧 `raw_ocr.json` / `observed_text.txt` / `baseline_layout.json`
- `comparisons/`：两帧逐条 LIMIT 对照
