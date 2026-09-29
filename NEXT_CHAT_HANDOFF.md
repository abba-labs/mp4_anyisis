# 新对话交接：mp4_anyisis

> 更新：2026-09-29，testvm01两帧真实测试已完成，执行环境阻塞已解除；现在推进局部修复，不再准备相同的两帧实验。
> 本次审阅进入head：`77a8c575c175e9c4ae6f320e85af5451ac89c88d`。该提交是测试电脑新增的真实结果；本次ChatGPT仅复核证据并更新交接，没有新增推理、生产修复或Office。
> 开始及推送前必须重新查实际分支head，不假定无人更新。继续同一开发分支，main不改、PR不合并、不强推。

## 0. 当前接续摘要

| 项目 | 已核验状态 |
|---|---|
| 仓库/分支 | abba-labs/mp4_anyisis / feat/open-source-thin-pipeline-20260928 |
| PR/main | 草稿PR #3，未合并；main历史快照e82f95eb8d71ca1dd212377507e72ef67c89ad1b |
| 执行方式 | 测试电脑从Git取得文档/代码，从已有Actions工件取得缓存，执行后将报告和原生文字结果提交回同一分支；不依赖聊天附件 |
| 已完成基线 | 110张一秒抽样画面、17候选+40原帧=57个输入，57完成、0待处理；不代表源内容覆盖完整 |
| 最新真实测试 | 2026-09-29_1018_testvm01，提交77a8c57；2920/2950两帧mobile GeneralOCR完成，planned2、pending0、error=null |
| 环境/证据 | 测试机Python3.11.16、固定Paddle版本；两份raw JSON及日志已提交；summary记录344个原生文件前后未变 |
| LIMIT.07 | 本次raw两处已经是vcen；首次识别层已复现下划线错误。2950另有“进配置”缺“行” |
| LIMIT.08首行 | 本次raw同框完整保留首行，历史最终overall同框文字为空；强烈支持调查重组，尚未捕获历史同次执行路径 |
| LIMIT.08续行更正 | 原JSON中仍为vision_footnote，原Markdown也保留“其他使能信号（比如vcen等）打开；”；不是整条文字从Markdown消失，而是首行缺失且未形成完整正确条款 |
| 待执行对照 | mobile 2项已完成；原计划server 2项未执行，依据首次识别问题需要再执行，不把2/2写成4/4 |
| 最近代码回归 | 历史d99ff89a2ae2c65a25e55145b6a451d8a6da06bf的153项通过，非本次新增回归、非内容准确率 |
| 内容状态 | 原57项约束完整锚点仍4/8；11个一级资料单元仍0完整通过、4有已知失败、7未完成核对 |
| 下一实际动作 | 在已有测试机上，对2950做同一次局部PP-Structure前后观测；若复现即做最小修复、2920回归和实际Word检查，不止于再写一份诊断 |

## 1. 先读当前结论，不重读全部历史

1. [本次实测复核与下一步任务](docs/test_runs/2026-09-29_1018_testvm01/REVIEW_AND_NEXT.md)：当前最高优先执行单，以其中对原报告的更正为准。
2. [测试电脑原报告](docs/test_runs/2026-09-29_1018_testvm01/TEST_REPORT.md)及同目录run_metadata.json、results/mobile/summary.json、raw_ocr.json、comparisons和日志。原报告和SHA256SUMS保持不可变，审阅补充单独保存。
3. [独立测试电脑交接](docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md)：环境、下载、日志和归档命令仍有效；其中“先跑两帧mobile”的首次任务已完成，不重复执行。
4. 实现需要时再读src/mp4_analysis/thin/parser.py、output.py和固定PaddleX3.7.2源码。8条独立源原文在docs/step11_evidence.json的limit_clauses.records。

测试电脑已有 `.venv-test`、模型缓存和 `work/test_machine_baseline/restored/sarc`；实际路径仍由测试机核查，不假定聊天机器拥有同一环境。缺少PP-Structure其他模型时才补齐，不重建已可用环境或下载相同工件。

## 2. 复核发现与不能夸大的结论

本次读取了提交报告、日志、summary、原生OCR关键字段；还对会话已有完整基线ZIP重算SHA256并读取其中原JSON/Markdown。两个提交的baseline_layout.json之Git blob及SHA256与原ZIP对应成员一致。未对全部新提交文件独立重算哈希，未重新推理。

原报告的“2950第08条整条及续行均未进入Markdown”不准确：续行实际在图片后、2.5标题前保留，标签为vision_footnote。原Markdown SHA256为 `30566ae11793ada6cea978ef1a7f3c70d55d8ec2813fbbe861c116af5ac66a3d`，具体路径及逐项证据见REVIEW_AND_NEXT.md。修复时必须区分首行丢失、续行关联/标签和下划线错误。

