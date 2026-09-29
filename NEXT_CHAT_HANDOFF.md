# 新对话交接：mp4_anyisis

> 更新：2026-09-29，第十一轮。原57项解析已完成，整片内容仍FAIL；本轮完成g18检测层定位、建立11个源资料单元台账及8条约束原文基线。没有新增OCR文字推理、Word/Excel或通过验收的整合文档。
> 进入head：e9b7f4ba1ffc3d9cc2fe27b6574ba9693d587690。检测实测提交f7177e6c0868b3c8b3ad6a6e6e182e4d86acf567；台账/回归提交ef8f5b405de16faacb9b455d0002a31728202a46。接续前查询PR #3实际head，不假定无人更新。

## 0. 当前接续摘要

| 项目 | 已核实状态 |
|---|---|
| 仓库/分支 | abba-labs/mp4_anyisis / feat/open-source-thin-pipeline-20260928 |
| PR/main | #3仍为草稿、未合并；main未修改，快照e82f95eb8d71ca1dd212377507e72ef67c89ad1b |
| 既定处理 | 110张一秒抽样画面、17候选+40原帧=57输入；57完成、0待处理；不证明全部内容覆盖 |
| 旧缓存 | 344个native文件再次逐字节核对未变；原Word/Excel/JSON未改 |
| g18定位 | 原候选与源675均检出10格；人工紧框两者像素完全相同且都检出7格；不是源6格，仍FAIL |
| 本轮推理 | 5个分类/单元格检测对照，0新增OCR文字推理；检测循环8.247秒，不含环境、导入及分类器初始化 |
| 接入决定 | 不接入人工ROI或全局阈值修改，不改变生产默认；g78上轮局部改善继续保留 |
| 验收台账 | 源目录7小节+4类前置资料=11一级单元；0完整通过、4有已知失败、7未完成核对；不是整体完成百分比 |
| 约束基线 | 源2920/2950核对8条完整原文；现有结果4/8完整字符串锚点命中，不是50%准确率 |
| 新定位 | LIMIT.07原始OCR已将vc_en读成vcen；LIMIT.08源2950清晰首行的原始识别为空，不是Word导出才丢失 |
| 回归 | 固定Python3.11/OpenCV4.10/Pandoc3.1.11.1：131通过、0失败/错误/跳过；不是131项内容验收 |
| 当前交付状态 | 无新的完整验收样本、无新Office输出；全部内容/接缝、密集MemoryMap、整片Office仍未通过 |
| 下一唯一动作 | 围绕2.4的05—08，用现成原文基线和OCR框做识别层小范围对照，先闭环一个内容单元；不重复g18实验 |

详细记录：[第十一轮](docs/step11_detection_and_acceptance_2026-09-29.md)、[机器证据及8条原文](docs/step11_evidence.json)。源清单：[sarc_review_units_v1.json](tests/fixtures/sarc_review_units_v1.json)。这些是当前入口，旧31/26恢复和g78/g18已完成实验不应重新执行。

## 1. 阅读顺序

先查实时PR head，然后读本页、step11记录和JSON。按任务读取：
1. tests/fixtures/sarc_review_units_v1.json、scripts/build_content_review.py、tests/test_content_review.py：源单元台账、门禁及核对链接。
2. docs/step11_evidence.json的limit_clauses：8条源原文、命中job及已定位OCR问题；原生JSON的overall_ocr_res与parsing_res_list需分开检查。
3. src/mp4_analysis/thin/parser.py、output.py：单一解析后端、成功缓存、原生结果及可选Pandoc重导出。
4. scripts/probe_saved_cell_detection.py及工作流saved-cell-detection.yml只是本轮已完成的5项检测诊断，不无理由重跑。

历史第十轮交接永久保留在固定提交e9b7f4ba1ffc3d9cc2fe27b6574ba9693d587690的NEXT_CHAT_HANDOFF.md。其链接的第九/八/前七轮交接和docs/step10_saved_table_repair_2026-09-29.md继续有效。TASKS.md、REFACTOR_PLAN.md仍是历史大框架方案，不按它们重新设计。

## 2. 当前证据与缓存

### 完整57项缓存，不重新生成

run36439891744 / artifact10978920126，103046931字节。
SHA256：6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86。
到期2026-10-28T15:06:46Z。完整输出根restored/sarc。新摘要是restored/resume_summary.json，restored/summary.json为旧31/26状态，不能混用。

