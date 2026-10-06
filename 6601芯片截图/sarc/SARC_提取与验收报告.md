# SARC 原图提取与验收报告

## 第十三轮当前结论：主体阅读交付与局部验收分开

2026-10-06。用户确认局部图内小字不应阻塞整体原理理解后，本轮形成来源导读及LRS/LLD联合修改索引。现有SARC64/64张首轮、全仓124/200、78条来源位置均不变；没有新增原图视觉核对，也没有新增缺口关闭。LLD19＋LRS3＋辅助1＝23组及S01继续开放。

主体资料可用于理解已确认的请求链、两条数据处理路径、过采求和及结果输出。涉及具体公式、位宽、精确时序或模糊配置时，仍须定点核实。该用途说明不是原文修订、硬件验证或最终逐字验收通过。

阅读入口：[工作链路与6601修改导读](SARC_工作链路与6601修改导读.md)、[联合修改索引](SARC_6601修改点总览.md)、[待补清单](SARC_待补原始资料清单.md)。本轮保存及边界检查见`../reviews/SARC_DELIVERY_ROUND13_REVIEW_20261006.md`及同轮VERIFY/REMOTE_SAVE。三份原图还原正文逐字节保持；导读为已有来源的辅助读物，不作为第四份最终还原正文。

## 第十二轮历史结论：已全量回查，仍待原始资料

现有SARC的64张PNG全部完成首轮后，原登记24组局部缺口及S01已全部定点回查（第八～十二轮）。补齐确认文字，关闭AUX-U02；仍有23组局部缺口＝LLD19＋LRS3＋辅助1，另有S01。没有未首轮处理的SARC整张图，也没有未发布分片；不等于来源连续性或逐字验收通过。确定来源位置仍78条，C11/C46仍不完整。全仓124/200不变，EFC5组暂缓，XBAR/CPLD/HAC_WRAP不混入SARC。

待补清单：`6601芯片截图/sarc/SARC_待补原始资料清单.md`，逐组给出原图、区域、剩余内容和所需资料。下一步为取得同版清晰源后按组补录及验收；没有新来源时不再重复整轮放大，也不把候选或遮挡自动关闭。

本轮4张（辅助2＋连续性边界2）；实际正文、台账和回读见`SARC_GAP_ROUND12_REVIEW_20261005.md`、IMAGE_LEDGER、VERIFY及REMOTE_SAVE，均在reviews目录。下方旧状态仅为历史快照。

## 第十一轮历史断点

第十一轮已回查LLD-U19及LRS-U01的两个来源、U02、U03，共5张原PNG。方案正文补两个黑色结果寄存器块8*(16+16)bit；LRS两图节点S/H纠为SH，需求里的S/H保留。19组LLD与3组LRS均已定点回查，但仍有局部缺字，未关闭整组。下一批只回查辅助U01/U02与S01，并归集未满足验收的来源清单；首轮64/64、全仓124/200、78条来源位置不变。

实际提交、回读和逐图记录见`6601芯片截图/reviews/SARC_GAP_ROUND11_REMOTE_SAVE_20261005.json`及同轮REVIEW/IMAGE_LEDGER。下方为历史快照。

## 第十轮历史断点

第十轮回查LLD-U13～U18六张原PNG，补入PIPE RAM末行1111/0000/0001及中断图cfg_*_int_force_ind、寄存器读、intr。小字未清的部分全部保留，无整组关闭。U01～U18已定点回查；SARC64/64、全仓124/200和78条来源位置不变。下一批：LLD-U19（GameViewer_YbkCdqx6qz.png），再LRS三组和辅助两组；S01单列来源连续性回查。

详细记录和实际提交/回读：`6601芯片截图/reviews/SARC_GAP_ROUND10_REVIEW_20261005.md`及同轮REMOTE_SAVE。下方旧断点是历史快照。

## 第九轮历史断点

第九轮已回查LLD-U07～U12六张原PNG，补入sample/conversion、signed下方两行说明、缓存j-1/j+1索引和计数输入拼接。全部仍有局部缺口，无整组关闭；已完成U01～U12定点回查，不重复首轮。SARC64/64、全仓124/200不变，LLD19＋S01、LRS3、辅助2继续开放；78条来源位置不变。下一项LLD-U13：GameViewer_ZwgMgCyaeL.png左右时序图。

