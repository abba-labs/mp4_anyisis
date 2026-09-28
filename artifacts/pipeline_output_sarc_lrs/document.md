# ET6601_SARC_LRS_Document

ET6601SARC模块LRS设计文档
设计：
郑汶
评审：
XXXXXXX
批准：_
设计:
批准：
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第1/16页

ETMCU-ET6601

### 第2/16

V1.0
ETMCU
SARC
页
保密等级：口绝密
私密
■内部公开
口外部公开
表1-1修订记录
版本号。
修订内容
修订日期
修订人员。
20230919。
牟崎瑞。
1、在预处理通道之后新增8个预处理滤波器通道；
20240819
肖中平
2、修改FUNC.SPEC【18】偏置校准处理的位宽，从s(5.0)
修订内容。
修订日期。
肖中平。
变为s(15,2)；
合入6801的优化点。
20250909
郑汶
1．Fix增益补偿的-2048问题。

### 2.上报结果合并处理，2通道采样数据合并到一个寄存器中

1

### 3.

采样结果输出到cpu时钟域下。

### 4.EOC中断触发位置增加。


### 5.Oneshot模式的再使能优化；

增加需求：支持对模拟的放电时序控制；←
2026/09/22 
v1.0

### 2.增加用户预处理滤波过采求和功能；

36增加用户预处理的观测功能；

### 2.

增加用户预处理滤波过采求和功能：
t
lt
七
工
翌创微电子保密信息未经授权禁止扩散

### 第2/16页


### 第3/16

V1.0
ETMCU
SARC
贡
保密等级：口绝密
私密
■内部公开
外部公开
目录
图目录
4
未找到图形项目表。
表目录

### 第1章

模块介绍

### 1.1

模块简介

### 1.2

应用说明

### 第2章

需求规格
5

### 2.1

功能需求

### 2.2

2中断管理
13

### 2.3

事件管理
14

### 2.4

约束说明
.14
.15
未找到图形项白表
功能需求.
中断管理
15

### 2.3事件管理

一
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第3/16页

ETMCU-ET6601

### 第4/16

V1.0
ETMCU
SARC
页
保密等级：口绝密
私密
■内部公开
口外部公开
图目录
口私密
未找到图形项目表。，
图目录。
表目录。
表1-1
修订记录

### 第4/16页


### 第5/16


### 第1章 模块介绍.


### 第1章模块介绍


### 1.1模块简介。

SARADC主要用于采集片外电压、电流、温度、压力等信息，采样片内温度、电
压、电流信息（可选），以及采样片内运放输出。
本文主要介绍内置SARADC数字控制器的设计规格。
Chano
SARADC
CALC
存通
PChano
PFChan0
sCho
BChan 0
Sumo
Chan1
ChanD
预处理
道
预处理滤波通道
缓存通道1
SCho
ready
校准通道
PChan1
SCh1
BChan1
Sum1
SH
SARCORE
data
CAL
......
SCh7
Sum7
ChanN
trigger
one
薄波通道
缓存通道2
CPU/DMA
BChano
采样通
FChan 1
道选择
SARADC
CTRL
校准、
原处理、滤波、缓存控制
FChan7
模拟电路
触发信号管理

### 1.1cu模块简介。

压、电流信息（可选），以及采样片内运放输出
Chano
CALC
预处理滤波通道
缓存通道1
PChano
sCho
BChanO
Sumo
Chan1
ready
校准通道
PChan1
sCh1
5um1
SH
SARCORE
CAL
......
sCh7
BChan15
Sum7
ISY
ChanN
trigger
滤波通道
缓存通道2
FChan0
CPU/DMA
BCha
采样通
FChan1
道选择
SARADC
BChan'1
CTRL
校准、
预处理、滤波、缓存控制
FChan7
模拟电路
触发信号管理
数字电路

### 1.2应用说明

ChanO
CALC
预处理滤波通道
缓存通道1
PChanO
SCho
BChano
Sumo
Chan1
ready
校准通道
data
PChan1
sCh1
Sum1
SH
SARCORE
CAL
......
SCh7
BChan15
Sum7
usy
ChanN
trigger
done
滤波通道
缓存通道2
CPU/DMA
FChano
BChanO
采样通
FChan1
道选择
SARADC
CTRL
校准
处理、滤波、缓存控制
.....
FChan7
模拟电路
触发信号管理
数字电路

