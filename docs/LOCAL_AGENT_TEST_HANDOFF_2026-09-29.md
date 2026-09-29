# mp4_anyisis：技术路线与测试电脑整包执行任务

> 更新：2026-09-29。用户最新分工：ChatGPT负责关键技术路线、难点突破及路线级复核；独立测试电脑上的模型负责实现、常规调试、测试、成品检查和提交。取消“完成一个小实验就交回ChatGPT等待下一步”的节奏。
> 修订基线：7d28c3b670ceda673af4102b4660c6159d4a57ee。开始及推送前重新核对实际head。本次仅下发技术决策和执行任务，没有新推理或新增内容通过项。
> 沿用旧文件路径，避免增加入口。本页覆盖旧交接中的执行顺序；旧证据及验收标准不变。以前的“下一唯一动作”是任务包内的一个步骤，不再是每次提交后的停工点。

## 1. 分工和自主执行权限

| 责任方 | 负责 | 不再承担 |
|---|---|---|
| ChatGPT | 原理分析、上游能力边界、关键适配方向、跨画面整合技术约束；处理有最小反例的路线级阻塞；复核里程碑 | 逐个安装包排障、逐文件小修改、反复触发测试、每个小实验后的批准 |
| 测试电脑模型 | 复用环境；按本页路线实现和调试；连续完成对照、回归、Office检查；保存证据并提交Git | 不把任务止于诊断报告，不把普通报错都交回用户 |
| 用户 | 需求范围、资源/权限和不可逆操作的决定 | 不搬运聊天附件，不逐项批准正常开发/测试 |

测试端在已授权测试机和工作分支内，可以自行完成小范围适配、现有入口接线、相关测试、输出组织和公开依赖/模型补齐。正常实现、证据支持的候选对照、失败修正、再次验证不需要逐步询问用户或ChatGPT。

仍不允许：改main、强推、合并或修改PR元数据；重建框架；引入新生产解析后端；创建/修改/手动触发GitHub Actions工作流；放宽权限；上传私有资料到新外部服务；覆盖原生证据。跨越这些边界必须升级，不能自行扩大授权。

**小步验证继续保留，但在测试端连续完成；小步实验不再成为聊天往返单位。** 普通小提交用于回滚，不构成批准点。会话结束保留当前包的断点，下一会话继续，不重选题。ChatGPT每轮仍在20分钟内总结；这不是要求测试端每20分钟重新准备一套交接或重新初始化。

## 2. 当前事实与不能重复的工作

以[实测报告](test_runs/2026-09-29_1018_testvm01/TEST_REPORT.md)、[复核更正](test_runs/2026-09-29_1018_testvm01/REVIEW_AND_NEXT.md)、[Python策略](PYTHON_ENVIRONMENT_POLICY.md)为准：

- SARC既定57个输入已处理，344个native文件属于保留基线；抽样处理完成不证明源内容完整。
- testvm01已完成2920/2950两帧mobile GeneralOCR，环境已可用。不原样重跑mobile两项；原计划server两项尚未执行。
- 第07条在本次raw中两处已是vcen。2950第08条首行在新raw存在、历史最终结果缺失；续行在原Markdown仍保留为独立片段，不是整条文字全被删除。
- 同次PP-Structure清空路径已于2026-09-29捕获（10个写入事件，hurdles循环:427误伤旁观者行），最小修复已验证，证据见docs/test_runs/2026-09-29_1215_testvm01_p3/TEST_REPORT.md；独立复测差异不是同次轨迹。
- 原57项完整约束锚点仍4/8；11个一级单元仍0完整通过、4已知失败、7未完成核对。本页不改变通过数。
- Python允许3.10—3.12，不锁补丁版本。已用3.11.16跑通就继续复用，不为切版本重新安装。

三个逻辑模块、一条本地流水线、一个默认PP-StructureV3解析后端不变。核心继续复用PyAV/FFmpeg、OpenCV、PaddleOCR/PaddleX、Pandoc；不自写OCR、表格求解器或配准算法。[R1]

## 3. 三个完整交付任务包

任务包数量用于组织交付，不是等权完成百分比。

| 任务包 | 交付目标 | 测试端连续完成 | 完成判断 |
|---|---|---|---|
| A：约束章节闭环 | 2.4约束说明Word、原生结果与逐条证据 | 同次轨迹、最小修复、必要识别器对照、污染/续行处理、8条核对、Word检查 | 8条内容、编号、标点、下划线、顺序、跨屏关联、无污染与Word均通过；否则保留失败清单 |
| B：图表恢复与导出闭环 | 代表性图表修复结果及稳定导出路径 | 复用g78/Pandoc结果；处理g18检测层问题；普通表与密集表分层验证；图像和Office检查 | 对源单元格及图像区域验证，不以格数、列数或文件存在代替正确性 |
| C：SARC整合与扩展验收 | SARC整合候选、完整性清单和成品包；再推进其他视频 | 源位置组织、跨画面关联/去重、章节总装、11单元核对、覆盖补查、其他视频验证 | 全部适用门禁通过才标SARC通过；其余4份视频各自单列，不自动继承 |

