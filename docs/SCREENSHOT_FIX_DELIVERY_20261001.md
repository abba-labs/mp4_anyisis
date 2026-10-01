# 截图版 R1—R6 修复交付与本地测试说明

日期：2026-10-01。
仓库：`abba-labs/mp4_anyisis`。
开发分支：`feat/open-source-thin-pipeline-20260928`；草稿 PR #3。

## 0. 本次交付是什么

本次修复基线是 `8428f253de9e9ef72f6b84e2c1010b3d32239fba`，对应此前源码审阅的 R1—R6。生产补丁和针对性回归用例已经提交；**ChatGPT 没有执行这些测试、OCR、模型调用、Word/Excel生成或渲染。代码状态为 PATCHED_AWAITING_LOCAL_TEST，不是运行已通过。**

本地的任务是按本文连续完成验证、记录真实结果并提交，不重新设计框架，不再沿用旧视频任务。先运行低成本回归，再连续验证两组截图，最后一次交付报告与实际文件；不需要每个步骤向用户请示。

固定分支，不改main、不强推、不合并或更改PR，不修改/触发历史工作流。开始和推送前核对实际远端head；本地有未提交内容先检查保护，不用reset/clean覆盖。

## 1. 修复对照表

| ID | 本次代码修改 | 本地必须证明 | 不能宣称 |
|---|---|---|---|
| R1 | `document_format.table_model`拒绝会丢语义的sup/sub/s等标记和不支持的样式；组装保留该表的区域图与unsupported_table记录 | `10<sup>3</sup>`绝不静默导出成普通103；普通文字表仍可转换；原生HTML不改 | 回退图片不等于恢复可编辑表格；没有新增公式OCR |
| R2a | 新`document_checks`按正文块/单元格比较，保留字间空格、重复空格、制表符与换行；HTML普通空格仍允许正常换行 | A B/AB、两个空格/一个空格、两个段落/一个段落能区分 | 不再把删除所有空白后的相等当通过 |
| R2b | Word检查正文中的图片引用顺序、关系、资源存在与解码像素身份 | 缺图、换图、乱序、断链必须报EXPORT_MISMATCH或导出错误 | 图片资源检查不证明版式、裁剪范围或文字识别正确 |
| R2c | 在转换前根据候选明确声明的行、物理单元格和span建立只读约束；分别比较转换器输出和存盘后XLSX | 空合并格、跨度、单元格位置/值/类型、声明范围改变必须报警 | 这不是从图像推断网格的表格求解器；没有自动修表 |
| R3 | `batch_cli.load_plan`仅全局检查语法/危险路径，普通源目录缺失转为逐组PREPARE_FAILED | 缺失组失败，可用组仍准备和处理；危险交叉路径仍整体拒绝 | 全部组失败不能写成处理成功 |
| R4 | 按证据图hash和该截图块内容hash累计review_coverage，当前pending重建为唯一项，历史另存 | 先查e1后查e2不会丢e1覆盖或残留e2待复核；修改未重查内容使该项失效 | 模型报告已看过不等于独立内容验收，critical未决不自动关闭 |
| R5 | 公共build同时保护原截图目录与整个单文档OCR项目；新包携带source_protection，apply/reexport继承 | 所有入口禁止向源树/受管理OCR树导出；集合deliveries合法兄弟目录仍可用 | 旧包没有保护字段时无法推断丢失的原路径，使用新build生成包 |
| R6 | 单组run和集合execute从准备前计时，准备/查缓存/parse调用等分开记录；CLI另外报告当前命令时间 | 人为准备延迟进入总时间；缓存旧timings不当成新推理，集合初次准备不漏记 | 函数计时不包含解释器启动；精确进程墙钟须额外从外部计量 |

没有更换OCR后端：OpenCV选框、Pillow裁剪、PP-StructureV3解析、Pandoc 3.1.11.1导Word、PaddleX 3.7.2现有转换器导Excel继续复用。`document_checks.py`仅执行只读一致性校验，不写入或推断网格。

## 2. 拉取代码和环境记录

