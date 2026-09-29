# 新对话交接：mp4_anyisis

> 更新：2026-09-29，第十二轮。原57项仍完成，整片内容仍FAIL。本轮纠正“最终overall_ocr_res就是原始OCR”的错误归因，完成57份结果只读检查；新的两帧OCR对照因创建工作流被工具安全检查拦截，实际没有运行，也没有新Office产物。
> 进入head：7439828860937531464afa7af83459d497c11bb8；代码/固定环境回归提交804555688abc4505316ab8957672ba712ca31923。开始前查询PR #3及分支实时head，不修改main、不自动合并。

## 0. 当前接续摘要

| 项目 | 已核实事实 |
|---|---|
| 分支/PR | feat/open-source-thin-pipeline-20260928；草稿PR #3，未合并 |
| 架构 | 三个逻辑模块，一条本地流水线，单一PP-StructureV3默认后端，未改默认参数 |
| 原计划 | 110张一秒抽样画面，17候选+40原帧=57输入；57完成、pending0；不证明内容完整 |
| 原生证据 | 与原ZIP逐字节比较344个native文件，0变化 |
| 重要纠正 | PaddleX3.7.2的standardized_data会清空/替换overall_ocr_res.rec_texts，因此最终JSON不是未经修改的首次OCR快照 |
| 只读扫描 | 57份结果、287个登记导出文件通过哈希核对；24份结果有空文字且分数保留的观察，共47处。不是47处已确认漏行 |
| LIMIT.08 | 源2950首行清楚，最终索引6为空且分数0.99185；源码存在清空路径，但尚未捕获该帧原执行轨迹，不能断言首次识别为空 |
| 新对照脚本 | probe_saved_text_recognition.py已提交；计划两帧×两种既有识别模型，共4项，实际执行0、待执行4 |
| 执行阻塞 | 新建saved-text-recognition.yml被OpenAI工具安全检查拦截；没有创建/运行该工作流，没有通过其他端点绕过 |
| 回归 | 现有回归工作流正常执行；固定环境145通过，0失败/错误/跳过，非OCR准确率测试 |
| 资料验收 | 仍0/11个一级单元完整通过，4有已知失败、7未完成核对；原57项中的约束完整锚点仍4/8 |
| 新Office | 0；没有本轮Word/Excel或视觉验收，没有新增整片通过样本 |
| 下一唯一动作 | 取得获准的执行路径，运行已提交两帧GeneralOCR对照，先看原mobile模型在版面重组前能否保留第08条 |

