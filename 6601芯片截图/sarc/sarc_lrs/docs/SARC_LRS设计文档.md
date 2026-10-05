# ET6601 SARC 模块 LRS 设计文档

> 来源：本仓库 `sarc_lrs/images/` 的13张原始PNG，来源提交 `d80a74e83e4bf942905844e61efd5d169e37c815`；图片不缩放、不改写。按原文阅读顺序转录，不按文件名排序。
> 状态：13张完成本批首轮原图核对。正文、需求条目和表格已重新转录；3组图内局部小字仍待确认，见文末“转录复核记录”。首轮核对不是最终逐字符验收。
> 原图明确规定浅蓝色和清绿色相关区域为ET6601改动，包括线、背景和底纹；本文件第二部分按该规则记录，不沿用其他IP的颜色含义。普通目录超链接不作为修改标记。
> 删除线用 `~~删除内容~~` 保存。“转录注”“图中文字转录”和文末复核记录是整理者说明，不是原作者正文。原文自身差异、空项和特殊拼写照录，不根据其他芯片资料补齐。

## 第一部分：原始文档精准还原

<!-- source: GameViewer_1h9LEjdFpy.png -->
> 原图：[GameViewer_1h9LEjdFpy.png](../images/GameViewer_1h9LEjdFpy.png)。左页封面、右页批准栏。

ET6601 SARC 模块 LRS 设计文档

设计：郑汶  
评审：XXXXXXX  
批准：XXXXXXX

<!-- source: GameViewer_aAOwVv2FCQ.png -->
> 原图：[GameViewer_aAOwVv2FCQ.png](../images/GameViewer_aAOwVv2FCQ.png)。先左页修订表，再右页表尾、颜色说明和目录。

### 表1-1 修订记录

| 版本号 | 修订内容 | 修订日期 | 修订人员 |
|---|---|---|---|
|  |  | 20230919 | 牟崎瑞 |
|  | 1、在预处理通道之后新增8个预处理滤波器通道；<br>2、修改FUNC.SPEC【18】偏置校准处理的位宽，从s(5,0)变为s(15,2)； | 20240819 | 肖中平 |
|  | 合入6801的优化点。<br>1. Fix增益补偿的-2048问题。<br>~~2. 上报结果合并处理，2通道采样数据合并到一个寄存器中。~~<br>3. 采样结果输出到cpu时钟域下。<br>4. EOC中断触发位置增加。<br>~~5. Oneshot模式的再使能优化，~~ | <u>20250909</u> | 郑汶 |
|  | 增加需求：支持对模拟的放电时序控制； | 20251205 | 郑汶 |
| v1.0 | 6601在6801的基础上调整，文档中使用浅蓝色体现修改；<br>1. 增加抢占功能；<br>2. 增加用户预处理滤波过采求和功能；<br>3. 增加用户预处理的观测功能；<br>4. | 2026/09/22 | 郑汶 |
|  | 1. 增加触发到开始采样，抢占触发到开始采样的延迟指标需求 | 2026/10/1 | 郑汶 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

> 转录注：末11行为空白续行（左页8行、右页3行）；v1.0的“4.”后原图未填写文字，不补写。20250909属于原文历史修订，划去条目照留，不直接归为6601新增。

注：浅蓝色和清绿色相关区域为ET6601新加的改动，包括线，背景及底纹部分；

### 目录

Contents

目录  
图目录  
未找到图形项目表。  
表目录

第1章　模块介绍  
1.1　模块简介  
1.2　应用说明  
第2章　需求规格

<!-- source: GameViewer_abFYmuKlpf.png -->
> 原图：[GameViewer_abFYmuKlpf.png](../images/GameViewer_abFYmuKlpf.png)。左页接续目录；右页为图、表目录。

2.1　功能需求  
2.2　中断管理  
2.3　事件管理  
2.4　约束说明  
2.5　触发源说明

### 图目录

未找到图形项目表。

### 表目录

表1-1　修订记录

<!-- source: GameViewer_WtOrHaAqvH.png -->
> 原图：[GameViewer_WtOrHaAqvH.png](../images/GameViewer_WtOrHaAqvH.png)。左页模块介绍，右页开始需求条目。

### 第1章　模块介绍

#### 1.1 模块简介

SAR ADC主要用于采集片外电压、电流、温度、压力等信息，采样片内温度、电压、电流信息（可选），以及采样片内运放输出。

本文主要介绍内置SAR ADC数字控制器的设计规格。

> 图中文字转录（原图没有图号）：`Chan 0`、`Chan 1`、`……`、`Chan N`；`S/H`、`SARCORE`、`SARADC CALC`、`SARADC CTRL`、`CAL`；`ready`、`data`、`busy`、`done`、`trigger`；“采样通道选择”“触发信号管理”“模拟电路”“数字电路”。处理侧可辨标题为“预处理通道”“预处理滤波通道”“滤波通道”“缓存通道1”“缓存通道2”，输出为“to CPU/DMA”。
> 预处理通道框可辨 `PChan0`、`PChan1`、`PChan15`；预处理滤波及求和框可辨 `PFChan 0`、`PFChan 1`、`PFChan 7`、`SCh0`、`SCh1`、`SCh7`；滤波框可辨 `FChan0`、`FChan1`、`FChan7`；两组缓存框分别显示 `BChan 0`、`BChan 1`、`BChan 15`，求和结果框显示 `Sum0`、`Sum1`、`Sum7`，中间均有省略点。
> ⚠️ 原图待复核（SARC-LRS-U01）：控制器右侧长箭头上的完整细字和少量节点小字仍不能逐字符确认；同文FUNC.SPEC【44】处有重复结构图，已交叉查看但不据正文补造图中文字。完整结构、颜色和连线以原图为准。

#### 1.2 应用说明

> 转录注：原图此标题与第2章之间没有应用说明正文。

### 第2章　需求规格

#### 2.1 功能需求

