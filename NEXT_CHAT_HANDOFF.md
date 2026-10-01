# 当前交接：R1—R6补丁已提交，按交付文档进行本地验证

更新：2026-10-01。用户要求先修复源码复核发现的问题，再把指导本地测试的交付文档放进仓库。

**当前状态：PATCHED_AWAITING_LOCAL_TEST。六类问题均已提交针对性代码修改和回归用例；ChatGPT没有运行测试、OCR、视觉模型、Word/Excel生成或渲染，也没有取得编译检查通过证据。不将代码落库称为运行通过。**

## 1. 唯一最新测试入口

完整交付文档：**[SCREENSHOT_FIX_DELIVERY_20261001.md](docs/SCREENSHOT_FIX_DELIVERY_20261001.md)**。
交付文档提交：`9dc0ae4db261d0a366f8eedacf8f0dcd79f2fb0b`。
生产补丁截至：`5e500b4b6263b4b77295805c14ec432c37a55b9c`。
针对性用例：`tests/test_screenshot_review_fixes.py`，提交`935f7cab4340a22f6518df09be2accfd5b25fd7d`；已写、未执行。

本次进入head为`8428f253de9e9ef72f6b84e2c1010b3d32239fba`；旧审阅报告保留在[SCREENSHOT_7E68E89_REVIEW_20261001.md](docs/reviews/SCREENSHOT_7E68E89_REVIEW_20261001.md)，其“未修复”是当时快照，不再作为当前补丁状态。

仓库`abba-labs/mp4_anyisis`，工作分支`feat/open-source-thin-pipeline-20260928`，PR #3保持草稿。开始和推送前重新查询实际head，保护并发修改。main未改，不强推、不合并或改PR元数据；本次没有修改或触发工作流，提交带skip ci。

## 2. 六类补丁的真实内容

| ID | 已修改代码 | 本地验证重点 |
|---|---|---|
| R1 | document_format拒绝不能保真转换的sup/sub/s等语义标记；document_bundle保留区域图片并记录unsupported_table | 不再把10的三次方静默转成103；图片回退不计为可编辑表格恢复 |
| R2 | 新document_checks按有序文字块、字间空格、图片关系/像素身份、候选声明span与实际XLSX核对；document_format接入转换前后检查 | 缺空格、段落粘连、缺图/换图、空合并格/跨度/位置变化应报警；不把声明结构当源结构准确 |
| R3 | batch_cli不因普通输入目录缺失在load_plan阶段整体退出；资源失败留给逐组准备 | 缺失组失败，可用组继续；非法计划和危险路径仍全局拒绝 |
| R4 | document_review按证据图与单元内容hash累计coverage；唯一当前pending、独立历史；修改影响已有覆盖时失效 | e1后e2覆盖累计，补查后pending退出；critical未决不自动关闭 |
| R5 | 公共build核对原截图与整个单文档OCR项目隔离，校验项目owner；新候选记录source_protection，apply/reexport继承 | 不向原图树/受管理OCR树写派生成品；集合deliveries兄弟目录保持可用 |
| R6 | pipeline与集合execute在准备前计时，记录不重叠阶段；CLI补当前命令时间字段 | 准备开销计入；嵌套明细不重复累计；缓存native.timings仍为历史；进程启动另用外层墙钟 |

这次没有更换PaddleOCR/PaddleX、没有新模型服务、没有自研OCR或图像表格求解器。新校验只解释候选已有的显式span，不从图像推断或修补网格。

注意：已被旧版压平的content.json不能通过reexport自动找回上标等语义。应使用保存的原生JSON重新build新候选，不需要重跑OCR。新交付身份包含document_checks.py，旧校验结果不会冒充新导出验证。旧包缺失来源保护字段时，先用新build重建后再修订。

## 3. 本地一次连续完成的工作

完整命令、依赖、R1—R6通过条件、恢复/失败注入方法和最终报告要求都在交付文档中。复用现有Python 3.10—3.12虚拟环境及模型缓存，不重建环境。

```bash
python -m pytest -q tests/test_screenshot_review_fixes.py
python -m pytest -q
```

先记录针对性与全量回归的真实结果，不用历史通过数代替。随后为现有34张详细设计、27张LRS确认真实ROI；已有配置直接复用：

```bash
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
# 检查两组全部裁图，使用本次真实完整approval_id。
python -u -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

只处理指定文档区域，不用full-image绕过未知整屏边界。截图数不等于原文页数；批量输出、缓存恢复、模型修订、Word/Excel实物一致性和内容抽检分开报告。不得凭文件存在、模型自评或导出返回码给内容PASS。

本地按交付文档连续验证后，把报告、运行日志、实际文件及来源、用量/计时和失败明细提交到`docs/screenshot_runs/<新RUN_ID>/`，并更新本交接。遇普通代码缺陷直接保留复现与修复证据，不重新规划架构，也不重新排查旧视频样本。

## 4. 仍有的范围限制

- 所有代码补丁和新用例均未由ChatGPT运行；真实效果待本地验证。本次无新的准确率、速度、费用或内容通过数。
- 不自动跨截图去重、推断原始分页、跨图拼表或生成式去水印。上游格式不支持时有显式区域图片回退，而非承诺全部表格可编辑。
- 模型仍是本地已有获准看图能力读取任务并返回差异，不是自动部署或调用新视觉服务。coverage是有身份的已阅声明，不等于独立内容验收。
- `screenshots.py`曾被拦截的更新本轮没有重试，该文件仍保持原版本；批次64位hash路径未缩短，Windows选择短输出根。
- 历史视频工作流未迁移、未修改或运行；不能据旧CI配置宣传截图版已测试通过。
- 原图、原native、旧候选、失败记录不覆盖；不读取或提交凭据；不自动清锁或强推。

第1—3轮功能入口仍可参考README、docs/SCREENSHOT_BATCH_RUN.md和docs/SCREENSHOT_DOCUMENT_OUTPUT.md；与本次修复的计时/覆盖/校验说明不一致时，以本文和新交付文档为准。
