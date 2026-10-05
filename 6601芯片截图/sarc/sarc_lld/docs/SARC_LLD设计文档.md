# SARC 模块方案设计

> 来源：本仓库sarc_lld目录40张原始PNG；原文封面标题《SARC模块方案设计》，保持一份原始文档。
> 第八～十轮定点回查：U01～U18已按原PNG再次查看，并补入确认字形。U01～U19均尚有局部缺口；U19及LRS/辅助缺口是下一批。本轮不是全文第二遍验收。
> 首轮覆盖40张不等于来源页已完整或逐字验收通过：U01～U19共19组局部字形/遮挡缺口及S01来源连续性疑点仍未关闭。
> 按原文顺序、双页先左后右；重复图号、删除线、原文拼写/参数和作者空白保留。浅蓝/清绿按原文声明归集，6002/6801历史说明另列。
> 来源commit：`d80a74e83e4bf942905844e61efd5d169e37c815`；本轮输入HEAD：`d75fc901b5914d165f1a797e49a60fa6a81b4e0c`，输入LLD blob：`33bed8b0c1348ba02e616557fbbd3785661ed393`。台账见`../../../reviews/SARC_LLD_ROUND5_IMAGE_LEDGER_20261005.json`，实际保存见本轮REMOTE_SAVE。

## 第一部分：原始文档逐图还原

## 原图：`GameViewer_be9VqBBdbM.png`

[查看原始PNG](../images/GameViewer_be9VqBBdbM.png)

### 【左页】

# SARC 模块方案设计

> 转录注：封面公司标识保留在原图中；窗口标题、账号水印及播放器信息不属于正文。

### 【右页】

设计：郑汶  
评审：  
批准：

---

## 原图：`GameViewer_aPDFQVxWhA.png`

[查看原始PNG](../images/GameViewer_aPDFQVxWhA.png)

### 【左页】

**表1-1 修订记录**

| 版本号 | 修订内容 | 修订日期 | 修订人员 |
|---|---|---|---|
| | 首次修订 | | |
| | 1、在预处理通道之后新增8个预处理滤波器通道； | 20240819 | 肖中平 |
| | ET6801下修改点如下：<br>1. 增益补偿-2048处理；<br>2. 同步输出adc结果到cpu_wrap；<br>3. fifo模式的空溢出/满溢出标志问题fix；<br>4. eoc中断位置增加；<br>5. 模拟变更(物理通道通道增加等) | 2025/9/30 | 郑汶 |

> 转录注：以上版本号单元格原图为空；表尾另有14个全空白续行。没有用录屏日期填入修订日期，没有把明确标为ET6801的历史条目当作ET6601新增。

### 【右页】

注：浅蓝色和清绿色相关区域为ET6601新加的改动，包括线，背景及底纹部分；

> 转录注：本句为原文青色底纹说明，是本份文档变更标记的判定依据；目录链接的蓝色不据此自动算成变更。

---

## 原图：`GameViewer_3ZWo3TthG6.png`

[查看原始PNG](../images/GameViewer_3ZWo3TthG6.png)

### 【左页】

# 目录

- 1. 模块 OR_DR 需求
- 2. 概述
- 3. 功能描述
- 4. 接口说明
  - 4.1 SARADC 接口信号
  - 4.2 SARADC 接口时序
    - 采样时间
    - 接口时序
- 5. 方案设计
  - 5.1 SARC 整体结构
  - 5.2 时钟关系
  - 5.3 SARADC CALC
  - 5.4 外部触发源
  - 5.1 触发模式

### 【右页】

  - 单次触发模式
  - 连续触发模式
- 5.1 blanking 机制
- 5.1 优先级队列管理
- 5.2 SARADC 控制器看门狗
- 5.3 SARADC 控制时序
- 5.4 ADC 同步模式
- 5.5 软件直接触发采样
- 5.6 SARADC 控制器中断
- 5.7 转换后处理
- 5.8 预处理通道
- 5.9 滤波通道
  - IIR
  - FIR
  - 滑动平均
  - 非滑动平均
  - 滤波器实现时序
  - FIR 滤波器参数存储

> 原文差异：目录的5.1等编号多次重复且与后续正文不同。各处分别照录，不修订原编号。

---

## 原图：`GameViewer_v6tUVs7H0k.png`

[查看原始PNG](../images/GameViewer_v6tUVs7H0k.png)

### 【左页】

- FIR 滤波器输入采样结果 PIPELINE
- 5.10 缓存通道
- 5.11 DMA 数据请求
- 5.12 乘法器复用
- 5.13 状态告警处理
  - CORE 和 VC 状态
  - 触发超时告警
- 6. 约束
- 7. 遗留问题
- 8. 可优化点
  - 8.1 乘法器复用
- 9. 参考文献

### 【右页】

# 图目录

# 1. 模块 OR_DR 需求

SARC（SARADC Controller）模块，以《OR_DR》《SARC模块LRS设计文档》为需求依据，在本文档中进行方案设计。

**表1 SARC 模块设计需求**

> 图表转录注：此表是页面内嵌的小截图，未显示列标题。下表列名“分组／需求编号／项目／要求／空列／归属／末空列”为转录定位说明，不是补造的原表标题。首列“支持2个ADC控制器”为跨18行的合并单元格；空列保留。模糊处以【未辨】表示，详见SARC-LLD-U01。

| 分组 | 需求编号 | 项目 | 要求 | 空列 | 归属 | 末空列 |
|---|---|---|---|---|---|---|
| 支持2个ADC控制器 | DR_SARADC_001 | ADCCORE数量 | 支持2个ADC控制器，每个控制器支持32个采样通道 | | HAC | |
| | DR_SARADC_002 | 采样校准 | 支持每一个ADC CORE的增益和偏置校正 | | HAC | |
| | DR_SARADC_003 | 扩展采样 | 【未辨：采样相关整句小字】 | | HAC | |
| | DR_SARADC_004 | 虚拟通道数 | 每个ADC控制器支持16个虚拟通道 | | HAC | |
| | DR_SARADC_005 | ADCCLK时钟分频 | 支持ADCCLK预分频，分频系数实时软件可配置 | | HAC | |
| | DR_SARADC_006 | 【未辨：项目小字】 | 【未辨：每个虚拟通道的配置说明】 | | HAC | |
| | DR_SARADC_007 | blanking | 支持每一个ADC控制器虚拟通道0支持blanking触发流程 | | HAC | |
| | DR_SARADC_008 | 通道优先级 | 虚拟通道优先级支持4个虚拟优先级配置，支持最高优先级抢占低优先级 | | HAC | |
| | DR_SARADC_009 | 预处理通道 | 支持每个虚拟通道转换后的数据进行预处理通道 | | HAC | |
| | DR_SARADC_010 | 上下门限比较 | 支持每个虚拟通道的预处理后的数据进行上下门限判断，超门限时上报中断及状态 | | HAC | |
| | DR_SARADC_011 | 预处理滤波通道 | 每个core支持8通道的用户预处理【未辨】滤波算法FIR、IIR、【未辨】；<br>红字可辨部分：1. 支持IIR，阶数最大不大于1阶；2. FIR类型1~4阶；<br>第3、4子项有红色删除线，完整被删文字【未辨】；<br>5. 过采求和数量最大为16，过采间隔可配，过采参数实时影子加载；<br>6. 可选地支持打断处理方式resume、continue模式； | | HAC | |
| | 【划去行，编号疑似DR_SARADC_012】 | 【划去，文字未辨】 | 【划去，文字未辨】 | | HAC | |
| | DR_SARADC_013 | 缓存通道数 | 每个core支持8个对转换后数据的缓存通道 | | HAC | |
| | DR_SARADC_014 | 同步采样 | 支持ADC控制同步采样 | | HAC | |
| | DR_SARADC_015 | 状态查询 | SARADC支持ADCCORE、虚拟通道当前状态可查询 | | HAC | |
| | DR_SARADC_016 | FIFO模式 | SARADC支持对采样结果存储寄存器FIFO模式进行DMA搬移 | | HAC | |
| | DR_SARADC_017 | 模拟校准 | 支持ATE对SARADC进行校准，校准参数写入OTP | | HAC | |
| | DR_SARADC_018 | 数据输出 | 支持通过快捷窗口将SARC采样数据寄存器传输到M7_WRAP | | HAC | |

> ⚠️ 原图待复核：SARC-LLD-U01。内嵌表的多处小字、红字和删除线文字无法逐字符确认；上表仅逐行保留可辨内容，不以LRS或其他芯片资料补全。尤其第011行的1~4阶与后续正文不一致时，仍保留各自原文。
> 原图：[GameViewer_v6tUVs7H0k.png](../images/GameViewer_v6tUVs7H0k.png)，右页下方表1。

---

## 原图：`GameViewer_LWEUsHJgSN.png`

[查看原始PNG](../images/GameViewer_LWEUsHJgSN.png)

### 【左页】

# 2. 概述

SARADC主要用于采集片外电压、电流、温度、压力等信息，采样片内温度、电压、电流信息（可选），以及采样片内运放输出。

本文主要介绍内置SARADC控制器的设计方案，主要涵盖ADC工作模式配置和管理，数字校准，虚拟通道映射，优先级控制，采样触发控制，采样缓存处理，信号预处理，事件管理和中断上报等功能。

**当前版本sarc不支持差分模式，仅支持单端模式，但文档中仍保留相关差分内容。**

# 3. 功能描述

**图中文字转录（图1，图名在右页）：**

- 左侧输入：Chan 0、Chan 1、……、Chan N；采样通道选择；模拟逻辑、数字逻辑。
- 核心及控制：SARADC CALC、SH、SARCORE、SARADC CTRL、触发信号管理。
- 连接标签可辨：SH、trigger、ready、data、busy、done。
- 数据路径：校准通道CAL；预处理通道PChan 0、PChan 1、……、PChan15；预处理滤波通道PFChan 0、PFChan 1、……、PFChan 7；浅蓝色SCh0、SCh1、……、SCh7。
- 缓存：上组BChan 0、BChan 1、……、BChan15，浅蓝色Sum0、Sum1、……、Sum7；下组BChan 0、BChan 1、……、BChan15；CPU/DMA。
- 滤波通道：FChan0、FChan1、……、FChan7。
- 框图分区标题补录：校准通道、预处理通道、预处理滤波通道、缓存通道1、滤波通道、缓存通道2。

> ⚠️ 原图待复核：SARC-LLD-U02。结构图控制器右侧长箭头的完整文字及少量小节点标签仍不清楚，不借类似图猜补；上述只是可辨文字，连线以原图为准。
> 原图：[GameViewer_LWEUsHJgSN.png](../images/GameViewer_LWEUsHJgSN.png)，左页底部图1。

### 【右页】

**图1 SARADC框图**

SARC模块主要实现SARADC IP的采样控制和数据后处理，具体功能包括：

1、支持对SARADC模拟IP进行配置和管理；

2、支持对SARADC模拟IP进行数字校准（SARADC CALC）；

3、支持SARADC通道到虚拟通道映射；

4、支持SARADC通道触发信号优先级抢占控制；

5、支持SARADC通道事件管理和中断上报；

6、支持SARADC通道输出的缓存和预处理；

7、支持触发信号的周期延迟blanking机制。

8、支持SARADC预处理之后的数据可选地经过预处理滤波器，滤波器滤波器的类型为fir1~8阶/iir1~4阶，软件可配置；

9、支持预处理滤波通道启用过采样求和功能；

> 转录注：第4条“抢占”和第9条为浅蓝色；第8条原文“滤波器滤波器”重复，未润色。

---

## 原图：`GameViewer_ZQLidR9zmC.png`

[查看原始PNG](../images/GameViewer_ZQLidR9zmC.png)

### 【左页】

# 4. 接口说明

## 4.1 SARADC 接口信号

| 信号 | 输入／输出 | 说明 |
|---|---|---|
| **时钟复位** | | |
| clk_adc | 输入 | SARC输入ADC时钟，与clk_sarc同步 |
| adc_rst_n | 输入 | clk_adc复位信号，低电平有效 |
| **AHB3.0总线** | | |
| sarc_hclk | 输入 | 总线时钟 |
| sarc_hresetn | 输入 | 总线复位信号，低有效 |
| sarc_haddr[11:0] | 输入 | 12-bit系统地址总线，超出寄存器空间的高位地址不能使用。 |
| sarc_hburst[2:0] | | Burst类型，支持固定长度的4、8和16拍 |
| sarc_hprot[3:0] | 输入 | 保护控制信号 |
| sarc_hsize[2:0] | 输入 | 传输数据位宽指示，32bit时应为3’b010。 |
| sarc_htrans[1:0] | 输入 | 当前传输类型，IDLE，BUSY，NONSEQ，SEQ |
| sarc_hwdata[31:0] | 输入 | 写数据总线 |
| sarc_hwrite | 输入 | 高表示写传输，低表示读传输。 |
| sarc_hrdata[31:0] | 输出 | 读数据总线。 |
| sarc_hready | 输入 | 总线输出给IP的hready_in信号，用于防止总线对IP的背靠背访问。 |
| sarc_hreadyout | 输出 | 高：传输在总线上结束。<br>低：延长传输周期。 |
| sarc_hresp | 输出 | 传输响应，向Master提供传输状态信息。<br>OKAY：传输完成；<br>ERROR：传输错误； |
| sarc_hsel | 输入 | slave选择信号 |
| **ADC CORE接口** | | |

### 【右页】

| 信号 | 输入／输出 | 说明 |
|---|---|---|
| **转换控制** | | |
| sarc_d2a_adc_en | 输出 | SARADC使能信号 |
| sarc_d2a_adc_start | 输出 | SARADC启动转换信号，ADC时钟域下的脉冲信号 |
| sarc_d2a_adc_spltime_en | 输出 | SARADC增加采样时长功能控制信号 |
| sarc_d2a_adc_trig_mode | 输出 | SARADC触发模式选择信号（为常值1，仅支持单次触发模式） |
| sarc_d2a_adc_mux_se<4:0> | 输出 | SARADC单端通道选择信号 |
| ~~sarc_d2a_adc_mux_df<3:0>~~ | ~~输出~~ | ~~SARADC差分通道选择信号，mux_se为差分P端，mux_df为差分N端~~ |
| sarc_a2d_adc_data<11:0> | 输入 | SARADC输出数据信号，12bit无符号数 |
| sarc_a2d_adc_ready | 输入 | SARADC输出数据生效信号 |
| sarc_a2d_outrd_hold | 输出 | 输出5拍的窗口信息，模拟保证ready&data时序不受抢占控制拉低sarc_d2a_adc_en的控制； |
| **校正控制** | | |
| sarc_d2a_adc_gain_att | 输出 | 默认为0，默认ADC增益为1；<br>使能校正时置为1，ADC增益为(1-32/4096)。 |
| d2a_saradc_cmp_com_sel<2:0> | 输出 | SARADC0内部共模选择<br>3’b000：1.80V；<br>3’b001：1.65V；<br>3’b010：1.70V；<br>3’b011：1.75V；<br>3’b100：1.85V；<br>3’b101：1.90V；<br>3’b110：1.95V；<br>3’b111：2.00V； |
| sarc_d2a_adc_os_se_tune<3:0> | 输出 | 配置单端模式下ADC offset模拟补偿值 |
| sarc_d2a_adc_os_df_tune<3:0> | 输出 | 配置差分模式下ADC offset模拟补偿值 |
| sarc_d2a_adc_cal_se_refp_inj | 输出 | 控制ADC单端侧输入vrefp |
| sarc_d2a_adc_cal_se_refn_inj | 输出 | 控制ADC单端侧输入vrefn |
| ~~sarc_d2a_adc_cal_df_refp_inj~~ | ~~输出~~ | ~~控制ADC差分侧输入vrefp~~ |

> 转录注：sarc_hburst方向单元格原图空白；不补“输入”。sarc_a2d_outrd_hold整行为浅蓝色，虽然信号名含a2d，方向仍照录“输出”。差分相关行仅按实际删除线保留，未划去的差分描述不擅自删除。

---

## 原图：`GameViewer_XEDw3yfNAf.png`

[查看原始PNG](../images/GameViewer_XEDw3yfNAf.png)

### 【左页】

