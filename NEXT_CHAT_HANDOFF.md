# 当前交接：截图指定区域开发，第1轮已提交代码

更新：2026-10-01。用户最新要求：**由ChatGPT直接开发，收敛为三轮；测试、真实OCR和成品验收留给本地，本轮不执行。** 这覆盖之前把小开发全部交给本地的分工。三轮针对软件实现范围，不用未测试的代码承诺识别准确率。

仓库 `abba-labs/mp4_anyisis`；工作分支 `feat/open-source-thin-pipeline-20260928`；PR #3保持草稿。进入head `87ab3df584d0bb9f3404e0cc5fea5f69972ca126`。本轮实现与使用说明截至 `26306d5d9951e90681a9941a81b53a60f5862e21`，随后为本交接提交；继续前重新查实际head，不覆盖并发更新。不改main、不强推、不合并或修改PR元数据。

**本轮没有运行测试、OCR推理、GUI选框或Word/Excel渲染验收。** 提交信息带skip-ci，本轮不以自动测试数量作为成绩。曾尝试只下载源文件做静态语法检查，下载连接失败，未得到语法检查通过结果；不据此停止已完成的Git代码交付。

## 1. 现在已经实现的功能

| 范围 | 真实代码状态 |
|---|---|
| 区域选择 | `screenshots.select_region` 调用已安装OpenCV selectROI，保存整组默认区域；支持单图覆盖、原图尺寸与预览坐标映射 |
| 批量裁剪 | Pillow读取静态PNG，检查尺寸/区域，生成仅文档区域的独立PNG；原截图不改、不拷入结果目录 |
| 显式输入边界 | 缺少ROI、取消、越界不回退到整屏；已经只包含文档的输入必须显式full-image；OCR需确认具体裁图批次 |
| 源清单与排序 | 存在manifest时按index并核对文件集合/数量/声明尺寸；没有时自然排序并标未验证页序；拒绝混合父目录、隐藏/非PNG与非本地文件引用 |
| 输入身份 | 根据原始内容hash、顺序、ROI和裁图hash建立批次，不再按文件大小判断是否换图；改区域/源图后旧approval_id失效 |
| 全组预览 | 准备阶段生成所有裁图及错误项的preview.html，不初始化Paddle；确认后才允许OCR |
| OCR接线 | 只将经hash核对的裁图传给现有NativeParser；记录逐图状态、耗时、缓存和失败；保留未处理项；模型不可用不重复尝试全部图片 |
| 结果与复核任务 | 截图版index/report及review_tasks.json只引用裁图；没有自动视觉调用，不把任务文件生成叫模型复核完成 |
| 迁移收尾（部分） | 删除PyAV直接依赖；增加screenshot-analysis命令别名，保留旧包名；README改成截图使用说明；清除test_reconstruction里已删除视频功能的导入/断言，保留两项仍适用的解析与输出断言，未执行 |

这是“已实现、未验证”，不是61张已经处理完。当前 `--word` 仍然只导出每张截图的上游原生Word，不能称为整文档输出。原生解析、既有Pandoc转换器和历史缺陷证据未被重写。

## 2. 本轮改动位置与接口

- `src/mp4_analysis/thin/screenshots.py`：新输入适配。`discover_screenshots`、`prepare_screenshots`、`select_region`、`region_box`。
- `src/mp4_analysis/thin/utils.py`：内容hash、原子JSON写入、目录隔离和单写者锁。旧load_screenshots入口要求显式ROI并转发到新批次准备，不再复制整屏。
- `src/mp4_analysis/thin/pipeline.py`：先准备/确认裁图，再懒加载解析器；按模型参数与实现hash隔离结果目录，逐项持久化状态。
- `src/mp4_analysis/thin/cli.py`：`--select-region`、`--reference-image`、`--override-image`、`--roi-config`、`--full-image`、`--prepare-only`、`--accept-crops`；保留设备、线程、模型、表格参数。
- `pyproject.toml`、`README.md`、`tests/test_reconstruction.py`：依赖、入口说明与失效视频引用收尾；未修改现有工作流。

逻辑仍为截图输入、原生解析、结果输出三个层次。没有新OCR、配准、表格求解器、截图GUI平台、数据库、Agent调度器或服务端。新增模块只是调用Pillow/OpenCV的输入适配，不是重建框架。

### ROI与批次契约

ROI JSON：schema=1，coordinate_system=`source_pixels_ltrb_exclusive`；default为`image_size:[width,height]`和`box:[left,top,right,bottom]`，右下不包含；overrides以准确PNG文件名为键。whole-image必须显式`full_image:true`，不可用缺省或越界触发。

`prepare_screenshots(source, output, roi_config=..., full_image=False)`返回manifest加batch_directory。manifest包含每张源hash、ROI、裁图hash、准备状态和approval_id。approval_id基于实际裁图清单与错误项；它是调用者确认输入范围的标记，不是内容验收证明。

