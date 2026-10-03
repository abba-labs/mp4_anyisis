# SARC XBAR 总线互联设计文档

> 本文档由大模型逐图逐页提取自原始截图，不作主观修饰，忠实还原原文。
> 图表、时序波形及模糊部分均标注对应截图原图文件名供查阅。


---
## 图像编号 1 (原图: `GameViewer_064VlD8fJy.png`)

### 【左页】

Reserved
INPUTXBAR9
CLB5_OUT13
ETIMOUT9
Reserved
Reserved
SRPWM_XBAR_SYNCO
INPUTXBAR_CLU2OUT[0]
Reserved
INPUTXBAR10
PT_ERR
ETIMOUT10
Reserved
Reserved
SRPWM_XBAR_SYNC1
INPUTXBAR_CLU2OUT[1]
INPUTXBAR11
Reserved
ERRORSTS
ETIMOUT11
XCLK OUT
Reserved
Reserved
INPUTXBAR_CLU2OUT[2]
TMCUhuanz
INPUTXBAR12
SRPWM_XBAR_SYNC2
Reserved
STM1_0C3
Reserved
Reserved
SRPWM_XBAR_SYNC3
INPUTXBAR_CLU2OUT[3]
INPUTXBAR13
ERRORSTS
Reserved
Reserved
EPWMO_FAULTREAL
Reserved
Reserved
ETIMO_FAULTREAL
EPWMI _FAULTREAL
Reserved
INPUTXBAR14
ETIMI FAULTREAL
EPWM2_FAULTREAL
Reserved
Reserved
ETIM2_FAULTREAL
EPWM3_ FAULTREAL
Reserved
INPUTXBAR15
ETIM3 FAULTREAL
EPWM4_FAULTREAL
Reserved
CFG_OPXB_SWx
ETIM4_FAULTREAL
EPWMS FAULTREAL
Reserved
CFG_OPXB_SWx
ETIMS FAULTREAL
EPWM6_ FAULTREAL
Reserved
Reserved
ETIM6_FAULTREAL
EPWM7_FAULTREAL
Reserved
Reserved
ETIM7 FAULTREAL
EPWMS_FAULTREAL
Reserved
Reserved
ETIM8 _FAULTREAL
EPWM9_ FAULTREAL
Reserved
Reserved
ETIM9 FAULTREAL
EPWM10_FAULTREAL
Reserved
Reserved
ETIM10 FAULTREAL
EPWM11FAULTREAL
Reserved
Reserved
ETIM11 FAULTREAL
Reserved
Reserved
ETIM12_FAULTREAL
STM2_0CO
Reserved
Reserved
ETIM13_FAULTREAL
STM2_0C1
Reserved
Reserved
ETIMOUT12
STM2_0C2
Reserved
Reserved
ETIMOUT13
STM2_0C3
Reserved
Reserved
Reserved
STM3_0CO
Reserved
Reserved
Reserved
STM3_0CT
Reserved
Reserved
Reserved
STM3_0C2
Reserved
Reserved
Reserved
STM3_0C3
Reserved
Reserved
Reserved
STM4_OC0
Reserved
Reserved
Reserved
STM4_0C1
Reserved
Reserved
Reserved
STM4_0C2
Reserved
Reserved
Reserved
STM4_0C3
h7137
Reserved
Reserved
Reserved
STMS_OCO
Reserved
Reserved
Reserved
ETHO
Reserved
Reserved
CMP_OUT16
STM5_OC2
Reserved
Reserved
CMP_OUT17
STMB_0C3
Reserved
Reserved
CMP_OUT18
Reserved
Reserved
Reserved
CMP_OUT19
Reserved


### 【右页】

Reserved
Reserved
CMP_OUT20
Reserved
Reserved
Reserved
CMP_OUT21
Reserved
XBAR.SPEC【28】
OUTPUTXBAR支持对选通信号进行高
电平锁存操作，锁存信号可配置清零
XBAR.SPEC【29】
OUTPUT-XBAR支持输出使能和输出极
性配置
XBAR.SPEC【30】OUTPUTXBAR支持同步路径，CMPC
分一路同步后的事件信号给OUTPUTXBAR→OUTPUT
XBAR支持异步路径，通过WARPMUX2配置选择；非异
步路径同步处理后再取沿及展宽
XBAR.SPEC【31】OUTPUTXBAR支持输出信号展宽，固
定展宽16拍，是否展宽可配置
XBAR.SPEC【32】
支持OUTPUTXBAR输出14bit，连接
到 IOMUX
XBAR.SPEC33】
支持软件可配置14bitCFGOPXBSWx
寄存器，分别对应14个OUTPUTXBAR输出
1080F



---
## 图像编号 2 (原图: `GameViewer_3njiF8SofL.png`)

### 【左页】

发脉冲会被复用为dma的触发源；使用该脉冲作为DMA触发
源时需要在DMAMUX进行配置
BIMCU huan
8.遗留问题
9.参考文献
[1]
Microchip CLC.pdf
BTNCU huan. T1
BTMCU huan.JS
[2]
ET3101 OR DR.xlsx
文档结尾
BTMCU huan
RTMCU huan.7i
BIMCU


### 【右页】

&TMCU muan.11
BTCU muan.13
ETNCU mar 11 2026-10-02-21 59
ZTMOU
ETMCV hian.11
fps
297 I
331 I
12080F



---
## 图像编号 3 (原图: `GameViewer_7jsvVSVHdw.png`)

### 【左页】


#### 5.6CLU逻辑处理模块

逻辑处理模块支持以下8种逻辑处理组合，通过可配置逻辑
单元模式选择寄存器进行选择。其中，D触发器、J-K触发器和
锁存器的相关逻辑采用基于工作时钟的寄存器时序逻辑进行实
现。
ETMCIVhan J1 2026-
ETMCUua.11 2026-10-02-7159
BTNCU P026-10-02-81:59
BIMCU


### 【右页】

AND -OR
OR-XOR
门1
逻辑输出
逻辑输出
门3
门4
MODE<2:0> = 000
MODE<2:0> = 001
4输入AND
S-R锁存器
门1
门2
逻辑输出
逆辑输出
门3
门3
门14
ETNCU hu
MODE<2:0> = 010
MODE<2:0> = 011
带置1和复位功能的1输入D触发器
带复位功能的2输入D触发器
门4
门2
逻辑输出
门1
h.13 2026-10-02-215
门3
门3
MODE<2:0>= 100
MODE<2:0> = 101
带复位功能的J-K触发器
带置1和复位功能的1输入透明锁存器
门4
门2
速辑输出
门2
逻辑输出
门4
门1
门3
ETHCIUhu
MODE<2:0> = 110
MODE<2:0> = 111
12080F



---
## 图像编号 4 (原图: `GameViewer_7vrsONkjgD.png`)

### 【左页】

XBAR.LIMIT.SPEC【02】：当前虽然对各个xbar加入了异步
路径，但由于其它模块目前大多只支持同步信号输入，所以从
inputxbar输入的信号还是要求做同步处理（该部分在IO做），
另外xbar输出也要选择打一拍（ouptxbar可以选择不打拍直接
发送到 GPIO)。
4.接口说明
BTNCI muian.1/2026-10-02-21:
BIMCU 5

#### 4.1接口列表

表1
XBAR模块接口信号说明
信号
输入
说明
输出
xbar hclk
输入
R7MCI hua. 1 2026-10-02-
总线时钟
BIMCU
输入
xbar_hresetn
总线复位信号，低有效
中断
输出
xbar_intr[6-1:0]
XBAR产生的中断信号，高电平有
APB总线
xbar pclk
功能接口
gpio_xbardata[80-1:0]
输入
IO到XBAR的输入信号
ETHOU ?
pflash_ecc_err
EIMCU
pflash_bus_err
输入
dflash_ecc_err
EFC到XBAR的ECC和BUSerror信号
dflash bus err
输入
sarc2xbar_ev[9-1:0]
SARCO/1到XBAR的看门狗超门限事
件信号


### 【右页】

