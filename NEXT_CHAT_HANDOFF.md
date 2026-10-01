# 当前交接：截图指定区域首版，第3轮主要实现已交付

更新：2026-10-01。用户授权ChatGPT连续三轮开发，明确不要求ChatGPT测试。**本轮完成第3轮主要接线；没有运行测试、编译检查、GUI、OCR、视觉模型、Word/Excel生成或渲染。实现落库不等于运行/内容验收通过。**

仓库：abba-labs/mp4_anyisis；工作分支：feat/open-source-thin-pipeline-20260928；PR #3保持草稿。进入head为`54cfef4049470194c1d5facdf360b39166f97c14`；本轮实现及README截至`71115f7353c0700a48bf950422ad4ba75cbeb0cb`，随后是本交接提交。继续前核对远端实际head；不改main、不强推、不合并或修改PR，不覆盖并发更新。提交均带skip-ci，未修改/手动触发工作流。

## 1. 本轮已提交什么

| 范围 | 已编码实现 |
|---|---|
| 多文档入口 | batch_cli的prepare/run/status；一个JSON计划包含多组独立来源/ROI/输出；整组预览后一次确认，顺序执行并独立记录组结果 |
| 增量复用 | native_cache读取同项目旧run；原图hash、ROI、裁图hash/尺寸、模型/参数及原生解析实现一致才复用；复制前后验证所有原生输出，不改旧文件 |
| 同组恢复 | pipeline逐项状态、每次attempt快照、当前墙钟时间；损坏/失败/不匹配结果先保留到failed_attempts；成功项可复用 |
| 部分结果交付 | ScreenshotRunError携带run报告；集合入口可从部分run组织带未决和来源回退的候选；仍为PARTIAL_FAILURE，不假报完整识别 |
| 候选版本复用 | 相同内容/导出设置/实现且已封包文件哈希完整、上次导出无错误时复用候选；否则新版本，不覆盖旧产物 |
| 导出专用恢复 | document_cli reexport从冻结工具稿/修订稿产生新导出版，既不重跑OCR，也不重放模型修改，保留原始review_response/applied_changes |
| 路径与写入边界 | utils加入目录重定向检查和完整hash碰撞检查；新的run目录为r_加16位定位符，真实身份仍保存；兼容保留旧长run目录 |
| 使用说明 | README、docs/SCREENSHOT_BATCH_RUN.md与examples/screenshot_collection.json；原第2轮修订格式文档仍有效 |

原有OpenCV选框、Pillow区域裁剪、PP-StructureV3解析、Pandoc Word及PaddleX表格转换继续复用。没有另造OCR、表格求解、配准算法、截图软件、数据库、队列或模型服务。

## 2. 本轮未成功的写入和仍保留的限制

尝试更新`screenshots.py`以缩短**批次**目录并补输入检查时，被平台安全检查拦截。未重试该操作、未改通道绕过；该文件仍为原第1轮版本（blob `3ee7e547fdcee0e5b3056ce90785b062e6ec5d0f`）。被拦截的整次文件更新均未生效，不能声称其中附加检查已入库。

因此：**批次层仍使用完整64位hash；本轮已成功缩短的是运行层run目录及新增交付版本名。** Windows仍建议选择短输出根，如`D:/ocr/efc`；没有保证任意深路径都可用，不以这个非核心收缩项阻塞已提交的批量功能。不要重新创建一套路径框架，也不要把被拦截操作自动重新提交。

旧.github/workflows仍有视频参数，此前未获准修改/触发，本轮未动。它们不作为当前截图CLI的生产入口，也不能宣称CI已经迁移通过。历史报告和旧视频流程只作证据归档，不再执行。

实际61张裁剪/OCR效果、缓存恢复、平台兼容性、Word/Excel版式及内容正确率全部待本地验证；本轮没有新成品或通过数量。

## 3. 本地接手最短动作：现有两组一起运行

使用现有虚拟环境的python，不重新搭建OCR/模型服务。两组源截图仍为34张详细设计、27张LRS；不等于61页完整原文。每组先在有桌面的电脑选择文档区域；已有可用ROI则跳过选框。

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" --select-region "work/regions/efc_detail.json"
python -m mp4_analysis.thin.cli "screenshots/efc模块lrs设计文档" --select-region "work/regions/efc_lrs.json"
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
```

查看打印出的collection_preview.html及两组全部裁图，使用其真实完整approval_id：

```bash
python -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