记录：`6601芯片截图/reviews/SARC_GAP_ROUND9_REVIEW_20261005.md`；正式保存及回读见同轮REMOTE_SAVE。下方旧断点仅为历史快照。


## 第八轮定点回查

U01～U06已按6张原PNG回查，方案正文补入表1第002行“采样校准”、图1的SH与分区标题、图5-3的Signed B=A和Signed C[15:0] = B[11:0] << 2及round/sat标签。没有用后文、辅助异版或其他芯片资料猜补。6组仍有残缺；U05是实际遮挡，不能用放大恢复被遮像素。

SARC仍64/64首轮，LLD19组＋S01、LRS3组、辅助2组；确定来源位置78不变。旧“辅助0/11”正文状态已同步为11/11，未把局部回查充当整份复验。下一项U07。实际正文提交及回读见[第八轮回执](../reviews/SARC_GAP_ROUND8_REMOTE_SAVE_20261005.json)，细节见[回查记录](../reviews/SARC_GAP_ROUND8_REVIEW_20261005.md)。

## 第七轮报告（历史快照）

2026-10-05，第七轮：辅助余6张已完成，辅助11/11、SARC64/64首轮；全仓124/200，剩余76张属于XBAR/CPLD/HAC_WRAP。64/64不等于逐字准确或来源页完整。

本批补回旧稿缺失的c74/qNBg/Wb2三张，完整保存校准、FIR/IIR/非滑动平均、预处理校正和定标通路；重录9ak校准15bit及signed删除线；核对抢占四模块七条连线、过采求和全标签和浅蓝区。旧辅助8块乱序碎片已替换为11来源独立索引，不拼成伪造连续文档。

未关闭LLD19组＋S01、LRS3组；辅助新增AUX-U01（iir_coeff上方限定字）/U02（yBUF输入说明中段）两组。下一步逐项回查，不将这些缺口删除来宣称完成。确定修改位置78，辅助标记另列；EFC5组暂缓。

[辅助正文](sarc_diagrams/docs/SARC功能框图说明.md)；[第七轮记录](../reviews/SARC_AUX_ROUND7_REVIEW_20261005.md)；[台账](../reviews/SARC_AUX_ROUND7_IMAGE_LEDGER_20261005.json)；[保存回执](../reviews/SARC_AUX_ROUND7_REMOTE_SAVE_20261005.json)。下一定点LLD-U01，v6tUVs7H0k右页表1。

## 第六轮报告（历史快照，以下旧断点不再生效）

# SARC 原图提取与验收报告

更新：2026-10-05，第六轮辅助图首批。

辅助图5/11整图首轮，SARC58/64、全仓118/200；其余6张未核。已更新同一份[SARC辅助图原始文字还原](sarc_diagrams/docs/SARC功能框图说明.md)，完整保存4路输入拼接、乘加/反馈、8路输出拼接、红色重定标批注及架构图全标签。四张重叠取景没有伪装成连续原文页；架构绿色是模拟电路图例，不是修改色。

旧辅助稿仅8个来源块，未覆盖c74、qNBg、Wb2三张；它们已列待转录，不以旧“忠实还原”声明当验收。LLD19组及S01、LRS3组、EFC5组均保持，78条确定来源位置未变。下一张9akceoHcVF，随后余5张；完成后再定点回查。

[第六轮复核](../reviews/SARC_AUX_ROUND6_REVIEW_20261005.md)；[逐图台账](../reviews/SARC_AUX_ROUND6_IMAGE_LEDGER_20261005.json)；[保存回执](../reviews/SARC_AUX_ROUND6_REMOTE_SAVE_20261005.json)。本批不是最终验收。

## 第五轮报告（历史快照，旧断点不再生效）

# SARC 原图提取与验收报告

更新：2026-10-05，第五轮。分支：`docs/restore-6601-screenshots`。

## 当前结论与接续

**本批第37～40张4张，方案设计累计40/40首轮至文末；SARC相关53/64，全仓113/200，剩87张。** 不是最终验收：方案U01～U19共19组局部缺口与S01来源连续性疑点、LRS3组均未关闭。EFC5组仍按用户安排暂缓。

