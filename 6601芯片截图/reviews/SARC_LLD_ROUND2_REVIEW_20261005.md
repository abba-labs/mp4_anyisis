# SARC方案设计第二轮原图复核记录

日期：2026-10-05。分支：`docs/restore-6601-screenshots`。

## 1. 本批范围

本批完成方案设计前14/40张原始PNG首轮逐图核对，范围从封面至5.3校正状态机。两张接口截图完整复核共65个信号行；后26张只保留历史正文，尚未进行本轮逐图核对。LRS13张和EFC两份正文不改动。

原始封面是《SARC模块方案设计》，最终仍一份Markdown存放在旧`sarc_lld/docs/SARC_LLD设计文档.md`，不是把原文改写成另一种设计文档。

## 2. 实质修订

| 问题 | 本轮处理 |
|---|---|
| 旧稿按文件名字母顺序，封面在第8组、接口在第39/37组 | 以原图目录、章节和续表确定前14张顺序，正文开篇恢复；其余26张仅候选衔接，不宣称已验收顺序 |
| 差分校正表第1步和续页分开 | 顺序核实为UUhaiE4moy→QZWwXnmnv1→O2LOSI5xZO；完成9个步骤及前后注释，不把流程图插到续表中间 |
| 接口信号漏行/字符混乱 | 65个信号行逐项核对；补clk_adc、sarc_d2a_adc_spltime_en、sarc_wdt_dma_src_is_dly等；HBURST方向空白照留 |
| 删除线丢失 | 恢复差分mux及refp/refn注入共3行、adc_pwdn=0，以及第三ADC路径的原图删除线；未划去的差分描述不删除 |
| 图5-1/5-2新增和删除节点混同 | 按原文浅蓝/清绿规则定位求和/过采节点及第三组被删路径，不能从残留框图推断仍有3个ADC |
| 校准公式及控制图只剩碎片 | 恢复两处16次求和除16、gain和offset公式，单端/差分各9步、5步软件流程、图5-5交互和图5-6四状态五条件 |
| UI提示混入正文 | 去掉已核对页的账号/时间/播放器/弹窗文字；实际被弹窗挡住的抢占句登记U05，不依据后文猜写 |
| 颜色或历史标题导致假修改 | 15条明确标记/6601文字的位置归集；C11含遮挡。红字/黑色删除线/历史ET6801条目另列B01～B07，不冒充明确6601新增 |

## 3. 逐图记录

| 页序 | 原图 | 核对范围 |
|---:|---|---|
| 01 | [GameViewer_be9VqBBdbM.png](../sarc/sarc_lld/images/GameViewer_be9VqBBdbM.png) | 封面及署名；真实标题SARC模块方案设计 |
| 02 | [GameViewer_aPDFQVxWhA.png](../sarc/sarc_lld/images/GameViewer_aPDFQVxWhA.png) | 修订表3条非空记录、14空白行、明确颜色规则；历史ET6801记录不冒充6601 |
| 03 | [GameViewer_3ZWo3TthG6.png](../sarc/sarc_lld/images/GameViewer_3ZWo3TthG6.png) | 目录前两页、原重复5.1编号保留 |
| 04 | [GameViewer_v6tUVs7H0k.png](../sarc/sarc_lld/images/GameViewer_v6tUVs7H0k.png) | 目录末页、OR_DR说明及18行内嵌表可辨内容；U01 |
| 05 | [GameViewer_LWEUsHJgSN.png](../sarc/sarc_lld/images/GameViewer_LWEUsHJgSN.png) | 概述、9项功能、图1标签和求和标记；U02 |
| 06 | [GameViewer_ZQLidR9zmC.png](../sarc/sarc_lld/images/GameViewer_ZQLidR9zmC.png) | 4.1接口前半，32信号行；恢复clk_adc、spltime_en及删除线、outrd_hold |
| 07 | [GameViewer_XEDw3yfNAf.png](../sarc/sarc_lld/images/GameViewer_XEDw3yfNAf.png) | 4.1接口后半，33信号行；DMA源打拍、ATE/中断/TESTPIN/CPU等完整行 |
| 08 | [GameViewer_BMYV2LGXFN.png](../sarc/sarc_lld/images/GameViewer_BMYV2LGXFN.png) | 4.2采样时长、图4-1可辨文字、右页5条说明；U03 |
| 09 | [GameViewer_Wwj0z78cha.png](../sarc/sarc_lld/images/GameViewer_Wwj0z78cha.png) | 5.1连接关系和结构图；第三ADC删除及求和/过采节点；U04 |
| 10 | [GameViewer_bG98ufwLis.png](../sarc/sarc_lld/images/GameViewer_bG98ufwLis.png) | 模块说明跨页续接、ovs_ctrl/queue_manage/flag及sum；U05提示框遮挡 |
| 11 | [GameViewer_3VjshoX5So.png](../sarc/sarc_lld/images/GameViewer_3VjshoX5So.png) | blanking说明、图5-3数据路径、4组格式及时钟；U06 |
| 12 | [GameViewer_UUhaiE4moy.png](../sarc/sarc_lld/images/GameViewer_UUhaiE4moy.png) | ADCCLK、图5-4、4个校正公式、单端9步和差分第1步；U07 |
| 13 | [GameViewer_QZWwXnmnv1.png](../sarc/sarc_lld/images/GameViewer_QZWwXnmnv1.png) | 差分第2～9步、两阶段补偿与4条数字要求、校准软件5步；adc_pwdn删除线 |
| 14 | [GameViewer_O2LOSI5xZO.png](../sarc/sarc_lld/images/GameViewer_O2LOSI5xZO.png) | 图5-5全部可辨交互、图5-6四状态五条件、作者DAC待补说明 |