示例JSON路径相对于examples目录；区域配置不在Git时需由采集机提供真实文件，不由ChatGPT预填坐标。输出根可改成较短绝对路径；修改计划后先重新prepare。准备失败/区域越界不退回整屏；错误组保留状态。配置语法或非法路径的整体错误会在执行前拒绝。

结果索引为输出根的index.html。每组独立d_<id>目录；交付在deliveries/d_<id>/v_<定位符>_<版本>/。source原图不拷入交付，evidence只包含批准文档裁图。

同输入/计划中断后，重复相同run命令。改图/顺序/ROI须重新prepare和确认，未变项可以跨批次复用；失败/损坏缓存不当成功。不要删除旧输出或清缓存从头跑。

## 4. Office或模型后续不需重跑OCR

仅导出失败或从HTML候选补Office：

```bash
python -m mp4_analysis.thin.document_cli reexport ACTUAL_BUNDLE_DIRECTORY -o work/deliveries/efc_export_v2
```

导出使用第2轮已有Pandoc及上游表格转换器。新目录必须不存在。失败保留候选与错误并返回2；没有OCR或视觉调用。source_accuracy、图像完整性和版式渲染仍未由文件一致性校验证实。

真实视觉复核继续用已有获准通道读取最终包review_tasks.json及裁图，只返回差异。结构和来源约束见docs/SCREENSHOT_DOCUMENT_OUTPUT.md。

```bash
python -m mp4_analysis.thin.document_cli inspect-review ACTUAL_RESPONSE.json
python -m mp4_analysis.thin.document_cli apply ACTUAL_TOOL_BUNDLE ACTUAL_RESPONSE.json -o work/deliveries/efc_reviewed_v1 --accept-changes ACTUAL_RESPONSE_SHA256
```

程序不调用外部模型或读取凭据。不将阅图任务生成或JSON合法当成内容PASS；模型/Token/费用不可观测时如实unknown，不写0。

## 5. 缓存与计时的重要口径

缓存仅同项目索引。精确匹配源图、ROI、裁图、模型和parser.py/_layout_parsing_patch.py；纯目录调度变化不要求重做原生推理。每个旧run批准记录、源manifest及文件哈希必须匹配。

原native输出按原样复制，旧JSON里的生产路径只是历史记录，不被用于读取本次模型图像。实际输入仍是新批次批准裁图；复用来源单独记cache_origin。

report.json的cache_hits含同run及跨批次命中；cross_batch_cache_hits单列跨批次；inference_attempts_this_run是进入原生解析的尝试数，不是成功内容数。每次elapsed_seconds是当前调用墙钟，缓存native.timings为历史，不得冒充新推理时间。集合分别记录OCR、导出、总历时及文档复用状态。

锁不自动删除。Ctrl+C/SIGTERM尽力保存状态，强杀/断电不保证finally；操作人确认进程已终止后再检查残留锁。原始失败目录、原图和旧Word/表格不覆盖。

## 6. 交接清单与真实状态

本轮生产改动：utils.py、pipeline.py、document_cli.py、pyproject.toml；新增native_cache.py、batch_cli.py、document_reexport.py。第2轮document_bundle/document_format/document_review保持现有能力。输入screenshots.py更新被拦截，保持原文件。

本地接下来做的是**运行验证和发现问题后的修复**，不是继续重画架构或再写一轮方案。优先连续运行两组、验证区域外排除、缓存不串页/不误命中、失败独立、实际文档完整性，再统计内容抽检与耗时。原文缺页、区域内遮挡、模型误识别和复杂表格仍可能未决，不能为了三轮开发完成就假报识别准确率。

三轮主要实现已交付；区域选择、OCR调用、整文档组织、模型修订导入、多组运行及恢复均有代码入口。**软件尚未运行验收，不能标生产可用或全部任务已通过。** 不承诺聊天之外后台执行。历史第2轮交接保留在54cfef4固定提交。
