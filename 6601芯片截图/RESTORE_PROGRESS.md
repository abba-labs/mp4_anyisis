# ET6601 原图还原进度与验收台账

更新日期：2026-10-05。工作分支：`docs/restore-6601-screenshots`。

## 1. 当前断点

**第三轮已将EFC LLD累计前24/36张首轮核对正文写回GitHub；本批新增核对第13～24张，第二轮仅本地保存的前12张也已并入。下一张为第25张GameViewer_Jv14xpHsSC.png。**

正文：[EFC详细设计文档](efc/efc_lld/docs/EFC详细设计文档.md)。正文提交：`5ebf63883ab20d5bd97fd2fc01bbda7ae10c4679`；blob：`f1d78519289d23f9b8833ba9f02de1cf07fdc20f`，91310字节；GitHub回读与本地一致。

本批记录：[逐图复核记录](reviews/EFC_LLD_ROUND3_REVIEW_20261005.md)、[36张原图清单](reviews/EFC_LLD_ROUND3_IMAGE_LEDGER_20261005.json)、[保存检查](reviews/EFC_LLD_ROUND3_SAVE_VERIFY_20261005.json)。LLD有9组局部小字/条件仍待复核，详见记录；不是仅9个字。累计41条修订/红字/删除线证据、5条蓝字说明，证据数不是独立功能修改数。

全仓已首轮核对48/200张：LRS24＋LLD24；剩余152张未完成本轮逐图核对。这不是正确率或最终验收率。LRS原24张成果未改动，仍保留1处U01；LRS正文提交`0de59b53b4ed6134ade4bc3320880d5b6f2c9ae9`、blob`06b91f036a6427d0c48ec71525f0caf3c415af38`，25条证据和4条蓝字说明均保留。

只继续具体断点，不从封面重做，不重新合并CPLD_INTERFACE。所有文档均未最终验收；不可用链接/列数/哈希通过来替代逐字符核对。

## 2. 原始截图清点

清点依据：源包`SOURCE_MANIFEST.json`中的Git树清单，来源commit为`db9422fd7345fb0b600c7ac6c9db25a3140344ed`。排除`.review_cache`及派生裁切图后，共200张原始截图，合计192193751字节。清点文件不是逐字准确性验收。

| 原始文档/资料组 | 原始截图数 | 本轮状态 | 后续动作 |
|---|---:|---|---|
| CPLD_INTERFACE（十组旧来源合计） | 32 | 合并正文已存在；本轮尚未重新逐图复核 | 保留一份完整文档，按32张来源核对 |
| CPLD_REG | 9 | 本轮待复核 | 逐行核对寄存器表 |
| CPLD PPI说明文档 | 7 | 本轮待复核 | 保持原始独立文档 |
| EFC LRS | 24 | 首轮逐图核对已保存；1处待复核 | 保留准确断点，后续处理局部疑点与二次复核 |
| EFC LLD | 36 | 前24张首轮核对并提交；9组局部待复核，后12张待处理 | 从第25张继续 |
| SARC功能框图资料组 | 11 | 本轮待复核，原始文档边界待确认 | 不以截图分组自动认定文档边界 |
| SARC LLD | 40 | 本轮待复核 | 正文精校及明确修改标记 |
| SARC LRS | 13 | 本轮待复核 | 正文精校及明确修改标记 |
| SARC XBAR资料组 | 27 | 本轮待复核，原始文档边界待确认 | 先确认来源和阅读顺序 |
| HAC_WRAP架构资料 | 1 | 本轮待复核 | 核对全部文字及明确修改标记 |
| **合计** | **200** | **未最终验收** | **不能将旧文档的完成声明视为本轮验收证据** |

模块合计：CPLD48，EFC60，SARC91，HAC_WRAP1。CPLD_INTERFACE来源分布：interface_cpld3、interface_cpld_cfg6、interface_cpld_crg1、interface_cpld_tcu1、interface_dma1、interface_efpga16、interface_efpga_cfg1、interface_int1、interface_ppi1、interface_test_pin1。

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
| 08 | GameViewer_6F5qGwog2V.png | 6278ce6f8200618f0f5763844ba1a949abda37f8 | 图1-6、Wafer Testing、地址空间表；首轮核对，U01未解决 |
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

### U01：局部像素不足，仍待复核

- 原图：[GameViewer_6F5qGwog2V.png](efc/efc_lrs/images/GameViewer_6F5qGwog2V.png)，左页Boot流程图，CRG旁第一个黄色框第一行。
- 该行前两个字无法100%确认；只登记疑似“拉低芯片复位”，没有写成确定正文。
- 已尝试原始PNG及局部放大查看；不能通过再次缩放或技术推理制造不存在的细节。
- 后续仅使用更清晰的同源截图/原始文档确认该局部。不需要停止其他原图的处理，也不能将此项自动改为已解决。

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


## 6. EFC LLD接续与保存记录

完整36张原图的阅读序号、文件名、字节数、Git blob、SHA-256和首轮核对状态见`reviews/EFC_LLD_ROUND3_IMAGE_LEDGER_20261005.json`；第13～24张详细转录范围及LLD-U01～U09见`reviews/EFC_LLD_ROUND3_REVIEW_20261005.md`。25～36张的顺序仍待原图确认，已有转录不当作已验收。

本批正文恢复两处nSWBOOT1/nBOOT1删除线，核对34行FCTRL接口、图2-3～2-14可辨文字、访问保护与READ MODE修改标记。第25～36张未核对正文原样保留；其尾段SHA-256为`de869668e70cee995b18312196756ac18cedb68ee127bed09ca34f381f8b4e94`。

下一张路径：`efc/efc_lld/images/GameViewer_Jv14xpHsSC.png`。先核对问题单、READ MODE CHANGE等待tMH批注及代码截图，再继续26～36张。对看不清的字段定位登记，不依据代码常识或其他芯片资料补全。后续再进行局部疑点及全文二次复核。

保存异常已处理：首次写入的未核对尾段有1处AXI被误转写成APB，全文比对发现后恢复原字节，最终blob回读一致。一时性修复workflow已自删除；该次额外artifact上传失败不影响已成功提交的正文，但不能标为运行全成功。详情留存在保存检查JSON。
