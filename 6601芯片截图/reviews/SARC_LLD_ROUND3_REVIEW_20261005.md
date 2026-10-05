# SARC方案设计第三轮原图核对记录

日期：2026-10-05。分支：`docs/restore-6601-screenshots`。

## 1. 本批范围与保存边界

**本批新核对第15～31张，共17张原始PNG；方案设计累计31/40张完成首轮核对，至5.17滤波通道开篇。末9张保留原有转录，尚未本轮逐图核对。** 原始文档仍为一份[SARC模块方案设计](../sarc/sarc_lld/docs/SARC_LLD设计文档.md)。

输入head：`3d8da927cc13d4f8b6edd4d48001f2769f8365b7`；输入LLD blob：`064e09e52bfdb767785d2be156619fec1463628a`。本批输出106097字节、blob `dfe3dc2a6f70183888289d96c8768517be107c56`、SHA-256 `1190fc86ce592af28f4258511a8c0d530469eb9d59637d0ae8310ffc1b7578e6`。本记录形成于发布前，实际入库与完整字节回读以同目录`SARC_LLD_ROUND3_REMOTE_SAVE_20261005.json`为准，不用“本地已保存”冒充提交。

第一至十四张正文块逐字节保留；第三十二至四十张历史正文块也逐字节保留。只改变本批17张原图对应正文、汇总和状态信息；没有改动任何原PNG、EFC、LRS、XBAR或辅助图原有正文。

## 2. 本轮实质修订

| 范围 | 本批实际结果 |
|---|---|
| 触发和Blanking | 完整恢复外部128/64触发源原文、两行触发模式表、单次/连续触发、Blanking窗口与重复告警；图5-7～5-12可辨标签、三状态及转换条件 |
| 队列与软件触发 | 全部队列信号与p0模式指示、同步/冗余波形、软件set/硬件clear优先级和0x000F跨页示例；另一路SOFT_TRIGER原文拼写照留 |
| 采样和抢占 | 图5-15四状态、九条箭头含两条未标字箭头；采样时序及抢占控制原文；“包含blanking情况的冲突”删除线恢复，不能再当有效要求 |
| ready/flag及延时 | 交接区outrd_hold保证ready/data；start、ready与flag恢复三条；p0抢占后的DLYSTAMP重锁存及过采第一次锁存两段蓝字 |
| 校准与预处理 | 图5-19/5-20可辨位宽定标；6002相对6001的pre_gain历史变更单列，不冒充6601新增 |
| FIR/IIR与参数 | 恢复公式5-1～5-4、FIR/IIR结构全部可辨节点、四项参数配置与跨页影子更新；图中所有寄存器标签保留 |
| 缓存及运算数据流 | 输入增益4路拼接式、缓存3条正文、16bit*16bit跨页句、wrap/sat/溢出、输出缩放8路拼接；局部不清楚条件登记U11/U12 |
| 过采和通道 | 结构及全部11条蓝字（过采控制6条、求和2条、其它3条），保留36bit、resume/conti、告警/清除、shadow及中断/dma说明 |
| 超门限和主滤波开篇 | 6001→6002的CBC/ONESHOT历史对照、实时状态和事件输出、两幅检测图；5.17滤波输入及最高32阶原文 |
| 修改位置索引 | 新增C16～C40共25条，LLD累计40条；B08～B13共6条另列，其他标记累计13条。LRS32＋LLD40共72条是来源位置数，不是独立功能数 |

## 3. 页序纠正和逐图记录

上一轮后26张只有候选排序。本次核实后，正确的相邻关系为：

- `UFTfaW6Wm8 → Ef2CwLAmR0 → vZO2NlUXdv`：FIR说明→FIR/IIR结构→实现参数。
- `vZO2NlUXdv → PecSuT1xBB → SeEx4da40l`：输入增益/缓存→“乘法起的位宽为”→“16bit*16bit”与数据流。
- `pVe1evLu6f → NaDPGTeO6W`：5.15过采、5.16的6001说明→6002说明及5.17。原候选中的NaDPGTeO6W不能插到FIR与IIR之间。