**LRS.SARC.FUNC.SPEC【01】**　支持3个12位ADC内核，单个ADC最高采样率4.1Msps，每个ADC支持独立~~Power-gating~~Clock-gating以便节省功耗；

**LRS.SARC.FUNC.SPEC【02】**　每个ADC支持32个采样复用通道，支持单端输入（数字侧按32采样通道预留控制接口，模拟测按实际通道实现）；

**LRS.SARC.FUNC.SPEC【03】**　ADC工作时钟支持通过系统时钟进行1-8分频，最高时钟频率66.6M；

**LRS.SARC.FUNC.SPEC【04】**　支持2个独立的ADC数字控制器，SARC0~1，分别配置和管理2个ADC内核，支持通过AHB总线进行配置管理，支持软复位/模块使能/clock-gating；

**LRS.SARC.FUNC.SPEC【05】**　每个ADC支持校准算法实现（模拟提供校准方案，数字实现）；校准阶段上报校准寄存器结果：s(16,2)

**LRS.SARC.FUNC.SPEC【06】**　2个ADC可以工作在同步模式下（基于相同触发源选择）进行同步采样（同时采样不同信号）或者冗余采样（同时采样相同信号），2个ADC也可以工作在非同步模式下（基于不同触发源选择）；

**LRS.SARC.FUNC.SPEC【07】**　每个ADC控制器支持16个虚拟通道VC、16个预处理通道PC、8个预处理滤波通道PFC+8个求和通道SCh、8个滤波通道FC、2\*16个采样结果缓存通道BC、1\*8个求和结果寄存器，其中，预处理通道、缓存通道分别与虚拟通道一一对应，滤波通道和虚拟通道映射由软件配置；

<!-- source: GameViewer_nGNAOmfeWa.png -->
> 原图：[GameViewer_nGNAOmfeWa.png](../images/GameViewer_nGNAOmfeWa.png)。左页首段续接上一图FUNC.SPEC【07】，已在上方并成完整句；之后先左页08～11，再右页12～14。

**LRS.SARC.FUNC.SPEC【08】**　每个ADC控制器支持基于虚拟通道配置扩展采样时间（范围0-256个ADCCLK周期数）；

**LRS.SARC.FUNC.SPEC【09】**　每个ADC控制器支持基于虚拟通道定义：虚拟通道使能、采样优先级、S/H窗口、采样通道、触发源、触发方式，用户预处理通道等采样参数；

**LRS.SARC.FUNC.SPEC【10】**　每个ADC控制器支持4个优先级配置0~3（基于虚拟通道），配置数值越小，优先级越高；在同等优先级情况下，虚拟通道编号值越小，优先级越高；

**LRS.SARC.FUNC.SPEC【11】**　支持p0高优先级虚拟通道抢占低优先级虚拟通道抢占；

a) 低优先级虚拟通道在高优先级通道结束后，继续低优先级请求；  
b) 增加使能控制；  
c) 仅p0可抢占其它低优先级；  
d) p0内部不进行抢占；

**LRS.SARC.FUNC.SPEC【12】**　支持发生采样事件冲突时（多个虚拟通道同时被触发采样），可配置支持两种优先级处理：

- 低优先级采样事件被丢弃，只响应最高优先级采样事件；
- 所有被同时触发的采样事件按优先级进行排队处理，默认该模式；

**LRS.SARC.FUNC.SPEC【13】**　支持基于虚拟通道配置单次触发采样和连续触发采样模式：

- 单次触发采样：虚拟通道采样配置一次只响应一次触发采样（VC_EN打开一次只响应一次触发）
- 连续触发采样：虚拟通道采样配置一次可响应多次触发采样（VC_EN打开时可连续响应触发），默认该模式

模拟ADCCORE也存在单次模式/连续模式概念，但以上描述为数字测的单次触发采样、连续触发采样功能。模拟ADCCORE的固定为单次模式，即数字侧每发一个start，触发一次采样。

**LRS.SARC.FUNC.SPEC【14】**　每个ADC控制器支持基于虚拟通道进行Trigger-to-sample延迟计算，并上报延迟时间（SYSCLK周期计数），当sample被高优先级通道抢占后，原通道的Trigger-to-sample会在重新开始sample时更新延迟时间，过采样启用时在过采第一次开始sample上报，后续过采过程中不再上报；

<!-- source: GameViewer_Kd7bk57Vx3.png -->
> 原图：[GameViewer_Kd7bk57Vx3.png](../images/GameViewer_Kd7bk57Vx3.png)。左页15～19，右页为Blanking图与20～22。

**LRS.SARC.FUNC.SPEC【15】**　每个ADC控制器支持软件直接控制一个或多个虚拟通道开始采样（不通过采样触发信号）。

**LRS.SARC.FUNC.SPEC【16】**　支持软件输出采样触发，同其它硬件采样触发通路一致；

**LRS.SARC.FUNC.SPEC【17】**　每个ADC控制器中，虚拟通道0支持一个Blanking事件功能，该功能可屏蔽。支持blanking的延迟触发时间可配置，且对所有触发源统一配置，为16bit SYSCLK周期计数；

**LRS.SARC.FUNC.SPEC【18】**　每个ADC控制器Blanking管理模块，对所有blanking触发源的blanking窗口长度配置相同，为16bit SYSCLK周期计数器。

**LRS.SARC.FUNC.SPEC【19】**　blanking窗口内虚拟通道0的触发（专用周期触发源）可以正常响应，窗口内若出现其他虚拟通道触发信号（非专用周期触发），待blanking窗口结束后，按优先级处理。若Blanking窗口内，非专用周期触发出现重复触发，上报告警，并忽略该重复触发；

> 图中文字转录（原图无图号）：`Blanking trig`、`Blanking 延迟触发`、`Blanking 窗口`、`vc0触发源`、`其他vc触发源`，以及星形、○、□、△触发标记。
> 右侧原文：“blanking窗口结束后，根据优先级，响应○□△各一次。”“blanking窗口内○□△出现重复触发，产生告警。”
> 窗口位置和各触发标记的对应关系保留在原图中，不凭空重画。