| 信号 | 输入／输出 | 说明 |
|---|---|---|
| ~~sarc_d2a_adc_cal_df_refn_inj~~ | ~~输出~~ | ~~控制ADC差分侧输入vrefn~~ |
| sarc_d2a_adc_test_sel | 输出 | ADC测试模式选择。<br>0：测试模式关闭<br>1：测试模式打开，ADC测试模式包括（ADC测量模拟内部其他待观测节点电压，DAC校正时需要ADC对其输出信号检测等） |
| sarc_d2a_adc_ibias_sel[1:0] | 输出 | ADC ibias电流调节 |
| sarc_d2a_adc_ref_mode | 输出 | SARADC0参考电压模式选择<br>1’b0：参考电压为VREFHI（3.3V或2.5V），ADC输出摆幅为3.3V或2.5V；<br>1’b1：参考电压为1.65V，ADC输出摆幅为3.3V； |
| sarc_d2a_adc_ready_sel | 输出 | SARADC0 ready时序选择信号，<br>1’b0：ready时序模拟顶层对齐模式；<br>1’b1：ready时序模拟底层对齐模式； |
| **ATE接口** | | |
| sarc_ate_data_val | 输出 | sarc_ate_data_out[11:0]的val有效信号 |
| sarc_ate_data_out[11:0] | 输出 | 采样结果经过校正后输出，ATE测试数据，u(12,0)范围0~4095 |
| **触发源接口** | | |
| sarc_trig_in<127:0> | 输入 | 128个触发源输入 |
| sarc_blk_trig_in<63:0> | 输入 | 64个blanking窗口的触发源输入 |
| **中断信号接口** | | |
| sarc_intr | 输出 | 中断输出 |
| sarc_eoc0_intr | 输出 | 完成数据转换中断0输出 |
| sarc_eoc1_intr | 输出 | 完成数据转换中断1输出 |
| sarc_eoc2_intr | 输出 | 完成数据转换中断2输出 |
| sarc_eoc3_intr | 输出 | 完成数据转换中断3输出 |
| **ADC采样触发源输出（来自EOC）** | | |
| sarc_eoc2spl_trig<1:0> | 输出 | sarc输出的2bit采样触发源信号。从16个虚拟通道的EOC中独立配置选择2bit。 |
| **看门狗接口** | | |
| sarc2etim_evt_out<3:0> | 输出 | 4bitADC上下门限检测事件输出到ETIM模块，从16个虚拟通道中独立配置选择 |

### 【右页】

| 信号 | 输入／输出 | 说明 |
|---|---|---|
| sarc2xbar_evt_out<3:0> | 输出 | 4bitADC上下门限检测事件输出到XBAR模块，从16个虚拟通道中独立配置选择 |
| **DMA握手接口** | | |
| sarc_dma_req[3:0] | 输出 | burst transfer request source<br>输出到dma_mux模块进行DMA握手处理 |
| sarc_dma_single[3:0] | 输出 | Single transfer request source<br>输出到dma_mux模块进行DMA握手处理 |
| sarc_adcevt_dma_req | 输出 | 超狗上下门限dma请求输出 |
| sarc_adcevt_dma_single | 输出 | 超狗上下门限dma请求输出 |
| sarc_dma_ack[3:0] | 输入 | dmac acknowledge signal<br>DMA应答信号，sarc模块内部不用 |
| sarc_wdt_dma_src_is_dly | 输入 | wdt_dma_src是否打拍<br>0:不打拍；（6003固定接0）<br>1:打1拍；（3101/6002C）<br>6601项目先固结0进行时序收敛，若不行在切换到固结1上。 |
| **SRAM CTRL BUS** | | |
| sysc_sarc_1rw_ctrl_bus[63:0] | 输入 | fir filter data sram ctrl bus |
| sysc_sarc_1r1w_ctrl_bus[63:0] | 输入 | fir filter parameter sram ctrl bus |
| **TESTPIN** | | |
| sarc_testpin0_sel[7:0] | 输入 | sarc_testpin0的选择信号 |
| sarc_testpin1_sel[7:0] | 输入 | sarc_testpin1的选择信号 |
| sarc_testpin2_sel[7:0] | 输入 | sarc_testpin2的选择信号 |
| sarc_testpin3_sel[7:0] | 输入 | sarc_testpin3的选择信号 |
| sarc_testpin[3:0] | 输出 | sarc_testpin测试信号输出 |
| **输出到CPU内部寄存器** | | |
| sarc2cpu_data_vld | 输出 | sarc输出有效数据指示，sarc时钟域下的单周期脉冲 |
| sarc2cpu_data[15:0] | 输出 | sarc输出数据 |
| sarc2cpu_vc_num[3:0] | 输出 | sarc输出数据所属虚拟通道指示 |

> 转录注：“超狗”“若不行在切换”是原图表述，未润色；sarc_wdt_dma_src_is_dly的6601说明为明确项目文字，未推断该选择已经完成时序验证。跨两张截图的接口表用重复表头标记来源位置，仍属4.1同一张连续表。

---

## 原图：`GameViewer_BMYV2LGXFN.png`

[查看原始PNG](../images/GameViewer_BMYV2LGXFN.png)

### 【左页】

## 4.2 SARADC 接口时序

### 采样时间

单次ADC转换中，采样最小用2.5UI，转换用13UI，打拍用0.5UI，总共16UI。这样ADC的最高采样率50M时钟为3.125MHz，66M时钟为4.125MHz。

### 接口时序

**图4-1 SARADC接口时序示意**

**图中文字转录：** clk、counter、start、spltime_en、trigger_mode、saradc_mode、mux_se[3:0]、mux_df[3:0]、sample、conversion、ready、data。

counter可辨值依次为15、0、1、……、14、15、0、1、2、……、15；saradc_mode标注se、df；mux_se标注n、n+1、n+2，mux_df标注m；spltime_en窗口标注X+1；sample第二次窗口有X；data标注x、data n、data n+1。

> ⚠️ 原图待复核：SARC-LLD-U03。spltime_en上方两行细小注释和部分波形长度小字不能逐字符确认；上列可辨值不代替完整波形，不能按正文计算来补图中文字。
> 原图：[GameViewer_BMYV2LGXFN.png](../images/GameViewer_BMYV2LGXFN.png)，左页图4-1。

### 【右页】

说明：

- 上图中，2个红色的沿和2个绿色的沿分别表示两次采样转换的开始和结束。
- 采样转换结果控制信号ready是根据start或者spltime_en的下降沿（二者较晚的一个下降沿）拉低。
- start、spltime_en信号由SARC控制器产生，通过计数器控制（计数范围为0～（15+spltime）），不与ready信号握手。
- ready信号由模拟ADC产生，在ready的上升沿将data数据拍出。
- 不增加采样时间模式下，每次采样转换固定为16个UI；增加采样时间模式下，每次采样转换时间为spltime+16UI。

> 原文差异：4.1接口表的mux_se为<4:0>，本图标注[3:0]；分别保存，不改图的位宽。图中红/绿沿在原文已说明为时序标识，不据此归为6601变更。

---

## 原图：`GameViewer_Wwj0z78cha.png`

[查看原始PNG](../images/GameViewer_Wwj0z78cha.png)

### 【左页】

# 5. 方案设计

## 5.1 SARC 整体结构

### SARC 连接关系

共有2个ADC CORE，每个ADC CORE对应1个控制器SARC，每个SARC占用一条AHB总线。结构如下：

**图5-1 SARC模块与总线和ADCCORE的连接关系**

**图中文字转录：** AHB_BRG；AHB 0、AHB 1、AHB 2；adc ctrl 0、adc ctrl 1、~~adc ctrl 2~~；adc core 0、adc core 1、~~adc core 2~~。

> 转录注：正文“2”为浅蓝色；右侧AHB 2/adc ctrl 2/adc core 2路径为浅蓝色标记，其中adc ctrl 2、adc core 2标签有删除线，按原图保留被删路径，不转成仍存在的第三个实例。

### SARC 设计框图

SARC模块整体框图如下：

### 【右页】

**图5-2 SARC模块结构框图**

**图中文字转录：**

- 外部输入与前级：capture posedge（两处）；blanking；trig mask；vc_flag_ctrl；queue_manage；sarc_conver_info_queue；digi-anal IF timing；soft_force；CALC。
- SARC 0中的可辨数据处理/缓存标签：pre-processing*16、Filter*8、dig_cal（os/gain）、reg1*16、reg2*16、hi/lo detect；新增浅蓝色ovs_ctrl、sum_ctrl、sum*8。
- 区域与外部核心：SARC 0、SARC 1、~~SARC 2~~；ADC CORE 0、ADC CORE 1、~~ADC CORE 2~~；AHB0、AHB1；ev_out。
- SARC2整块浅蓝色，区内标签、路径有删除线；SARC0新增求和相关框为浅蓝色，保留其原图位置。

> ⚠️ 原图待复核：SARC-LLD-U04。图5-2中部分细小连线名、触发源下标、trig mask框内配置全名及左侧注释尚不能逐字符确认。右上远程提示框也覆盖了图的局部，不能把弹窗文字当正文。
> 原图：[GameViewer_Wwj0z78cha.png](../images/GameViewer_Wwj0z78cha.png)，右页上方图5-2。

**capture_posedge：** 外部触发源的上升沿捕获处理。128个外部采样触发源和64个blanking触发源经过上升沿捕获处理后，每个SARC控制器单独处理。

**trig mask：** 根据配置vc_en、vc_trig_sel和vc_trig_mode来屏蔽无效的采样触发，输出16个bit的脉冲数据，代表16个VC的采样触发状态。同时该模块根据blanking机制的配置，从blanking的触发源中选择输出blanking的有效触发信号blanking_trig。

**blanking：** 实现blanking管理功能。触发经过该模块时，如果blanking_en不使能，则直接输出原触发；如果blanking_en使

> 转录注：末句跨图续接，下一张左页从“能，则输出……”继续。

---

## 原图：`GameViewer_bG98ufwLis.png`

[查看原始PNG](../images/GameViewer_bG98ufwLis.png)

### 【左页】

能，则输出blanking管理后的有效窗口标志信号。blanking窗口有效信号内，只有VC0可以正常触发采样，其它VC需要要待blanking窗口结束后再排队进行采样。

**vc_flag_ctrl：** VC转换标志管理模块。该模块根据VC的触发状态、软件启动转换状态soft_force等相关信息，管理虚拟通道VC的转换标志。VC有转换请求，其相应的vc_flag置1，否则置0。该模块输出16bit的vc_flag标志，代表16个VC的转换标志。当blanking窗口有效时，该模块只输出vc0的转换flag，待blanking窗口结束后，再输出正常操作的所有转换flag。包含一个过采样ovs_ctrl模块，当虚拟通道的启用滤波过采样求和功能时，接收外部触发，自动完成N次采样触发，根据resume/conti模式配置，并获取queue_manage输出排队信息，自动高优先级抢占情况下的恢复处理；

**queue_manage：** SARC控制器的转换队列管理模块。该模块为SYSCLK时钟域。根据digi-anal_IF_timing模块返回的计数器状态，通过VC转换标志vc_flag[15:0]、VC的优先级配置vc_priority[31:0]，输出当前有转换请求的VC中，优先级最高

### 【右页】

的一个VC编号。若开启抢占功能，当前正在转【原图被远程提示框遮挡】现p0的转换请求，输出当前p0的请求；

> ⚠️ 原图待复核：SARC-LLD-U05。右页首行从“当前正在转”后至换行前被远程提示框覆盖；只能保存上面的可见前后片段，不能用后面的优先级章节或旧转录补成完整句。
> 原图：[GameViewer_bG98ufwLis.png](../images/GameViewer_bG98ufwLis.png)，右页最上方浅蓝色段落。

**vc_flag_ctrl**模块负责触发采样、软件采样和blanking功能等处理后的最终转换请求，进行过采模式下的flag控制，抢占模式下的flag恢复。**queue_manage**模块按优先级对转换请求进行调度。两个模块将sarc的采样转换控制分成两个互不耦合的阶段。

**sarc_conver_info_queue：** 转换参数管理模块。根据queue_manage模块输出的当前优先级最高的VC编号，读取该VC的相关转换参数，输出到digi-anal_IF_timing模块。

**digi-anal_IF_timing：** 数模接口转换时序产生模块，产生ADCCORE工作的相关控制时序。

**digi_cal：** 数字域的校正处理模块。

**pre-processing：** 预处理模块、预处滤波。

**filter：** 滤波模块。

**reg1/2：** 结果缓存模块。

**sum_ctrl：** 过采求和模块；

**sum：** 求和结果输出；

> 转录注：从“包含一个过采样ovs_ctrl模块”起的段落、queue_manage的抢占续句、“进行过采模式下的flag控制，抢占模式下的flag恢复”、sum_ctrl和sum为浅蓝色。原文“需要要待”“当虚拟通道的启用”“自动高优先级……”照录，没有主观润色。

---

## 原图：`GameViewer_3VjshoX5So.png`

[查看原始PNG](../images/GameViewer_3VjshoX5So.png)

### 【左页】

说明：

- queue_manage模块在准备下一次转换通道号调度时，如果检测到blanking有效，则不启动正在排队转换的VC，需要待VC0的触发源（blanking窗口有效时的专用触发源）到来时启动VC0的转换。blanking结束后，继续执行之前的队列。

### SARC 数据流程

SARC模块转换结果数据处理流程及相关配置系数：

转换结果从ADCCORE输出，先将12bit无符号数转成12bit有符号数s(12,0)，然后将整数和小数位各扩展2bit得到s(16,2)，以此数据形式经过数字校正dig_cal、预处理pre_process和滤波处理filter，最终得到s(16,2)有符号数，将此数据通过软件配置进行定点格式转换，然后存入对应的缓存通道。

**图中文字转录（图5-3，图名在右页）：**

- 上方格式条可辨：u(12,0)；Signed A[12:0]；Signed B=A；Signed C[15:0] = B[11:0] << 2；C为s(16,2)。A对应等式和末列注释仍见U06。
- 三个虚线处理区的末端小框均为round、sat；按原图标签补录，不由运算原理反推系数。
- 分区：ADC校准参数处理；用户配置参数处理；滤波处理。
- 可辨路径标签：a2d_data_out、signed、cal_data_out、pre_data_out、filter_data_out、EVTOUT；result reg 1（16*16bit）、result reg 2（16*16bit）；sum reg（8*20bit）。
- 图中保留加法、乘法、累加、截位及格式转换方框的原始连接；新增浅蓝色求和框和sum reg标记仍由原图表达。

> ⚠️ 原图待复核：SARC-LLD-U06。图5-3中的系数全名、部分位宽/定标、signed等式和小框文字不能逐字符确认；图内数字不得由正文推导补齐。
> 原图：[GameViewer_3VjshoX5So.png](../images/GameViewer_3VjshoX5So.png)，左页底部数据流程图。

### 【右页】

**图5-3 SARC 数据流程图**

注意：

1、**s(a,b)：** 表示a bit有符号数，a为总的位宽（包括1bit符号位+整数位宽+小数位宽），b表示小数位宽；

2、**u(a,b)：** 表示a bit无符号数，a为总的位宽（整数位宽+小数位宽），b表示小数位宽；

各采样结果上报位置数据格式处理：

校准阶段上报校准寄存器结果：s(16,2)

ATE测试时输出结果：u(12,0)，范围0~4095

用户预处理后上报结果：s(16,2)；s(16,0)（寄存器实际只有s(15,0)有效，最高位均为符号位）

滤波处理后上报结果：s(16,2)，u(12,0)范围0~4095

> 转录注：以上四处结果格式在原图为红字；原文没有在这些句子中明确版本，不把普通红色强调自动归为已确认的6601新增。

## 5.2 时钟关系

SYSCLK：此时钟为SRAC控制器模块工作时钟，直接用AHB的总线时钟。

> 转录注：原文拼写为“SRAC”，保留，不自动改成“SARC”。

---

## 原图：`GameViewer_UUhaiE4moy.png`

[查看原始PNG](../images/GameViewer_UUhaiE4moy.png)

### 【左页】

ADCCLK：模拟core的工作时钟，通过SYSCLK时钟分频，最高66MHz。

中，每个ADC core的时钟ADCCLK相同，不支持独立分频。

> 转录注：“中，”前没有可见的正文词语，未凭上下文补写。

## 5.3 SARADC CALC

整体的框图，软件配合模拟/数字完成offset/gain的检测+补偿。

**图5-4 SARADC 校正整体框图**

**图中文字转录：** 模拟、数字、软件；Vrefp、Vrefn；SAR ADC；模拟内部offset补偿；模拟内部gain补偿；图中加法、乘法和后级处理方框按原图保留。

> ⚠️ 原图待复核：SARC-LLD-U07。图5-4右侧控制信号的完整拼写、系数位宽、数字域小框名称及输出下标不清楚，未从接口表类推补写。
> 原图：[GameViewer_UUhaiE4moy.png](../images/GameViewer_UUhaiE4moy.png)，左页中部图5-4。

其中数字部分，滤波器累加平均实现检测，运算后得到offset/gain的值。

检测：

滤波平均

### 【右页】

输入vrefp

\[
\mathrm{code\_refp}=(\sum_{1}^{16}\mathrm{a2d\_data\_out})\div16
\]

输入vrefn

\[
\mathrm{code\_refn}=(\sum_{1}^{16}\mathrm{a2d\_data\_out})\div16
\]

运算得到offset/gain

```text
d2soc_adc_gain_value = code_refp-code_refn
d2soc_adc_os_value = (code_refp+code_refn)/2-2048
```

### 校正流程如下

**运算，数字实现**

**单端模式运算流程：**

| 原编号 | 原文步骤 |
|---|---|
| 1 | d2a_adc_cal_se_refp_inj设置为1，配置ADC单端侧输入vrefp。 |
| 2 | d2a_adc_gain_att设置为1，配置ADC增益衰减为(1-32/4096)。 |
| 1 | ADC转换16次，对16个转换结果做累加平均，得到无符号数code_refp值。 |
| 4 | d2a_adc_cal_se_refp_inj设置为0，关掉vrefp的注入。 |
| 5 | d2a_adc_cal_se_refn_inj设置为1，配置ADC单端侧输入vrefn。 |
| 6 | ADC转换16次，对16个转换结果做累加平均，得到无符号数code_refn值。 |
| 7 | 计算得到offset/gain值d2soc_adc_gain_value/d2soc_adc_os_value |
| | 其中gain=code_refp-code_refn；offset=(code_refp+code_refn)/2-2048。 |
| 8 | d2a_adc_gain_att设置为0，关掉ADC增益衰减。 |
| 9 | d2a_adc_cal_se_refn_inj设置为0，关掉vrefn的注入。 |