下表“旧候选序号”是上一轮临时顺序，不是原文页码。阅读时每张先左后右。

| 当前序号 | 原始PNG | 旧候选序号 | 本批核对范围 |
|---:|---|---:|---|
| 15 | [GameViewer_CCQu4ftpmA.png](../sarc/sarc_lld/images/GameViewer_CCQu4ftpmA.png) | 15 | 5.4外部触发；图5-7；5.5单次触发完整正文/两行模式表 |
| 16 | [GameViewer_NaOtfAzWwn.png](../sarc/sarc_lld/images/GameViewer_NaOtfAzWwn.png) | 16 | 图5-8/5-9；连续触发和blanking开篇 |
| 17 | [GameViewer_a0rP8s7Oan.png](../sarc/sarc_lld/images/GameViewer_a0rP8s7Oan.png) | 17 | blanking告警与图5-10～5-12，三状态三有字转移 |
| 18 | [GameViewer_40i6eF4ZKV.png](../sarc/sarc_lld/images/GameViewer_40i6eF4ZKV.png) | 18 | 优先级队列全部输入输出，抢占模式蓝字和图5-13；5.8 |
| 19 | [GameViewer_NwJydpcqGX.png](../sarc/sarc_lld/images/GameViewer_NwJydpcqGX.png) | 19 | 同步/冗余两图全部可辨标签及正文 |
| 20 | [GameViewer_Pv1TFSu3Dw.png](../sarc/sarc_lld/images/GameViewer_Pv1TFSu3Dw.png) | 20 | 软件强制置位完整说明/跨页示例；另一软件触发蓝字；5.10 |
| 21 | [GameViewer_sKXvcDs2Yn.png](../sarc/sarc_lld/images/GameViewer_sKXvcDs2Yn.png) | 21 | 图5-15四状态及九条箭头；图5-16时序标签 |
| 22 | [GameViewer_ba6sdetThH.png](../sarc/sarc_lld/images/GameViewer_ba6sdetThH.png) | 22 | 图5-17/5-18可辨时序；U08 |
| 23 | [GameViewer_LoWatHzLVG.png](../sarc/sarc_lld/images/GameViewer_LoWatHzLVG.png) | 23 | 1.1.1抢占；blanking冲突删除线；ready/flag恢复；U09 |
| 24 | [GameViewer_mjeYzTB3j7.png](../sarc/sarc_lld/images/GameViewer_mjeYzTB3j7.png) | 24 | 5.11延时捕获新增两段；5.12及校准图；U10 |
| 25 | [GameViewer_UFTfaW6Wm8.png](../sarc/sarc_lld/images/GameViewer_UFTfaW6Wm8.png) | 25 | 5.13预处理补偿；5.14/FIR公式5-1/5-2 |
| 26 | [GameViewer_Ef2CwLAmR0.png](../sarc/sarc_lld/images/GameViewer_Ef2CwLAmR0.png) | 27 | FIR/IIR结构及公式5-3/5-4；重复5.14.1照留 |
| 27 | [GameViewer_vZO2NlUXdv.png](../sarc/sarc_lld/images/GameViewer_vZO2NlUXdv.png) | 28 | 5.14.3参数四条完整原文、影子更新、全部寄存器标签 |
| 28 | [GameViewer_PecSuT1xBB.png](../sarc/sarc_lld/images/GameViewer_PecSuT1xBB.png) | 30 | 输入增益四路拼接；缓存三条；计算数据流开篇；U11 |
| 29 | [GameViewer_SeEx4da40l.png](../sarc/sarc_lld/images/GameViewer_SeEx4da40l.png) | 29 | 16bit*16bit续句、三条计算原文、8路缩放、sat/wrap；U12 |
| 30 | [GameViewer_pVe1evLu6f.png](../sarc/sarc_lld/images/GameViewer_pVe1evLu6f.png) | 31 | 5.15全部11条蓝字及结构；5.16/6001末句 |
| 31 | [GameViewer_NaDPGTeO6W.png](../sarc/sarc_lld/images/GameViewer_NaDPGTeO6W.png) | 26 | 承接6001→6002阈值输出；两张CBC/ONESHOT图；5.17与FIR图 |

