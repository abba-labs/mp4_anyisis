# EFC 原图提取与验收报告

日期：2026-10-05。分支：`docs/restore-6601-screenshots`。来源：本仓库EFC原始截图，不引入其他芯片资料。

## 1. 结论

**EFC的60张原图已全部完成首轮逐图核对：LRS 24张、LLD 36张；没有再留一批未处理整页。** 本轮补完LLD第25～36张，回查原有10组问题（LRS 1组、LLD 9组），其中7组核实补入，3组仍有局部残余；另在尾段登记2组原图小字问题，当前共5组未解决，全部位于LLD。

可辨内容已经写入两份完整Markdown；复杂图保留原图链接及可辨标签，代码截图保留可辨原始变量、条件、常量和diff，不补截图外代码。**仍不能宣布“全部字符准确无误”或“EFC全文最终验收通过”**：这5组需要更清晰的同源文件才能消除，不可通过重复放大、借用旧芯片资料或猜测关闭。

本轮是既有首轮工作收尾及疑点定点回查，不声称对既有60张又做了独立完整第二遍逐字验收。来源文件数、链接和哈希检查只证明对应的覆盖与保存条件，不证明字符准确率。

| 交付项 | 范围 | 状态 |
|---|---|---|
| [EFC LRS完整还原](efc_lrs/docs/EFC模块LRS设计文档.md) | 24张；原文正文、表格、图1-1～1-19及修改标记 | 原已登记U01关闭；保留原文差异，不等于第三方最终验收 |
| [EFC LLD完整还原](efc_lld/docs/EFC详细设计文档.md) | 36张；正文、接口表、代码、时序/状态图、系统评估和参考文献 | 末12张已处理；5组局部源图问题待更清晰原件 |
| [ET6601修改点总览](EFC_6601修改点总览.md) | 25条LRS＋52条LLD原图记录，逐项来源索引 | 原始文字仍在对应完整文档；77不是独立功能数 |
| 原图与台账 | 60个唯一原始PNG及固定Git blob/SHA-256 | 原图字节未修改；原图数量不是正确率 |

## 2. 本轮补完的12张原页

| 序号 | 原图 | 本轮实际处理内容 |
|---:|---|---|
| 25 | [GameViewer_Jv14xpHsSC.png](efc_lld/images/GameViewer_Jv14xpHsSC.png) | 恢复内嵌问题单的可辨字段、同步读时序标签及diff代码，保留READ MODE CHANGE红字；U10定位无法辨明的小字 |
| 26 | [GameViewer_SnGFBV0cqH.png](efc_lld/images/GameViewer_SnGFBV0cqH.png) | 恢复三段代码及红色批注；模式表15列、10行和5条Notes完整衔接；X不猜改为0/1 |
| 27 | [GameViewer_isM3FELYfq.png](efc_lld/images/GameViewer_isM3FELYfq.png) | 恢复明确的4项ET6601读模式优化，tNVS参数行及Sector Erase时序标签；“保持一致”不说成新增 |
| 28 | [GameViewer_98qp0YcXAk.png](efc_lld/images/GameViewer_98qp0YcXAk.png) | 恢复ECC读写域段取反红字和图2-15/2-16可辨标签；接续DFX错误说明；U11记录控制信号小字 |
| 29 | [GameViewer_bJ7d9eVqlF.png](efc_lld/images/GameViewer_bJ7d9eVqlF.png) | 逐项转录编程顺序、选通、不一致和配置ECC错误，保留清零要求的青蓝字 |
| 30 | [GameViewer_hoWrmQ3kyX.png](efc_lld/images/GameViewer_hoWrmQ3kyX.png) | 分别转录数据ECC、门控/复位APB、门控AXI错误，不把配置和数据接口混为一谈 |
| 31 | [GameViewer_OCJBCUSbNK.png](efc_lld/images/GameViewer_OCJBCUSbNK.png) | 完成13项DFX错误说明及ECC注入；恢复4行配置表，sec默认值原图空白照留 |
| 32 | [GameViewer_x2k55BuYBA.png](efc_lld/images/GameViewer_x2k55BuYBA.png) | 读datapath标签、两级pipeline、latency与吞吐说明；原作者拼写不润色 |
| 33 | [GameViewer_b5AJYTEhY1.png](efc_lld/images/GameViewer_b5AJYTEhY1.png) | 补回39/78/31/60us及1.85/0.925/2.32/1.21Mbps等遗漏值，完整转录擦除与RETRY估算 |
| 34 | [GameViewer_f9t1x50Gvk.png](efc_lld/images/GameViewer_f9t1x50Gvk.png) | 11行对外要求及跨页续句；PR0数字0修正，整行删除线保留；不执行原文钉钉动作 |
| 35 | [GameViewer_vC7gPIngZA.png](efc_lld/images/GameViewer_vC7gPIngZA.png) | 3组时钟/复位标签和T>0；测试矩阵原来误拆的单元格恢复为4行 |
| 36 | [GameViewer_V6W79lgJB6.png](efc_lld/images/GameViewer_V6W79lgJB6.png) | 7条参考文献及右页空白范围确认；不借所列文献填补正文 |

### 表格错接与漏项的处理

DFLASH/PFLASH接口续表的84/72信号行沿用既有已核对成果；FCTRL表保持34行。本轮新增模式表10行、ECC注入表4行；对外要求表保留11行。