本轮详见[step12报告](docs/step12_ocr_provenance_2026-09-29.md)、[机器证据](docs/step12_evidence.json)。第十一轮完整交接保留在[固定提交7439828](https://github.com/abba-labs/mp4_anyisis/blob/7439828860937531464afa7af83459d497c11bb8/NEXT_CHAT_HANDOFF.md)，其中关于最终overall_ocr_res等同原始OCR的表述由本轮纠正；其余约束、工件及历史链接继续有效。

## 1. 阅读顺序

先查实时head，然后读本页、step12报告和JSON；再读scripts/probe_saved_text_recognition.py、scripts/audit_post_layout_ocr.py及对应两份tests。原生产入口仍是src/mp4_analysis/thin/parser.py、output.py、video.py和pipeline.py。台账为tests/fixtures/sarc_review_units_v1.json，8条原文在docs/step11_evidence.json的limit_clauses。

不重复g18检测、g78模式对照、旧31/26续跑或完整视频。TASKS.md、REFACTOR_PLAN.md仍是历史大框架方案，不按其重新设计。

## 2. 完整缓存与运行证据

### 57项完整缓存，优先复用

run36439891744 / artifact10978920126，103046931字节。
SHA256：6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86。
到期2026-10-28T15:06:46Z。完整输出根restored/sarc，新摘要是restored/resume_summary.json；restored/summary.json仍为历史31/26，不要误用。

五份原始MP4已在仓库MP4目录，不再索取。SARC视频SHA256：e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a。
原解析指纹：878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb。
参数不变：sample_seconds=1、start=0、无end/max_frames/ROI、reconstruct=True、mobile、default、CPU2线程、MKLDNN、word=True。
固定解析环境Python3.11.16、PaddleOCR3.7.0、PaddleX3.7.2、PaddlePaddle3.2.2、python-docx1.2.0、OpenCV4.10.0.84、PyAV16.0.1；Pandoc3.1.11.1只是可选输出转换器。

### 第十二轮回归

run36502469518 / artifact11005258557；SHA256：7869d2623ee3b835695e2ed47a8801b417421459f8906b0ae0edfc457a00d7d4。
到期2026-10-29T00:20:00Z。JUnit实际读取145通过、0跳过。新增14项是脚本输入和证据归因防护，不是新增14项内容通过。本地只新跑审计6项，不能说本地做了全部固定环境回归。

### 原有隔离证据仍保留

g78/g18四项：run36496321097 / artifact11003745957，SHA256 4b15309ca4a4ece0f0635e060db59559e544fe14862e17b5220ddae2c5de6780。
g18五项检测：run36500318940 / artifact11005180919，SHA256 855812fd8b7f3928a6cef964bec6b3aa3c6771ac3a9420c0d3b1d17dd8b111b5。
这些均已实测，不再为拿到同一结果重跑。

本轮还只读查看历史原生样本artifact10972499264：旧默认模型的frame2891已经有完整LIMIT.05，但帧/配置与57项基线不同，不能混入基线或当作本轮修复。详情和哈希在step12_evidence.json。

## 3. 下一步具体做什么

先解决获准执行入口，再运行已经提交的scripts/probe_saved_text_recognition.py；该脚本默认仅处理2920、2950两个已有source_frame任务，不调用视频、拼接或表格流程。第一组mobile detector+mobile recognizer，第二组同detector+server recognizer，保存版面重组前的原生JSON。实际运行后必须核对返回的检测参数、来源哈希和默认设置差异，不能仅凭构造参数自称与旧流水线完全相同。

先判断第08条在不换mobile识别器时是否原本存在。如果存在，进一步锁定版面重组清空；若确实没有，再研究识别。第07条下划线也以真正的前置输出作证。不能把已修改的overall_ocr_res当作前置快照，不能拼写正确原句覆盖模型结果。捕获真实改善后，再做完整8条及Word检查。

工作流创建被安全检查拦截是当前明确阻塞，不是模型失败，也不是GitHub测试失败；不要未经确认用其他端点重建同一被拒绝动作。本地本轮缺OCR依赖且DNS下载失败，不能假定本地可立即真实推理。没有新运行工件时继续写NOT_RUN，不能伪造运行ID或完成数。

## 4. 只读审计结果如何复核

```bash
python scripts/audit_post_layout_ocr.py work/full/restored/sarc -o work/post_layout_audit.json
```

原47处的job和索引已经完整写入step12_evidence.json，除非证据改变，不必每轮重扫。只读审计不是修复，不提高资料通过数。

源2950保存的长行框[197,146,1082,169]与细框[567,162,714,169.3287353515625]的small-overlap为0.955，但只覆盖长行面积约5.06%。这是上游清空条件的几何反例，不是捕获原分支的完整重放。没有证明实际调用顺序前不宣称已定位全部47处的共同根因。

## 5. 尚未完成与纪律

原8条完整锚点仍4/8、11个资料单元仍0完整通过，不能报告虚构整体完成百分比。OCR污染、编号/条款、g18结构、全部接缝与内容覆盖、密集MemoryMap、整片Office、其余视频及Windows/离线部署继续未验收。

只使用成熟开源能力做薄适配；不自造OCR、表格/配准求解器或复杂平台；不换大框架、不盲换模型。保留原生结果、原图、指纹和失败记录；不改原文/单元格/真值制造通过。新实现、测试、分析同分支提交，提交前重查head。main不改、PR保持草稿、不自动合并。每轮20分钟内总结实际完成、失败和未完成，详细记录入库，不承诺后台交付。