### 1.2应用说明.

*第2章需求规格

### 2.1功能需求.

LRS.SARC.FUNC.SPEC【01】支持3个12位ADC内核，单个ADC最高采样率
采通
BChan 1

### 4.1Msps，每个ADC支持独立Power-gatingClock-gating以便节省功耗；6

LRS.SARC.FUNC.SPEC【02】每个ADC支持32个采样复用通道，支持单端输入
LRS.SARC.FUNC.SPEC【03】ADC工作时钟支持通过系统时钟进行1-8分频，最
高时钟频率

### 第2章需求规格。

2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第5/16页

ETMCU-ET6601

### 第6/16

V1.0
ETMCU
SARC
页
保密等级：口绝密
口私密
■内部公开
口外部公开
（数字侧按32采样通道预留控制接口，模拟测按实际通道实现）；
私密
外部公开
别配置和管理2个ADC内核，支持通过AHB总线进行配置管理，支持软复位
/模块使能/clock-gating；
数字实现)；校准阶段上报校准寄存器结果：s(16.2)。
选择）进行同步采样（同时采样不同信号）或者余采样（同时采样相同信号），
北
2个ADC也可以工作在非同步模式下（基于不同触发源选择）；
处理通道PC、8个预处理滤波通道PFC+8个求和通道SCh、8个滤波通道FC、
2*16个采样结果缓存通道BC、1*8个求和结果寄存器，其中，预处理通道、缓
存通道分别与虚拟通道一一对应，滤波通道和虚拟通道映射由软件配置：
时间（范围0-256个ADCCLK周期数）；
使能、采样优先级、S/H窗口、采样通道、触发源、触发方式，用户预处理通
道等采样参数；
拟通道），配置数值越小，优先级越高；在同等优先级情况下，虚拟通道编号
发采样），可配置支持两种优先级处理：
·低优先级采样事件被丢弃，只响应最高优先级采样事件；
·所有被同时触发的采样事件按优先级进行排队处理，默认该模式；
样模式
样模式：
单次触发采样：虚拟通道采样配置一次只响应一次触发采样（VC_EN打开
一次只响应一次触发）
连续发采样：虚拟通道采
VCEN打开
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第6/16页


### 第7/16

V1.0
ETMCU
SARC
页
保密等级：口绝密
■内部公开
口外部公开
时可连续响应触发），默认该模式
模拟ADCCORE也存在单次模式/连续模式概念，但以上描述为数字测的单次
触发采样、连续触发采样功能。模拟ADCCORE的固定为单次模式，即数字侧
私密
每发一个start，触发一次采样。
sample延迟计算，并上报延迟时间（SYSCLK周期计数），当 sample被高优先
级通道抢占后，原通道的Trigger-to-sample会在重新开始sample时更新延迟时
V 1.0
间；
拟通道开始采样（不通过采样触发信号）。
一致；9
间；09
一致；
事件功能，该功能可屏蔽。支持blanking的延迟触发时间可配置，且对所有触
发源统一配置，为16bitSYSCLK周期计数；
blanking触发源的blanking窗口长度配置相同，为16bit SYSCLK周期计数器。+
源）可以正常响应，窗口内若出现其他虚拟通道触发信号（非专用周期触发），
待blanking窗口结束后，按优先级处理。若Blanking窗口内，非专用周期触发
出现重复触发，上报告警，并忽略该重复触发；
☆VcO触发源
Blanking延迟触发
O
trig
口
其他vc触发源
☆
vcO触发源
和增益校准处理（模拟ADCs(15,2)和增益u(14,12))；
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第7/16页

★
△
LRS.SARC.FUNC.SPEC【19】每个ADC控制器支持对采样结果进行数字域偏置
T

### 第8/16