原五份MP4仍在仓库MP4目录，不需要再次索取。SARC源SHA256为e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a。原解析指纹878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb。原参数sample_seconds=1、start=0、无end/max_frames/ROI、reconstruct=True、mobile、default、CPU2线程、MKLDNN、word=True。

### 本轮5项检测诊断

run36500318940 / artifact11005180919。
SHA256：855812fd8b7f3928a6cef964bec6b3aa3c6771ac3a9420c0d3b1d17dd8b111b5。
到期2026-10-28T23:54:59Z。results/summary.json、五个子目录中的input.png/classification.json/detection.json、run.log及tested_source.tar可直接复核。它不是完整缓存。所有模型为固定PaddleOCR3.7.0/PaddleX3.7.2/PaddlePaddle3.2.2；没有文字推理。

### 本轮回归

run36500737618 / artifact11004804880。
SHA256：4f2b237716e0334baaf9ab0567007cce2c67e85234922ce5850725e1b16c76ea。
到期2026-10-28T23:58:50Z。JUnit已下载核实131通过/0跳过。本地Python3.13.5为130通过/1跳过，缺PyAV，不冒充固定环境。

g78上轮改进及g18原cells对照仍在run36496321097/artifact11003745957，SHA256 4b15309ca4a4ece0f0635e060db59559e544fe14862e17b5220ddae2c5de6780，到期2026-10-28T23:09:47Z。不要为了拿到同一结果重跑。

## 3. 如何使用验收台账

```bash
python scripts/build_content_review.py work/full/restored/sarc \
  --ledger tests/fixtures/sarc_review_units_v1.json -o work/content_review
```

只读检查视频身份、源帧/产物哈希，输出index.html、review.json。HTML指向源缓存中的真实帧、PTS及原生Markdown/Word/Excel，需保留缓存路径。提供的mp4_step11_review_bundle.zip只是有限源图/产物核对包，不是完整缓存；历史sandbox链接不保证新会话可用。

11项来自独立源目录/前置画面，大小不同；尚不是逐字逐格、短暂页面的完整清单。PASS必须有coverage、text、tables、images、office各适用门禁的实际证据，不能因文件生成自动通过。4项有已知失败，7项未完成核对，不等于剩余7项都正确；不据此编造整体完成度。后续更新须保留版本和证据，不能删失败单元来抬高比例。

## 4. 已定位问题，避免重复劳动

### g18

原候选及源675的原框[117,396,1166,529]均10格。人工紧框[117,396,1166,510]两者PNG哈希完全相同，均7格，V1.0仍被格内线错拆。裁剪只去掉部分多余框，尚无可接入的通用修复。调阈值删掉一个框会留缺口，不是恢复6格。保留FAIL，不全局切cells、不补绘或手合并格子。

### 2.4约束说明

源2920/2950核对8条原文。只忽略空白，01—04在若干已有job中命中完整字符串；05—08没有完整精确匹配，但部分内容已识别，不能称全片完全缺失。

07：源vc_en在overall_ocr_res就变成vcen。08：源2950的[197,146,1082,169]首行清楚但rec_texts为空，2920有前半，2950有后半且丢下划线。这是下轮识别层实验入口，不能改Word、拼字符串或硬补原文冒充识别改善。原始2950图已在完整缓存frames/frame_00002950.png，无需索取视频。

## 5. 本轮结束及下一步纪律

实现/测试/分析已在同一分支。未修改生产三模块、默认后端/参数、main或旧二进制，PR保持草稿。先用固定版本公开能力做识别层最小对照，证明05—08改善后回归完整8条与Office；g18检测定位已完成，不再重复原样实验。随后按台账依次闭环其他内容单元，而不是只增加文件数或测试数。

三个模块、一条本地顺序流水线、一个默认PP-StructureV3后端；只做薄适配，不自造OCR、表格/配准求解器或复杂平台。保留全部原生证据，不改原文、单元格、验收锚点或指纹骗缓存。无新增Office生成/渲染验收必须明确；完整内容、其余接缝、密集表格和其余视频仍未通过。每轮20分钟内简短总结真实完成/失败/未完成，详细记录进仓库，不承诺后台自动交付。