`run(..., prepare_only=True)`只准备。`run(..., accept_crops=<exact approval_id>)`才解析。不接受旧视频参数。复核任务的image相对本次run目录为`../../frames/<crop>.png`，允许读取根必须限定在对应批次frames，不得回到源整屏目录。源截图只作为外部不可变来源归档。

输出按 `output/batches/<batch_id>/runs/<execution_id>/` 隔离，完整源hash和ROI绑定在manifest中。Windows优先使用较短输出根，后续收尾可缩短目录ID并保留完整身份校验，避免传统路径长度限制。

## 3. 已经存在的启动命令（留给本地执行，本轮未运行）

复用已有虚拟环境，以下python替换为该环境解释器；不用重装OCR、不新建视觉服务。

```bash
# 有桌面的机器：为一组截图选框，同时准备整组裁图预览。
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o "work/efc_detail" --select-region "work/regions/efc_detail.json"

# 已有区域配置或无桌面处理机：只准备，不运行OCR。
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o "work/efc_detail" --roi-config "work/regions/efc_detail.json" --prepare-only

# 查看打印出的preview.html后，用其实际完整approval_id替换APPROVAL_ID。
python -m mp4_analysis.thin.cli "screenshots/efc详细设计文档" -o "work/efc_detail" --roi-config "work/regions/efc_detail.json" --accept-crops APPROVAL_ID
```

单图例外使用`--select-region 已有配置 --override-image 实际文件名.png`，之后重新预览并取得新approval_id。另一组`efc模块lrs设计文档`独立配置、独立输出。未取得实际截图边界，不预填猜测坐标。

`latest.json`定位当前批次，`latest_result.json`定位当前OCR运行，report逐项保留PARSED_UNVERIFIED/INPUT_ERROR/FAILED/BLOCKED/INTERRUPTED/PENDING。任意未解决项不会自动变成PASS。同一成功运行可以复用缓存；变更源图或ROI生成新批次。目前尚未跨不同批次复用未变页面的OCR，这项留给后续增量优化，不把整个新批次的缓存命中夸大为逐页增量已完成。

## 4. 后两轮固定实现范围，不重新规划或做局部实验

### 第2轮：整文档输出＋可重放视觉修订

基于本轮实际run/report/review_tasks接口继续，先读当前源码而不是历史视频流程。

1. 复用既有Pandoc及原生HTML/XLSX，按清单顺序组成一份文档候选、表格集和图片集；最终阶段统一导出。不能靠任意剪切拼接OOXML、自研表格合并求解器或改标点“顺便修正”。
2. 给任务添加稳定block/cell/evidence ID与裁图边界；本地Agent继续通过获准看图能力填结构化差异。建立文件导入→前置值/hash/来源/操作范围校验→独立reviewed稿→重导出，不部署新服务，不发未经授权外部API。
3. 保留原生内容与全部修改记录，正文/表格有未决则显式标出。模型复核和程序格式检查不能单独产生内容PASS。导出后回读实际文件的一致性检查作为生产代码实现，但不在ChatGPT侧运行测试或渲染。

### 第3轮：首版接线收尾与本地交付

完成批量使用入口、错误恢复、输入变化的增量复用、短路径/来源边界和文档收尾；将已实现功能接成明确命令。整组区域预览及本地验证仍交给本地，不能宣称已运行61张。只修工程共性问题，不回到逐个标点或旧视频候选排查。

本轮首次只确认第1轮代码落库，不把剩余两轮内容写成已经实现。测试不占ChatGPT开发轮次，也不以未执行测试的数量提高完成度。

## 5. 持续边界与未完成事项

- 实际截图输入仍为34张详细设计、27张LRS，共61张；张数不是文档页数/覆盖率。输入集合、原始截图和历史原生结果本轮未改。
- OpenCV GUI实际可用性、全部61张裁图/模型效果、排序覆盖、Word/Excel成品正确性都尚待本地验证。未知值、来源不可读和未决项保留，不按已有答案补写。
- 现有工作流仍可能引用旧MP4及旧参数；本轮未修改/手动触发工作流，之前的工作流授权边界仍有效。源码/依赖已更新不能冒称所有历史CI已迁移通过。
- 原生Word按图输出仍有上游局限；当前新版pipeline没有再使用旧录屏index作为生产入口，但旧output.py工具函数为历史调用/后续Pandoc复用而保留，不删除有用导出能力。
- 没有部署视觉模型、没有新模型调用、没有推理用量或速度/准确率实测。review_tasks.json只是模型输入任务接口。
- 不改main、不强推、不合并PR、不自动清除锁或覆盖别人的输出目录。所有更新使用当前文件SHA，出现冲突先读新内容再整合。

历史规划及旧工作量预算保留在87ab3df固定提交；旧视频TASKS/REFACTOR_PLAN和历史报告不再指挥本轮执行。下一条开发任务直接是第2轮，不再索要用户重述需求或把实施任务重新交回本地。
