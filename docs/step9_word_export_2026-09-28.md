# 第九轮：复用57份缓存，修复Word表格导出边界

进入本轮 head：7581f4e3ff1b513f4843c19d6bd882589023a7df。实现/测试/固定转换器CI完成于136bbafbdb95b12eca2b83afc921015f714347da。没有改main、没有合并PR、没有修改解析后端、模型、抽帧或拼接配置。

## 1. 当前进展，不是产品验收

原始57个解析输入仍全部完成。新增的是独立、显式的输出层重导出，不是重新推理，也不替换native内的Word/Excel/JSON。

| 检查 | 实际结果 |
|---|---|
| 完成工件 | 10978920126；完整ZIP SHA256仍为6a215eeb43435bd13619005fb8db87bcdc2cf4cd162315b6bd37cb88282f6f86 |
| 原生文件 | 将344个native文件与原ZIP逐字节比较，0变化 |
| 新Word重导出 | 57尝试，56成功，1明确拒绝；没有待处理 |
| 拒绝项 | group_000078_a：原生HTML异常行/合并结构经转换会丢掉非空单元格文字，因此拒绝发布派生Word |
| 成功输出中的表格 | 27张，逐格位置、合并范围、非空与空单元格、文字与对应原生XLSX一致（仅忽略空白）；同组旧Word只有13张一致 |
| 代码回归 | 固定Python3.11、OpenCV4.10、Pandoc3.1.11.1环境111 passed，0 failed，0 skipped |
| 内容验收 | 仍FAIL。与原生XLSX一致只证明导出一致性，原生表格本身也可能错；不是27张表对原视频全部正确 |

## 2. 锁定固定版本根因

读取PaddleX v3.7.2官方源码：
https://github.com/PaddlePaddle/PaddleX/blob/v3.7.2/paddlex/inference/common/result/converter/word_converter.py
Git blob：54dfb94af659f1b1256ff074ff4d6975ba305e86。

_parse_html_table只保留每个td/th的文字和图片片段，丢弃rowspan/colspan；_write_block按每行物理td数量取max_cols，再从第0列依次填入Word，未建立原HTML合并关系。这与frame_00000452中的SARC从B2错到A2、全部合并消失直接对应。没有换OCR模型。

原生HTML同源对照采用已安装的成熟Pandoc3.1.11.1：
https://github.com/jgm/pandoc/releases/tag/3.1.11.1

仅使用其Markdown→HTML→DOCX转换，python-docx只设置参考文档表格网格样式。不自写表格求解器、配准、文字纠错或排版引擎；Pandoc作为可选外部程序，不增加第二个文档解析后端。

## 3. 最小对照与扩大检查

### 3.1 已有明确改善

frame_00000452的源表框[118,118,1166,227]，3行4列。新Word保留A1:A2、C1:C2、D1:D2、A3:D3，B2为原生识别值“SARC 20:1”，不再放到A2。这里20:1仍是识别污染，没有删除它来制造内容通过；标志仍是错误的文本而不是源图形。

group_000018_b中同时存在横向、纵向合并；新Word保留与原生HTML/XLSX相同的5列结构。原生识别已经把保密等级放进过窄的第一列，新Word也保留了该缺陷，渲染可见多行挤压，因此不能说这个页面成品已验收。

group_000012_b的Word内嵌JPG与原生JPG逐字节相同，渲染没有新增裁断。frame_00002890复位原句仍在；原有编号O1、缺02、录屏水印/时间污染仍在。

查看了上述4份最终派生Word的4页渲染。其余52份未做逐页视觉验收，Excel本轮未新增视觉验收；没有把批量生成当作全片验收。

### 3.2 两个扩大实验发现的失败，均有回归

第一次Markdown→HTML默认启用markdown_in_html_blocks，将frame_00000181表格中的“+ I”当列表，导致整个表不再成为Word表格；frame_00000211也受影响。只关闭该上游扩展，原输入不变，两张表恢复。新增最小“+ I”单元格回归。

group_000078_a页头HTML的第二行多出一个带保密等级文字的单元格，与上方rowspan组合后溢出。Pandoc会静默丢弃这段非空文字。未硬改列数/文字/HTML：输出适配在发布前比对HTML与DOCX的表数量及非空物理单元格文字顺序（保留重复值），不一致即拒绝。它只是丢失报警，不是表格求解器，也不验证所有空格/合并几何。

初版产生的57份派生文件属于失败实验，未替换最终目录；最终56份和1失败记录分开保存。原生57份Word始终存在且未改。

### 3.3 对照定位方法

不能按_table_1、_table_2文件名顺序直接对比Word第1、2张表：原生文件编号与正文阅读顺序不总一致。检查脚本用parsing_res_list中的完整block_content精确匹配同一原生HTML，再定位同名XLSX，记录源bbox。没有用内容近似匹配、移动列或修改fixture使结果通过。

## 4. 使用方法与限制

安装原项目依赖及外部Pandoc3.1.11.1。保持默认流水线不变，显式输出命令：

```bash
python scripts/export_saved_word.py work/step8/restored/sarc -o work/step9_word
python scripts/check_saved_word_export.py work/step8/restored/sarc/native work/step9_word -o work/step9_word_comparison.json
```

也接受单个native/job目录。输出目录必须是新目录；原生缓存校验失败、原生导出有errors、转换器版本不符、缺图片、外部资源、超时、表格文字丢失都报错，不覆盖旧文件。每个派生目录保存document.docx、intermediate.html、reference.docx及export.json；中间HTML依赖原缓存图片，不宣称是独立完整网页。export.json带版本、来源签名、输入输出哈希和未验收标记。

当前这不是默认Word导出的自动替换；正文Markdown解释、图形标志、分页、所有表格结构和独立录屏泛化尚未验收。不要把重排后的Word宣传为原稿复原。

## 5. 测试与运行证据

本地输出实验Python3.13.5、python-docx1.2.0、Pandoc3.1.11.1；与正式Python3.11不同。本地110 passed/1 skipped，跳过项为未安装PyAV的真实编解码测试。

正式回归run36444198176，工件10978754667，SHA256 22c09b88ccd8af62d5b018e8f77a04a9a6e9cc05a4b9c5f8fdddcfa606e739a2，到期2026-10-28T15:31:47Z。已下载JUnit核实111通过、0跳过，并保存转换器版本、安装包哈希、源码哈希。新增19项主要保护真实合并、位置、地址文本、图片字节、缓存不变、错误拒绝和两项实际失败。

需如实记录一个流程失误：第一次output.py提交匹配旧thin-pipeline.yml的宽泛paths，自动触发了旧六画面真实OCR回归run36443563353；其原生执行成功，内容门禁仍失败。该运行没有参与本轮输出改进对照，也没有重跑/覆盖已完成57-job工件。后续output.py修正使用[skip ci]避免再次触发昂贵旧流程，随后独立修改adapter-tests.yml，完整运行了上述111项回归，不是关闭验收来变绿。

详细机器摘要见step9_word_export_evidence.json。可复现检查脚本与所有代码、测试均在本分支。

## 6. 下一步唯一优先动作

从已完成工件的reconstruction.json读取group_000078_a成员和源映射，对照原帧、候选图及原生表格HTML，定位异常保密等级单元格是在拼接输入层还是结构识别层产生。暂不重新跑全片、不换引擎、不手改该单元格。随后再推进章节/条款覆盖清单和水印污染治理；全片覆盖、密集MemoryMap、全部Office成品均继续保持未验收。
