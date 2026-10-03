# SARC LLD 详细设计文档

> 本文档由大模型逐图逐页提取自原始截图，不作主观修饰，忠实还原原文。
> 图表、时序波形及模糊部分均标注对应截图原图文件名供查阅。


---
## 图像编号 1 (原图: `GameViewer_1EC7JuTBH6.png`)

### 【左页】

DATAPIPE采用单口RAM实现。RAM地址为8位，高3位
选择滤波通道0-7，低5位表示每个滤波通道的32个PIPEDATA。
缓存通道
每个SARADC控制器包含2组16*16bit结果寄存器。每组的
16个寄存器与虚拟通道一一对应。
第一组：存储上报用户偏置和增益计算处理后的采样结果，
支持s(16,2)和s(16,0）（寄存器实际只有s(15,0)有效，最高两位
均为符号位）两种结果上报格式可配置选择；
第二组：存储上报滤波计算处理后的采样结果，支持s(16,2)
和u(12,0)两种结果上报格式可配置选择;
每个SARADC控制器包含1组8*20bit结果寄存器，该结果
格式同第一组格式配置选择一致，支持输出 s(20,2),s(19,0)；8
个寄存器与用户预处理滤波通道一一对应。
采样结果上报支持result_ovf（结果被覆盖标志）、resultval
（结果有效标志）、result data（结果数据）。


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-24结果寄存器读写`，完整结构与时序请查看原图 `GameViewer_1EC7JuTBH6.png`。

Result_in_enb
Result _in
Ids_Result_reg
Result_val_in_enb
Result_val_in
Ids_Result_val_reg
Result_ovf_in_enb
Result_ovf_in
an. 11 2026-10-02-21-44
Re ad ciear
Result_ovf_reg

**图5-24结果寄存器读写**

时序示意
6002新增实现：用SARADC控制器使能cfg_sarcen的上升
沿清零resultovf（结果被覆盖标志）、resultval（结果有效标
志）、result_data（结果数据）寄存器状态。
ETNCIbhuar

#### 5.19通过fifo模式读取采样结果

每个ADC控制器有如下2组结果存储寄存器，每组包含16
个寄存器，分别对应16个vc，
·用户偏置和增益计算处理后的采样结果寄存器组
·滤波计算处理后的采样结果寄存器组
1080F



---
## 图像编号 2 (原图: `GameViewer_3VjshoX5So.png`)

### 【左页】

说明：
queue_manage
模块在准备下一次转换通道号调度时，如果检
测到blanking有效，则不启动正在排队转换的VC，需要待
VCo的触发源（blanking窗口有效时的专用触发源）到来时
启动VCo的转换。blanking结束后，继续执行之前的队列。
SARC数据流程
SARC模块转换结果数据处理流程及相关配置系数：
BTMCU hoan
转换结果从ADCCORE输出，先将12bit无符号数转成12bit
有符号数 s(12,0)，然后将整数和小数位各扩展2bit得到 s(16,2),
以此数据形式经过数字校正dig_cal、.预处理pre_process和滤波
处理filter，最终得到 s(16,2)有符号数，将此数据通过软件配置
进行定点格式转换，然后存入对应的缓存通道。
(o'zt)n
用户配置参数处理
EVTOUT
ETHCU 3
滤波处理
ETMCU mian. 1i


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-3SARC数据流程图`，完整结构与时序请查看原图 `GameViewer_3VjshoX5So.png`。


**图5-3SARC数据流程图**

注意:
1、s(a,b)：表示a bit有符号数，a为总的位宽（包括1bit符
号位+整数位宽+小数位宽），b表示小数位宽；
2、u(a,b)：表示a bit无符号数，a为总的位宽（整数位宽+
小数位宽），b表示小数位宽；
BTMCU huan Ji
各采样结果上报位置数据格式处理：
校准阶段上报校准寄存器结果：s(16,2)
ATE测试时输出结果：u(12,0)，范围0~4095
用户预处理后上报结果：s(16,2)；s(16,0)
（寄存器实际只有
s(15,0)有效，最高位均为符号位)
滤波处理后上报结果：s(16,2)，u(12,0)范围0~4095

#### 5.2 时钟关系

hian li 2026-10-02
SYSCLK：此时钟为 SRAC控制器模块工作时钟，直接用
AHB的总线时钟。
1080F



---
## 图像编号 3 (原图: `GameViewer_3ZWo3TthG6.png`)

### 【左页】

目录
. Ji
1. 模块 OR DR需求
2. 概述
3.功能描述
ETNCU hoan.T1
4.接口说明
BTMCU huan. J3

#### 4.1SARADC接口信号


#### 4.2 SARADC 接口时序

采样时间
接口时序
BTMCV man. 11 2086-10-02-21:42
5.方案设计

#### 5.1SARC整体结构


#### 5.2时钟关系


#### 5.3 SARADC CALC


#### 5.4外部触发源

FTMCU

#### 5.1触发模式



### 【右页】

单次触发模式
连续触发模式
5. 1blanking机制
.J1 2026-10-92-21:42

#### 5.1优先级队列管理


#### 5.2 SARADC控制器看门狗


#### 5.3 SARADC控制时序


#### 5.4ADC 同步模式

huan, 11 20a6-10-02-27:42

#### 5.5软件直接触发采样

ETHCI

#### 5.6SARADC控制器中断


#### 5.7转换后处理


#### 5.8预处理通道


#### 5.9滤波通道

BTMOU huan. J1 026-10-02-21:42
ETMCU muan. J1 2026-10-00-21:
HR
FIR
滑动平均
非滑动平均
MOU hiar. 13
滤波器实现时序
3 2026-10-02-21;42
FIR滤波器参数存储
12080F



---
## 图像编号 4 (原图: `GameViewer_40i6eF4ZKV.png`)

### 【左页】


#### 5.7优先级队列管理

队列管理模块实现16个虚拟通道VC的转换序列调度管理。
vc_flag_in[15:0]为vc_flag_ctrl 模块输出，指示虚拟通道
（vc15-vc0）的转换请求标志，1表示对应虚拟通道有转换请求，
0表示无请求。
vc_priority[31:0]为虚拟通道（vc15-vco）的优先级指示，每
个虚拟通道2bit表示。
vc_num[3:0]为优先级队列管理模块输出，指示下一个启动转
换的虚拟通道VC编号，即输出当前优先级最高的虚拟通道编
号。
vc_num_val为优先级队列管理模块输出有效指示，指示输出
的vc_num[3:0]虚拟通道编号有效。
none_flag指示当前没有需要转换的队列，所有触发转换完成。
该信号高电平有效，为0表示还有队列需要转换。
preemtive_md：po优先级抢占模式指示，1为po可抢占模式,
0为不可抢占模式；


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-13优先级队列管理`，完整结构与时序请查看原图 `GameViewer_40i6eF4ZKV.png`。

priority_confilct:抢占模式开启下的优先级指示，1指示优先
级冲突，当前存在pO优先级请求，需由外部的请求处理模块重
发vc_numreq完成处理后，才会拉低；未开启抢占功能时一直
为0;
vc_queue

**图5-13优先级队列管理**

BTNCU huan. Ji 2026-10-02-2) 49

#### 5.8.ADC同步模式

同步采样：多个ADCCORE同时采样不同信号源。
几余采样：多个ADCCORE同时采样相同信号源。
由于ADC的触发源选择独立，故在实现ADC同步模式时，
需要软件保证将参与同步模式的ADC配置为相同的采样触发信
号源。
ADC同步并联模式下，软件在启动同步采样转换时，要确保
当前参与同步采样的ADCCORE都处于IDLE状态。
2026-10-02-21;43
1080F



---
## 图像编号 5 (原图: `GameViewer_a0rP8s7Oan.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-10blanking机制原理示意`，完整结构与时序请查看原图 `GameViewer_a0rP8s7Oan.png`。

blanking窗口内虚拟通道0的触发（专用周期触发源）可以
正常响应，窗口内若出现其他虚拟通道的触发信号，记录该虚
拟通道被触发的行为但不响应，待blanking窗口结束后，T再按
各自优先级进行排队响应。
若Blanking窗口未结束，其他触发信号（非专用周期触发）
出现重复触发，上报告警，并忽略该重复触发（blanking窗口
内非VCO的触发信号只记录一次）。
blanking机制的基本原理如下图：
vaD柱发源
Blanking延近远触发
Bianking 家口
ttg.
★banking腐口细束胆，根据价先级，明应O口△各一次，
biankagm口内O口出现量复技发，产生专善，
ETHCU hnan.li

**图5-10blanking机制原理示意**

RTMCV hlan 2i 2026-10-02-21:4
RTMCU huar 1i 9026-1
ETMCU miam.11


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-11blanking机制`，完整结构与时序请查看原图 `GameViewer_a0rP8s7Oan.png`。

> 📌 **【图表提示】**: 此处包含图表 `图5-12blanking模块状态转移`，完整结构与时序请查看原图 `GameViewer_a0rP8s7Oan.png`。

banking_en
blanking_trig
bianking
ETNOU/
blanking_fiag
delay
alaniing window len

**图5-11blanking机制**

时序示意图
BTMCU huan.J1 0
ETNCU huan Ji 2026-10-02-2) 49
BLANK_IDLE
wait for en &&trig
blank_en_r==1 &&
blank_trig==1
BLANK_DELAY
win_cnt==blank_len_r
n11
trig delay
delay_cnt==blank_delay_r
BLANK_WORK
generate blank valid window