恢复FIFO映射和bitmap时序、EOC三个选项/16bit延时及输入关系、6002清单整段删除线、6601“1+4路”中断和跨页求和选项、DMA_MUX及FIFO请求说明、CPU_WRAP两组/200M跨页蓝字，保留第7/8节原空白。新增U16～U19为四图细字；前三幅重复图5-20、两个/三个选项、enc_p和adc_result/sarc_result差异照录。

正文：[SARC模块方案设计](sarc_lld/docs/SARC_LLD设计文档.md)；[第五轮记录](../reviews/SARC_LLD_ROUND5_REVIEW_20261005.md)；[逐图台账](../reviews/SARC_LLD_ROUND5_IMAGE_LEDGER_20261005.json)；[远端回执](../reviews/SARC_LLD_ROUND5_REMOTE_SAVE_20261005.json)。前36个原图正文块逐字节保留，辅助图/XBAR/LRS/EFC及原PNG未改。

| 范围 | 首轮状态 | 未完成 |
|---|---|---|
| 方案设计 | 40/40 | 19组局部缺口＋S01，未最终验收 |
| SARC LRS | 13/13 | 3组图内缺口 |
| 辅助图 | 0/11整图 | 边界、同源版本、全部图内文字待核 |
| XBAR | 0/27，独立 | 不计为SARC子文档或修改点 |

C42～C46新增5条，LLD46＋LRS32＝78条来源记录，不是独立功能数；B16～B19另列。C46图内缺字与原C11遮挡保留，不冒充完整准确记录。

**下一入口：辅助图`GameViewer_323Uh2DKeH.png`整图核对，并确认其与方案第29张相同局部的边界。** 这只是辅助资料的核对入口，不认定文件名排序为原始文档页序；仍按每4～6张正式保存。现有辅助Markdown须读最新版本后再改，不把旧包内容覆盖入库；不再从方案第32或37张重新开始。

## 第四轮报告（历史快照，以下旧断点不再生效）

# SARC 原图提取与验收报告

更新：2026-10-05，第四轮。分支：`docs/restore-6601-screenshots`。

## 当前结论与接续

**方案设计本批新核对第32～36张5张，累计36/40；SARC LRS13张保持不变。SARC相关49/64首轮，全仓109/200，剩余91张。** 首轮覆盖数不是准确率或最终验收率；辅助图整图仍0/11。

本批正文：[SARC模块方案设计](sarc_lld/docs/SARC_LLD设计文档.md)；[第四轮详细记录](../reviews/SARC_LLD_ROUND4_REVIEW_20261005.md)；[逐图台账](../reviews/SARC_LLD_ROUND4_IMAGE_LEDGER_20261005.json)；[修改点总览](SARC_6601修改点总览.md)。第三轮正文块及C01～C40/B01～B13保留，未重复恢复分片。

恢复FIR/IIR完整公式与嵌入低通说明、alpha范围、滑动/非滑动平均、时序图可辨标签、8行RAM地址切片与PIPELINE、5.18格式和5.19开篇。图5-23的图注由第34张右图跨到第35张左页，未误归到参数RAM图；原文非线性、s(16,0)/s(15,0)差异和原图省略号照录。

| 文档/资料 | 原图数 | 当前范围 |
|---|---:|---|
| SARC LRS | 13 | 首轮13张、3组缺口；正文未改 |
| SARC模块方案设计 | 40 | 首轮36张；U01～U15共15组局部缺口，另有来源连续性疑点S01；末4张未核对 |
| 辅助图 | 11 | 整图0/11；不跨版本补字 |
| 独立XBAR | 27 | 独立未处理，不计为SARC子文档 |

新增C41一条，LLD41＋LRS32＝73条来源位置；B14/B15另列，其他标记累计15条。U13为第34张两幅时序图细字，U14为第35张极细时标，U15为第36张数据常量。S01记录61–62→65–66的界面屏幕号跳号，63–64未定位；尚不能仅由界面数字断言内容缺页。