在仓库根目录操作。以下`python`表示本机已经可用的虚拟环境解释器，例如Linux的`.venv-test/bin/python`；激活环境后可直接使用python。复用Python 3.10—3.12，不锁补丁版本，不为本次修复重新安装模型。

```bash
git status --short
git fetch origin
git switch feat/open-source-thin-pipeline-20260928
git pull --ff-only origin feat/open-source-thin-pipeline-20260928
git rev-parse HEAD
python --version
python -m pip check
python -c "import PIL, lxml, openpyxl, docx, pytest; print('local regression dependencies importable')"
```

遇分叉先检查并整合，禁止强推。已有依赖不升级；只缺个别依赖时按`pyproject.toml`声明补齐并记录实际版本。新安装命令才是`python -m pip install -e '.[parser,document,dev]'`；依赖已齐只注册新命令时使用`python -m pip install --no-deps -e .`。无需下载第二套OCR或部署新的视觉服务。

记录以下内容到`docs/screenshot_runs/<RUN_ID>/`，RUN_ID用本次实际日期时间与机器标识，不沿用旧报告名称：测试完整commit SHA、Python/包版本、操作系统、CPU/GPU/线程、模型配置、命令及退出码。不要记录凭据、Token、认证header或包含凭据的remote URL。

## 3. 先运行针对性回归，再运行仓库回归

Linux/WSL示例，Windows PowerShell可手动创建同名报告目录后运行相同python命令：

```bash
RUN_ID=$(date +%Y%m%d_%H%M%S)_local
REPORT="docs/screenshot_runs/$RUN_ID"
mkdir -p "$REPORT"
git rev-parse HEAD > "$REPORT/tested_commit.txt"
python --version > "$REPORT/python.txt"
python -m pip freeze > "$REPORT/environment.txt"
python -m pytest -q tests/test_screenshot_review_fixes.py --junitxml="$REPORT/fixes.xml"
python -m pytest -q --junitxml="$REPORT/regression.xml"
```

`tests/test_screenshot_review_fixes.py`为新交付用例：合成PNG、内存表格、python-docx小文档、伪时钟及目录夹具，不初始化Paddle、不调用视觉模型。**用例已写，未在ChatGPT侧执行；以本机实际收集/通过/失败数为准。**

如仓库全量回归另有旧脚本/依赖问题，保留失败日志和准确原因，不恢复video模块、不跳过有效测试制造全绿；与本次R1—R6回归结果分别记录。普通确定性代码错误在本地连续修复，必要改动和失败前后证据一起提交。不要再次花多轮重新调查已明确的六项机制。

## 4. 实际截图先确认区域，不重拍现有资料

输入仍是：

- `screenshots/efc详细设计文档/`：34张。
- `screenshots/efc模块lrs设计文档/`：27张。

61张是截图数量，不是文档页数或准确率。先保存两组源PNG和manifest的SHA256清单；运行结束再计算，必须逐字节未改变。临时失败/补图/排序测试只对工作副本做，不修改Git中的源截图。

已有真实ROI配置直接复用。没有配置时在有桌面的采集机操作：

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" --select-region work/regions/efc_detail.json
python -m mp4_analysis.thin.cli "screenshots/efc模块lrs设计文档" --select-region work/regions/efc_lrs.json
```

无GUI的测试机读取采集机提供的配置，不为此重装OCR。不要预填猜测坐标，不用`--full-image`绕过整屏的区域选择。按真实布局设置单图overrides，确认文字下缘、表格线、图形边框和页码范围；区域外工具栏/侧边栏必须排除。

```bash
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
```

打开输出的`collection_preview.html`及两组全部裁图。示例配置相对路径以`examples/`为基准，默认工作根是`work/screenshot_collection`；Windows可改为短绝对路径。每组区域/顺序有变化就重新prepare并取得新approval_id。

## 5. 连续跑完两组并记录完整墙钟

```bash
python -u -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

