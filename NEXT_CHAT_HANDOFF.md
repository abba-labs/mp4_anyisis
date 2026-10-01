# 当前交接：截图首版已完成源码复核，仍需适配修复

更新：2026-10-01。用户要求“好好复核一遍，是不是真的搞定了”。

**当前结论：主体代码已经接线，但不能宣布已经可靠完成；源码复核为REQUIRES_FIXES，运行验收仍为NOT_RUN。** 本次不是新一轮OCR、模型或Office测试，也没有修改生产代码。

完整复核：[SCREENSHOT_7E68E89_REVIEW_20261001.md](docs/reviews/SCREENSHOT_7E68E89_REVIEW_20261001.md)。报告提交：`83b398fe5a13ef9d474ee3f2d83d81ede311320a`。
审查代码固定为`7e68e89076640f27354f2aa6ad8c1edc24ecf0b7`，不是依靠PR旧正文判断。该提交的[第3轮完整交接](https://github.com/abba-labs/mp4_anyisis/blob/7e68e89076640f27354f2aa6ad8c1edc24ecf0b7/NEXT_CHAT_HANDOFF.md)完整保留此前入口、限制和历史。

仓库：`abba-labs/mp4_anyisis`；工作分支：`feat/open-source-thin-pipeline-20260928`；PR #3保持草稿。main不改，不强推，不合并或改PR元数据。继续前查询远端实际head，修改文件使用实时blob SHA，保护并发更新。报告/本交接提交带skip ci；没有修改或触发工作流。

## 1. 哪些能力确实有代码，哪些没有经过验证

已编码：显式选区域、批量裁剪预览、裁图批准、PP-StructureV3调用、内容hash/ROI缓存、整份文档候选、外部视觉差异导入、独立修订/重导出、多组入口及恢复。

正常调用链的OCR与模型证据只引用裁图，原整屏不拷入文档交付。OpenCV选框、Pillow裁剪、已有PP-StructureV3、Pandoc与PaddleX表格转换继续复用，不需要第二套引擎或自研算法。

但61张实际区域、真实OCR、Word/Excel内容与版式、增量命中及平台兼容性没有在ChatGPT侧执行验收；不可用“主体代码有了”换成“所有功能已通过”。本次是源码路径复核，报告中的反例是静态推论，不冒称已运行的测试。

## 2. 本次复核发现的6类问题

| ID | 问题 | 主要位置 | 当前状态 |
|---|---|---|---|
| R1 | 表格允许sup/sub等内联标记，但转为纯文本时丢语义；条件满足时会出现例如10的三次方变成普通103 | document_format.table_model/_cell_text/table_html | 未修复 |
| R2 | 成品一致性检查删除所有空白、未核对Word图片资源；Excel主要核对转换后的存盘一致性，不足以证明候选结构保留 | document_format.check_docx/export_bundle | 未修复 |
| R3 | 一组源目录缺失在load_plan阶段中止整个集合，其他可用组无法进入分组失败处理 | batch_cli.load_plan | 未修复 |
| R4 | 分批复核覆盖ID被本次列表替换，旧pending不退出、已复核页可能再次被标pending | document_review.apply_review | 未修复 |
| R5 | 独立build只保护当前batch，未完整继承主CLI对原截图及整个OCR工作树的隔离规则 | document_bundle.build_document | 未修复 |
| R6 | 单组elapsed在prepare之后开始，多组总elapsed也漏最初prepare，不能叫完整命令墙钟 | pipeline.run/batch_cli.execute | 未修复 |

R1是特定受支持标记出现时的数据保留缺陷，不表示已在当前截图观察到该错误。R2是校验盲区，不表示本轮观察到某份实际Word丢图。其余具体触发条件、影响、修复方向在完整报告中。

## 3. 接续工作：集中修正适配层，不再扩大方案

源码修复仍由ChatGPT承担；本地负责实际执行验证。不是把这6类已经定位的问题转回本地让其重新研究，也不是再设计一套框架。

优先完成R1/R2，避免内容被转换改变或漏检；并行收尾R3/R4失败隔离与复核状态、R5公共目录约束、R6阶段计时。保留成熟库，不自写OCR、表格网格求解、公式推理或复杂工作流平台。源码补丁完成后再交本地完整验证两组截图，不恢复逐字逐格来回交接。

原有限制继续成立：不自动推断原始分页、跨图去重/拼表；模型复核是任务文件与差异导入，不是无人值守视觉服务；内容PASS不能由模型自报或文件格式检查产生。

## 4. 现有操作入口仍可查阅，但不能视为已验收

- [README](README.md)：单组区域、OCR与文档命令。
- [SCREENSHOT_BATCH_RUN](docs/SCREENSHOT_BATCH_RUN.md)：多组prepare/run/status及恢复。
- [SCREENSHOT_DOCUMENT_OUTPUT](docs/SCREENSHOT_DOCUMENT_OUTPUT.md)：模型差异、apply/reexport格式。
- [示例集合](examples/screenshot_collection.json)：当前两组截图的计划；不能预填未知ROI。

源集合仍为` screenshots/efc详细设计文档/ `34张和` screenshots/efc模块lrs设计文档/ `27张，共61张截图，不等于61页完整原文。复用现有虚拟环境、模型和成功缓存；不重新安装第二套OCR。

典型入口（留给本地实际运行）：

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" --select-region "work/regions/efc_detail.json"
python -m mp4_analysis.thin.cli "screenshots/efc模块lrs设计文档" --select-region "work/regions/efc_lrs.json"
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
# 查看实际全组预览；以下值由本批生成，不能虚构或复用过期值。
python -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

导出和模型修订的独立入口仍为`python -m mp4_analysis.thin.document_cli build/inspect-review/apply/reexport`，具体参数按使用说明。R1—R6未修正前，不能把运行返回或CONSISTENT等局部检查标志当整份资料可靠完成。

## 5. 持续保护与未授权范围

原图、原native、旧候选、失败日志不覆盖。ROI缺失/越界不回退整屏。用户内部材料不擅自发送新服务，不读取或打印凭据。锁不自动删除；强杀残留锁由操作人确认进程后处理。

`screenshots.py`第3轮更新曾被安全检查拦截；该文件仍为原第1轮版本，本次只读，未重试或绕过。64位batch目录与旧视频工作流是已记录的剩余限制，不借此次审阅自动重做被阻止的操作或修改工作流。Windows继续选短输出根，不能保证任意深路径。

本次没有新增OCR结果、测试通过数、速度、费用或正确率。只新增了来源固定的审阅报告及本页状态更正；生产实现仍是7e68e89对应的版本。