cmpc_ctriph[22*1-1:0]
cmpc_ctrip[22*1-1:0]
输入
cmpc_ctripouth[22*1-1:0]
CMPC0~10到XBAR的比较结果信号
cmpc_ctripout[22*1-1:0]
wdto_req_rec
输入
wdt1 reg rec
看门狗请求事件输入
输入
cpuo_rst_rec
CPU复位请求事件输入
输入
cpu0 lockup
CPU死锁事件输入
输入
cpuo halted
CPUhalted事件输入
cpuo_ecc_err
输入
CPUECC错误事件输入
输入
CPU复位请求事件输入
cpul_rst_rec
同步电平信号，高有效
cpu1_lockup
输入
CPU死锁事件输入
同步电平信号，高有效
输入
cpu1_halted
CPUhalted事件输入
异步电平信号，高有效
输入
cpul_ecc_err
CPUECC错误事件输入
输入
sram_ecc_err
SRAMECC错误事件输入
输入
can_ecc_err
CANECC告警输入
输入
bus timeout
总线超时事件输入
输入
cpuobus err
CPU总线错误事件输入
CPU总线错误事件输入
cpul_bus_err
输入
同步电平信号，高有效
时钟异常事件输入
clock fault
输入
输入
por uv_warn
欠压告警输入
输入
por_ov_warn
过压告警输入
输入
pwr_ocp_wam
过流告警输入
输入
power_err
供电异常告警输入
输入
temp_warn
过温告警输入
输入
stm_oc0_exp[6-1:0]
STM0~6比较器0事件
输入
stm_oc1_exp[6-1:0]
STM0-6比较器1事件
stm_oc2_exp[6-1:0]
输入
STM0-6比较器2事件
输入
stm_oc3_exp[6-1:0]
STM0~6比较器3事件
输入
epwm_xbar_sync[4-1:0]
SPWM到XBAR的SYNC输入
spwm_adcsoca
输入
SPWM到XBAR的ADC触发信号
spwm_adcsocb
输入
etim_pwm_out[14-1:0]
ETIM的PWM输出信号
输入
ETIM的PWM输出使能信号
etim pwm out oe n[14-1:0]
输入
ETIM输出的同步信号
etim sync_out evt
fps
172 Ⅱ
12080F



---
## 图像编号 5 (原图: `GameViewer_b4H5jcq6ED.png`)

### 【左页】

INPUTXBAR实现IO输入信号的XBAR处理，实现结构如
下图所示。
BAR,OUTy
3101A6003INFUT_XB.R处理
相对于6002，前处理模块放到IOMUX处理；
支持实现异步路径输出，异步路径通过输入异步模式寄存器
gpio_async_mod 和输出异步模式寄存器xbar_async_mod 进行配
置选择，仅支持静态配置（在初始化程序完成，切换模式可能
出现毛刺和功能异常），默认选择同步路径。PWMXBAR类同。
如果不止一个GPIO通过MUXOR合并到输出，则只要其中
一个GPIO处于输入异步模式，则整个路径均处于异步模式，
须按照异步模式进行配置。否则，异步模式同步路径可能出现
毛刺。


### 【右页】

