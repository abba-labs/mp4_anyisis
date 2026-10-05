# SARC方案设计第五轮原图核对记录

日期2026-10-05，唯一分支`docs/restore-6601-screenshots`。输入HEAD`d75fc901b5914d165f1a797e49a60fa6a81b4e0c`；输入正文blob`33bed8b0c1348ba02e616557fbbd3785661ed393`。第四轮已发布回读后才继续本批。

## 本批实质正文工作

第37～40张4张，累计40/40至文末；真实相邻关系`cTDH1vvDLo → m4qMLaqKqw → u5JeUrg4ga → YbkCdqx6qz`。每张先左后右，界面显示73–74、75–76、77–78、79。界面号只辅助来源定位，不转录为原文页码。

| 顺序 | 原图 | 正文内容 |
|---:|---|---|
| 37 | GameViewer_cTDH1vvDLo.png | FIFO映射、两个注意项、全部bitmap/data可辨格；5.20 EOC三个位置及16bit SYSCLK延时冲突；批注enc_p照录 |
| 38 | GameViewer_m4qMLaqKqw.png | EOC输入关系及两时序；6002清单标题/说明/四项全删除线；6601 1+4路及4套源清单开篇 |
| 39 | GameViewer_u5JeUrg4ga.png | 跨页浅蓝8bit求和中断源；中断处理图；DMA_MUX/4通道/FIFO/6801历史说明；CPU_WRAP蓝字开篇 |
| 40 | GameViewer_YbkCdqx6qz.png | adcreg_receive/200M跨页蓝字、CPU_WRAP图可辨标记；6.约束、7.遗留问题、8.参考文献，作者空白保留 |

正文仍是`../sarc/sarc_lld/docs/SARC_LLD设计文档.md`一份。前36个原图正文块逐字节保留；LRS、EFC、XBAR、辅助正文及原始PNG未改。未OCR、未用其它芯片/代码/常识补图。

## 来源位置、缺口及差异

C42～C46新增5条：6601中断1+4及删除项、跨页4套可选源、DMA浅蓝求和源、CPU_WRAP跨页两组/200M、CPU_WRAP图修改标记。LLD46＋LRS32＝78条位置归集记录，不是独立功能数；C43/C45各保留两张出处，C46未辨部分挂U19。B16～B19分别为6002 EOC、被删6002中断清单、6002 DMA标题及6801 DMA历史段，其他标记累计19条。

U16：第37张右下EOC图vc/delay细下标；U17：第38张左中VC行全名及细沿；U18：第39张中断图测试字段/读出文字/输出两标识；U19：第40张CPU_WRAP图时钟/配置输入/寄存器/位宽与浅蓝标线范围。可辨片段、候选和来源区域在正文内逐一登记。U01～U15、LRS3组、EFC5组与S01全部保留，未假关闭。

原文“两个”EOC位置却列三个选项、三个不同图均编号5-20、enc_p/end_p、sarc0.sarc_result与sarc1.adc_result、DMA清单16*2等分别照录。不能把1+4路中断照技术推理改写，也不能把CPU_WRAP正文200M反向填入模糊图字。

## 保存检查及准确下一入口

全仓113/200首轮，SARC53/64；方案19组局部缺口与S01并列，未最终验收。本批8目标文件采用当前blob约束的限定补丁，所有旧blob和全部输出字节哈希通过后才写入；只推送本分支、不force。实际内容提交、远端下载逐字节比较见ROUND5_REMOTE_SAVE，暂存不算正式发布。

下一入口`6601芯片截图/sarc/sarc_diagrams/images/GameViewer_323Uh2DKeH.png`；先确认辅助资料边界并做整图，不把旧四张局部核对计为整图。辅助11张仍0/11。原S01未闭合，不能将40/40首轮视为来源完整性保证。
