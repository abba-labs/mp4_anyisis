# ET6601 原图还原进度与验收台账

## 第九轮最新断点

第九轮已回查LLD-U07～U12六张原PNG，补入sample/conversion、signed下方两行说明、缓存j-1/j+1索引和计数输入拼接。全部仍有局部缺口，无整组关闭；已完成U01～U12定点回查，不重复首轮。SARC64/64、全仓124/200不变，LLD19＋S01、LRS3、辅助2继续开放；78条来源位置不变。下一项LLD-U13：GameViewer_ZwgMgCyaeL.png左右时序图。

记录：`6601芯片截图/reviews/SARC_GAP_ROUND9_REVIEW_20261005.md`；正式保存及回读见同轮REMOTE_SAVE。下方旧断点仅为历史快照。


更新日期：2026-10-05。工作分支：`docs/restore-6601-screenshots`。

## 1. 当前状态（SARC第八轮：缺口定点回查）

U01～U06的6张原图已回查并更新方案正文；无整组关闭，未扩张首轮计数。详见[第八轮记录](reviews/SARC_GAP_ROUND8_REVIEW_20261005.md)和同轮REMOTE_SAVE。

第六轮5张保存回读后，本批再核6张，辅助11/11已整图首轮。旧稿漏掉的c74Kardt0X、qNBgXqkj5C、Wb2pLAEGMa三图已补正文；不再有未首轮的SARC原始PNG。

[辅助正文](sarc/sarc_diagrams/docs/SARC功能框图说明.md)、[本批记录](reviews/SARC_AUX_ROUND7_REVIEW_20261005.md)、[11张台账](reviews/SARC_AUX_ROUND7_IMAGE_LEDGER_20261005.json)、[远端回执](reviews/SARC_AUX_ROUND7_REMOTE_SAVE_20261005.json)。辅助图不是已证实连续同版的原始文档，A编号仅为来源索引。

全仓124/200首轮＝EFC60＋SARC64；剩76＝独立XBAR27＋CPLD48＋HAC_WRAP1。SARC64/64是已存64张PNG覆盖，不证明原文来源页完整或最终准确。未关闭：LLD19组＋S01，LRS3组，辅助AUX-U01/U02两组。EFC5组暂缓。修改位置78条保持；辅助颜色/批注另列。

下一步从LLD-U07的UUhaiE4moy（图5-4）继续；U01～U06无新清晰同源材料时不重复整轮回查；每4～6张定点原图完成正文、缺口、当前入口的实际保存和回读。不得把15bit辅助图覆盖5bit正文，不重复恢复任何旧分片。

## 2. 原始截图清点

清点依据：源包`SOURCE_MANIFEST.json`中的Git树清单，来源commit为`db9422fd7345fb0b600c7ac6c9db25a3140344ed`。排除`.review_cache`及派生裁切图后，共200张原始截图，合计192193751字节。清点文件不是逐字准确性验收。

| 原始文档/资料组 | 原始截图数 | 本轮状态 | 后续动作 |
|---|---:|---|---|
| CPLD_INTERFACE（十组旧来源合计） | 32 | 合并正文已存在；本轮尚未重新逐图复核 | 保留一份完整文档，按32张来源核对 |
| CPLD_REG | 9 | 本轮待复核 | 逐行核对寄存器表 |
| CPLD PPI说明文档 | 7 | 本轮待复核 | 保持原始独立文档 |
| EFC LRS | 24 | 全部首轮核对，U01已核实；原文差异保留 | 不重复处理已解决的图1-6小字 |
| EFC LLD | 36 | 全部首轮核对；仅5组源图细字待确认 | 只按第四轮报告定位回查，不再留未处理整页 |
| SARC辅助框图资料组 | 11 | 11张整图首轮；2组局部字形待确认；保留独立来源边界 | 定点回查，不跨版本填字 |
| SARC方案设计（旧sarc_lld） | 40 | 40张首轮至文末；19组局部缺口及S01未关闭 | 先核辅助图边界，再以确认同源同版区域定点回查 |
| SARC LRS | 13 | 首轮逐图核对；3组图内小字待确认 | 保持一份完整文档，后续定点复核 |
| 独立XBAR文档（旧sarc_xbar） | 27 | 封面已确认，正文未首轮核对 | 独立处理，不混入SARC修改点 |
| HAC_WRAP架构资料 | 1 | 本轮待复核 | 核对全部文字及明确修改标记 |
| **合计** | **200** | **未最终验收** | **不能将旧文档的完成声明视为本轮验收证据** |

原目录合计：CPLD48，EFC60，sarc目录91，HAC_WRAP1。sarc目录91中含SARC相关64（LRS13、方案40、辅助图11）及独立XBAR27；目录合计不能等同原始文档边界。CPLD_INTERFACE来源分布：interface_cpld3、interface_cpld_cfg6、interface_cpld_crg1、interface_cpld_tcu1、interface_dma1、interface_efpga16、interface_efpga_cfg1、interface_int1、interface_ppi1、interface_test_pin1。