-10(no"vBXN
UO_XBAR_PROC
(uluno'svgx)
UI_XBAR_PROC
Ban. J1
INXBAR_OUTTS)
U15_XBAR_PROC
U_NXB
U_XBAR_POST
图2INPUTXBAR模块处理框图
PWMXBAR模块
PWMXBAR实现结构如下图所示。
ETNCUhnar. 1 2026-J0-02-21:59
12080F



---
## 图像编号 6 (原图: `GameViewer_BJDG1Zjxti.png`)

### 【左页】

输入
SRAMECC错误事件输入
sram_ecc_err
同步电平信号，高有效
输入
CANECC告警输入
can_ecc_err
同步电平信号，高有效
输入
总线超时事件输入
bus_timeout
同步电平信号，高有效
BIMCU huan2
输入
cpuo_bus_err
CPU总线错误事件输入
同步电平信号，高有效
输入
CPU总线错误事件输入
cpul_bus_err
同步电平信号，高有效
clock_fault
输入
时钟异常事件输入
同步电平信号，高有效
a2d_pmu_borhl
输入
por_uv_warn
a2d_pmu_borll
同步电平信号，高有效
a2d_pmu_ovrhl
ETNCUhian11200
BINCU 5
输入
por_ov_warn
a2d_pmu_ovrl
同步电平信号，高有效
输入
过流告警输入
pwr_ocp_warn
同步电平信号，高有效
输入
供电异常告警输入
power_err
同步电平信号，高有效
输入
temp_warm
过温告警输入
同步电平信号，高有效
STM0-1比较器0事件
同步脉冲信号，高有效，脉冲宽度软
RTMCUhia.112025
输入
stm_oc0_exp[6-1:0]
BIMCU
件可配，认宽度为16个STM工作时
钟周期
STM0~1比较器1事件
同步脉冲信号，高有效，脉冲宽度软
stm_oc1_exp[6-1:0]
输入
件可配，默认宽度为16个STM工作时
钟周期
STM0~1比较器2事件
stm_oc2_exp[6-1:0]
输入
同步脉冲信号，高有效，脉冲宽度软
件可配，认宽度为16个STM工作时
钟周期
BIMCU
STM0~1比较器3事件
输入
同步脉冲信号，高有效，脉冲宽度软
stm_oc3_exp[6-1:0]
件可配，认宽度为16个STM工作时
钟,周期


### 【右页】

SPWM到XBAR的SYNC输入
输入
epwm_xbar_sync[4-1:0]
单周期同步脉冲信号，高有效
spwm_adcsoca
输入
SPWM到XBAR的ADC触发信号
单周期同步脉冲信号，高有效，
spwm_adcsocb
输入
ETIM的PWM输出信号
etim_pwm_out[14-1:0]
电平或脉冲信号，高有效
输入
ETIM的PWM输出使能信号
etim_pwm_out_oe_n[14-1:0]
电平或脉冲信号，低有效
ETIM输出的同步信号
输入
etim_sync_out_evt
脉冲信号，脉冲宽度为16个eTimer时
10~02-21.56
钟周期，高有效
输出
inputxbar_data[16-1:0]
INPUTXBAR到SRPWM的输出信号
电平或脉冲信号，有效电平可配置
输出
xbar2sarc_cludata[4-1:0]
XBAR到SARC的CLU信号
电平或脉冲信号，有效电平可配置
输出
xbar2etim_cludata[4-1:0]
XBAR到ETIM的CLU信号
电平或脉冲信号，有效电平可配置
输出
xbar2etim_fault[14-1:0]
XBAR到ETIM的fault信号
电平或脉冲信号，有效电平可配置
输出
XBAR到SPWM的fault信号
xbar2spwm_fault[16-1:0]
电平或脉冲信号，有效电平可配置
xbar2stm0_erg_trig_Osrc
输出
xbar2stm0_erg_trig_1src
xbar2stm1_erg_trig_Osrc
xbar2stml_erg_trig_1src
xbar2stm2_erg_trig_Osrc
xbar2stm2_erg_trig_1src
xbar2stm3_erg_trig_Osrc
XBAR到STM0~1的紧急触发源信号
xbar2stm3_erg_trig_1src
电平或脉冲信号，高有效
xbar2stm4_erg_trig_Osrc
xbar2stm4_erg_trig_1src
xbar2stm5_erg_trig_Osrc
xbar2stm5_erg_trig_1src
输出
OUTPUTXBAR到IOMUX的输出信号
outputxbar_data[14-1:0]
电平或脉冲信号，有效电平可配置
输出
OUTPUTXBAR到IOMUX的输出信号
outputxbar_data_oe_n[14-1:0]
使能
电平或脉冲信号，低有效
输出
XBAR到HAC的CPUhalted信号
cpuo_halted_sync
dan
同步电平信号，高有效
cpul halted sync
输出
XBAR到HAC的CPUhalted信号
11080F



---
## 图像编号 7 (原图: `GameViewer_CpOsnywQhu.png`)

### 【左页】

XBAR.SPEC【13】
INPUTXBAR支持送出5个中断源
XBAR.SPEC【14】
INPUTXBAR支持异步路径，以减小封
ETNO
波延迟及其它用应用场景，输出端通过WARP_MUX2配置
选择；
XBAR.SPEC【15】INPUT XBAR 输出连接到中断模块、
SRPWM、ETIMER、SARC、PWM XBAR、ETIM XBAR、
OUTPUTXBAR，及 ETIM & SARC& OUTPUTCLU
BTMCU huan 71
ETMCU mian.11
EIMCU hian.li
ETMCV han.1i 2026-70-02-71:58
ETMCUhian218026-10-02-21:58
BTMQU Tzuan. li


### 【右页】

GPI00-
GPIOX
INPUT XBAR
TMCU han.11
INT
SRPWM
PWM XBAR
E TIM XBAR
HCV huan.Ji 2026-10-02-21-58
16 oupluL
EIIMER
ETIM CLU
SARCCLU
SARC
TNCV
OUTPUT CLU
XBAR

#### 3.3PWMXBAR

ETCV
ET6801修改点：
12080F



---
## 图像编号 8 (原图: `GameViewer_CqeT5pUL1x.png`)

### 【左页】

Reserved
INPUTXBAR6
Reserved
CPUO_HALT
Reserved
Reserved
Reserved
FLASH_ ERR
INPUTXBAR7
Reserved
Reserved
ETIMOUT7
Reserved
Reserved
Reserved
CPUI HALT
INPUTXBARS
Reserved
Reserved
ETIMOUTS
Reserved
Reserved
Reserved
Reserved
Reserved
INPUTXBAR9
Reserved
ETIMOUT9
Reserved
Reserved
Reserved
ETIMOUT10
INPUTXBAR10
Reserved
Reserved
ETIMOUT11
Reserved
Reserved
Reserved
ETIMOUT12
INPUTXBAR11
Reserved
Reserved
ETIMOUT13
Reserved
Reserved
Reserved
SRPWM_XBAR_SYNCO
Reserved
INPUTXBAR12
Reserved
SRPWM_XBAR_SYNC1
Reserved
Reserved
Reserved
SRPWM_XBAR_SYNC2
Reserved
INPUTXBAR13
ERRORSTS
SRPWM_XBAR_SYNC3
EPWMO_FAULTREAL
Reserved
Reserved
ETIMO_FAULTREAL
EPWM1_FAULTREAL
INPUTXBAR14
Reserved
ETIM1_FAULTREAL
EPWM2_FAULTREAL
Reserved
Reserved
ETIM2_FAULTREAL
EPWM3_FAULTREAL
Reserved
INPUTXBAR15
ETIM3_FAULTREAL
EPWM4_FAULTREAL
Reserved
Reserved
ETM4_FAULTREAL
Reserved
EPWM5_FAULTREAL
Reserved
ETIM5_FAULTREAL
Reserved
EPWM6_FAULTREAL
Reserved
ETIM6_FAULTREAL
EPWM7_FAULTREAL
Reserved
Reserved
ETIM7_FAULTREAL
Reserved
EPWM8_FAULTREAL
Reserved
ETIM8_FAULTREAL
EPWM9_FAULTREAL
Reserved
Reserved
ETIM9_FAULTREAL
EPWM10_FAULTREAL
Reserved
Reserved
ETIM10_FAULTREAL
EPWM11_FAULTREAL
Reserved
Reserved
ETIM11_FAULTREAL
Reserved
Reserved
Reserved
ETIM12_FAULTREAL
Reserved
Reserved
Reserved
ETIM13_FAULTREAL
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
STCU
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved
Reserved


### 【右页】

Reserved
Reserved
CMP_EVT16
Reserved
Reserved
Reserved
CMP_EVT17
Reserved
Reserved
Reserved
CMP_EVT18
Reserved
Reserved
Reserved
CMP_EVT19
Reserved
Reserved
Reserved
CMP_EVT20
Reserved
Reserved
Reserved
CMP_EVT21
Reserved
XBAR.SPEC【17】
PWMXBAR支持对选通信号进行高电
平锁存操作，锁存信号可配置清零
XBAR.SPEC【18】
IPWMXBAR支持输出使能和输出极性
配置
XBAR.SPEC【19】
PWMXBAR支持异步路径，以减小封
波延迟，输出端通过WARPMUX2配置选择
XBAR.SPEC【20】
支持PWMXBAR输出16bit，顶层选择
后分别连接到12个PWM通道

#### 3.4ETIM XBAR

ET6801修改点：
16）新增CMPC通道 CMP_EVT7>21；新增CMP_EVT*_OR_EVT*
17）新增SDFM通道SD2/3FLT*EVT*；新增SD*FLT*_EVT0_OR_EVT1
18）新增 CPU1_HALT
269 n
1080F



---
## 图像编号 9 (原图: `GameViewer_DjSL3rXWx4.png`)

### 【左页】

202F-10-02-21:58
ETMCU muan 11
WTMCU
ETMCU huar: 11
EJMCU huan J1 2026-10-02-31-58
RTMCU huan.S
BTMCU Thian.11
ETMC11 7181.J1
ETMCI maan. 1i
BTHCV hian 11 8026-10-02-21:58
Q026-10-02-21:58


### 【右页】

修订记录
ETMOU
ETMCV mvan.15
版本号
修订内容
修订日期
修订人员
V1.0
首次修订
肖均
V1.1
OUTPUTXBAR输出位宽由8bit修改为14bit
肖均
OUTPUTXBAR交换ERRORSTS和EXTSYNCOUT位置，与其他表
V12
肖均
格保持一致
刷新支持锁定寄存器内容
肖均
V1.3
增加INPUTXBAR滤波窗口配置分组描述
增加OUTPUTXBAR输出模式选择描述
刷新接口信号列表
肖均
V1.4
刷新接口信号特征表
V1.5
增加4.3节信号对应关系
肖均
V1.5
修改XBAR.SPEC<04>表格部分信号名后缀
8G:10-00-01-9200
肖均
2026-10~12-27
在6002的基础上修改3101和6003的xbar
V2.0
袁云龙
V2.1
OPXB和COXB新增异步处理
袁云龙
对inputxbar/pfxb/cbxb/cixb新增展宽处理以适应srpwm100M场
袁云龙
V2.2
V3.0
ET6801xbar:信号源变化，对标p65x
袁云龙
V3.1
修改DMA触发源描述
袁云龙
V4.0
更新ET6601XBAR修改点
牛婷婷
12080F



---
## 图像编号 10 (原图: `GameViewer_FilEyIUnoO.png`)

### 【左页】

5. 方案设计

#### 5.1 INPUT XBAR 模块


#### 5.2PWMXBAR模块

WTMCU an. li

#### 5.3ETIMXBAR模块


#### 5.4 OUTPUT XBAR 模块


#### 5.5XCSA/XCET/XCOX模块


#### 5.6 CLU逻辑处理模块

EINCU huan, J1 2026-10-02-21-58

#### 5.7 CLU中断事件触发

KTMCU S
6. 寄存器设计
7. 中断说明
8.遗留问题
9. 参考文献
ETMC1 17137.J1
ETMCI muan. 1i
ETICV
BTMC hian 1i
ETMCU Tuan. 1i


### 【右页】

1. 概述
XBAR（crossbar）模块主要功能，是为芯片的输入管脚、输
出管脚和内部模块之间提供灵活的连接关系，这些连接关系可
通过配置进行选择，同时可通过内部集成的CLU（configurable
logic unit）对部分连接关系进行逻辑运算，以提供更大的灵活
性和可能性。
ET3101:本文档为在6002xbar文档的基础上进行修改，主要
修改包括
1.修改input-xbar，去除前处理模块（该部分被放在IOMUX
处理);
2.对所有xbar加入了异步路径；
3.加入了 clb_ inputxbar/clb_xbar/clb_output_xbar
4.修改了opxb和coxb的结构，5对上报和同步加入了异步处
理 jiraET3101-77;
5.GPIO的数量由84个变为80个。
ETMCVmuan.11 2026-10-
ET6801修改点：
1080F



---
## 图像编号 11 (原图: `GameViewer_Gg0PKIieqf.png`)

### 【左页】

STIM TRSEL(STIMER
Triger Selection），输出送往
STIMER(6*32bit stimer) ;
■SAXB(ADCXBAR)，输出送往ADC;
■EFXB(ETIMER Fault_in XBAR)，输出送往 ETIMER;
■OPXB(Output XBAR)，输出送往 IOMUX;
■CLU 模块，输入信号来源为INPUT XBAR，输出到 SARC、
ETIM 和 Output XBAR。
BTMG
■CIXB(CLB INPUTXBAR)，输出送往 CLB;
■CBXB(CLBXBAR)，输出送往CLB
■COXB(CLBOUTPUTXBAR)，输出送往 IOMUX
■cbb_int_gen 中断处理模块
STMCU
3.需求规格

#### 3.1整体

hian 1i8026-10-02-21:58
XBAR.SPEC【01]
XBAR模块支持AMBA3APB总线接口
协议


### 【右页】

XBAR.SPEC【02】
支 持_INPUT XBAR， PWM XBAR,
ETIMER XBAR和OUTPUT XBAR，支 持_CLB_INPUT
XBAR,CLB XBAR,CLB OUTPUTXBAR
XBAR.SPEC【03】
支持STIMER紧急故障触发源输出
XBAR.SPEC【04】
XBAR支持输入故障使能和合并，通过
配置Fault对应bit使能实现；支持将errorsts
（flash|syserr|PT_err）发送到IO
signal name ofimput
bit width
bit order
pllash_ecc_err
plash_bus_err
dflash_ecc_e
合并为FLASH_ERR
dflash_bus_er
wdto_req_rec
wdt1_req_rec
cpuo_rst _rec
cpu0_lockup
NCVTRU8n.11 2026-10-02-21
cpul_rst _rec
cpul_lockup
合并为SYS_ERR
cpul_ecc_err
sram_ecc_err
can_ecc_err
bus_timeout
cpu0_bus_en
cpul_bus_en
Hcmian.11
por_uv_warm
por_ov_warm
合并为PT_ERR
pw_ocp_wam
power_err
Q026-10-02-21:58
11080F



