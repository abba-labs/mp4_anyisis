# SARC LRS 需求规格文档

> 本文档由大模型逐图逐页提取自原始截图，不作主观修饰，忠实还原原文。
> 图表、时序波形及模糊部分均标注对应截图原图文件名供查阅。


---
## 图像编号 1 (原图: `GameViewer_1h9LEjdFpy.png`)

### 【左页】

ETMCUhua.11
BTHCU huan, Ji
BTMCU han 13
TMCUhian.13
ETMCU han.14
ET6601SARC模块LRS设计文档
s 203
n.11
设计：
郑cu汶
,1i
评审：XXXXXXX


### 【右页】

批准：
2026-10-02-21;28
FTMCU Tnian.
ETMC hua.J1
, li 2026-10-02-81:
Q026-10-02-21:28
17080F



---
## 图像编号 2 (原图: `GameViewer_aAOwVv2FCQ.png`)

### 【左页】


**表1-1修订记录**

版本号
修订内容
修订日期
修订人员
HTNCU Thuam.11
牟崎瑞
BTMCU huan, i
1、在预处理通道之后新增8个预处理滤波器通道；
肖中平
2、修改FUNC.SPEC【18】偏置校准处理的位宽，从s(5.0)
变为s(15,2);
合入6801的优化点。
郑汶
1.Fix增益补偿的-2048问题。
2.上报结果合并处理，2通道采样数据合并到一个寄存器中
3．采样结果输出到cpu时钟域下。
ETMCU han.11
4.EOC中断触发位置增加。
5. Oneshot模式的再使能优化，
增加需求：支持对模拟的放电时序控制；
郑汶
6601在6801的基础上调整，文档中使用浅蓝色体现修改；
郑汶
1.增加抢占功能；
v1.0
2.增加用户预处理滤波过采求和功能；
BTMCIT huan. Ji
3.增加用户预处理的观测功能；
BTMCU hua.13
1.增加触发到开始采样，抢占触发到开始采样的延迟指
郑汶
标需求


### 【右页】

注：浅蓝色和清绿色相关区域为ET6601新加的改动，包括线，背景及底
纹部分；
ETMC h/an.J1 2026-10-02-2112
目录
ETMC/ huan. T1
Contents
且录
图目录
, li 2026-10-02-81:
未找到图形项目表。
表且录

### 第1章

模块介绍
模块简介
应用说明
dan
需求规格
第2 章
Q026-14
11080F



---
## 图像编号 3 (原图: `GameViewer_abFYmuKlpf.png`)

### 【左页】

功能需求
中断管理
事件管理
BTHCU huan, Ji
约束说明
触发源说明
8TMCu Thran.13 2026-10-02-
ETMCV mian. 11
BTMCIT
ETNCV
ETMCV
, 1i


### 【右页】

图目录
ETNCU Thjan.11
未找到图形项目表。
EJMCU huanJi
ETNCI/
表目录

**表 1-1**

修订记录
, li 2026-10-02-81:
EIMCU
Q026-10-02-21:28
17080F



---
## 图像编号 4 (原图: `GameViewer_CeKX8gRMOe.png`)

### 【左页】

evtsel.hi
limit.hi
YEVT
limit.lo
dcevtsts.triplo
evtsel.lo
HTMCU
BTMCU huan,li
clear.h
clear.lo
CBC clearlogic
sample1
sample2
sample3
超门限
超门限
不趟门限
BTMC0 moar,11 2026-10-02-21-26
ETMOU uan.13
ONESHOT
超门限事件优先级高于softclear事件；
LRS.SARC.FUNC.SPEC【23】
每个ADC控制器支持16个虚拟通
道的超门限检测事件进行mux选择后输出4bit告警信号，每bit告
警信号支持独立从16个虚拟通道的超门限检测事件中配置选择；
并且每个ADC控制器独立输出2组4bit告警信号，一组到XBAR，
另一组到ETIM;
LRS.SARC.FUNC.SPEC【24】
每个ADC控制器支持8个滤波通
道，基于虚拟通道配置选择对应的滤波通道，滤波器输入为ADC
校准后采样结果，每个通道支持滤波类型：FIR（阶数可任意配置，


### 【右页】

