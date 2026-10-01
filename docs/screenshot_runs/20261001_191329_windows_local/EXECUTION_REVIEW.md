# 本次上传核查：回归有结果，但OCR零成功，端到端交付未完成

核查日期：2026-10-01。
核查上传提交：`88fc04797af9e4bc52b520824ea00ef668062523`。
实际测试基线：`tested_commit.txt`记载`3c13a5622007394c6603fd998a6dda7ded427928`，与上传提交的父提交一致。
原TEST_REPORT.md及根交接中的另一条完整SHA与此不符；以实际tested_commit.txt为准，原记录保留，不回填测试数据。

## 1. 结论

**REGRESSION_RESULTS_RECORDED / OCR_EXECUTION_BLOCKED / END_TO_END_NOT_COMPLETED。**
不能使用`LOCAL_REGRESSION_PASSED_BATCH_VERIFIED`表达业务链路已经通过。缺引擎时能正确报错是故障处理结果，不是正常OCR或资料恢复通过。本次也不能据此判定截图OCR路线本身的准确率。

核查依据均来自本目录提交文件：

| 项目 | 上传证据 | 正确解释 |
|---|---|---|
| 针对性回归 | fixes.xml与TEST_REPORT.md记录20通过 | 既有补丁的这些用例得到运行结果，不证明真实资料识别质量 |
| 仓库回归 | regression.xml记录138项、8跳过、0失败 | 130通过；跳过包含缺numpy及多项缺Pandoc的真实导出测试，不是报告所称都属于Linux特有依赖 |
| 裁图 | 报告称34+27张准备完成，ROI为[71,140,1849,958] | 这是准备记录；本次提交未附实际ROI JSON/全部裁图预览，尚不能从报告文字确认所有页面边缘正确 |
| 详细设计OCR | run.log：FAILED 1、BLOCKED 33、cache_hits 0 | 成功OCR输入为0/34；不是34张识别完成 |
| LRS OCR | run.log：Native engine failed to initialize，组级FAILED | 27张没有进入成功OCR；不能写第二组业务处理通过 |
| Word | run.log：Pandoc executable is required for document.docx | 本次Word导出未完成 |
| 视觉优化 | 提交未包含实际模型差异、应用记录或新修订稿 | 没有完成证据，不能说已经跑通工具+模型效果验证 |
| 12.0650秒 | wall_clock.txt及run.log | 是本次失败调用的墙钟，不是61张识别吞吐或完整交付时间 |
| 源文件保护 | pre/post文件内容同一blob | 上传的前后记录一致；不能将这一结果混同于提取正确 |

环境清单中没有paddleocr、paddlex、paddlepaddle、numpy或OpenCV；日志也记录paddlex版本为None。Python3.13.7本身不是本次缺依赖的全部解释，更不能声称改一个Python版本就解决识别问题。关键是运行命令使用的那个解释器必须具备真实解析环境。

本次提交只有报告、JUnit、日志和环境/哈希记录，没有本次实际Word、Excel、冻结content、模型返回或可取回的成品包。run.log里的Windows绝对路径不是其他机器可以直接读取的归档地址。

## 2. 已定位的交付逻辑问题与本次补丁

原批量入口捕获ScreenshotRunError后，无论成功识别多少张都会调用文档组装器。组装器设计上会为没有native内容的单元保留裁图。这种证据回退不能成为“识别成品”，尤其当成功OCR数量为零。

补丁提交：`187a1077261082d1aa28c83fa29ba33e1af53ea1`，只修改已有`src/mp4_analysis/thin/batch_cli.py`：

- `run`先检查当前解释器的必要模块及所请求Pandoc的存在性。缺项返回`ENVIRONMENT_BLOCKED`、退出码2，保留历史状态，不进入模型或自动文档组装。
- 新增同入口的`doctor`动作，报告实际解释器、缺失模块、版本及Pandoc位置；不安装、不下载、不初始化模型。
- 即使预检有模块而模型运行失败，成功OCR输入为零时也不自动生成文档交付；显示`OCR_FAILED`和`successful_ocr_inputs=0`。
- 批次索引及状态明确显示成功OCR数量；数量仍不是准确率。部分成功可以保留带缺口的候选，整体继续如实失败。
- `prepare`仍不要求安装OCR，采集/选框电脑与推理电脑可以分开。
- `doctor`的`PREREQUISITES_PRESENT`仅代表发现模块与可执行文件，不证明动态库能加载、模型已准备、Pandoc版本符合或内容质量通过。
- 未更换后端、未修改截图算法、未修改工作流、未删除旧失败候选。单独build的证据回退仍可用于诊断；本次限制的是批量入口的自动交付。

