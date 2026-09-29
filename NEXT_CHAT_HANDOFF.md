# 新对话交接：mp4_anyisis

> 更新：2026-09-29，独立测试电脑交接修订。用户的测试环境在另一台电脑；交接入口必须在Git，不能要求测试机取得聊天附件或访问ChatGPT临时目录。
> 2026-09-29 实测完成：2920/2950 两帧 mobile GeneralOCR 真实运行已执行，报告见 [docs/test_runs/2026-09-29_1018_testvm01/TEST_REPORT.md](docs/test_runs/2026-09-29_1018_testvm01/TEST_REPORT.md)；原 57 项基线未动（57 完成、0 待处理）。
> **执行者先完整阅读 [独立测试电脑交接](docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md)。** 本文件路径中的LOCAL_AGENT沿用历史命名，不代表用户当前电脑。正文修订提交：`322e71954dd69ab82a2e8b2ce4200b1b740f24a9`。
> 本次进入head：`fd9df1273bd0c708e2e0acbc016ced56823871e6`。本次仅更新交接文档，没有改生产代码、依赖、模型或工作流，没有新增OCR、Office或内容通过项。旧附件式交接保留在[修订前固定版本](https://github.com/abba-labs/mp4_anyisis/blob/fd9df1273bd0c708e2e0acbc016ced56823871e6/NEXT_CHAT_HANDOFF.md)，不得再把其中聊天包入口当作测试机的前置条件。

## 0. 当前接续摘要

| 项目 | 已核验状态 |
|---|---|
| 仓库/分支 | abba-labs/mp4_anyisis / feat/open-source-thin-pipeline-20260928 |
| PR/main | 草稿PR #3，未合并；main未修改，不强推、不自动合并 |
| 当前执行方式 | 另一台测试电脑从Git拉取文档和代码，从同一私有仓库的已有Actions工件取得缓存，执行后报告/原生文字结果写回同一分支 |
| 既定流水线 | 110张一秒抽样画面，17候选+40原帧=57个输入，57完成、0待处理；不代表内容完整 |
| 内容验收 | 11个一级资料单元：0完整通过、4有已知失败、7未完成核对 |
| 完整约束锚点 | 原57项结果仍4/8；不是项目完成50%或OCR准确率 |
| 待执行诊断 | mobile 两项已产生真实结果（运行 2026-09-29_1018_testvm01，见下）；server 两项未跑（按交接文档：只有证据需要时才跑，不盲跑）。诊断结论：2950 LIMIT.08 首行丢失在重组阶段；2920 LIMIT.07 的 vcen 为首次 OCR 结果，非重组改写 |
| 最近实测代码 | d99ff89a2ae2c65a25e55145b6a451d8a6da06bf |
| 最近代码回归 | 153通过、0跳过，包含模拟引擎测试；不是153项文字准确性验证 |
| 历史环境阻塞 | 只描述聊天工具/聊天容器，不证明另一台测试电脑也无法执行 |
| 最新实测 | [2026-09-29_1018_testvm01](docs/test_runs/2026-09-29_1018_testvm01/TEST_REPORT.md)：mobile 识别器实测 2 帧，planned=2、pending=0、error=null、native_files_unchanged=true；两份 raw_ocr.json、observed_text.txt、脱敏日志、逐条 LIMIT 对照已归档 |
| 下一唯一动作 | 捕获 2950 LIMIT.08 同一次局部 PP-Structure 重组前后轨迹，定位存量 overall_ocr_res #6（框 [197,146,1082,169]、分数 0.9919）文字被置空的原因；再考虑最小修复。不换模型、不重设计框架、不重跑全片 |

生产仍为三个逻辑模块、一条本地流水线、一个默认PP-StructureV3解析后端。用户要的是可靠提取录屏中实际可见的文档、表格和图片；不自造OCR、表格/配准求解器或复杂平台。旧TASKS.md和REFACTOR_PLAN.md是历史方案，不按其重做框架。

## 1. 测试电脑的唯一执行入口

完整操作见 [docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md](docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md)，已包含：

- 分支克隆/快进、实际head查询及未提交改动保护。
- 在GitHub读取既有工件、来源及两帧哈希校验，不需要聊天ZIP。
- Linux/WSL和Windows PowerShell固定Python3.11环境、两帧真实执行命令及日志要求。
- 8条约束的源位置核对、识别/重组归因边界、最小修复和Word验收条件。
- `docs/test_runs/<RUN_ID>/`下的报告与原生JSON提交要求，结果不必先回传聊天。

使用仓库脚本 `scripts/probe_saved_text_recognition.py`。**不以 `scripts/run_text_control_bundle.py` 作为Git检出入口**：它依赖此前聊天选择性输入包的bundle_manifest，仓库检出并不自带该包。

不用新建、修改或手动触发GitHub Actions工作流。取旧工件是读取数据，不是重跑远程任务。二进制缓存目前在Actions工件中，不在Git文件树；不能把git pull说成已经下载缓存。

## 2. 当前完整缓存与来源

完整57项缓存：

```text
Run ID: 36439891744
Artifact ID: 10978920126
Name: full-recording-resumed-validation
ZIP bytes: 103046931
ZIP SHA256: 6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86
Recorded expiry UTC: 2026-10-28T15:06:46Z（下载前实时核查）
Output root: restored/sarc
Current summary: restored/resume_summary.json
Current report: restored/sarc/report.json
```

`restored/summary.json`是旧31/26状态，不是最新摘要。完整工件344个native文件没有被后续交接修改。测试电脑优先复用已有同哈希副本，不重复下载；缺失时按照交接文档从GitHub获取。工件过期或认证失败应记录准确阻塞，不能重新抽样或推理冒充恢复。

原SARC视频SHA256：`e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a`。
原解析指纹：`878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb`。
原配置：sample_seconds=1、start=0、无end/max_frames/ROI、reconstruct=True、mobile、default、CPU2线程、MKLDNN、word=True。原五份MP4已在仓库MP4目录，不再向用户索要。

固定解析环境：Python3.11，PaddleOCR3.7.0、PaddleX3.7.2、PaddlePaddle3.2.2、opencv-contrib-python4.10.0.84、PyAV16.0.1、python-docx1.2.0。原环境Python补丁3.11.16/Linux；测试电脑平台和补丁差异需记录。Pandoc3.1.11.1只用于Word重导出，不阻塞首次OCR。

最近153项回归：run36504291037 / artifact11006127883；ZIP SHA256 `951e2f4e9355d26b2b60a1d462dddc146c4ac8deb2335ad31f9948d449cc59e9`，记录到期2026-10-29T00:41:41Z。这是历史实测证据，不是本次新增测试。

## 3. 下一次执行与研究边界

在已安装项目及固定依赖的测试电脑，仓库根执行（python必须指向选定Python3.11解释器）：

```bash
python scripts/probe_saved_text_recognition.py work/test_machine_baseline/restored/sarc --recognizer mobile --preflight
python scripts/probe_saved_text_recognition.py work/test_machine_baseline/restored/sarc --recognizer mobile --evidence docs/step11_evidence.json -o work/test_machine_mobile_01/results/mobile
```

完整交接中有两平台日志/退出码处理，不只看终端显示。preflight不导入Paddle、不下载模型、不推理；通过后仍须实际执行第二条。输出目录必须新建，不覆盖旧结果。

真实返回参数需与原text_det_params完全一致：limit_side_len736、limit_type=min、thresh0.3、max_side_limit4000、box_thresh0.6、unclip_ratio1.5、text_rec_score_thresh0。参数漂移保存raw并报错，不删检查或硬改期望值。

关键归因纠正继续有效：最终 `overall_ocr_res`经过上游standardized_data改写，不是首次GeneralOCR快照。第2950帧最终长行文字为空，不足以证明首次识别失败。先比较真实raw、源图和最终结果；需要时再捕获同一次局部PP-Structure调用前后轨迹，不把独立两次结果差异当成旧执行轨迹。

8条源原文在 `docs/step11_evidence.json` 的limit_clauses.records。只忽略排版空白，保留标点/下划线/编号。先mobile再据证据决定server，不盲换模型、不拼正确原句覆盖输出、不把GeneralOCR伪造成完整NativeParser缓存。

## 4. 结果必须回写本仓库

测试执行者在同一分支新建 `docs/test_runs/<RUN_ID>/`，提交TEST_REPORT.md、run_metadata.json、必要的原生raw_ocr.json/observed_text.txt、summary.json、逐条差异、脱敏日志/退出码和SHA256清单，并更新本文件链接实际报告。2026-09-29_1018_testvm01 已按此提交（见顶部链接与 §0 最新实测）。

原图通过已有工件路径/哈希引用，不重复提交全部视频和103MB缓存；机器上保留完整原生结果。大二进制未归档时明确位置与缺口，不能把聊天附件当唯一交付位置，不虚构新的Actions工件ID。

新代码、相关测试与报告提交同一开发分支；推送前重查远端head、审查并发更新，只暂存本轮文件，不强推、不修改main、不自动合并。现有CI触发范围先读，不通过无关源码改动触发全片OCR。每轮20分钟内报告实际已完成、失败与未完成，不以测试数代替内容恢复。

## 5. 历史证据和未完成项

- [2026-09-29 mobile 实测报告](docs/test_runs/2026-09-29_1018_testvm01/TEST_REPORT.md)（运行 `2026-09-29_1018_testvm01`）：2920/2950 两帧 mobile GeneralOCR 真实结果；逐条对照见 `docs/test_runs/2026-09-29_1018_testvm01/comparisons/`。原 57 项基线未动。

- [第十三轮执行准备](docs/step13_execution_readiness_2026-09-29.md)、[第十三轮机器证据](docs/step13_evidence.json)：原两帧真实对照未运行；旧聊天选择性包仅历史交付，不是当前依赖。
- [第十二轮归因纠正](docs/step12_ocr_provenance_2026-09-29.md)、[机器证据](docs/step12_evidence.json)：47处空文字/非零分数观察不是47处已确认漏行，不能重复扫描当修复。
- [第十一轮源内容台账](docs/step11_detection_and_acceptance_2026-09-29.md)、[8条原文与证据](docs/step11_evidence.json)、[源资料单元](tests/fixtures/sarc_review_units_v1.json)。
- [第十轮局部表格对照](docs/step10_saved_table_repair_2026-09-29.md)：g78局部结构改善已实测，g18仍FAIL，不重复原样实验。
- [本次修订前完整交接](https://github.com/abba-labs/mp4_anyisis/blob/fd9df1273bd0c708e2e0acbc016ced56823871e6/NEXT_CHAT_HANDOFF.md)及其链接的全部历史记录继续保留；与当前不同的附件依赖，以本页为准。

OCR污染、编号/条款、g18分格、全部接缝/源内容覆盖、密集MemoryMap、整片Office、其余视频及Windows/离线验收仍未完成。本次只有Git交接修订，不提高任何内容完成率。