A为当前主线；B的既有结果整理、C的只读清单和总装骨架不依赖A修复，可以穿插推进。一个字符或一张表未解决，不冻结全部工作。C的最终通过等待内容合格，但建立可复核候选不必等所有Bug修完。

优先单一代码写入者。确有多执行者时只分派互不覆盖的工作，不并发修改同一文件或Git工作区，不为分工新增平台。

## 4. 技术路线A：内容保留，不靠手补原文

### 4.1 首选机制与修复假设

固定PaddleX v3.7.2的standardized_data在多布局框处理中，以calculate_overlap_ratio(ocr_box, crop_box, 'small')大于0.8清空其他OCR文字，随后才填入部分重识别结果。比较的是交集/较小框面积，并不保证被清空的长行已被替代区域覆盖。[U1]

已有条件反例：长行[197,146,1082,169]与小框的small-overlap约0.955，但交集只覆盖长行约5.06%。这是值得优先验证的机制，不证明历史2950实际调用顺序。[R2]

**首选假设：局部片段不能仅凭覆盖自身，就清空没有被有效替代的整行。** 同次轨迹若确认此机制，仅在该删除调用点验证更保守的覆盖判断；上游已有large模式，可作为候选复用。不是已验证修复，不允许全局把small替换成large。还应检查删除时机：没有有效替代结果时，不应先不可逆丢弃原观察。

若实际是其他分支导致丢失，按轨迹处理，不为符合假设修改记录。验证须覆盖重复文字、跨块切分和阅读顺序，不只检查首行出现。

### 4.2 本次新增源码核查：运行时函数绑定

PaddleOCR v3.7.0的PPStructureV3导入并应用_patch_layout_parsing.py；该补丁同时替换layout_parsing.utils和pipeline_v2中的重叠/最小包围框函数，解决整数溢出和空框。它仍保留small/large面积语义，不代表已修复当前漏行。[U2][U3]

同次轨迹中顺手记录实际函数module、源文件和身份，避免只修改utils而pipeline_v2仍绑定旧函数，或把数值修复误当成内容修复。以测试机安装包为准。此检查随轨迹完成，不另开一个准备阶段。

### 4.3 执行到修复与Word，而不是停在轨迹

对2950执行一次原配置PP-Structure，深拷贝GeneralOCR返回、standardized_data入口/出口及实际清空/替换事件，保存最终原生JSON/Markdown。复现后立即在同环境做候选修复对照，再用2920及受影响类型的代表性样本回归。未复现则保留差异，不制造轨迹。

适配限定版本、隔离、可撤销，不全局改site-packages，不按帧号/文本/索引特判。新代码/配置必须有独立修复身份或缓存签名，写新派生目录。现有NativeParser缓存不匹配时会重建target，因此禁止将原native目录作为不同配置实验target。[R1]

第07条已有首次识别错误证据，测试端获准直接执行现有probe的server识别器对照，无需再请示；保持mobile检测器及其他参数不变。不要调用固定追加mobile的聊天bundle包装器。

```bash
# 仅在没有相同server结果时；PY/SOURCE指向已有环境和缓存，NEW_RUN为新目录。
"$PY" scripts/probe_saved_text_recognition.py "$SOURCE" --recognizer server \
  --evidence docs/step11_evidence.json -o "$NEW_RUN/results/server"
```

识别器与重组是两个变量，分别验证后才组合。不得同时改二者再把改善归因给其中一个。

### 4.4 污染与续行是派生资料整理，不是改写识别

原图、raw、旧native不改。派生正文可以排除有源位置、方向、跨帧证据的录屏叠加文字，保留排除记录。不能仅凭像ETMCU的字符串设黑名单，因为它也可能是有效正文/页头；不擦除源图水印，不从真值补字。

允许按页/段落关系关联真实观察到的相邻片段，每段保留来源。旧规则禁止“拼正确原句冒充单次OCR”，不禁止透明的跨屏整合。vision_footnote标签不等于可以丢弃那段文字；归属不确定就保留待核对。

GeneralOCR JSON不能伪装成完整NativeParser缓存。Word使用真实匹配契约的结果及已有输出能力。8条全部核对且无污染、无重复/缺条、跨屏关系与Office正确后，才能讨论2.4通过。

## 5. 技术路线B：复用完整表格能力，不自己分格