## 4. 未解决项

原U01～U07未动；本批新增U08～U12。累计已核对区12组，不是12个字，也不是整份40张只有12组问题；余9张还未核对。

| 编号 | 原图位置 | 仍待逐字符确认的内容 |
|---|---|---|
| SARC-LLD-U08 | 第22张GameViewer_ba6sdetThH.png，图5-17 | spltime_en上方两处注释、部分时序小框名称和间隔小数值 |
| SARC-LLD-U09 | 第23张GameViewer_LoWatHzLVG.png，图5-18三处嵌入时序表 | 完整行名、细小注释、周期列数及波形色块起止；源表格链接未作为已取得文件 |
| SARC-LLD-U10 | 第24张GameViewer_mjeYzTB3j7.png，图5-19采样校准 | signed下方细字及顶部范围；辅助图offset为15bit而本页5bit，不互相覆盖 |
| SARC-LLD-U11 | 第28张GameViewer_PecSuT1xBB.png，输入数据和运算结果的缓存图 | 清除逻辑完整布尔式、MUX选择条件及细小数组下标 |
| SARC-LLD-U12 | 第29张GameViewer_SeEx4da40l.png，计算数据流图上部 | 计数器周围的复合条件、比较/选择标签和下标；中央/底部已用相同局部分图核对 |

局部可辨内容与原始PNG链接均保留。不能因原文需要更清晰源文件而猜补、删除行，或把局部登记当成完整验收。

## 5. 辅助图只作已核实的局部对照

| 辅助原图 | 本轮局部判断 | 使用边界 |
|---|---|---|
| 抢占功能.png | 与第23张主题相同，但其单一ready反馈和start与正文图的多回线/start-en不一致 | 不替换正文图、不补三个嵌入时序表的细字 |
| GameViewer_9akceoHcVF.png | 右下“滤波处理”局部节点/定标与第31张相符；左上校准offset为15bit，与第24张5bit不同 | 只核对一致滤波局部的标签；不覆盖校准版本，不关闭U10 |
| GameViewer_323Uh2DKeH.png | 中央乘加局部与第29张相符，“补两位符号位”、定标可辨 | 用相同局部辨字；辅助图外围额外红色解释不移植为正文 |
| GameViewer_T5Wi63Rflj.png | 输出移位拼接/sat-wrap局部与第29张相符 | 用相同局部核对8路拼接及选择信号；上部计数控制U12仍在 |

这四张仅做特定局部对应核查，**11张辅助图的完整首轮核对数仍为0**。不凭“画得相像”就把不同版本的图合并，也不借其他芯片资料填缺。

## 6. 原文差异照录

正文及图中的preemtive_md、priority_conflict、priority_cnflt、priority_conflt、priority_cflt，sarc_smaple_ctrl/sarc_sample_ctrl，SOFT_TRIGER/soft_trigger、cfg_pflt_p_num/cfg_pflt_num等按原处保留；不统一拼写。5.14.1两次、1.1.1抢占、多个5-18/5-19/5-20和5-x均为原文，未重编号。

本节27bit累加器与后文浅蓝“扩展36bit加法器”并存；图内补两位符号位不自动改成36bit。5.15标题“预处理过采和通道”及“乘法起”、参数配置中的“器器”“种”等可见原字照录。历史6001/6002说明与6601浅蓝内容区分。

## 7. 校验及下一入口

校验包括40张LLD原PNG的字节、Git blob和SHA-256，40个唯一原图锚点及顺序，前14与末9块未改，已核对区表格列数，C01～C40及B01～B13连续性、删除线、公式和原图链接。它们不是逐字符准确率证明。没有硬件运行，也未将文中时序需求/性能描述当实测结果。

**下一张第32张：`GameViewer_iSOJmCn28m.png`，接5.17滤波通道的后续图与FIR/IIR说明。** 之后核对33～40，再处理11张辅助图整图，最后定点回查已有疑点；不重做封面，不重新应用旧补丁，XBAR27张独立管理。

全仓首轮104/200（EFC60＋LRS13＋LLD31），剩余96张。SARC相关44/64首轮；这些数值均不是最终验收率。