**下一张为第37张GameViewer_cTDH1vvDLo.png，接5.19 FIFO后续，再至5.20中断开篇。** 本批实际写回和逐字节回读以`SARC_LLD_ROUND4_REMOTE_SAVE_20261005.json`为准。末4张完成后核对11张辅助图，再用确认同源同版资料定点回查；EFC5组和LRS3组保持，不假关闭。

## 第二轮方案设计记录（历史保留）

以下为上一轮范围与状态；旧“下一张”等不再是当前断点，以本文开头为准。

# 第二轮：SARC原图提取与验收报告

更新：2026-10-05，第二轮。工作分支：`docs/restore-6601-screenshots`。

## 当前结论与接续

**LRS13张首轮成果保持不变；方案设计本轮新增前14/40张首轮核对，范围从封面至5.3校正状态机。SARC相关64张中已核对27张；全仓200张中累计87张，其余113张未首轮核对。** 这些数量不是正确率或最终验收率；封面预览不额外计数。

本批已恢复65个接口信号行、校准公式/单端和差分各9步流程、图5-5交互及图5-6四状态五条件；补回差分接口和adc_pwdn等删除线，按原图修正页面顺序。被远程提示框实际挡住的文字没有猜补。

| 文档/资料 | 来源数 | 当前范围与状态 |
|---|---:|---|
| SARC LRS | 13 | 13张首轮已保存；原3组细字问题保留，本轮不改正文 |
| SARC模块方案设计（旧LLD目录） | 40 | 前14张首轮已保存；7组局部细字/遮挡待确认；后26张仍为历史待复核正文 |
| SARC辅助框图 | 11 | 未逐图核对；边界及能否补充清晰同源图仍需核实 |
| 独立XBAR文档（旧sarc_xbar目录） | 27 | 独立待处理，不计为SARC子文档 |

正文：[SARC模块方案设计](sarc_lld/docs/SARC_LLD设计文档.md)。[本批详细记录](../reviews/SARC_LLD_ROUND2_REVIEW_20261005.md)列出14张来源、实质修订、7组问题及原文差异；[逐图台账](../reviews/SARC_LLD_ROUND2_IMAGE_LEDGER_20261005.json)明确每张状态。

修改索引累计LRS32＋本轮LLD15＝47条出现位置，LLD C11含遮挡、原句不完整；15和47都不是独立功能数。无明确6601归属的红字、黑色删除线及历史条目另列；不能把它们都当成新增功能。

**下一张：第15张GameViewer_CCQu4ftpmA.png，5.4外部触发源及5.5单次触发模式；随后接GameViewer_NaOtfAzWwn.png。** EFC保持暂缓状态，LRS不从头重做；后26张候选顺序仍需看图确认。

## 第一轮LRS复核记录（历史保留）

以下保留第一轮实际工作、逐图记录及3组缺口；其中“下一批”等为历史状态，当前断点以上节为准。

# 第一轮：SARC LRS原图提取与验收报告

日期：2026-10-05。分支：`docs/restore-6601-screenshots`。本批依据本仓库SARC原始截图；不使用ET60157/ET6801手册或程序替代原图。

## 1. 本批结果

**LRS的13张原始PNG完成首轮逐图核对并重新转录。** 48条功能需求、5条中断需求、1条事件需求、8条约束及2条触发源需求按原文顺序完整列出；其中3组图内细字仍未达到逐字符确认，不能宣称全文100%准确或最终验收通过。

正文保持一份文档：[ET6601 SARC模块LRS设计文档](sarc_lrs/docs/SARC_LRS设计文档.md)。[6601修改点总览](SARC_6601修改点总览.md)索引32条原图出现位置，不等于32项独立功能修改。方案设计和辅助图的修改点尚未全量提取。

## 2. 先修正文档边界

当前`sarc/`目录共91张原始截图、93807289字节。这是目录清点，不是91张都属于同一份SARC文档。