> 转录注：第3个操作行在原图编号为“1”，未自动改为“3”。公式求和下标在原图仅为1，没有添加索引变量。

**差分模式运算流程：**

| 原编号 | 原文步骤 |
|---|---|
| 1 | d2a_adc_cal_se_refp_inj设置为1，配置ADC单端侧输入vrefp。<br>d2a_adc_cal_df_refn_inj设置为1，配置ADC差分端侧输入vrefn。 |

> 转录注：差分表在下一张GameViewer_QZWwXnmnv1.png左页续接第2～9步，不与校正时序图混排。虽概述说明当前不支持差分模式，原文保留的差分流程仍完整照录。

---

## 原图：`GameViewer_QZWwXnmnv1.png`

[查看原始PNG](../images/GameViewer_QZWwXnmnv1.png)

### 【左页】

**差分模式运算流程（续）：**

| 原编号 | 原文步骤 |
|---|---|
| 2 | d2a_adc_gain_att设置为1，配置ADC增益衰减为(1-32/4096)。 |
| 3 | ADC转换16次，对16个转换结果做累加平均，得到无符号数code_refp值。 |
| 4 | d2a_adc_cal_se_refp_inj/d2a_adc_cal_df_refn_inj设置为0，关掉注入 |
| 5 | d2a_adc_cal_se_refn_inj设置为1，配置ADC单端侧输入vrefn。<br>d2a_adc_cal_df_refp_inj设置为1，配置ADC差分端侧输入vrefp。 |
| 6 | ADC转换16次，对16个转换结果做累加平均，得到无符号数code_refn值。 |
| 7 | 计算得到offset/gain值d2soc_adc_gain_value/d2soc_adc_os_value |
| | 其中gain=code_refp-code_refn；offset=(code_refp+code_refn)/2-2048。 |
| 8 | d2a_adc_gain_att设置为0，关掉ADC增益衰减。 |
| 9 | d2a_adc_cal_se_refn_inj/d2a_adc_cal_df_refp_inj设置为0，关掉注入。 |

注：

1 第6步累加平均芯片内用asic实现，第7步计算offset/gain值用软件实现。

2 整体流程重复两次，第一次根据校正得到的offset补偿值，用模拟补偿的方式进行补偿。第二次根据校正得到的offset/gain补偿值，用数字补偿的方式进行补偿。

**补偿，模拟/数字实现，软件控制。**

对数字需求：

1、数字实现加法器/乘法器，根据软件配置的offset_coeff/gain_coeff系数，对ADC输出进行以下补偿，输出补偿后结果。

2、加法器/乘法器可以bypass，原始ADC输出码字直接送出来。

3、d2a_adc_gain_att模拟配置值可以软件控制。

4、d2a_adc_os_se_tune<3:0>、d2a_adc_os_df_tune<3:0>模拟补偿值可以软件配置。

### 【右页】

每个ADC均提供校准功能，包含模拟校正和数字校正，支持单端输入转换与差分输入转换校正。本版ADC支持os/gain的前台校正。在校准过程中，应用不得使用ADC，必须等待至校准完成。

ADC校准的软件流程如下：

1. 确保ADC_CTL1寄存器中~~adc_pwdn=0、~~adc_en=0。
2. 设置adc_cal_ch_mode=0（单端输入）或adc_cal_ch_mode=1（差分输入），选择此次校准的输入模式。
3. 将adc_cal_flag置1（软件置1）。
4. 软件配置cfg_sarc_adc_cal_conv_start启动校正转换，硬件上报转换结果的平均值。
5. 校正完成后，将adc_cal_flag置0（软件置0）。

此处的16次转换由硬件配置启动。

> 原文差异：“当前版本不支持差分”与本页“支持单端输入转换与差分输入转换校正”分别照录，不能据此删掉后者。adc_pwdn=0有删除线，adc_en=0没有删除线。

---

## 原图：`GameViewer_O2LOSI5xZO.png`

[查看原始PNG](../images/GameViewer_O2LOSI5xZO.png)

### 【左页】

**图5-5 校正控制说明**

**图中文字与交互转录：**

| 发起端／位置 | 原文标注 | 接收端／位置 |
|---|---|---|
| SOC | PD=0 & ADC_EN_R=0 | SARC |
| SOC | adc_cal_flag=1 | SARC |
| SARC | ADC_EN=1 | ANALOG |
| SOC | 配置转换参数 | ANALOG |
| SOC | cal_conversion_start=1 | SARC |
| SARC | 16次校正序列转换 | ANALOG |
| ANALOG | 转换结果返回 | SARC |
| SARC | 16次平均 | SARC黄色处理框 |
| SARC | cal_aver_val=1 | SOC |
| SARC | 16次转换平均值 | SOC |
| 图中黄色框 | 重复参数配置到结果返回过程 | |
| SOC黄色框 | 计算offset&gain coeff | |
| SOC | analog_os/gain_coeff | ANALOG |
| SOC | adc_cal_flag=0 | SARC |

> 转录注：此表仅将图内可辨交互转成文字，列标题是转录辅助；原时序/虚线与布局保留在原图。PD=0与上一页被删除的adc_pwdn=0不互相替换。

### 【右页】

**图5-6 校正状态机**

初始节点指向CAL_IDLE。

| 当前状态 | 原图条件 | 下一状态 |
|---|---|---|
| CAL_IDLE | adc_en_r==0 && adc_cal_flag==1 | CAL_START |
| CAL_START | cal_conv_start==1 | CAL_CONV |
| CAL_CONV | cal_conv_done==1 | CAL_AVER |
| CAL_AVER | adc_en_r==0 && adc_cal_flag==1 | CAL_START |
| CAL_AVER | adc_en_r==1 &#124;&#124; adc_cal_flag==0 | CAL_IDLE |

**注意：此处需要补充DAC校正需求和流程，以及ADC需要配合的工作。**

> 转录注：最后的“需要补充”是原作者待办，本次仅照录，不自行编写DAC校正需求。该图四个状态和五个条件按原图保存，不用代码执行结果替代图中文字。

---

## 原图：`GameViewer_CCQu4ftpmA.png`

[查看原始PNG](../images/GameViewer_CCQu4ftpmA.png)

### 【左页】

#### 5.4 外部触发源

外部共有128个采样触发源和64个blanking触发源（含reserved位域），每个ADC控制器支持16个虚拟通道VC0-VC15。

SARC的采样触发源如下：

见SARC模块LRS文档触发源说明

个SARC的blanking触发源如下：

见SARC模块LRS文档触发源说明

对外部输入触发源，先在sarc_wrap进行取上升沿操作处理后送入对应的sarc_core，再根据16个VC的使能配置、触发源选择配置及触发模式配置，屏蔽无效触发源，产生16个VC对应的16bit有效触发源。

blanking触发源的处理类似采样触发源。

**图5-7 外部触发源处理**

图中文字转录：输入`trig_in[127:0]`，依次经`Capture posedge`、`trig mask`，输出`trig_masked[15:0]`。`trig mask`框内三行：`ADC_VCx_CTL.VC_EN`、`ADC_VCx_CTL.TRIG_SEL`、`ADC_VCx_CTL.TRIG_MODE`。

> 转录注：“个SARC的blanking触发源如下”开头的“个”为原图正文，未当作水印删除；本页64个blanking触发源与LRS触发表的数量不在此擅自统一。

### 【右页】

#### 5.5 触发模式

| 模式 | 说明 |
|---|---|
| 单次触发模式 | VC一次配置只触发一次转换，VC_EN打开一次只响应一次触发 |
| 连续触发模式 | VC一次配置可多次触发转换，VC_EN打开时，可连续响应多次触发 |

> 转录注：以上为原图两行无独立表头的对照表；“模式／说明”为转录列名。

##### 单次触发模式

单次触发模式：虚拟通道每次配置生效后，只响应一次触发。

要求软件每次配置通道前将对应的虚拟通道使能vc_en关闭，待配置完成后再打开，硬件通过vc_en的上升沿动作来产生虚拟通道重新配置参数的标志。

检测到该虚拟通道配置且VC_EN有效，ONE_SHOT_EN置1，等待该虚拟通道的触发。

检测到触发TRIG且ONE_SHOT_EN为高，将VC_FLAG置1，同时将ONE_SHOT_EN置0。

待该虚拟通道获得优先级后，开始启动转换操作。

注意：在单次触发模式下，当VC的触发产生时，如果对应的ONE_SHOT_EN信号为低，此时不能将对应的VC_FLAG置1，即该VC不响应本次触发。

---

## 原图：`GameViewer_NaOtfAzWwn.png`

[查看原始PNG](../images/GameViewer_NaOtfAzWwn.png)

### 【左页】

**图5-8 单次触发模式时序示意**

图中文字转录：`VC_EN`、`CONFIG`、`TRIG`、`ONE_SHOT_EN`、`VC_FLAG`、`SARC_START`；配置标记`config A`、`config B`；两段标记`1`、`2`；第三次触发旁标注`not conversion`。波形边沿及间隔见原图。

##### 连续触发模式

连续触发模式：虚拟通道配置完成且使能打开后，可以重复生效等待触发事件来临，直至软件配置虚拟通道使能关闭。

在连续触发模式下，只要VC_EN有效，在检测到该虚拟通道的触发TRIG时，就将该VC_FLAG置1。

待该虚拟通道获得优先级后，开始启动转换操作。

### 【右页】

**图5-9 连续触发模式时序示意**

图中文字转录：`VC_EN`、`CONFIG`、`TRIG`、`VC_FLAG`、`START`；配置标记`config A`；两段标记`1`、`2`。本图末路信号原名为`START`，不与图5-8的`SARC_START`自动改成同名。

#### 5.6 blanking机制

每个SARADC控制器中包含Blanking管理模块，支持一个Blanking事件，可以对非VC0的采样触发信号进行延迟Blanking操作，该功能可屏蔽。仅虚拟通道0支持Blanking管理。实现VC0的周期性等间隔采样功能。

Blanking支持2类触发源：eTimer/SuperPWM。

blanking的触发延迟时间可配置，且对所有blanking触发源统一配置，为16bit，SYSCLK计数器。

对所有blanking触发源，blanking窗口长度相同且可配置，为16bit，SYSCLK计数器。

---

## 原图：`GameViewer_a0rP8s7Oan.png`

[查看原始PNG](../images/GameViewer_a0rP8s7Oan.png)

### 【左页】

blanking窗口内虚拟通道0的触发（专用周期触发源）可以正常响应，窗口内若出现其他虚拟通道的触发信号，记录该虚拟通道被触发的行为但不响应，待blanking窗口结束后，再按各自优先级进行排队响应。

若Blanking窗口未结束，其他触发信号（非专用周期触发）出现重复触发，上报告警，并忽略该重复触发（blanking窗口内非VC0的触发信号只记录一次）。

blanking机制的基本原理如下图：

**图5-10 blanking机制原理示意**

图中文字转录：`Blanking trig`、`Blanking延迟触发`、`Blanking窗口`、`vc0触发源`、`其他vc触发源`。图中☆表示vc0触发源，○、□、△分三行标记其他触发源。

图右两条说明：

- blanking窗口结束后，根据优先级，响应○□△各一次。
- blanking窗口内○□△出现重复触发，产生告警。

### 【右页】

**图5-11 blanking机制**

时序示意图

图中文字转录：`clk`、`blanking_en`、`blanking_trig`、`blanking_flag`、`blanking delay`、`blanking window len`。周期编号、波形边沿与双向区间箭头保留在原图。

**图5-12 blanking模块状态转移**

| 状态 | 框内原文 |
|---|---|
| BLANK_IDLE | wait for en && trig |
| BLANK_DELAY | trig delay |
| BLANK_WORK | generate blank valid window |

| 转移 | 原图条件 |
|---|---|
| 起始节点→BLANK_IDLE | 起始箭头未附文字 |
| BLANK_IDLE→BLANK_DELAY | `blank_en_r==1 && blank_trig==1` |
| BLANK_DELAY→BLANK_WORK | `delay_cnt==blank_delay_r` |
| BLANK_WORK→BLANK_IDLE | `win_cnt==blank_len_r` |

> 转录注：以上两个表为原图状态和箭头文字的转录；未补原图未写出的异常路径或计数规则。

---

## 原图：`GameViewer_40i6eF4ZKV.png`

[查看原始PNG](../images/GameViewer_40i6eF4ZKV.png)

### 【左页】

#### 5.7 优先级队列管理

队列管理模块实现16个虚拟通道VC的转换序列调度管理。

vc_flag_in[15:0]为vc_flag_ctrl模块输出，指示虚拟通道（vc15-vc0）的转换请求标志，1表示对应虚拟通道有转换请求，0表示无请求。

vc_priority[31:0]为虚拟通道（vc15-vc0）的优先级指示，每个虚拟通道2bit表示。

vc_num[3:0]为优先级队列管理模块输出，指示下一个启动转换的虚拟通道VC编号，即输出当前优先级最高的虚拟通道编号。

vc_num_val为优先级队列管理模块输出有效指示，指示输出的vc_num[3:0]虚拟通道编号有效。

none_flag指示当前没有需要转换的队列，所有触发转换完成。该信号高电平有效，为0表示还有队列需要转换。

preemtive_md：p0优先级抢占模式指示，1为p0可抢占模式，0为不可抢占模式；

> 变更标记：最后一段为浅蓝色；`preemtive_md`照录原文拼写，不按英文常识补入字母。

### 【右页】

priority_conflict：抢占模式开启下的优先级指示，1指示优先级冲突，当前存在p0优先级请求，需由外部的请求处理模块重发vc_num_req完成处理后，才会拉低；未开启抢占功能时一直为0；

> 变更标记：以上整段为浅蓝色。

**图5-13 优先级队列管理**

图中文字转录：中心`vc_queue`；左侧输入`vc_flag_in[15:0]`、`vc_priority[31:0]`、`vc_num_req`、`preemtive_md`；右侧输出`vc_num[3:0]`、`vc_num_val`、`none_flag`、`priority_conflict`。其中`preemtive_md`和`priority_conflict`为浅蓝/清绿文字，分别位于输入侧和输出侧。

#### 5.8 ADC同步模式

同步采样：多个ADCCORE同时采样不同信号源。

冗余采样：多个ADCCORE同时采样相同信号源。

由于ADC的触发源选择独立，故在实现ADC同步模式时，需要软件保证将参与同步模式的ADC配置为相同的采样触发信号源。

ADC同步并联模式下，软件在启动同步采样转换时，要确保当前参与同步采样的ADC CORE都处于IDLE状态。

---

## 原图：`GameViewer_NwJydpcqGX.png`

[查看原始PNG](../images/GameViewer_NwJydpcqGX.png)

### 【左页】

ADC同步并联模式下，ADC CORE的采样保持时间、触发模式（单次或连续）需要保持一致。

**同步采样**

图中文字转录：公共`ADCCLK`；上组`ADC0.START`、`ADC0.SPLTIME_EN`、`ADC0.SH`、`ADC0.CONVERSION`、`ADC0.VC_CH`、`ADC0.READY`；下组`ADC1.START`、`ADC1.SPLTIME_EN`、`ADC1.SH`、`ADC1.CONVERSION`、`ADC1.VC_CH`、`ADC1.READY`。两组通道值分别为`channel n`和`channel m`；顶部段标记`1`、`2`。

同步采样：多个CORE同时采样不同信号源

### 【右页】

**冗余采样**

图中文字转录：公共`ADCCLK`；上组`ADC0.START`、`ADC0.SPLTIME_EN`、`ADC0.SH`、`ADC0.CONVERSION`、`ADC0.VC_CH`、`ADC0.READY`；下组`ADC1.START`、`ADC1.SPLTIME_EN`、`ADC1.SH`、`ADC1.CONVERSION`、`ADC1.VC_CH`、`ADC1.READY`。两组通道值均为`channel n`；顶部段标记`1`、`2`。

冗余采样：多个CORE同时采样相同信号源

> 转录注：本张两幅时序图未见独立图号，不根据相邻图号补造编号。全部边沿、周期对齐和采样区间以原图为准。

---

## 原图：`GameViewer_Pv1TFSu3Dw.png`

[查看原始PNG](../images/GameViewer_Pv1TFSu3Dw.png)

### 【左页】

#### 5.9 软件直接触发采样

在SARADC控制器使能打开的前提下，无论虚拟通道是否配置了相应的触发源，且无论相应的触发源是否产生，软件通过对相应寄存器置位，可以触发启动对应虚拟通道进行采样转换。软件向置位寄存器ADC VC Force Register(ADC_VC_FRC)写1来实现，该寄存器硬件自清零。

该寄存器有16个有效bit位，分别对应16个虚拟通道，指示对应虚拟通道通过软件启动转换开始标志。该寄存器相应bit位写1会强制将ADC_VC_FLG寄存器的对应位置1，用于软件控制启动转换。该位写0无效，该位软件读操作返回0。