---
## 图像编号 12 (原图: `GameViewer_K9wJHSnqdx.png`)

### 【左页】

202F-10-02-21:58
ETMCU muan 11
WTMCU huan.Ji
ETMCU huar: 11
EJMCU huan J1 2026-10-02-31-58
BTMCUhuan.S
BTMCU Thian.11
ETMC11 7181.J1
ETMCI maan. 1i
BTHCV hian 11 8026-10-02-21:58


### 【右页】

目录
ETMCU han. 11
ETHCV hvan.15
1.概述
2. 功能描述
3.需求规格
BTMCIIhuaY.T1

#### 3.1整体

BTMCU hoan.13 2026-10-02-27-58

#### 3.2 INPUT XBAR


#### 3.3 PWM XBAR


#### 3.4 ETIM XBAR

han 11 2026-10-08-21:58

#### 3.5 OUTPUT XBAR

ETMC/ Hun 13 2026-10-m2-27

#### 3.6 CLU


#### 3.7 XBAR约束

4. 接口说明

#### 4.1 接口列表


#### 4.2接口信号特征

RTMCI/Taan.11
ETMCV man.11

#### 4.3信号对应关系

12080F



---
## 图像编号 13 (原图: `GameViewer_LS0PAMbqAJ.png`)

### 【左页】

ETIMOUT7
etim pwm_out[7]
输入信号
ETIMOUT8
etim_pwm_out[8]
输入信号
ETIMOUT9
etim_pwm_out[9]
输入信号
ETIMOUT10
etim_pwm_out[10]
输入信号
ETIMOUT11
etim pwm _out[11]
输入信号
etim_pwm_out[12]
输入信号
ETIMOUT12
BIMCU huan
ETIMOUT13
etim_pwn_out[13]
输入信号
inxb _ dout[0]
INPUTXBAR0
INPUTXBAR 输出
inxb_ dout[1]
INPUTXBAR1
INPUTXBAR输出
INPUTXBAR2
inxb_ dout[2]
INPUTXBAR 输出
INPUTXBAR3
inxb dout[3]
INPUTXBAR输出
INPUTXBAR4
inxb_ dout[4]
INPUTXBAR输出
inxb_ dout[5]
INPUTXBAR5
INPUTXBAR 输出
INPUTXBAR6
inxb dout[6]
INPUTXBAR输出
INPUTXBAR 输出
inxb_dout[7]
INPUTXBAR7
BTMCU S
inxb_ dout[8]
INPUTXBAR8
INPUTXBAR输出
inxb_ dout[9]
INPUTXBAR9
INPUTXBAR输出
inxb_dout[10]
INPUTXBAR10
INPUTXBAR输出
INPUTXBAR11
inxb_ dout[11]
INPUTXBAR输出
inxb dout[12]
INPUTXBAR12
INPUTXBAR 输出
inxb_dout[13]
INPUTXBAR13
INPUTXBAR 输出
inxb_ dout[14]
INPUTXBAR14
INPUTXBAR输出
inxb_ dout[15]
INPUTXBAR15
INPUTXBAR 输出
SRPWM_XBAR_SYNCO
epwm_xbar_sync[0]
输入信号
BIMCU
SRPWM_XBAR_SYNC1
epwm_xbar_sync[1]
输入信号
epwm_xbar_sync[2]
SRPWM XBAR_SYNC2
输入信号
epwm_xbar_sync[3]
SRPWM_XBAR_SYNC3
输入信号
ADCSOCAO
spwm_adcsoca
输入信号
ADCSOCBO
spwm_adcsocb
输入信号
EXTSYNCOUT
etim_sync_out_evt
输入信号
cpul _halt
CPU1_HALT
输入同步后信号
CPU2_HALT
cpu2_ halt
输入同步后信号
FLASH_ERR
flash err
内部产生，参见错误列表
EIMCU
SYS_ERR
sys_err
内部产生，参见错误列表
PT ERR
pt err
内部产生，参见错误列表
ERRORSTS
errorsts
flash_err sys_err |pt_err
CFG ETXB SWx
cfg etxb sw[*]
配置信号，*对应每个输出bit


### 【右页】

CMP_OUTO
cmpc_ctripouth[0]
输入信号
CMP_OUT1
cmpc_ctripout[0]
输入信号
CMP_OUT2
cmpc_ctripouth[1]
输入信号
CMP_OUT3
cmpc_ctripout[1]
输入信号
CMP OUT4
cmpc_ctripouth[2]
输入信号
CMP_OUT5
cmpe_ctripoutl[2]
输入信号
CMP_OUT6
cmpc_ctripouth[3]
输入信号
CMP_OUT7
cmpc_ctripout[3]
输入信号
CMP_OUT8
cmpc_ctripouth[4]
输入信号
CMP_OUT9
cmpc_ctripout[4]
输入信号
CMP_OUT10
cmpc_ctripouth[5]
输入信号
CMP_OUT11
cmpc_ctripout[5]
输入信号
CMP_OUT12
cmpc_ctripouth[6]
输入信号
CMP_OUT13
cmpc_ctripout[6]
输入信号
CMP_OUT14
cmpc_ctripouth[7]
输入信号
CMP_OUT15
cmpc_ctripout[7]
输入信号
cmpc_ctripouth[8]
CMP_EVT16
输入信号
cmpc_ctripout[8]
CMP_EVT17
输入信号
CMP_EVT18
cmpc_ctripouth[9]
输入信号
CMP EVT19
cmpc_ctripoutl[9]
输入信号
输入信号
CMP_EVT20
cmpc_ctripouth[10]
CMP_EVT21
cmpc_ctripoutl[10]
输入信号
CMP_OUT0_OR_OUT1
cmpc_ctripouth_or [0]
cmpc_ctripouth[0] cmpc_ctripout[0]
CMP_OUT2_OR_OUT3
cmpc_ctripouth_or_ []
cmpc_ctripouth[1] cmpc_ctripoutl[]
CMP_OUT4_OR_OUT5
cmpc_ctripouth_or_1[2]
cmpc_ctripouth[2] cmpc_ctripoutl[2]
CMP_OUT6_OR_OUT7
cmpc_ctripouth _or 1[3]
cmpc_ctripouth[3] cmpc_ctripout[3]
CFG_OPXB_SWx
cfg_opxb_sw[]
配置信号，*对应每个输出bit
STMO_OCO
stm_oc0_exp[0]
输入信号
STM0_OC1
stm_oc1_exp[0]
输入信号
STM0_0C2
stm_oc2_exp[0]
输入信号
STM0_OC3
stm_oc3_exp[0]
输入信号
STM1_0CO
stm_oc0_exp[1]
输入信号
stm_oc1_exp[1]
STM1_0C1
输入信号
stm_oc2_exp[1]
STM1_0C2
输入信号
STM1_0C3
输入信号
stm oc3 exp[1]
输入信号
stm_oc0_exp[2]
STM2_OC0
输入信号
stm oc1 exp[2]
STM2 0C1
fps
12080F



---
## 图像编号 14 (原图: `GameViewer_m38yfM9SyS.png`)

### 【左页】

temp_wam
XBAR.SPEC【05】
支持 XCSA、XCET和 XCOX 三个 CLU
可配置逻辑组合功能
XBAR.SPEC【06】支持XBAR中断上报，INPUTXBAR支
持5个中断独立输出，CLU模块支持中断合并输出，对每
个中断源，可配置中断使能、中断屏蔽、中断清除、强制
中断．可查询原始中断和中断状态
XBAR.SPEC【07】支持XBAR配置锁定，通过配置一个
16bitKEY实现寄存器写保护，支持写保护的寄存器包括：
Fault使能配置、Stimer紧急触发源配置、CLU相关配置、
滤波窗口、滤波使能配置、输入输出极性配置、MUX-OR
配置、输入输出使能配置、输出选择配置、软件信号源配
置、输出脉宽扩展配置、输出模式选择
XBAR.SPEC【08】支持触发源状态上报（待定？
暂不
实现）
BTMCUh
ETMCU hian li
EIMQU tauan


### 【右页】


#### 3.2INPUT XBAR

XBAR.SPEC【09】mINPUTXBAR支持输入信号源来自芯片
IOcellC端经过处理后的信号(bypass/sync/3sample/6sample),
覆盖80个GPIO输入
J12026-10-02-2158
Epi_in_modl
spi,i_mody
IOMUX
CMos
PAD
opou'jno"gd?
IOCTRL
pomno'gds
OEN
DST
XBAR.SPEC 【10】
INPUTXBAR支持对信号进行4bit分组
并进行mux-or选通
XBAR.SPEC【11】
INPUTXBAR支持对选通信号进行高电
平锁存操作，或上下沿检测操作，锁存信号可配置清零
XBAR.SPEC【12】
INPUTXBAR支持输出使能和输出极性
配置
1080F



