# 新对话交接：mp4_anyisis

> 更新：2026-09-28，第九轮。57个既定解析输入已完成；本轮只针对现成结果改进Word导出，内容验收仍FAIL。不要按旧31完成/26待处理重新运行。
> 本轮进入head：7581f4e3ff1b513f4843c19d6bd882589023a7df；实际完成固定环境回归的实现提交：136bbafbdb95b12eca2b83afc921015f714347da。开始前必须查询PR #3实时head。

## 0. 当前接续摘要

| 项目 | 当前事实 |
|---|---|
| 仓库/分支 | abba-labs/mp4_anyisis / feat/open-source-thin-pipeline-20260928 |
| PR | #3，草稿、未合并；main未改，不强推、不自动合并 |
| 架构 | 三个模块、一条本地流水线、单一PP-StructureV3解析后端，薄适配 |
| 原处理计划 | 110张一秒抽样画面，17候选+40原帧=57个输入，57完成、0待处理；抽样不证明覆盖 |
| 本轮实现 | output.py新增显式Pandoc重导出及脚本，不替换默认原生Word，不重跑57项OCR |
| 重导出 | 57尝试，56派生Word，1拒绝：group_000078_a原生异常HTML经转换丢失文字，已拦截 |
| 原生证据 | 344个native文件与原工件逐字节一致，未改输入、缓存、原生Word/Excel |
| 表格改善 | 成功输出27张表的网格、合并、位置及文字与对应原生XLSX一致；同组旧Word仅13张一致。这不是27张表对源视频全正确 |
| 视觉检查 | 查看4份最终派生Word；架构图未新增裁切。第二张表的源识别错误造成窄列挤压仍存在，其余52份未逐页视觉检查 |
| 回归 | 固定Python3.11/OpenCV4.10/Pandoc3.1.11.1：111通过、0失败、0跳过 |
| 内容结论 | FAIL。OCR污染、部分条款/编号、异常表格、全片覆盖、全部接缝、密集MemoryMap仍未解决 |
| 下一步第一件事 | 用既有源帧和映射定位group_000078_a异常表格起源，不硬改单元格、不重跑全片 |

详细本轮记录：[docs/step9_word_export_2026-09-28.md](docs/step9_word_export_2026-09-28.md)。机器证据：[docs/step9_word_export_evidence.json](docs/step9_word_export_evidence.json)。第八轮内容记录及恢复证据仍保留在docs/step8_content_review_2026-09-28.md和docs/resume_evidence_2026-09-28.json。

## 1. 先读哪些文件

先查实时PR head，再依次读本文件、step9记录与JSON、src/mp4_analysis/thin/output.py、scripts/export_saved_word.py、scripts/check_saved_word_export.py、tests/test_saved_word_export.py、tests/test_word_export_loss_guard.py。检查输入问题时再读video.py和reconstruction.json。

前七轮全部约束、否定方案和研究方法保留在[原交接固定提交](https://github.com/abba-labs/mp4_anyisis/blob/76e5fd9de4d7065e35cc31359959859046bf5404/NEXT_CHAT_HANDOFF.md)。第八轮接续入口保留在[上一交接固定提交](https://github.com/abba-labs/mp4_anyisis/blob/7581f4e3ff1b513f4843c19d6bd882589023a7df/NEXT_CHAT_HANDOFF.md)。旧TASKS.md/REFACTOR_PLAN.md不是当前开发计划。

## 2. 当前完整缓存与运行证据

首选已完成工件：run36439891744 / artifact10978920126，103046931字节，SHA256：
`6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86`。
到期2026-10-28T15:06:46Z。ZIP内已完成输出为restored/sarc，保留原31项完整ZIP。不要返回只完成31项的旧工件做无效恢复。原始五份MP4仍在仓库MP4目录，不需要再次索取。

解析指纹仍为`878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb`，配置未变：sample_seconds=1、start=0、无end/max_frames/ROI、reconstruct=True、mobile、table_mode=default、CPU2线程、MKLDNN、word=True。原解析环境Python3.11.16、PaddleOCR3.7.0/PaddleX3.7.2/PaddlePaddle3.2.2/python-docx1.2.0/OpenCV4.10。

本轮回归：run36444198176 / artifact10978754667，SHA256：
`22c09b88ccd8af62d5b018e8f77a04a9a6e9cc05a4b9c5f8fdddcfa606e739a2`，到期2026-10-28T15:31:47Z。111通过，包含19项新输出回归，不是111项内容准确率验收。

本地导出实验Python3.13.5，110通过/1跳过（无PyAV）；不冒充正式环境。临时sandbox文件不保证跨会话存在，不能只凭旧链接宣称已取得工件。

## 3. 现成结果如何只重导出Word

安装外部Pandoc3.1.11.1及python-docx1.2.0，运行：

```bash
python scripts/export_saved_word.py work/step8/restored/sarc -o work/step9_word
python scripts/check_saved_word_export.py work/step8/restored/sarc/native work/step9_word -o work/step9_word_comparison.json
```

支持单个native/job目录；输出必须是新的、不与源包含的目录。原生文件哈希或导出状态不合格、外部资源、缺图、转换警告、超时、表格文字丢失均拒绝。批量结果记录export_summary.json；本工件预计group_000078_a被拒绝，不能把非零退出码隐去。

这是可选输出能力，不是另一个解析后端；原Word继续作为未修改证据保留。每个成功目录保存中间HTML、参考DOCX、document.docx和export.json。中间HTML的图片仍依赖源缓存；派生Word重排不代表原始版面复原。

## 4. 已定位的原因和边界

PaddleX3.7.2的word_converter.py在_parse_html_table丢弃rowspan/colspan，在_write_block按每行物理单元格填充，导致合并消失及SARC从B2错到A2。Pandoc同源HTML转换保留合并。

必须关闭markdown_in_html_blocks，否则“+ I”会变成列表，导致181/211表格损坏。group_000078_a异常原生HTML多出的单元格会被Pandoc静默丢弃；当前发布前文字顺序检查能拦截，不是修好了异常结构。未手改文字、列数或锚点。检查表格映射用完整HTML精确匹配，不按文件编号猜阅读顺序。

frame452的原生“SARC 20:1”、V1.0+、图形标志文本化仍错；复位2890的O1/缺02仍在邻帧核对范围内；原架构图证据不能推导所有跨屏图恢复成功。

流程注意：首个output.py提交意外触发旧六画面OCR工作流36443563353，原生执行成功、内容门禁失败。它不是输出改善证据，也没有修改57项缓存。后续输出修正避免再次触发，独立adapter-tests运行全111项。不要声称整轮完全没有任何OCR执行。

## 5. 下一步及纪律

第一动作：从已完成工件reconstruction.json定位group_000078_a成员、源图到候选映射，对照保密等级行和各单元格，判断异常源自拼接还是解析结构；先读固定版本上游代码，再做仅改变一个因素的最小实验，保留原产物。证明改善并经第二个同类样本验证后才接入，不盲换后端。

随后是章节/条款覆盖清单、录屏污染、首次效率及正确源位置去重；密集工作表仍单独研究。不用文件数、测试数或与原生XLSX一致冒充资料恢复正确。不启动旧31/26恢复工作流，不修改start/抽样伪装续跑。

每轮修改、测试和分析同分支提交，更新本页；main和旧二进制不改，PR维持草稿。普通回复简短，详细记录进仓库；每轮20分钟内总结真实已完成、失败、未完成，不承诺后台交付。
