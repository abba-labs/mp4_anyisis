# SARC待补原始资料清单

2026-10-05，第十二轮。**23组局部缺口＋S01仍开放；AUX-U02已核实关闭。** 原24组均已定点回查，不是还有24组没看过，也不是23张整图未处理。已有64张首轮覆盖不证明来源完整或逐字验收。

## 优先取得的资料

同版《SARC模块方案设计》（截图Word窗口名为“SARC模块设计方案”）及其内嵌图表、同版《ET6601 SARC模块LRS设计文档》、截图所指抢占控制.xlsx、qNBg辅助图红字清晰局部。可提供保留批注和变更标记的原Word/原绘图文件或原比例清晰截屏；版本需先核对，不能用其它芯片手册替代。

## 尚未关闭的23组

表内文件简称均指`GameViewer_<简称>.png`；LLD原图在`sarc_lld/images/`，LRS在`sarc_lrs/images/`，AUX在`sarc_diagrams/images/`。每行链接到实际原图，不按表序冒充原文页序。

| 编号 | 原图／区域 | 尚待确认及已缩小部分 | 需要的同版来源 |
|---|---|---|---|
| LLD-U01 | [v6tUVs7H0k](sarc_lld/images/GameViewer_v6tUVs7H0k.png)；右页表1 | DR_SARADC_003/006/011细字、012删除字等；002“采样校准”已补 | 同版OR_DR内嵌表或原Word |
| LLD-U02 | [LWEUsHJgSN](sarc_lld/images/GameViewer_LWEUsHJgSN.png)；图1 CTRL右侧 | 长箭头完整语句及小节点细字；SH与分区标题已补 | 同版结构图原件 |
| LLD-U03 | [BMYV2LGXFN](sarc_lld/images/GameViewer_BMYV2LGXFN.png)；图4-1 | spltime_en两行批注、细刻度/长度 | 同版时序图原件 |
| LLD-U04 | [Wwj0z78cha](sarc_lld/images/GameViewer_Wwj0z78cha.png)；图5-2 | 连线/配置名、下标、小字与右上遮挡 | 同版无遮挡图5-2 |
| LLD-U05 | [bG98ufwLis](sarc_lld/images/GameViewer_bG98ufwLis.png)；右页首行 | “当前正在转”之后被弹窗遮挡；C11不完整 | 同一页无遮挡来源 |
| LLD-U06 | [3VjshoX5So](sarc_lld/images/GameViewer_3VjshoX5So.png)；图5-3 | A等式、末列注、系数/细位宽等；B=A、C移位已补 | 同版数据流图 |
| LLD-U07 | [UUhaiE4moy](sarc_lld/images/GameViewer_UUhaiE4moy.png)；图5-4 | 控制输入、数字小框、细位宽/下标 | 同版校准流程原图 |
| LLD-U08 | [ba6sdetThH](sarc_lld/images/GameViewer_ba6sdetThH.png)；图5-17 | spltime_en两行注及细数值；sample/conversion已补 | 同版时序图 |
| LLD-U09 | [LoWatHzLVG](sarc_lld/images/GameViewer_LoWatHzLVG.png)；三处嵌入时序表 | 行名、细字、周期列与色块起止 | 截图所指同版抢占控制.xlsx |
| LLD-U10 | [mjeYzTB3j7](sarc_lld/images/GameViewer_mjeYzTB3j7.png)；图5-19校准 | 5bit偏置范围前导符号仍不清；signed两行与0~4已补 | 该5bit版本清晰原图，不用15bit替代 |
| LLD-U11 | [PecSuT1xBB](sarc_lld/images/GameViewer_PecSuT1xBB.png)；缓存图 | 清除布尔式与选择条件；j-1/j+1数组已补 | 同版缓存图原件 |
| LLD-U12 | [SeEx4da40l](sarc_lld/images/GameViewer_SeEx4da40l.png)；计数控制上部 | 复合条件和输出全名；p_arg与p_arg+q_arg已补 | 同版运算数据流图 |
| LLD-U13 | [ZwgMgCyaeL](sarc_lld/images/GameViewer_ZwgMgCyaeL.png)；左右实现时序 | 中文批注、来源标签、信号大小写、counter/红条件；末行位串已补 | 同版完整时序图 |
| LLD-U14 | [e8XPWSdAMt](sarc_lld/images/GameViewer_e8XPWSdAMt.png)；左下RAM时序 | clk上方整串细时间轴刻度 | 同版时序图高分辨率原件 |
| LLD-U15 | [1EC7JuTBH6](sarc_lld/images/GameViewer_1EC7JuTBH6.png)；图5-24上部 | 三组红常量仅保留16'dx/16'dy/16'dz候选 | 同版结果寄存器时序图 |
| LLD-U16 | [cTDH1vvDLo](sarc_lld/images/GameViewer_cTDH1vvDLo.png)；右下EOC | vc和delay完整细下标 | 同版EOC图 |
| LLD-U17 | [m4qMLaqKqw](sarc_lld/images/GameViewer_m4qMLaqKqw.png)；左中EOC输入 | VC行完整信号名及细沿对齐 | 同版EOC输入时序图 |
| LLD-U18 | [u5JeUrg4ga](sarc_lld/images/GameViewer_u5JeUrg4ga.png)；中断图最右侧 | “中断输出”后完整标识/分隔符；force_ind、寄存器读、intr已补 | 同版中断处理图 |
| LLD-U19 | [YbkCdqx6qz](sarc_lld/images/GameViewer_YbkCdqx6qz.png)；CPU_WRAP图 | 时钟图例、蓝色配置/寄存器及划线范围、部分下标；C46不完整 | 同版CPU_WRAP交互图 |
| LRS-U01 | [WtOrHaAqvH](sarc_lrs/images/GameViewer_WtOrHaAqvH.png) / [TxOL7pU1gm](sarc_lrs/images/GameViewer_TxOL7pU1gm.png)；结构图两处 | CTRL长箭头和小标签；两图SH已按字形修正 | 同版LRS结构图 |
| LRS-U02 | [hTRpPSKxgI](sarc_lrs/images/GameViewer_hTRpPSKxgI.png)；FUNC27数据流 | 系数、定标、signed说明和小方框字 | 同版LRS数据流原件 |
| LRS-U03 | [eyXbfnO5PJ](sarc_lrs/images/GameViewer_eyXbfnO5PJ.png)；右上EOC | vc完整下标 | 同版LRS EOC图 |
| AUX-U01 | [qNBgXqkj5C](sarc_diagrams/images/GameViewer_qNBgXqkj5C.png)；IIR系数上方红字 | “约定…>0”的中间限定字；要/需仅为候选 | 该张清晰局部或原绘图文件 |

