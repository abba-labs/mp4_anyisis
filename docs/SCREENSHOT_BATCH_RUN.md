# 截图首版：多文档连续执行与恢复

更新：2026-10-01。第3轮实现说明。代码已提交，不代表已运行通过；ChatGPT没有执行测试、OCR、GUI、视觉模型或Office生成/渲染。

## 1. 本轮新增接口

- `python -m mp4_analysis.thin.batch_cli prepare PLAN.json`：逐组生成裁剪预览，不初始化Paddle。
- `python -m mp4_analysis.thin.batch_cli run PLAN.json --accept-plan SHA256`：确认整个准备快照后，逐组OCR及文档输出，失败组不隐藏、不终止其他独立组。
- `python -m mp4_analysis.thin.batch_cli status PLAN.json`：只读当前集合状态，不重新准备或识别。
- `python -m mp4_analysis.thin.document_cli reexport BUNDLE -o NEW_BUNDLE`：从冻结初稿/修订稿重试导出，原文、旧版、原OCR和模型意见均不重跑、不覆盖。

命令别名为`screenshot-batch`和`screenshot-document`。尚未更新可编辑安装时直接使用上面的`python -m`。Python指向现有虚拟环境，不要求重新安装环境或另部署模型。

## 2. 两组现有截图的最短执行顺序

仓库中已有34张详细设计和27张LRS截图；数量不等于完整原始页数。先在能显示桌面窗口的电脑分别保存ROI，没有桌面的处理机读取同一ROI文件即可。坐标不能由未查看截图的Agent猜填。

```bash
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" --select-region "work/regions/efc_detail.json"
python -m mp4_analysis.thin.cli "screenshots/efc模块lrs设计文档" --select-region "work/regions/efc_lrs.json"
python -m mp4_analysis.thin.batch_cli prepare examples/screenshot_collection.json
```

打开打印的`collection_preview.html`，进入两组链接检查全部裁图及错误项。复制本次输出的完整approval_id，然后执行：

```bash
python -m mp4_analysis.thin.batch_cli run examples/screenshot_collection.json --accept-plan ACTUAL_APPROVAL_ID
python -m mp4_analysis.thin.batch_cli status examples/screenshot_collection.json
```

ACTUAL_APPROVAL_ID必须替换为真实值。它确认的是当前输入范围与计划，不证明文字准确。已有正确ROI不需再选择；个别截图使用第1轮的`--override-image`，之后重新prepare/确认整个集合。

`examples/screenshot_collection.json`中所有相对路径以该JSON所在目录为基准，而不是命令所在工作目录。示例因此使用`../screenshots/...`和`../work/...`。配置无凭据、无模型地址、无虚构坐标。

### 配置含义

- `output_root`：集合输出根；必须与所有源截图目录隔离。建议使用短绝对路径，例如Windows的`D:/ocr/efc`，但不要覆盖现有非本程序管理的目录。
- `documents`：每份文档一个唯一小写ASCII ID、source和roi_config；已裁好的截图可以明确使用full_image=true替代roi_config。
- `ocr`：沿用现有NativeParser参数。word=false表示不逐截图生成Word，不禁止最终整份Word。
- `export`：word/xlsx为最终文档导出开关；复用已有Pandoc 3.1.11.1及PaddleX 3.7.2表格导出。
- 原始PNG、源manifest与历史缓存不改。每份文档独立目录，不跨文档混合来源或强行合并跨图表格。

## 3. 增量复用具体做什么

`native_cache.py`只索引同一个截图项目目录中先前成功的run；不是数据库或新的缓存服务。

复用同时要求：完整原图SHA256、准确ROI、裁图SHA256/尺寸、parser fingerprint、原生Word开关，以及parser.py和版本补丁的实现hash一致。原run的批准记录必须与其manifest一致。每个原生文件及adapter.json在复制前后均核查，输出中不得有额外文件或符号链接。

顺序改变、补一张截图或其他截图区域改变形成新批准批次后，未变截图可以复制已验证的原生结果，不再次推理。目标新目录中的原生内容保持原样；原生JSON里的旧生产路径仅是历史元数据，不作为本次模型输入。新的run记录自己的裁图及cache_origin。

调度代码可改变目录组织；原生推理/导出实现不同则不复用。跨组不共享缓存。图像相似、OCR文字相似、文件大小相同都不是复用条件。没有做语义去重或忽略细小字符变化。

report.json分别记录cache_hits、cross_batch_cache_hits、inference_attempts_this_run及当前调用墙钟时间。缓存项里的native.timings属于历史生产记录，不能累加成此次推理耗时。这里的inference_attempts是进入原生解析的尝试数，不是成功识别数量。

## 4. 中断、失败和重导出

### OCR中断或部分失败