**图5-12blanking模块状态转移**

RTNOV
304 I
12080F



---
## 图像编号 6 (原图: `GameViewer_aPDFQVxWhA.png`)

### 【左页】


**表1-1修订记录**

huan.
版本号
修订内容
修订日期
修订人员
BTMCU muan.1i
BTMCU huan.Ji
首次修订
肖中平
1、在预处理通道之后新增8个预处理滤波器通道；
ET6801下修改点如下：
郑汶
1.增益补偿-2048处理；
同步输出adc结果到cpu_wrap:
ETHCIhuan
3.fifo模式的空溢出/满益出标志问题fix；
. Ji
4.eoc中断位置增加；
5.模拟变更(物理通道通道增加等)
ETHCU huan, 1i
ETHOU hauan li
2026-70~02-7


### 【右页】

注：浅蓝色和清绿色相关区域为ET6601新加的改动，包括线，背景及底
纹部分；
ETHCUhUa3,11 2026-10-m2-21: 42
ETHC/
BTMCU huan. Ji 0026-10-02-21:42
. J1 2026-10-0-21:
FTMOU hran.J3
3 2026-10-02-21;42
dan
13080F



---
## 图像编号 7 (原图: `GameViewer_ba6sdetThH.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-17`，完整结构与时序请查看原图 `GameViewer_ba6sdetThH.png`。

X+1
. Ji
saradc_mode
Xn
X n+1
mux se[3:0]
Xn+2
mux, d[3:0]。
xm
Xdatan
X@ata n+1

**图5-17**

BTMCU huan.j3 2026-10
数模接口信号时序示意
BTMCU hoan. Ji
87MCV731873.13
ETMCU Tnuan.Z1


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-18一次采样转换控制时序示意`，完整结构与时序请查看原图 `GameViewer_ba6sdetThH.png`。

PD
sarad_en
saradc_start
SH
coversion
ue"swgds~ape
apow.aotg3e/es
saradc_mode
uan. 11 2026-10-02-2) 49
sarac_mx_se3.0-Ho
channeli n
channel m
sarad_mu_d3.0[
H0
saradc_ready
oid data
resutn
saradc_data
VCO.FLAG
VC1.FLAG

**图5-18一次采样转换控制时序示意**

ETMoyhuar.2)
ETNOV;43
2026-10-02-21;43
12080F



---
## 图像编号 8 (原图: `GameViewer_be9VqBBdbM.png`)

### 【左页】

CHENGDUET
MICROELECTRONCS COJAT,
ETICU huan
ETHOI hua.1 2026-10-02-2242
ETHCU huan. J3
SARC #
模块方案设计
ETHCU huan, 11 2028-10-02-21:42
ETHO/
ETMCU muan.11
FTMCU T


### 【右页】

设计:
郑汶
评审!
批准:
ETMCU nOan, 11
ETHCI
BTMCU huan.Ji 0026-10-02-21:42
. J1 2026-10-00-21:6
FTMCU hrar. 13
3 2026-10-02-21;42



---
## 图像编号 9 (原图: `GameViewer_bG98ufwLis.png`)

### 【左页】

能，则输出blanking管理后的有效窗口标志信号。blanking窗口
有效信号内，只有VCO可以正常触发采样，其它VC需要要待
blanking窗口结束后再排队进行采样。
vc_flag_ctrl：VC转换标志管理模块。该模块根据VC的触发
状态、软件启动转换状态softforce等相关信息，管理虚拟通道
VC的转换标志。VC有转换请求，其相应的vc_flag置1，否则
置0。该模块输出16bit的vc_flag标志，代表16个VC的转换
标志。当blanking窗口有效时，该模块只输出vco的转换flag，
待blanking窗口结束后，再输出正常操作的所有转换flag。包
含一个过采样ovs_ctrl模块，当虚拟通道的启用滤波过采样求和
功能时，接收外部触发，自动完成N次采样触发，根据
resume/conti模式配置，并获取queue_manage输出排队信息，
自动高优先级抢占情况下的恢复处理；
queue_manage：SARC 控制器的转换队列管理模块。该模块
为 SYSCLK 时钟域。根据 digi-anal_IF_timing 模块返回的计数
器状态，通过VC转换标志vc_flag[15:0]、VC 的优先级配置
vc_priority[31:0]，输出当前有转换请求的VC中，优先级最高
2086-10~02-21:43


### 【右页】

络环境，以改善远程控制体验。
的一个VC 编号。若开启抢占功能，当前正在转
口本次远程不再提醒
知道了
现po的转换请求，输出当前po的请求；
vc_flag_ctrl模块负责触发采样、软件采样和blanking功能等
处理后的最终转换请求，进行过采模式下的flag控制，抢占模
式下的flag恢复。queue_manage模块按优先级对转换请求进行
调度。两个模块将sarc的采样转换控制分成两个互不耦合的阶
段。
sarc_conver_info_queue：转换参数管理模块。根据
queue_manage模块输出的当前优先级最高的vC编号，读取该
VC 的相关转换参数，输出到digi-anal_IF_timing模块。
digi-anal_IF_timing：数模接口转换时序产生模块，产生
ADCCORE工作的相关控制时序。
digi_cal：数字域的校正处理模块。
pre-processing：预处理模块、预处滤波。
filter：滤波模块。
reg1/2：结果缓存模块。
sum_ctrl：过采求和模块；
ETNCV
sum:求和结果输出；
2026-10-02-21;43
1080F



---
## 图像编号 10 (原图: `GameViewer_BMYV2LGXFN.png`)

### 【左页】


#### 4.2 SARADC接口时序

BT采样时间
8TMChuan.Ji/
Ji
单次ADC转换中，采样最小用2.5UI，转换用13UI，打拍用

#### 0.5UI，总共16UI。这样ADC的最高采样率50M时钟为


#### 3.125MHz，66M时钟为4.125MHz。

接口时序
.J3
counter
san
X+1-
triger_mode
saradc_mode
Xn+1
mux_se[3:0]
X0+2
huan
Xdatan
时序示意


### 【右页】

络环境，以改善远程控制体验。
口本次远程不再提醒
知道了
说明：
上图中，2个红色的沿和2个绿色的沿分别表示两次采样转换
的开始和结束。
采样转换结果控制信号ready是根据start或者spltime_en的下
降沿（二者较晚的一个下降沿）拉低。
start、spltime_en信号由 SARC控制器产生，通过计数器控制
（计数范围为0～（15+spltime）），不与ready信号握手。
ready信号由模拟ADC产生，在ready的上升沿将data数据
拍出。
不增加采样时间模式下，“每次采样转换固定为16个UI；增加
采样时间模式下，C每次采样转换时间为spltime+16UI。
JMCU(n1am.1i 2026-10-02-21;42
ETHCV ;42
1080F



---
## 图像编号 11 (原图: `GameViewer_CCQu4ftpmA.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-7外部触发源处理`，完整结构与时序请查看原图 `GameViewer_CCQu4ftpmA.png`。


#### 5.4外部触发源

112026-10~02-21:42
外部共有128个采样触发源和64个blanking触发源（含
reserved位域），每个ADC控制器支持16个虚拟通道VCo-VC15。
SARC的采样触发源如下：
见SARC模块LRS文档触发源说明
个 SARC 的 blanking触发源如下：
见SARC模块LRS文档触发源说明
对外部输入触发源，先在sarc_wrap进行取上升沿操作处理后
送入对应的sarc_core，再根据16个VC的使能配置、触发源选
择配置及触发模式配置，屏蔽无效触发源，产生16个VC对应
的16bit有效触发源。
blanking触发源的处理类似采样触发源。
tigin[127:0,capture
trig mask
trig_masked[15:0],
posedge
ADC_VC_CTL,TRIG_MOD
RTMCV plan 2i 2026-

**图5-7外部触发源处理**

ETMCU mian. 1i


### 【右页】


#### 5.5触发模式

单次触发模式VC一次配置只触发一次转换，VCEN打开一次只响应一次触发
连续触发模式VC一次配置可多次触发转换，VC_EN打开时，可连续响应多次触发
单次触发模式
：18-20-07-980
单次触发模式：虚拟通道每次配置生效后，只响应一次触发。
要求软件每次配置通道前将对应的虚拟通道使能vcen 关闭，
待配置完成后再打开，硬件通过vcen的上升沿动作来产生虚
拟通道重新配置参数的标志。
检测到该虚拟通道配置且VC EN有效，ONE SHOTEN置
1，等待该虚拟通道的触发。
检测到触发TRIG且ONESHOTEN为高，将VCFLAG置
1，同时将ONESHOTEN置0。1:4
待该虚拟通道获得优先级后，开始启动转换操作。
注意：在单次触发模式下，当VC的触发产生时，如果对应
的ONE_SHOT_EN信号为低，此时不能将对应的VCFLAG置
1，即该VC不响应本次触发。
1080F



---
## 图像编号 12 (原图: `GameViewer_cTDH1vvDLo.png`)

### 【左页】

对每组结果寄存器分别增加1个对应的寄存器，该寄存器可
通过软件配置bitmap映射为fifo模式，两组结果寄存器对应fifo
模式的参数独立配置。
cfg_*_fifo_vc_sel选择在vc_en有效的vc中，哪些vc对应的
结果寄存器映射到fifo，默认vc_en有效的vc都映射到fifo。即
有效的 bitmap=cfg_*_fifo_vc_sel & cfg_vc_en。
注意：
·软件在初始化或者更新bitmap相关配置后，都需要对
cfg_*_fifo_bitmap_reload进行写 1操作。
●软件配置vc的采样顺序必须按照bitmap配置中vc编号从
小到大的顺序。
硬件控制fifo映射关系的bitmap时序如下图所示：
ETMCI TRian.
fifo_rd_valid_out
fifo_rd_ack_im
fifo_rd_data_in
判断reload条件：用
ETNO
One-hot取反后与原
值与
BTMCUhian.1i


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-20EOC延时处理示意`，完整结构与时序请查看原图 `GameViewer_cTDH1vvDLo.png`。


