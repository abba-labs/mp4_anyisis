# 新对话交接：mp4_anyisis

> 更新：2026-09-29，第十轮。原57个输入已完成；group_000078_a页头结构的隔离修复已实测，内容验收仍FAIL。不要重跑旧31/26恢复任务，也不要重复已经完成的g78实验。
> 本轮进入head：a239d8fdeb83da471d09add57a6a993c43542745。四项真实推理提交dd77665345b30c11899d42567de560291fc77cf7；最终脚本及回归提交41e21dcd80a12224b6f2b9e0332061694d93bd21。接续先查询PR #3实时head，不修改main或自动合并。

## 0. 当前摘要

| 项目 | 事实 |
|---|---|
| 分支 | feat/open-source-thin-pipeline-20260928；PR #3仍为草稿 |
| 原计划 | 110个一秒抽样画面、17候选+40原帧=57输入；57完成、pending0，不证明全部内容覆盖 |
| 原生缓存 | 344个native文件前后哈希一致；原Word/Excel/JSON和原输入未改 |
| 本轮实测 | 4个新原生解析成功；3份派生Word、1个默认源图对照因丢字被明确拒绝 |
| g78改善 | group_000078_a采用既有cells参数，页头恢复3×4网格、6物理格、4组合并，Word不再因异常第7格丢字而拒绝 |
| 边界 | OCR文字未纠正；位域表窄列、错误字符和条款覆盖仍FAIL；不是整页内容通过 |
| 第二样本 | group_000018_b仍错误：源3×4，cells输出5×4，检测层已过分割；因此没有全局改默认参数 |
| 回归样本 | frame452原正确表格拓扑保持，原识别污染也仍在 |
| 独立源图对照 | frame2373默认模式复现6检测框/7HTML格和Word拒绝；支持g78故障在结构生成而非接缝 |
| 成品检查 | 本轮实际渲染查看g78两页、g18一页；未新增Excel视觉验收，未验收全片Office |
| 最终回归 | 固定Python3.11/OpenCV4.10/Pandoc3.1.11.1：119通过、0失败/错误/跳过；不是119项内容准确率 |
| 下一唯一动作 | 复用现成g18对照及源675/705/735/765，定位单元格检测为何把6个源格分成10个框 |

详细记录：[step10_saved_table_repair](docs/step10_saved_table_repair_2026-09-29.md)，[机器证据](docs/step10_saved_table_evidence.json)。当前生产三个模块、单一PP-StructureV3后端和默认表格模式均未改变；新增是隔离实验与显式选择已有job的脚本能力。

## 1. 阅读顺序和历史入口

先查实时PR head，然后读本页、上述step10文档与JSON、scripts/probe_saved_table_cells.py、tests/test_saved_table_probe.py、tests/test_saved_table_probe_cli.py。研究检测问题再读现成reconstruction.json、原生table_res_list、固定PaddleX v3.7.2源码。

原有输出适配位于src/mp4_analysis/thin/output.py，执行入口scripts/export_saved_word.py；表格对照脚本scripts/check_saved_word_export.py。不更改历史验收锚点。