## 3. EFC LRS逐图记录（第一轮保留）

下表按原文阅读顺序排列，不按文件名排序。每张均核对左页后右页；状态“首轮核对”不代表最终验收。图片目录统一为`efc/efc_lrs/images/`；正文中保留每张原图链接。

| 顺序 | 原图文件名 | Git blob SHA | 核对范围与状态 |
|---:|---|---|---|
| 01 | GameViewer_XujivZGdpN.png | 6071999af1889349e5d11ed3a49e7556e13e3027 | 封面、设计/评审/批准；首轮核对 |
| 02 | GameViewer_fpb2HKWthL.png | 0f668520ae43c6831dff98cdf9809b83dd20afcf | 修订记录1.0/1.1及目录；首轮核对；C01~C02 |
| 03 | GameViewer_tD5gCQa3Jp.png | 502b286ba01a9c9c370ecc2711738d23170f1824 | 目录续页；1.2.12紧急撤销确为原文 |
| 04 | GameViewer_bqG5XHiWOd.png | 1ecc11346c5907096a2a273e9cbd1b548b4aeec1 | 图表目录及模块简介；保留原文Salve等拼写 |
| 05 | GameViewer_jyfWngVZvO.png | 2ff9392ee722328603f47a20426ef7c13ca71b07 | 图1-1/1-2、流程步骤和标签；首轮核对 |
| 06 | GameViewer_oT9ct4X3PL.png | cd9c98ef948e1b9e29f29371ac1c6508d26f4841 | 图1-3/1-4、软复位/门控、跨页续句；首轮核对 |
| 07 | GameViewer_N4leDL0su5.png | 80434f13dc9f408edfd309edfa12462de95c0b49 | 图1-5、蓝字说明；首轮核对 |
| 08 | GameViewer_6F5qGwog2V.png | 6278ce6f8200618f0f5763844ba1a949abda37f8 | 图1-6、Wafer Testing、地址空间表；首轮核对；第四轮U01已核实 |
| 09 | GameViewer_BG11R4KzQV.png | 02a96c52907bc580207db05784cd35be03b1910a | 地址表末行、图1-7/1-8/1-9、红字间接读取要求；C03 |
| 10 | GameViewer_u7x2KWkvm5.png | c2b4c741c55e89286253d1379a6cee952087623a | 图1-10/1-11、Main/RDN读写；首轮核对 |
| 11 | GameViewer_RIxO2iF81c.png | 01fcf8d7f8ad7457ddfd56d14b87e7da08dc9cb8 | 图1-12/1-13、0.8~1ms Retry与擦除流程；首轮核对 |
| 12 | GameViewer_nD3eu17L6q.png | cced27ec701836f3cb60b3140c298e82e5d2c204 | 六行间接访问寄存器表、图1-14、RECALL；首轮核对 |
| 13 | GameViewer_bTZBDjzsW4.png | dd8861d78cfffe4d68ba5ec5b53abaae0a8e6486 | 图1-15/1-16、Retry超过20次返回、寄存器key；首轮核对 |
| 14 | GameViewer_cSaHi20ulN.png | f62bdc5c1505f348d354b0eb85ee9cf1912bcbc6 | key续页、NVR_CFG写保护、图1-17；首轮核对 |
| 15 | GameViewer_BiWjxKhdcj.png | ebf5bd9883f47315717350bb97cd4ebdad1d4a81 | NVR写保护续页、图1-18、1.2.10.1；首轮核对 |
| 16 | GameViewer_5UxkiNGtxh.png | eef116c8b7f8ebc74ea69d7806c6ba85f0a587c9 | 架构条目5~9、八行OTP表及全部红字；C04~C09 |
| 17 | GameViewer_MMRNU2QuKX.png | 75e24c9d3f5ec2fbf14441d5df4f31ad94cffa1b | 图1-19、紧急撤销、CLK/RST；正文1.2.11已核实，非未识别项 |
| 18 | GameViewer_gYLpTulBVN.png | 7e593cf83f5971e6a5c59e1565c00c0e41b7068e | SOC01~09、BANK地址与红字；C10~C12 |
| 19 | GameViewer_cQ0Ir7RHZa.png | f76b81dbebe9a5e7cc2c96d55de028ec17df3e5f | ECC删除线/使能、SOC10、SEC01~06、CPU1；C13~C18 |
| 20 | GameViewer_7Jsq6PhQM2.png | 92a3ccb30fe8b4c34a48938747b4a63dfdfca9f8 | SEC07~13、USER OTP、sector/16KB；C19~C20 |
| 21 | GameViewer_LLELUTfGM7.png | 14a1b76911163e1b909bcaacce4ff4bc6d28da2d | SEC13续页、全片擦除六步、SEC15/16、FLASH01~06；C21~C24 |
| 22 | GameViewer_Umv4eQVy3N.png | 611640cd6caaefc4818a4cf52eb0a1a0f1284cbc | FLASH06续页~11、DFT/DFX/RBST；C25 |
| 23 | GameViewer_gLi3yEXagB.png | 9e880a571cc75627d844ec424c5afb6fee0441fa | RBST续页、中断、事件、LIMIT01~06；首轮核对 |
| 24 | GameViewer_BMgqvo1P0z.png | 0e2e17ab03fd5b3e800a9a5d22e91afc85b1f1c4 | LIMIT07/08、触发源、五条参考文献；首轮核对 |