已有结论：g78检测6格却HTML生成7格，cells已局部改善；g18原帧与候选都检测过分格，重复cells或手工删框不能恢复正确几何。Pandoc解决导出保留，不修正原本错误的识别。[R3]

**有依据的g18候选：use_e2e_wired_table_rec_model。** 固定版本公开接口透传该参数；官方教程说明启用后使用表格结构模型、不使用单元格检测器。[U3][U4] 当前已定位检测过分割，这是一条不同机制的待验证路径，不是第二个生产后端。

执行前只核对历史是否已有同输入/同版本/同配置结果；有则直接复用，不重新候选排查。不把参数存在当成结果正确，不同时强开cells混淆变量。保留默认结果，对g18、g78、原正常frame452核对物理格、合并、文字及源位置。失败不删格、不改真值、不全局切换参数。

密集MemoryMap是单独高风险类型。先复用历史失败矩阵，不再围绕同一截图盲换后端。批准路径仍不足时提交最小反例和实际模型/结构差异，由ChatGPT处理路线；普通表格与输出集成继续。

图像继续复用OpenCV现成配准/接缝和源图。g12既有通过只在限定矩形；单帧完整图优先保留，需要跨屏才核对对应接缝。不补画缺失字符/边界，不自写配准。

将已有Pandoc导出接成明确稳定的输出选择，默认策略升级须由代表性证据支持；保留原生输出及身份，不将“与原XLSX一致”视为“源表正确”。接线、测试、Office逐项检查由测试端完成，无需ChatGPT逐文件实施。

## 6. 技术路线C：按源资料组织，不直接串联57份结果

57输入是观察，不是57页原文。write_index只是索引，没有跨批次去重。OpenCV源到画布映射也未全部验收，不能直接作为已确认页身份。[R1]

在现有输出模块内做薄适配，复用video.json、reconstruction.json、parsing_res_list和11单元台账。普通JSON记录派生块到源视频/帧/坐标/原生产物及处理原因的对应，不建新数据库、服务、插件或通用求解器。

- 同一源位置的重复观察可以折叠；不同位置即使文字相同也不能删。只有空间/页身份及上下文支持才去重，保留所有来源；不确定时保留片段与缺口。
- 已核验映射用于相应范围内定位，跨批次复杂配准升级ChatGPT，不自研算法。相邻片段可透明关联，但不从真值倒推内容，不按SARC专用编号硬编码。
- 复用上游或Pandoc转换/拼装。PPStructureV3有concatenate_markdown_pages接口，但须满足实际输入契约；它存在不代表能自动解决录屏跨帧去重，不把所有观察直接串起来就称完整恢复。[U3]
- 图片、表格、正文保留源位置关系。未解决项在候选中显著标识，不伪装成已验收原稿。

先交付SARC整合候选和真实缺口表，再逐项关闭。需要补查短暂画面时，只对明确覆盖缺口新增观察并单独记账；既有57项计划/缓存不变。不改变start/抽样冒充续跑，不为一个缺口重跑全部OCR。

SARC全部适用门禁通过后，再以相同标准验证其余4份视频，各自记录结果；新视频验证不算重复旧SARC，但不能用一份通过替代5份验收。

## 7. 升级条件与成果回写

普通安装、参数传递、日志、输出接线、相关回归由测试端自行完成。仅在同次轨迹推翻机制、批准候选在代表性输入仍无效、需要新核心路线/后端，或必须跨越授权/验收边界时升级。

升级材料写在当前TEST_REPORT.md：一个最小失败输入引用、固定版本/模型身份、原生结果、具体差异、已完成的有依据对照和一个明确问题。不另建一套汇报框架。升级该问题，不冻结整个项目；继续其他可独立任务。不得声称ChatGPT会后台自动接手。

每个任务包一个唯一RUN目录，内部按attempt/候选分开；失败summary、日志、raw不清空重用。小步提交可以回滚，但不用每次等批准。

```text
docs/test_runs/<RUN_ID>/
  TEST_REPORT.md          # 成果、真实通过/失败、路线级阻塞
  run_metadata.json      # 源、环境、模型、代码、参数、时间/退出码
  SHA256SUMS.txt
  results/               # 必要原生JSON、summary、文字
  comparisons/           # 源位置对照及派生来源关系
  trace/                 # 仅实际捕获的轨迹
  logs/                  # 脱敏环境/运行/失败日志
```

小规模可审查的Office/渲染交付样本可按现有约定提交同一私有分支；大文件用已批准的持久存储并记录位置/哈希/期限。没有可取回二进制，不把“测试机存在”说成别人可验收。不提交环境、权重、字体文件、凭证、全量旧缓存或重复视频。

