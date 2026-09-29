# 新对话交接：mp4_anyisis

> 更新：2026-09-29，第十三轮。没有新增真实OCR或成品验收；运行环境仍阻塞。已交付可直接调用现有脚本的两帧输入包及无推理预检，不将准备工作算作资料恢复。
> 进入head：62cd6774770d7960a68ee72780c3e5352c7502d7；实现/回归提交d99ff89a2ae2c65a25e55145b6a451d8a6da06bf。接续前查PR #3及分支实时head；不改main、不自动合并。

## 0. 当前摘要

| 项目 | 已核验事实 |
|---|---|
| 分支/PR | feat/open-source-thin-pipeline-20260928，草稿PR #3，未合并 |
| 既定流水线 | 原57项已处理，0待处理；不代表源资料完整 |
| 内容验收 | 11个一级资料单元仍0完整通过，4有已知失败、7未完成核对；原57项的8条约束仍4个完整锚点命中 |
| 新诊断执行 | 原两帧×两种识别器4项仍执行0、待执行4；只优先选择mobile两项，不算完成率改变 |
| 本轮实现 | 现有文本对照脚本支持--recognizer及--preflight，返回参数漂移会留原生JSON并报错；新增本地包入口 |
| 真实预检 | 两张输入及对应原生导出哈希通过；BLOCKED_RUNTIME，退出2，执行0项 |
| 当前环境 | 沙箱Python3.13.5，缺三个Paddle包和Python3.11；公开依赖域名DNS失败，下载失败 |
| Harness | 只读capabilities返回404，客户端300秒未出现；当前暴露工具也只有只读健康/能力查询，不能假定可执行代码 |
| 先前拒绝 | 没有重建或经其他端点绕过被拒绝的saved-text-recognition.yml |
| 运行包 | mp4_step13_two_frame_run_bundle.zip，841220字节，选择性输入包，不含解释器/依赖/模型，不是新OCR结果 |
| 原始证据 | 完整原ZIP未改；包中12个原工件成员逐字节核对相同，含2帧、9个native文件和原report |
| 测试 | 本地相关16项通过；现有固定环境CI153通过、0失败/错误/跳过，包含模拟引擎测试，不是OCR准确率 |
| 新Office/新增通过 | 均0，没有新增Word/Excel或视觉验收 |
| 下一动作 | 在获准且已配置固定依赖的Python3.11环境真实跑mobile两帧，返回raw_ocr.json及summary.json；不要再重复静态审计 |

详细记录：[step13执行准备](docs/step13_execution_readiness_2026-09-29.md)、[机器证据](docs/step13_evidence.json)。上一轮完整交接、全部历史工件与研究边界保留在[固定提交62cd677](https://github.com/abba-labs/mp4_anyisis/blob/62cd6774770d7960a68ee72780c3e5352c7502d7/NEXT_CHAT_HANDOFF.md)。旧TASKS.md及REFACTOR_PLAN.md仍不是当前执行计划。

## 1. 接续阅读

先查实时head，再读本页和step13记录/JSON、scripts/probe_saved_text_recognition.py、scripts/run_text_control_bundle.py、tests/test_saved_text_preflight.py。诊断源原文在docs/step11_evidence.json的limit_clauses；stage归因以docs/step12_ocr_provenance_2026-09-29.md为准。

不要重复g18、g78、47处只读扫描或旧31/26续跑。最终overall_ocr_res经过版面重组，不能当成首次GeneralOCR快照；仍未捕获第2950帧实际清空轨迹。没有新推理证据前，不修改默认模型或上游重组算法来制造通过。

## 2. 当前证据

完整57项基线：run36439891744 / artifact10978920126，103046931字节，SHA256：
`6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86`。
到期2026-10-28T15:06:46Z，根restored/sarc。原五份MP4已在仓库MP4目录，不索要重传。旧344个native成员没有被本轮重推理或改写。

本轮回归：run36504291037 / artifact11006127883，4974字节，SHA256：
`951e2f4e9355d26b2b60a1d462dddc146c4ac8deb2335ad31f9948d449cc59e9`。
到期2026-10-29T00:41:41Z；已下载并核实JUnit153通过、0跳过。

本轮选择性运行包SHA256：
`ff69c1ce0d20c01c056508bc1606c7e87bb4fbfffdde434b692e04a69b813ab1`。
文件名mp4_step13_two_frame_run_bundle.zip，841220字节。该文件通过当前对话交付，没有作为GitHub Actions新推理工件上传；不能编造artifact ID或假定sandbox永远可用。

包内baseline/sarc只有2920、2950两帧及对应完整9个native文件。原report.json逐字节保留仍登记57项，其他55项没有打包。这是显式选择性副本，不是完整57项恢复。所有入口文件有bundle_manifest.json哈希；expected_text与原仓库文件逐字节一致，不参与改写输出。

## 3. 执行命令与范围

在已安装固定项目依赖和模型的Python3.11环境中，进入包解压目录：

```bash
python scripts/run_text_control_bundle.py --preflight
python scripts/run_text_control_bundle.py
```

Windows Python启动器可用py -3.11替换python。输出为results/mobile；现存目录拒绝覆盖，可传--output指定新目录。请保留整个结果目录，包括summary.json、两份raw_ocr.json、源图和baseline_layout.json。

直接使用完整基线：

```bash
python scripts/probe_saved_text_recognition.py work/full/restored/sarc --recognizer mobile --preflight
python scripts/probe_saved_text_recognition.py work/full/restored/sarc --recognizer mobile -o work/mobile_before_layout
```

预检只验证选中输入、Python3.11及paddleocr3.7.0/paddlex3.7.2/paddlepaddle3.2.2元数据，不导入Paddle、不下载模型、不推理；返回2表示环境不符合。它不证明所有依赖可导入或模型可用。实际运行继续沿用原固定环境OpenCV4.10，已保存参数为limit_side_len736、limit_type=min、thresh0.3、max_side_limit4000、box_thresh0.6、unclip_ratio1.5、text_rec_score_thresh0。

先只跑mobile组确认第08条在版面重组前是否存在，再决定是否需要server识别器对照。完整4项计划仍未执行，不通过删掉server计划抬高比例。当前脚本无参数时仍保留原四项行为。

## 4. 必须维持的边界

三个逻辑模块、一条本地流水线、一个默认PP-StructureV3解析后端。只做薄适配，不重造OCR、表格/配准求解器或复杂平台；不强推、不改main、不自动合并、不索要PAT。

源标点、下划线、编号、单元格和验收真值不改；不拼正确原句替代识别。保留原图/原生输出/指纹，未验证不接入默认。g18分格、文字污染、全部内容覆盖、接缝、密集MemoryMap、全部Office及其余视频仍未验收。

本轮源码、测试、记录均提交当前分支。没有新的识别修复，不提高整体完成百分比。运行环境未可用时应明确阻塞，不反复用新脚本/回归数量替代真实结果。每轮20分钟内结束并报告真正完成、失败和未完成项。