V1.0
ETMCU
SARC
页
私密
■内部公开
口外部公开
工
样结果进行用户偏置和增益处理（用户配置偏置s(16,2)和增益s(15,12))；
增益处理后的采样结果进行上下电平超门限独立检测，可配置选择CBC和
中断源）、DMA请求（mux-or后的事件信号）和输出事件；超上下门限的告警
口私密
实时状态通过状态寄存器上报，告警历史状态上报通过中断模块中的status寄
存器上报；
evtsel.hi
limit.hi
pulse
set
adcevtsts.triphi
adc_result
clear
limit.lo
EVT
evtsel.lo
sample1
超门限
不超门限
hwclear
CBC
ONESHOT
sample3/
事件进行mux选择后输出4bit告警信号，每bit告警信号支持独立从16个虚拟
道配置选择对应的滤波通道，滤波器输入为ADC校准后采样结果，每个通道
支持滤波类型：FIR（阶数可任意配置，且根据配置阶数实时输出滤波结果，最
仔器工报；
sanplel
somplea
ampi4
不起门限
softtear
las
FVT
告警信号
组到
LRS.SARC.FUNC.SPEC【23】每个ADC控制器支持8个滤波通道，基于虚拟通
大32阶）、IIR（1阶）、滑动平均（归入FIR）和非滑动平均，通过配置选择；
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第8/16页

ETMCU-ET6601

### 第9/16

V1.0
ETMCU
SARC
页
保密等级：
口绝密
私密
内部公开
口外部公开
■内部公开
每组包括16个16bit寄存器，每个16bit寄存器对应一个虚拟通道的采样结果，
支持CPU和DMA读取采样结果（32个结果上报寄存器地址连续），支持8*20
个求和结果寄存器，地址连续于上诉2组结果；

### 第一组：存储上报用户偏置和增益计算处理、预处理滤波的结果，支持s(16,2)

和s(15.0)两种结果上报格式可配置选择；

### 第二组：存储上报滤波计算处理后的采样结果，支持s(16,2)和u(12,0)两种

结果上报格式可配置选择；滤波处理后上报结果：s(16,2)、u(12,0);09
求和结果：对第一组结果进行求和结果，根据第一组输出格式匹配为s(20,2)
和s(19,0)
选择后同步到CPU时钟域下，快速响应CPU读动作。
两个虚拟通道的结果放）
络环境，
口本次
a）两个虚拟通道的结果放入一个寄存器中。
和S(19.0)
ADC校准参数处理
用户配置参数处理
a2d dats_out
resultreg1
处疆
16*16bit
s(16,2)
s(15,2)/04,0可造择
pre_data_ou
款小数位各扩属2b万62），以
电平组门限检测
→EVTOUT
为用读计其寄础：得到结茶完用s（16,2）
滤波处理
sumreg
16.21
g+20bit
16.2）（12,可地
LRS.SARC.FUNC.SPEC【27】每个ADC控制器支持基于虚拟通道进行采样结果
更新标志位上报；
LRS.SARC.FUNC.SPEC【26】每个ADC控制器支持如下采样结果处理数据流：
12,0)
a2d_ data_out
萨常小数信各扩展b
2）.以
为屋读计其赛础，得到暗基定点s（16.2）
sum ree
s[29t]
8*20bit.
iz）/（z'9t
被覆盖标志位上报．
LRS.SARC.FUNC.SPEC【29】每个ADC支持4+1个DMA请求通道，
a）4个DMA请求通道可从如下DMA请求源中独立配置选择：
络环境，
款小数位各扩司
为用读计算赛础。得到桑定点s（16.2）
口本次
EOC脉冲信号（基于虚拟通道，16bit）
2组结果寄存器锁存有效采样结果（基于虚拟通道，16bit*2）
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第9/16页

ETMCU-ET6601

### 第10/16