---
## 图像编号 15 (原图: `GameViewer_nneQMiNCGh.png`)

### 【左页】

STM2_0C2
stm_oc2_exp[2]
输入信号
STM2_0C3
stm_oc3_exp[2]
输入信号
stm_oco_exp[3]
STM3_0C0
输入信号
STM3_0C1
stm_oc1_exp[3]
输入信号
STM3 0C2
stm_oc2 exp[3]
输入信号
输入信号
stm_oc3_exp[3]
STM3_0C3
BIMCU huan?
STM4_0C0
stm_oco_exp[4]
输入信号
STM4_0C1
stm_oc1_exp[4]
输入信号
stm_oc2_exp[4]
STM4_OC2
输入信号
stm_oc3_exp[4]
STM4_0C3
输入信号
STM5_0C0
stm_oc0_exp[5]
输入信号
STM5_0C1
stm_oc1_exp[5]
输入信号
STM5_0C2
stm_oc2_exp[5]
输入信号
STM5_OC3
stm_oc3_exp[5]
输入信号
xcox_dout[0]
OUTPUTXBARCLU输出信号
INPUTXBAR_CLU2OUT[0]
BTMCU S
xcox_ dout[1]
INPUTXBAR_CLU2OUT[1]
OUTPUTXBARCLU输出信号
xcox_dout[2]
INPUTXBAR_CLU2OUT[2]
OUTPUTXBARCLU输出信号
INPUTXBAR_CLU2OUT[3]
xcox_dout[3]
OUTPUTXBARCLU输出信号
Reserved
1b0
保留位
OUTPUT_XBRO
outputxbar_data[0]
output_xbar的输出信号
OUTPUT_XBR1
outputxbar _data[1]
output_xbar的输出信号
OUTPUT_XBR2
outputxbar _data[2]
output_xbar的输出信号
OUTPUT_XBR3
outputxbar_data[3]
output_xbar的输出信号
OUTPUT_XBR4
outputxbar _data[4]
output_xbar的输出信号
BIMCU
OUTPUT_XBR5
outputxbar
_data[5]
output_xbar的输出信号
OUTPUT_XBR6
outputxbar
data[6]
output_xbar的输出信号
outputxbar_data[7]
OUTPUT_XBR7
output_xbar的输出信号
OUTPUT_XBR8
outputxbar _data[8]
output_xbar的输出信号
OUTPUT_XBR9
outputxbar _data[9]
output_xbar的输出信号
outputxbar _data[10]
OUTPUT_XBR10
output_xbar的输出信号
OUTPUT_XBR11
[1tjexep reqxndino
output_xbar的输出信号
OUTPUT_XBR12
outputxbar_data[12]
output_xbar的输出信号
OUTPUT_XBR13
outputxbar _data[13]
output_xbar的输出信号
EIMCU
epwm2xbar_fault_real[0]
EPWMO_FAULTREAL
输入信号
EPWM1_FAULTREAL
epwm2xbar_fault_real[1]
输入信号
EPWM2_FAULTREAL
epwm2xbar_fault_real[2]
输入信号
EPWM3_FAULTREAL
epwm2xbar_fault_real[3]
输入信号


### 【右页】

EPWM4 _FAULTREAL
epwm2xbar_fault_real[4]
输入信号
EPWM5_FAULTREAL
epwm2xbar_fault_real[5]
输入信号
EPWM6_ FAULTREAL
epwm2xbar_fault_real[6]
输入信号
EPWM7_FAULTREAL
epwm2xbar_fault_real[7]
输入信号
EPWM8_FAULTREAL
epwm2xbar_fault_real[8]
输入信号
EPWM9_ FAULTREAL
epwm2xbar_fault_real[9]
输入信号
EPWM10_FAULTREAL
epwm2xbar_fault_real[10]
输入信号
EPWM11_ FAULTREAL
epwm2xbar_fault_real[11]
输入信号
etim2xbar_fault_real[0]
ETIMO_FAULTREAL
输入信号
ETIMI_FAULTREAL
etim2xbar_fault_real[1]
输入信号
ETIM2 FAULTREAL
etim2xbar_fault_real[2]
输入信号
ETIM3_ FAULTREAL
etim2xbar_fault_real[3]
输入信号
ETIM4 FAULTREAL
etim2xbar_fault_real[4]
输入信号
ETIM5 FAULTREAL
etim2xbar_fault_real[5]
输入信号
ETIM6 FAULTREAL
etim2xbar_fault_real[6]
输入信号
ETIM7 FAULTREAL
etim2xbar_fault_real[7]
输入信号
ETIM8_ FAULTREAL
etim2xbar_fault_real[8]
输入信号
ETIM9_FAULTREAL
etim2xbar_fault_real[9]
输入信号
ETIM10_FAULTREAL
etim2xbar_fault_real[10]
输入信号
ETIM11_FAULTREAL
etim2xbar_fault_real[11]
输入信号
ETIM12_FAULTREAL
输入信号
etim2xbar_fault_real[12]
ETIMI3FAULTREAL
etim2xbar_fault_real[13]
输入信号
XCLK_OUT
xclkout
CRG XCLK
5.方案设计

#### 5.1 INPUT XBAR 模块

ET6801:去除了3101中增加的展宽的逻辑；
fps
ms
12080F



---
## 图像编号 16 (原图: `GameViewer_NY8OuaK0XB.png`)

### 【左页】

输出
inputxbar_data[16-1:0]
INPUTXBAR到其他模块的输出信
xbar2sarc_cludata[4-1:0]
输出
XBAR到SARC的CLU信号
xbar2etim cludata[4-1:0]
输出
XBAR到ETIM的CLU信号
输出
xbar2etim_fault[14-1:0]
XBAR到ETIM的fault信号
输出
XBAR到SPWM的fault信号
xbar2spwm_fault[16-1:0]
BIMCU huan
xbar2stm0_erg_trig_Osrc
输出
xbar2stm0_erg_trig_1src
xbar2stm1_erg_trig_Osrc
xbar2stml_erg_trig_1src
xbar2stm2_erg_trig_Osrc
xbar2stm2_erg_trig_1src
xbar2stm3_erg_trig_Osrc
XBAR到STM0~5的紧急触发源信号
xbar2stm3_erg_trig_1src
xbar2stm4_erg_trig_Osrc
xbar2stm4_erg_trig_1src
xbar2stm5_erg_trig_0src
ETMCUman11202
BIMCU huan. 5
xbar2stm5_erg_trig_1src
输出
outputxbar_data[14-1:0]
OUTPUTXBAR到IOMUX的输出信
输出
outputxbar_data_oe_n[14-1:0]
OUTPUTXBAR到IOMUX的输出信
号使能
输出
cpuo_halted_sync
XBAR到HAC的CPUhalted信号
cpu1 halted sync
输出
XBAR到HAC的CPUhalted信号
输入
sysc testpin0_sel[7:0]
TESTPINO选择信号
sysc_testpin1_ sel[7:0]
输入
TESTPIN1选择信号
输入
BIMCU
sysc testpin2_sel[7:0]
TESTPIN2选择信号
sysc testpin3 sel[7:0]
输入
TESTPIN3选择信号
输出
xbar testpin[4-1:0]
XBAR到SYSC的TESTPIN信号
输出
xint_dma_req[4:0]
xbar的中断脉冲被发送到DMAMUX
作为触发源
输出
xint_dma_single[4:0]
xbar的中断脉冲被发送到DMAMUX
作为触发源
输出
errorsts
flash err|sys _errIpt err
muanli
epwm2xbar_faultreal[11:0]
输入
srpwm fault real
etim2xbar_fault_real [13:0]
输入
etim fault_real
EIMCU
xclkout
输入
crg_xclk


### 【右页】


#### 4.2接口信号特征

表2
XBAR接口信号特征
ETHCU huan, Ji
信号
输入输
说明
输入
gpio_xbar_data[80-1:0]
IO到XBAR的输入信号
异步信号，电平或脉冲
pflash_ecc_err
pflash_bus_err
EFC到XBAR的ECC和BUSerror信号
输入
dflash_ecc_err
同步电平信号，高电平表示error有
效，EFC软件清0
dflash bus err
SARCO/1到XBAR的看门狗超门限事
件信号
输入
sarc2xbar_evt[9-1:0]
同步脉冲信号，高有效，脉冲宽度取
决于输入电压、参考比较值和对应
ADC虚拟通道采样频率
cmpc_ctriph[22*1-1:0]
CMPC0~3到XBAR的比较结果信号，
cmpc_ctripl[22*1-1:0]
输入
同步脉冲信号，高有效，最小脉冲宽
cmpc_ctripouth[22*1-1:0]
cmpc ctripoutl[22*1-1:0]
度为1个CMPC时钟周期
wdto_req_rec
看门狗请求事件输入
输入
wdt1_req_rec
同步电平信号，高有效
输入
CPU复位请求事件输入
同步电平信号，高有效
输入
CPU死锁事件输入
cpuo_lockup
同步电平信号，高有效
输入
CPUhalted事件输入
cpuo_halted
异步电平信号，高有效
输入
cpuo_ecc_err
CPUECC错误事件输入
同步电平信号，高有效
CPU复位请求事件输入
输入
cpul_rst_rec
huan
同步电平信号，高有效
输入
cpul_lockup
CPU死锁事件输入
同步电平信号，高有效
CPUhalted事件输入
cpul_halted
输入
异步电平信号，高有效
dan
CPUECC错误事件输入
cpul_ecc_err
输入
同步电平信号，高有效
167 Ⅱ
11080F



---
## 图像编号 17 (原图: `GameViewer_nYxX2xZgHL.png`)

### 【左页】

沿展宽
经过异步处理后下降
沿展宽
BIMCU Tuan 1i
etim的输入
OR
cfg_oemod[1:0]
dout_oe_n
1 'b1
1 'b0
TNCYhhan J12026
BTMCU huan. S

#### 5.5 XCSA/XCET/XCOX 模块

XBAR中包含三组CLU处理模块，根据连接关系不同，分
为XCSA、XCET和XCOX，C三个模块独立配置，实现完全一
致。主要完成简单逻辑组合实现和选择，以及中断上报。具体
实现结构如下图所示。
BIMCU


### 【右页】

沿中断检测
遥标0
LNXBAR_CLU2SARCI
&TMCU muan. J1
DNXEAR OLT
DNXBAROUT
INXBAR
OLT
INXBAR,CLL2SARC[9-
U_XCSA
da_outs
DXBAR_OUT
NXBAKOUT
沿中断检
DXBAR_OLT
适标0
DNXBAR_OUT3
-DNX BAR,CLUETIMP)
FTNCU 59
IXBAKOUTIL!
U3_CLU
DNXBAR_CLU2ETD43}
DXBAR_OUT|IS
U_XCET
de_onta
che_pol
DXBAR_OLTIO
中心
DXBAROUTU
LIX BAK OUTI
DXBAR_OUT[3]
DNXBAR_CLU2OUTP)-
INXBAR_CLU2OUT[3]
U_XCox
ETMChuan.Ji
图4XCSA、
XCET和XCOX模块框图
223 Ⅱ
12080F