| 现有目录 | 原图数 | 按原图核实的文档边界 | 本批处理 |
|---|---:|---|---|
| sarc_lrs | 13 | 封面为《ET6601 SARC模块LRS设计文档》 | 13张首轮核对；正文一份；3组图内细字待复核 |
| sarc_lld | 40 | 封面为《SARC模块方案设计》；不是从文件名推断标题 | 只核实封面边界，不算40张首轮核对完成；下一批 |
| sarc_diagrams | 11 | 图形来源资料，包含处理流程/滤波图；当前截图未确认统一封面和原始文件边界 | 仅清点并预览用于定位，不把11张宣称已逐字核对或独立正式文档已验收 |
| sarc_xbar | 27 | 封面明确《ET6601 XBAR模块需求规格与设计方案》；是独立XBAR文档，不是“SARC XBAR总线互联文档” | 留在旧目录避免断链，另列待处理；不混入SARC正文和修改点 |

封面依据：[SARC LRS](sarc_lrs/images/GameViewer_1h9LEjdFpy.png)、[SARC方案设计](sarc_lld/images/GameViewer_be9VqBBdbM.png)、[独立XBAR文档](sarc_xbar/images/GameViewer_yUpAyoEWMN.png)。本轮没有迁移原图、改动SARC LLD/XBAR原文或重新合并CPLD。

SARC相关来源暂按LRS13＋方案设计40＋辅助图11＝64张管理；另27张为独立XBAR来源。待辅助图边界核实后更新地图，不按旧分组自动新建原始文档。全仓原图仍200张，本批首轮核对累计73张（此前EFC60＋本批LRS13），不是验收率或正确率。封面边界检查和预览图不另增完成数。

## 3. 本轮实质修订

| 原问题 | 本轮处理 |
|---|---|
| 旧稿按文件名字母排列，模块介绍被放到第12组，触发表穿插正文 | 按修订表/目录→模块介绍→FUNC01～48→中断/事件/约束→触发表恢复完整顺序；原图不改名 |
| 水印、账户名、时间和播放器噪声大量进入正文 | 逐图辨别后清除非文档文字，不对正文技术词做批量推断替换 |
| 旧稿最高时钟频率漏值 | 原图FUNC03中的66.6M补回 |
| 删除线丢失造成错误要求 | 恢复Power-gating删除线、历史修订2/5项删除线；加法器36替代删除线27，不再写成3627bit |
| 触发表拆散、漏CMPC/STM信号及ETIM事件 | sample表恢复12行，CMPC从10到0共22项信号、STM6项均列出；Blanking独立3行；补全EVT01的ETIM整条 |
| 内嵌两张表只剩少量文字 | 两张16列数据对齐表及上下文英语逐项转录，保留Table 3/Table 4原名；没有访问外部文献补内容 |
| 把蓝色当作普通说明可能漏6601修改 | 依据原文颜色声明整理32条来源记录；目录超链接和历史引用图配色不机械算新增 |
| 复位数量、位域重叠、拼写被误当OCR噪声 | 3/2内核、SARC0/1/2表头、107重叠、tm5、模拟测/数字测、end_p/enc_p均分别保留；差异不靠技术常识统一 |

## 4. LRS逐图记录

下表为本次核实的阅读顺序。状态统一为“首轮原图核对，非最终验收”；具体原始字节数/哈希见[来源清单](../reviews/SARC_ROUND1_IMAGE_LEDGER_20261005.json)。