V1.0
ETMCU
SARC
页
保密等级：口绝密
私密
■内部公开
口外部公开
ADC校准参数处理
用户配置参数处理
(12,0)
(16,2)
resultreg1
data out
16*16bit
款小数位各属2bn方16.2）
平组门限检锁
EVTOUT
为屋读计算础，得到是定用s（16,2）
滤波处理
sumreg
8*20bit
16,2)u(12,0可地源
更新标志位上报；
工
被覆盖标志位上报．
a）4个DMA请求通道可从如下DMA请求源中独立配置选择：
[16,2] signec
.2）12.0可地
EOC脉冲信号（基于虚拟通道，16bit）
2组结果寄存器锁存有效采样结果（基于虚拟通道，16bit*2）
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第9/16页

口私密
外部公开
电平超门限检测结果事件（基于虚拟通道*16bit）
过采样求和完成事件：（基于过采样求和通道8bit）
ETMCU-ET6601

### 第10/16

V1.0
ETMCU
SARC
页
保密等级：口绝密
私密
■内部公开
口外部公开
b）1个16个虚拟通道电平超门限检测结果事件或输出；
非空信号进行DMA请求，两个fifo的非空信号可独立选择到4个dma请求通
道，默认配置下不选择fifo的DMA请求；
V 1.0。
IDLE：对应ADC空闲
BUSY：对应ADC正在采样。
通道指示（IDLE时指示上一个采样的虚拟通道号，BUSY时指示当前正在
采样的虚拟通道号）。
立查询：
IDLE：对应虚拟通道空闲
PENDING：对应虚拟通道被有效触发，但处于排队状态。
BUSY：对应虚拟通道正在被执行采样。
拟通道被触发正在排队时又收到新的触发信号），上报采样触发冲突告警，每
个虚拟通道独立上报告警，该告警需要软件清除；
式为u(12.0)，范围为0~4095；
如下两种方式：
模拟ADC_CORE输出asyncready信号：控制器使用异步方式处理该ready
信号（默认选择）；
模拟AFE_TOP打拍输出syncready信号：控制器使用同步方式处理该ready
信号；
ADC校准算法处理时产生的采样结果；
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第11/16

搬移，每个ADC控制器新增两套寄存器用于fifo模式，分别对应用户偏置/增
益处理和滤波处理的采样结果数据通道；。
道结果是否映射到fifo中，bitmap由软件配置（默认为vc_en），硬件维护，
初始加载或者参数修改需要通过软件配置reload加载，vc的采样顺序必须按照
bitmap配置中vc编号从小到大的顺序；或者应用约束所有映射到fifo的vc必
须采用同一个触发源，且均处于同一个优先级；
LRS.SARC.FUNC.SPEC【39】支持软件对fifo深度的配置，fifo深度默认为16；
LRS.SARC.FUNC.SPEC【4O】通过fifo寄存器地址读取采样结果时，需要清除对
LRS.SARC.FUNC.SPEC【37】SARADC支持对采样结果按照fifo模式进行DMA
LRS.SARC.FUNC.SPEC【38】fifo模式下支持bitmap映射具体通道，控制虚拟通
应结果寄存器中的val和ovf标志；
LRS.SARC.FUNC.SPEC【41】支持通过fifo寄存器地址读取采样结果时，上报每
次读取结果对应的vc编号；
LRS.SARC.FUNC.SPEC【42】支持fifo状态上报，包含空，满，空溢出，满溢出，
fifo中数据个数。
求和通道SCh。
SARADC
ChanO
CALC
缓存通道
PChano
PFChan0
sCho
BChan 0
Chan1
ready,
校准通道
data
PChan1
SCh1
BChan1
Sum1
LRS.SARC.FUNC.SPEC【43】在预处理通道之后支持8个预处理滤波器通道、8个
缓存通道1
PChanO
SCho
BChanO
Sumo
ready
5Ch1
SARCORE
CAL
......
PChan 15
SCh7
Sum7
ChanN
trigger
Hone
乘波通道
缓存通道2
FChanO
CPU/DMA|
采样通
FChan1
道选择
SARADC
CTRL
校准、
处理、滤波、缓存控制
FChan7
模拟电路
触发信号管理
LRS.SARC.FUNC.SPEC【42】支持fifo状态上报，包含空，满，空溢出，满溢出，
fifo中数据个数。
求和通道SCh。
ChanO
CALC
预处
预处理滤波通道
PChanO
PFChan0
SCho
BChan0
Sumo
Chan1
ready,
data
校准通道
PChan1
PFChan 1
SCh1
BChan1
Sum1
SH
SARCORE
CAL
......
+.*...
SCh7
Sum7
usy
ChanN
trigger
done
滤波通道
缓存通道2
FChano
CPU/DIA
BChano
采样通
FChan1
道选择
SARADC
CTRL
校准。
处理、滤波、缓存控制
FChan7
模拟电路
触发信号管理
数字电路
↑
1）从16个预处理通道映射到8个预处理滤波器通道（映射关系寄存器可配，
最多只能从16个预处理通道中选择8个映射到预处理滤波器通道，其他的
bypass）；
2）预处理滤波支持ir滤波器（直接1型）1~4阶软件可配置，支持fir滤波器
1~8阶软件可配置；
fio中数据个数。
LRS.SARC.FUNC.SPEC【43】在预处理通道之后支持8个预处理滤波器通道、8个
求和通道SCh。
ChanO
CALC
预处理滤波通道
缓存通道1
PChan0
SCho
BChan0
Sumo
Chan1
ready,
校准通道
data
PChan1
PFChan 1
Sch1
BChan1
Sum1
SH
SARCORE
CAL
......
SCh7
BChan 15
Sum7
usy
ChanN
trigger
done
承波通道
缓存通道2
FChano
CPU/DMA
BChanO
采样通
FChan1
道选择
SARADC
CTRL
校准、预处理、滤波、缓存控制
FChan7
模拟电路
触发信号管理
数字电路
↑
1）从16个预处理通道映射到8个预处理滤波器通道（映射关系寄存器可配，
最多只能从16个预处理通道中选择8个映射到预处理滤波器通道，其他的
bypass）；t
2）预处理滤波支持ir滤波器（直接1型）1~4阶软件可配置，支持fir滤波器
1~8阶软件可配置；
求和通道SCh。
ChanO
CALC
预处理通道
预处理滤波通道
缓存通道1
PChan0
sCho
BChan0
Sumo
Chan1
ready,
校准通道
data
PChan1
PFChan 1
SCh1
BChan1
Sum1
SH
SARCORE
CAL
......
SCh7
Sum7
ousy
ChanN
trigger
done
滤皮通道
缓存通道2
CPU/DMA
FChanO
采样通
FChan1
道选择
SARADC
CTRL
校准、预处理、滤波、缓存拉制
FChan7
模拟电路
触发信号管理
数字电路
1）从16个预处理通道映射到8个预处理滤波器通道（映射关系寄存器可配，
最多只能从16个预处理通道中选择8个映射到预处理滤波器通道，其他的
bypass）；
2）预处理滤波支持ir滤波器（直接1型）1~4阶软件可配置，支持fir滤波器
1~8阶软件可配置；
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第11/16页

Hone
康波通道
BChano
BChan1
校准、
预处理、滤波、缓存控制
↑
ETMCU-ET6601

### 第12/16

V1.0
ETMCU
SARC
页
保密等级：口绝密
私密
内部公开
口外部公开
口私密
■内部公开
3）预处理滤通道输入数据可进行放大和缩小（算数左移或者算数右移，带符号
移位），移位的范围为：-1~2（负数表示左移，正数表示右移；原始预处理
通道输入数据为s(16,2)，此处为了对标TI：ET6801-DOC\05.数字设计\03
implementation-with-the-fmac-using-stm32cubeg4-mcu-package-
stmicroelectronics(1)(2).pdf);
In theADC,thefactorKADc=8isappliedusing theleft justificationfeature.TheADCresult(aftersubtracting the
offset)isa12-bitsignedinteger.nright-alignedformat,theresultissign-extendedto16-bits:
Table3.Right alignedADCdata
15
14
13
12
11
10
9
8
7
6
5
3
2
1
sign
b11
b10
b9
b8
b7
b6
b5
b4
b3
b2
b1
bo
Table4.LeftalignedADCdata
4
0
农
b)
c)
求和功能；70
bg
求和功能；
间隔期间允许其它低优先级进行采样；
d)
count及N支持影子加载，触发时完成影子值到生效值更新；
e)
过采期间忽略新触发，但会告警；
G
过采样被高优先级通道打断后，支持resume、conti模式；
g)
过采功能支持使能控制；
a)
低优先级虚拟通道在高优先级通道结束后，继续低优先级请求；
b）增加使能控制；
翌创微电子保密信息未经授权禁止扩散

