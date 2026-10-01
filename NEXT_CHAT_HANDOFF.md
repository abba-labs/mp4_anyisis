# 当前交接：本地OCR零成功，端到端交付尚未完成

更新：2026-10-01。用户反馈最新上传效果很差。本次已读取上传提交、原报告、环境、日志、JUnit和实际测试SHA；结论以运行日志为准，不再以回归数量代表文档提取效果。

**当前状态：REGRESSION_RESULTS_RECORDED / OCR_EXECUTION_BLOCKED / END_TO_END_NOT_COMPLETED。**
这不是截图准确率已经测出很低，而是这次上传的真实OCR没有成功执行。不要继续使用`LOCAL_REGRESSION_PASSED_BATCH_VERIFIED`作为整体交付状态。

## 1. 当前事实与唯一接续入口

最新执行核查及连续执行要求：
**[docs/screenshot_runs/20261001_191329_windows_local/EXECUTION_REVIEW.md](docs/screenshot_runs/20261001_191329_windows_local/EXECUTION_REVIEW.md)**。

核查的上传提交：`88fc04797af9e4bc52b520824ea00ef668062523`。
实际测试基线：`tested_commit.txt`记载`3c13a5622007394c6603fd998a6dda7ded427928`，与上传提交父节点一致。原报告另一完整SHA为文字记录不一致，不能用它覆盖实际文件。

| 环节 | 上传证据支持的状态 |
|---|---|
| 针对性/仓库回归 | 上传记录20通过；全量130通过、8跳过。不是真实OCR通过数 |
| 裁图 | 报告记载34+27张就绪；未上传完整裁图/ROI文件，未由ChatGPT目视确认全部边缘 |
| EFC详细设计识别 | run.log：1 FAILED、33 BLOCKED、0缓存；成功OCR为0/34 |
| EFC LRS识别 | 引擎初始化失败，组级FAILED；27张没有成功OCR结果 |
| 真实Word | run.log明确缺少Pandoc，未完成导出 |
| 模型修订 | 无本次真实差异、应用记录与修订稿的提交证据 |
| 12.0650秒 | 失败执行的墙钟，不是61张OCR速度 |
| 原图安全 | 上传的前后hash清单相同；这不等于内容恢复正确 |

环境清单缺paddleocr/paddlex/paddlepaddle/numpy/OpenCV；日志也记录paddlex为None。回归跳过明确包括缺numpy和Pandoc，不应全部描述成Linux专属依赖。原报告、JUnit、日志不改，核查为追加记录。

## 2. 已提交的最小交付保护

代码提交：`187a1077261082d1aa28c83fa29ba33e1af53ea1`。
仅修改已有`src/mp4_analysis/thin/batch_cli.py`，没有更换OCR、裁剪工具或另建平台：

- 多组`run`启动前发现当前解释器必要模块缺失，或用户请求Word但找不到Pandoc时，返回`ENVIRONMENT_BLOCKED`及退出码2，不进入批量OCR/自动文档组装；历史状态保留。
- 新增`doctor`动作，显示真正使用的解释器、缺失模块和Pandoc位置；不安装、不下载、不加载模型。
- 模块存在但后续实际模型运行仍失败、成功OCR为零时，标`OCR_FAILED`，禁止自动生成“全截图回退”交付包。
- 集合结果明确记录`successful_ocr_inputs`。部分成功仍可以产生带缺口候选，不能标完整通过。
- `prepare`继续独立于OCR安装；不要求采集电脑安装推理环境。

**该补丁已提交、未在ChatGPT侧运行验证。** 预检只发现模块和程序存在，不证明动态库、模型权重、固定转换器版本或内容质量可用。单独build的诊断性证据回退仍保留，不作为零成功的正常业务交付。

## 3. 本地下一步：一次完成真正的两组提取及修订

不要再只交“错误处理通过”。执行Agent先检查现有解释器，优先复用已经可用的Python3.10—3.12 OCR环境；当前Windows宿主Python3.13能跑pytest，不证明已经装好解析引擎。缺失环境则在授权测试电脑准备受支持的虚拟环境，按`pyproject.toml`补齐`.[parser,document,dev]`及现有导出器要求的Pandoc3.1.11.1，不卸载系统环境、不清模型缓存、不索要用户重复截图。

以下`python`始终替换为同一个已确认环境解释器：

```bash
python -c "import sys; print(sys.executable); print(sys.version)"
python -m mp4_analysis.thin.batch_cli doctor examples/screenshot_collection.json
```

发现缺项就补齐再执行，不把`PREREQUISITES_PRESENT`当内容PASS，也不要在“包已装好”处停工。

```bash
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
# 查看本次两组完整裁图，使用当前真正生成的批准ID。
python -u -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

已有真实ROI配置和61张输入继续复用；报告里的坐标不能替代未归档的配置。区域位置变化的例外按既有方式覆盖，不用full-image绕过文档范围确认。同机同项目恢复保留成功缓存和失败记录；换处理电脑导致来源根变化时使用新的短输出根，不删除旧身份记录。

运行成功后继续用本地已有获准看图能力读包内review_tasks.json与evidence裁图，输出真实差异，并经document_cli inspect-review/apply生成修订稿。不要部署另一视觉服务，不把模型未运行写成已优化。

本轮交回：两组实际成功/失败/未运行数量、工具初稿和修订稿、Word/表格/content、ROI配置和运行manifest、逐图报告与export_report、真实模型差异、抽检分子分母、耗时和可观测用量。归档到新的`docs/screenshot_runs/<RUN_ID>/`或获准可取回的稳定工件，不能只有D盘路径。未全部正确也同步，但必须如实。

## 4. 已有文档继续复用

- [R1—R6交付与测试规程](docs/SCREENSHOT_FIX_DELIVERY_20261001.md)：补丁用例与完整运行检查，禁止用跳过掩盖未验证功能。
- [批量入口](docs/SCREENSHOT_BATCH_RUN.md)：多组准备、批准、执行和恢复。
- [文档与视觉意见格式](docs/SCREENSHOT_DOCUMENT_OUTPUT.md)：build/inspect-review/apply/reexport。
- [示例计划](examples/screenshot_collection.json)：两组来源及区域配置路径。

单独回归仍有价值，但成果首屏必须是“实际识别多少、产物是什么、剩余什么问题”，不再先报20/20、130通过。此次新增批量保护也需在本地核对缺依赖阻断、零成功抑制导出和正常真实运行，不拿新代码落库冒充测试结果。

## 5. 持续边界

仓库`abba-labs/mp4_anyisis`，分支`feat/open-source-thin-pipeline-20260928`，草稿PR#3。开始/推送前查询实际head，不改main、不强推、不合并或改PR/工作流。原图、原native、旧候选和原始失败记录不覆盖，不记录凭据，不自动清锁。

只处理指定区域，取消/越界不退回整屏。没有恢复视频路线，也没有新增OCR后端。上下标等不能安全解释的结构保留区域图并标未决，不伪造可编辑恢复。不自动跨截图去重、拼表或恢复不可见内容，模型声明已阅不等于独立内容验收。

`screenshots.py`此前被拦截的修改未重试；批次目录仍为64位hash，Windows使用短输出根。历史视频工作流未修改、不作为截图业务验证入口。

本轮未取得当前截图二进制可视副本，未目视核对ROI；未看到本次未上传的Office产物，未启动本地测试电脑、OCR或视觉调用。不能将这次执行失败外推为截图方案必然不可行，也不能承诺补齐环境后准确率必然达标。