**LRS.SARC.FUNC.SPEC【20】**　每个ADC控制器支持对采样结果进行数字域偏置和增益校准处理（模拟ADC s(15,2)和增益u(14,12)）；

**LRS.SARC.FUNC.SPEC【21】**　每个ADC控制器支持基于虚拟通道对校准后的采样结果进行用户偏置和增益处理（用户配置偏置s(16,2)和增益s(15,12)）；

**LRS.SARC.FUNC.SPEC【22】**　每个ADC控制器支持基于虚拟通道对用户偏置和增益处理后的采样结果进行上下电平超门限独立检测，可配置选择CBC和ONESHOT两种方式产生相应的超门限事件，可上报中断（上下门限独立作为中断源）、DMA请求（mux-or后的事件信号）和输出事件；超上下门限的告警实时状态通过状态寄存器上报，告警历史状态上报通过中断模块中的status寄存器上报；

<!-- source: GameViewer_CeKX8gRMOe.png -->
> 原图：[GameViewer_CeKX8gRMOe.png](../images/GameViewer_CeKX8gRMOe.png)。左页延续上下门限图和23～24；24续句位于右页顶部。

> 图中文字转录（原图无图号）：`limit.hi`、`adc_result`、`limit.lo`、`clear.hi`、`clear.lo`、`CBC clear logic`、`pulse`、`set`、`clear`、`adcevtsts.triphi`、`adcevtsts.triplo`、`evtsel.hi`、`evtsel.lo`、`EVT`；比较器“+”“-”及或门符号见原图。
> 时序标签：`sample1 超门限`、`sample2 超门限`、`sample3 不超门限`、`sample4 超门限`；`CBC`、`ONESHOT`、`sw clear`、`soft clear`。清零位置与波形保持原图，不把示意图当成实测波形。

超门限事件优先级高于soft clear事件；

**LRS.SARC.FUNC.SPEC【23】**　每个ADC控制器支持16个虚拟通道的超门限检测事件进行mux选择后输出4bit告警信号，每bit告警信号支持独立从16个虚拟通道的超门限检测事件中配置选择；并且每个ADC控制器独立输出2组4bit告警信号，一组到XBAR，另一组到ETIM；

**LRS.SARC.FUNC.SPEC【24】**　每个ADC控制器支持8个滤波通道，基于虚拟通道配置选择对应的滤波通道，滤波器输入为ADC校准后采样结果，每个通道支持滤波类型：FIR（阶数可任意配置，且根据配置阶数实时输出滤波结果，最大32阶）、IIR（1阶）、滑动平均（归入FIR）和非滑动平均，通过配置选择；

**LRS.SARC.FUNC.SPEC【25】**　每个ADC控制器支持2组采样结果上报寄存器，每组包括16个16bit寄存器，每个16bit寄存器对应一个虚拟通道的采样结果，支持CPU和DMA读取采样结果（32个结果上报寄存器地址连续），支持8\*20bit求和结果寄存器，地址连续于上述2组结果；

- 第一组：存储上报用户偏置和增益计算处理、预处理滤波的结果，支持s(16,2)和s(15,0)两种结果上报格式可配置选择；
- 第二组：存储上报滤波计算处理后的采样结果，支持s(16,2)和u(12,0)两种结果上报格式可配置选择；滤波处理后上报结果：s(16,2)、u(12,0)；
- 求和结果：对第一组结果进行求和结果，根据第一组输出格式匹配为s(20,2)和s(19,0)

**LRS.SARC.FUNC.SPEC【26】**　用户预处理通道结果、滤波通道结果两组结果mux选择后同步到CPU时钟域下，快速响应CPU读动作。

a) 两个虚拟通道的结果放入一个寄存器中。

<!-- source: GameViewer_hTRpPSKxgI.png -->
> 原图：[GameViewer_hTRpPSKxgI.png](../images/GameViewer_hTRpPSKxgI.png)。左页27～30a，右页接30b～34。

**LRS.SARC.FUNC.SPEC【27】**　每个ADC控制器支持如下采样结果处理数据流：

> 图中文字转录（原图无图号）：`ADC校准参数处理`、`用户配置参数处理`、`滤波处理`；`adc_data_out`、`signed`、`cal_data_out`、`pre_data_out`、`filter_data_out`；`round`、`sat`、加法/乘法/求和符号；`EVTOUT`；`result reg 1 16\*16bit`、`result reg 2 16\*16bit`，浅蓝色求和块及`sum reg 8\*20bit`。原图数据支路、颜色和运算次序见原图。
> ⚠️ 原图待复核（SARC-LRS-U02）：图内系数完整名、部分定标/位宽小字、signed块下的完整说明与小方框名称在当前截图中不足以逐字符确认；仅保留上列可辨内容，不从FUNC条目或其他图猜填。

**LRS.SARC.FUNC.SPEC【28】**　每个ADC控制器支持基于虚拟通道进行采样结果更新标志位上报；

**LRS.SARC.FUNC.SPEC【29】**　每个ADC控制器支持基于虚拟通道进行采样结果被覆盖标志位上报。

**LRS.SARC.FUNC.SPEC【30】**　每个ADC支持4+1个DMA请求通道，

a) 4个DMA请求通道可从如下DMA请求源中独立配置选择：

- EOC脉冲信号（基于虚拟通道，16bit）
- 2组结果寄存器锁存有效采样结果（基于虚拟通道，16bit\*2）
- 电平超门限检测结果事件（基于虚拟通道\*16bit）
- 过采样求和完成事件；（基于过采样求和通道8bit）

b) 1个16个虚拟通道电平超门限检测结果事件或输出；

**LRS.SARC.FUNC.SPEC【31】**　支持在通过fifo读取采样结果模式下，通过fifo的非空信号进行DMA请求，两个fifo的非空信号可独立选择到4个dma请求通道，默认配置下不选择fifo的DMA请求；