#### 5.20 SARADC 控制器中断

6002功能增加点1（产生EOC标志）：
ETMCU huian.1i
每个ADC控制器的虚拟通道支持对应EOC（end-of-
conversion）信号产生，用于触发中断，EOC脉冲信号可配置
选择如下两个产生位置，每个ADC控制器的虚拟通道统配置：
S/H窗口结束时刻，
采样转换结束时刻，默认选择
S/H窗口开始时刻
支持EOC选择位置时刻到中断产生的上沿延时可配置，16bit
SYSCLK时钟计数值；且每个ADC控制器的虚拟通道统一配
置。如果当前EOC到来时，上一个EOC的延时处理没有完成，
则在该时刻输出上一个EOC 的中断触发，同时当前EOC进行
延时模块进行延时处理。
end_p到未时，上一个end_p的delay还没
有完成，则在该时割输出上一个end_p的
int_trig，然后当前enc_p进行delay棋块重
d'pua
新开始计数延时，
int_trig
Hdelay_
ETNCUV

**图5-20EOC延时处理示意**

233 Ⅱ
1080F



---
## 图像编号 13 (原图: `GameViewer_e8XPWSdAMt.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-23FIR和IIR滤波器实现时序示意`，完整结构与时序请查看原图 `GameViewer_e8XPWSdAMt.png`。


**图5-23FIR和IIR滤波器实现时序示意**

FIR滤波器参数存储
EIMCU
ETWCU huan.Ji
Ram_slice_O(fir_cho data)
Ram_slice_1(fir_ch1 data)
ITTTT-OTO: 00000-OTO
Ram_slice_2(fin ch2 data)
Ram_slice_3(fir_ch3 data)
ETNC hua7 11 202F-70-02-21
Ram_slice_4(fir_ch4data)
BTHCU huan. Ji
Ram_slice_5(fir_ch5 data)
Ram_slice_6(fir_ch6data)
Ram_slice_7(fir ch7data)
ETMCI
From idserb
From ids data
From ids enb Id
Ram_ce_n
Ram_we_n
From ids data
Ram_rdata
quz sp, o4
toid data
Ram_rdata to ids
RTMCIhian.Ti 202
STMCI
RTMCI


### 【右页】

FIR的滤波参数由AHB总线配置，在SARC内部由1个简单
双口RAM存储。该RAM与IDS之间采用间接寻址访问，写操
作只能总线访问，读操作可由总线和内部逻辑二者共同访问，
但内部逻辑的访问优先级高。
RAM地址为8位，高3位选择滤波通道0-7，低5位表示每
个滤波通道的32个参数地址。
FIR滤波器输入采样结果PIPELINE
BTMCl/ buan. 1 2026-
Ram_slice_x(fir_chxdata)
Data_pipe[0]
Data_pipe[1]
Data pipe[2]
ETNC!!
Data_pipe[3]
Data_pipe[29]
Data_pipe[30]
Data_pipe[31]
ETNCIT huan: 11 2026-10-02-21 44
12 fp
2080F



---
## 图像编号 14 (原图: `GameViewer_Ef2CwLAmR0.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-xFIR滤波器的结构`，完整结构与时序请查看原图 `GameViewer_Ef2CwLAmR0.png`。