且根据配置阶数实时输出滤波结果，最大32阶）、IIR（1阶）
滑动平均（归入FIR）和非滑动平均，通过配置选择：
LRS.SARC.FUNC.SPEC【25】每个ADC控制器支持2组采样结果
上报寄存器，每组包括16个16bit寄存器，每个16bit寄存器对应
一个虚拟通道的采样结果，支持CPU和DMA读取采样结果（32
个结果上报寄存器地址连续），支持8*20bit求和结果寄存器，地址
连续于上述2组结果；
●第一组：存储上报用户偏置和增益计算处理、预处理滤波的结果，
支持s(16,2)和s(15,0)两种结果上报格式可配置选择；
第二组：存储上报滤波计算处理后的采样结果，支持s(16,2)和
u(12,0)两种结果上报格式可配置选择；滤波处理后上报结果：
s(16,2)、u(12,0);
求和结果：对第一组结果进行求和结果，根据第一组输出格式匹
配为 s(20,2)和 s(19,0)
LRS.SARC.FUNC.SPEC【26】1用户预处理通道结果、滤波通道结
果两组结果mux选择后同步到CPU时钟域下，快速响应CPU读
动作。
a)两个虚拟通道的结果放入一个寄存器中。
1080F



---
## 图像编号 5 (原图: `GameViewer_Dt52xixULd.png`)

### 【左页】

IPTEST
iptest_adc_start
[75:54]
CMPC
(cmpe_ctripl[10],cmpe_ctriph[10],
cmpe_ctripl[9],cmpe_ctriph[9],
cmpe_ctripl[8],cmpe_ctriph[8],
HTMCU
BTMCU huan, li
cmpe_ctip[7],cmpe_ctriph[7],
cmpe_ctripl[],cmpe_ctriph[6],
cmpe_ctrip[5],cmpe_ctriph[5],
cmp_ctripl[4],cmpe_ctriph[4]
cmpc_ctip[2],cmpc_ctriph[2],
cmp_ctripl[1],cmpe_ctriph[1],
ETICU moar.13 2026-10-02-n1:28
BTNG
STM
[99:76]
{ tm5_oc_exp[3:0],
stm4_oc_exp[3:0],
stm2_oc_exp[3:0]
stm1_oc_exp[3:0],
BTMCU huan. 2026-10-02-21:2
stm0_oc_exp[3:0]
BIMCU hian.
[103:100]
CLU
xbar2sarc_cludata[3:0]
ADCEOC
[107:104]
( sarel_ eoc2spl_trig [1:0],
sarc0_eoc2spl_trig[1:0]]
RESERVED
[109:107]
OP.
[110]
GPIO (inputxbar)
inputxbar_data[4]
RESERVED
[126:111]
OP.
SOFT_START
[127]
sarc_sof_start
ETMCU has.1i
LRS.SARC.TRIG.SPEC【02】Blanking功能支持如下触发源进行触


### 【右页】

发启动：
blanking角发源
位域
SARCO/1/2
SPWM
[23:0]
(epwm_sadc_trig[23:0])
BTMO
ETIM
[49:36]
etim2adc_evt[13:0]
RESERVED
[52:50]
OP.
BTMCV Tu18,11 3026-18-02-27:28
BTMOU Tian, 11
BTMCU h18. 7)
ETMC/ huar.11
216 Ⅱ
254 Ⅱ
17080F



---
## 图像编号 6 (原图: `GameViewer_eyXbfnO5PJ.png`)

### 【左页】

f)过采样被高优先级通道打断后，支持resume、conti模式；
g)过采功能支持使能控制；
LRS.SARC.FUNC.SPEC【48】*
不抢占模式下，从触发输出到发出
模拟的采样控制延迟在4个ADCCLK时钟以内，抢占模式下从高
优先级触发到发出模拟的采样控制延迟在6个ADCCLK以内；
BTMCUhuaYi
ETMCU han.12

#### 2.2中断管理

LRS.SARC.INTR.SPEC【O1】每个ADC控制器的虚拟通道支持对应
EOC（end-of-conversion）信号产生，用于触发中断，EOC脉冲信
号可配置选择如下三个产生位置，每个ADC控制器的虚拟通道统
一配置：
S/H窗口结束时刻，
采样转换结束时刻，默认选择
S/H窗口开始时刻
LRS.SARC.INTR.SPEC【02】支持EOC选择位置时刻到中断产生的
上沿延时可配置，16bitSYSCLK时钟计数值；且每个ADC控制器


### 【右页】