**LRS.SARC.FUNC.SPEC【32】**　每个ADC支持工作状态可独立查询：

- IDLE：对应ADC空闲
- BUSY：对应ADC正在采样
- 通道指示（IDLE时指示上一个采样的虚拟通道号，BUSY时指示当前正在采样的虚拟通道号）

**LRS.SARC.FUNC.SPEC【33】**　每个ADC控制器支持16个虚拟通道工作状态可独立查询：

- IDLE：对应虚拟通道空闲
- PENDING：对应虚拟通道被有效触发，但处于排队状态
- BUSY：对应虚拟通道正在被执行采样

**LRS.SARC.FUNC.SPEC【34】**　同一个虚拟通道，若采样事件来不及处理（即该虚拟通道被触发正在排队时又收到新的触发信号），上报采样触发冲突告警，每个虚拟通道独立上报告警，该告警需要软件清除；

<!-- source: GameViewer_TxOL7pU1gm.png -->
> 原图：[GameViewer_TxOL7pU1gm.png](../images/GameViewer_TxOL7pU1gm.png)。左页开头“软件清除”续接34，已合并；之后35～39及右页39续句～44。

**LRS.SARC.FUNC.SPEC【35】**　支持校准后数据输出供ATE测试使用，输出数据格式为u(12,0)，范围为0~4095；

**LRS.SARC.FUNC.SPEC【36】**　每个ADC控制器接收模拟ADC返回采样结果支持如下两种方式：

- 模拟ADC_CORE输出async ready信号：控制器使用异步方式处理该ready信号（默认选择）；
- 模拟AFE_TOP打拍输出sync ready信号：控制器使用同步方式处理该ready信号；

**LRS.SARC.FUNC.SPEC【37】**　用cfg_sarc_en的上升沿清零采样结果寄存器，清除ADC校准算法处理时产生的采样结果；

**LRS.SARC.FUNC.SPEC【38】**　SARADC支持对采样结果按照fifo模式进行DMA搬移，每个ADC控制器新增两套寄存器用于fifo模式，分别对应用户偏置/增益处理和滤波处理的采样结果数据通道；

**LRS.SARC.FUNC.SPEC【39】**　fifo模式下支持bitmap映射具体通道，控制虚拟通道结果是否映射到fifo中，bitmap由软件配置（默认为vc_en），硬件维护，初始加载或者参数修改需要通过软件配置reload加载，vc的采样顺序必须按照bitmap配置中vc编号从小到大的顺序；或者应用约束所有映射到fifo的vc必须采用同一个触发源，且均处于同一个优先级；

**LRS.SARC.FUNC.SPEC【40】**　支持软件对fifo深度的配置，fifo深度默认为16；

**LRS.SARC.FUNC.SPEC【41】**　通过fifo寄存器地址读取采样结果时，需要清除对应结果寄存器中的val和ovf标志；

**LRS.SARC.FUNC.SPEC【42】**　支持通过fifo寄存器地址读取采样结果时，上报每次读取结果对应的vc编号；

**LRS.SARC.FUNC.SPEC【43】**　支持fifo状态上报，包含空，满，空溢出，满溢出，fifo中数据个数。

**LRS.SARC.FUNC.SPEC【44】**　在预处理通道之后支持8个预处理滤波器通道、8个求和通道SCh。

> 图中文字转录（原图无图号）：此处再次出现模块结构图，包含`SARADC CALC`、`SARADC CTRL`、`S/H`、`SARCORE`、`CAL`、`ready`、`data`、`busy`、`done`、`trigger`；输入`Chan 0`、`Chan 1`、省略点、`Chan N`；预处理、预处理滤波、滤波、缓存两组通道与`to CPU/DMA`输出；浅蓝色`SCh0`、`SCh1`、`SCh7`及`Sum0`、`Sum1`、`Sum7`，中间为省略点。PChan/PFChan/FChan/BChan的可辨编号与模块简介图分别保留，不计为又一组硬件实例。
> 转录注：本处控制长箭头的细字与简介图同属SARC-LRS-U01，完整图仍链接本张原图。

<!-- source: GameViewer_PJZbqwPIEg.png -->
> 原图：[GameViewer_PJZbqwPIEg.png](../images/GameViewer_PJZbqwPIEg.png)。左页续接44的1）～3）及引用图片；右页为4）～5）、45～47e。

1）从16个预处理通道映射到8个预处理滤波器通道（映射关系寄存器可配，最多只能从16个预处理通道中选择8个映射到预处理滤波器通道，其他的bypass）；

2）预处理滤波支持iir滤波器（直接1型）1~4阶软件可配置，支持fir滤波器1~8阶软件可配置；

3）预处理滤通道输入数据可进行放大和缩小（算数左移或者算数右移，带符号移位），移位的范围为：-1~2（负数表示左移，正数表示右移；原始预处理通道输入数据为s(16,2)，此处为了对标TI：`\ET6801-DOC\05.数字设计\03 HAC\SARC\V100\01.需求分析\01.竞品资料\dm00605584-digital-filter-implementation-with-the-fmac-using-stm32cubeg4-mcu-package-stmicroelectronics(1)(2).pdf`）；

> 转录注：以下英语与两张16列表格是本张截图内嵌引用图的内容，仅转录本图可见部分，没有访问引用文献补写。

In the ADC, the factor K<sub>ADC</sub> = 8 is applied using the left justification feature. The ADC result (after subtracting the offset) is a 12-bit signed integer. In right-aligned format, the result is sign-extended to 16-bits:

**Table 3. Right aligned ADC data**

| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sign | sign | sign | sign | b11 | b10 | b9 | b8 | b7 | b6 | b5 | b4 | b3 | b2 | b1 | b0 |

In left aligned mode the result is shifted left by 3, retaining only one sign bit:

**Table 4. Left aligned ADC data**

| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sign | b11 | b10 | b9 | b8 | b7 | b6 | b5 | b4 | b3 | b2 | b1 | b0 | 0 | 0 | 0 |

4）乘法器位宽：16\*16bit，加法器位宽：支持36~~27~~bit（此处对标FMAC）；

> 转录注：原图“36”为浅蓝色，“27”带删除线，二者相邻；不是“3627bit”。

5）预处理滤波通道的输入输出最大数据速率跟ADC最高采样率保持一致；

**LRS.SARC.FUNC.SPEC【45】**　支持对模拟的放电时序控制；

**LRS.SARC.FUNC.SPEC【46】**　支持用户预处理过程的中间值观测；

a) 1\*原始采样值u(12,0)；  
b) 1\*模拟校正值s(16,2)、u(12,0)；  
c) 16vc\*PFC滤波输出结果s(16,2)、s(15,0)；  
d) 8个vc\*过采样求和结果输出s(20,2)、s(19,0)；

**LRS.SARC.FUNC.SPEC【47】**　支持基于用户预处理滤波通道的过采样触发、过采求和功能；

a) 过采求和次数N <=16；  
b) 采样间隔count为22bit配置，单位为sarc工作时钟；  
c) 间隔期间允许其它低优先级进行采样；  
d) count及N支持影子加载，触发时完成影子值到生效值更新；  
e) 过采期间忽略新触发，但会告警；  
f) 过采样被高优先级通道打断后，支持resume、conti模式；  
g) 过采功能支持使能控制；

<!-- source: GameViewer_eyXbfnO5PJ.png -->
> 原图：[GameViewer_eyXbfnO5PJ.png](../images/GameViewer_eyXbfnO5PJ.png)。左页首两行续接47f～g，已在上方合并；之后48、中断管理，再右页续句和时序图。

**LRS.SARC.FUNC.SPEC【48】**　不抢占模式下，从触发输出到发出模拟的采样控制延迟在4个ADCCLK时钟以内，抢占模式下从高优先级触发到发出模拟的采样控制延迟在6个ADCCLK以内；

#### 2.2 中断管理

**LRS.SARC.INTR.SPEC【01】**　每个ADC控制器的虚拟通道支持对应EOC（end-of-conversion）信号产生，用于触发中断，EOC脉冲信号可配置选择如下三个产生位置，每个ADC控制器的虚拟通道统一配置：

- S/H窗口结束时刻，
- 采样转换结束时刻，默认选择
- S/H窗口开始时刻

**LRS.SARC.INTR.SPEC【02】**　支持EOC选择位置时刻到中断产生的上沿延时可配置，16bit SYSCLK时钟计数值；且每个ADC控制器的虚拟通道统一配置。如果当前EOC到来时，上一个EOC的延时处理没有完成，则在该时刻输出上一个EOC的中断触发，同时当前EOC进行延时模块进行延时处理；

> 图中文字转录（原图无图号）：波形名`end_p`、`int_trig`；时间箭头`delay_i`、`delay_j`。批注原文：“end_p到来时，上一个end_p的delay还没有完成，则在该时刻输出上一个end_p的int_trig，然后当前enc_p进行delay模块重新开始计数延时。”
> ⚠️ 原图待复核（SARC-LRS-U03）：各脉冲框内`vc`后的完整下标在当前截图中无法逐字符确认；不根据左右脉冲次序猜写i/j/k。批注中前文end_p与后文enc_p分别照录。

**LRS.SARC.INTR.SPEC【03】**　每个ADC支持上报延时冲突告警，即当前EOC到来时，上一个EOC的延时处理未完成状态，告警状态软件读清；并且同时上报延时未处理完成的虚拟通道编号；

**LRS.SARC.INTR.SPEC【04】**　每个ADC支持5路中断输出；

1. 其中1路中断包括：

- 电平超门限中断（基于虚拟通道，超门限脉冲触发中断，超上下门限独立中断源，共16bit\*2）

2. 另外4路中断中，每1路中断可独立选择以下中断作为中断源；

- EOC脉冲信号（基于虚拟通道，16bit）
- 2组结果寄存器锁存有效采样结果中断（基于虚拟通道，16bit\*2）
- 过采求和结果有效中断（基于过采求和通道，8bit）

**LRS.SARC.INTR.SPEC【05】**　每个ADC支持中断溢出告警指示；

<!-- source: GameViewer_XDCKpTnaH0.png -->
> 原图：[GameViewer_XDCKpTnaH0.png](../images/GameViewer_XDCKpTnaH0.png)。左页事件管理、约束01～04；右页约束05～08和采样触发源表头。

#### 2.3 事件管理

**LRS.SARC.EVT.SPEC【01】**　每个ADC控制器支持如下事件输出：

- ADC输出到XBAR电平超门限检测输出事件\*4（从16个VC事件中独立配置选择）
- ADC输出到ETIM电平超门限检测输出事件\*4（从16个VC事件中独立配置选择）

#### 2.4 约束说明

**LRS.SARC.LIMIT.SPEC【01】**　ADC数字控制器不能早于模拟ADC解复位；

**LRS.SARC.LIMIT.SPEC【02】**　ADC数字控制器不能早于模拟ADC使能有效；

**LRS.SARC.LIMIT.SPEC【03】**　系统时钟频率不能低于ADC工作时钟频率；

**LRS.SARC.LIMIT.SPEC【04】**　外部输入的采样触发源脉冲需要为正脉冲，且脉冲宽度要大于1个系统时钟周期（因为是同步处理）；

**LRS.SARC.LIMIT.SPEC【05】**　使用超过16阶FIR滤波时，系统时钟频率必须大于ADC工作时钟频率的2倍以上；（2个连续需要FIR滤波处理的采样，需要最小间隔FIR滤波阶数个系统时钟周期）

**LRS.SARC.LIMIT.SPEC【06】**　ADC校准时，要求软件关闭模拟ADC使能，待校准流程完成后再打开模拟ADC使能；