---
## 图像编号 18 (原图: `GameViewer_qPba5rmgGl.png`)

### 【左页】

clear/set
-SOURCE[X)-
6002ETIMPUT_XBAR处理
OR
EF)B_OUT[X]
pol sd
BIMCU muan
-SOURCE[X)
3101&6003ETIM_XBAR处理
OR
ETIMXBAR支持异步路径；
BTMCU huan. JS

#### 5.4 OUTPUT XBAR 模块

OUTPUTXBAR实现结构如下图所示。
BTMCU fuan. li
SOURCE)x)
6002IOUTPLT_XBAR处理
3101460030LPUT_XBAR修改后处理
50 URCE)x)
OR
OPXB_OUT(X-
EIMCU


### 【右页】

1.OUPUTXBAR支持异步路径；
2.原来 cfg_opxb_exp_en ==1"bo 时，不扩展但打拍输出;
现改为不扩展直接输出；
3.参考LRS.spec[36]，输出 etim_oen 信号(#O＇)在图中表示，
ids文档中包含相关描述：包含配置信号cfg_oemod，为0
或3时输出低有效，,为1时输出 etim_oen；为2时输出高
电平 (无效)

#### 4.2024102185RTL后修改：由于加入了异步路径，dout_oe_n

信号为了保持和pwm同相位，去除了dout_oe_n的寄存输

#### 5.2024102185RTL后修改：相较之前加入了异步处理，信号

若寄存上报以及取沿必须经过异步处理；
cfg_dsel
cfg_expen
结果
异步输出
经过异步处理后输出
锁存值
异步输出
异步输出
经过异步处理后展宽
ETHC/
输出锁存值
经过异步处理后上升
1080F



---
## 图像编号 19 (原图: `GameViewer_qZ6VVLkkSM.png`)

### 【左页】


#### 3.5OUTPUT XBAR

ET6801修改点：
CMP OUT* 0-7>0-21；去除 CMP OUT*OR OUR*
1)
BTMCU huan.
2)
新增SDFM通道SD2/3FLT*EVT*；去除SD*FLT*EVTO_OREVT1
(TI无)
3)
新增 CLB4/5_OUT*
4)
新增 ADCA EXTMUX_SEL4
BTHC/ huan.T1 2026-10-02-
RTMCU huan.JS
5)
无 CPUO_ADCCHECKEVTO
6)
CFG OPXB SWx(TI 无)
7)
SPWM XBAR_SYNCx(TI 无)
8)
INPUTXBAR CLU OUT(TI 无)
9)
STM_OC 3>6(TI 无)
10)
无 FSI
无 EPG*OUT*
12)
新增 CPU1 HALT
13）新增XCLK OUT
BTMO
BIMCU
ET6601修改点：
去除SDFM通道SD*FLT*EVT*


### 【右页】

2)
去除CLB* OUT*
3)
去除 ADCC EVT*
4)
去除EPWM12~17FAULTREAL
ETMCVhuan,1i
5)
新增ETIMOUT12/13和ETIM12/13FAULTREAL
XBAR.SPEC【27】
OUTPUTXBAR支持对输入信号源进行
4bit分组并进行mux-or选通，信号源选择如下表所示：
Reserved
CMP_OUTO
ADCA_EVTO
ETIMOUTO
CMP_OUT1
INPUTXBARO
Reserved
Reserved
Reserved
ADCA_EVT1
CMP_OUT2
ETIMOUT1
Reserved
CMP_OUT3
INPUTXBAR1
Reserved
CMP_OUT4
Reserved
ADCA_EVT2
ETIMOUT2
CMP_OUT5
INPUTXBAR2
Reserved
Reserved
CMP_OUT6
Reserved
ADCA_EVT3
ETIMOUT3
CMP_OUT7
INPUTXBAR3
Reserved
Reserved
CMP_OUT8
Reserved
ADCB_EVTO
ETIMOUT4
CMP_OUT9
Reserved
INPUTXBAR4
STMO_OCO
CMP_OUT10
ADCB_EVT1
Reserved
ETIMOUT3
CMP_OUT11
Reserved
INPUTXBAR5
STM0_OC1
CMP_OUT12
Reserved
ADCB_ EVT2
ETIMOUT6
CMP_OUT13
ADCSOCAO
Reserved
STMO_0C2
Reserved
ADCB_EVT3
EXTSYNCOUT
CMP_OUT15
ADCSOCBO
Reserved
STM0_OC3
Reserved
FLASH ERR
Reserved
ERRORSTS
Reserved
INPUTXBAR6
Reserved
STM1_0CO
Reserved
Reserved
CPUO_HALT
Reserved
Reserved
INPUTXBAR7
Reserved
ETIMOUT7
STM1_0C1
Reserved
Reserved
CPU1_HALT
Reserved
INPUTXBARS
Reserved
ETMOUT8
Reserved
Reserved
SYS_ERR
STM1_0C2
11080F



---
## 图像编号 20 (原图: `GameViewer_SMcbqY9aCU.png`)

### 【左页】

1.信号列表变动；其中pfxb和opxb信号选择mux32>64;
2.去除之前由于CLB工作在100M增加的展宽电路；
3. inputxbar 中断数量 4>5。
MTMCU man.
ET6601修改点：
1.去除
CLB
INPUT XBAR、CLB OUTPUT XBAR
CLB XBAR;
ETMCL
2.OUTPUT_XBAR 输出从’12 位修改为 14 位；（up to final
1Olist)
3.寄存器配置接口从AMBA3AHBLite改为AMBA3AHB,
nManager改为APB接口生成ids 文件。（xbar_cfg写pclk脉
冲用hclk取沿，xbar_cfg读hclk脉冲需要展宽，有哪些信
号？）
4.复位可配置不受WDG和系统软复位影响
BTIChian 1i2026-
ETMCIhian1i2026-
ETMCU Tuan.li


### 【右页】

2.功能描述
han.13
DESIINAHOP
图1.XBAR模块结构框图
Tuan.112026-10-02-271
XBAR支持对GPIO输入信号和来自内部模块的信号进行选
择、逻辑计算等处理，处理后的信号可送往SRPWM、ADC、
ETIMER、STIMER、CLB-和IO，作为后级模块的信号输入？
触发事件或故障处理信号。
XBAR主要由以下几个模块组成：
TMCVmuanli
■INXB(INPUTXBAR)，输出送往各内部模块；
■PFXB(PWMXBAR)，输出送往SRPWM;
2080F