+yin]
BIMCU
b[1]
BTNCU hua
. Ji
xin-1]
b[2]
X(n-2)
b[3]
BTMCUhua.7:3026-10-02-21:43
[-ux
STLU huan.Ji
[Nq
X(n-N]
图5-xFIR滤波器的结构
hiar. Ti 2026
ETICU
ETMCU han. li

#### 5.14.1IIR滤波器（直接1型）

Y=B*X+A*Y
(5-3)
ZK-o bXn-k+ZM akyn-k)
(5-4)


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-xIIR滤波器（直接1型）的结构`，完整结构与时序请查看原图 `GameViewer_Ef2CwLAmR0.png`。

这个功能实现了一个无限脉冲响应(IIR)滤波器。滤波器输出
向量Y是长度为N+1的系数向量B和不确定长度的向量X的
卷积，加上延迟输出向量Yi与长度为M的第二个系数向量A的
卷积。Y中每次新增的元素：n=B*Xn+A*Yn-1，其中
M个Y中的元素组成。
IIR滤波器（直接1型）的结构如下图所示。
x[n]
x[n-1]
[n-1]
ETNCU hian.li 2026-10-02-21:
x[n-2]
×[n-3]
[n-3]
[n-N]
[n-M]
ETNCU ;43
图5-xIIR滤波器（直接1型）的结构
2026-10-02-21;43
1080F



---
## 图像编号 15 (原图: `GameViewer_HFc4FYW2ed.png`)

### 【左页】

滑动平均
“滑动平均功能通过FIR滤波器实现，可以归入FIR滤波类
型，通过用户参数配置实现。
“滑动平均”就是按我们事先设定的信号个数将输入信号加以
平均。譬如，按每4个信号做一次平均，如下图所示：
x(n)
x(n1)
x(n-2)
(eu)x
z-1
ETMCU haan. J3
h(2)(
h(0)
y(n)
ran.T1 2026-70-02-2
非滑动平均
ETMCI
“非滑动平均”滤波，根据用户配置的滤波次数，将2n个转
换结果进行累加，然后通过将累加和右移n位，得到非滑动平
均的滤波结果。其原理示意图如下：
KTMO)I


### 【右页】

x[0)
.Ti
2"个
u<<
>filter_data_out
n取值范围为4bit可配置，良
即最大滤波次数为215
BTMC(/ buan. 11
ETMOII hoan.11
ETMCIF hian. 1
ETNC(l
12080F



---
## 图像编号 16 (原图: `GameViewer_iSOJmCn28m.png`)

### 【左页】

FIR
6002修改点：阶数可任意配置，且根据配置阶数实时输出滤
波结果，最大32阶。
有限脉冲响应(Finite ImpulseResponse,FIR)。线性，不带反馈。
y(k) = Z a(n)x(k-n)
ETNOI han 14 2026-10-02
BTHCU haan. J3
x(k)：输入时间序列;
a(n)：滤波器参数，N为滤波器的阶数;
y(k)：输出时间序列;
ETMCI
FIR滤波器图解形式：
a(1)
a(3)×
4(0)e
a(4)-
a(N-1)
RTMCy haan i2026
KTMOI


### 【右页】

无限脉冲响应(Infinite Impulse Response，IR)。非线性，带反
馈。
y(n) =
ar3(n -k) +ba(n - k)
k=1
k=0
x(n)：输入时间序列;
buan. 11
a(k)、b(k)：滤波器参数，N、M为滤波器的阶数;
y(n)：输出时间序列;
SARC模块通过一阶低通滤波器来实现一阶IR滤波。一阶低
通滤波算法原理如下：
1.一阶低通滤波算法原理
BTMCl
阶减波，又叫一价惯性滤波，或一阶低通减波，款件实现RC低通滤波圈的功能。
Y(n) =aαX(n) + (1 -α)Y(n - 1)
式中：α为滤波系数，X(n)为本次采样值，Y(n-1)为上次滤波输出值，Y(n)为本次滤波输出值
2080F



---
## 图像编号 17 (原图: `GameViewer_LoWatHzLVG.png`)

### 【左页】


#### 1.1.1抢占功能

T22a.11
BIMCU huan.
ve_flag_ctrl
ETMCU hUE
ve_f1ag[15:0]
-none_f1ag→
priority_enflt+
sare_smaple_ctr1
vc_queue
start/er
模拟ADC
ua.j3
抢占功能控制如下：
rc_num/val-
&TMCU hoan. J3
1.由vc_queue模块完成识别vc_flag_ctrl输入的vc_flag[15:0]中的优先
级冲突,包含blanking情况的冲突，判定当前队列优先级和当前输出
的vc_num的优先级是否冲突，输出priority_cnflt信号；
2.sarc_sample_ctrl模块识别到priority_cnflt信号，根据priority_cnflt的
时机进行不同的时序控制：：
ii.
可直接进行抢占；
需delay发起抢占(不区分队列是否存在其它请求，统一delay);


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `时序图原文件：ET6601-DOCI05.数字设计`，完整结构与时序请查看原图 `GameViewer_LoWatHzLVG.png`。

> 📌 **【图表提示】**: 此处包含图表 `图5-18采样抢占时序图`，完整结构与时序请查看原图 `GameViewer_LoWatHzLVG.png`。

TNCUhuarn.11
若抢占发生在连续两笔转换的交接区，需输出sarca2doutrdhold
使模拟保证不影响第一次的ready&data的返回时序；
huan Ji 2026-10-02-2) 49
时序图原文件：ET6601-DOCI05.数字设计
103%20HACISARCIV100\01.需求分析\02.需求分析\抢占控制.xlsx

**图5-18采样抢占时序图**

1.模拟接收抢占控制，完成采样转换后返回高优先级对应的ready及
data信息；
2.vc_flag_ctrl接收该ready信号，priority_conflt，start信号；
a)发出 start 后清除vc_flag;
26-10-02-21;43
b)若期间因抢占导致该对应的start无法返回ready，需重新将vc_flag
拉起；
c)使用对应返回的ready指示该vc_flag的完整结束；
2026-10-02-21;43
12080F



---
## 图像编号 18 (原图: `GameViewer_LWEUsHJgSN.png`)

### 【左页】

2.概述
SARADC主要用于采集片外电压、电流、温度、压力等信息，
采样片内温度、电压、电流信息（可选），以及采样片内运放输
出。
本文主要介绍内置SARADC控制器的设计方案，主要涵盖
ADC工作模式配置和管理，数字校准，虚拟通道映射，优先级
控制，采样触发控制，采样缓存处理，信号预处理，事件管理
和中断上报等功能。
当前版本sarc不支持差分模式，仅支持单端模式，但文档中仍保留
相关差分内容。
3. 功能描述
ETMCV 20
ETICU
EIMCU
SCRADC


### 【右页】

图1.SARADC框图
SARC模块主要实现SARADCIP的采样控制和数据后处理，
具体功能包括：
1、支持对SARADC模拟IP进行配置和管理；
2、支持对SARADC模拟IP进行数字校准（SARADC
CALC);
3、支持SARADC通道到虚拟通道映射；
huan.Ji
4、
支持SARADC通道触发信号优先级抢占控制；
5、支持SARADC通道事件管理和中断上报；
6、
支持SARADC通道输出的缓存和预处理；
7、
支持触发信号的周期延迟blanking机制。
Tuan. J1 2026-10-00-21:
8、支持 SARADC 预处理之后的数据可选地经过预处理滤波
器，滤波器滤波器的类型为firl~8阶/iirl~4阶，软件可配
置;
9、支持预处理滤波通道启用过采样求和功能；
EINCU
;
1080F



---
## 图像编号 19 (原图: `GameViewer_m4qMLaqKqw.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-20EOC模块输入信号时序关系图`，完整结构与时序请查看原图 `GameViewer_m4qMLaqKqw.png`。

下图指示EOC模块输入信号的时序关系：
EOC的位置可以配置选择采样结束或者转换结束：
采样结束sh_endp：adc_spltime_en为低时（无扩展采样）选
择 adc_start_ld 的下降沿信号 adc_start_ld_neg（sysclk）；
adc_spltime_en为高时（有扩展采样）选择adc_spltime_en_1d的
下降沿信号adc_spltime_en_1d_neg（sysclk）;
转换结束 cvt_end_p：选择 adc_ready_in_ld 的上升沿信号
adc_ready_sarc (sysclk);
ETMCI TRan. 13

**图5-20EOC模块输入信号时序关系图**

6002功能修改点2（中断源）：
每个ADC支持1路中断输出中断源包括：
DEOC 脉冲信号（基手虚拟通道，16bit）
ETMCU hian. Ti


### 【右页】

21:4号
口电平超门限中断（基手虚拟通道，超门限脉冲触发中断，
超上下门限独立中断源，共16bit*2）
口2组结果寄存器锁存有效采样结果中断（基手虚拟通道，
16bit*2)
口1组求和结果寄存器锁存有效采样结果中断（基手求和通道，
8bit)
6601功能修改点2（中断源）：
每个ADC支持1+4路中断输出，1个中断源包括：
口EOC脉冲信号（基手虚拟通道，16bit）
口电平超门限中断（基于虚拟通道，超门限脉冲触发中断，
超上下门限独立中断源，共16bit*2）
口2组结果寄存器锁存有效采样结果中断（基手虚拟通道，
16bit*2)
4套中断逻辑可以任选以下源作为中断源；
EOC脉冲信号（基于虚拟通道，16bit）
口2组结果寄存器锁存有效采样结果中断（基于虚拟通道，
16bit*2)
1080F



---
## 图像编号 20 (原图: `GameViewer_mjeYzTB3j7.png`)

### 【左页】


#### 5.11角

触发采样延时捕获
该功能为6002新增。
8TMCU huan. J1
ETHCU huan.
每个ADC控制器支持基于虚拟通道进行Trigger-to-sample 延
迟计算，并上报延迟时间（SYSCLK周期计数);
延迟时间为收到有效触发到采样开始的时间，每个虚拟通道
独立上报。
每个 ADC 控制器有一个基于 SYSCLK 的全局 12bit free-run
计数器，最大可计4096个SYSCLK时钟周期，该计数器的值
软件可实时读取。
注意：当 Trigger-to-sample 的延迟时间超过4096 个周期时,
会上报错误的延迟时间值。
当收到采样触发时，锁存触发时刻计数值REQSTAMP上报，
用该触发的采样开始时刻（adc_start 的上升沿）计数器值减去
REQSTAMP，将得到的差值DLYSTAMP锁存上报。
当由于pO优先级抢占发生时，低优先级会在第二次采样开始
时更新DLYSTAMP值；


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图 5-19 Trigger-to-sample时序示意`，完整结构与时序请查看原图 `GameViewer_mjeYzTB3j7.png`。

> 📌 **【图表提示】**: 此处包含图表 `图5-19采样结果校准`，完整结构与时序请查看原图 `GameViewer_mjeYzTB3j7.png`。

过采样启用时，该延时捕获仅在过采样的第一次开始时锁存
延迟值；
REOSTAMP
ETMCU hian.1
SPLSTAMP
adc_trig
adc_start
DLYSTAMP
free-run
counter

**图 5-19 Trigger-to-sample时序示意**

采样结果校准补偿
每个ADC采样结果统一校准补偿，不区分虚拟通道。（模拟
ADC 偏置 s(5,0)和增益 u(14,12))。
ADC校准参数处理

#### 1.0%

signed
u(2,0)
(14,12)
(16,2)
2d_data,out
cal_data_out
ETNCV huan:1i 2026-10-02-21;43

**图5-19采样结果校准**

2080F



---
## 图像编号 21 (原图: `GameViewer_NaDPGTeO6W.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-20超门限检测原理`，完整结构与时序请查看原图 `GameViewer_NaDPGTeO6W.png`。

> 📌 **【图表提示】**: 此处包含图表 `图5-20超门限检测结果输出形式`，完整结构与时序请查看原图 `GameViewer_NaDPGTeO6W.png`。

6002：上下门限检测输出使用CBC或者ONESHOT两种模式
（软件配置选择）。CBC模式下，a根据每个新的采样结果是否
超门限控制是否输出告警；ONESHOT模式下，一旦产生了超
门限告警，需要软件进行清除。每个超门限检测通道输出1bit
事件，上下门限告警通过mux-or的方式输出。同时单独上报超
上下门限的实时状态。
nl1202
limit.hi
ETMO
edcevtsts.triphi
clear
adc_result
ETMCU haan. J3
>EVT
limit.lo
dcevtsts.triplo
evtsel.lo
clear.hi
clear.lo
CBC clearlogic

**图5-20超门限检测原理**

ETMCV321a7. 1 7026-10-02-21: 4
ETMCI
sample2
sample2
超门限
超门阀
不超门限
ONSHOT
ETMCV han 1 2026-10-02-

**图5-20超门限检测结果输出形式**

ETMCIT


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-20FIR滤波`，完整结构与时序请查看原图 `GameViewer_NaDPGTeO6W.png`。

滤波通道
an.1i
滤波处理模块的数据输入为校准补偿后的采样结果。
此处区别：6001是用户预处理补偿后结果，6002是校准补偿
后结果。
滤波类型：FIR、IIR、滑动平均（归入FIR，由软件配置系
数)、非滑动平均。
FIR滤波阶数要任意可配置，最高32阶。并且根据配置阶数
对滤波结果实时输出。
TNCl1
滤波处理
s(16,2) signed
al_data_ou
fiter_dats_out

**图5-20FIR滤波**

ETMCII
ETNCI/ ;44
2080F



---
## 图像编号 22 (原图: `GameViewer_NaOtfAzWwn.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-8单次触发模式时序示意`，完整结构与时序请查看原图 `GameViewer_NaOtfAzWwn.png`。

VC_EN
CONFIG
BTMCU han.Ti
BTMGU hoan.Ji
TRIG
ONE_SHOT_EN
VEFUAG
SARC_START

**图5-8单次触发模式时序示意**

BTMCU han.J3
连续触发模式
连续触发模式：虚拟通道配置完成且使能打开后，可以重复
生效等待触发事件来临，直至软件配置虚拟通道使能关闭。
在连续触发模式下，只要VCEN有效，在检测到该虚拟通
道的触发TRIG时，就将该VC_FLAG置1。1:4
待该虚拟通道获得优先级后，开始启动转换操作。
ETMCU huar.
ETMCU hian.li


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-9连续触发模式时序示意`，完整结构与时序请查看原图 `GameViewer_NaOtfAzWwn.png`。

VC_EN
CONFIG
TRIG
VC_FLAG
START

**图5-9连续触发模式时序示意**


#### 5.6 blanking机制

BTNCU ) 49
每个SARADC控制器中包含，Blanking管理模块，支持一个
Blanking事件，可以对非VCo的采样触发信号进行延迟Blank-
ing操作，该功能可屏蔽。仅虚拟通道0支持Blanking管理。实
现VCO的周期性等间隔采样功能。
Blanking支持2类触发源：eTimer/SuperPWM。
blanking 的触发延迟时间可配置，且对所有blanking 触发源
统一配置，为16bit，SYSCLK计数器。
对所有blanking触发源，blanking窗口长度相同且可配置，
为 16bit，SYSCLK计数器。
2026-10-02-21;43
1080F