**LRS.SARC.LIMIT.SPEC【07】**　对虚拟通道vc的配置，需要将对应的vc_en关闭后进行配置，配置完成后再将vc_en打开；

**LRS.SARC.LIMIT.SPEC【08】**　ADC数字控制器的使能信号需要早于控制器内的其他使能信号（比如vc_en等）打开；

#### 2.5 触发源说明

**LRS.SARC.TRIG.SPEC【01】**　每个ADC控制器中16个虚拟通道支持如下采样触发源信号可独立配置选择：

| sample 触发源 | 位域 | SARC0/1 |
|---|---|---|
| SPWM | [23:0] | {epwm_sadc_trig[23:0]} |
| ETIM | [49:36] | etim2adc_evt[13:0] |
| RESERVED | [52:50] | 'd0 |
| IPTEST | 53 | iptest_adc_start |
| CMPC | [75:54] | {cmpc_ctripl[10],cmpc_ctriph[10],<br>cmpc_ctripl[9],cmpc_ctriph[9],<br>cmpc_ctripl[8],cmpc_ctriph[8],<br>cmpc_ctripl[7],cmpc_ctriph[7],<br>cmpc_ctripl[6],cmpc_ctriph[6],<br>cmpc_ctripl[5],cmpc_ctriph[5],<br>cmpc_ctripl[4],cmpc_ctriph[4],<br>cmpc_ctripl[3],cmpc_ctriph[3],<br>cmpc_ctripl[2],cmpc_ctriph[2],<br>cmpc_ctripl[1],cmpc_ctriph[1],<br>cmpc_ctripl[0],cmpc_ctriph[0]} |
| STM | [99:76] | {tm5_oc_exp[3:0],<br>stm4_oc_exp[3:0],<br>stm3_oc_exp[3:0],<br>stm2_oc_exp[3:0],<br>stm1_oc_exp[3:0],<br>stm0_oc_exp[3:0]} |
| CLU | [103:100] | xbar2sarc_cludata[3:0] |
| ADCEOC | [107:104] | {sarc1_eoc2spl_trig[1:0],<br>sarc0_eoc2spl_trig[1:0]} |
| RESERVED | [109:107] | 'd0 |
| GPIO（inputxbar） | [110] | inputxbar_data[4] |
| RESERVED | [126:111] | 'd0 |
| SOFT_START | [127] | sarc_soft_start |

<!-- source: GameViewer_Dt52xixULd.png -->
> 原图：[GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png)。左页从IPTEST开始接续前图的采样表，已合并为上表12行；右页为Blanking表及文档末尾。
> 转录注：STM首个信号原图为`tm5_oc_exp`，后续为`stm4`～`stm0`，不擅自补s。`[109:107]`与上一行`[107:104]`在107重叠，原图如此；表中`[24:35]`未列出，不补造保留行。

**LRS.SARC.TRIG.SPEC【02】**　Blanking功能支持如下触发源进行触发启动：

| blanking 触发源 | 位域 | SARC0/1/2 |
|---|---|---|
| SPWM | [23:0] | {epwm_sadc_trig[23:0]} |
| ETIM | [49:36] | etim2adc_evt[13:0] |
| RESERVED | [52:50] | 'd0 |

> 转录注：本表表头确为`SARC0/1/2`，未改写为上一表的`SARC0/1`。原图其后为文档末尾和空白，没有更多触发源行。