在同一时钟cycle，如果软件set此位，同时硬件clear ADC_VC_FLG寄存器的对应位，则软件set的优先级高，即ADC_VC_FLG寄存器对应位响应软件set，此时ADC_VC_OVF寄存器（虚拟通道启动转换溢出标志）的对应bit位不受影响。

例如软件配置ADC_VC_FRC寄存器为0x000F，在SARADC控制器使能打开的前提下，则ADC_VC_FLG寄存器中VC0、

### 【右页】

VC1、VC2、VC3对应位置1，即该4个虚拟通道被软件强制触发，然后根据对应优先级进行排队转换。

> 转录注：以上两页为同一句连续举例；没有将“VC0、”后的VC1～VC3丢弃或单独改写。

**图5-19 软件直接触发采样**

图中文字转录：`软件配置`→`ADC_VC_FRC`→`硬件操作`；软件配置框由左至右为`… 1 1 1 1`，下标为`VC3 VC2 VC1 VC0`。右上`ADC_VC_FLG`框为`… 1 1 1 1`，下标`VC3 VC2 VC1 VC0`，右箭头`排队转换`；右下`ADC_VC_FRC`框为`… 0 0 0 0`，下标`VC3 VC2 VC1 VC0`。

还支持另一软件触发，软件通过配置CFG_SARC_VC_SOFT_TRIGER.cfg_sarc_vc_soft_trigger[15:0]；该触发脉冲在触发选择列表上，触发功能需经过触发选择，与其它硬件触发源的功能类似；

> 变更标记：以上“还支持另一软件触发”整段为浅蓝色。原寄存器名`SOFT_TRIGER`只有一个G，字段名`soft_trigger`有两个g，各自照录，不自动统一。图5-19中的普通色块另保留原图，不仅因着色便推断新增寄存器。

#### 5.10 SARADC控制时序

转换控制模块，根据时序和队列状态，向队列管理模块申请转换出队，然后根据出队虚拟通道号及相应的转换配置参数，产生相应的数模接口信号输出到模拟ADC控制采样转换。

---

## 原图：`GameViewer_sKXvcDs2Yn.png`

[查看原始PNG](../images/GameViewer_sKXvcDs2Yn.png)

### 【左页】

**图5-15 采样转换控制状态机示意**

| 状态 | 原图框内说明 |
|---|---|
| SAMPLE_IDLE | do nothing |
| SAMPLE_PRE | empty jump |
| SAMPLE_START | begin sample |
| SAMPLE_CONTI | keep sample |

| 转移 | 原图条件 |
|---|---|
| 起始节点→SAMPLE_IDLE | 起始箭头未附文字 |
| SAMPLE_IDLE→SAMPLE_IDLE | `none_flag==1` |
| SAMPLE_IDLE→SAMPLE_PRE | `none_flag==0` |
| SAMPLE_PRE→SAMPLE_START | 箭头未附文字 |
| SAMPLE_START→SAMPLE_IDLE | `vc_num_val==0` |
| SAMPLE_START→SAMPLE_CONTI | `vc_num_val==1` |
| SAMPLE_CONTI→SAMPLE_CONTI | `adc_cnt<adc_spltime+13` |
| SAMPLE_CONTI→SAMPLE_PRE | `adc_cnt>=adc_spltime+13 && none_flag==0` |
| SAMPLE_CONTI→SAMPLE_IDLE | `adc_cnt>=adc_spltime+13 && none_flag==1` |

### 【右页】

**图5-16 触发采样时序图**

图中文字转录，信号自上而下：`clk_sarc`、`clk_adc`、`trig_in`、`trig`、`vc_trig`、`vc_flag`、`none_flag`、`vc_num_req`、`vc_num_val`、`vc_num_o`、`vc_num_d`、`adc_start`、`adc_start_1d`、`adc_start_2d`、`pos_vc_num`、`adc_cnt`。

`vc_num_o`、`vc_num_d`、`pos_vc_num`的数据框标为`vc_num`；`adc_cnt`的数据依次显示`'H0`、`'H1`、`……`、`'HD`、`'HE`、`'HF`、`'H0`、`'H1`。各信号边沿及对齐关系保留在原图。

> 原文差异：此前软件触发图编号为5-19，本张又为5-15/5-16。按正文阅读次序保存，不按图号重排或补造5-14。

---

## 原图：`GameViewer_ba6sdetThH.png`

[查看原始PNG](../images/GameViewer_ba6sdetThH.png)

### 【左页】

**图5-17 数模接口信号时序示意**

图中文字转录：`clk`、`counter`、`start`、`spltime_en`、`trigger_mode`、`saradc_mode`、`mux_se[3:0]`、`mux_df[3:0]`、`ready`、`data`。采样和转换区间的两个小框分别为`sample`、`conversion`（第九轮按原图字形补录）。

可辨值及区间标记：`saradc_mode`为`se`、`df`两段；`mux_se[3:0]`标`n`、`n+1`、`n+2`；`mux_df[3:0]`中间段为`m`；采样延长段为`X+1`；数据段标`data n`、`data n+1`。`counter`可辨的前段为15、0、1，后续含14、15、0、1、2；省略点和波形边界仍见原图。

> ⚠️ 原图待复核（SARC-LLD-U08）：`sample`、`conversion`已在第九轮补录；`spltime_en`上方两行极小注释及部分区间数值仍无法从当前截图逐字符确认。可辨片段包含`spltime_en`、`X+1`，没有补成确定的完整说明句。
> 原图：[GameViewer_ba6sdetThH.png](../images/GameViewer_ba6sdetThH.png)，左页图5-17。

### 【右页】

**图5-18 一次采样转换控制时序示意**

图中文字转录，自上而下：`ADCCLK`、`PD`、`saradc_en`、`saradc_start`、`S/H`、`coversion`、`adc_spltime_en`、`saradc_trigger_mode`、`saradc_mode`、`saradc_mux_se<3:0>`、`saradc_mux_df<3:0>`、`saradc_ready`、`saradc_data`、`trig`、`VC0.FLAG`、`VC1.FLAG`。

顶部六段标记`1`～`6`。`saradc_mux_se<3:0>`依次标`'H0`、`channel n`、`channel m`；`saradc_mux_df<3:0>`标`'H0`；数据框标`old data`、`result n`、`result m`。

> 转录注：原图拼写`coversion`照录，不自动改成conversion。波形箭头、对齐和区间长度以原图为准，不自行解释六段所代表的额外阶段。

---

## 原图：`GameViewer_LoWatHzLVG.png`

[查看原始PNG](../images/GameViewer_LoWatHzLVG.png)

### 【左页】

#### 1.1.1 抢占功能

图中文字转录：`vc_flag_ctrl`、`vc_queue`、`sarc_smaple_ctrl`、`模拟ADC`；信号`vc_flag[15:0]`、`none_flag`、`priority_cnflt`、`vc_num_req`、`vc_num/val`、`start/en`。图中浅蓝回接线由右侧返回`vc_flag_ctrl`，`priority_cnflt`箭头为浅蓝色；没有为未标名的回接线补造信号名。

抢占功能控制如下：

1. 由vc_queue模块完成识别vc_flag_ctrl输入的vc_flag[15:0]中的优先级冲突，~~包含blanking情况的冲突，~~判定当前队列优先级和当前输出的vc_num的优先级是否冲突，输出priority_cnflt信号；
2. sarc_sample_ctrl模块识别到priority_cnflt信号，根据priority_cnflt的时机进行不同的时序控制：：

   ii. 可直接进行抢占；

[本页左下抢占时序原图](../images/GameViewer_LoWatHzLVG.png)

需delay发起抢占(不区分队列是否存在其它请求，统一delay)；

> 变更标记：本页“抢占功能控制如下”至“统一delay”为浅蓝文字；“包含blanking情况的冲突”在浅蓝文字上带删除线，必须保留删除性质。图中模块名为`sarc_smaple_ctrl`，正文为`sarc_sample_ctrl`，各自照录。原编号`1.1.1`、`ii.`及连续两个冒号均保留。

### 【右页】

[本页右上抢占时序原图](../images/GameViewer_LoWatHzLVG.png)

若抢占发生在连续两笔转换的交接区，需输出sarc_a2d_outrd_hold使模拟保证不影响第一次的ready&data的返回时序；

[本页右中交接区抢占时序原图](../images/GameViewer_LoWatHzLVG.png)

时序图原文件：ET6601-DOC\05.数字设计\03%20HAC\SARC\V100\01.需求分析\02.需求分析\抢占控制.xlsx

**图5-18 采样抢占时序图**

1. 模拟接收抢占控制，完成采样转换后返回高优先级对应的ready及data信息；
2. vc_flag_ctrl接收该ready信号，priority_conflt，start信号；

   a) 发出start后清除vc_flag；

   b) 若期间因抢占导致该对应的start无法返回ready，需重新将vc_flag拉起；

   c) 使用对应返回的ready指示该vc_flag的完整结束；

> 变更标记：本页可辨正文、文件路径和后续条目均为浅蓝色。后半段原文`priority_conflt`与前半段`priority_cnflt`不同，不统一拼写。原图号5-18与前一张一次采样图重复，分别保留。

> ⚠️ 原图待复核（SARC-LLD-U09）：本张共三处嵌入的电子表格时序片段；可辨`clk`、`start`、`ready`等标签和分组波形，但完整行名、细小注释、周期列数及色块精确起止仍不能逐项确认。它们没有被替换成推测的时序表，也未被省略为无来源的空白；全部保留在本张原图中。
> 原图：[GameViewer_LoWatHzLVG.png](../images/GameViewer_LoWatHzLVG.png)，左下、右上和右中三处。

> 同源范围核查：辅助目录`抢占功能.png`虽有同主题框图，但其回线明确标`ready`、输出为`start`，与本页的多条回接线及`start/en`不同，不能直接代替本页框图或用来补上时序片段的小字。

---

## 原图：`GameViewer_mjeYzTB3j7.png`

[查看原始PNG](../images/GameViewer_mjeYzTB3j7.png)

### 【左页】

#### 5.11 触发采样延时捕获

该功能为6002新增。

每个ADC控制器支持基于虚拟通道进行Trigger-to-sample延迟计算，并上报延迟时间（SYSCLK周期计数）；

延迟时间为收到有效触发到采样开始的时间，每个虚拟通道独立上报。

每个ADC控制器有一个基于SYSCLK的全局12bit free-run计数器，最大可计4096个SYSCLK时钟周期，该计数器的值软件可实时读取。

**注意：当Trigger-to-sample的延迟时间超过4096个周期时，会上报错误的延迟时间值。**

当收到采样触发时，锁存触发时刻计数值REQSTAMP上报，用该触发的采样开始时刻（adc_start的上升沿）计数器值减去REQSTAMP，将得到的差值DLYSTAMP锁存上报。

当由于p0优先级抢占发生时，低优先级会在第二次采样开始时更新DLYSTAMP值；

> 变更标记：最后一段为浅蓝色；前文明确“6002新增”属于历史功能，不冒充ET6601新增。

### 【右页】

过采样启用时，该延时捕获仅在过采样的第一次开始时锁存延迟值；

> 变更标记：以上整句为浅蓝色，接续左页抢占后的延时捕获说明。

**图5-19 Trigger-to-sample时序示意**

图中文字转录：`adc_trig`、`adc_start`、`free-run counter`；时刻标记`REQSTAMP`、`SPLSTAMP`；区间标记`DLYSTAMP (SPLSTAMP-REQSTAMP)`。计数框依次可见`0 1 2 3 4 5 6 7 8`，折断线后为`4091 4092 4093 4094 4095 0 1`；不补出被折断的整段数列。

#### 5.12 采样结果校准补偿

每个ADC采样结果统一校准补偿，不区分虚拟通道。（模拟ADC偏置s(5,0)和增益u(14,12)）。

**图5-19 采样结果校准**

图中文字转录：`ADC校准参数处理`；主路径`a2d_data_out`→`signed`→加法节点→乘法节点→`round`→`sat`→`cal_data_out`。虚线框标签`dig_cal`。

可辨控制与格式：`cal_offset`、`cal_gain/4096`、`5bit signed`、`14bit unsigned`；输入`u(12,0)`，signed后和加法后均为`s(16,2)`，偏置`s(5,0)`，增益`u(14,12)`，乘法后`s(30,14)`，round后`s(18,2)`，输出`s(16,2)`。

图中`signed`下方两行说明补录：整数小数位各扩展2bit为s(16,2)，以此作为后续计算基础，得到结果定点s(16,2)。增益顶部范围为`0~4`。

> ⚠️ 原图待复核（SARC-LLD-U10）：第九轮已补两行中文及增益范围；5bit signed下方偏置范围的前导符号仍不够清晰，范围数值不以位宽推导填写。辅助图的15bit版本未用于替换此处5bit版本，U10暂不整组关闭。
> 原图：[GameViewer_mjeYzTB3j7.png](../images/GameViewer_mjeYzTB3j7.png)，右页底部。

> 原文差异：本张两幅图都标为5-19，且前面的软件触发图也为5-19；按原文分别保留，不重编号。

---

## 原图：`GameViewer_UFTfaW6Wm8.png`

[查看原始PNG](../images/GameViewer_UFTfaW6Wm8.png)

### 【左页】

#### 5.13 用户预处理补偿

用户预处理补偿有16个通道，与虚拟通道一一对应。（用户配置偏置s(16,2)和增益s(15,12)）。

6002相对于6001修改点：pre_gain参数格式由u(14,12)修改为s(15,12)。

**图5-20 用户预处理补偿**

图中文字转录：标题“用户配置参数处理”；虚线框`pre_process`。`cal_data_out`经加法、乘法、`round`、`sat`后输出`pre_data_out`。加法输入`pre_offset`，标注`16bit signed`、`s(16,2)`；乘法输入`pre_gain/4096`，标注`15bit signed`、`-4~4`、`s(15,12)`。

| 位置 | 原图定标 |
|---|---|
| cal_data_out／加法输出 | s(16,2) |
| 乘法输出 | s(31,14) |
| round输出 | s(19,2) |
| sat输出／pre_data_out | s(16,2) |

#### 5.14 预处理滤波通道

每个SARC包含有8个通道的预处理滤波通道，可以通过配置寄存器将16个预处理通道映射到这8个预处理滤波通道（映射方式与6002中滤波器通道的映射方式类似）。每个预处理滤波通道可以配置为1~4阶的iir滤波（直接1型）或者1~8阶的fir滤波器。

### 【右页】

##### 5.14.1 FIR滤波器

\[
Y=B*X \tag{5-1}
\]

\[
y_n=2^R\times\sum_{k=0}^{N}b_kx_{n-k}\tag{5-2}
\]

该功能执行长度为N+1的向量B与不定长度的向量X的卷积。Y中每次增加的元素y_n都是用点积来计算的：y_n=B*X_n，其中X_n=[x_{n-N},...,x_n]由N+1个X中的元素组成。

该功能对应于有限脉冲响应（FIR）滤波器，其中向量B包含滤波器系数，向量X包含输入数据，R为滤波器输出的缩放因子。

FIR滤波器的结构如下图所示。

> 转录注：本页“6002相对于6001”是原作者写出的历史版本差异，不转称ET6601新增。

---

## 原图：`GameViewer_Ef2CwLAmR0.png`

[查看原始PNG](../images/GameViewer_Ef2CwLAmR0.png)

### 【左页】

**图5-x FIR滤波器的结构**

图中文字转录：输入`x[n]`，延迟链标签`x[n-1]`、`x[n-2]`、`x[n-3]`、`x[n-N]`；系数`b[0]`、`b[1]`、`b[2]`、`b[3]`、`b[N]`；延迟单元`z⁻¹`，乘法节点`×`、加法节点`+`，末端乘以`2^R`输出`y[n]`。图中省略号保留为原图中的省略号，未擅自展开中间级数。

##### 5.14.1 IIR滤波器（直接1型）

\[
Y=B*X+A*Y\tag{5-3}
\]

\[
y_n=2^R\left(\sum_{k=0}^{N}b_kx_{n-k}+\sum_{k=1}^{M}a_ky_{n-k}\right)\tag{5-4}
\]

### 【右页】

这个功能实现了一个无限脉冲响应(IIR)滤波器。滤波器输出向量Y是长度为N+1的系数向量B和不确定长度的向量X的卷积，加上延迟输出向量Y'与长度为M的第二个系数向量A的卷积。Y中每次新增的元素：y_n=B*X_n+A*Y_{n-1}，其中X_n=[x_{n-N},...,x_n]由N+1个X中的元素组成，Y_{n-1}=[y_{n-M},...,y_{n-1}]由M个Y中的元素组成。

IIR滤波器（直接1型）的结构如下图所示。

**图5-x IIR滤波器（直接1型）的结构**

图中文字转录：输入`x[n]`，前向系数`b[0]`、`b[1]`、`b[2]`、`b[3]`、`b[N]`，前向延迟单元`z⁻¹`；输出`y[n]`，反馈系数`-a[1]`、`-a[2]`、`-a[3]`、`-a[M]`，反馈延迟单元`z⁻¹`；前向延迟标签`x[n-1]`、`x[n-2]`、`x[n-3]`、`x[n-N]`，反馈延迟标签`y[n-1]`、`y[n-2]`、`y[n-3]`、`y[n-M]`；图中有`×`、`+`、`2^R`以及中间级省略号。