---
## 图像编号 23 (原图: `GameViewer_NwJydpcqGX.png`)

### 【左页】

ADC同步并联模式下，ADCCORE的采样保持时间、触发模
式（单次或连续）需要保持一致。
ETMO
BTMGU hoan.
同步采样
ADCCLK
ADCO.START
8TICUh87.137026-10-02-21: 43
ADCO.SPLTIME_EN
8TMCU hpan. Ji
ADCO.SH
ADCO.CONVERSION
ADCO,VC_CH
ADCO.READY
ADC1.START
ADC1.SPLTIME_EN
ADC1.SH
ADC1.CONVERSION
AOC1VC_CH
chantel m
ADC1.READY
同步采样：多个CORE同时采样不同信号源
KTMOI) pian.i 2026-10
ETMCU man. 1i


### 【右页】

穴余采样
EMou
ADCO.START
ADC0.SPLTME_EN
ADCO.SH
an112026-10-02-2)49
ADCO.CONVERSION
ADCO.VC_CH
channeln
ADCO.READY
ADC1.START
ADC1.SPLTIME_EN
ADC1.SH
ADC1.CONVERSION
ADC1VC_CH
channeln
ADC1.READY
几余采样：多个CORE同时采样相同信号源
2026-10-02-21;43
ETMcy huan
12080F



---
## 图像编号 24 (原图: `GameViewer_O2LOSI5xZO.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-5校正控制说明`，完整结构与时序请查看原图 `GameViewer_O2LOSI5xZO.png`。

SOC
SARC
ANALOG
i PD=0 & ADC_EN_R=0
BTMCU hian. i
: adc_cal_flag=1
BTMCU haan.Ji
iADC_EN=1
：配适转换参数
.cal_conversion_start=1
16次校正序列转换
转换结果返回
16次平均
BTMCV m2an,J3
BTMCU huan.J3
cal_aver_val=1
重复参数配适到结果返回过程
计算offset&gaincoeff
analog_os/gain_coeff
: adc_cal_flag=0
ETMCU han. li
SOC
SARC
ANALOG

**图5-5校正控制说明**

BTMCU huam.11
BTMCV hran 1i
ETMCU mian. 1i


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-6校正状态机`，完整结构与时序请查看原图 `GameViewer_O2LOSI5xZO.png`。

PTMCUhuarn.11
CAL_IDLE
adc_en_r==0 &&
adc_cal_flag==1
CAL_START
B7NC/ huar. 1 2026-10-02-2) 49
cal_conv_start==1
adc_en_r==1 II
adc_cal_flag==0
CAL_CONV
adc_en_r==0 &&
adc_cal_flag==1
电话：12-80-01-9208
cal_conv_done==1
BTNCU huan. Ji 2026-10-02-21:
CAL_AVER

**图5-6校正状态机**

注意：此处需要补充DAC校正需求和流程，以及ADC 需要
配合的工作。
12080F



---
## 图像编号 25 (原图: `GameViewer_PecSuT1xBB.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-x输入数据增益调整`，完整结构与时序请查看原图 `GameViewer_PecSuT1xBB.png`。

(pre_datsa_in[15: 0], 3 d0)
((1 (pre_data_in[15]], pre_data_in[15: 0],2 d0]
f1t_at_in[15:0]
([2 (rre_data_in[15]]], pre_data_in [15: 0], 1’ d0)-
((3 (pre_dats_in[15]]), pre_data_in[15:0])
ETHCU hans. Ji
cfe_pf1t_idst_eain_adj[1:0]
图5-x输入数据增益调整

#### 5.14.3.3滤波器的输入数据和运算结果缓存

BTMOU huan.J
1、当滤波器通道配置为fir滤波器时，滤波器的输入数据需
要根据阶数进行缓存，待后面的滤波运算使用。当滤波器的
flt_dat_vld==1时，将所有的输入数据（包含最近的cfg_p_arg个
输入数据）向后移动一个寄存器，最旧的数据不再需要，所以
被丢弃。
2、当滤波器通道配置为iir滤波器时，滤波器的输入数据和
输出结果都需要根据阶数进行缓存，前cfg_p_arg个寄存器缓存
最新的 cfg_p_arg 个输入数据。后 cfg_q_arg 个寄存器缓存
cfg_q_arg个最新的输出结果，c用于反馈支路的运算，最旧的数
据不再需要，所以被丢弃。


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-x输入数据和运算结果的缓存`，完整结构与时序请查看原图 `GameViewer_PecSuT1xBB.png`。