### 第12/16页

过米浆和次数N<=16；
采样间隔count为22bit配置，单位为sarc工作时钟；
f)

### 第13/16

V1.0
ETMCU
SARC
页。
保密等级：口绝密
私密
■内部公开
口外部公开
页
外部公开
*2.2中断管理
of-conversion）信号产生，用于触发中断，EOC脉冲信号可配置选择如下三个
产生位置，每个ADC控制器的虚拟通道统一配置：
S/H窗口结束时刻，
采样转换结束时刻，默认选择
S/H窗口开始时刻
工
配置，16bitSYSCLK时钟计数值；且每个ADC控制器的虚拟通道统一配置。
如果当前EOC到来时，上一个EOC的延时处理没有完成，则在该时刻输出上
一个EOC的中断触发，同时当前EOC进行延时模块进行延时处理；
end_p到来时，上一个end_p的delay还没
有完成，则在该时刻输出上一个end_p的
int_trig，然后当前enc_p进行delay模块重
end_p
新开始计数延时。
-delay_i
delay_j
来时，上一个EOC的延时处理未完成状态，告警状态软件读清；并且同时上报
延时未处理完成的虚拟通道编号；
1．其中1路中断包括：
电平超门限中断（基于虚拟通道，超门限脉冲触发中断，超上下门限独立中
断源，共16bit*2）