测试矩阵的“内部接口／内部FIFO”属于一个单元格的两行字，SVA只有一个勾；“性能／BOOT”同样是一个单元格的两行字，FPGA只有一个勾。已经恢复4行表，不能把两组拆开后擅自把勾分给子项。机器检查只检查行列，不代替这次看图核实。

## 3. 已解决的7组旧问题

| 原编号 | 源图位置 | 本轮核实结果 |
|---|---|---|
| LRS-U01 | LRS图1-6、GameViewer_6F5qGwog2V.png，CRG旁黄色框 | “拉低芯片复位，把CPU启动Hold住；EFC复位撤销，启动EFC操作。”已补回 |
| LLD-U02 | 第13张，右页下方黄色框 | “如果需要做复位，Flash需要做：”已核实；不自行改成软复位或硬复位 |
| LLD-U03 | 第14张，图2-4 | s12_fctrl_state前缀已辨明，数字1照录 |
| LLD-U04 | 第17张，图2-6 | rst_curst_working==1'b1及WR框的“根据”已补回 |
| LLD-U05 | 第18张，图2-7 | ST_UPT_STS末行“minus first to valid cnt”已补回，不润色英文 |
| LLD-U07 | 第22张，图2-11 | PROG0/PROG1/PRE1/PROG3括号中的tWS、tNVS、tADH/tPREPGH、tPGH已补回 |
| LLD-U08 | 第23张，图2-12/2-13 | tCFS/tWFS、tWFH/tCFH、tCFL、tWS、tNVS已补回 |

以上状态只指原先登记位置在本轮已可辨；不用于替其他位置作类推。

## 4. 仍需更清晰同源资料的5组

原图均为1920×1080。以下是可定位的剩余文本缺口，不是未处理整页，也不是仅剩5个字。已使用原PNG与局部裁切查看；放大不增加原始像素信息。

| 编号 | 原图与具体位置 | 尚不能确定的内容 | 本轮已完成的局部修订 |
|---|---|---|---|
| LLD-U01 | [第5张GameViewer_oiTQxKdn2v.png](efc_lld/images/GameViewer_oiTQxKdn2v.png)，右页图1-2的两组结构图 | NVR/NVR_CFG/RDN容量小字、少量引脚完整名和总线下标 | 补录无下标的20个可确认控制/输出标签；未依据LRS反推容量 |
| LLD-U06 | [第21张GameViewer_ceValKI1oj.png](efc_lld/images/GameViewer_ceValKI1oj.png)，右页图2-10 | 蓝色状态名完整前缀、底部retry条件框的部分细字 | 中央“且”“>=”和自环“读操作未结束”已辨明；完整拼写仍不擅补 |
| LLD-U09 | [第24张GameViewer_xS9sUaBAU3.png](efc_lld/images/GameViewer_xS9sUaBAU3.png)，左页底部/右页顶部波形 | 部分小数值、最后一路信号名及右页波形左下参数名 | 图2-14复合条件回查，read_cmd_lat改正；tMS/tMH五列表格回查 |
| LLD-U10 | [第25张GameViewer_Jv14xpHsSC.png](efc_lld/images/GameViewer_Jv14xpHsSC.png)，左页内嵌问题单、右页代码上方小字 | 完整问题描述、姓名列表、完整状态字形、附件完整文件名、代码上方细字 | 标题、可辨字段、差分代码和红色批注已提取；不可辨部分不删除，也不拼成假完整句 |
| LLD-U11 | [第28张GameViewer_98qp0YcXAk.png](efc_lld/images/GameViewer_98qp0YcXAk.png)，左页图2-15控制输入 | 写分拆/全1判断和部分ECC使能信号的完整拼写 | 门名、已辨数据位段、正文ECC取反说明保留，未知前缀未猜写 |

真正关闭这些位置需要对应EFC LLD原始DOCX/PDF、原始Visio/波形/表格，或同一页面更高分辨率截图。现有截图之外的ET60157/ET6801规格不能作为填字依据。统一从此表的局部位置恢复，不重跑60张封面到末页的盲目扫描。

## 5. 原文差异与识别缺口分开

原文能看清但自身不一致的地方，不标成“没识别出来”，也不修改设计。包括：LRS目录/正文紧急撤销编号、NVR分区及3KB/5KB用户OTP说法、PFLASH整片与sector/32KB保护粒度、不同图默认时钟，LLD接口0x00/0x5A、25～200/25～100MHz、模块名/状态名差异，以及图2-16标题仍为“写入图”。

LRS原D01～D05及第三轮LLD差异记录继续保留。本文不对哪个设计版本正确作裁决。

## 6. 校验范围

校验记录：[EFC_ROUND4_VERIFY_20261005.json](../reviews/EFC_ROUND4_VERIFY_20261005.json)。60张原始PNG分别检查字节数、Git blob、SHA-256；两份完整文档检查来源锚点、图片链接、表格列数、代码围栏及来源记录编号连续性。

正文提交、台账更新与远端文件校验分别记录；不因工作流绿色就宣称视觉验收通过。本轮没有运行硬件测试，也没有把文中性能估算或测试矩阵作为实测结果。

本阶段状态：**全部EFC源图已处理并形成可复核交付；5组源图细字未达到逐字符验收，最终内容验收仍未通过。** 未解决项不会被自动更名为已完成。