---
## 图像编号 21 (原图: `GameViewer_tikzmykACG.png`)

### 【左页】

图5CLU模块逻辑处理模式
T5.7 CLU中断事件触发
hian
BIMCU huain
CLU模块支持对输出信号进行信号沿检测，并产生中断事件
脉冲信号。可通过cfg_xc*_intedg_sel[1:0]配置，检测信号上升
沿，下降沿，或同时检测上升沿和下降沿。
ETMCI
imedg,se[0]
BTMOU5
中断源检测
Th_dou
中断源脉冲
fg_xrt_intedg_sel[1]
中断源检测
ETMCU han.11 2026-10-02-071
图6CLU模块中断源产生
6.寄存器设计
. Ti 2026-10-0
参见文档：xbarids.docx


### 【右页】

7.中断说明
xcox3
&TNCU Tmuan. J1
xcox2
xcoxl
xcox0
xcet3
clu_i nt_sre_pul se[11:d]
xcet2
cbb_int_genl
xcetl
xcet0
xcsa3
[]qx
ETCU man.11 2026-10-02-21 59
xcsa2
xcsal
xbar_intrl5: 0]
xcsa0
xbar_ihtr[4: 0]
inxb_dout [15:11]
cbb_int_gen0
input_xbar
xint_dmg_req[4: 0]
xint_dmg_single[4: 0]
图70xbar中断结构
xbar例化了两个cbb_int_gen，分别处理来自INPUTXBAR和
CLU的中断;
INPUTXABR的输出【15：11】作为中断触发源，同时该触
1080F



---
## 图像编号 22 (原图: `GameViewer_V3t3Z6WQYi.png`)

### 【左页】

SOURCE[X]
6002PWMPUT_XBAR处理
OR
PFXB_OUT[X}
BTMO
pol,sd
BIMCU Tuan 1i
SOURCE[X]
3101&6003PWMLXBAR处理
锁存
PWMXBAR支持异步模式；
PWMXBAR送两组信号给SRPWM，一组12bit同步信号，
一组12bit异步信号，与INPUTXBAR合并为2组18bit信号
由SRPWM选择使用。异步模式下，同步信号和异步信号之间
有延时差，同步模式下为相同信号。
ETMCUhua7.13
BIMCU


### 【右页】

OR
PFXBAR_OUTIO)-
8TMCU han,Ji
UO_XBAR_PROC
OR
PFXBAR_OUT[1]-
UI_XBAR_PROC
TMCU muan.Ji 2026-10-02-21/59
PFXBAR_OUT[11]-
UII_XBAR_PROC
U_FFXB
U_XBAR_POST
图3PWMXBAR模块框图
3ETIMXBAR模块
ETIMXBAR实现结构如下图所示。
FTNCU han.71 2026-10-
12080F



---
## 图像编号 23 (原图: `GameViewer_x1UNjKA5fU.png`)

### 【左页】

ET6601修改点：
去除SDFM通道SD*FLT*EVT*和SD*FLT*_EVTO_OREVT1
2)
去除EPWM12~17FAULTREAL
2-21:5P
XBAR.SPEC【21】
ETIMXBAR支持对输入信号源进行4bit
分组并进行mux-or选通，c信号源选择如下表所示：
Reserved
CMP_EVT0
ADCA_EVTO
Reserved
CMP_EVT1
INPUTXBARO
ADCA_EVTI
Reserved
CMP_EVT2
Reserved
ADCA_EVT2
Reserved
CMP EVT3
INPUTXBARI
ADCA EVT3
Reserved
CMP_EVT4
Reserved
ADCB_EVT0
Reserved
CMP EVT5
INPUTXBAR2
ADCB EVT1
Reserved
CMP EVT6
Reserved
ADCB_EVT2
Reserved
CMP_EVT7
INPUTXBAR3
ADCB_EVT3
Reserved
CMP_EVT8
ERRORSTS
ADCC_EVTO
Reserved
CMP_EVT9
INPUTXBAR4
ADCC_EVT1
Reserved
CMP_EVT10
EXTSYNCOUT
ADCC_EVT2
Reserved
CMP EVT11
INPUTXBAR5
ADCCEVT3
Reserved
CMP_EVTO_OR_EVT1
EPWMO_FAULTREAL
CMP_EVT12
Reserved
CMP_EVT13
INPUTXBAR6
EPWM1_FAULTREAL
Reserved
EPWM2_FAULTREAL
CMP_EVT14
CFG_ETXB_SWx
Reserved
CMP_EVT15
INPUTXBAR7
EPWM3_FAULTREAL
Reserved
CMP_EVT16
Reserved
EPWM4_FAULTREAL
Reserved
CMP_EVT17
INPUTXBARS
EPWM5_FAULTREAL
Reserved
CMP_EVT18
Reserved
EPWM6_FAULTREAL
Reserved
INPUTXBAR9
EPWM7FAULTREAL
CMP_EVT19
Reserved
CMP_EVT20
Reserved
EPWM8_ FAULTREAL
Reserved


### 【右页】

EPWM9_FAULTREAL
CMP_EVT21
INPUTXBAR10
Reserved
CMP_EVT2_OR_EVT3
Reserved
EPWM10 FAULTREAL
Reserved
INPUTXBAR11
CMP_EVT4_OR_EVT5
EPWM11_FAULTREAL
Reserved
Reserved
CMP_EVT6_OR_EVT7
Reserved
Reserved
CMP_EVT8_OR_EVT9
INPUTXBAR12
Reserved
Reserved
CMP_EVT10_OR_EVT11
Reserved
Reserved
Reserved
CMP_EVT12_OR_EVT13
INPUTXBAR13
Reserved
Reserved
CMP_EVT14_OR_EVT15
Reserved
Reserved
Reserved
INPUTXBAR14
CMP_EVT16_OR_EVT17
Reserved
Reserved
CMP_EVT18_OR_EVT19
Reserved
CFG_ETXB_SWx
Reserved
INPUTXBAR15
CMP_EVT20_OR_EVT21
ERRORSTS
Reserved
XBAR.SPEC【22】ETIMXBAR支持对选通信号进行高电
平锁存操作，锁存信号可配置清零
XBAR.SPEC【23】
ETIMXBAR支持输出使能和输出极性
配置
XBAR.SPEC【24】
ETIMXBAR支持异步路径，输出端通
过WARPMUX2配置选择
XBAR.SPEC【25】
支持ETIMXBAR输出14bit，分别连接
到14个ETIMER通道
XBAR.SPEC【26】
支持软件可配置14bitCFGETXBSWx
寄存器，分别对应14个ETIMER通道XBAR选择
11080F



---
## 图像编号 24 (原图: `GameViewer_XqmNqCU6Lw.png`)

### 【左页】

同步电平信号，高有效
输出
errorsts
flash err sys err pt err
epwm2xbar_fault_real[11:0]
输入
srpwm
输入
etim2xbar_fault_real [13:0]
etim
xclk_out
crg_ xclk
BIMCU huan
注:
1、
电平信号为常高或常低信号，或为从0到1或从1到0翻转一次信
号，或为软件配置控制信号
2、脉冲信号为硬件控制0-1-0信号（高脉冲信号）或1-0-1信号（低
脉冲信号），脉冲宽度固定或软件可配置，或依赖其他输入

#### 4.3信号对应关系

BTNCI Tua, 11 902F-10-02-31:59
BIMCU
信号标识
信号名
信号来源说明
cmpe_ctriph[0]
CMP_EVTO
输入信号
CMP_EVT1
cmpc_ctripl[0]
输入信号
CMP_EVT2
cmpc_ctriph[1]
输入信号
CMP_EVT3
cmpc_ctripl[]
输入信号
CMP_EVT4
cmpc_ctriph[2]
输入信号
CMP_EVT5
cmpc_ctripl[2]
输入信号
输入信号
CMP EVT6
cmpc_ctriph[3]
CMP_EVT7
cmpc_ctrip[3]
输入信号
cmpc_ctriph[4]
CMP_EVT8
输入信号
CMP_EVT9
cmpc_ctripl[4]
输入信号
CMP_EVT10
cmpc_ctriph[5]
输入信号


### 【右页】