### 2.另外4路中断中，每1路中断可独立选择以下中断作为中断源；

EOC脉冲信号（基于虚拟通道，16bit）
2组结果寄存器锁存有效采样结果中断（基于虚拟通道，16bit*2）
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第13/16页

LRS.SARC.INTR.SPEC【04】每个ADC支持5路中断输出；
ETMCU-ET6601

### 第14/16

V1.0
SARC
保密等级：口绝密
私密
■内部公开
口外部公开
ETMCU
页
口私密
外部公开
北
过采求和结果有效中断(基于过采求和通道，8bit)
"2.3事件管理.
每个ADC控制器支持如下事件输出：

### 2.3事件管理

工
ADC输出到XBAR电平超门限检测输出事件*4（从16个VC事件中独立
配置选择）

### 2.4约束说明

宽度要大于1个系统时钟周期（因为是同步处理）；
小间隔FIR滤波阶数个系统时钟周期）
准流程完成后再打开模拟ADC使能；
进行配置，配置完成后再将vc_en打开；

### 第15/16

其他使能信号（

### 2.5触发源说明。

发源信号可独立配置选择：
sample触发源。
位域。
SARCO/1
SPWM
[23:0]
每个ADC控制器中16个虚拟通道支持如下采样触
ETIM
[49:36] 
etim2adc_evt[13:0]
RESERVED
[52:50]
*OP。
IPTEST
53
iptest_adc_start
CMPC
[75:54] 
cmpcctripl[10],cmpc_ctriph[10],
LRS.SARC.TRIG.SPEC【01】
位域
OP。
cmpc_ctripl[9l.cmpc_ctriph[9],
触发源说明
OP
*OP
STM
[99:76]
tm5_oc_exp[3:0],
stm0_oc_exp[3:0]}
CLU
[103:100]
xbar2sarc_cludata[3:0]
ADCEOC
[109:104]
Lsarc2_eoc2spl_trig [1:0],
2022年12月22日
翌创微电子保密信息未经授权禁止扩散

### 第15/16页

ETMCU-ET6601

### 第16/16

V 1.0
ETMCU
SARC
页
保密等级：口绝密
私密
■内部公开
外部公开
V1.0
sarc0_eoc2spl_trig[1:0]}
GPIO（inputxbar)
[110]
inputxbar_data[4]
RESERVED
[127:111]
tOP.
Blanking功能支持如下触发源进行触发启动：
blanking触发源
位域
SPWM
[23:0]
口私密
[110]。
OP
ETIM
[49:36]
etim2adc_evt[13:0]
[52:50]