**这项补丁没有在ChatGPT侧执行测试、OCR或Office验收。** 它防止重复做无效执行和误认成品，不是识别质量改进的实测结果。

## 3. 本地现在连续完成一件事：真正识别两组并交回成品

不要重新画架构，不再只交一次“错误处理通过”的报告。缺依赖应由执行Agent处理环境或报告明确阻塞，不能把业务未运行标作成功。

### 3.1 确定真正的运行环境

先检查现有环境及实际解释器位置。以前测试机的Python3.11环境不等于这台Windows宿主已经存在同样环境，不要直接运行系统Python后假定它包含OCR。

```bash
python -c "import sys; print(sys.executable); print(sys.version)"
python -m mp4_analysis.thin.batch_cli doctor examples/screenshot_collection.json
```

所有后续`python`必须使用同一个已核对的解释器。优先复用已经可用的Python3.10—3.12 OCR虚拟环境。不存在时，执行Agent在这台已授权测试电脑准备一个受支持环境，并按仓库声明安装`.[parser,document,dev]`；不要污染或卸载系统环境，不锁Python补丁版本。已有环境只补缺失项，不清空模型缓存。Python3.13的真实OCR兼容性本次没有验证，不因pytest可执行就扩大支持声明。

Word按现有导出器需要Pandoc3.1.11.1。确保所用进程能找到可执行文件，或在集合计划export.pandoc指定已有程序的绝对路径。不要用关闭Word导出替代用户要求的Word交付。

### 3.2 复用截图和区域，连续执行

保留本次61张原截图、既有ROI及失败记录，不要求用户重新截图。使用本机实际ROI JSON；报告里的坐标不能代替缺失的文件。边缘/页面位置有变化的例外应在该组配置中覆盖，不自动回退全屏。

```bash
python -m mp4_analysis.thin.batch_cli doctor examples/screenshot_collection.json
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
# 使用当前预览真正生成的approval_id，不复制旧报告中的值。
python -u -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

doctor发现缺项先补齐，再连续执行，不为每一步等待聊天批准。若只是在同一个项目恢复，保留原输出和缓存；在另一电脑迁移来源根路径时用新的短输出根，不强行删除原项目身份标记。

本次实际运行之后，用现有获准视觉能力处理文档包review_tasks.json及evidence裁图，生成真实差异，按既有document_cli inspect-review/apply形成新修订稿；不部署另一套模型服务。看不清的内容标未决，不抄expected_text。

### 3.3 完成标准与归档

业务报告第一屏必须是以下结果，不再先突出测试数量：

- 两组各自输入数、成功OCR数、失败数、未运行数；新的`successful_ocr_inputs`取本次程序记录，而非裁图READY数。
- 实际生成的整份Word、表格文件、content.json及图片证据；失败项如实列出。不把全图回退包当可编辑识别成果。
- 工具初稿及模型修订稿，真实模型差异和应用记录；无模型执行则明确NOT_RUN。
- 文字/关键字段/表格的源位置抽检数、正确/错误/缺失/未决数；ROI边缘检查与内容准确性分开。
- 全流程和分阶段墙钟、实际模型用量。失败调用不作为成功吞吐；没有账单信息时金额未知。
- ROI配置、裁图/输入manifest、逐图report.json、collection_status.json、export_report.json及日志，与实际产物一并提交到新的`docs/screenshot_runs/<RUN_ID>/`。大文件可以放获准且可取回的稳定工件，必须有位置和hash，不能只有测试机本地路径。

回归仍按已有交付文档执行并记录真实跳过原因；本次新增入口至少核对缺依赖阻断、零成功不自动导出和正常真实批次三条路径。不必全部内容正确才同步结果，但不成功的项目不能标PASS。

## 4. 本次审阅边界

已经读取最新提交、根交接、TEST_REPORT、run.log、environment、JUnit和上传文件目录，并核对了实际测试SHA。本次无法取得截图二进制的可视副本，未目视确认ROI，没有看到未上传的Office文件。没有把“未上传”推定为其他电脑永远不存在该文件；结论限定于这次上传的执行和证据。

不修改main、不强推、不改PR或工作流。原TEST_REPORT、日志和JUnit原样保留，本文为追加审阅与执行纠偏。