## 4. 未解决来源位置

| 编号 | 原图位置 | 缺口 |
|---|---|---|
| SARC-LLD-U01 | v6tUVs7H0k，右页表1 | 18行OR_DR内嵌表中的若干细字/红字/删除内容；不是没有处理整张表 |
| SARC-LLD-U02 | LWEUsHJgSN，图1 | 控制器右侧长箭头及少量节点细字 |
| SARC-LLD-U03 | BMYV2LGXFN，图4-1 | spltime_en上方注释和部分波形长度小字 |
| SARC-LLD-U04 | Wwj0z78cha，图5-2 | 信号全名、配置/下标、左侧小字及提示框覆盖局部 |
| SARC-LLD-U05 | bG98ufwLis，右页首行 | queue_manage抢占说明中段被弹窗覆盖；C11只录可见前后文字 |
| SARC-LLD-U06 | 3VjshoX5So，图5-3 | 系数、signed等式、定标/位宽与小框名 |
| SARC-LLD-U07 | UUhaiE4moy，图5-4 | 控制输入、数字处理框和位宽下标 |

7组仅指已核对前14张的缺口，不是整份LLD仅剩7组，更不是仅7个字。原PNG及裁切已查看；后续须同源清晰图，不能借其他芯片资料或代码常识填字。第4张表中【未辨】保留对应行，缺失的原文不能伪造为完整需求。

## 5. 原文差异（不是转录错误）

目录多处5.1重复且与正文不同；概述不支持差分，但校正章节保留差分流程；接口mux_se<4:0>而时序图[3:0]；sarc_a2d_outrd_hold方向为输出；hburst方向空白；单端第三步编号为1；SRAC拼写、“需要要待”/“当虚拟通道的启用”保留。图4-1的红/绿沿是采样时序标识，不当作版本差异。图5-6原作者“需要补充DAC校正需求和流程”照录，不代作者扩写。

## 6. 保存/检查边界和接续

来源127个导出文件原始字节重新校验；本批40张LLD均有唯一来源锚点，但只有前14张完成首轮视觉核对。检查了已核对区表格列数、65个接口信号行、公式/删除线、来源编号、原图链接和26个未核对正文块未改变。机器检查和保存校验不等于字符准确率100%。没有硬件测试。

下一张固定为第15张`GameViewer_CCQu4ftpmA.png`，先处理5.4外部触发源、图5-7与5.5单次触发模式，再接`GameViewer_NaOtfAzWwn.png`。后26张暂排顺序需要逐图验证，不从封面重做。LRS的3组图内疑点、EFC的5组遗留均不在本轮关闭；独立XBAR27张不混入SARC。