的虚拟通道统一配置。如果当前EOC到来时，上一个EOC的延时
处理没有完成，则在该时刻输出上一个EOC的中断触发，同时当
前EOC进行延时模块进行延时处理；
end_p到来时，上一个end_p的delay还没
有充成，则在该时刻输出上一个end_p的
int_trig，然后当前enc_p进行delay模共重
va
end_p
新开始计数延时。
int_trig
-delay_
LRS.SARC.INTR.SPEC【03】每个ADC支持上报延时冲突告警，即
当前EOC到来时，上一个EOC的延时处理未完成状态，告警状态
软件读清；并且同时上报延时未处理完成的虚拟通道编号；
LRS.SARC.INTR.SPEC【04】每个ADC支持5路中断输出；
1.其中1路中断包括：
·电平超门限中断（基于虚拟通道，超门限脉冲触发中断，超上下
门限独立中断源，共16bit*2）
2.另外4路中断中，每1路中断可独立选择以下中断作为中断源；
EOC脉冲信号（基于虚拟通道，16bit）
2组结果寄存器锁存有效采样结果中断（基于虚拟通道，16bit*2）
过采求和结果有效中断(基于过采求和通道，8bit)
LRS.SARC.INTR.SPEC【05】每个ADC支持中断溢出告警指示；



---
## 图像编号 7 (原图: `GameViewer_hTRpPSKxgI.png`)

### 【左页】

LRS.SARC.FUNC.SPEC【27】
每个ADC控制器支持如下采样结果
处理数据流：
BTNCU huan
BTMCU huan,li
ADC校准参数处理
用户配置参数处理
滤波处理
LRS.SARC.FUNC.SPEC【28】
每个ADC控制器支持基于虚拟通道
进行采样结果更新标志位上报；
LRS.SARC.FUNC.SPEC【29】
每个ADC控制器支持基于虚拟通道
进行采样结果被覆盖标志位上报.
LRS.SARC.FUNC.SPEC【30】MC每个ADC支持4+1个DMA请求通
道，
a)4个DMA请求通道可从如下DMA请求源中独立配置选择：
EOC脉冲信号（基于虚拟通道，16bit）
2组结果寄存器锁存有效采样结果（基于虚拟通道，16bit*2）
电平超门限检测结果事件（基于虚拟通道*16bit）
过采样求和完成事件；（基于过采样求和通道8bit）


### 【右页】

b)1个16个虚拟通道电平超门限检测结果事件或输出；
LRS.SARC.FUNC.SPEC【31】支持在通过fifo读取采样结果模式
下，通过fifo的非空信号进行DMA请求，两个fifo的非空信号可
独立选择到4个dma请求通道，默认配置下不选择fifo的DMA请
求;
LRS.SARC.FUNC.SPEC【32】
每个ADC支持工作状态可独立查询：
·IDLE：对应ADC空闲
BUSY：对应ADC正在采样
通道指示（IDLE时指示上一个采样的虚拟通道号，BUSY时指
示当前正在采样的虚拟通道号）
LRS.SARC.FUNC.SPEC【33】
每个ADC控制器支持16个虚拟通
道工作状态可独立查询：
EIMC
●IDLE：对应虚拟通道空闲
PENDING：对应虚拟通道被有效触发，但处于排队状态
BUSY：对应虚拟通道正在被执行采样
2026-10-02-21;28
LRS.SARC.FUNC.SPEC【34】同一个虚拟通道，若采样事件来不
及处理（即该虚拟通道被触发正在排队时又收到新的触发信号），
上报采样触发冲突告警，每个虚拟通道独立上报告警，该告警需要
7080F



---
## 图像编号 8 (原图: `GameViewer_Kd7bk57Vx3.png`)

### 【左页】

LRS.SARC.FUNC.SPEC【15】
每个ADC控制器支持软件直接控制
一个或多个虚拟通道开始采样（不通过采样触发信号）。
LRS.SARC.FUNC.SPEC【16]】M
支持软件输出采样触发，同其它硬
件采样触发通路一致；
LRS.SARC.FUNC.SPEC【17]
每个ADC控制器中，虚拟通道0支
持一个Blanking事件功能，该功能可屏蔽。支持blanking的延迟
触发时间可配置，且对所有触发源统一配置，为16bitSYSCLK周
BTACU
期计数；
LRS.SARC.FUNC.SPEC【18】每个ADC控制器Blanking管理模
块，对所有blanking触发源的blanking窗口长度配置相同，为
16bitSYSCLK周期计数器。
LRS.SARC.FUNC.SPEC【19】Mcblanking窗口内虚拟通道0的触发
（专用周期触发源）可以正常响应，窗口内若出现其他虚拟通道触
发信号（非专用周期触发），待blanking窗口结束后，按优先级处
理。若Blanking窗口内，非专用周期触发出现重复触发，上报告
警，并忽略该重复触发；
ETMCI
ETMCI han.