3、当配置cfg_pflt buf clr==1(软件写清信号)时，输入数据
和运算结果缓存可以被清除；当加载新的滤波器参数时，可以
通过配置cfg_pflt_rdy_buf_clr_sel寄存器来选择是否需要清除输
入数据和运算结果缓存。
(*:1U
_ d g~ [[15.0]
BTKCUbuan.3 2026-10-02-21 48
[.[015.0]
ETNCU hian.1i 2026-10-02-21:
图5-x输入数据和运算结果的缓存

#### 5.14.3.4滤波器运算的数据流图

Cu
1、滤波器的本质为乘加运算，在实现过程中用内部计数器
来控制输入数据和滤波器系数的乘加，乘法起的位宽为
1080F



---
## 图像编号 26 (原图: `GameViewer_Pv1TFSu3Dw.png`)

### 【左页】


#### 5.9软件直接触发采样

在SARADC控制器使能打开的前提下，无论虚拟通道是否配
置了相应的触发源，且无论相应的触发源是否产生，软件通过
对相应寄存器置位，可以触发启动对应虚拟通道进行采样转换。
软件向置位寄存器 ADC VC Force Register(ADC_VC_FRC)写 1
来实现，该寄存器硬件自清零。
该寄存器有16个有效bit位，分别对应16个虚拟通道，指示
对应虚拟通道通过软件启动转换开始标志。该寄存器相应bit位
写1会强制将ADCVCFLG寄存器的对应位置1，用于软件控
制启动转换。该位写0无效，该位软件读操作返回0。
在同一时钟cycle，如果软件set此位，同时硬件clear
ADC_VCFLG寄存器的对应位，则软件set的优先级高，即
ADC_VC_FLG寄存器对应位响应软件set，此时ADC_VC_OVF
寄存器（虚拟通道启动转换溢出标志）的对应bit位不受影响。
例如软件配置ADCVCFRC寄存器为OxO0OF，在SARAD
控制器使能打开的前提下，则ADC_VCFLG寄存器中VCO、
2026-10~02-21:43


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-19软件直接触发采样`，完整结构与时序请查看原图 `GameViewer_Pv1TFSu3Dw.png`。

VC1、VC2、VC3对应位置1,°即该4个虚拟通道被软件强制触
发，然后根据对应优先级进行排队转换。
ADC_VC_FLG
FTH
ADC_VC_FRC
ADC_VC_FRC

**图5-19软件直接触发采样**

还支持另一软件触发，软件通过配置
an.112026-10-02-2149
CFG_SARC_VC_SOFT_TRIGER.cfg_sarc_vc_soft_trigger[15:0],该触发脉
冲在触发选择列表上，触发功能需经过触发选择，与其它硬件触发源的
功能类似；

#### 5.10SARADC控制时序

转换控制模块，根据时序和队列状态，向队列管理模块申请
转换出队，然后根据出队虚拟通道号及相应的转换配置参数，1:
产生相应的数模接口信号输出到模拟ADC控制采样转换。-1
ETMOy huar.
ETNOU huan.
2026-10-02-21;43
080F



---
## 图像编号 27 (原图: `GameViewer_pVe1evLu6f.png`)

### 【左页】

预处理过采求和通道
ETMCU hrian.
E7NCU hvan, 1 2026-10-02-21: 44
. Ji
1ntr/dma处理
re_f lag_e tr1
(ptc_cho"T)
-10-02-21;44
vs_f.sg[15 ;0]
prioritr_d1t
ETNO
BTMOy
. J3
ve_4ue ue
sare_sample_ctrl
携报ADC
过采控制侧：
增加8套采样间隔、过采样次数配置，作用于ovsctrl0~7；
过采样通道连接在预处理滤波通道后，与虚拟通道的映射关系同预处
理通道滤波一致；
若虚拟通道映射到过采样通道，则vc_flag_ctrl的ovs_ctrl增加flag的
自动拉起机制，未达到过采次数时自动按间隔设置拉高对应的vc_flag;
*该虚拟通道的触发信号来临时完成影子加载，生效软件的配置；
uan
*，无论是否开启抢占功能，过采过程中如果出现其它高优先级的虚拟通
道请求priority_cflt，或blanking窗口，进行resume、conti恢复；


### 【右页】

*若过采期间来临新触发，硬件上忽略该触发，但告警，软件可清除该
告警；
求和侧：
ETNCU huan.Ti
*对预处理滤波输出进行按过采次数进行求和功能；
*优先级冲突的处理，resume的恢复模式下，需清零求和结果；
其它：
加法器单元可复用滤波逻辑中的扩展36bit加法器；
*过采求和结果完成后可输出中断/dma请求；
*该功能需有使能控制；

#### 5.16采样结果超门限检测

超门限检测的对象为用户预处理补偿后的采样结果。
检测包括超上门限和超下门限检测，每个用户预处理通道的
采样结果独立配置上下门限值、2独立检测、独立输出检测结果。
此处修改:
6001：对检测结果进行滤波处理，且超上下门限单独输出告
警。
080F



---
## 图像编号 28 (原图: `GameViewer_QZWwXnmnv1.png`)

### 【左页】

2、d2aadc_gainatt设置为1，配置ADC增益衰减为(1-32/4096)。
3、ADC转换16次，对16个转换结果做累加平均，得到无符号数code_refp
值。
4、d2a_adc_cal_se_refp_inj/d2a_adc_caldf_refn_inj设置为0，关掉注入
5、d2a_adc_cal_se_refn_inj设置为1，配置ADC单端侧输入vrefn。
d2a_adccal_dfrefp_inj设置为1，配置ADC差分端侧输入vrefp。
BTMGU hvans.J3
6、ADC转换16次，对16个转换结果做累加平均，得到无符号数code_refn
值。
7、计算得到offset/gain值d2soc_adc_gain_value/d2soc_adc_os_value
其中 gain=code_refp-code_refn; offset=(code_refp+code_refin)/2-2048。
8、d2a_adc_gainatt设置为0，关掉ADC增益衰减。
9、d2aadccalserefninj/d2aadc_caldfrefpinj设置为0，关掉注入。
注:
1第6步累加平均芯片内用asic实现，第7步计算offset/gain值用软件
实现。
2整体流程重复两次，第一次根据校正得到的ofset补偿值，用模拟补
偿的方式进行补偿。第二次根据校正得到的offset/gain补偿值，用数字
补偿的方式进行补偿。
补偿，模拟/数字实现，软件控制。
对数字需求：
1、数字实现加法器/乘法器，根据软件配置的offset_coeff/gainLcoeff系数，对ADC输
出进行以下补偿，输出补偿后结果。
2、加法器/乘法器可以bypass，原始ADC输出码字直接送出来。
3、d2a_adc_gain_att模拟配置值可以软件控制。
4、d2a_adc_os_se_tune<3:0>、d2a_adc_os_df_tune<3:0>模拟补偿值可以软件配置。
2026-10~02-21


### 【右页】

每个ADC均提供校准功能，包含模拟校正和数字校正，支
持单端输入转换与差分输入转换校正。本版ADC支持os/gain
的前台校正。在校准过程中，应用不得使用ADC，必须等待
至校准完成。
ADC校准的软件流程如下：
1. 确保 ADC_CTL1 寄存器中 ade pwdn=0、adc_en=0。
2．设置adc_cal_ch_mode=0（单端输入）或
adc_cal_chmode=1（差分输入），选择此校准的输入模式。
-13．将 adc_cal_flag 置 1 （软件置 1)。
4．软件配置cfg_sarc_adc_cal_conv_start 启动校正转换，硬
件上报转换结果的平均值。
5．校正完成后，将adc_calflag置0（软件置0）。
此处的16次转换由硬件配置启动。
ETHC/
2026-10-02-21;43
1080F



---
## 图像编号 29 (原图: `GameViewer_SeEx4da40l.png`)

### 【左页】

16bit*16bit,0中间累加器的位宽为27bit~中间累加器溢出时可
以选择wrap或者 saturate（通过寄存器cfg_pflt_clip选择），同
时会上报溢出状态到上预处理滤波器通道的上报寄存器；
2、滤波器的运算结果可以通过cfg_pflt_r_arg寄存器进行缩
放，缩放之后的结果可以通过cfg_pflt_acc_out_wrap_sel寄存器
进行saturate或者wrap到16bit数据输出；
3、在实现时，数据流图中乘法器、加法器、累加结果寄存
器等资源将与用户预处理补偿模块复用；
ETHCU h1an. 73
ETMC 7uan, 11
ETMCI/
ETMCI) 2 2026-10-02-21;44
8TMCVmian.11
ETMCII muan. 11


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-x滤波器运算的数据流图`，完整结构与时序请查看原图 `GameViewer_SeEx4da40l.png`。

：10-20-01-9208
rlt dali
ETNCU hian.Ti
9.[3:0]
.et [3.0
(nt mt.nrcant/ni. t8)
(26.22)
IL,ot,a[rtM[i:e]
buan.Ti 2026-10-02-21-44
-(26.28
(t of[n t, ixJ[5.0]
ns (2)
(3 2
( [2]a[22]]
(26. (3)
I3r_],at_0,[25] ], nL os1,dal. ua[25.3]
an.li 2028-10-02-21
Tp (i.oal 4u,[]],n _al sa. ue[2-]
16 B)
TMCIT
efxpU es[2.0]
图5-x滤波器运算的数据流图
FTNOU
13080F



---
## 图像编号 30 (原图: `GameViewer_sKXvcDs2Yn.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-15采样转换控制状态机示意`，完整结构与时序请查看原图 `GameViewer_sKXvcDs2Yn.png`。

SAMPLE_IDLE
do nothing
t=beg"ouou C
8TMCu
(none_fagi=0
. Ji
SAMPLE_PRE
empty jump
ad_cnt>=adc_sptime+13 &
T--feeuou
ad_ont>sadc_spltime+13 &&
SAMPLE_START
Onmbey"ouou
[begin sample
vc_num_vals=1
8TMCU huan.J3
SAMPLE_CONTI
BTMCU hoan. Ji
keep sample

**图5-15采样转换控制状态机示意**

BTNCV TR1a 11 2026-10-02-21
ETMOU Thuan. T1 026-10-02-21:43
TMCU huar 1i 2026-10~02-21:43


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-16触发采样时序图`，完整结构与时序请查看原图 `GameViewer_sKXvcDs2Yn.png`。

cik_sare |U.U 1
_ng
ve_fag
gons_ag
vc_num_reg
vc_num_al
vc_oum
Xvc_rum
ETNCU huan J1 2026-10-02-2) 48
s_num
X,num
ad_stat
aoc_start,1d
adc_starl_2d
p05_v_num
vc_num
ve_num
a8c_ont
XHXHXHXHXHXX

**图5-16触发采样时序图**

ETMOU huar.Z)
ETNOV ;43
2026-10-02-21;43
12080F



---
## 图像编号 31 (原图: `GameViewer_u5JeUrg4ga.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-20中断处理`，完整结构与时序请查看原图 `GameViewer_u5JeUrg4ga.png`。

口1组求和结果寄存器锁存有效采样结果中断（基于求和通道
8bit)
当中断产生时，上一中断还未响应（中断未被清除），可此时
产生中断溢出告警指示。
中断处理按下面的方式统一处理：
激始中新高存器‘int,raw_pt
中断状志存器 _int_status_rpt
BTMCU Tuan.J4 202
BINCU
ETMCIhuan.Ji
cfg.*jint,en
中新使报信号
(电子)
中国批发信号
中新缩出”3nt
中新测试高门司
ran,11 2026-10
RTMCU.huan. 7 2026-10-02-2
TNCI
中新苏服信号
ETMCI Tan. 1i
中新处理模块

**图5-20中断处理**


#### 5.21.DMA数据请求

hian.12 0026-20-02-21:44
6002修改点（DMA请求源）：
BTMCU hian.1i


### 【右页】

每个ADC支持4个DMA请求通道，每个DMA请求通道可
从如下DMA请求源中独立配置选择（sarc只选择DMA请求源
输出，DMA握手功能在DMAMUX模块中实现）：
●EOC脉冲信号（基于虚拟通道，16bit）
·2组结果寄存器锁存有效采样结果（基于虚拟通道，16*2）
·电平超门限检测结果事件（基于虚拟通道*16bit）
1组求和结果寄存器锁存有效采样结果（基于求和通道，
8bit)
在通过fifo读取采样结果模式下，通过fifo的非空信号进行
DMA请求，两个fifo的非空信号可独立选择到4个dma请求通
道，默认配置下不选择fifo的DMA请求。
6801增加将16个虚拟通道的电平超门限检测结果事件或结
果作为新增的dma请求事件。

#### 5.22数据同步到 CPU_WRAP

U huan: li
为了使得cpu 能够快速获取adc采样结果，减少总线延迟，
将adc采样结果同步到 cpu_wrap中。6601修改成两组，



---
## 图像编号 32 (原图: `GameViewer_UFTfaW6Wm8.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-20用户预处理补偿`，完整结构与时序请查看原图 `GameViewer_UFTfaW6Wm8.png`。


#### 5.13用户预处理补偿

. Ji
用户预处理补偿有16个通道，与虚拟通道一一对应。（用户
配置偏置s(16,2)和增益 s(15,12))。
6002相对于6001修改点：pre_gain参数格式由u(14,12)修改
为 s(15,12)。
用户配置参数处理
(16,2)]
(16,2)
cal_dsta_ou
pre_dsta_out

**图5-20用户预处理补偿**

ETMCV hvan, 11 2026-10-02-21;43

#### 5.14预处理滤波通道

每个SARC包含有8个通道的预处理滤波通道，可以通过配
置寄存器将16个预处理通道映射到这8个预处理滤波通道（映
射方式与6002中滤波器通道的映射方式类似）。每个预处理滤
波通道可以配置为1~4阶的ir滤波（直接1型）或者1~8阶的
fir滤波器。


### 【右页】


#### 5.14.1 FIR滤波器

Y-B*X
y,=2R×Z-0bkXn-k
(5-2)
该功能执行长度为N+1的向量 B与不定长度的向量X的卷
积。Y中每次增加的元素yn都是用点积来计算的：y,=B*Xn，其
中Xn=n-N，"Xn由N+1个X中的元素组成。
该功能对应于有限脉冲响应（FIR）滤波器，其中向量B包含
滤波器系数，向量X包含输入数据，R为滤波器输出的缩放因
子。
FIR滤波器的结构如下图所示。
KTNOU hian. 1
ETKCV ;43
2026-10-02-21;43
2080F



---
## 图像编号 33 (原图: `GameViewer_UUhaiE4moy.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-4SARADC校正整`，完整结构与时序请查看原图 `GameViewer_UUhaiE4moy.png`。

ADCCLK：模拟core的工作时钟，通过SYSCLK时钟分频，
最高66MHz。
中，每个ADC core的时钟ADCCLK相同，不支持独立分频。

#### 5.3 SARADC CALC

02F-10-02-21:48
整体的框图，软件配合模拟/数字完成offset/gain的检测+补偿。
棋报数字
款件
ADC

**图5-4SARADC校正整**

体框图
其中数字部分，滤波器累加平均实现检测，运算后得到
offset/gain的值。
检测:
RTIO) huan.
ETMCU hian.
滤波平均


### 【右页】

输入vrefp
code_refp= (Z16a2d_data_out )→16
输入vrefn
code_refn = (Z16a2d_data_out )→ 16
运算得到offset/gain
d2soc_adc_gain_value= code_refp-code refn
11 2026-10-02-2) 49
d2soc_adc_os_value=(code_refp+code_refn)/2-2048
校正流程如下：
运算，数字实现
单端模式运算流程：
1、d2aadc_calserefpinj设置为1，配置ADC单端侧输入vrefp。
2、d2a_adc_gain_att设置为1，配置ADC增益衰减为(1-32/4096)。
1、ADC转换16次，对16个转换结果做累加平均，得到无符号数code_refp
值。
4、d2a_adc_calse_refp_inj设置为0，关掉vrefp的注入。
5、d2aadc_calse_refninj设置为1，配置ADC单端侧输入vrefn。
6、ADC转换16次，对16个转换结果做累加平均，得到无符号数code_refn
值。
7、计算得到offset/gain值d2soc_adc_gain_value/d2soc_adc_os_value
其中 gain=code refp-code refn;offset=(code_refp+code_refn)/2-2048。
8、d2a_adc_gain_att设置为0，关掉ADC增益衰减。
9、d2a_adc_cal_se_refn_inj设置为0，关掉vrefn的注入。
ETC// huar. 11
差分模式运算流程：
1、d2a_adc_cal_se_refp_inj设置为1，配置ADC单端侧输入vrefp。
d2a_adc_cal_dfrefninj设置为1，配置ADC差分端侧输入vrefn。
2080F



---
## 图像编号 34 (原图: `GameViewer_v6tUVs7H0k.png`)

### 【左页】

FIR滤波器输入采样结果PIPELINE

#### 5.10缓存通道

DMA数据请求
BTMCU huans. Ji

#### 5.12乘法器复用


#### 5.13状态告警处理

CORE和 VC状态
触发超时告警
ETNCU hoan 71
6. 约束
BTMCU huan. J3
7.遗留问题
8.可优化点

#### 8.1乘法器复用

9. 参考文献
BTMCV
ETHCU
0026-70~02-21:42


### 【右页】

图目录
ETMCU Tuan. J1 2026-10-92-21:42
1. 模块 OR DR 需求
SARC（SARADCController）模块，以《OR DR》《SARC
模块LRS设计文档》为需求依据，在本文档中进行方案设计。
表1
SARC模块设计需求
SARADC
ORE量
更持2个ADC控制用
DRSARADC.002
豆持等一个ADC.COR[的增益0需量收正
DR SARADC.003
DRSARAOC004
DRSARACC.005
ADCCLK分糖
每个ADC腔制器变除16个也
DR, SARADC. 006
更将ADCCK系分需，分盗系数更持件可配量
DR,SARADC_007
banking
亚号个ADC控晶aoblasking能
ETMCU uan. J1 2026-10-00-21:
DR_SARADC_008
DR SARADC 009
更持每个感拟速测时处理因的激据进行上下门限为断，超门
DR,SARACC,010
上下门限比载
变球2个ADC控制(器
或系数不少于1位
联采用1-40
DR_SARADC_011
DRSARAOC.013
DR SARADC 014
更将ADC减的国步需样
DR SARADC 01S
SARADCAUSADCCORE.
ARAOC.016
DRSARAOC017
更持ATETSARADC进疗控率：检准争暂事入OTP
SARADC更拍时系用维E服FIFO提式通行DMAR聘
DR_SARADC_018
变的通过快速度口期SARC需群验服高存器管份到N7WRAP
12080F



---
## 图像编号 35 (原图: `GameViewer_vZO2NlUXdv.png`)

### 【左页】


#### 5.14.3预处理滤波通道的实现结构


#### 5.14.3.1滤波器通道的参数配置

. J
1、fir和iir的实现复用同一种结构，通过配置参数
cfg_pflt_type来区分滤波器的类型（O:fir；l：iir);
2、通过参数cfg_p_arg和参数cfg_q_arg来区分滤波器器的阶
数；cfg_p_arg为滤波器前馈系数的个数，等于fir的阶数+1;
cfg_q_arg为滤波器反馈系数的个数，等于ir 的阶数，当滤波器
配置为fir时，"cfg_q_arg应该等于O;
3、cfg_pflt_coeff[x)（x=0~8）为滤波器的系数，16bit有符号
数，前面部分为前馈系数后面部分为反馈系数，，配合
cfg_p_arg 和 cfg_q_arg 使用;
4、cfg_pfltp_num为滤波器的通道编号，当通道编号与滤波
器的通道对应时，并且cfg_pflt_rdy=元l(滤波器参数在影子寄存
器种准备好时)，同时flt_cal_en==0（该通道的滤波器没有在运
算时），可将影子寄存器中的参数刷新到对应滤波通道的活动寄


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-x滤波器通道参数配置`，完整结构与时序请查看原图 `GameViewer_vZO2NlUXdv.png`。

存器。待滤波通道的参数切换完成后，内部硬件自动清除
cfg_pflt_rdy寄存器。
当cfg_pflt_rdy==1&&
(flt_cal_en==0),
并且cfg_pflt_num等于预处
理滤波器通道的编号时，ids
dlg,p_coew[0]
中滤波器的系数等参数会加
dg,pt,coef[1]
fn,coeffp)
载到预处理滤波器的内部寄
存器，实现滤波器参数切换
fit,coeffm]
[u]gs0 gd 6p
cfg.pt.p.arg
ftcoeffa]
cfg.pt._q.arg
p_arg
clg.ptt_num
q_arg
fitype
cfg.ptt_type
BTNCU buan.T1
cfg pft rdy
滤波器参数切换完成后，
硬件会自动拉低ids的
cfg_pflt_rdy
图5-x滤波器通道参数配置

#### 5.14.3.2滤波器的输入数据增益调整

ETNCU hian.1i 2028-10-02-21:
为了适用不同的场景，需要对预处理滤波通道的输入数据进
行缩放（通过左移或者右移实现），缩放的范围为：-1～2（负数
表示左移，正数表示右移）。如下图所示。
ETNCU huan.
dan
2026-10-02-21;43
080F



---
## 图像编号 36 (原图: `GameViewer_Wwj0z78cha.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-1SARC模块与总线和ADCCORE的连接关系`，完整结构与时序请查看原图 `GameViewer_Wwj0z78cha.png`。

5.方案设计
8TMChuan.Ji/

#### 5.1 SARC 整体结构

BTMCUhuan.Ji
SARC连接关系
共有2个ADC CORE，每个ADC CORE对应1个控制器
SARC，每个SARC占用一条AHB总线。结构如下：
AHB_BRG
DaHY
adc ctrl o
adc ctrl 1
adeetrl2
adc core0
adccore1
adc.core.2
ETICU huan.71

**图5-1SARC模块与总线和ADCCORE的连接关系**

SARC设计框图
SARC模块整体框图如下：
ETHCU
BTMCUTuan.1i


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图5-2SARC模块结构框图`，完整结构与时序请查看原图 `GameViewer_Wwj0z78cha.png`。

络环境，以改善远程控制体验。
本次远程不再提醒
知道了
2026-10~02-21:43

**图5-2SARC模块结构框图**

capture_posedge：外部触发源的上升沿捕获处理。128个外
部采样触发源和64个blanking触发源经过上升沿捕获处理后，
每个SARC控制器单独处理。
trig mask：根据配置 vc_en、vc_trig_sel和vc_trig_mode 来屏
蔽无效的采样触发，输出16个bit的脉冲数据，代表16个VC
的采样触发状态。同时该模块根据blanking机制的配置，从
blanking 的触发源中选择输出 blanking的有效触发信号blank-
ing_trig.
blanking：实现 blanking 管理功能。触发经过该模块时，如
果blanking_en不使能，则直接输出原触发；如果blanking_en使
1080F



---
## 图像编号 37 (原图: `GameViewer_XEDw3yfNAf.png`)

### 【左页】

控制 ADG 差分侧输入 vrein
sare _d2a_ade_cal_ df refn_ inj
输出
ADC测试模式选择。
sarc_d2a_adc_test_sel
0：测试模式关闭
输出
1：测试模式打开，ADC测试模式包括（ADC测
EIMCU huan. Ji
量模拟内部其他待观测节点电压，DAC校正时需
要ADC对其输出信号检测等）
输出
ADCibias电流调节
sarc_d2a_adc_ibias_sel[1:0]
sarc_d2a_adc_ref_mode
SARADCO参考电压模式选择
1“b0：参考电压为VREFHI（3.3V或2.5V），
输出
ADC输出摆幅为3.3V或2.5V
1’b1：参考电压为1.65V，ADC输出摆幅为

#### 3.3V.

sarc_d2a_adc_ready_sel
SARADCOready时序选择信号，
BTMCU huan.J3
输出
1“bo：ready时序模拟顶层对齐模式；
1’b1：ready时序模拟底层对齐模式；
ATE接口
输出
sarc_ate_data_val
sarc_atedata_out[11:0]的val有效信号
采样结果经过校正后输出，ATE测试数据，
sarc_ate_data_out[11:0]
u(12,0)范围0~4095
触发源接口
输入
sarc_trig_in<127:0>
128个触发源输入
ETHCU
输入
64个blanking窗口的触发源输入
sarc_blk _trig_in<63:0>
中断信号接口
输出
sarc intr
中断输出
sarc_eoco_intr
输出
完成数据转换中断0输出
sarc_eoc1_intr
输出
完成数据转换中断1输出
sarc_eoc2_intr
输出
完成数据转换中断2输出
输出
sarc_eoc3_intr
完成数据转换中断3输出
ADC采样触发源输出（来自EOC）
输出
sarc输出的2bit采样触发源信号。从16个虚拟通
sarc_eoc2spl_trig<1:0>
ETHCU
道的EOC中独立配置选择2bit。
FIMCU
看门接口
输出
sarc2etim_evt_out<3:0>
4bitADC上下门限检测事件输出到ETIM模块，
从16个虚拟通道中独立配置选择


### 【右页】

输出
sarc2xbar_evt_out<3:0>
4bitADC上下门限检测事件输出到XBAR模块，
从16个虚拟通道中独立配置选择
DMA握手接口
输出
sarc_dma_req[3:0]
burst transfer request source
输出到dma_mux模块进行DMA握手处理
输出
sarc_dma_single[3:0]
Single transfer request source
输出到dma_mux模块进行DMA握手处理
输出
sarc_adcevt_dma_req
超狗上下门限dma请求输出
sarc_adcevt_dma_single
输出
超狗上下门限dma请求输出
输入
sarc_dma_ack[3:0]
dmac acknowledge signal
DMA应答信号，sarc模块内部不用
wdt_dma_src是否打拍
0:不打拍；（6003固定接0)
输入
1:打1拍；(3101/6002C)
6601项目先固结0进行时序收敛，若不行在切换
到固结1上。
SRAM CTRLBUS
sysc_sare_1rw_ctrl bus[63:0]
输入
firfilter data sram ctrl bus
输入
sysc_sarc_1rlw_ctrl_bus[63:0]
firfilterparametersramctrlbus
IESTPIN
sarc_testpinO_sel[7:0]
输入
sarc testpino的选择信号
sarc_testpin1_sel[7:0]
输入
sarctestpin1的选择信号
输入
sarc_testpin2_sel[7:0]
sarctestpin2的选择信号
输入
sarc_testpin3_sel[7:0]
sarc_testpin3的选择信号
sarc_testpin[3:0]
输出
sarc testpin测试信号输出
输出到CPU内部寄存器
输出
sarc输出有效数据指示，sarc时钟域下的单周期
sare2cpu_data_vld
脉冲
输出
sarc2cpu_data[15:0]
sarc输出数据
sarc2cpu_vc_num[3:0]
输出
sarc输出数据所属虚拟通道指示
FIMCU
fps
12080F



---
## 图像编号 38 (原图: `GameViewer_YbkCdqx6qz.png`)

### 【左页】

adcreg_receive 需根据时钟方案调整交互方式，所有逻辑在
下;
sare (20000
.Ji
sarel. ad:_resu2t
8001r-2001clmn
ssrc0. sars_result
sarc_sdcresult_receive
ids result reg!
dsresult rego
mun(3 :0)
ETMCIIhuan.Ji
6.约束
KTIC参考《SARC模块LRS设计文档》中2.4节-约束说明。
ETMCH Tman.li
7.遗留问题
8.参考文献
BTMCh1an.1i 0026-20-02-21:44
ETMCUhian.li
文栏结尾
第79屏(共79屏)


### 【右页】

ZTNCU
KTMCIT 5
ETNCV muan.Ji 2026-10-02-21-44
ETNCU T22an.JI
ETMC/ huan.Ti
FTNCU
12080F



---
## 图像编号 39 (原图: `GameViewer_ZQLidR9zmC.png`)

### 【左页】

4.接口说明

#### 4.1SARADC接口信号

BTMCU huan.Ji
信号
输入
说明
输出
时钟复位
输入
SARC输入ADC时钟，与clksarc同步
adc_rst_n
输入
clk_adc复位信号，低电平有效
AHB3.0总线
输入
总线时钟
sarc_hclk
BTMCU huan.Ji
输入
sarc_hresetn
总线复位信号，低有效
输入
sare_haddr[11:0]
12-bit系统地址总线，超出寄存器空间的高位地
址不能使用。
sarc_hburst[2:0]
Burst类型，支持固定长度的4、8和16拍
输入
sarc_ hprot[3:0]
保护控制信号
输入
sarc_ hsize[2:0]
传输数据位宽指示，32bit时应为3"b010。
输入
sarc_htrans[1:0]
当前传输类型，IDLE，BUSY，NONSEQ，SEQ
输入
sarc_hwdata[31:0]
写数据总线
sarc_hwrite
输入
高表示写传输，低表示读传输。
输出
sarc_hrdata[31:0]
读数据总线。
输入
总线输出给IP的hready_in信号，用于防止总线对
sarc_ hready
IP的背靠背访问。
高：传输在总线上结束。
sarc_hreadyout
输出
低：延长传输周期。
传输响应，向Master提供传输状态信息。
ETHCU
OKAY：传输完成；
sarc_hresp
输出
EIMCU
ERROR：传输错误；
输入
sarc hsel
slave选择信号
ADCCORE接口


### 【右页】

转换控制
sarc_d2a_adc_en
输出
SARADC使能信号
SARADC启动转换信号，ADC时钟域下的脉冲
sarc_d2a_adc_start
输出
信号
输出
SARADC增加采样时长功能控制信号
输出
sarc_d2a_ade_trig_mode
SARADC触发模式选择信号（为常值1，仅支持
单次触发模式）
sarc d2a adc mux se<4:0>
输出
SARADC单端通道选择信号
输出
sare_d2a_ade_mux_df<3:0>
SARADC差分通道选择信号，mux_se为差分P
端，mux-d为差分N端
sarc_a2d_adc_data<11:0>
输入
SARADC输出数据信号，12bit无符号数
sarc_a2d_adc_ready
输入
SARADC输出数据生效信号
输出
sarc_a2d_outrd_hold
输出5拍的窗口信息，模拟保证ready&data时序
不受抢占控制拉低sarcd2aadc_en的控制；
校正控制
输出
默认为0，默认ADC增益为1；
sarc_d2a_adc_gain_att
使能校正时置为1，ADC增益为(1-32/4096)。
SARADCO内部共模选择
3'b000:1.80V;
3'b001: 1.65V
3'b010:1.70V;
d2a_saradc_cmp_com_sel<2:0>
输出
3'b011: 1.75V;
3'b100:1.85V;
3'b101: 1.90V;
ETMOU huan
3'b110:1.95V
3'b111: 2.00V:
输出
sarc_d2a_adc_os_se_tune<3:0>
配置单端模式下ADCoffset模拟补偿值
输出
配置差分模式下ADCoffse模拟补偿值
sarc_d2a_adc_os_df_tune<3:0>
输出
控制ADC单端侧输入vretp
sarc_d2a_adc_cal_se_refp_inj
输出
控制ADC单端侧输入vrefn
sarc_d2a_adc_cal_se_refn_inj
控制ADC差分侧输入vrefp
输出
dan
sare_d2a_ade_cal_df_refp_inj
12080F



---
## 图像编号 40 (原图: `GameViewer_ZwgMgCyaeL.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图5-22预处理和滤波处`，完整结构与时序请查看原图 `GameViewer_ZwgMgCyaeL.png`。

滤波器实现时序
ready
data
datao
data1
ve1
ve0
手：18-80-01
dotao
datal
veo
ve1
Core1data会
ne ae
率到适时构
. Ji
pre_vs
fromcom 1
pre_val
ADC1
交织
ETHCv1
ETMCI

**图5-22预处理和滤波处**

理时序示意
8TMCI/ han 1i
RTMCI


### 【右页】

Ir data vel
_ date val, d
.Ti
Rr_out_en
Fir_data wal
y cata,val.d
pre
pre_data
data1
动：17-20-0T-97
pre_vai_4d
pre data _Id
daa0
datl
dsso
dats1
BTMC/ buan. 11
Coeft_am_rd .
Coeff_m_rd
Coeft ram addr
Coe_ram ydu
coeft ram dan_d
pipe_ sm nd id
pipe. ram_rd 2
pige_ram_rd_id_neg_pule
pipe_em_add:
pipe_sm_rdan
BTNCI/
ppe ram rdata_ 1d
pipe_gm_wr
piae_sm_rd_t
TMCFman.21
ETCI)
12080F

