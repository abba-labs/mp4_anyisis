# mp4_anyisis 当前交接：技术突破与整包执行

> 更新：2026-09-29。用户已明确改变分工：**ChatGPT负责大的技术突破；测试电脑模型负责实现、常规调试、测试和成品验收。** 不再每做一个小实验就交回聊天等待批准。
> 本次修订进入head：7d28c3b670ceda673af4102b4660c6159d4a57ee。整包执行文档提交：143161d6b15b61ba74108fb192823e70ec85cdc8。开始和推送前重新查询实际head。本次只更新技术决策和任务授权，没有新增OCR、生产修复、Office或内容通过项。
> **当前执行入口只有本页和[技术路线与测试电脑整包执行任务](docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md)。** 旧文档中的“下一唯一动作”是任务包内步骤，不再是停工/重新请示点；原始证据与验收标准仍有效。

## 1. 测试端现在直接做什么

从Git拉取最新工作分支，复用已可用环境和缓存，连续执行任务包A。过程中正常实现、调试、对照、相关回归和Word检查无需逐步请示。A中的局部难点不要冻结B/C可独立推进的部分。

| 包 | 必须交付的成果 | 执行边界 |
|---|---|---|
| A：约束章节闭环 | 2.4约束说明Word、8条源位置对照及真实通过/失败结论 | 2950同次重组观测→有依据的最小修复→2920等回归；第07条已有识别错误证据，可自行完成尚未执行的server识别器对照；最终核对污染、续行和Word |
| B：图表与导出闭环 | 代表性图表结果、稳定导出及源位置验收 | 复用g78/Pandoc改善，不重跑旧实验；g18依据检测层问题验证未做过的上游结构路径；密集表单列风险；不自研分格/配准 |
| C：SARC整合与扩展 | SARC整合候选、完整性清单和成品包，随后其他4份视频独立验收 | 先做不依赖A的来源清单/总装；按源位置关联/去重，不直接串57份观察；有缺口才定点新增证据，旧缓存不变 |

ChatGPT负责机制分析、上游能力选择、跨画面整合技术约束和路线级失败。测试端负责把这些方向真正落地到结果，不只提交诊断报告。仅当批准路线被实测否定、需要新核心算法/后端或跨授权边界时升级；其他工作继续。

任务包数量不是等权完成率。阶段候选可标REVIEW_REQUIRED，全部适用门禁通过才PASS。汇报以“交付、内容通过、残留风险、下一任务包”为准，不以新增脚本/测试数代替进展。

## 2. 当前已经完成与仍未完成

| 项目 | 已有证据支持的状态 |
|---|---|
| 仓库/分支 | abba-labs/mp4_anyisis / feat/open-source-thin-pipeline-20260928 |
| PR/main | 草稿PR #3未合并；main快照e82f95eb8d71ca1dd212377507e72ef67c89ad1b；不改main、不强推、不修改PR元数据 |
| 基础链路 | 110张一秒抽样画面→17候选+40原帧→57项已处理、0待处理；有实际文件，不证明内容完整 |
| 最新真实OCR | 2026-09-29_1018_testvm01，提交77a8c57；2920/2950 mobile两项完成，pending0、error=null，记录344个原生文件未变 |
| 第07条 | 本次raw两处已经是vcen；2950另有“进配置”缺“行”，首次识别层已复现错误 |
| 第08条首行 | 新raw存在，历史最终overall同框文字为空；强烈支持重组调查，尚未捕获同次清空路径 |
| 第08条续行 | 原JSON标vision_footnote，原Markdown保留“其他使能信号（比如vcen等）打开；”；不是整条从Markdown消失 |
| 原计划识别对照 | mobile两项已完成；server两项尚未执行，现由测试端按任务A自主完成，不重跑mobile凑数量 |
| 图表与输出 | g78有局部结构改善、Pandoc有合并保留改善；g18、密集表、全部接缝和全部Office未通过 |
| 内容验收 | 原57项完整约束锚点4/8；11一级单元0完整通过、4已知失败、7未完成核对；没有整片通过样本 |
| 环境 | testvm01已可运行；Python支持范围3.10—3.12，已用3.11.16跑通就复用，不重新安装 |

[实测原报告](docs/test_runs/2026-09-29_1018_testvm01/TEST_REPORT.md)及其raw/日志不可改写；[REVIEW_AND_NEXT](docs/test_runs/2026-09-29_1018_testvm01/REVIEW_AND_NEXT.md)对续行、独立复测归因和计时的更正继续有效。其旧单步执行节奏由本页覆盖。

## 3. 已下发的技术方向，不冒充已验证解决

具体依据、候选及禁止事项见[整包执行文档第4—6节](docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md)。