## 4. EFC LRS待复核与原文差异（保留）

### U01：第四轮已核实关闭

原图：[GameViewer_6F5qGwog2V.png](efc/efc_lrs/images/GameViewer_6F5qGwog2V.png)。本轮再次查看CRG旁黄色框的局部字形，确认“拉低芯片复位”，已补入LRS正文；不再列为未解决项。以下D01～D05仍是已确认的原文差异，不因U01关闭而被消除。

### D01~D05：原文差异已看见，必须保留

| 编号 | 原文位置 | 差异 | 处理 |
|---|---|---|---|
| D01 | 目录tD5gCQa3Jp；正文MMRNU2QuKX | 目录1.2.12紧急撤销，正文1.2.11紧急撤销；正文交叉引用仍为1.2.11.3/1.2.11.4 | 各处照录；不得再标成未看原图的编号疑点 |
| D02 | 目录fpb2HKWthL；正文6F5qGwog2V | 目录含1.2.6数据预取，后续目录编号与正文不同 | 不编造未出现的正文段落，不改原编号 |
| D03 | 6F5qGwog2V地址表；BiWjxKhdcj/5UxkiNGtxh及后文SEC | NVR分区表与后文ROM/OTP/OB区域描述不完全一致 | 分别按原文保存，不自行统一芯片规格 |
| D04 | 5UxkiNGtxh架构第9条；LLELUTfGM7 SEC13 | PFLASH写保护“以整片为单位”与“以sector/32KB为单位”并存 | 保留两处并标记出处，不选一个覆盖另一个 |
| D05 | jyfWngVZvO图1-1；6F5qGwog2V图1-6 | 上电流程默认25MHz，Boot图默认256KHz | 保留各自图中文字，不按常识改动 |

## 5. EFC LRS第一轮检查证据与验收边界

已执行：83个导出文件SHA-256校验；EFC LRS24个唯一原图锚点；图1-1至1-19引用覆盖；原图链接存在性；Markdown表格列数一致性；25个修改证据编号连续性；ECC删除线和CPU1关键字检查；1处显式待复核标记检查；正文远端blob与本地输出一致性。

机器检查只能发现覆盖、格式、链接及保存问题，不能替代人工逐字核对，不能据此宣称字符准确率100%。本批没有硬件运行测试，也不应产生硬件通过结论。

正文以一份Markdown保存，跨页表格/续句已连续衔接并标出来源。复杂时序图和连线仍以原图为准；没有凭空重画图形。

CPLD为新IP，不机械增加旧IP修改总结。继承IP的红字只说明原图标红；没有明确旧版本依据时，不擅自写“旧值→新值”。蓝字单列，不混入确定修改数量。


## 6. EFC LLD接续与保存记录（历史快照，非当前入口）

> 以下是EFC第三轮当时的断点；当前EFC已36/36首轮、5组遗留且用户暂缓。不得把本节旧“下一张”当作实时任务。

完整36张原图的阅读序号、文件名、字节数、Git blob、SHA-256和首轮核对状态见`reviews/EFC_LLD_ROUND3_IMAGE_LEDGER_20261005.json`；第13～24张详细转录范围及LLD-U01～U09见`reviews/EFC_LLD_ROUND3_REVIEW_20261005.md`。25～36张的顺序仍待原图确认，已有转录不当作已验收。

本批正文恢复两处nSWBOOT1/nBOOT1删除线，核对34行FCTRL接口、图2-3～2-14可辨文字、访问保护与READ MODE修改标记。第25～36张未核对正文原样保留；其尾段SHA-256为`de869668e70cee995b18312196756ac18cedb68ee127bed09ca34f381f8b4e94`。

下一张路径：`efc/efc_lld/images/GameViewer_Jv14xpHsSC.png`。先核对问题单、READ MODE CHANGE等待tMH批注及代码截图，再继续26～36张。对看不清的字段定位登记，不依据代码常识或其他芯片资料补全。后续再进行局部疑点及全文二次复核。

保存异常已处理：首次写入的未核对尾段有1处AXI被误转写成APB，全文比对发现后恢复原字节，最终blob回读一致。一时性修复workflow已自删除；该次额外artifact上传失败不影响已成功提交的正文，但不能标为运行全成功。详情留存在保存检查JSON。