### 【右页】

Blanking延运触发
Blanking窗口
trig
其他vc解发源
+binking置口内O口△出现重复群发，产生专旨，
LRS.SARC.FUNC.SPEC【20】
每个ADC控制器支持对采样结果进
行数字域偏置和增益校准处理（模拟ADCs(15,2)和增益u(14,12));
LRS.SARC.FUNC.SPEC【21】
每个ADC控制器支持基于虚拟通道
对校准后的采样结果进行用户偏置和增益处理（用户配置偏置
s(16,2)和增益 s(15,12));
LRS.SARC.FUNC.SPEC【22】每个ADC控制器支持基于虚拟通道
对用户偏置和增益处理后的采样结果进行上下电平超门限独立检
测，可配置选择CBC和ONESHOT两种方式产生相应的超门限事
件，可上报中断（上下门限独立作为中断源）、DMA请求（mux-or
后的事件信号）和输出事件；超上下门限的告警实时状态通过状态
寄存器上报，告警历史状态上报通过中断模块中的status寄存器上
报；
EINCUA
1080F



---
## 图像编号 9 (原图: `GameViewer_nGNAOmfeWa.png`)

### 【左页】

道VC、116个预处理通道PC、8个预处理滤波通道PFC+8个求和
通道SCh、8个滤波通道FC、2*16个采样结果缓存通道BC、1*8
HTMCL
个求和结果寄存器，其中，预处理通道、缓存通道分别与虚拟通道
一对应，滤波通道和虚拟通道映射由软件配置；
LRS.SARC.FUNC.SPEC【08】每个ADC控制器支持基于虚拟通道
配置扩展采样时间（范围0-256个ADCCLK周期数）；
LRS.SARC.FUNC.SPEC【09】每个ADC控制器支持基于虚拟通道
定义：虚拟通道使能、采样优先级、S/H窗口、采样通道、触发源、
触发方式，用户预处理通道等采样参数；
LRS.SARC.FUNC.SPEC【10】每个ADC控制器支持4个优先级配
置0~3（基于虚拟通道），配置数值越小，优先级越高；在同等优
先级情况下，虚拟通道编号值越小，优先级越高；
LRS.SARC.FUNC.SPEC【11】支持pO高优先级虚拟通道抢占低
优先级虚拟通道抢占；
a)低优先级虚拟通道在高优先级通道结束后，继续低优先级请求；
b)增加使能控制；
c)仅po可抢占其它低优先级；
d)po内部不进行抢占；


### 【右页】

LRS.SARC.FUNC.SPEC【12】-10~支持发生采样事件冲突时（多个虚
拟通道同时被触发采样），可配置支持两种优先级处理：
●低优先级采样事件被丢弃，只响应最高优先级采样事件；
所有被同时触发的采样事件按优先级进行排队处理，默认该模式；
LRS.SARC.FUNC.SPEC【13】
支持基于虚拟通道配置单次触发采
样和连续触发采样模式：
●单次触发采样：虚拟通道采样配置一次只响应一次触发采样
（VCEN打开一次只响应一次触发）
·连续触发采样：虚拟通道采样配置一次可响应多次触发采样
（VCEN打开时可连续响应触发），默认该模式
模拟ADCCORE也存在单次模式/连续模式概念，但以上描述为数
字测的单次触发采样、连续触发采样功能。模拟ADCCORE的固
定为单次模式，即数字侧每发一个start，触发一次采样。
LRS.SARC.FUNC.SPEC【14】每个ADC控制器支持基于虚拟通道
进行Trigger-to-sample延迟计算，并上报延迟时间（SYSCLK周期
计数），当sample被高优先级通道抢占后，原通道的Trigger-to-
sample会在重新开始sample时更新延迟时间，过采样启用时在过
采第一次开始sample上报，后续过采过程中不再上报；
1080F



---
## 图像编号 10 (原图: `GameViewer_PJZbqwPIEg.png`)

### 【左页】