- **内容保留**：调查small-overlap使小片段清空长行的机制；同次轨迹证实后，只在实际删除点验证保守覆盖/有效替代条件，不全局改重叠算法，不手补原文。上游large模式仅为候选。
- **实际运行绑定**：固定PaddleOCR封装包含layout运行时补丁，会替换PaddleX的部分函数；采集轨迹同时核对真实函数身份，避免只查静态文件。该补丁解决溢出/空框，不等于已解决本项目漏行。
- **表格路径**：固定版本已有use_e2e_wired_table_rec_model，可验证不经单元格检测器的结构识别路径；只在历史没有相同实验时执行，不盲换后端、不把接口存在当有效。
- **跨画面整合**：复用现成映射和源坐标，把原始证据与派生正文分开；允许有来源的片段关联和录屏叠加内容排除，但不按字符串猜测删除，不把人工真值注入结果。上游Markdown拼装不等于自动录屏去重。

本次ChatGPT做的是技术分析与路线下发；这些新候选尚未在测试机实际验证。若证明无效，按最小反例升级，不继续无依据排列组合。

## 4. 只读必要资料，不重新遍历历史

1. 本页及[整包执行文档](docs/LOCAL_AGENT_TEST_HANDOFF_2026-09-29.md)。
2. [Python策略](docs/PYTHON_ENVIRONMENT_POLICY.md)：覆盖历史3.11-only要求，现有环境优先复用。
3. [testvm01复核](docs/test_runs/2026-09-29_1018_testvm01/REVIEW_AND_NEXT.md)和同目录原报告/JSON：mobile结果已存在。
4. [8条原文](docs/step11_evidence.json)中的limit_clauses.records、[11单元清单](tests/fixtures/sarc_review_units_v1.json)。原文只用于验收，不改写模型输出。
5. 实现需要时读取src/mp4_analysis/thin/{video,parser,pipeline,output}.py与固定上游源码；表格/导出旧实测见docs/step9_word_export_2026-09-28.md、step10_saved_table_repair_2026-09-29.md、step11_detection_and_acceptance_2026-09-29.md。

旧TASKS.md和REFACTOR_PLAN.md仍为历史方案，不重启大框架。不得重复g18/g78原样对照、47处静态扫描、旧31/26续跑或完整SARC OCR，只为拿到已存在的证据。

## 5. 缓存、环境与取回方式

测试机已有.venv-test、官方模型缓存和work/test_machine_baseline/restored/sarc；路径由测试机核查，不假定聊天容器可访问。同哈希副本直接复用。缺缓存才从已有Actions工件读取，不需要新工作流。

```text
Full baseline run: 36439891744
Artifact: 10978920126 / full-recording-resumed-validation
ZIP bytes: 103046931
ZIP SHA256: 6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86
Recorded expiry UTC: 2026-10-28T15:06:46Z（下载前实时核查）
Output root: restored/sarc
Current summaries: restored/resume_summary.json; restored/sarc/report.json
```

restored/summary.json是历史31/26，不混用。git pull不包含二进制缓存；原五份MP4在MP4目录，不索要重传。

源视频SHA256：e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a。
原解析指纹：878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb。
原57项显式配置：sample_seconds1、start0、无end/max_frames/ROI、reconstruct=True、mobile、default表格模式、CPU2线程、MKLDNN、word=True。工程构造默认ocr_models为server，不与这份实验混称。

Python按3.10—3.12策略；当前机制对照固定PaddleOCR3.7.0/PaddleX3.7.2/PaddlePaddle3.2.2及模型参数。原OpenCV4.10.0.84、PyAV16.0.1、python-docx1.2.0；Pandoc3.1.11.1用于既有Word转换。同环境比较原/修改实现，跨环境差异必须记录。

原参考153项代码回归为d99ff89的历史运行36504291037；后续Python策略测试提交f62b4b4的既有CI运行36514074396也已成功。均不是本次新OCR或内容验收。

## 6. 连续推进、提交与验收

每个任务包使用docs/test_runs/<新RUN_ID>/记录成果，实验内保留attempt、原生JSON、真实轨迹、日志、退出码、哈希及源位置对照。可审查的小规模Office样本按现有约定进入同一私有仓库；大二进制只放已批准的持久位置并记录可取回路径。不存在可取回文件就明确归档缺口，不依赖聊天附件、不虚构工件ID。

保留原图、旧缓存、原始报告和失败summary。新修复必须记录新身份/配置，使用新目录；不以旧缓存命中冒充新代码执行。真实验收未通过，只报局部改善或REVIEW_REQUIRED，不硬补内容、不调低标准。

提交前重查工作区和远端，处理并发修改，只暂存本轮文件；不reset/clean覆盖别人改动、不强推、不改main、不合并或改PR元数据、不新建工作流。检查既有CI触发范围，避免无关全片推理。

**无需等ChatGPT给每个小步骤发“继续”。** 测试端在已授权范围内自行完成实现→对照→修正→回归→成品检查；只把有最小证据的路线级问题升级，其他任务继续。ChatGPT仅在当前会话处理交回的问题，不承诺后台自动开发。

修订前全部交接与记录保留在[7d28c3b固定版本](https://github.com/abba-labs/mp4_anyisis/blob/7d28c3b670ceda673af4102b4660c6159d4a57ee/NEXT_CHAT_HANDOFF.md)及其链接。当前推进方式改变，不意味着内容进度已增加。