里程碑汇报只需：交付了什么、哪些源内容通过、残留风险/阻塞、下一任务包。测试数、脚本数、文件生成都不是内容通过。整合候选允许REVIEW_REQUIRED；完整验收才PASS。原11单元通过数须有全部适用门禁证据，不改变分母制造进度。

## 8. Git、缓存和环境最短入口

继续abba-labs/mp4_anyisis的feat/open-source-thin-pipeline-20260928。先git status、git fetch并核对远端；干净可快进时git pull --ff-only。不自动reset/clean/stash，不覆盖并发修改，不强推，只暂存本轮文件。提交前检查既有CI触发范围，不通过无关改动重跑全片。

testvm01已有.venv-test、模型缓存和work/test_machine_baseline/restored/sarc，先核对实际存在后复用。新环境按PYTHON_ENVIRONMENT_POLICY.md，不执行旧3.11-only。当前对照固定PaddleOCR3.7.0/PaddleX3.7.2/PaddlePaddle3.2.2及模型/参数；其他版本差异如实记录。

完整基线（有相同副本就不下载）：

```text
Run: 36439891744
Artifact: 10978920126 / full-recording-resumed-validation
ZIP bytes: 103046931
ZIP SHA256: 6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86
Recorded expiry UTC: 2026-10-28T15:06:46Z
Root: restored/sarc
Current summaries: restored/resume_summary.json; restored/sarc/report.json
```

缺缓存才实时核查并只读取得旧工件，不新建工作流：

```bash
gh api repos/abba-labs/mp4_anyisis/actions/runs/36439891744/artifacts --jq '.artifacts[] | select(.id == 10978920126) | {id,name,expired,expires_at,digest}'
gh run download 36439891744 --repo abba-labs/mp4_anyisis \
  --name full-recording-resumed-validation --dir work/test_machine_baseline
```

gh run download直接解压，不等于已验证原ZIP哈希；取得原ZIP才校验ZIP，解压后按输入/adapter哈希核查。旧restored/summary.json仍是31/26，不使用。认证/过期失败明确记录，不重建缓存冒充恢复。五份原MP4均在MP4目录，不索要重传。

源视频SHA256：e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a。
帧2920文件SHA256：567bd31e2447165c93aaee349869edf4c0eb28b16d0137db70799214fb083cb7。
帧2950文件SHA256：d2fe16ef0d8c919e3ed9d48cce4d9920f3e95c420a26bc5e1a28802953b86770。
原解析指纹：878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb。

原57项显式使用mobile检测/识别；工程构造函数默认ocr_models为server，不能混淆代码默认与历史实验配置。旧原文/真值/配置/缓存不变，新结果有新身份。

## 9. 技术依据及有效性边界

[R1] 当前src/mp4_analysis/thin/{video,parser,pipeline,output}.py；核查基线7d28c3b。应用适配继续落在这些逻辑模块，不新建平台。

[R2] docs/step12_ocr_provenance_2026-09-29.md及docs/test_runs/2026-09-29_1018_testvm01/REVIEW_AND_NEXT.md：最终overall可变、5.06%条件反例与续行更正；反例不是同次轨迹。

[R3] docs/step9_word_export_2026-09-28.md、docs/step10_saved_table_repair_2026-09-29.md、docs/step11_detection_and_acceptance_2026-09-29.md。已有g78/Pandoc改善和g18失败保留；旧OCR归因以较新更正为准。

[U1] PaddleX v3.7.2，读取约388—485行，blob 83ab5dec1bb07f3b188a3f82da464550c1ab49ec：
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/pipelines/layout_parsing/pipeline_v2.py
清空逻辑是源码事实；large候选有效性仍待实测。

[U2] PaddleOCR v3.7.0，完整读取运行时补丁：
https://github.com/PaddlePaddle/PaddleOCR/blob/v3.7.0/paddleocr/_pipelines/_patch_layout_parsing.py
修整数溢出/空框，不宣称已修复当前漏行；部署身份需实际核对。

[U3] 固定版本PPStructureV3公开封装，读取参数透传、补丁导入及Markdown拼装接口：
https://github.com/PaddlePaddle/PaddleOCR/blob/v3.7.0/paddleocr/_pipelines/pp_structurev3.py
接口存在不是样本通过。

[U4] 官方教程对端到端有线表模式的说明：
https://paddlepaddle.github.io/PaddleOCR/main/en/version3.x/pipeline_usage/PP-StructureV3.html
教程为滚动文档，接口是否存在以U3固定源码及实际安装包为准；本文未运行新表格实验，不将候选视为已解决。

旧单步式交接永久保留在7d28c3b固定提交及更早Git历史。旧TASKS.md和REFACTOR_PLAN.md不重新启用。当前任务是测试端完整执行A，不是再写准备报告；B/C独立部分继续，路线级阻塞按第7节升级。