| 顺序 | 原始PNG | 本批核对范围 |
|---:|---|---|
| 01 | [GameViewer_1h9LEjdFpy.png](sarc_lrs/images/GameViewer_1h9LEjdFpy.png) | 封面：ET6601 SARC模块LRS设计文档；设计、评审、批准栏。 |
| 02 | [GameViewer_aAOwVv2FCQ.png](sarc_lrs/images/GameViewer_aAOwVv2FCQ.png) | 修订表6条非空记录、11个空白续行；历史删除线；v1.0与2026/10/1修改及颜色说明；目录前半。 |
| 03 | [GameViewer_abFYmuKlpf.png](sarc_lrs/images/GameViewer_abFYmuKlpf.png) | 目录2.1～2.5；图目录原文“未找到图形项目表”；表目录表1-1。 |
| 04 | [GameViewer_WtOrHaAqvH.png](sarc_lrs/images/GameViewer_WtOrHaAqvH.png) | 模块简介、结构图可辨标签、FUNC01～07首段；3/2内核差异和Power-gating删除线；U01。 |
| 05 | [GameViewer_nGNAOmfeWa.png](sarc_lrs/images/GameViewer_nGNAOmfeWa.png) | FUNC07续句、08～14，p0抢占及Trigger-to-sample时机。 |
| 06 | [GameViewer_Kd7bk57Vx3.png](sarc_lrs/images/GameViewer_Kd7bk57Vx3.png) | FUNC15～22；软件触发、Blanking图、偏置/增益与超门限。 |
| 07 | [GameViewer_CeKX8gRMOe.png](sarc_lrs/images/GameViewer_CeKX8gRMOe.png) | 阈值逻辑/波形可辨标签、FUNC23～26，跨页FIR续句和8\*20bit结果。 |
| 08 | [GameViewer_hTRpPSKxgI.png](sarc_lrs/images/GameViewer_hTRpPSKxgI.png) | FUNC27～34，数据流图、DMA与状态；U02图内细字。 |
| 09 | [GameViewer_TxOL7pU1gm.png](sarc_lrs/images/GameViewer_TxOL7pU1gm.png) | FUNC34续句、35～44；FIFO配置约束与重复结构图，U01重复位置。 |
| 10 | [GameViewer_PJZbqwPIEg.png](sarc_lrs/images/GameViewer_PJZbqwPIEg.png) | FUNC44第1）～5）及两张16列嵌入表；36/27删除线；45～47e。 |
| 11 | [GameViewer_eyXbfnO5PJ.png](sarc_lrs/images/GameViewer_eyXbfnO5PJ.png) | FUNC47f/g、48；INTR01～05及EOC波形，U03的vc下标。 |
| 12 | [GameViewer_XDCKpTnaH0.png](sarc_lrs/images/GameViewer_XDCKpTnaH0.png) | EVT01、LIMIT01～08、TRIG01的前3行；ETIM事件整条补回。 |
| 13 | [GameViewer_Dt52xixULd.png](sarc_lrs/images/GameViewer_Dt52xixULd.png) | TRIG01剩余9行与TRIG02的3行；CMPC22项、STM6项；表中重叠位域和tm5照录；文档末尾。 |

## 5. 未解决项及后续入口

| 编号 | 原图位置 | 仍不能逐字符确认的内容 |
|---|---|---|
| SARC-LRS-U01 | WtOrHaAqvH左页结构图及TxOL7pU1gm右页重复图 | 控制器右侧长箭头的完整文字及少量节点细字 |
| SARC-LRS-U02 | hTRpPSKxgI左页数据处理图 | 系数完整名、部分位宽/定标、signed说明及小框名称 |
| SARC-LRS-U03 | eyXbfnO5PJ右页EOC时序图 | 脉冲内vc完整下标；其余波形标签和批注已转录 |

3组不是3个字，也不是未处理整页。原图及可辨片段均保留；辅助图有相关数据流程图但尚未核实每一项是否与LRS插图相同，不能跨图猜填。后续只对这些局部使用同源更清晰来源核对，不反复从LRS封面重做。

**下一批转到`sarc_lld/docs/SARC_LLD设计文档.md`。** 从封面`GameViewer_be9VqBBdbM.png`及修订表`GameViewer_aPDFQVxWhA.png`确认顺序后，按原始章节处理40张图，不按文件名遍历；封面已看过不等于正文已核对。完成方案设计后处理11张辅助图，再回查LRS图内疑点。XBAR27张独立管理，不能自动混入SARC修改点。

EFC两份正文、总览、验收报告及5组缺口均保持本轮开始时状态；用户暂缓EFC不等于这5组已解决。

## 6. 校验与验收边界

源包固定提交`d80a74e83e4bf942905844e61efd5d169e37c815`，只新增私有只读导出工作流。原始SARC目录91张PNG与初始源提交的Git blob一致。本批校验源包127个文件的Git blob、SHA-256和字节数；原图链接、13个来源锚点、需求编号完整连续性、表格行列、删除线及32条修改位置索引均检查。

本次为LRS首轮逐图核对和文档边界检查，不声称独立第二遍全文验收。机器检查、远端保存回执及工作流成功只能证明各自范围，不能证明字符准确率或硬件通过。EFC原文件未改动；未核对的LLD、辅助图及XBAR正文也未改动。