用本批真实批准值替换ACTUAL_APPROVAL_ID。完整运行前由外层终端计时，Linux可用`/usr/bin/time -p`，PowerShell可用`[Diagnostics.Stopwatch]::StartNew()`包住命令；保留退出码与标准输出/错误。不要只把函数elapsed当成进程全程时间。

新计时含义：

- 单组`report.elapsed_seconds`：run函数进入、裁图准备、解析/缓存直至最终报告快照；不含调用者后续文档总装和末次写报告。
- 单组`stage_timings`：prepare、cache_scan、cache_lookup、parser_call、other互不重叠；parser_call包含懒加载、推理及原生导出，不是纯推理时间。
- 集合`elapsed_seconds`：execute进入至最终快照，包含最初集合准备；initial_prepare + document_execution + other构成主分解。
- 每组`pipeline_stage_timings`是嵌套明细，**不能再次累加到集合总时间上**。批准后单组重复校验/准备的开销已经包含，不能隐去。
- CLI stdout的`current_command_seconds`是本次main进入至输出快照；`status`命令中的该值只是查询耗时，不是历史OCR耗时。
- 缓存中的`native.timings`是历史生产记录，不计为本次推理；实际用`inference_attempts_this_run`、cache_hits和cross_batch_cache_hits说明复用。

运行完一次交回两组所有输入的终态、实际产物和失败清单。局部内容错误记录后继续，不因一个标点停工或重跑全组。

## 6. 用已有原生结果重建新候选，不重跑OCR补导出

**本次改变了内容转换和校验代码。旧版content.json若已把上标压成普通字符，reexport无法恢复丢失语义。应从原生JSON重新build一个新候选目录；不是重做OCR。** 集合入口的交付身份已加入新校验代码hash，不会把旧校验生成的文档冒作新版本。

```bash
python -m mp4_analysis.thin.document_cli build ACTUAL_RUN_DIRECTORY -o work/deliveries/efc_fixed_tool_v1
```

已有新候选只有Office导出失败时，再使用：

```bash
python -m mp4_analysis.thin.document_cli reexport ACTUAL_NEW_BUNDLE -o work/deliveries/efc_fixed_export_v2
```

目标目录必须不存在。检查`export_report.json`：R2新增有序文本块/图片核查，Excel同时有`candidate_to_converter`和`candidate_to_saved`。EXPORT_ERROR/MISMATCH不能改成PASS；调查是输入不支持、转换确实改变内容，还是校验映射需要修复，不能改回删除空白或放宽标准。

R1回退只保留该表区域PNG；无法安全取得表bbox时才保留整个批准的文档裁图。两者都不得含ROI外像素。报告统计可编辑表格数与图片回退数，不能把图片回退当Excel准确恢复。

## 7. 恢复、失败隔离与修订要一并检查

在隔离的工作副本/测试计划中完成以下检查，生产原图和旧缓存保持不动：

| 检查 | 操作与必须结果 |
|---|---|
| 重复运行 | 同一输入与配置再次运行；未变成功页复用，实际推理尝试应为0（没有旧成功缓存的页除外），新耗时与旧timings分离 |
| 单页变化 | 工作副本更换一张同字节长度但不同内容PNG并同步manifest；重新确认批次；该页不得命中错误缓存，其他未变页可复用 |
| 区域变化 | 只改某页ROI；新批准值必需，受影响页身份改变，不能读取区域外原图 |
| 中断恢复 | 在工作副本运行中Ctrl+C，再执行同命令；成功结果保留，未完项继续；不自动删除仍被进程持有的锁 |
| 一组缺失 | 单独计划放入一个合法但不存在的源路径和一个可用组；prepare逐组记录，批准该部分计划后可用组运行；总状态PARTIAL_FAILURE |
| 分两次模型复核 | 第一份响应报e1已复核，针对新候选第二份报e2；e1/e2覆盖应累计，当前pending各一项且完成后退出；critical验收项仍在 |
| 修改影响覆盖 | 改一个此前已报告复核的单元但未重新声明复核；只使该单元覆盖失效，其他未变证据保留 |
| 目录保护 | 独立build尝试写入原图子目录、OCR项目内其他batch外目录均拒绝且不创建新父目录；集合deliveries兄弟目录正常 |
| 无模型/导出副作用 | build/apply/reexport不得新增OCR调用；修改响应hash或原值后必须拒绝，不能覆盖工具稿 |