> 转录注：本页IIR标题确为重复的“5.14.1”，图号确为“5-x”。公式的加号与图内反馈系数的负号分别保留，不据公式知识改写任一处。本页承接上一张FIR末句；超门限检测续页不应插入此处。

---

## 原图：`GameViewer_vZO2NlUXdv.png`

[查看原始PNG](../images/GameViewer_vZO2NlUXdv.png)

### 【左页】

##### 5.14.3 预处理滤波通道的实现结构

###### 5.14.3.1 滤波器通道的参数配置

1、fir和iir的实现复用同一种结构，通过配置参数cfg_pflt_type来区分滤波器的类型（0：fir；1：iir）；

2、通过参数cfg_p_arg和参数cfg_q_arg来区分滤波器器的阶数；cfg_p_arg为滤波器前馈系数的个数，等于fir的阶数+1；cfg_q_arg为滤波器反馈系数的个数，等于iir的阶数，当滤波器配置为fir时，cfg_q_arg应该等于0；

3、cfg_pflt_coeff[x]（x=0~8）为滤波器的系数，16bit有符号数，前面部分为前馈系数，后面部分为反馈系数，配合cfg_p_arg和cfg_q_arg使用；

4、cfg_pflt_p_num为滤波器的通道编号，当通道编号与滤波器的通道对应时，并且cfg_pflt_rdy==1（滤波器参数在影子寄存器种准备好时），同时flt_cal_en==0（该通道的滤波器没有在运算时），可将影子寄存器中的参数刷新到对应滤波通道的活动寄存器。

### 【右页】

待滤波通道的参数切换完成后，内部硬件自动清除cfg_pflt_rdy寄存器。

**图5-x 滤波器通道参数配置**

| 左侧配置寄存器列 | 右侧活动寄存器列 |
|---|---|
| cfg_pflt_coeff[0] | flt_coeff[0] |
| cfg_pflt_coeff[1] | flt_coeff[1] |
| …… | …… |
| cfg_pflt_coeff[n] | flt_coeff[n] |
| cfg_pflt_p_arg | p_arg |
| cfg_pflt_q_arg | q_arg |
| cfg_pflt_num | 原图此行无对应右侧行 |
| cfg_pflt_type | flt_type |
| cfg_pflt_rdy | 原图此行无对应右侧行 |

> 转录注：上表只是分别列出两列的标签；不表示两侧原本不存在的一一连线。

图中两段原文：

当cfg_pflt_rdy==1&&(flt_cal_en==0)，并且cfg_pflt_num等于预处理滤波器通道的编号时，ids中滤波器的系数等参数会加载到预处理滤波器的内部寄存器，实现滤波器参数切换

滤波器参数切换完成后，硬件会自动拉低ids的cfg_pflt_rdy

###### 5.14.3.2 滤波器的输入数据增益调整

为了适用不同的场景，需要对预处理滤波通道的输入数据进行缩放（通过左移或者右移实现），缩放的范围为：-1~2（负数表示左移，正数表示右移）。如下图所示。

> 转录注：正文cfg_pflt_p_num和图中cfg_pflt_num、正文cfg_p_arg/cfg_q_arg与图中cfg_pflt_p_arg/cfg_pflt_q_arg的差别均按原文保留，不自动重命名。跨页“活动寄／存器”在此连续衔接。

---

## 原图：`GameViewer_PecSuT1xBB.png`

[查看原始PNG](../images/GameViewer_PecSuT1xBB.png)

### 【左页】

**图5-x 输入数据增益调整**

图中选择信号：`cfg_pflt_idat_gain_adj[1:0]`。四路输入原文如下。

| 选择值 | 输入拼接式 |
|---|---|
| 0 | `{pre_data_in[15:0],3'd0}` |
| 1 | `{{1{pre_data_in[15]}},pre_data_in[15:0],2'd0}` |
| 2 | `{{2{pre_data_in[15]}},pre_data_in[15:0],1'd0}` |
| 3 | `{{3{pre_data_in[15]}},pre_data_in[15:0]}` |

图中文字转录：多路选择输出`19bit`，经`round`得到`17bit`，经`sat`输出`flt_dat_in[15:0]`。选择值的蓝色仅在此记录为图中文字颜色，未按四项独立新增功能计数。

###### 5.14.3.3 滤波器的输入数据和运算结果缓存

1、当滤波器通道配置为fir滤波器时，滤波器的输入数据需要根据阶数进行缓存，待后面的滤波运算使用。当滤波器的flt_dat_vld==1时，将所有的输入数据（包含最近的cfg_p_arg个输入数据）向后移动一个寄存器，最旧的数据不再需要，所以被丢弃。

2、当滤波器通道配置为iir滤波器时，滤波器的输入数据和输出结果都需要根据阶数进行缓存，前cfg_p_arg个寄存器缓存最新的cfg_p_arg个输入数据。后cfg_q_arg个寄存器缓存cfg_q_arg个最新的输出结果，用于反馈支路的运算，最旧的数据不再需要，所以被丢弃。

### 【右页】

3、当配置cfg_pflt_buf_clr==1（软件写清信号）时，输入数据和运算结果缓存可以被清除；当加载新的滤波器参数时，可以通过配置cfg_pflt_rdy_buf_clr_sel寄存器来选择是否需要清除输入数据和运算结果缓存。

**图5-x 输入数据和运算结果的缓存**

图中文字转录：分为`j==0`、`j>0`两组；可辨标签包括`flt_cal_dat_pre[j][15:0]`、`flt_dat_in[15:0]`、`16'd0`、`flt_cal_dat_o[15:0]`、`flt_dat_in_vld==1`、`flt_cal_en`、`flt_ch_num`、`flt_ch_vld`、`flt_buf_clr`。补录下组的两个相邻输入标签：`flt_cal_dat_pre[j-1][15:0]`、`flt_cal_dat_pre[j+1][15:0]`。寄存器、MUX、反馈和清除连线仍见原始PNG；未清楚的选择条件保持U11。

> ⚠️ 原图待复核（SARC-LLD-U11）：两组buffer图顶部清除逻辑的完整布尔表达式、部分MUX选择条件及细小数组下标，不能从当前截图逐字符确认。已保留可辨标签，不按buffer工作原理补全逻辑。
> 原图：[GameViewer_PecSuT1xBB.png](../images/GameViewer_PecSuT1xBB.png)，右页两组buffer图。

###### 5.14.3.4 滤波器运算的数据流图

1、滤波器的本质为乘加运算，在实现过程中用内部计数器来控制输入数据和滤波器参数的乘加，乘法起的位宽为

> 转录注：本页“乘法起”为原图文字；该句直接续接下一张左页的“16bit*16bit”，不在中间插入其他章节。

---

## 原图：`GameViewer_SeEx4da40l.png`

[查看原始PNG](../images/GameViewer_SeEx4da40l.png)

### 【左页】

16bit*16bit，中间累加器的位宽为27bit，中间累加器溢出时可以选择wrap或者saturate（通过寄存器cfg_pflt_clip选择），同时会上报溢出状态到上预处理滤波器通道的上报寄存器；

2、滤波器的运算结果可以通过cfg_pflt_r_arg寄存器进行缩放，缩放之后的结果可以通过cfg_pflt_acc_out_wrap_sel寄存器进行saturate或者wrap到16bit数据输出；

3、在实现时，数据流图中乘法器、加法器、累加结果寄存器等资源将与用户预处理补偿模块复用；

### 【右页】

**图5-x 滤波器运算的数据流图**

上部计数/控制图的可辨标签：`p_arg[3:0]`、`q_arg[3:0]`、`flt_type`、`flt_cnt[3:0]`、`flt_en`、`flt_buf_clr`、`flt_cal_en`、`4'd0`、`4'd1`。左侧`flt_type`控制的MUX输入0为`p_arg[3:0]`，输入1为`p_arg[3:0]+q_arg[3:0]`；其输出全名仍待确认。具体连线、反馈和其他多路选择条件见原图。

> ⚠️ 原图待复核（SARC-LLD-U12）：计算数据流图上部计数器周围的复合条件、部分比较/选择标签和细小下标，尚不能逐字符确认；下方可确认的乘加与缩放部分已分别转录，不能把整幅图标成完整文字化。
> 原图：[GameViewer_SeEx4da40l.png](../images/GameViewer_SeEx4da40l.png)，右页上部计数/控制图。

**乘加部分图中文字转录：**

| 位置 | 原图文字／定标 |
|---|---|
| 两个乘法输入 | `flt_cal_dat[flt_idx][15:0]`、`flt_coeff[flt_idx][15:0]`，s(16,15) |
| 乘法输出 | s(32,30) |
| flr之后 | s(24,22) |
| 红色处理注释 | 补两位符号位 |
| 加法器输入 | s(26,22) |
| 加法器结果 | `flt_acc`，s(27,22) |
| wrap／sat选择 | `cfg_pflt_clip`；wrap分支0，sat分支1 |
| 选择后结果 | s(26,22) |
| 累加结果寄存器 | `flt_cal_dat_o_pre[25:0]`；使能`flt_cal_en` |
| 累加起始选择 | `flt_cal_st`；一路`26'd0`，另一路为累加结果反馈 |
| 溢出检测标签 | `flt_acc[26]`、`flt_acc[25]`、`flt_cal_en`、`flt_ovf`；异或及与门连接见原图 |

**输出缩放部分图中文字转录：**

图中以`cfg_pflt_r_arg[2:0]`选择8路移位拼接输入。

| 选择值 | 输入拼接式 |
|---|---|
| 7 | `{flt_cal_dat_o_pre[25:0]}` |
| 6 | `{{1{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:1]}` |
| 5 | `{{2{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:2]}` |
| 4 | `{{3{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:3]}` |
| 3 | `{{4{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:4]}` |
| 2 | `{{5{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:5]}` |
| 1 | `{{6{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:6]}` |
| 0 | `{{7{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:7]}` |

右侧格式示意为`s(26,22)`→`<<R`→`s(26,22-R)`→`s(26,15)`，旁边红字“合并”。浅蓝/清绿部分包含`sat`、`wrap`及选择信号`cfg_pflt_acc_out_wrap_sel`，0选择sat、1选择wrap，输出`flt_cal_dat_o[15:0]`，定标`s(16,15)`。

> 同源局部核对注：本页中央乘加区域与辅助原图[GameViewer_323Uh2DKeH.png](../../sarc_diagrams/images/GameViewer_323Uh2DKeH.png)中的对应区域，底部移位/输出区域与[GameViewer_T5Wi63Rflj.png](../../sarc_diagrams/images/GameViewer_T5Wi63Rflj.png)中的对应区域已按框、连线及标签逐项比对后用于辨字。辅助图外围额外红色解释没有并入本页作者正文；此局部对照不等于辅助图整页已完成核对。上部U12仍保留。
> 原文差异：本节正文27bit、图中s(27,22)与下一节蓝字“扩展36bit加法器”分别保留；没有替作者推断一套最终位宽。红字“补两位符号位”不是“扩展36bit”。

---

## 原图：`GameViewer_pVe1evLu6f.png`

[查看原始PNG](../images/GameViewer_pVe1evLu6f.png)

### 【左页】

#### 5.15 预处理过采和通道

本节原图无独立图号的结构图，可辨文字如下：`vc_flag_ctrl`内含浅蓝`ovs_ctrl 0~7`；`vc_flag[15:0]`送入`vc_queue`，其`vc_num`送入`sarc_sample_ctrl`，`start`送入“模拟ADC”，`data`送入`sarc_pflt (pfc_ch0~7)`，再送入浅蓝`sum_ctrl`中的`sum_ch0~7`。上方“寄存器菜单”中有`sum0~sum7`，右侧标注`intr/dma处理`。反馈信号标注`priority_cflt`；反馈分支及图中连线见原图。

**过采控制侧：**（以下原文为浅蓝字）

- 增加8套采样间隔、过采次数配置，作用于ovs_ctrl0~7；
- 过采样通道连接在预处理滤波通道后，与虚拟通道的映射关系同预处理通道滤波一致；
- 若虚拟通道映射到过采样通道，则vc_flag_ctrl的ovs_ctrl增加flag的自动拉起机制，未达到过采次数时自动按间隔设置拉高对应的vc_flag；
- 该虚拟通道的触发信号来临时完成影子加载，生效软件的配置；
- 无论是否开启抢占功能，过采过程中如果出现其它高优先级的虚拟通道请求priority_cflt，或blanking窗口，进行resume、conti恢复；

### 【右页】

（续上页浅蓝字）

- 若过采期间来临新触发，硬件上忽略该触发，但告警，软件可清除该告警；

**求和侧：**（原文浅蓝字）

- 对预处理滤波输出进行按过采次数进行求和功能；
- 优先级冲突的处理，resume的恢复模式下，需清零求和结果；

**其它：**（原文浅蓝字）

- 加法器单元可复用滤波逻辑中的扩展36bit加法器；
- 过采求和结果完成后可输出中断/dma请求；
- 该功能需有使能控制；

#### 5.16 采样结果超门限检测

超门限检测的对象为用户预处理补偿后的采样结果。

检测包括超上门限和超下门限检测，每个用户预处理通道的采样结果独立配置上下门限值、独立检测、独立输出检测结果。

此处修改：

6001：对检测结果进行滤波处理，且超上下门限单独输出告警。

> 转录注：原图标题确为“预处理过采和通道”，未自行补“求”字；priority_cflt与前文priority_conflict、priority_cnflt/priority_conflt按各处原图拼写保留。上页“过采控制侧”末项跨页续接。本页6001条目紧接下一张6002条目，不将下一张误放在FIR结构图之前。

---

## 原图：`GameViewer_NaDPGTeO6W.png`

[查看原始PNG](../images/GameViewer_NaDPGTeO6W.png)

### 【左页】

6002：上下门限检测输出使用CBC或者ONESHOT两种模式（软件配置选择）。CBC模式下，根据每个新的采样结果是否超门限控制是否输出告警；ONESHOT模式下，一旦产生了超门限告警，需要软件进行清除。每个超门限检测通道输出1bit事件，上下门限告警通过mux-or的方式输出。同时单独上报超上下门限的实时状态。

**图5-20 超门限检测原理**

图中文字转录：`limit.hi`、`adc_result`、`limit.lo`；两路比较器，图内以`+`、`-`标记输入端；`pulse`、`set`、`clear`；上、下支路分别标注`adcevtsts.triphi`、`adcevtsts.triplo`、`evtsel.hi`、`evtsel.lo`、`clear.hi`、`clear.lo`、`CBC clearlogic`；事件汇合输出`EVT`。比较器、置位/清除支路和门连接保留在原图，不另加原图未写的比较公式。

**图5-20 超门限检测结果输出形式**

图中文字转录：`sample1 超门限`、`sample2 超门限`、`sample3 不超门限`、`sample4 超门限`；两路输出标注`CBC`、`ONESHOT`；红色标注`hw clear`指向CBC清除处，`soft clear`指向ONESHOT清除处。波形边沿位置以原图为准。

### 【右页】

#### 5.17 滤波通道

滤波处理模块的数据输入为校准补偿后的采样结果。

此处区别：6001是用户预处理补偿后结果，6002是校准补偿后结果。

滤波类型：FIR、IIR、滑动平均（归入FIR，由软件配置系数）、非滑动平均。

FIR滤波阶数要任意可配置，最高32阶。并且根据配置阶数对滤波结果实时输出。

**图5-20 FIR滤波**

图中文字转录：标题“滤波处理”，虚线框`filter`；输入`cal_data_out`；系数`filter_coeff`，`s(13,12) signed`；乘法节点`X`旁标注`32个X`，乘法输出`s(29,14)`；求和节点`Σ`输出`s(34,14)`，随后`round`输出`s(22,2)`，`sat`输出`s(16,2)`至`filter_data_out`，并标注`s(16,2) signed`。

> 同源局部核对注：本页“滤波处理”局部与[GameViewer_9akceoHcVF.png](../../sarc_diagrams/images/GameViewer_9akceoHcVF.png)中对应滤波框的节点、定标和“32个X”标注进行了对照，仅该一致局部用于辨字。该辅助图左上ADC校正的offset位宽与本文件第24张不同，未将该版本差异覆盖到第24张，也未据此关闭U10。
> 转录注：本页三幅图均标5-20，照留原图号。6001/6002的差异和图中红色hw/soft clear不是明示的ET6601新增；未混入本轮6601修改条目。本张正确位置为第31张，承接5.16并引入5.17。

---

## 原图：`GameViewer_iSOJmCn28m.png`

[查看原始PNG](../images/GameViewer_iSOJmCn28m.png)

### 【左页】

#### FIR

6002修改点：阶数可任意配置，且根据配置阶数实时输出滤波结果，最大32阶。

有限脉冲响应(Finite Impulse Response, FIR)。线性，不带反馈。

$$
y(k)=\sum_{n=0}^{N-1}a(n)x(k-n)
$$

x(k)：输入时间序列；  
a(n)：滤波器参数，N为滤波器的阶数；  
y(k)：输出时间序列；

FIR滤波器图解形式：

图中文字转录：输入`x(n)`，输出`y(n)`；抽头参数依次标为`a(0)`、`a(1)`、`a(2)`、`a(3)`、`a(4)`、`a(N-1)`；延迟方框均标`Z⁻¹`，中间以省略号连接；乘法节点为`×`，下方为逐级加法节点。图中使用n，正文公式使用k，分别照录。连线与抽头位置保留原图，不重画或补出省略号中的节点。