本次GeneralOCR与历史PP-Structure是独立两次运行；不能直接把差异当成同一次调用的清空轨迹。下一步深拷贝GeneralOCR刚返回的结果，捕获standardized_data前/后和实际清空/替换位置，再作最小修复。不要再把最终overall_ocr_res误称未经改写的首次OCR快照。

耗时应按summary解释：同引擎初始化22.496秒；两个case各自处理7.793秒、4.1659秒；总elapsed38.183秒。报告“7.793秒含22.5秒初始化”不成立，两个case重复记录的初始化字段不能重复相加。首个模型下载失败日志保留；后续失败summary也要保留，用新attempt目录，不能清空后复用。

## 3. 下一轮执行与停止条件

详见REVIEW_AND_NEXT.md第4节。仅用2950做原配置局部PP-Structure观测，保留原生前后快照及源位置。诊断包装不全局修改site-packages；不从验收原文补写输出，不按帧号、索引或关键字特判，不自行重造重组平台。

一旦捕获可复现路径，优先上游已有能力或最小版本限定适配；同图原实现/修改实现对照，检查首行恢复且续行不丢、不重复，并用2920回归。将合约匹配的原生结果经现有输出路径导出Word，实际读文本、渲染检查。不能把GeneralOCR JSON伪造成NativeParser成功缓存。

第07条raw本身已错，不能指望重组修复自动补下划线。P0取得结果后，确有需要才直接用现有probe的--recognizer server进行同检测器对照；不调用固定追加mobile的bundle包装器，不重复成功mobile推理，不全局改默认模型。

首行改善只报局部改善；完整8条、无污染/缺条/错序、跨屏关联及实际Word都合格才讨论2.4通过。无法复现或修复时保留真实失败和差异，不硬补、不假报通过。

## 4. 原缓存与固定环境

```text
Full baseline run: 36439891744
Artifact: 10978920126 / full-recording-resumed-validation
ZIP bytes: 103046931
ZIP SHA256: 6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86
Recorded expiry UTC: 2026-10-28T15:06:46Z（缺缓存时先实时核查）
Output root: restored/sarc
Current summary: restored/resume_summary.json
Current report: restored/sarc/report.json
```

`restored/summary.json`是历史31/26状态，不能混用。原五份MP4在仓库MP4目录，不索要重传；缓存不在Git文件树，git pull不等于下载工件。有相同哈希副本就直接复用。

源视频SHA256：`e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a`。
原解析指纹：`878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb`。
基线：sample_seconds=1、start=0、无end/max_frames/ROI、reconstruct=True、mobile、default、CPU2线程、MKLDNN、word=True。不要修改抽样/start冒充续跑或改指纹骗缓存。

固定环境：Python3.11（原环境与本次测试记录均3.11.16）、PaddleOCR3.7.0、PaddleX3.7.2、PaddlePaddle3.2.2、opencv-contrib-python4.10.0.84、PyAV16.0.1、python-docx1.2.0。平台、权重身份和实际返回参数分别记录；Pandoc3.1.11.1仅用于可选Word输出。

历史153项回归：run36504291037 / artifact11006127883，SHA256 `951e2f4e9355d26b2b60a1d462dddc146c4ac8deb2335ad31f9948d449cc59e9`，记录到期2026-10-29T00:41:41Z。

## 5. 回写与项目边界

新运行另建docs/test_runs/<新RUN_ID>/，原报告、raw、日志、失败summary和SHA清单不覆盖；保存真实前后轨迹、源位置差异及适用的Word检查。必要代码、测试和报告提交同一分支并更新本页，不把聊天传ZIP作为必须步骤。大二进制放获授权位置并记录哈希/取得方式，不提交环境、模型权重、凭证或全量旧缓存。

提交前检查工作区、远端head和并发修改；只暂存本轮文件，不强推、不改main、不合并或改PR元数据。不要创建/修改工作流或通过无关提交触发整片OCR。

三个模块、一条本地流水线、一个默认PP-StructureV3后端保持。禁止重做框架、盲换引擎、手改原文/标点/下划线/单元格/真值。不要重复g18/g78已完成对照、47处静态扫描、旧31/26恢复或全片重跑。每轮20分钟内汇报真实已完成/失败/未完成，不以测试数量代替资料恢复。

历史根交接完整保留在[77a8c57固定版本](https://github.com/abba-labs/mp4_anyisis/blob/77a8c575c175e9c4ae6f320e85af5451ac89c88d/NEXT_CHAT_HANDOFF.md)及其链接；旧TASKS.md/REFACTOR_PLAN.md不是当前方案。此前聊天端执行受阻只属历史，不能继续阻止已可用的测试电脑推进。

识别污染、编号/条款、g18结构、全部接缝/内容覆盖、密集MemoryMap、整片Office及其余视频仍未验收。当前新增的是已完成真实诊断和审阅后的明确修复入口，不是生产修复或整体交付通过。
