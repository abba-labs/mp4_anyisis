# 新对话交接：mp4_anyisis

> 更新：2026-09-28，第八轮。当前流程已完成57个既定解析输入，但内容验收仍FAIL。不要继续按旧“31完成、26待处理”状态重跑。
> 本轮进入head为76e5fd9de4d7065e35cc31359959859046bf5404；本文件提交会继续改变head，接续前必须查询PR实际head。
> 前七轮完整交接与失败教训永久保留在[原交接固定提交](https://github.com/abba-labs/mp4_anyisis/blob/76e5fd9de4d7065e35cc31359959859046bf5404/NEXT_CHAT_HANDOFF.md)。本页更新当前入口，不废弃其中的工程约束、原始证据与研究方法；旧状态以本页和本轮工件为准。

## 0. 当前接续摘要

| 项目 | 当前已核验事实 |
|---|---|
| 仓库/分支 | abba-labs/mp4_anyisis / feat/open-source-thin-pipeline-20260928 |
| PR | #3，仍为草稿，未合并；不修改main、不强推 |
| main快照 | e82f95eb8d71ca1dd212377507e72ef67c89ad1b，本轮未修改 |
| 实测实现提交 | 4913170f93b5808deb1c306a2c2f7a00653b83f3 |
| 本轮运行/工件 | 36439891744 / 10978920126 |
| 流程结果 | 同一110画面、17拼接候选、57输入；31实际缓存命中、26新增成功、0失败、0待处理 |
| 时间/状态 | 续跑475.105秒，REVIEW_REQUIRED，不是内容验收通过 |
| 缓存证据 | 原31份结果的170个文件逐字节未变；原始ZIP也完整保存在新工件 |
| 原生文件 | 57份Word、30份Excel、58份Markdown（含索引），仍不是一份整合文档 |
| 回归 | 固定环境92 passed / 0 failures / 0 errors / 0 skipped；其中12项新增缓存防护测试 |
| 复位条款 | 原句已在2828/2890/2920结果出现，2890的Word也保留；但2890漏掉源可见的条款02、编号01读成O1 |
| 架构图 | group_000012_b限定图片矩形与源512逐像素相同，Word嵌图未再裁断；不代表全部接缝通过 |
| 普通表格 | HTML/XLSX保留本例合并，Word丢失合并、SARC从B2挪到A2；文字本身也有污染 |
| 内容结论 | FAIL；完整性、其余接缝、全部单元格、整片Office与密集MemoryMap仍未验收 |
| 下一唯一优先动作 | 复用已完成工件，定位并最小对照验证PaddleX3.7.2原生Word导出丢失rowspan/colspan，不重跑OCR |

本轮证据：[resume_evidence](docs/resume_evidence_2026-09-28.json)、[源位置内容检查](docs/step8_content_review_2026-09-28.md)、[机器可读检查](docs/step8_content_review_2026-09-28.json)。旧docs/handoff_evidence_2026-09-28.json保留为首次31/26恢复的不可变基线，不是最新运行摘要。

## 1. 目标与不能改变的约束

把授权录屏实际可见的文档、表格、图片可靠提取出来。三个逻辑模块、一条本地顺序流水线、一个默认PP-StructureV3后端，复用成熟开源能力，只做薄适配。

不自造OCR、表格求解器、配准算法、通用排版平台；不引入数据库、队列、多引擎投票或复杂插件框架。旧TASKS.md、REFACTOR_PLAN.md是历史方案，不按其中大框架执行。不能硬改单元格、规格文字、验收锚点或降低标准。不能用文件生成、列数正确、回归通过冒充资料正确。

所有改动、测试、分析和交接提交同一工作分支；不合并任何PR、不覆盖旧二进制、不索要PAT或再次索要仓库已有MP4。普通回复短，详细记录进仓库。每轮对话20分钟内必须总结，提前预留记录时间。

## 2. 阅读顺序

先查询实时PR head，再读本页和docs/resume_evidence_2026-09-28.json。随后按顺序读取：

1. docs/step8_content_review_2026-09-28.md及同名JSON；需要历史边界时完整阅读上方固定提交的旧交接。
2. README.md、pyproject.toml。
3. src/mp4_analysis/thin/pipeline.py、video.py、parser.py、output.py、cli.py。
4. scripts/resume_full_recording.py、.github/workflows/full-recording.yml。
5. tests/test_resume_full_recording.py、test_reconstruction.py、test_thin_pipeline.py。
6. tests/fixtures/native_acceptance.json、scripts/check_native_samples.py；它们是历史固定原帧测试，不是整片通用验收器。

生产三个模块本轮未改，新增的是实验恢复预检和测试。固定OpenCV4.10公开detail拼接兼容问题已经修复，不要倒回依赖升级方案。

## 3. 本轮实现与证据

- 2d8ce5d：新增恢复脚本；先只读检查视频/计划/指纹/原生输入输出哈希，再调用原流水线。任何不符先停止，避免NativeParser缓存未命中时清理成功目录。
- 03645ef：12项防护测试，包括指纹、输入/输出损坏、job顺序、word开关、错误缓存、空输出、修改start和路径越界。
- 4913170：工作流下载并保留原完整ZIP，按旧environment.txt约束安装，恢复同一57-job计划；保存预检、真实命中、错误、原文件不变性及新摘要。
- 本轮回归另有运行36439831638/工件10976953470，JUnit同为92通过。不是92项OCR准确率测试。

完整新ZIP：103046931字节，SHA256为6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86。已实际下载、重算哈希并核对报告。工件到期时间2026-10-28T15:06:46Z，30天保留不是永久存储。

原工件10972954977的原ZIP在新工件根original_10972954977.zip，SHA256仍为c83a0889a2a56dbff4c1736010eb238031845837f62d5866a9c3462d14716fd2。

## 4. 当前真实故障层

### 原生解析层

组合图标题“1.2 应用说明”清晰，但原生结果仅“1.2”。页头表SARC混入20:1，V1.0多出+。源2890清晰含条款02，但其原生结果与Word缺失；该条款在2920原生结果出现。因此不能说全片完全丢了条款02，也不能说2890已正确恢复。

### Word导出层

frame_00000452页头表，源A1:A2、C1:C2、D1:D2、A3:D3合并，原生HTML/XLSX正确保留；DOCX没有w:gridSpan/w:vMerge，第二行文字挪列，保密等级挤入第一列。故应先研究已有HTML到Word的上游导出，而不是换OCR或重跑视频。固定源码下载曾被本地DNS阻断，本轮尚未完成源码复核和修复实验。

### 局部图像检查边界

group_000012_b的[166,374,1084,710]与源512的[166,301,1084,637]完全相同。该源帧自己已显示完整架构图，所以不夸大为只有跨屏才能恢复；鼠标遮挡仍在。原生JPG与Word内JPG哈希相同，渲染检查无新增裁断。其余接缝未验收。

## 5. 原视频位置

五份均已在MP4目录：ET6601_SRC_LRS设计文档.mp4（当前SARC）；GameViewer_96iLJ4Cokv.mp4（MemoryMap）；EFC设计文档.mp4；ET6601_EFC模块LRS设计文档.mp4；SRC模块设计方案.mp4。

SARC文件SHA256为e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a。当前抽样只证明这些已选画面有处理去向，不证明原视频所有可见内容被选中。

## 6. 下一轮如何恢复当前完成结果

先下载新工件10978920126并核对哈希，不要只取旧补丁ZIP，也不要假定前对话sandbox仍在。

新工件内：

- restored/sarc/：当前完整输出，含57份adapter、原帧、候选、report与索引。
- restored/resume_summary.json、restored/resume_preflight.json：本轮真实统计和指纹。
- resume.log、environment.txt、tests.xml、tested_commit.txt、tested_source.tar：本轮运行证据。
- restored/summary.json：旧运行的摘要，不能误当本轮结果。

环境Python3.11.16，av16.0.1，opencv-contrib-python4.10.0.84，paddlepaddle3.2.2，paddleocr3.7.0，paddlex3.7.2，python-docx1.2.0。解析指纹878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb。

相同全片参数：sample_seconds=1.0,start=0,end=None,max_frames=None,roi=None,reconstruct=True,ocr_models=mobile,table_mode=default,threads=2,mkldnn=True,word=True。

首次恢复脚本和当前工作流有意固定旧31/26基线以复现实验；下一轮不要再次运行它们从旧包重新推理26个。使用新工件的57份成功结果，保留不可变副本；只研究导出时不调用全片OCR。不修改adapter指纹骗缓存，不改变start/采样密度制造续跑，不清空缓存。

## 7. 接下来的内容验收

复位原句已找到，但整个约束章节仍需逐条编号/原文比较。架构图仅限定矩形通过，其余候选接缝与来源覆盖待查。普通表格须逐非空单元格与合并关系核对。Word已实际渲染三份：图、页头表、复位条款；不能说全部57份验收过。Excel已读取结构和类型，视觉渲染因artifact_tool启动超时未完成。

整片需按章节、页面、图表建立“源观察→输出位置→核对状态→遗漏/不确定”清单；采样时间覆盖与内容覆盖分别记。密集MemoryMap位置锚点仍保留旧FAIL，不在本轮重复盲换引擎。

## 8. 后续优先级

先用现成普通表格HTML定位PaddleX3.7.2 Word合并导出；最小实验成功后验证第二张同类表，再接入。然后检查标题/条款遗漏、其余接缝与整片覆盖、去重和阅读顺序、首次运行效率，最后继续密集表独立研究及其余视频/离线Windows扩展。不要通过字符串相似度删除不同地址、编号或有效重复值。

## 9. 固定研究方法

先定位失败层：输入可见性→抽帧→拼接→文字→结构分配→导出。再查固定版本官方源码/文档，不能拿最新接口套旧版本。固定同输入和源位置，优先只改一项，保存原生产物、哈希、参数、耗时与差异。证明改善后再接入并跨样本回归；没改善则保留隔离记录。不自写求解器、不生成缺失内容、不为测试迁就模型改真值。

## 10. 下轮交接纪律

提交前重新查head；保留本轮来源和旧失败教训。结束时记录实现/文档提交、run/artifact/hash/期限、成功/失败/pending、实际内容检查范围、未做事项和下一唯一动作。GitHub工具错误、环境失败、执行失败、内容失败分别写。不要把后台运行当成会自动交付，也不以测试增加抬高主观完成率。