### 【右页】

#### IIR

无限脉冲响应(Infinite Impulse Response, IIR)。非线性，带反馈。

$$
y(n)=\sum_{k=1}^{N}a_k y(n-k)+\sum_{k=0}^{M}b_k x(n-k)
$$

x(n)：输入时间序列；  
a(k)、b(k)：滤波器参数，N、M为滤波器的阶数；  
y(n)：输出时间序列；

SARC模块通过一阶低通滤波器来实现一阶IIR滤波。一阶低通滤波算法原理如下：

> 原文嵌入说明图文字：
>
> **1. 一阶低通滤波算法原理**
>
> 一阶滤波，又叫一阶惯性滤波，或一阶低通滤波，软件实现RC低通滤波器的功能。
>
> $Y(n)=\alpha X(n)+(1-\alpha)Y(n-1)$
>
> 式中：α为滤波系数，X(n)为本次采样值，Y(n-1)为上次滤波输出值，Y(n)为本次滤波输出值

其中，滤波系数的取值范围为：0 ≤ alpha ≤ 1。

> 转录注：原文“IIR……非线性”照录，不按技术常识改写；公式中下标a_k/b_k与说明段a(k)/b(k)分别保留。嵌入说明的链接配色不是本文件的6601变更声明；左页明确“6002修改点”另列B14，不冒充6601新增。

---

## 原图：`GameViewer_HFc4FYW2ed.png`

[查看原始PNG](../images/GameViewer_HFc4FYW2ed.png)

### 【左页】

#### 滑动平均

“滑动平均”功能通过FIR滤波器实现，可以归入FIR滤波类型，通过用户参数配置实现。

“滑动平均”就是按我们事先设定的信号个数将输入信号加以平均。譬如，按每4个信号做一次平均，如下图所示：

图中文字转录：四个抽头标注`x(n)`、`x(n-1)`、`x(n-2)`、`x(n-3)`；三处延迟方框标`Z⁻¹`；四路乘法系数分别为`h(0)=1/4`、`h(1)=1/4`、`h(2)=1/4`、`h(3)=1/4`，汇入`Σ`，输出`y(n)`。图未显示独立图号，保留本原图链接。

#### 非滑动平均

“非滑动平均”滤波，根据用户配置的滤波次数，将2ⁿ个转换结果进行累加，然后通过将累加和右移n位，得到非滑动平均的滤波结果。其原理示意图如下：

### 【右页】

图中文字转录：左端`x(2ⁿ-1)`，右端`x(0)`；各延迟方框为`Z⁻¹`，中间以省略号连接；抽头汇入`+`节点，旁注`2ⁿ个`，经`>>n`方框输出`filter_data_out`。图接左页“非滑动平均”段，不另造图号。

n取值范围为4bit可配置，即最大滤波次数为2¹⁵。

---

## 原图：`GameViewer_ZwgMgCyaeL.png`

[查看原始PNG](../images/GameViewer_ZwgMgCyaeL.png)

### 【左页】

#### 滤波器实现时序

**图5-22 预处理和滤波处理时序示意**

图中文字转录（依图中区域自上而下；本表列名为转录索引，不是原图表头）：

| 区域 | 可确认的标签／文字 |
|---|---|
| 主输入波形 | `clk`、`ready`、`data`、`vc_num`、`se/df`、`counter` |
| 输入数据／通道标记 | `data0`、`data1`、`data2`；`vc0`、`vc1`、`vc2` |
| 预处理输出波形 | `pre_val`、`pre_data`、`vc_num`；数据仍标`data0`、`data1`、`data2`，通道仍标`vc0`、`vc1`、`vc2` |
| 滤波输出指示 | `iir`、`fir`、`no-aver` |
| 中部小图 | `cal_val`、`pre_val`；其左侧来源标签及上方中文批注未能完整确认，见U13 |
| 下部小图 | `To core 0`；`ready`、`cal_val`、`pre_val`、`ADC 1`、`交织`；下方两路`iir`、`fir` |

> ⚠️ 原图待复核（SARC-LLD-U13）：本页“Core 1 data…”后的中文批注、中部来源标签（只确认末尾1）、时钟上沿细刻度及counter各格完整数值不能从当前截图100%确认。以上没有据常识补成时序说明。
> 原图：[images/GameViewer_ZwgMgCyaeL.png](../images/GameViewer_ZwgMgCyaeL.png)，左页时序图中上部及中部小图。时序边沿、空白波形格、两行counter的对应关系保留原图。

### 【右页】

本页为滤波器实现时序图；其图名“图5-23 FIR和IIR滤波器实现时序示意”显示在下一张左页开头，按跨页图注衔接。

图中文字转录（以下分组仅用于定位原图）：

| 区域 | 可确认的标签／可辨片段 |
|---|---|
| 顶部时钟／计数 | `clk`、`counter` |
| 上部IIR/FIR输出波形 | 五行有名波形中的`data_val`、`data_val_d`、`out_en`可辨；完整前缀及大小写列入U13候选，不当作已确认接口名 |
| 预处理波形 | `pre_val`、`pre_data`、`pre_val_1d`、`pre_data_1d`、`pre_val_2d`、`pre_data_2d`；数据格标`data0`、`data1` |
| 系数RAM波形 | `Coeff_ram_rd_r`、`Coeff_ram_rd`、`Coeff_ram_addr`、`Coeff_ram_rdata`、`Coeff_ram_rdata_1d` |
| PIPE RAM波形 | `pipe_ram_rd`、`pipe_ram_rd_1d`、`pipe_ram_rd_2d`、`pipe_ram_rd_1d_neg_pulse`、`pipe_ram_addr`、`pipe_ram_rdata`、`pipe_ram_rdata_1d`、`pipe_ram_wr` |
| PIPE RAM最后一行及底部两行 | `pipe_ram_rd_…`、`…clr_flag`、`…clr_done`可辨；全名与底部两处红色条件见U13 |

> ⚠️ 原图待复核（SARC-LLD-U13，续）：上部五行有名波形疑似依次为`Iir_data_val`、`Iir_data_val_d`、`fir_out_en`、`Fir_data_val`、`fir_data_val_d`；另有两条相邻无名数据波形。完整大小写须回查原图，不能以此候选建立信号表。底部疑似`pipe_ram_rd_lst`、`Fir_clr_flag`、`fir_clr_done`，亦不作为已确认全名。第十轮按原图补录PIPE RAM末行三个数据格依次为`1111`、`0000`、`0001`；各counter小格及底部红色计数条件仍缺逐字符确认。
> 原图：[images/GameViewer_ZwgMgCyaeL.png](../images/GameViewer_ZwgMgCyaeL.png)，右页上部输出波形、最下方三行及细刻度。已保留可辨波形标签，不以旧稿错识别或设计常识填满。

---

## 原图：`GameViewer_e8XPWSdAMt.png`

[查看原始PNG](../images/GameViewer_e8XPWSdAMt.png)

### 【左页】

**图5-23 FIR和IIR滤波器实现时序示意**

> 转录注：该图名承接上一张右页的时序图，不给下方RAM参数存储图重复套用此图号。

#### FIR滤波器参数存储

图中8行存储切片及左侧地址逐行转录如下；表头为转录索引：

| 图中地址 | 图中存储切片标签 |
|---|---|
| `000-00000 : 000-11111` | `Ram_slice_0(fir_ch0 data)` |
| `001-00000 : 001-11111` | `Ram_slice_1(fir_ch1 data)` |
| `010-00000 : 010-11111` | `Ram_slice_2(fir_ch2 data)` |
| `011-00000 : 011-11111` | `Ram_slice_3(fir_ch3 data)` |
| `100-00000 : 100-11111` | `Ram_slice_4(fir_ch4 data)` |
| `101-00000 : 101-11111` | `Ram_slice_5(fir_ch5 data)` |
| `110-00000 : 110-11111` | `Ram_slice_6(fir_ch6 data)` |
| `111-00000 : 111-11111` | `Ram_slice_7(fir_ch7 data)` |

下方RAM访问时序图标签依次为：`clk`、`From ids enb`、`From ids data`、`From ids enb 1d`、`Ram_ce_n`、`Ram_we_n`、`From ids data`、`to ids enb`、`to ids data`。数据波形中的标签为`data`、`Ram_rdata`、`Ram_rdata to ids`。两处`From ids data`按原图重复保留，不把后者擅改成另一信号。

> ⚠️ 原图待复核（SARC-LLD-U14）：RAM访问时序图clk上方的极细时间轴数字不能逐项确认，信号行名和数据标签已列出，不能据波形推算并补写整串刻度。
> 原图：[images/GameViewer_e8XPWSdAMt.png](../images/GameViewer_e8XPWSdAMt.png)，左页下方时序图上沿。边沿及读写间隔仍以原图为准。

### 【右页】

FIR的滤波参数由AHB总线配置，在SARC内部由1个简单双口RAM存储。该RAM与IDS之间采用间接寻址访问，写操作只能总线访问，读操作可由总线和内部逻辑二者共同访问，但内部逻辑的访问优先级高。

RAM地址为8位，高3位选择滤波通道0-7，低5位表示每个滤波通道的32个参数地址。

#### FIR滤波器输入采样结果PIPELINE

图中标题：`Ram_slice_x(fir_chx data)`。

| 图中地址 | 图中数据标签 |
|---|---|
| `x-00000` | `Data_pipe[0]` |
| `x-00001` | `Data_pipe[1]` |
| `x-00010` | `Data_pipe[2]` |
| `x-00011` | `Data_pipe[3]` |
|  | `……` |
| `x-11101` | `Data_pipe[29]` |
| `x-11110` | `Data_pipe[30]` |
| `x-11111` | `Data_pipe[31]` |

> 转录注：省略号为原图自身内容，未擅自展开Data_pipe[4]～[28]。下一张左页DATA PIPE说明承接本图。

---

## 原图：`GameViewer_1EC7JuTBH6.png`

[查看原始PNG](../images/GameViewer_1EC7JuTBH6.png)

### 【左页】

DATA PIPE采用单口RAM实现。RAM地址为8位，高3位选择滤波通道0-7，低5位表示每个滤波通道的32个PIPEDATA。

#### 5.18 缓存通道

每个SARADC控制器包含2组16*16bit结果寄存器。每组的16个寄存器与虚拟通道一一对应。

第一组：存储上报用户偏置和增益计算处理后的采样结果，支持s(16,2)和s(16,0)（寄存器实际只有s(15,0)有效，最高两位均为符号位）两种结果上报格式可配置选择；

第二组：存储上报滤波计算处理后的采样结果，支持s(16,2)和u(12,0)两种结果上报格式可配置选择；

> 【原文浅蓝色】每个SARADC控制器包含1组8*20bit结果寄存器，该结果格式同第一组格式配置选择一致，支持输出s(20,2),s(19,0)；8个寄存器与用户预处理滤波通道一一对应。

采样结果上报支持result_ovf（结果被覆盖标志）、result_val（结果有效标志）、result_data（结果数据）。

### 【右页】

**图5-24 结果寄存器读写时序示意**

图中信号标签自上而下为：`Result_in_enb`、`Result_in`、`Ids_Result_reg`、`Result_val_in_enb`、`Result_val_in`、`Ids_Result_val_reg`、`Result_ovf_in_enb`、`Result_ovf_in`、`Result_ovf_reg`。

图中顶部三处`New data`，两处总线读标记`Ahb read x`、`Ahb read z`；`Ids_Result_val_reg`和`Result_ovf_reg`左侧各有`Read clear`标注。数据格的细小常量见U15；波形边沿、寄存器底纹及总线读虚线保留原图。

> ⚠️ 原图待复核（SARC-LLD-U15）：Result_in和Ids_Result_reg中的三组红色数据常量不能逐字符确认；疑似`16'dx`、`16'dy`、`16'dz`，仅作定位候选，不作为确定值写入正文。
> 原图：[images/GameViewer_1EC7JuTBH6.png](../images/GameViewer_1EC7JuTBH6.png)，右页图5-24上部两条数据波形。

6002新增实现：用SARADC控制器使能cfg_sarc_en的上升沿清零result_ovf（结果被覆盖标志）、result_val（结果有效标志）、result_data（结果数据）寄存器状态。

#### 5.19 通过fifo模式读取采样结果

每个ADC控制器有如下2组结果存储寄存器，每组包含16个寄存器，分别对应16个vc，

- 用户偏置和增益计算处理后的采样结果寄存器组
- 滤波计算处理后的采样结果寄存器组

> 转录注：5.19后续文字接下一张左页，不把本页两条项目写成完整FIFO规格。浅蓝色8*20bit段列C41；6002清零实现另列B15。s(16,0)与括号内s(15,0)按原文分别保留，不统一格式。

---

## 原图：`GameViewer_cTDH1vvDLo.png`

[查看原始PNG](../images/GameViewer_cTDH1vvDLo.png)

### 【左页】

> 转录衔接：承接第36张5.19两组结果寄存器的说明。

对每组结果寄存器分别增加1个对应的寄存器，该寄存器可通过软件配置bitmap映射为fifo模式，两组结果寄存器对应fifo模式的参数独立配置。

`cfg_*_fifo_vc_sel`选择在vc_en有效的vc中，哪些vc对应的结果寄存器映射到fifo，默认vc_en有效的vc都映射到fifo。即有效的bitmap=`cfg_*_fifo_vc_sel & cfg_vc_en`。

注意：

- 软件在初始化或者更新bitmap相关配置后，都需要对`cfg_*_fifo_bitmap_reload`进行写1操作。
- 软件配置vc的采样顺序必须按照bitmap中vc编号从小到大的顺序。

硬件控制fifo映射关系的bitmap时序如下图所示：

> 图中文字转录（原图未见独立图号或图名，不自行编号）：从上到下为`cfg_fifo_bitmap_reload`、`fifo_rd_valid_out`、`fifo_rd_ack_in`、`fifo_rd_data_in`、`fifo_bitmap`。data格依次为`0`、`1`、`2`、`3`；bitmap格依次为`0000`、`1111`、`1110`、`1100`、`1000`、`1111`。两处红字分别为`sw reload`、`hw reload`；右侧批注为“判断reload条件：用One-hot取反后与原值与”。波形沿及连线以原PNG为准。

### 【右页】

#### 5.20 SARADC控制器中断

6002功能增加点1（产生EOC标志）：

每个ADC控制器的虚拟通道支持对应EOC（end-of-conversion）信号产生，用于触发中断，EOC脉冲信号可配置选择如下两个产生位置，每个ADC控制器的虚拟通道统一配置：

□S/H窗口结束时刻，

□采样转换结束时刻，默认选择

□S/H窗口开始时刻

支持EOC选择位置时刻到中断产生的上沿延时可配置，16bit SYSCLK时钟计数值；且每个ADC控制器的虚拟通道统一配置。如果当前EOC到来时，上一个EOC的延时处理没有完成，则在该时刻输出上一个EOC的中断触发，同时当前EOC进行延时模块进行延时处理。

**图5-20 EOC延时处理示意**

> 图中文字转录：两行信号`end_p`、`int_trig`；图中两段`delay`及各脉冲框内`vc`带细小下标，见U16。框内批注：“end_p到来时，上一个end_p的delay还没有完成，则在该时刻输出上一个end_p的int_trig。然后当前enc_p进行delay模块重新开始计数延时。”
> 转录注：原文写“两个”但下列有三个选项，分别照录；批注的`enc_p`与前文`end_p`不同，按各处保留；6002历史说明不改写为6601新增。

> ⚠️ 原图待复核（SARC-LLD-U16）：图5-20各vc脉冲框下标和两段delay的细小下标尚不能逐字符确认；不能按先后顺序补成i/j/k等确定值。可辨基名及完整批注已录。
> 原图：[GameViewer_cTDH1vvDLo.png](../images/GameViewer_cTDH1vvDLo.png)，右页下部EOC延时示意。

## 原图：`GameViewer_m4qMLaqKqw.png`

[查看原始PNG](../images/GameViewer_m4qMLaqKqw.png)

### 【左页】

下图指示EOC模块输入信号的时序关系：

EOC的位置可以配置选择采样结束或者转换结束：

采样结束sh_end_p：adc_spltime_en为低时（无扩展采样）选择adc_start_1d的下降沿信号adc_start_1d_neg（sysclk）；

adc_spltime_en为高时（有扩展采样）选择adc_spltime_en_1d的下降沿信号adc_spltime_en_1d_neg（sysclk）；

转换结束cvt_end_p：选择adc_ready_in_1d的上升沿信号adc_ready_sarc（sysclk）；

**图5-20 EOC模块输入信号时序关系图**

> 图中文字转录：上组可辨`adc_start`、`adc_spltime_en`、`adc_spltime_en_1d`、`adc_spltime_en_1d_neg`、`adc_start_1d`、`adc_start_1d_neg`及VC数据行；数据框`VC1`、`VC2`。下组可辨`adc_ready_in`、`adc_ready_in_1d`、`adc_ready_sarc`、`adc_ready_vc_num`；数据框`VC1`、`VC2`。完整波形沿与下标见原图，不据采样原理重画。
> ⚠️ 原图待复核（SARC-LLD-U17）：上组VC数据行的完整信号名疑似`vc_num_sarc`，小字大小写/分隔符不能完全确认；两组细波形沿对齐关系不以文字推算替代。原图：[GameViewer_m4qMLaqKqw.png](../images/GameViewer_m4qMLaqKqw.png)，左页中部两组时序。