1）从16个预处理通道映射到8个预处理滤波器通道（映射关系
寄存器可配，最多只能从16个预处理通道中选择8个映射到预
处理滤波器通道，其他的bypass）；
ETMCUJn
2）预处理滤波支持ir滤波器（直接1型）1~4阶软件可配置，
支持fir滤波器1~8阶软件可配置；
3）预处理滤通道输入数据可进行放大和缩小（算数左移或者算数
右移，带符号移位），移位的范围为：-1～2（负数表示左移，正
BTICU
数表示右移；原始预处理通道输入数据为s(16,2)，此处为了对
标TI：ET6801-DOC\05.数字设计\03HACISARCIV100\01.需求分
析101.竞品资料\dm00605584-digital-filter-implementation-with-
the-fmac-using-stm32cubeg4-mcu-package-
stmicroelectronics(1)(2).pdf);
ETMCUhoan.
In the ADC, thefactor KADc =8 is applied using the left justification feature.The ADC result (after subtracting the
offset) is a 12-bit signed integer. In right-aligned format, the result is sign-extended to 16-bits:
Table 3. Right aligned ADC data
sign
sign
sign
b10
In left aligned mode the result is shifted left by 3, retaining only one sign bit:
ETMCUhnas,1i
Table 4.Left aligned ADC data
sign
b11
b10


### 【右页】

乘法器位宽：16*16bit，加法器位宽：支持3627bit
4)
（此处对
标 FMAC）；
5）预处理滤波通道的输入输出最大数据速率跟ADC最高采样率
保持一致；
LRS.SARC.FUNC.SPEC【45】
支持对模拟的放电时序控制；
LRS.SARC.FUNC.SPEC 【46]
支持用户预处理过程的中间值观测：
a)1*原始采样值u(12,0);
ETNCL
b)1*模拟校正值 s(16,2)、u(12,0);
c)16vc*PFC滤波输出结果s(16,2)、s(15,0);
d)8个vc*过采样求和结果输出 s(20,2)、s(19,0);
LRS.SARC.FUNC.SPEC【47】
支持基于用户预处理滤波通道的过
采样触发、过采求和功能；
a)过采求和次数 N<=16;
b)采样间隔count为22bit配置，单位为sarc工作时钟；
c)间隔期间允许其它低优先级进行采样；
d)count及N支持影子加载，触发时完成影子值到生效值更新；
e)过采期间忽略新触发，但会告警；
1080F



---
## 图像编号 11 (原图: `GameViewer_TxOL7pU1gm.png`)

### 【左页】

软件清除；
LRS.SARC.FUNC.SPEC【35】
支持校准后数据输出供ATE测试使
用，输出数据格式为u(12,0)，范围为0~4095；
ETMO
LRS.SARC.FUNC.SPEC【36】
每个ADC控制器接收模拟ADC返
回采样结果支持如下两种方式：
模拟ADC_CORE输出async ready信号：控制器使用异步方式
处理该ready信号（默认选择）；
模拟AFE_TOP打拍输出syncready信号：控制器使用同步方式
处理该ready信号；
LRS.SARC.FUNC.SPEC【37】用cfg_sarc_en的上升沿清零采样结
果寄存器，清除ADC校准算法处理时产生的采样结果；
LRS.SARC.FUNC.SPEC【38】MCSARADC支持对采样结果按照fifo
模式进行DMA搬移，每个ADC控制器新增两套寄存器用于fifo
模式，分别对应用户偏置/增益处理和滤波处理的采样结果数据通
LRS.SARC.FUNC.SPEC【39】fifo模式下支持bitmap映射具体通
道，控制虚拟通道结果是否映射到fifo中，bitmap由软件配置（默
认为vcen），硬件维护，初始加载或者参数修改需要通过软件配


### 【右页】

置reload加载，vc的采样顺序必须按照bitmap配置中vc编号从小
到大的顺序；或者应用约束所有映射到fifo的vc必须采用同一个
触发源，且均处于同一个优先级；
LRS.SARC.FUNC.SPEC【40】
支持软件对fifo深度的配置，fifo深
度默认为16；
LRS.SARC.FUNC.SPEC【41】
通过fifo寄存器地址读取采样结果
时，需要清除对应结果寄存器中的val和ovf标志；
LRS.SARC.FUNC.SPEC【42】
支持通过fifo寄存器地址读取采样
结果时，上报每次读取结果对应的vc编号；
LRS.SARC.FUNC.SPEC 【43】
10~支持fifo状态上报，包含空，满，空
溢出，满溢出，fifo中数据个数。
LRS.SARC.FUNC.SPEC【44】
在预处理通道之后支持8个预处理
滤波器通道、8个求和通道SCh。
SERADC