## S01：来源连续性另列，不计入23组字形缺口

[第32张iSOJmCn28m](sarc_lld/images/GameViewer_iSOJmCn28m.png)界面为61–62，右页IIR说明结束于0≤alpha≤1；[第33张HFc4FYW2ed](sarc_lld/images/GameViewer_HFc4FYW2ed.png)界面为65–66，左页从“滑动平均”起。第十二轮再次逐图查看，未取得63–64对应来源。需要同版5.17这一段的连续原文/连续截图来确认关系。界面屏幕号不等于正文页码；不宣称已证实漏两页、不造缺页正文、不把无页码辅助图插作这两页。

## 已核实关闭的局部

**SARC-AUX-U02**：[Wb2pLAEGMa](sarc_diagrams/images/GameViewer_Wb2pLAEGMa.png)下行中间s(16,15)下方原句为“同时作为滤波乘法器输入yBUF”。第十二轮按原PNG局部字形确认并补入辅助正文。本项关闭不意味着辅助整组来源同版或SARC最终验收。

## 补齐与验收入口

同版确认→只核该图/区域→补同一完整Markdown→同步修改位置和缺口状态→正式提交并回读。C11/U05的弹窗遮挡需要无遮挡来源；C46/U19的蓝色标记需保留颜色/删除线，不能仅交没有标记的纯文本。64张首轮、78条来源位置、保存哈希均不是独立功能数或准确率。

当前Project文件索引及已连接Drive按源文件名检索未取得相应同版原件，仅表示本次未检索到。没有新来源时保持具体缺口，不反复同图放大，不自动合并异版图。第八～十二轮详细记录与保存回执在`../reviews/`，它们不替代上表的原始来源。