~~6002功能修改点2（中断源）：~~

~~每个ADC支持1路中断输出，中断源包括：~~

~~□EOC脉冲信号（基于虚拟通道，16bit）~~

### 【右页】

> 转录衔接：以下三条仍属于左页被划去的6002中断源清单，删除线连续保留。

~~□电平超门限中断（基于虚拟通道，超门限脉冲触发中断，超上下门限独立中断源，共16bit*2）~~

~~□2组结果寄存器锁存有效采样结果中断（基于虚拟通道，16bit*2）~~

~~□1组求和结果寄存器锁存有效采样结果中断（基于求和通道，8bit）~~

6601功能修改点2（中断源）：

每个ADC支持1+4路中断输出，1个中断源包括：

~~□EOC脉冲信号（基于虚拟通道，16bit）~~

□电平超门限中断（基于虚拟通道，超门限脉冲触发中断，超上下门限独立中断源，共16bit*2）

~~□2组结果寄存器锁存有效采样结果中断（基于虚拟通道，16bit*2）~~

4套中断逻辑可以任选以下源作为中断源；

□EOC脉冲信号（基于虚拟通道，16bit）

□2组结果寄存器锁存有效采样结果中断（基于虚拟通道，16bit*2）

> 转录衔接：第三个选项在下一张左页首行，列表未在本页结束。

## 原图：`GameViewer_u5JeUrg4ga.png`

[查看原始PNG](../images/GameViewer_u5JeUrg4ga.png)

### 【左页】

> 转录衔接：以下浅蓝条目承接第38张“4套中断逻辑”清单。

□1组求和结果寄存器锁存有效采样结果中断（基于求和通道，8bit）

> 原图标记：上条整行浅蓝色。

当中断产生时，上一中断还未响应（中断未被清除），此时产生中断溢出告警指示。

中断处理按下面的方式统一处理：

**图5-20 中断处理**

> 图中文字转录：左侧由上到下为“中断使能信号”“中断触发信号”“中断测试寄存器”“中断清除寄存器”“中断屏蔽信号”；使能/屏蔽旁为“电平”，测试/清除旁为“脉冲”。图中可辨`cfg_*_int_en`、`cfg_*_int_clr`、`cfg_*_int_mask`，内部“中断锁存”、`D`、“中断处理模块”；上部“原始中断寄存器：int_raw_rpt”“中断状态寄存器：int_status_rpt”。右侧输出含`int`。逻辑门、连线、反馈、输出前寄存器以及原图图号均保留在来源图中，不自行重新解释。
> ⚠️ 原图待复核（SARC-LLD-U18）：第十轮已确认测试寄存器信号为`cfg_*_int_force_ind`，上方读出端为“寄存器读”，D右侧紧邻标签为`intr`，均按字形补录。更右侧“中断输出”后的完整标识/分隔符仍不够清晰，U18保留此残余，不凭中断通用模板补写。
> 原图：[GameViewer_u5JeUrg4ga.png](../images/GameViewer_u5JeUrg4ga.png)，左页中部“中断处理”图。
> 转录注：本图与前两张的EOC示意均原标“图5-20”，不自动重编号。

#### 5.21 DMA数据请求

6002修改点（DMA请求源）：

### 【右页】

每个ADC支持4个DMA请求通道，每个DMA请求通道可从如下DMA请求源中独立配置选择（sarc只选择DMA请求源输出，DMA握手功能在DMA_MUX模块中实现）：

- EOC脉冲信号（基于虚拟通道，16bit）
- 2组结果寄存器锁存有效采样结果（基于虚拟通道，16*2）
- 电平超门限检测结果事件（基于虚拟通道*16bit）
- 1组求和结果寄存器锁存有效采样结果（基于求和通道，8bit）

> 原图标记：以上列举的最后一项为浅蓝色；前三项黑色。原文第二项写`16*2`，不补成`16bit*2`。

在通过fifo读取采样结果模式下，通过fifo的非空信号进行DMA请求，两个fifo的非空信号可独立选择到4个dma请求通道，默认配置下不选择fifo的DMA请求。

6801增加将16个虚拟通道的电平超门限检测结果事件或结果作为新增的dma请求事件。

#### 5.22 数据同步到CPU_WRAP

为了使得cpu能够快速获取adc采样结果，减少总线延迟，将adc采样结果同步到cpu_wrap中。6601修改成两组，

> 原图标记：“6601修改成两组，”为浅蓝色，续句位于下一张左页；不能将页尾逗号当成句子结束。

## 原图：`GameViewer_YbkCdqx6qz.png`

[查看原始PNG](../images/GameViewer_YbkCdqx6qz.png)

### 【左页】

> 转录衔接：承接第39张5.22“6601修改成两组，”；以下整段浅蓝色。

adcreg_receive需根据时钟方案调整交互方式，所有逻辑在200M下；

> 图中文字转录（本图未见独立图号/图名）：左侧堆叠标签分别为~~sarc2.adc_result~~、`sarc1.adc_result`、`sarc0.sarc_result`；左下两框“预处理运算结果”“滤波运算结果”，选择信号`cfg_outd_sel`及`0`、`1`。右侧接收框标题`sarc_adcresult_receive`；内部“SARC0通道”“SARC1通道”和浅蓝“SARC2通道”。右下寄存器块可辨`ids_result_reg0`、`ids_result_reg1`；浅蓝顶块、时钟图例、位宽/数组及右侧配置输入见U19。原文`adc_result`/`sarc_result`差异照录，不自行统一。
> ⚠️ 原图待复核（SARC-LLD-U19）：上部sarc/cpu_wrap时钟括号、双色图例小字、总线标识及下方位宽说明、四个右侧浅蓝配置输入、浅蓝寄存器块完整名字/标线范围、结果组宽度和部分data/valid/vc_num下标不能全部逐字符确认。第十一轮已确认两个黑色寄存器块`ids_result_reg0`、`ids_result_reg1`内的宽度均为`8*(16+16)bit`。其余可辨片段为`data`、`valid`、`vc_num`；传输标签疑似`data[15:0]/valid/vc_num[3:0]`，仅记为候选。浅蓝SARC2通道行的横线性质/范围需保留原图回查。不得把正文“200M”“两组”反向填入图中字形或推断全部删除范围。
> 原图：[GameViewer_YbkCdqx6qz.png](../images/GameViewer_YbkCdqx6qz.png)，左页上半部CPU_WRAP交互图。

### 6. 约束

参考《SARC模块LRS设计文档》中2.4节-约束说明。

### 7. 遗留问题

### 8. 参考文献

> 转录注：原图第7、8节仅见标题，下面无作者正文，不添加本次转录疑点或外部参考文献到原文空白处。

### 【右页】

> 转录注：右侧未见文档正文，仅有水印/界面，保持原文空白；这些噪声不转录。

## 第二部分：截图明确标注的ET6601修改点（40张首轮范围）

### 原文颜色依据

第2张右页原文：“注：浅蓝色和清绿色相关区域为ET6601新加的改动，包括线，背景及底纹部分；”。[原图](../images/GameViewer_aPDFQVxWhA.png)。目录蓝色链接不据此判定，历史文档图的原有配色不据此判定。

以下C01～C15为来源出现位置，其中C11含源图遮挡、文字尚不完整。15不是15项独立功能；同一改动在图和正文中重复出现会分别定位。仅按原图保存，不补旧版本参数。

| 编号 | 所在章节／表格 | 原始文字或可辨标签 | 原图标记及边界 | 原始截图 |
|---|---|---|---|---|
| C01 | 第3章图1，浅蓝色新增节点 | SCh0、SCh1、……、SCh7；Sum0、Sum1、……、Sum7 | 图内新增浅蓝色节点；仅转录可辨标签，不推断额外实例 | [GameViewer_LWEUsHJgSN.png](../images/GameViewer_LWEUsHJgSN.png) |
| C02 | 第3章功能第4条 | 支持SARADC通道触发信号优先级抢占控制； | “抢占”为浅蓝色 | [GameViewer_LWEUsHJgSN.png](../images/GameViewer_LWEUsHJgSN.png) |
| C03 | 第3章功能第9条 | 支持预处理滤波通道启用过采样求和功能； | 整条浅蓝色 | [GameViewer_LWEUsHJgSN.png](../images/GameViewer_LWEUsHJgSN.png) |
| C04 | 4.1，sarc_a2d_outrd_hold行 | sarc_a2d_outrd_hold；输出；输出5拍的窗口信息，模拟保证ready&data时序不受抢占控制拉低sarc_d2a_adc_en的控制； | 信号、方向及说明整行浅蓝色；不按信号名更改方向 | [GameViewer_ZQLidR9zmC.png](../images/GameViewer_ZQLidR9zmC.png) |
| C05 | 4.1，sarc_wdt_dma_src_is_dly行 | 6601项目先固结0进行时序收敛，若不行在切换到固结1上。 | 明确6601文字；不代表当前时序验证通过 | [GameViewer_XEDw3yfNAf.png](../images/GameViewer_XEDw3yfNAf.png) |
| C06 | 5.1 SARC连接关系 | 共有2个ADC CORE，每个ADC CORE对应1个控制器SARC，每个SARC占用一条AHB总线。 | “2”为浅蓝色；不由此覆盖其他页保留的旧描述 | [GameViewer_Wwj0z78cha.png](../images/GameViewer_Wwj0z78cha.png) |
| C07 | 图5-1，第三组连接 | AHB 2；adc ctrl 2；adc core 2 | 第三组浅蓝色；adc ctrl 2及adc core 2有删除线，文字仍保留 | [GameViewer_Wwj0z78cha.png](../images/GameViewer_Wwj0z78cha.png) |
| C08 | 图5-2，SARC0新增节点 | ovs_ctrl；sum_ctrl；sum*8 | 浅蓝色节点；其他图内细字见U04，不替节点补齐功能 | [GameViewer_Wwj0z78cha.png](../images/GameViewer_Wwj0z78cha.png) |
| C09 | 图5-2，第三控制器区域 | SARC 2；ADC CORE 2 | 整块浅蓝色并有删除线；保留被删路径 | [GameViewer_Wwj0z78cha.png](../images/GameViewer_Wwj0z78cha.png) |
| C10 | 5.1，vc_flag_ctrl段 | 包含一个过采样ovs_ctrl模块，当虚拟通道的启用滤波过采样求和功能时，接收外部触发，自动完成N次采样触发，根据resume/conti模式配置，并获取queue_manage输出排队信息，自动高优先级抢占情况下的恢复处理； | 整段浅蓝色；原句语法照录 | [GameViewer_bG98ufwLis.png](../images/GameViewer_bG98ufwLis.png) |
| C11 | 5.1，queue_manage右页首行 | 若开启抢占功能，当前正在转【原图被远程提示框遮挡】现p0的转换请求，输出当前p0的请求； | 浅蓝色；含U05遮挡，记录不完整，不计为已完整恢复的句子 | [GameViewer_bG98ufwLis.png](../images/GameViewer_bG98ufwLis.png) |
| C12 | 5.1，vc_flag_ctrl/queue_manage职责说明 | 进行过采模式下的flag控制，抢占模式下的flag恢复。 | 该句浅蓝色；其后模块解耦说明为黑字 | [GameViewer_bG98ufwLis.png](../images/GameViewer_bG98ufwLis.png) |
| C13 | 5.1，sum_ctrl说明 | sum_ctrl：过采求和模块； | 整行浅蓝色 | [GameViewer_bG98ufwLis.png](../images/GameViewer_bG98ufwLis.png) |
| C14 | 5.1，sum说明 | sum：求和结果输出； | 整行浅蓝色 | [GameViewer_bG98ufwLis.png](../images/GameViewer_bG98ufwLis.png) |
| C15 | 图5-3，求和结果节点 | sum reg；8*20bit | 图内求和相关浅蓝色标记；系数及其他细字仍在U06 | [GameViewer_3VjshoX5So.png](../images/GameViewer_3VjshoX5So.png) |

### 第三轮新增来源位置C16～C40

本批17张新增25条来源位置记录，累计C01～C40。记录数不是独立功能数；C11的原遮挡仍未解决。

| 编号 | 所在章节／表格 | 原始文字或可辨标签 | 原图标记及边界 | 原始截图 |
|---|---|---|---|---|
| C16 | 5.7左页末段 | preemtive_md：p0优先级抢占模式指示，1为p0可抢占模式，0为不可抢占模式； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_40i6eF4ZKV.png](../images/GameViewer_40i6eF4ZKV.png) |
| C17 | 5.7右页首段 | priority_conflict：抢占模式开启下的优先级指示，1指示优先级冲突，当前存在p0优先级请求，需由外部的请求处理模块重发vc_num_req完成处理后，才会拉低；未开启抢占功能时一直为0； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_40i6eF4ZKV.png](../images/GameViewer_40i6eF4ZKV.png) |
| C18 | 图5-13输入/输出 | preemtive_md；priority_conflict | 两个浅蓝/清绿信号标签；与正文同主题不同来源位置。 | [GameViewer_40i6eF4ZKV.png](../images/GameViewer_40i6eF4ZKV.png) |
| C19 | 5.9软件触发末段 | 还支持另一软件触发，软件通过配置CFG_SARC_VC_SOFT_TRIGER.cfg_sarc_vc_soft_trigger[15:0]；该触发脉冲在触发选择列表上，触发功能需经过触发选择，与其它硬件触发源的功能类似； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_Pv1TFSu3Dw.png](../images/GameViewer_Pv1TFSu3Dw.png) |
| C20 | 抢占功能无编号结构图 | priority_cnflt；start/en；vc_num/val；vc_flag_ctrl；sarc_smaple_ctrl | 图中浅蓝反馈线及priority_cnflt标记；其余为定位标签，不把所有黑字也归为新增。 | [GameViewer_LoWatHzLVG.png](../images/GameViewer_LoWatHzLVG.png) |
| C21 | 1.1.1抢占功能控制第1条 | 1. 由vc_queue模块完成识别vc_flag_ctrl输入的vc_flag[15:0]中的优先级冲突，~~包含blanking情况的冲突，~~判定当前队列优先级和当前输出的vc_num的优先级是否冲突，输出priority_cnflt信号； | 浅蓝正文中“包含blanking情况的冲突”有删除线；原文删除性质保留。 | [GameViewer_LoWatHzLVG.png](../images/GameViewer_LoWatHzLVG.png) |
| C22 | 1.1.1抢占功能控制第2条及两种时机 | 2. sarc_sample_ctrl模块识别到priority_cnflt信号，根据priority_cnflt的时机进行不同的时序控制：：<br>ii. 可直接进行抢占；<br>需delay发起抢占(不区分队列是否存在其它请求，统一delay)； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_LoWatHzLVG.png](../images/GameViewer_LoWatHzLVG.png) |
| C23 | 图5-18交接区说明 | 若抢占发生在连续两笔转换的交接区，需输出sarc_a2d_outrd_hold使模拟保证不影响第一次的ready&data的返回时序； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_LoWatHzLVG.png](../images/GameViewer_LoWatHzLVG.png) |
| C24 | 图5-18后的模拟返回说明 | 1. 模拟接收抢占控制，完成采样转换后返回高优先级对应的ready及data信息； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_LoWatHzLVG.png](../images/GameViewer_LoWatHzLVG.png) |
| C25 | 图5-18后的vc_flag_ctrl处理 | 2. vc_flag_ctrl接收该ready信号，priority_conflt，start信号；<br>a) 发出start后清除vc_flag；<br>b) 若期间因抢占导致该对应的start无法返回ready，需重新将vc_flag拉起；<br>c) 使用对应返回的ready指示该vc_flag的完整结束； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_LoWatHzLVG.png](../images/GameViewer_LoWatHzLVG.png) |
| C26 | 5.11左页末段 | 当由于p0优先级抢占发生时，低优先级会在第二次采样开始时更新DLYSTAMP值； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_mjeYzTB3j7.png](../images/GameViewer_mjeYzTB3j7.png) |
| C27 | 5.11右页首段 | 过采样启用时，该延时捕获仅在过采样的第一次开始时锁存延迟值； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_mjeYzTB3j7.png](../images/GameViewer_mjeYzTB3j7.png) |
| C28 | 5.14.3.4计算数据流图底部 | sat；wrap；cfg_pflt_acc_out_wrap_sel；flt_cal_dat_o[15:0]；s(16,15) | sat/wrap选择部分为浅蓝/清绿；最后两个为对应黑色输出标签，未推断旧版本选择。 | [GameViewer_SeEx4da40l.png](../images/GameViewer_SeEx4da40l.png) |
| C29 | 5.15结构图 | ovs_ctrl 0~7；sum_ctrl；sum_ch0~7；sum0~sum7 | 浅蓝新增控制/求和节点；图内其它黑字仍完整列在正文。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C30 | 5.15过采控制侧第1条 | 增加8套采样间隔、过采次数配置，作用于ovs_ctrl0~7； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C31 | 5.15过采控制侧第2条 | 过采样通道连接在预处理滤波通道后，与虚拟通道的映射关系同预处理通道滤波一致； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C32 | 5.15过采控制侧第3条 | 若虚拟通道映射到过采样通道，则vc_flag_ctrl的ovs_ctrl增加flag的自动拉起机制，未达到过采次数时自动按间隔设置拉高对应的vc_flag； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C33 | 5.15过采控制侧第4条 | 该虚拟通道的触发信号来临时完成影子加载，生效软件的配置； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C34 | 5.15过采控制侧第5条 | 无论是否开启抢占功能，过采过程中如果出现其它高优先级的虚拟通道请求priority_cflt，或blanking窗口，进行resume、conti恢复； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C35 | 5.15过采控制侧第6条/跨页 | 若过采期间来临新触发，硬件上忽略该触发，但告警，软件可清除该告警； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C36 | 5.15求和侧第1条 | 对预处理滤波输出进行按过采次数进行求和功能； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C37 | 5.15求和侧第2条 | 优先级冲突的处理，resume的恢复模式下，需清零求和结果； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C38 | 5.15其它第1条 | 加法器单元可复用滤波逻辑中的扩展36bit加法器； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C39 | 5.15其它第2条 | 过采求和结果完成后可输出中断/dma请求； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| C40 | 5.15其它第3条 | 该功能需有使能控制； | 浅蓝色原文；按本文件颜色声明归集，不推断旧值。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |

### 第四轮新增来源位置C41

第32～36张新增1条明确来源位置，LLD累计41条；LRS32＋LLD41＝73条来源位置，不是独立功能数。

| 编号 | 所在章节／表格 | 原始文字 | 原图标记及边界 | 原始截图 |
|---|---|---|---|---|
| C41 | 5.18 缓存通道，左页浅蓝段 | 每个SARADC控制器包含1组8*20bit结果寄存器，该结果格式同第一组格式配置选择一致，支持输出s(20,2),s(19,0)；8个寄存器与用户预处理滤波通道一一对应。 | 整段浅蓝色；按原文变更声明归集。与LRS及5.15同主题的重复位置不当成另一组实例。 | [GameViewer_1EC7JuTBH6.png](../images/GameViewer_1EC7JuTBH6.png) |

### 第五轮新增来源位置C42～C46

第37～40张新增5条来源归集记录，LLD累计46条；LRS32＋LLD46＝78条位置记录，不是独立功能数。跨页C43/C45各保留两张出处；C46有U19局部缺口，不计为全部图中文字准确。

| 编号 | 所在章节／表格 | 原始文字或可辨标签 | 原图标记及边界 | 原始截图 |
|---|---|---|---|---|
| C42 | 5.20 6601中断源，第38张右页 | 6601功能修改点2（中断源）：每个ADC支持1+4路中断输出，1个中断源包括：<br>~~□EOC脉冲信号（基于虚拟通道，16bit）~~<br>□电平超门限中断（基于虚拟通道，超门限脉冲触发中断，超上下门限独立中断源，共16bit*2）<br>~~□2组结果寄存器锁存有效采样结果中断（基于虚拟通道，16bit*2）~~ | 原文明示6601；其中两条有删除线，不作为现行未删要求。 | [GameViewer_m4qMLaqKqw.png](../images/GameViewer_m4qMLaqKqw.png) |
| C43 | 5.20 4套中断逻辑，跨第38～39张 | 4套中断逻辑可以任选以下源作为中断源；<br>□EOC脉冲信号（基于虚拟通道，16bit）<br>□2组结果寄存器锁存有效采样结果中断（基于虚拟通道，16bit*2）<br>□1组求和结果寄存器锁存有效采样结果中断（基于求和通道，8bit） | 位于6601说明下；第三选项跨页且浅蓝色。整组清单为一个归集记录，保留两张出处，不算多套新实例。 | [GameViewer_m4qMLaqKqw.png](../images/GameViewer_m4qMLaqKqw.png)；[GameViewer_u5JeUrg4ga.png](../images/GameViewer_u5JeUrg4ga.png) |
| C44 | 5.21 DMA请求源，右页浅蓝条目 | 1组求和结果寄存器锁存有效采样结果（基于求和通道，8bit） | 浅蓝色；与黑色6002/6801历史说明分开；不把4个DMA请求通道推断成新增数量。 | [GameViewer_u5JeUrg4ga.png](../images/GameViewer_u5JeUrg4ga.png) |
| C45 | 5.22 CPU_WRAP跨页浅蓝正文 | 6601修改成两组，adcreg_receive需根据时钟方案调整交互方式，所有逻辑在200M下； | 明确6601且浅蓝，跨页续句合为同一来源记录。 | [GameViewer_u5JeUrg4ga.png](../images/GameViewer_u5JeUrg4ga.png)；[GameViewer_YbkCdqx6qz.png](../images/GameViewer_YbkCdqx6qz.png) |
| C46 | 5.22 CPU_WRAP图内修改位置 | ~~sarc2.adc_result~~；浅蓝“SARC2通道”；其余浅蓝配置名、时钟/寄存器细字见U19 | 图中删除线及浅蓝区域位置记录；局部未完整辨字，不能据此推断所有删除范围或图中时钟/位宽新旧值。 | [GameViewer_YbkCdqx6qz.png](../images/GameViewer_YbkCdqx6qz.png) |

### 其他原图记录（不混入明确6601修改数）

| 编号 | 所在位置 | 原文／记录范围 | 边界 | 原图 |
|---|---|---|---|---|
| B01 | 修订记录 | 20240819的8个预处理滤波器通道；2025/9/30的ET6801五项修改 | 明确历史条目，不作为6601新增。 | [GameViewer_aPDFQVxWhA.png](../images/GameViewer_aPDFQVxWhA.png) |
| B02 | 表1嵌入OR_DR表 | 支持2个ADC控制器；支持最高优先级抢占低优先级；过采求和数量最大为16 | 红字/红色删除线；不是本页浅蓝/清绿标记。保留可辨原文并登记U01，未辨子项不计为完整修改。 | [GameViewer_v6tUVs7H0k.png](../images/GameViewer_v6tUVs7H0k.png) |
| B03 | 4.1差分通道行 | sarc_d2a_adc_mux_df<3:0>；输出；SARADC差分通道选择信号，mux_se为差分P端，mux_df为差分N端 | 原图黑色删除线；未单独标明版本。 | [GameViewer_ZQLidR9zmC.png](../images/GameViewer_ZQLidR9zmC.png) |
| B04 | 4.1差分vrefp注入行 | sarc_d2a_adc_cal_df_refp_inj；输出；控制ADC差分侧输入vrefp | 原图黑色删除线；未单独标明版本。 | [GameViewer_ZQLidR9zmC.png](../images/GameViewer_ZQLidR9zmC.png) |
| B05 | 4.1差分vrefn注入行 | sarc_d2a_adc_cal_df_refn_inj；输出；控制ADC差分侧输入vrefn | 原图黑色删除线；未单独标明版本。 | [GameViewer_XEDw3yfNAf.png](../images/GameViewer_XEDw3yfNAf.png) |
| B06 | 5.1数据格式说明 | 校准s(16,2)；ATE u(12,0)；用户预处理s(16,2)/s(16,0)；滤波s(16,2)/u(12,0) | 四组原文红色强调，未独立注明6601版本；全文在第一部分，不加入15条明确变更位置。 | [GameViewer_3VjshoX5So.png](../images/GameViewer_3VjshoX5So.png) |
| B07 | 5.3校准软件流程第1步 | adc_pwdn=0、 | 原图黑色删除线；adc_en=0未划去；未独立注明删除所属版本。 | [GameViewer_QZWwXnmnv1.png](../images/GameViewer_QZWwXnmnv1.png) |

### 第三轮其他原图记录B08～B13

| 编号 | 所在章节／表格 | 原始文字或可辨标签 | 原图标记及边界 | 原始截图 |
|---|---|---|---|---|
| B08 | 5.11开头 | 该功能为6002新增。 | 明确6002历史功能；本页后两处浅蓝新增另外列C26/C27。 | [GameViewer_mjeYzTB3j7.png](../images/GameViewer_mjeYzTB3j7.png) |
| B09 | 5.13 | 6002相对于6001修改点：pre_gain参数格式由u(14,12)修改为s(15,12)。 | 明确历史6001→6002，不改成6601新增。 | [GameViewer_UFTfaW6Wm8.png](../images/GameViewer_UFTfaW6Wm8.png) |
| B10 | 5.14.3.4图内 | 补两位符号位；合并 | 红色图注；没有单独注明6601版本，已用对应辅助局部辨字。 | [GameViewer_SeEx4da40l.png](../images/GameViewer_SeEx4da40l.png) |
| B11 | 5.16末段 | 6001：对检测结果进行滤波处理，且超上下门限单独输出告警。 | 与下一张6002形成历史对照，不是6601新增。 | [GameViewer_pVe1evLu6f.png](../images/GameViewer_pVe1evLu6f.png) |
| B12 | 5.16跨页续段 | 6002：上下门限检测输出使用CBC或者ONESHOT两种模式（软件配置选择）。CBC模式下，根据每个新的采样结果是否超门限控制是否输出告警；ONESHOT模式下，一旦产生了超门限告警，需要软件进行清除。每个超门限检测通道输出1bit事件，上下门限告警通过mux-or的方式输出。同时单独上报超上下门限的实时状态。 | 明确6002的CBC/ONESHOT输出形式；红色hw clear/soft clear为对应时序标识。 | [GameViewer_NaDPGTeO6W.png](../images/GameViewer_NaDPGTeO6W.png) |
| B13 | 5.17输入来源 | 此处区别：6001是用户预处理补偿后结果，6002是校准补偿后结果。 | 原文6001/6002输入位置差异，不改成6601新增。 | [GameViewer_NaDPGTeO6W.png](../images/GameViewer_NaDPGTeO6W.png) |

### 第四轮其他原图记录B14～B15

| 编号 | 所在章节／表格 | 原始文字 | 原图标记及边界 | 原始截图 |
|---|---|---|---|---|
| B14 | 5.17 FIR | 6002修改点：阶数可任意配置，且根据配置阶数实时输出滤波结果，最大32阶。 | 明确6002历史修改，不计为6601新增；本页IIR原文“非线性”照录，不按常识改写。 | [GameViewer_iSOJmCn28m.png](../images/GameViewer_iSOJmCn28m.png) |
| B15 | 5.18 图5-24下方 | 6002新增实现：用SARADC控制器使能cfg_sarc_en的上升沿清零result_ovf（结果被覆盖标志）、result_val（结果有效标志）、result_data（结果数据）寄存器状态。 | 明确6002新增，与同张浅蓝C41分开归类。 | [GameViewer_1EC7JuTBH6.png](../images/GameViewer_1EC7JuTBH6.png) |

### 第五轮其他原图记录B16～B19

| 编号 | 所在章节／表格 | 原始文字 | 原图标记及边界 | 原始截图 |
|---|---|---|---|---|
| B16 | 5.20 EOC | 6002功能增加点1（产生EOC标志）： | 原注明6002；完整原文、三个选项、16bit SYSCLK及延时冲突说明见第一部分；不改作6601新增。 | [GameViewer_cTDH1vvDLo.png](../images/GameViewer_cTDH1vvDLo.png) |
| B17 | 5.20 原被删除清单 | ~~6002功能修改点2（中断源）：~~<br>~~每个ADC支持1路中断输出，中断源包括：~~ | 标题、说明及跨左右页四个源全部删除线；全文逐条恢复。不与右页未删6601标题合并。 | [GameViewer_m4qMLaqKqw.png](../images/GameViewer_m4qMLaqKqw.png) |
| B18 | 5.21 DMA | 6002修改点（DMA请求源）： | 原文版本标题保留，跨页4个请求通道、DMA_MUX握手及FIFO选择照录；同节浅蓝求和条目另列C44。 | [GameViewer_u5JeUrg4ga.png](../images/GameViewer_u5JeUrg4ga.png) |
| B19 | 5.21 6801段 | 6801增加将16个虚拟通道的电平超门限检测结果事件或结果作为新增的dma请求事件。 | 明确6801历史说明，不冒充6601新增。 | [GameViewer_u5JeUrg4ga.png](../images/GameViewer_u5JeUrg4ga.png) |

### 未解决来源缺口

| 编号 | 图片与位置 | 尚待确认内容 |
|---|---|---|
| SARC-LLD-U01 | 第4张，表1嵌入OR_DR表 | 多处小字、红字和删除线被删文本；逐行已保留可辨部分，没有省略整行 |
| SARC-LLD-U02 | 第5张，图1结构图 | 长箭头文字和少量节点细字 |
| SARC-LLD-U03 | 第8张，图4-1 | spltime_en上方细字及部分波形长度标注 |
| SARC-LLD-U04 | 第9张，图5-2 | 连线/配置名/下标/左侧小字，右上局部受提示框遮挡 |
| SARC-LLD-U05 | 第10张，右页首行 | queue_manage浅蓝色抢占句被远程提示框遮住的中段；C11不完整 |
| SARC-LLD-U06 | 第11张，图5-3 | 系数全名、signed等式、位宽/定标及小框文字 |
| SARC-LLD-U07 | 第12张，图5-4 | 控制输入全名、数字域小框、位宽与输出下标 |
| SARC-LLD-U08 | 第22张，图5-17（GameViewer_ba6sdetThH.png） | spltime_en上方两处注释、部分时序小框名称和间隔小数值 |
| SARC-LLD-U09 | 第23张，图5-18三处嵌入时序表（GameViewer_LoWatHzLVG.png） | 完整行名、细小注释、周期列数及波形色块起止；源表格链接未作为已取得文件 |
| SARC-LLD-U10 | 第24张，图5-19采样校准（GameViewer_mjeYzTB3j7.png） | signed下方细字及顶部范围；辅助图offset为15bit而本页5bit，不互相覆盖 |
| SARC-LLD-U11 | 第28张，输入数据和运算结果的缓存图（GameViewer_PecSuT1xBB.png） | 清除逻辑完整布尔式、MUX选择条件及细小数组下标 |
| SARC-LLD-U12 | 第29张，计算数据流图上部（GameViewer_SeEx4da40l.png） | 计数器周围的复合条件、比较/选择标签和下标；中央/底部已用相同局部分图核对 |

40张首轮范围累计19组局部来源缺口：U01～U15保留，第五轮增加U16～U19。组数不是字符数；另有S01来源连续性疑点，不并入局部字形组数。

### 第四轮新增局部缺口及来源连续性疑点

| 编号 | 原图与区域 | 可辨内容及未解决部分 |
|---|---|---|
| SARC-LLD-U13 | 第34张GameViewer_ZwgMgCyaeL.png，左右两幅时序图 | 左图Core 1 data批注与中部来源标签、细刻度/counter；右图IIR/FIR部分全名和大小写、PIPE末行、clr两行及红色条件。可辨标签已逐组列出，候选不当作确定原字。 |
| SARC-LLD-U14 | 第35张GameViewer_e8XPWSdAMt.png，左页RAM访问时序图上沿 | 全部信号/数据标签已录；clk上方极细时间轴数字尚未逐项确认。 |
| SARC-LLD-U15 | 第36张GameViewer_1EC7JuTBH6.png，右页图5-24数据格 | 三组红色数据常量疑似16'dx/16'dy/16'dz，不能逐字符确认；9行信号和读清除/新数据标签已录。 |
| SARC-LLD-S01 | 第32张iSOJmCn28m与第33张HFc4FYW2ed之间 | 来源界面显示屏幕61–62后为65–66；63–64尚未定位。界面屏幕号不是文档正文页码，不能仅凭跳号断言漏失内容或补出假页。需继续用原截图或同源源文件核实。 |

原作者差异、重复编号和DAC待补项不自动修正。辅助图整图首轮已11/11（第七轮），但不等于全部同源同版；只在已确认相同的局部用于辨字。S01与U01～U19都不因首轮图数增加而自动关闭。

### 第五轮新增局部缺口U16～U19

| 编号 | 原图与区域 | 可辨片段与缺口 |
|---|---|---|
| SARC-LLD-U16 | [GameViewer_cTDH1vvDLo.png](../images/GameViewer_cTDH1vvDLo.png)，右页EOC延时图 | vc脉冲框及delay细小下标；可辨基名end_p/int_trig和框内批注已录。 |
| SARC-LLD-U17 | [GameViewer_m4qMLaqKqw.png](../images/GameViewer_m4qMLaqKqw.png)，左页两组EOC时序 | 上组VC数据行全名/分隔符及细沿对齐；疑似vc_num_sarc，只作候选。 |
| SARC-LLD-U18 | [GameViewer_u5JeUrg4ga.png](../images/GameViewer_u5JeUrg4ga.png)，左页中断处理图 | 测试寄存器完整信号、读出端汉字、D右输出两处标识；疑似cfg_*_int_force_ind。 |
| SARC-LLD-U19 | [GameViewer_YbkCdqx6qz.png](../images/GameViewer_YbkCdqx6qz.png)，左页CPU_WRAP图 | 时钟括号/双色图例、总线/位宽、4个浅蓝输入、浅蓝寄存器名字/标线范围、数据下标；data/valid/vc_num、8*16等可辨片段保留。 |

所有缺口仍开放。正文40张首轮已到文末，但S01未关闭，不声称来源文档完整页数已验收。