历史完整约束和失败记录继续有效：
- [第九轮交接固定版本](https://github.com/abba-labs/mp4_anyisis/blob/a239d8fdeb83da471d09add57a6a993c43542745/NEXT_CHAT_HANDOFF.md)
- [第八轮交接固定版本](https://github.com/abba-labs/mp4_anyisis/blob/7581f4e3ff1b513f4843c19d6bd882589023a7df/NEXT_CHAT_HANDOFF.md)
- [前七轮详细交接](https://github.com/abba-labs/mp4_anyisis/blob/76e5fd9de4d7065e35cc31359959859046bf5404/NEXT_CHAT_HANDOFF.md)

旧TASKS.md、REFACTOR_PLAN.md不是当前执行计划。不要重新设计框架或重复已否定的MemoryMap候选排查。

## 2. 当前证据如何取得

### 完整57项缓存：继续保留

run36439891744 / artifact10978920126；103046931字节；SHA256：
`6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86`。
到期2026-10-28T15:06:46Z；完整输出根为restored/sarc。原五份MP4在仓库MP4目录，不再向用户索取。SARC源视频SHA256为e4f131ad8a2393ca5b6eade841bbce55a2e3ea105c1023954a746a8524d7e09a。

### 本轮4项隔离对照：优先直接读，不重复推理

run36496321097 / artifact11003745957；3396758字节；SHA256：
`4b15309ca4a4ece0f0635e060db59559e544fe14862e17b5220ddae2c5de6780`。
到期2026-10-28T23:09:47Z。包含results/summary.json、results/native/<job>_<mode>/、results/word/<job>_<mode>/document.docx、输入及基线副本、上游固定源码、日志、环境及tested_source.tar。该小包不能替代完整57项缓存。

g78已改善候选为results/word/group_000078_a_cells/document.docx；g18为results/native/group_000018_b_cells/及对应Word。源2373默认Word拒绝记录必须保留，不忽略错误。此前56份派生Word与本轮新候选尚未组成一份整合文档或新的全片验收包。

### 最终119项回归

run36497200941 / artifact11003781872；4232字节；SHA256：
`8965e404c032ca0b3e0f8e5877fb71675303e820f809531d268e34e85ab48a2c`。
到期2026-10-28T23:17:54Z。已下载JUnit核实119通过/0跳过。本地Python3.13结果118通过/1跳过，缺PyAV，不冒充正式环境。

## 3. 固定环境和显式单项执行

完整基线：Python3.11.16、PaddleOCR3.7.0、PaddleX3.7.2、PaddlePaddle3.2.2、python-docx1.2.0、OpenCV4.10.0.84、PyAV16.0.1。Pandoc3.1.11.1只用于可选Word重导出，不是第二个文档解析后端。

原解析fingerprint：`878d1346af4cf2e518548be01c300f05ee15c8d4e5e5bee0223697d61cebd4bb`。
本次cells指纹：`49720955c71328580909712120f6c9a2c5cac8609cc88a2b1e473ff2d9c7af47`。
原视频参数仍sample_seconds=1、start=0、无end/max_frames/ROI、reconstruct=True、mobile、default、CPU2线程、MKLDNN、word=True。

有明确新假设且确需单项推理时，使用：

```bash
python scripts/probe_saved_table_cells.py work/full/restored/sarc \
  -o work/new_isolated_result --job group_000078_a --mode cells
```

这里是执行语法示例，不要求下轮重跑g78。--job只接受现有计划ID；可重复选择多个，不改变原计划、抽样或缓存。输出必须新目录；不匹配指纹/哈希则先失败；显式job的Word失败返回非零码，中断正确记录pending。默认不带--job是本次四输入实验，不要无理由重新跑。

## 4. 已定位的边界与下一动作

源g78页头bbox[117,19,1163,130]只有源2373支持，其他源映射从y=220以后开始，无跨源接缝。检测6框而HTML7格；源2373独立默认解析复现错误。cells使用上游已有几何转HTML，修正了此输入的结构；不手改保密等级或字数。

g18源页头约[117,396,1166,529]应为3×4/6物理格，检测已给10框、原HTML11格；cells仍为5×4并错误分割保密等级。先对源675/705/735/765与候选映射定位输入/检测层原因，不能因g78改善就全局切cells。

后续依次推进源章节/条款覆盖、录屏污染、其余接缝、源位置去重与首次运行成本。密集MemoryMap、其余视频、全部Office、Windows/离线部署仍未验收。源2890编号O1/漏02但邻帧2920有02，g12标题漏字及源图鼠标遮挡等历史内容失败没有被本轮解决。

## 5. 执行纪律

三个逻辑模块、一条本地顺序流水线、一个默认后端；只复用成熟开源能力做薄适配，不自造OCR/配准/表格求解器/复杂平台。先定位失败层，再查固定版本官方源码，固定输入单变量对照；保留原生结果，第二样本失败就不升级为默认能力。

不改源单元格、文字、验收锚点或指纹骗缓存，不降低标准；不把文件存在、列数正确、与原生Excel一致或测试通过当作源资料正确。不启动旧31/26恢复任务，不清空缓存，不强推/改main/自动合并。提交前重新检查head，分析与测试同分支，更新本页。普通回复简短，详细记录进仓库，每轮20分钟内总结实际已完成/失败/未完成，不承诺后台交付。