重复相同run命令即可，先核对当前批准快照；同组成功项复用，失败/损坏/配置不符的目标先完整移动到failed_attempts，再允许原生适配器写新结果。attempts保留每次调用的最终报告及被后续调用替换的历史快照。

批量入口处理Ctrl+C及SIGTERM，尽可能落盘状态；SIGKILL/断电不能保证finally执行，下一次仍须核对文件哈希。存在锁时不自动删除。确认没有对应进程在运行后，才由操作人检查锁；不编写kill所有Python或强制解锁命令。

集合计划或源图/ROI变化，旧accept-plan失效；新prepare后重新确认。已有相同集合可继续运行，文档输出不会因为命令重复就被覆盖。

### 部分OCR失败也生成可检查候选

batch_cli接收ScreenshotRunError携带的run报告，再调用现有build_document：有源裁图的失败页面采用可见来源回退，错误项进未决清单。该候选不是成功的可编辑恢复；集合状态仍为PARTIAL_FAILURE。输入/权限级失败无法生成候选时，记录原因并继续后续组。

### Word/Excel失败

HTML/content.json及错误报告保留。修好本机转换器环境后，在新版本目录重导出：

```bash
python -m mp4_analysis.thin.document_cli reexport ACTUAL_BUNDLE_DIRECTORY -o work/deliveries/efc_export_v2
```

不重新运行OCR，不再次消耗模型调用。不能把NEW_BUNDLE设为已有目录。部分导出仍失败返回退出码2；成功导出仍是REVIEW_REQUIRED，不自动PASS。

集合重新运行也会检查上次文档包；相同输入/原生文件/导出设置/输出实现及完整文件哈希匹配，并且上次导出无错误，才复用旧候选。失败或不匹配时生成带唯一后缀的新版本。单独reexport用于只重试导出的最短路径。

## 5. 输出在哪里

```text
work/screenshot_collection/
  collection_preparation.json
  collection_preview.html
  collection_status.json
  index.html
  attempts/
  d_efc_detail/
    latest_result.json
    batches/<完整旧批次hash>/
      frames/                     # 只有文档裁图
      runs/r_<16位短定位符>/       # 完整execution hash仍存.identity.json
        crop_approval.json
        report.json
        attempts/
        native/
        failed_attempts/
  d_efc_lrs/
  deliveries/
    d_efc_detail/
      delivery_<定位符>.json
      v_<定位符>_<版本后缀>/
        content.json
        document.html
        document.md
        document.docx             # 按导出结果
        tables/                   # 按导出结果
        images/
        evidence/                 # 仅批准裁图
        review_tasks.json
        bundle.json
        export_report.json
```

短路径只缩短运行目录和交付版本定位符，完整身份必须核查，遇前缀碰撞报错。第1/2轮已经存在的长运行目录兼容保留，不强制迁移。

**限制：本轮尝试缩短screenshots.py中的批次目录时，GitHub写入被平台安全检查拦截。该操作未再次提交，也未换通道绕过；screenshots.py维持原版本，批次层仍使用完整64位hash。因此Windows仍应选短输出根，未声称任意深路径均可运行。** 新的运行目录缩短与集合接线是其他已获准提交的独立变更。

## 6. 模型复核仍接第2轮接口

打开最终包的review_tasks.json，用已有获准看图能力连续核对文档裁图。外部返回格式及6种受限操作见SCREENSHOT_DOCUMENT_OUTPUT.md。程序不创建视觉服务，不将内部资料交给新供应商。

```bash
python -m mp4_analysis.thin.document_cli inspect-review ACTUAL_RESPONSE.json
python -m mp4_analysis.thin.document_cli apply ACTUAL_TOOL_BUNDLE ACTUAL_RESPONSE.json -o work/deliveries/efc_reviewed_v1 --accept-changes ACTUAL_RESPONSE_SHA256
```

人工/Agent确认整份响应后应用，旧native/初稿不改。关键字段及版式仍需源内容验收。费用不可观测明确unknown/UNMETERED_SUBSCRIPTION，不写0。

## 7. 留给本地的验证和迁移边界

本轮没有运行测试、真实截图批次、模型或Office。不是“61张全部通过”。本地连续完成区域检查、两组批量运行、修改单页后增量复用检查、导出失败后恢复、实际Word/Excel及内容抽检，不需要逐项回来请求下一步。

重点验证新旧输入身份、批准失效、失败独立记录、缓存内容不串页、重导出不改原稿、最终输出不含区域外像素。实际速度、识别准确率、模型费用必须实测，本次没有预估成真实数值。

旧.github/workflows仍有视频参数；未获准修改/触发，本轮未动，不能称CI已全部迁移。旧视频报告仅作历史，入口为README、本说明和根交接。不恢复视频模块来迁就旧工作流。