## 第二部分：截图明确标注的 ET6601 修改点
### 颜色与来源判定
本部分依据修订表右页原文：“浅蓝色和清绿色相关区域为ET6601新加的改动，包括线，背景及底纹部分”。原图：[GameViewer_aAOwVv2FCQ.png](../images/GameViewer_aAOwVv2FCQ.png)。这条规定适用于本份SARC LRS，不能套用其他IP的颜色判定。
下表共32条来源位置记录，含正文、修订表及重复出现的图、触发表；不等于32个独立功能变化。原文没有给出旧值的地方不编造“旧值→新值”。
| 编号 | 原始文字或可辨标记 | 所在章节／表格 | 原图 | 修改性质与范围 |
|---|---|---|---|---|
| C01 | 6601在6801的基础上调整，文档中使用浅蓝色体现修改；<br>1. 增加抢占功能；<br>2. 增加用户预处理滤波过采求和功能；<br>3. 增加用户预处理的观测功能；<br>4. | 表1-1，v1.0，2026/09/22 | [GameViewer_aAOwVv2FCQ.png](../images/GameViewer_aAOwVv2FCQ.png) | v1.0、该行文字、日期及修订人均为浅蓝色；原文明确增加；第4项空白 |
| C02 | 1. 增加触发到开始采样，抢占触发到开始采样的延迟指标需求 | 表1-1，2026/10/1 | [GameViewer_aAOwVv2FCQ.png](../images/GameViewer_aAOwVv2FCQ.png) | 修订内容为浅蓝色；日期和修订人按原表保留 |
| C03 | SCh0、SCh1、…、SCh7；Sum0、Sum1、…、Sum7 | 1.1模块简介，结构图 | [GameViewer_WtOrHaAqvH.png](../images/GameViewer_WtOrHaAqvH.png) | 求和通道与求和结果框为浅蓝色；只记录可辨标签，不推断所有细小连线文字 |
| C04 | ~~Power-gating~~ | FUNC.SPEC【01】 | [GameViewer_WtOrHaAqvH.png](../images/GameViewer_WtOrHaAqvH.png) | 原文有删除线；后接Clock-gating未删除；没有推断原版本或原因 |
| C05 | （数字侧按32采样通道预留控制接口，模拟测按实际通道实现） | FUNC.SPEC【02】 | [GameViewer_WtOrHaAqvH.png](../images/GameViewer_WtOrHaAqvH.png) | 括号内为浅蓝色；“模拟测”按原图保留 |
| C06 | 2；SARC0~1；2 | FUNC.SPEC【04】 | [GameViewer_WtOrHaAqvH.png](../images/GameViewer_WtOrHaAqvH.png) | 两个数量2及SARC0~1为浅蓝色；完整上下文为2个控制器管理2个内核；不把01中的3自动改成2 |
| C07 | 2；2 | FUNC.SPEC【06】 | [GameViewer_WtOrHaAqvH.png](../images/GameViewer_WtOrHaAqvH.png) | 同步/非同步描述中的两个数量2为浅蓝色；完整条目在正文 |
| C08 | 8个求和通道SCh；1\*8个求和结果寄存器 | FUNC.SPEC【07】跨页续句 | [GameViewer_WtOrHaAqvH.png](../images/GameViewer_WtOrHaAqvH.png)、[GameViewer_nGNAOmfeWa.png](../images/GameViewer_nGNAOmfeWa.png) | 浅蓝色；其余VC/PC/PFC/FC/BC数量按原文分别保存 |
| C09 | 支持p0高优先级虚拟通道抢占低优先级虚拟通道抢占；<br>a) 低优先级虚拟通道在高优先级通道结束后，继续低优先级请求；<br>b) 增加使能控制；<br>c) 仅p0可抢占其它低优先级；<br>d) p0内部不进行抢占； | FUNC.SPEC【11】 | [GameViewer_nGNAOmfeWa.png](../images/GameViewer_nGNAOmfeWa.png) | 正文及a～d均为浅蓝色；句内重复“抢占”照录 |
| C10 | 当sample被高优先级通道抢占后，原通道的Trigger-to-sample会在重新开始sample时更新延迟时间，过采样启用时在过采第一次开始sample上报，后续过采过程中不再上报； | FUNC.SPEC【14】后半段 | [GameViewer_nGNAOmfeWa.png](../images/GameViewer_nGNAOmfeWa.png) | 浅蓝色；前半段原有延迟计算文字不重复归为新增 |
| C11 | 支持软件输出采样触发，同其它硬件采样触发通路一致； | FUNC.SPEC【16】 | [GameViewer_Kd7bk57Vx3.png](../images/GameViewer_Kd7bk57Vx3.png) | 整句浅蓝色 |
| C12 | 支持8\*20bit求和结果寄存器，地址连续于上述2组结果；<br>求和结果：对第一组结果进行求和结果，根据第一组输出格式匹配为s(20,2)和s(19,0) | FUNC.SPEC【25】求和相关两处 | [GameViewer_CeKX8gRMOe.png](../images/GameViewer_CeKX8gRMOe.png) | 两处浅蓝色；第一、第二组其他格式说明照录 |
| C13 | sum reg 8\*20bit | FUNC.SPEC【27】，数据流图 | [GameViewer_hTRpPSKxgI.png](../images/GameViewer_hTRpPSKxgI.png) | 浅蓝色求和块及求和结果标签；图内其他小字仍有SARC-LRS-U02，不当成已完整转录 |
| C14 | 过采样求和完成事件；（基于过采样求和通道8bit） | FUNC.SPEC【30】a的最后一个请求源 | [GameViewer_hTRpPSKxgI.png](../images/GameViewer_hTRpPSKxgI.png) | 该项目为浅蓝色，4+1个DMA请求通道数本身为黑字 |
| C15 | 8个求和通道SCh；SCh0、SCh1、…、SCh7；Sum0、Sum1、…、Sum7 | FUNC.SPEC【44】及重复结构图 | [GameViewer_TxOL7pU1gm.png](../images/GameViewer_TxOL7pU1gm.png) | 句中8个求和通道SCh为浅蓝色；重复结构图的求和块为浅蓝色；不算另一组实例 |
| C16 | 乘法器位宽：16\*16bit，加法器位宽：支持36~~27~~bit（此处对标FMAC）； | FUNC.SPEC【44】第4）项 | [GameViewer_PJZbqwPIEg.png](../images/GameViewer_PJZbqwPIEg.png) | 36为浅蓝色，27为删除线；该处原文同时给出替换标记，可记录27改为36，不能写3627bit |
| C17 | 支持用户预处理过程的中间值观测；<br>a) 1\*原始采样值u(12,0)；<br>b) 1\*模拟校正值s(16,2)、u(12,0)；<br>c) 16vc\*PFC滤波输出结果s(16,2)、s(15,0)；<br>d) 8个vc\*过采样求和结果输出s(20,2)、s(19,0)； | FUNC.SPEC【46】 | [GameViewer_PJZbqwPIEg.png](../images/GameViewer_PJZbqwPIEg.png) | 正文和四个子项均为浅蓝色 |
| C18 | 支持基于用户预处理滤波通道的过采样触发、过采求和功能；<br>a) 过采求和次数N <=16；<br>b) 采样间隔count为22bit配置，单位为sarc工作时钟；<br>c) 间隔期间允许其它低优先级进行采样；<br>d) count及N支持影子加载，触发时完成影子值到生效值更新；<br>e) 过采期间忽略新触发，但会告警；<br>f) 过采样被高优先级通道打断后，支持resume、conti模式；<br>g) 过采功能支持使能控制； | FUNC.SPEC【47】，跨图a～g | [GameViewer_PJZbqwPIEg.png](../images/GameViewer_PJZbqwPIEg.png)、[GameViewer_eyXbfnO5PJ.png](../images/GameViewer_eyXbfnO5PJ.png) | 正文及a～g均为浅蓝色，f～g在下一截图首行 |
| C19 | 不抢占模式下，从触发输出到发出模拟的采样控制延迟在4个ADCCLK时钟以内，抢占模式下从高优先级触发到发出模拟的采样控制延迟在6个ADCCLK以内； | FUNC.SPEC【48】 | [GameViewer_eyXbfnO5PJ.png](../images/GameViewer_eyXbfnO5PJ.png) | 整句浅蓝色；这是原文需求，不是已实测时延 |
| C20 | 过采求和结果有效中断（基于过采求和通道，8bit） | INTR.SPEC【04】，另外4路的最后一个中断源 | [GameViewer_eyXbfnO5PJ.png](../images/GameViewer_eyXbfnO5PJ.png) | 该项目及圆点浅蓝色；5路中断总数为黑字，不推断增加路数 |
| C21 | SPWM；[23:0]；{epwm_sadc_trig[23:0]} | TRIG.SPEC【01】，SPWM行 | [GameViewer_XDCKpTnaH0.png](../images/GameViewer_XDCKpTnaH0.png) | 该行三个单元格为浅蓝色 |
| C22 | [49:36]；etim2adc_evt[13:0] | TRIG.SPEC【01】，ETIM行 | [GameViewer_XDCKpTnaH0.png](../images/GameViewer_XDCKpTnaH0.png) | 位域浅蓝色；信号下标13标浅蓝，信号名主体为黑色 |
| C23 | RESERVED；[52:50]；'d0 | TRIG.SPEC【01】，首个RESERVED行 | [GameViewer_XDCKpTnaH0.png](../images/GameViewer_XDCKpTnaH0.png) | 该行三个单元格为浅蓝色 |
| C24 | [75:54]；cmpc_ctripl[10],cmpc_ctriph[10],cmpc_ctripl[9],cmpc_ctriph[9],cmpc_ctripl[8],cmpc_ctriph[8],cmpc_ctripl[7],cmpc_ctriph[7],cmpc_ctripl[6],cmpc_ctriph[6],cmpc_ctripl[5],cmpc_ctriph[5],cmpc_ctripl[4],cmpc_ctriph[4] | TRIG.SPEC【01】，CMPC行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 位域和编号10～4的信号为浅蓝色；编号3～0为黑字，完整22项见原表 |
| C25 | CLU；[103:100] | TRIG.SPEC【01】，CLU行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 名称和位域浅蓝色；xbar2sarc_cludata[3:0]为黑字 |
| C26 | [107:104] | TRIG.SPEC【01】，ADCEOC行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 位域浅蓝色，两路eoc信号为黑字 |
| C27 | [109:107] | TRIG.SPEC【01】，ADCEOC后的RESERVED行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 109标浅蓝色；107与上一行重叠按原表保留 |
| C28 | [110] | TRIG.SPEC【01】，GPIO（inputxbar）行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 位域浅蓝色；inputxbar_data[4]为黑字 |
| C29 | [126:111] | TRIG.SPEC【01】，GPIO后的RESERVED行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 126标浅蓝色，其余原表内容保持 |
| C30 | SOFT_START；[127]；sarc_soft_start | TRIG.SPEC【01】，SOFT_START行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 该行名称、位域、信号为浅蓝色 |
| C31 | SPWM；[23:0]；{epwm_sadc_trig[23:0]} | TRIG.SPEC【02】，SPWM行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 该行名称、位域、信号为浅蓝色；不与sample表混为一个来源位置 |
| C32 | [49:36]；etim2adc_evt[13:0] | TRIG.SPEC【02】，ETIM行 | [GameViewer_Dt52xixULd.png](../images/GameViewer_Dt52xixULd.png) | 位域和信号下标13为浅蓝色；表头SARC0/1/2照录 |