---
## 图像编号 12 (原图: `GameViewer_WtOrHaAqvH.png`)

### 【左页】


### 第1章

模块介绍
BTMCUJuian.1i
BTMCU huan, li

#### 1.1模块简介

SARADC主要用于采集片外电压、电流、温度、压力等信息，采样
片内温度、电压、电流信息（可选），以及采样片内运放输出。
本文主要介绍内置SARADC数字控制器的设计规格。
ETMCU hian11
CA
ChnN
risser
SARADC
ETMCIT
8Oan 15

#### 1.2应用说明


### 第2章

需求规格
ETMChgan.1i

#### 2.1功能需求



### 【右页】

LRS.SARC.FUNC.SPEC【01】10~支持3个12位ADC内核，单个
ADC最高采样率4.1Msps，每个ADC支持独立Power-gatingClock-
gating以便节省功耗；
LRS.SARC.FUNC.SPEC【02】
每个ADC支持32个采样复用通道，
支持单端输入（数字侧按32采样通道预留控制接口，模拟测按实
际通道实现）；
LRS.SARC.FUNC.SPEC【03】
ADC工作时钟支持通过系统时钟进
行1-8分频，最高时钟频率；
LRS.SARC.FUNC.SPEC【04】
支持2个独立的ADC数字控制器，
SARCO~1，分别配置和管理2个ADC内核，支持通过AHB总线
进行配置管理，支持软复位/模块使能/clock-gating;
LRS.SARC.FUNC.SPEC【05】每个ADC支持校准算法实现（模拟
提供校准方案，数字实现)；校准阶段上报校准寄存器结果：s(16,2)
LRS.SARC.FUNC.SPEC【06】2个ADC可以工作在同步模式下
（基于相同触发源选择）进行同步采样（同时采样不同信号）或者
亢余采样（同时采样相同信号），2个ADC也可以工作在非同步模
式下（基于不同触发源选择）；
LRS.SARC.FUNC.SPEC【07】
每个ADC控制器支持16个虚拟通
dan



---
## 图像编号 13 (原图: `GameViewer_XDCKpTnaH0.png`)

### 【左页】


#### 2.3事件管理

LRS.SARC.EVT.SPEC【O1】每个"ADC控制器支持如下事件输出：
ADC输出到XBAR电平超门限检测输出事件*4（从16个VC事
件中独立配置选择）
件中独立配置选择)
BTMCUhoaY
ETMCU hian.11

#### 2.4约束说明

LRS.SARC.LIMIT.SPEC【01】
ADC数字控制器不能早于模拟
ADC解复位;
LRS.SARC.LIMIT.SPEC【02】
ADC数字控制器不能早于模拟
ADC使能有效；
LRS.SARC.LIMIT.SPEC【03】
系统时钟频率不能低于ADC工作时
钟频率;
LRS.SARC.LIMIT.SPEC 【04]
外部输入的采样触发源脉冲需要为
正脉冲，且脉冲宽度要大于1个系统时钟周期（因为是同步处理）；


### 【右页】

LRS.SARC.LIMIT.SPEC【05】10~使用超过16阶FIR滤波时，系统时
钟频率必须大于ADC工作时钟频率的2倍以上；（2个连续需要
FIR滤波处理的采样，需要最小间隔FIR滤波阶数个系统时钟周
期)
LRS.SARC.LIMIT.SPEC【06】，ADC校准时，要求软件关闭模拟
ADC使能，待校准流程完成后再打开模拟ADC使能；
LRS.SARC.LIMIT.SPEC【07】对虚拟通道vc的配置，需要将对应
的vcen关闭后进行配置，配置完成后再将vcen打开；
LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早
于控制器内的其他使能信号（比如vc_en等）打开；
STMCU Thian, 1i

#### 2.5触发源说明

ETNCU THU87. 11 2026-10-02-
LRS.SARC.TRIG.SPEC【01】每个ADC控制器中16个虚拟通道支
持如下采样触发源信号可独立配置选择：
sample 触发源
位域
SARCO/1
ETMCI/
SPWM
[23:0]
(epwm_sadc_trig[23:0])
ETIM
[49:36]
etim2adc_evt[13:0]
RESERVED
[52:50]