CMP_EVT11
cmpc_ctripl[5]
输入信号
CMP_EVT12
cmpc_ctriph[6]
输入信号
cmpc_ctripl[6]
CMP_EVT13
输入信号
CMP_EVT14
cmpc_ctriph[7]
输入信号
CMP EVT15
cmpc ctripl[7]
输入信号
cmpc_ctriph[8]
CMP_EVT16
输入信号
CMP_EVT17
cmpc_ctripl[8]
输入信号
CMP_EVT18
cmpc_ctriph[9]
输入信号
cmpc_ctripl[9]
CMP_EVT19
输入信号
CMP_EVT20
cmpc_ctriph[10]
输入信号
CMP_EVT21
cmpc_ctripl[10]
输入信号
CMP_EVT0_OR_EVT1
cmpe_ctriph_or_1[0]
cmpc_ctriph[0] | cmpc_ctripl[0]
CMP_EVT2_OR_EVT3
cmpc_ctriph_or_[1]
cmpc_ctriph[1] cmpc_ctripl[1]
CMP EVT4_OR_EVT5
cmpc_ctriph or [2]
cmpc_ctriph[2] cmpc_ctripl[2]
CMP_EVT6_OR_EVT7
cmpc_ctriph_or_l[3]
cmpc_ctriph[3] cmpc_ctripl[3]
CMP_EVT8_OR_EVT9
cmpc_ctriph_or_[4]
cmpc_ctriph[4] cmpc_ctripl[4]
cmpc_ctriph_or_I[5]
CMP_EVT10_OR_EVT11
cmpc_ctriph[5] I cmpc_ctripl[5]
cmpc_ctriph_or_[6]
CMP_EVT12_OR_EVT13
cmpc_ctriph[6] | cmpc_ctripl[6]
cmpc_ctriph_or_I[7]
CMP_EVT14_OR_EVT15
cmpc_ctriph[7] | cmpc_ctripl[7]
cmpc_ctriph_or_I[8]
cmpc_ctriph[8]]
CMP EVT16 OR EVT17
cmpc_ctripl[8]
cmpc_ctriph_or_[9]
cmpc_ctriph[9]] cmpc_ctripl[9]
CMP_EVT18_OR_EVT19
cmpc_ctriph_or_I[10]
CMP_EVT20_OR_EVT21
sarc2xbar_evt[0]
ADCA_EVTO
输入信号
sarc2xbar_evt[1]
ADCA_EVT1
输入信号
sarc2xbar_evt[2]
ADCA_EVT2
输入信号
sarc2xbar_evt[3]
ADCA_EVT3
输入信号
sarc2xbar_ev[4]
ADCB_EVTO
输入信号
sarc2xbar_evt[5]
ADCB_EVT1
输入信号
ADCB_EVT2
sarc2xbar_evt[6]
输入信号
ADCB_EVT3
sarc2xbar_evt[7]
输入信号
etim_pwm_out[0]
ETIMOUTO
输入信号
ETIMOUT1
etim_pwm_out[1]
输入信号
ETIMOUT2
etim pwm_out[2]
输入信号
etim_pwm_out[3]
ETIMOUT3
输入信号
ETIMOUT4
输入信号
etim pwm out[4]
输入信号
etim_pwm_out[5]
ETIMOUT5
输入信号
etim pwm out[6]
ETIMOUT6
fps
12080F



---
## 图像编号 25 (原图: `GameViewer_yl5bEptpgs.png`)

### 【左页】

XBAR.SPEC【34】支持输出模式选择配置，选择到
ETIMOUTx信号时，输出对应的OEN信号，也可配置固
定输出模式，和固定输出三态模式
ETMO

#### 3.6 CLU

6-10-02-21:5F
XBAR.SPEC【35】XBAR 包含 XCSA、XCET 和 XCOX 模
块，实现对INXB信号的逻辑组合，其输入为 INXB 模块
16bit输出，输出分别为4bit信号逻辑组合信号，通过各自
内置 4个 4输入 1输出的 CLU模块实现。XCSA、XCET
和XCOX模块输出分别送往SARC、ETIM和OPXB模块
作为后者输入
XBAR.SPEC【36】单个CLU模块支持8种逻辑功能可选
择，包括：1AND-OR、OR-XOR、4输入AND、S-R 锁存
器、带置1和复位功能的D触发器、带复位功能的D触发
器、带复位功能的J-K触发器、带置1和复位功能的透明
锁存器，其中，锁存器通过寄存器时序逻辑模拟


### 【右页】

XBAR.SPEC【37】
CLU模块支持输出旁路可配置，旁路模
式下，CLU固定选择输入4bit中的最低位输出
XBAR.SPEC【38】CLU模块支持输出使能可配置
XBAR.SPEC【39】CLU模块支持输出极性可配置，可结合
CLU输出使能实现输出电平软件可配置
XBAR.SPEC【4O】CLU模块支持中断上报，中断触发事件
可配置为：CLU输出上升沿中断事件和CLU输出下降沿中
断事件，可分别通过控制位使能
XBAR.SPEC【41】
支持将 XBAR 中断脉冲作为DMA触发
源，共5bit;
huan, Ji 2026-10-0
XBAR.SPEC【42】
支持XBARTESTPIN输出

#### 3.7XBAR约束

XBAR.LIMIT.SPEC【O1】：INPUTXBAR的输出会作为中断触发源，
该中断触发源在被选用为dma触发源时最好为脉冲信号，a否则会在
DMAMUX处产生相应的错误告警
1080F



---
## 图像编号 26 (原图: `GameViewer_yUpAyoEWMN.png`)

### 【左页】

202h-10-02-21:58
ETMCU muan 11
MTMCU muan.li
CHENGDUET
MICROELECTRONICS COJATO,
BTMCUhuan.S
ET6601 XBAR
模块
BTMCU hian.11
BTMGI
需求规格与设计方案
ETICV
ETHChian 1i2026
ETMCU tauan.1i


### 【右页】

设计：
牛婷婷
ETHCV hvan.15
评审;
批准:
202F-10-07-21.58
ETMC1 an,71 3026-10-02-2:58
BTNCU hST J3 2026-10-02-27-58
8G:18-00-01-9008
ETNCI h3n, 11
ETMCV
13080F



---
## 图像编号 27 (原图: `GameViewer_Z7r3yKz86a.png`)

### 【左页】

1)
新增CMPC通道CMP EVT7>21；去除CMP_EVT*_OR_EVT*（TI
无)
2)
新增SDFM通道SD2/3FLT*EVT*；去除SD*FLT*_EVTO_OR_EVT1
(TI 无)
3)
新增CLB4/5 OUT*
4)
新增EPWM TRIPOUT/DE TRIP/DE ACTIVE
新增 CPU*_ADCCHECK EVT
6)
新增ETIM TRIPOUT
gTMcuhuan.
7)
对比 TI，无MACN FEVT
8)
对比 TI，无FSI
9)
对比TI，无ECATSYNC
10)
ECAP 1-7(TI) >ETIM0-11
TMCU mian.1i
EIMCU hian.li
11)
INPUTXBAR1-14(TI) > INXB0-15
12)
CLB INPUTXBAR7-14>CBXB0-15
13）新增CPU1HALT
14）TI无SYS ERR/PT ERR/FLASHERR
15）PIEVECTERR（中断扩展模块错误）/UNCERR(内存访问错误）


### 【右页】

ET6601修改点：
去除SDFM通道SD*FLT*EVT*
2)
去除 CLB* OUT*和 CLB INPUTXBAR*
3)
去除ADCC EVT*
4)
去除EPWM12~17FAULTREAL
Delete / 6 (0#~5#)
6)
新增ETIMOUT12/13和ETIM12/13FAULTREAL
huan. Ji 2026-10-02-21-58
XBAR.SPEC【16】
PWMXBAR支持对输入信号源进行4bit
分组并进行mux-or选通，信号源选择如下表所示：
CMP_EVTO
ADCA_EVTO
Reserved
ETIMOUTO
CMP_ EVT1
INPUTXBARO
Reserved
Reserved
CMP_EVT2
ADCA_EVT1
ETIMOUT1
CMP EVT3
INPUTXBARi
Reserved
CMP EVT4
ADCA EVT2
Reserved
ETIMOUT2
CMP_EVT5
INPUTXBAR2
Reserved
CMP_EVT6
Reserved
ADCA_EVT3
ETIMOUT3
CMP_EVT7
INPUTXBAR3
Reserved
CMP_EVTS
Reserved
ADCB_EVTO
ETIMOUT4
CMP_EVT9
INPUTXBAR4
Reserved
Reserved
CMP_EVT10
Reserved
ADCB_EVT1
ETIMOUT5
Reserved
INPUTXBAR5
CMP_EVT11
Reserved
CMP_EVT12
Reserved
ADCB_EVT2
ETIMOUT6
Reserved
ADCSOCAO
SYS_ERR
CMP _EVT13
Reserved
ADCB_EVT3
CMP_EVT14
EXTSYNCOUT
CMP_EVT15
ADCSOCBO
Reserved
PT_ERR
Reserved
Reserved
Reserved
ERRORSTS
11080F