模型仍用本机已有获准看图通道，不部署新服务，不把内部图片擅自外发。只读取交付包`review_tasks.json`与文档裁图；不要给模型期望答案。

```bash
python -m mp4_analysis.thin.document_cli inspect-review ACTUAL_RESPONSE.json
python -m mp4_analysis.thin.document_cli apply ACTUAL_TOOL_BUNDLE ACTUAL_RESPONSE.json -o work/deliveries/efc_fixed_reviewed_v1 --accept-changes ACTUAL_RESPONSE_SHA256
```

分批复核第二份response必须绑定第一份修订包的新`content_sha256`，不能复用旧候选hash。`review_coverage`仅保存有身份绑定的已阅声明；关键字段独立核验、源不可读和结构问题仍单独列未决。

## 8. 实际成品验收，不拿文件存在代替准确率

两组分别核对前/中/后段的正文、普通表/密集表及图像。总抽检目标至少20段正文、100个源单元格、50个技术字段；实际不足则全查并说明。不排除难读样本来提高比例，未决/无法判读分开记录。

Word：回读标点、下划线、英文空格；在本地用Word或LibreOffice导PDF/图片并检查分页、窄列、图像、边界裁断。生产检查`layout_rendered=false`不会因有图片hash而变成true。

Excel：实际打开，核对位置、空合并格、跨行/跨列跨度、标识符及以`=`开头的字面文本；不得执行截图中“公式文本”。程序只核对明确声明的结构，源表识别是否正确仍要看图。

输出两组各自的：正确/错误/缺失/未决计数及分母；正文CER=(替换+删除+插入)/人工独立转录字符数；技术字段严格完全匹配率；单元格文字和源位置正确率；图片存在/完整性；图片回退和未恢复结构数量。工具初稿与模型修订稿使用同一组源样本，冻结后评分，不在评分中补答案直到PASS。

模型用量记录真实看图次数、图像量、可观测Token、重试及耗时。订阅没有账单时明确UNMETERED_SUBSCRIPTION/金额未知，不写0元。

## 9. 最终提交内容

在`docs/screenshot_runs/<RUN_ID>/`提交：

- `TEST_REPORT.md`：首屏两组状态/耗时/抽检数字/前三类剩余问题，R1—R6分别通过、失败或阻塞。
- 完整tested_commit、环境、命令、退出码、针对性与全量回归XML、运行日志、进程外墙钟记录。
- 源图前后hash、ROI配置、批次/运行/交付清单、实际最终文件或仓库授权持久位置及取回方法/hash。
- 模型真实响应、修订记录、coverage历史与当前未决、Word渲染检查、表格源位置对照。

大文件不要只记测试机绝对临时路径；交付必须可取回。不要提交凭据、无关用户资料、整个虚拟环境或模型权重。

最后更新NEXT_CHAT_HANDOFF.md，记录实际完整head、测试范围、哪些通过/未通过、下一明确动作。保存并推送到原开发分支；不改main、PR或工作流。没有全部通过也要交事实，不退回只写计划。

## 10. 仍然保留的范围边界

本轮不修改曾被平台拦截的screenshots.py更新，不自动重试；批次目录仍长hash，Windows选择短工作根。历史视频工作流未迁移也未执行，不能用它们判断新截图命令已通过。无自动跨截图去重/拼表，无自动视觉API，无生成式去水印；源不可见内容不补写。

参考成熟读取能力：
- python-docx段落/表格读取：https://python-docx.readthedocs.io/en/stable/api/table.html
- Word合并单元格表示：https://python-docx.readthedocs.io/en/latest/dev/analysis/features/table/cell-merge.html
- openpyxl合并范围读取：https://openpyxl.readthedocs.io/en/3.1/api/openpyxl.worksheet.merge.html

这些是实现接口依据，不是本工程真实运行通过证明。