### 历史修订删除线，不自动认定为6601新增
20250909“合入6801的优化点”中的第2项和第5项均有删除线；日期有下划线，详见表1-1。正文FUNC.SPEC【26】仍保留“两通道结果放入一个寄存器”的描述，两处分别照录，不擅自以修订表划线为理由删除正文。这两条历史记录未重复计入上述32条。

## 转录复核记录（非原文）
### 已辨明但不擅自修正的原文差异
| 编号 | 位置 | 原图实际内容与处理 |
|---|---|---|
| D01 | FUNC01、04、06和Blanking表头 | FUNC01仍写3个ADC内核；04/06为2，04为SARC0~1；Blanking表头SARC0/1/2。各处照录，不自行统一数量。 |
| D02 | TRIG01采样表 | ADCEOC [107:104]与RESERVED [109:107]重叠；23:0后接49:36，没有24～35行。保持原表，不补造条目。 |
| D03 | TRIG01 STM行 | 首个名称tm5_oc_exp，后五项stm4～stm0；原文如此，不补s。 |
| D04 | FUNC02、13、11及INTR02图注 | “模拟测”“数字测”、重复“抢占”，以及end_p/enc_p差异均照图保留；不润色为推断出的正确术语。 |
| D05 | 修订表20250909、FUNC26 | 历史两通道合并条目有删除线，正文仍有两通道结果合并描述；不自行裁决哪个设计版本正确。 |
| D06 | FUNC44第3）项及内嵌引用图 | 正文称“对标TI”，路径文件名和内嵌文字另有实际来源表述；只转录原图，不替换引用对象或访问外部文献填字。 |

### 未解决的图内细字
| 编号 | 原图与位置 | 未解决范围 | 后续处理 |
|---|---|---|---|
| SARC-LRS-U01 | WtOrHaAqvH左页结构图；TxOL7pU1gm右页重复图 | 控制长箭头完整文字与少量节点细字 | 用同源高分辨率图确认；可辨标签和原始连线已保留。 |
| SARC-LRS-U02 | hTRpPSKxgI左页数据流图 | 系数名、部分定标/位宽、signed说明及小框名称 | sarc_diagrams含数据流程来源图，可作为后续比对候选；本批未证明所有细节一致，不能直接填入。 |
| SARC-LRS-U03 | eyXbfnO5PJ右页EOC时序图 | 脉冲框内vc完整下标 | 不按时序常识猜i/j/k；图注其余可辨文字已转录。 |

本批已核对13张原始截图、48条FUNC、5条INTR、1条EVT、8条LIMIT、2条TRIG；采样触发表12行、Blanking表3行，内嵌两表各16列，均已转录。覆盖、列数和保存校验不等于逐字符准确率，3组图内缺口未关闭，全文尚未最终验收。
