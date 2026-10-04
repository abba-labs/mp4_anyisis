# EFC 模块详细设计文档

> 本文档由大模型逐图逐页提取自原始截图，不作主观修饰，忠实还原原文。
> 图表、时序波形及模糊部分均标注对应截图原图文件名供查阅。


---
## 图像编号 1 (原图: `GameViewer_98qp0YcXAk.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图2-15`，完整结构与时序请查看原图 `GameViewer_98qp0YcXAk.png`。

> 📌 **【图表提示】**: 此处包含图表 `图2-16 `，完整结构与时序请查看原图 `GameViewer_98qp0YcXAk.png`。

开启ECC和ECCWRRVS时，对于写入的ECC8bit内容的
第0、1、4-7bit进行取反，保证写数据为全1时，ECC计算结果
8’hC进行处理后也为8’hFF（全1），此时不会对FLASH内
容进行改写；
开启ECC和ECCRDRVS时，对于读出的ECC8bit内容的
第0、1、4-7bit进行取反，保证ECC校验时ECC数据为写入前
未取反的数据。
8TMCV

**图2-15**

ECC域段翻转写入图
f1ash_out[71: 68], f1ash_out [65:64]
DFF
DFT_RAP
72bit
FLASH
VREADI

**图2-16**

ECC域段翻转写入图
ETMOU hua


### 【右页】


### 第3章DFX说明


#### 3.1错误说明

ETMCU han. Ji
1. 写保护错误(wrperr):
当配置接口/数据接口尝试对受保护区域进行写/擦除操作时，
该信号置1．当信号置1后，写/擦除动作终止，不会对数据产
生任何改变；
该状态受对应的清零标志清零；
该状态必须清零才能执行新的写/擦除操作，否则会产生编
程顺序错误，下一次写/擦除操作也会被终止；（配置接口和数
据接口相同）
2.编程顺序错误(pgserr):
当编程顺序不正确时，该信号置1．满足以下条件时，即表示
编程顺序不正确：
A)
数据总线发出了写请求，但cfg_efc_write_en 并没有置
B）
写保护错误标记还未清零，又发出了新的写/擦除操
作;



---
## 图像编号 2 (原图: `GameViewer_9TPJx3syGF.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图2-3GFBAXIMPROC模块框图`，完整结构与时序请查看原图 `GameViewer_9TPJx3syGF.png`。

采用多bit域段多数判决进行校正保护，并且输出校正后的域段
EFC_EFUSE_PPROC_ARB：根据efc_option_ready 仲裁
GFBPOWERPROC与NVREFUSEPROC执行的命令，发送
给 GFB_CTRL模块;

#### 2.2.1. GFB AXIM PROC

GFB_CTRL
ETMCImuan.1

**图2-3GFBAXIMPROC模块框图**

该模块功能框图，主要功能模块概述；
AXI_GS：由 Synopsys 提供的 AXI 请求转换到 GIF(Generic
Interface)请求，GIF响应转换到AXI响应的DWIP;
GFBMPROCPROT：总线保护模块，实时监控总线的反馈情
况，当gating或复位产生时，将总线未完成的交互模拟完成，避
免总线挂死；同时产生门控AXI总线保护错误上报、复位AXI
总线保护错误上报；
通过上电读取NVR ROM Sector的flash_main_wrp/rdp_n，对
AXI总线访问MAIN空间读写保护区域，自动屏蔽写操作，读


### 【右页】

操作数据返回全0，并且根据配置使能决定是否返回总线错误；
GFBMPROCWRAP：将WRAP4/8读访问命令进行转换，当
到达Upper wrap boundary 的读命令地址转换到Lowerwrap
boundary;
GFB_MPROC_ASIZE：将读写命令转换为8B格式;
GFBMPROCMERGE：将写命令按FlashRoW进行拆分(Flash
编程可以在同一个Row内一次性完成)；接收读取返回的数据，
存放到 AXIM_R_FIFO（Depth=16，outstanding*＊burstlen）中,
然后发送到总线上；接收GFBCTRL返回的RESP信息，存放
到AXIM_RESP_FIFO（Depth=2）中，然后发送到总线上；

#### 2.2.2 GFB POWERPROC

根据外部电源信号，进行状态的跳转；
EIMCU muan 1i
执行POWER-ON过程，
用default时钟频率
）读NVR_CFG
在上电阶段需要执行：
如巢需要复位，Flash需要位：
在复位阶段需要执行：
）NVR
2）更新到Option寄存2
F7NCU muan. 13
因此将动作拆分为两个子过程：
1） EFC_POWER -- 读 NVR_CFG，set Config register；见图
1 fp!


## 原图：`GameViewer_Apm6lwGGlA.png`

### 【左页】

Flash Write 根据 SMIC 要求，最多只能一次翻转 36bit，因此将写入的数据分成高低 36bit，分两次分别写入，第一次写入低 36bit，高 36bit 置 1，第二次写入高 36bit，低 36bit 置 1；

**图2-12 Flash Set Config状态转移图**

> 状态转移图按原图保留，不自行重画。  
> 原图：`../images/GameViewer_Apm6lwGGlA.png`

### 【右页】

**图2-13 Flash Erase状态转移图**

> 状态转移图按原图保留，不自行重画。  
> 原图：`../images/GameViewer_Apm6lwGGlA.png`

---

## 图像编号 4 (原图: `GameViewer_AUvuEbreZL.png`)

### 【左页】


#### 2.2.3 NVR~EFUSE PROC

这个模块主要实现上电时发生上电解复位，
GFBPOWERPROC完成nvrshiftdone后，该模块发起flash
的NVRROM/OTPSECTOR区域的读，将其内容全部读出来返
回到其内部寄存器锁存下来。
模块接口说明
>时钟复位接口：时钟为晶振时钟；复位源为上电复位和硬
复位；
>nvr shiftdone接口：该信号用指示GFBPOWERPROC解
复位完成，NVR_CFG区域上电操作完成；
>输出ROM/OTP锁存信息，并进行多数判决：具体那些需要
输出按照硬件需求定，部分ROM/OTP信息送到EFCCFG
模块作为软件可读状态：
nvr_testcode[31:0]、sec_boot_dis[31:0]、cpu_limit_n[7:0]
flash_otp_gen_n[55:0]
nvr_cfg_unlock[7:0]
cpld_limit_n[7:0]、cpld_dbg_dis_n[7:0];
uid[255:0]Securekey[127:0];


### 【右页】

>送出 otp shift done用于指示 flash 的 NVR ROM/OTP区域
已锁存完毕，系统可根据ROM/OTP信息进行下一步流
程;
>送出RDP/WRP信息到EFCCFGPROCPROT模块，用于
该模块做flash读保护和写保护判断依据；
模块状态跳转
当发生上电复位，UGFBPOWERPROC完成NVRCFG读取
和Flash配置和Option读取，即完成nvrshiftdone后，读取
NVRROM/OTP（ROM Sector0~3，OTP Sector4~5，15）信息。

#### 2.2.4 EFC EFUSE PPROC ARB

将 NVR EFUSE_PROC 与 GFB CFG PROC 的输入输出根据
nvr_shift_done信号进行二选一仲裁；

#### 2.2.5 GFB CFG PROC PROT

本子模块接收EFCCFG过来的指令，如读NVR、写NVR、
擦除，产生对应的Flash读、写命令和数据，产生Flash擦除命
令，发送给下级模块；
999+
999+



---
## 图像编号 5 (原图: `GameViewer_b5AJYTEhY1.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图4-2写数datapath示意图`，完整结构与时序请查看原图 `GameViewer_b5AJYTEhY1.png`。


#### 4.2 写性能评估

EFC
AXLMASTER
AXIM_PROC (1D)
CACHE (1D)
ETMCVT2a7i12026-1002-21:40
ECC_GEN(1D)
GFB_CTRL(OD)
GFB_IF(1D)
S40_FCTRL (2D)
FLASH(XMS)
KIMCU

**图4-2写数datapath示意图**

写数据时，性能瓶颈在FLASH处，可以提升的地方就只在连
续编程上;
单次（72bit）编程大概39us-约
BIMCU
分两次36bit编程大概78us一约


### 【右页】

连续编程，那么72bit在Burst16下可以缩到31us左右=~约
连续编程，那么72bit分两次写入在Burst16下可以缩到60us
左右 -- 约
与 SMIC交流后，不能实现更长的Burst编程--有预编程和编
程两个阶段，都需要对应的地址和数据，也就意味着需要数据
缓存，这一版确定缓存16个数据；

#### 4.3擦除性能评估

数据擦除时，datasheet中给出的典型擦除时间是8~，根
据SMIC回复，可以直接使用:
1）sector擦除性能=1KB/=125KBps;
2）
整片擦除性能=512KB/=
块擦除时，使用RETRY模式可能会有一定的时间节省，单
次　sector RETRY²擦除是　0.~lms ＋VREAD2读 取
200ns*128=26us，需要RETRY擦除多少次不确定；如果只擦除
一次，那么 sector擦除性能可以提升到：1KB/=



---
## 图像编号 6 (原图: `GameViewer_bJ7d9eVqlF.png`)

### 【左页】

C）不一致错误标记还未清零，又发出了新的写/擦除操
作；
D)
ETMCO
配置ECC2bit错误标记还未清零，又发出了新的写/擦
除操作;
E）数据ECC 2bit错误标记还未清零，又发出了新的写/擦
除操作；
该状态受对应的清零标志清零；
该状态必须清零才能执行新的写/擦除操作，否则会产生编
程顺序错误，下一次写/擦除操作也会被终止，读操作会返回总
线ERROR；0°（配置接口和数据接口相同）
3.选通错误(strberr)：
TC当数据接口连续2次以上向同一个地址写同一字节时，该信
号置1．当信号置1后，写动作不会终止，应用程序可忽略该错
误，继续执行当前写操作，并可以继续执行新的写/擦除操作；
该状态受对应的清零标志清零；
该状态不须清零也可以执行新的写/擦除操作；
4.不一致错误(incerr)：
当配置接口上一笔命令还未执行完成，配置接口再次发出新的


### 【右页】

命令，就发生不一致错误，并且新的命令不会被执行；
该状态受对应的清零标志清零；
对于配置接口，该状态必须清零才能执行新的写/擦除操作，
否则会产生编程顺序错误，下一次写/擦除操作也会被终止；
数据接口不受该错误影响；
5.配置ECC1bit错误：
配置接口读取NVR／NVRCFG时，发生ECC1bit错误，并
纠错，该信号置1．当信号置1后，读取返回数据正确，应用程
序可忽略该错误，继续执行当前读操作，以及下一步操作（不需
要对当前地址进行retry处理）；
该状态受对应的清零标志清零；
该状态不须清零也可以执行新的读/写/擦除操作；
6.配置ECC2bit错误：
配置接口读取NVR／NVRCFG时，发生ECC2bit错误，该
信号置1．当信号置1后，读取返回数据不正确，应用程序无法
忽略该错误，需要对当前地址进行retry处理或其他动作；
该状态受对应的清零标志清零；
对于配置接口，该状态必须清零才可以执行新的读/写/擦除
1 fp


## 原图：`GameViewer_ceValKI1oj.png`

### 【左页】

**图2-9 Flash Power状态转移图**

> 状态转移图按原图保留，不自行重画。  
> 原图：`../images/GameViewer_ceValKI1oj.png`

状态会提供到 GFB_PPROC 模块，GFB_PPROC 模块在

### 【右页】

WORKING 状态时才会正常工作；

上电过程和下电过程的时序，由系统（Flash Power Switch & POR）来实现；

**注意：在 power_off 状态下，需要将 Flash 所有的输入接 0；**  
（S40NEF64KX72_S0_Application_Notes.pdf -- 1.2 POWER OFF）

#### 2.3.4 FCTRL_GFB_CMD_IF

**图2-10 FCTRL状态转移图**

> 状态转移图按原图保留，不自行重画。  
> 原图：`../images/GameViewer_ceValKI1oj.png`
## 原图：`GameViewer_f9t1x50Gvk.png`

## 第5章 对外部模块需求

| 序号 | 外部模块 | 要求 |
|---:|---|---|
| 1 | Power Switch/POR | 上电时、异常掉电时，PORb 与 VDD、VDD11 的时序需满足 Flash 要求； |
| 2 | 系统 | 模块内对 efc_aclk 和 efc_clk 不做异步处理，系统关注异步相关； |
| 3 | CORE_BUS | 本模块对 AXI 的支持特性：1）burst 类型只支持 INCR；2）Outstanding 为 3；3）不支持 out-of-order；4）不支持 LOCK/PROT/Cache；5）不支持 interleaving；6）不支持总线低功耗接口；7）不支持跨 4K； |
| 4 | CRG | Flash 工作时钟 flash_clk 频率不能高于 100MHz；两个工作时钟同源，且频率比为 efc_clk：flash_clk = 1:1 或 2:1；时钟关系见下图； |
| 5 | CRG | 1）模块软复位；2）模块时钟门控；3）芯片硬复位；4）POR 硬复位时，efc_rst_n 必然复位；以上功能由 CRG 模块实现，本模块内部不做额外处理；复位撤销顺序如下：1. 上电启动，撤销顺序为：flash*_por_rst_n -> por*_rst_n -> efc*_rst_n -> efc*_aresetn -> efc*_presetn；2. 系统软复位，撤销顺序为：efc*_rst_n -> efc*_aresetn -> efc*_presetn；3. 模块级软复位，只有 efc*_rst_n；注：如果这几个时钟都连接同一个时钟，那么同时复位也是满足需求的。 |
| 6 | CRG | EFC 上电过程结束后，需要将 EFC 的工作频率从 256KHz 切换到 25MHz 进行 Boot，再切换到 100MHz 进行工作； |
| 7 | CRG | 对 EFC 内的 3 个时钟，分开进行时钟门控，避免总线挂死； |
| 8 | CRG/软件 | EFC 工作频率的改变，必须保证 EFC 已有的操作处理完成，否则可能引起数据错误； |
| 9 | 软件 | 对 Flash 的先写后读（特别是背靠背操作），需要软件保证写完成以后再发起读操作；否则，可能发生数据不正确问题； |
| 10 | BOOTROM | NVR_CFG 的 PRO、PR1 信息，需要 bootrom 中进行读取，并配置这个替换内容到 efc 对应寄存器上，保证程序功能的正确性； |
| 11 | 软件 | OTA 切换时，cpu cache 需要被 disable，保证进行 OTA 切换时软件不会访问 Flash； |

**注：要求确认后，添加到钉钉共享文档，做为系统待办，便于统一跟踪。**

---

## 图像编号 9 (原图: `GameViewer_Fio2eDanFe.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `flash_nvrμotp_n[7:0][4:0]进行多数判决;6见图2-5;`，完整结构与时序请查看原图 `GameViewer_Fio2eDanFe.png`。

> 📌 **【图表提示】**: 此处包含图表 `图2-4EFCPOWER状态转移图`，完整结构与时序请查看原图 `GameViewer_Fio2eDanFe.png`。

2-4;
2）EFC RESET --读 取 NVR，更 新
OTP/OB
( NVR
BTN寄存
Sector5/6/7/14
flash_main_rdp_n[31:0],flash_main_wrp_n[31:0],flash_nvr_rdp_n[
0],flash_nvr_wrp_n[0] ; securelevel[16:0],nSWBOOT1,nBOOT1,
flash_nvrμotp_n[7:0][4:0]进行多数判决;6见图2-5;
那么上电阶段执行1）和2）子过程，并使用por_rst_n复位；
复位阶段只执行2）子过程；
GFB_POWER_OFF
inthis state
state to initial Flash
ua2z 11 0026-70-02-21.37
ETMCi
s12_fctr_state==GFB_PWR_WORKINGhard_arst_n=1b0
GFB_RD_NVRC
GFB_SETC
read_done
write_done
GFB_PWR_WORKING
setconfgregister
Iq(=u ise pley
readNVR_CFG

**图2-4EFCPOWER状态转移图**



### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图2-5EFCRESET状态转移图`，完整结构与时序请查看原图 `GameViewer_Fio2eDanFe.png`。

GFB_RST_DLE
in this state
RICU
reset use eft_arst_n
RTMC muan.1i
efc_power_state==GFB_RST_WORKING
fc_arst_n=160
GFB_RD_NVR
GFB_UPT_OPTION
read_done
write_ done = next cycle
GFB_RST_WORKNG
read NVR
(Q Imu~1s/e5)
update option registers

**图2-5EFCRESET状态转移图**

mian.1i 2026-20-02-21:37
根据状态，POWERCMD产生对应的Flash读、写命令和数
据，发送给下级模块；
到达GFB_RST_WORKING状态时，即对外输出
nvr_shift_done信号；从复位释放（porrstn和efc_rst n），到进
入GFBRST_WORKING状态，有超时机制，超过门限后也会输
出nvr_shift_done信号，但同时会上报超时状态；
当上电复位时，需要读NVR_CFG；
硬复位时，需要读取OTP/OB（NVRSector5/6/7/14）寄存器：
flash_main_rdp_n[31:0],flash_main_wrp_n[31:0],flash_nvr_rdp_n[
0],flash_nvr_wrp_n[0] ; securelevel[16:0],nSWBOOT1,nBOOT1,
flash_nvr_otp_n[7:0][4:0]进行多数判决;


## 原图：`GameViewer_GsJtl9ctbU.png`

### 【左页】

| 信号 | 方向 | 说明 |
|---|---|---|
| fctrl2gfb_rdata_vld | 输出 | Flash读数据有效，高电平有效 |
| fctrl2gfb_rdata[FLASH_DW-1:0] | 输出 | Flash读数据 |
| fctrl2gfb_resp_vld | 输出 | Flash反馈有效，高电平有效 |
| fctrl2gfb_resp | 输出 | Flash反馈信号；0：成功；1：失败； |
| efc_pwr_working | 输出 | Flash Power状态信号 |
| efc_fctrl_idle | 输出 | Flash未执行指令空闲信号 |

**Flash接口**

| 信号 | 方向 | 说明 |
|---|---|---|
| A[FLASH_AW-1:0] | 输出 | 地址信号 |
| DIN[FLASH_DIW-1:0] | 输出 | 写数据 |
| DOUT[FLASH_DOW-1:0] | 输入 | 读出数据 |
| RDEN | 输出 | 读使能信号 |
| NVR | 输出 | NVR指示 |
| NVR_CFG | 输出 | NVR_CFG指示 |
| LCK_CFG | 输出 | wafer testing后锁定为1 |
| CEb | 输出 | 片选使能 |
| WEb | 输出 | 写使能 |
| PROG | 输出 | 编程信号 |
| PROG2 | 输出 | 编程信号2 |
| PREPG | 输出 | 预编程信号 |
| ERASE | 输出 | 擦除信号 |
| CHIP | 输出 | 片擦除指示 |
| PORb | 输出 | 电源开关信号 |
| CONFEN | 输出 | 配置寄存器使能 |
| ARRDN[FLASH_ARRDNUM-1:0] | 输出 | 备用资源信号选择 |
| RECALL | 输出 | RECALL读指示 |
| DPD | 输出 | 低功耗模式 |
| VREAD1 | 输出 | Verify Read，主要用于retry erase后 |
| RETRY[FLASH_RETRYW-1:0] | 输出 | Sector的Retry Erase |

### 【右页】

#### 2.3.3 FCTRL_POWER_PROC

> 原图为 Flash Power 时序图，图内可确认信号包括 VDD/VDD11、PORb、DPD、CEb、RDEN、CLOCK、PROG、ERASE。复杂波形不自行重画。  
> 原图：`../images/GameViewer_GsJtl9ctbU.png`

---

## 图像编号 11 (原图: `GameViewer_hMzpsucGw1.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图2-2EFCGFB模块框图`，完整结构与时序请查看原图 `GameViewer_hMzpsucGw1.png`。


#### 2.2 EFC GFB

EFC_GFB
GFB_AXIM_PROC
GFB_CTRL
, 1i
AXLMASTER
AXM_IF
CACHE
CTR_STATE
ECC_CORR
CMD_MERGE
CMD_MLX
RD_MUX
ECC_GEN_W
RTMC!
ETMCII 2
GFB_IF
EFC_FCTR
GFB_POWER_PROC
EFc_CrQ_FROC
NMR_EFUSE_PROC
PR_STATE
POWER_CMD
EFC_CFG
POR
EIMCHr

**图2-2EFCGFB模块框图**

该模块功能框图，主要功能模块概述；
GFB_AXIM PROC：接收AXI总线读写 FLASH命令，分别
进行总线保护、WRAP命令整合、命令size调整、命令合并，读
取FLASH数据、返回RESP信息发送到总线上；
GFB_POWER_PROC：执行上电与复位时对Flash 的操作，读
取NVR_CFG，SetConfigReg，读取 OTP/OB域段；上述硬件自


### 【右页】

动加载涉及到启动模式、安全等级和信息安全的域段采用多bit
域段多数判决进行校正保护，并且输出校正后的域段值；
GFBCFGPROC：接收并处理EFCCFG过来的指令，根据
指令格式组合是否正确，访问区域是否有读写保护进行屏蔽检
查；01
GFBCTRL：子模块分别接收APB间接命令、POWER上电、
复位命令和AXI总线命令，进行MUX选择，写数据增加ECC
后，产生对应的命令给GFBIF模块，接收GFBIF模块返回的
命令，检查ECC后分别返回给命令来源；预取数据提高AXI总
线读访问效率；
GFBIF：将ECCGENW的数据，从接口发送给
EFC FCTRL；接收EFC FCTRL返回的数据和RESP，发送给下
级模块；
NVREFUSEPROC：上电时发生上电解复位，1:3
GFBPOWERPROC完成nvrshiftdone后，该模块发起flash
的 NVR ROM/OTP SECTOR (ROM Sector0~3， OTP Sector4~5,
15）区域信息的读，将读取的内容用寄存器寄存下来，输出给
SYSC模块和EFC内部保护逻辑使用，并输出otp_shift_done;
上述硬件自动加载涉及到启动模式、安全等级和信息安全的域段
2 fp
H080E



---
## 图像编号 12 (原图: `GameViewer_hoWrmQ3kyX.png`)

### 【左页】

操作；
数据接口不受该错误影响；
7.数据ECC1bit错误：
数据接口读取Main/RDN时，发生ECC1bit错误，并纠错，
该信号置1.当信号置1后，读取返回数据正确，应用程序可忽
略该错误，继续执行当前读操作，以及下一步操作（不需要对当
前操作进行retry处理）；
该状态受对应的清零标志清零；
该状态不须清零也可以执行新的读/写/擦除操作；
8.数据ECC2bit错误：
数据接口读取Main/RDN时，发生ECC2bit错误，该信号置
1．当信号置1后，读取返回数据不正确，应用程序无法忽略该
错误，需要对当前操作进行retry处理或其他动作；
该状态受对应的清零标志清零；
对于配置接口，该状态必须清零才能执行新的擦除操作，否
则会产生编程顺序错误，下一次擦除操作也会被终止；
对于数据接口，该状态必须清零才能执行新的写/擦除操作，
否则会产生编程顺序错误，下一次写/擦除操作也会被终止；


### 【右页】

在该错误未清零前，新的读操作也不再执行，总线数据返回
O，RESP返回ERROR；
9.门控APB总线访问错误：
当EFC的gating产生时，APB总线上还有数据交互未完成或
来了新的总线命令；
该状态不须清零也可以执行新的读/写/擦除操作；
n712026-10-02-21-4
上报中断，总线数据返回O，RESP返回ERROR；
10.复位APB总线访问错误：
当EFC的复位产生时，APB总线上还有数据交互未完成或来
了新的总线命令；
该状态不须清零也可以执行新的读/写/擦除操作；
上报中断，总线数据返回O，RESP返回ERROR;
11.门控AXI总线保护错误：
当EFC的gating产生时，AXI总线上还有数据交互未完成或
来了新的总线命令，总线保护模块将总线未完成的交互模拟完
成，避免总线挂死；
该状态不须清零也可以执行新的读/写/擦除操作；
上报中断，总线数据返回O，RESP返回ERROR；



---
## 图像编号 13 (原图: `GameViewer_isM3FELYfq.png`)

### 【左页】

Program Or
not retry Erase
RD MODE
VREAD1==1' b0
No Change
RD MODE
Change
RDIODE
Change
Normal
Recall
RIMCU manzTi
Read
Read
RD MODE
Vreadl
RD MODE
Change
Change
Only to
ARD MODE
Only to
Retry
No Change
Retry
Program Or
Erase(inc retry)
VREAD1==1' b1
ETNOUm/a11
1、ET6601中优化为只有RecallRead需要等待tMH，Normal
Read、Vreadl不等待，提升NormalRead、、Vreadl效率；
2、VREAD1在RETRYERASE操作中提前拉高，在非RETRY
ERASE和PROGRAM中保持不变，按照之前代码可能会出现
NormalRead的tMH等待时间不够的违例，因此将VREADl
拉高时间修改为tNVS之后：
INVS
PROG/ERASE/CEb/ARRDN/NVR/NVR_CFG/CHIP/Ato WEb setup
time
ETMOu 2
ETMCU Tuan. 1i


### 【右页】

Ax
ERAS
wEb
NEXT ERASE
ETICu
ERASE
CEb
NVR/ARRDN
/NVR_CFG
CHIP
RDEN
ETMO/ hoar 1 2026-10-02-21-39
CLOCK
PROG
Figure 4: Sector Erase Timing Diagram
Notes: (1) Ax is X address, means Au-7)
3、进入Program、ERASE时都将Recall拉低；（与ET6601方
案保持一致)
4、进入READ模式时，只根据VREAD1和Recall信号的变化
记录的READ MODE来决定是否要等待tMS，而不是每次
ERASE/PROGRAM都认为READMODE发生过变化;

#### 2.3.5 FCTRL GFB FLASH IF

根据状态机信息进行具体接口信号的生成；
080F



---
## 原图：`GameViewer_ix7GnZKXn3.png`

### 【左页】

### 1.1.3 Flash Power Switch 的连接关系

**图1-3 Flash Power Switch的连接关系图**

> 图内可确认标签：Flash_Power & POR、CRG、EFC、EFC_GFB、S40_FCTRL、FLASH、VDD、VDD11、por_rst_n。  
> 原图：`../images/GameViewer_ix7GnZKXn3.png`

### 【右页】

### 1.1.4 时钟域说明

**图1-4 FLASH_EFC模块内时钟域说明图**

> 图内可确认模块：AXI_MASTER、APB_MASTER、EFC_CFG、EFC_GFB、AXIM_IF、EFC_CFG_MAN、EFC_GFB_MAN、EFC_FCTRL、FLASH。  
> 原图：`../images/GameViewer_ix7GnZKXn3.png`

整个 EFC 模块使用了 5 个时钟，apb 时钟、axi 时钟、EFC 内部 core 时钟、EFSUE 时钟以及 Flash 时钟；

3 个时钟（apb 时钟、axi 时钟、EFC 内部 core 时钟）在系统上都是给的同一个时钟（如果有异步处理，也是在 NOC 总线上实现）；

Flash 时钟与 EFC 内部 core 时钟同源，时钟频率比为 1:1、1:2
## 原图：`GameViewer_Jv14xpHsSC.png`

### 【左页】

> 原页嵌入问题单截图，标题可确认：  
> **[EFC-BT] APB与AXI同时对NVR和MAIN进行访问时功能出错**  
> 其余问题单字段、附件与人员信息不作为正文猜测性转录。  
> 原图：`../images/GameViewer_Jv14xpHsSC.png`

### 【右页】

> 原页包含 Synchronous Read Cycle Timing Diagram、配置代码截图及红色批注；复杂图和代码截图按原图保留。  
> 原图：`../images/GameViewer_Jv14xpHsSC.png`

红色批注：

**并且进入 READ MODE CHANGE 阶段本身应该等待 tMH 时间逻辑也未生效，实际在等待之前 READ MODE 就切换了；**

---

## 图像编号 16 (原图: `GameViewer_kpuE7cPAm8.png`)

### 【左页】

efc rst n
输入
输入复位信号，低电平有效
efc_gclken
输入
flash工作时钟与efc_clk之间的分频使能
flash clk
输入
输入时钟，FLash工作时钟
电源相关
输入
por_rst_n
硬件复位信号，低电平有效；
复位表示Flash电源关闭，由POR提供；
该复位有效时，efcrstn必然有效，由CRG实
现；
flash por_rst _n
输入
flash硬件por复位信号，低电平有效
测试相关
输入
TEST_EN
测试使能信号
0：测试不使能，正常工作；
1：测试使能，可执行ATE、Wafertesting等动
作；
ETMCII
EFC_VREF
输入
Flash参考电压输入
EFC_TMO
输入输出
Flash测试模式
EFC_VPPO
输入输出
Flash VPPO
EFC_VPP1
输入输出
Flash VPP1
中断
efc int
输出
Flash产生的中断信号，高电平有效
SECUREERASE/OTP相关
nvrcfg_unlock[7:0]
输入
pflash0/pflash1/dflashnvr_cfg空间的读/写/擦
EIMCU
除保护
0x5A：打开保护，数据不能被读/写/擦除；
其他：关闭保护，数据能被读/写擦除；
输入
secure_erase_main_df
PFLASH收到DFLASHO强制擦除FLASHMAIN指
secure erasemain done pf输出
PFLASHMAIN擦除结束指示
CRG
nvrshift_done
输出
Option奇存器准备好，高电平有效；
CRG可以根据该信号，撤销CPU的复位，让CPU
开始进行Boot动作；
内部增加超时机制，超时后拉高；
cfg_efc_core_gate_en
输入
0：EFC未被门控；
1：EFC被门控，需避免总线被挂死；


### 【右页】

Q:37
timing信息
cfg_efc_timing_r[447:0]
输入
Flash使用的timing信息；
APB总线
efc_pclk
输入
APB时钟
han.11
efc_presetn
输入
APB复位信号，低电平有效
输入
efc psel
APB选择信号
efc_penable
输入
APB使能信号
efc _paddr[31:0]
输入
APB地址信号
efc_pwrite
输入
APB写指示信号
0：读操作；
1：写操作；
输入
efc pwdata[31:0]
APB写数据
输出
APB读数据
efc_prdata[31:0]
huem.11
efc_ pready
输出
APB准备好信号，高电平有效
efc _pslverr
输出
APB错误信号，高电平有效
AXI总线
efc_aclk
输入
AXI时钟
efc aresetm
输入
AXI复位，低电平有效
efe_awid[5:0]
输入
AXI写命令通道ID
输入
efc _awaddr[31:0]
AXI写地址
输入
efc_awlen[3:0]
AXI写burstlen
efc_awsize[2:0]
输入
AXI写数据宽度
man 1i 2026-10-02-21:
efe_awburst[1:0]
输入
AXI写类型
efc_awvalid
输入
AXI写有效指示，高电平有效
efc_awready
输出
AXI写准备好指示，高电平有效
efe_awlock
输入
AXI锁
efc_awcache
输入
AXI cache
输入
efc_awprot
AXI保护
efe_wid[5:0]
输入
AXI写数据通道ID
efc_wdata[63:0]
输入
AXI写数据
输入
efc_wstrb[7:0]
AXI写数据byte有效指示
efc_wlast
输入
AXI写last指示
efe_wvalid
输入
AXI写数据有效
efc_wready
输出
AXI写数据准备好指示，高电平有效
输出
efc bid[5:0]
AXI反馈通道ID
efc bresp[1:0]
输出
AXI反馈内容
12080F



---
## 图像编号 17 (原图: `GameViewer_kreeGdjIJX.png`)

### 【左页】

或1:6;
EFC 内的3个时钟（apb 时钟、axi时钟、EFC内部core 时
钟），在CRG内分开进行时钟门控，避免APB、AXI总线被挂
死；Flash时钟与EFC内部core时钟门控一致。
EFSUE时钟与EFC内部core时钟在OSC25MHz下同频同
源。
ETMCIman.

#### 1.2接口列表和接口时序

(026-10-08

**表1-1EFC_DFLASH接口信号说明**

时钟信号
输入输出说明
输入
输入时钟，频率为25MHz~200MHz
ETMGU
输入
efcrst n
输入复位信号，低电平有效
efc_gclken
输入
flash工作时钟与efc_clk之间的分频使能
flash_ clk
输入
输入时钟，flash工作时钟
电源相关
输入
por_rst_n
硬件复位信号，低电平有效；
复位表示Flash电源关闭，由POR提供；
该复位有效时，efc_rst_n必然有效，由CRG实
现；
flash por rst n
输入
flash硬件por复位信号，低电平有效
测试相关
TEST_EN
输入
测试使能信号
0：测试不使能，正常工作；
1：测试使能，可执行ATE、wafertesting等动
作；


### 【右页】

输入
EFC_VREF
Flash参考电压输入
输入输出
EFC_TMO
Flash测试模式
EFCVPPO
输入输出
Flash VPPO
输入输出
EFC_VPP1
Flash VPP1
中断
efc_int
输出
Flash产生的中断信号，高电平有效
OTP相关
clk_otp
输入
otp时钟，晶振时钟
输入
otp_rst_n
otp复位信号，低电平有效
rom_rd_en
输入
ROMSECTOR读保护信号有效指示，由sysc模块
送出
sysc_boot_exit_lockj
输入
BOOT退出锁定，控制OTP寄存器读写权限，由
SYSC模块配置下发
hem 11 8026-10-02-21:3
输出
otp_shift_done
otp shift完成指示信号，输出给SYSC，
DEBUGAUTH模块使用
输出
nvr_test_code[31:0]
芯片调试码，输出给SYSC，DEBUG_AUTH模
块使用
uid[255:0]
输出
芯片唯一ID，输出给DEBUG_AUTH模块使用
secure_ level[1:0]
输出
鉴权等级，输出给DEBUGAUTH模块使用
输出
secure_key[127:0]
鉴权密码，输出给DEBUG_AUTH模块使用
输出
CPU1限定使能
cpld_limit_n
输出
CPLD限定使能
cpld_dbg_dis_n
输出
CPLDJTAG接口调试禁止
nvrcfg_unlock[7:0]
输出
pflash1/dflashnvr_cg空间的读/写/擦除保护
0x00：打开保护，数据不能被读/写/擦除；
其他：关闭保护，数据能被读/写/擦除；
PFLASH相关
secure_erase_main done pf输入
PFLASHMAIN擦除结束标志
输出
secure_erase_main
DFLASH强制擦除PFLASHMAIN指示
CRG
输出
nvi_shift_done
Option奇存器准备好，高电平有效；
SYSC模块可以根据该信号，锁定启动模式；
12080F


## 原图：`GameViewer_l6EdkNy5JN.png`

### 【左页】

从 GFB 接口分解出对应的 CMD 指令和数据信息，根据指令类型进行状态跳转，并将状态发送给 FCTRL_GFB_FLASH_IF 模块；

将写数据信息存放到寄存器阵列中，然后将数据发送到 FLASH_IF 发送到 Flash；

将从 Flash 读取的数据，根据命令类型，进行擦除校验或者发送给 EFC_GFB 模块。

### 【右页】

**图2-11 Flash Write状态转移图**

> 状态转移图按原图保留，不自行重画。  
> 原图：`../images/GameViewer_l6EdkNy5JN.png`

---

## 图像编号 19 (原图: `GameViewer_MhzCnwHL7y.png`)

### 【左页】

EFCCMNWRPPROT(REG)：寄存器写保护模块，解除写保
护流程参考《EFC模块LRS设计文档》第1.2.10.1寄存器写保
护章节；
EFC_CMN_WRPPROT(NVR)：NVR写保护模块，解除写保护
流程参考《EFC模块LRS设计文档》第1.2.10.3NVR写保护章
节;
CFGFLASHIDS：该模块使用工具自动生成，
PFLASH/DFLASH需求分别生成，具体的配置参见
《efc_cfg_dflash_nmanager》/《efc_cfg_pflash_nmanager》，里面
包含：
1.Flash的timing参数，空间大小信息；
特别说明：在STM32、TI设计中，都是基于几个固定频率来
配置 Flash 接口的 timing参数；在当前设计中，是对所有 timing
参数都进行了配置（目的：a.支持任意频率；b.对Flash时序有
更大的容错空间）
default参数为25MHz频率下参数，当EFC内部CORE工作
频率变化时，FLASH 时钟频率也随之变化，软件配置 timing参
数来进行适配，可根据各timing参数自动计算对应的ids寄存器
值。


### 【右页】

Q1:37
2.写保护：寄存器写保护、key1/2，NVR写保护、key3/4;
3.写保护：mainarray的各个sector保护标记；
4.ECC：使能纯寄存器
5.正常操作：读、写、擦除，类型
6.中断相关：使能、状态、清零
7.上报：中断状态、Flash状态、DFX信息
ETMGU
ETNCO huam
EFC_INT_PARSE、INT_GEN MRG：中断上报、汇聚模块，
将中断上报给
CFGFLASHIDS并且汇聚后上报给
SOC CORE。
EINCU
ETMCUua). 3 2026-10-02-21;37
ETNCUhan.13
080F


## 原图：`GameViewer_nCyHpYzZqG.png`

### 【左页】

| 信号 | 方向 | 说明 |
|---|---|---|
| efc_bvalid | 输出 | AXI反馈有效指示，高电平有效 |
| efc_bready | 输入 | AXI反馈准备好指示，高电平有效 |
| efc_arid[5:0] | 输入 | AXI读命令通道ID |
| efc_araddr[31:0] | 输入 | AXI读地址 |
| efc_arlen[3:0] | 输入 | AXI读burstlen |
| efc_arsize[2:0] | 输入 | AXI读数据宽度 |
| efc_arburst[1:0] | 输入 | AXI读类型 |
| efc_arvalid | 输入 | AXI读有效指示，高电平有效 |
| efc_arready | 输出 | AXI读准备好指示，高电平有效 |
| efc_arlock | 输入 | AXI锁 |
| efc_arcache | 输入 | AXI cache |
| efc_arprot | 输入 | AXI保护 |
| efc_rid[5:0] | 输出 | AXI读数据通道ID |
| efc_rdata[63:0] | 输出 | AXI读数据 |
| efc_rresp[1:0] | 输出 | AXI读数据反馈指示 |
| efc_rlast | 输出 | AXI读数据last指示 |
| efc_rvalid | 输出 | AXI读数据有效指示，高电平有效 |
| efc_rready | 输入 | AXI读数据准备好指示，高电平有效 |

**AXI GS 相关信号**

| 信号 | 方向 | 说明 |
|---|---|---|
| efc_awlock[1:0] | 输入 | 外部可固定连接0 |
| efc_awcache[3:0] | 输入 | 外部可固定连接0 |
| efc_awprot[2:0] | 输入 | 外部可固定连接0 |
| efc_arlock[1:0] | 输入 | 外部可固定连接0 |
| efc_arcache[3:0] | 输入 | 外部可固定连接0 |
| efc_arprot[2:0] | 输入 | 外部可固定连接0 |

### 【右页】

## 第2章 详细设计

### 2.1 EFC_CFG

**图2-1 EFC_CFG模块框图**

> 图内可确认模块：SOC_CORE_MISC、INT_GEN_MRG、EFC_INT_PARSE、CFG_REGPROT、EFC_CFG_IDS、EFC_CFG_MAN、EFC_CFG、APB_MASTER、EFC_GFB、EFC_FCTRL。  
> 原图：`../images/GameViewer_nCyHpYzZqG.png`

该模块功能框图，主要功能模块概述；

CFG_REGPROT：当 EFC 时钟 gating 或者复位后 FLASH 未进入 working 状态时，禁止 APB 总线对 IDS 寄存器进行读写操作；寄存器写保护未解除前，除了寄存器、NVR 解除写保护操作外，禁止 APB 总线对 IDS 寄存器进行写操作；产生 APB 总线的各类错误告警。

---

## 图像编号 21 (原图: `GameViewer_OCJBCUSbNK.png`)

### 【左页】

12.复位AXI总线保护错误：
当EFC的复位产生时，AXI总线上还有数据交互未完成或来
了新的总线命令，总线保护模块将总线未完成的交互模拟完成，
避免总线挂死；
该状态不须清零也可以执行新的读/写/擦除操作；
上报中断，总线数据返回O，RESP返回ERROR;
13.FLASH配置总线发生读写保护记录：
当FLASH通过apb通路读写flash颗粒时发生违反读写保护
时，分别记录违反的第一个地址。

#### 3.2 DFX 设计

Truan.11
EIMCU
1.ECC错误注入（模拟ECC错误产生）：
由于Flash的特殊性（写入数据后无法直接更新，需要擦除后
再写入，并且Flash本身有擦除寿命），因此尽量减少对Flash的
写入动作，ECC错误注入在读取时进行模拟；因此，该功能在
EFCGFB/GFBIF模块内实现；


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图3-1ECC错误注入对应寄存器配置`，完整结构与时序请查看原图 `GameViewer_OCJBCUSbNK.png`。

序号
说明
Tueuofuo"oo"6p
ECC错说注入使能
160：不打开ECC错误注入：
1b1：打开ECC错误注入；
2d0
ECC错误注入类型：
1：2bt滑润：
other：更多biti措读：
16do
ECC错误注入对度地址
clg_efc_ecc_ergen_sec_r
地址sector范图：
0: NVR_CFG;
1: NVR;
2 RDN;

**图3-1ECC错误注入对应寄存器配置**

TMCLFHuTan.11
ETMCV g-m7
FTNCU han. 3 3026-10-02-71:40
13080F



---
## 原图：`GameViewer_oiTQxKdn2v.png`

### 【左页】

## 第1章 概要设计

### 1.1 功能框图

**图1-1 EFC模块框图**

> 图内可确认模块：CRG、EFC_CFG、EFC_GFB、EFC_FCTRL、FLASH、FLASH_POWER、APB_MASTER、AXI_MASTER。  
> 原图：`../images/GameViewer_oiTQxKdn2v.png`

该模块功能框图，主要功能模块概述；

EFC_CFG 模块：通过 APB 总线，接收 APB Master 来的配置；

EFC_GFB 模块：接收外部 CRG 信号，对 Flash 进行开关控制（电源打开时，需要对 Flash 进行读 NVR_CFG，再写 Flash CFG 的动作；然后才能进行正常工作）；通过 AXI 总线，接收 AXI Master 来的数据传输；

EFC_FCTRL 模块：接收来自 EFC_GFB、EFC_CFG 的数据和配置，产生 Flash 操作对应的时序处理，以达到控制 Flash 的目的；

### 【右页】

### 1.1.2 Flash 结构框图

**图1-2 S40 FLASH结构框图**

> 原图中为 S40 FLASH 内部结构框图；复杂图不自行重画。  
> 原图：`../images/GameViewer_oiTQxKdn2v.png`

---

## 图像编号 23 (原图: `GameViewer_Pi2p76SFY0.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图2-7Cache状态转移图`，完整结构与时序请查看原图 `GameViewer_Pi2p76SFY0.png`。

6）AXIM PROC后续发送的地址，如果大于CACHE中某些
地址，CACHE先释放小于AXIM PROC地址的数据，再填满
CACHE空间;
7）AXIMPROC后续发送的地址，如果小于CACHE首地
址，CACHE自动清空后，再和4）做同样动作；
ETHCUh1a112026

**图2-7Cache状态转移图**

CMDMUX将命令和数据都发送到ECCGENW中，如果
是写操作则添加ECC信息后送往下级模块；如果是读、擦除等
操作，则直接送往下级模块，无延迟；
ECCCORR将返回的数据进行ECC检测和纠错，然后送往


### 【右页】

RD DMUX;
1)
如果一致，则表明没有错误；
2)
如果有1bit错误，则产生中断并纠错；
ETICU
3)
如果有2bit及以上错误，则产生中断，并原始数据返
RD DMUX
将返回的数据，分发给
AXIM PROC/POWER PROC/CFG_PROC;
READ、RECALL操作，会经过ECC_CORR，进行ECC检测
和纠错;
VREAD CHK（含Retry，的VREAD CHK）操作，直接检测
GFBIF进来的数据是否全1，不经过ECCCORR，目的是检查
擦除操作是否擦干净，ECC域段和DATA 域段都必须为全1,;

#### 2.2.7 GFB IF

将ECC_GEN_W的数据，从接口发送给EFCFCTRL；
接收EFC_FCTRL返回的数据和RESP，发送给下级模块；



---
## 图像编号 24 (原图: `GameViewer_QiBBFQjMG4.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图2-6GFB CTRL状态转移图`，完整结构与时序请查看原图 `GameViewer_QiBBFQjMG4.png`。

寄存器复位默认为0且只受软件写控制，在bootrom退出时将该
寄存器写1，软件就无法进行该操作；（保证该操作只在bootrom
有权限);
2.《ET6601可信安全硬件详细设计说明》5.3.2章节对应寄存
器在EFC 实现;
otp的读写访问，受寄存器sysc_boot_exitlockj控制；
rom的读访问，受寄存器rom_rd_en控制;

#### 2.2.6 GFB CTRL

GFB_CTRL_WAITING
GFB_CTRL_IDLE
送到下吸模快
1b11g/b_cmd_ye
GFB_CTRL_WR
GFB_CTRL_RD
GFS_CTRL_BRESP
所有数需已限驱膜存后的mdlenm1发送完成
下一拍通图GFB.CTRLIDLE
ETMCyian 1i2
GFB_CTRL_WRESP
净持Flash的resp退国并提手，确认色完全写入Fush

**图2-6GFB CTRL状态转移图**



### 【右页】

CMD_MUX接收从CACHE/POWER PROC/CFG PROC来的
命令，并从中选择（绝度优先级，POWERPROC>
CFG PROC>CACHE)。
CACHE接收AXIM_PROC的读命令，并返回数据；
对于 AXIM PROC 相关的取数：
1）如果AXIM PROC读取burst 数据，所有都包含在
CACHE中，则不往Flash产生命令，直接从CACHE中取数返
回。
2）如果AXIMPROC读取burst数据，所有都不包含在
CACHE中，则往Flash产生命令，从Flash读取后返回数据；
3）如果AXIMPROC读取burst数据，部分在CACHE中，
部分不在CACHE中，按顺序返回数据，没在cache的就直接读
取 flash;
4）：AXIMPROC第一次读取数据，CACHE产生读取指令并
返回完数据后，自动增加地址，对Flash进行读取，i填满
CACHE空间；
5）AXIM_PROC后续发送的地址，正常情况下是和CACHE
中的首地址是一致的，则按1）处理即可；
5 fp



---
## 图像编号 25 (原图: `GameViewer_SnGFBV0cqH.png`)

### 【左页】

begin
if
((nrmrd_cmdfifo_empty==1'be&&efc_gclken==l"b1&&read_cmd_latl=read_cmd)
(ctrl_is_rd_p==1'bl
&& efc_gclken==1"b1&&read_cmd_lat!=read_cmd)
begin
read_nxtst
RD_ST_CHANGE;
elseif ((nrmrd_cmdfifo_empty)be &&efc_gclkenl"bl&&read_cmd_latread_cmd)
end
(ctrl_is_rd_p--1"bl
&& efc_gclken==1'bl&&read_cmd_lat==read_cmd)
begin
RD_ST_GETCMD;
read_nxtst
RIMCU manTi
end
else begin
read_nxtst
RD_ST_IDLE;
end
RDST_CHANGE
pua
begin
if
(cnt>=(12'de,maxs)
&&tmh_reached--1'b&& efc_gclken=1'b1)begin
read_nxtst
RD_ST_GETCMD;
end
else begin
read_nxtst
RD_ST_CHANGE;
pua
if
VREADI
begin
1'be;
end
else begin
lifixbug #25sbegin,makevreadpuli upwhen firstretry erase operation
//1r(readcurstamRD_ST_IDLE&&readnxtst/-RD_ST_IDLE)begin
if((cnd2flash_1f_a_Load-1"bl
l /apb access,axiwrite,axi read
(read_curst--RD_ST_IDLE6&read_nxtst!=RD_ST_IDLE)
begin
//fixbug
258end
VREADI
cnd2ftash_1f_vread;
else
end
end
end
RINCU
2、READMODE寄存分命令（包含写和擦除）：
assignefc_tck_gt_trc
ef9_efctcle_trcas
efc_ctk ernegedge ef_rst_n)begin
etc rst n
Tead cd Lan
elsebegin
reao_chd
但根据DATASHEET，只需要保证写和擦除时，Recall信号拉
低即可，NormalRead、VREAD1和写擦除交叉操作并不需要发


### 【右页】

生ReadMode切换：
PROG/PROG2
CONFEN
VREADI
RECALL
MODE
ERASE
ADDR
RETRY1
CHIP
PORb
DIN
CEb
DPD
Read
DOUT
AIN
DIN
AIN
Program
Sector Erase
AIN
Note
Chip Erase
Standby
All
Zero
Set Config
CBD
CBA
Deep Power Down
All
Zero
Power On Reset
All
Zero
Recall Read
AIN
DOUT
DOUT
AIN
Verify Read 1
Notes:
(1) X means either *oor'1', not other value.
(2) TMEN-I to enable test modes, In other cases, it should be 0.
(3) CBAisthe word numberofconfiguration data, usingAeo, CBD is the configuration data correspondingto the
CBA.
(4) ADDR column includes Address, NVR and NVR_CFG, and ARRDN pins.
(5) RETRYμsoj are '11' for single pulse sector erase, or changed regarding to retry order.
ET6601优化方案为：
IMCU
dan
13080F



---
## 原图：`GameViewer_Ts8jfg57vy.png`

### 【左页】

**表1-1 修订记录**

| 版本号 | 修订内容 | 修订日期 | 修订人员 |
|---|---|---|---|
| 1.0 | 从ET6003 EFC模块详细设计文档复制，参考ET6801进行修改 | 20260715 | 周玮玮 |
| 1.1 | 根据ET6601 OR-DR更新，新增64KX72=512KB的PFLASH，原有FLASH回退为DFLASH | 20260922 | 周玮玮 |

### 【右页】

# 目录

Contents

- 目录
- 图目录
- 表目录
- 第1章 概要设计
  - 1.1 功能框图
    - 1.1.2 Flash 结构框图
    - 1.1.3 时钟域说明
  - 1.2 接口列表和接口时序
  - 1.3 Safety Mechanism
- 第2章 详细设计
  - 2.1 EFC_CFG
  - 2.2 EFC_GFB

---

## 图像编号 27 (原图: `GameViewer_U3Lm9vj4H7.png`)

### 【左页】

CRG可以根据该信号，撤销CPU的复位，让CPU
开始进行Boot动作；
内部增加超时机制，超时后拉高；
cfg_efc_core_gate_en
输入
O：EFC未被门控；
1：EFC被门控，需避免总线被挂死；
APB总线
efe_pclk
输入
APB时钟
efc presetn
输入
APB复位信号，低电平有效
efc psel
输入
APB选择信号
efc penable
输入
APB使能信号
输入
efc_paddr[31:0]
APB地址信号
efc pwrite
输入
APB写指示信号
0：读操作；
1：写操作，
ZTMCIt
输入
efc_pwdata[31:0]
APB写数据
efe_prdata[31:0]
输出
APB读数据
efc pready
输出
APB准备好信号，高电平有效
efc pslverr
输出
APB错误信号，高电平有效
AI总线
efc aclk
输入
AXI时钟
efc_aresetn
输入
AXI复位，低电平有效
efc_awid[5:0]
输入
AXI写命令通道ID
efe_awaddr[31:0]
输入
AXI写地址
8IMCU
efc_awlen[3:0]
输入
AXI写burstlen
输入
efc _awsize[2:0]
AXI写数据宽度
efc_awburst[1:0]
输入
AXI写类型
efc_awvalid
输入
AXI写有效指示，高电平有效
efc_awready
输出
AXI写准备好指示，高电平有效
efc_awlock
输入
AXI锁
efc_awcache
输入
AXI cache
efc_awprot
输入
AXI保护
efc_ wid[5:0]
输入
AXI写数据通道ID
efe_wdata[63:0]
输入
AXI写数据
efc_wstrb[7:0]
输入
AXI写数据byte有效指示
efc_wlast
输入
AXI写last指示
efc_wvalid
输入
AXI写数据有效


### 【右页】

efc wready
输出
AXI写数据准备好指示，高电平有效
efc_bid[5:0]
输出
AXI反馈通道ID
efc_bresp[1:0]
输出
AXI反馈内容
efe_bvalid
输出
AXI反馈有效指示，高电平有效
efc bready
输入
AXI反馈准备好指示，高电平有效
efc_arid[5:0]
输入
AXI读命令通道ID
输入
efe_araddr[31:0]
AXI读地址
输入
efc_arlen[3:0]
AXI读burstlen
efc_arsize[2:0]
输入
AXI读数据宽度
efc_arburst[1:0]
输入
AXI读类型
efc arvalid
输入
AXI读有效指示，高电平有效
efc_arready
输出
AXI读准备好指示，高电平有效
输入
AXI锁
efc arlock
huem 11
输入
efc_arcache
AXI cache
efc_arprot
输入
AXI保护
efc_ rid[5:0]
输出
AXI读数据通道ID
efe_rdata[63:0]
输出
AXI读数据
efc rresp[1:0]
输出
AXI读数据反馈指示
efe_rlast
输出
AXI读数据last指示
efc_rvalid
输出
AXI读数据有效指示，高电平有效
efc_rready
输入
AXI读数据准备好指示，高电平有效
AXIGS相关信号
efc_awlock[1:0]
输入
外部可固定连接0
efc_awcache[3:0]
输入
外部可固定连接0
输入
efc_awprot[2:0]
外部可固定连接0
输入
外部可固定连接0
efc_arcache[3:0]
输入
外部可固定连接0
输入
efc arprot[2:0]
外部可固定连接0
Option输出
cfg _efc timing r[447:0]
输出
Flash使用的timing信息；
FINCU

**表1-2**

EFCPFLASH接口信号说明
时钟信号
输入输出
说明
输入
输入时钟，频率为25MHz~200MHz
12080F



---
## 原图：`GameViewer_V6W79lgJB6.png`

### 【左页】

# 参考文献

[1] 《ET6001 EFC 模块需求规格书》  
[2] 《Pegasus EFC 模块修改方案》  
[3] S40NEF64KX72_S0_Application_Notes.pdf  
[4] S40NEF64KX72_S0_Datasheet.pdf  
[5] ST_AN2606.pdf  
[6] STM32H7x3 参考手册.pdf  
[7] TMS320F28004x Real-Time Microcontrollers Technical Reference Manual

### 【右页】

（原图右页无正文内容。）

---

## 原图：`GameViewer_vC7gPIngZA.png`

### 【左页】

**图5-1 efc_clk和flash_clk时钟关系示意图**

> 图中可确认信号：efc_clk、flash_clk、efc_gclken、por_rst_n、efc_rst_n。复杂时序波形不自行重画。  
> 原图：`../images/GameViewer_vC7gPIngZA.png`

## 第6章 测试相关

| 测试点 | UT | SVA | IT | FPGA |
|---|---|---|---|---|
| 正常功能 | √ |  |  |  |
| 内部接口 |  | √ |  |  |
| 内部 FIFO |  |  |  |  |

> ⚠️ 原图待复核：测试矩阵在右页顶部仍有续表（可确认包含“连接关系”“性能”“BOOT”及勾选项），当前截图无法 100% 确认各勾选项所属列，因此不猜测。  
> 原图：`../images/GameViewer_vC7gPIngZA.png`

### 【右页】

为 FPGA 测试，编写 verilog 代码 eflash_fpga.v 用于模拟 eFlash 的功能行为（可综合）；那么 EFC 的整个功能都可得到测试，也可测试到 EFC 在系统中的行为（不可测试 eFlash 的时序，因为时序需要在 UT 测试保证）；

---

## 图像编号 30 (原图: `GameViewer_vOtMQKhCkV.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图 1-1`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 1-2`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 1-3 `，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图1-4...FLASHEFC模块内时钟域说明图`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-1 `，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图2-2`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图2-3`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-4`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-5`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-6`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-7`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-8`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-9`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-10`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-11`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-12`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

图目录
, 1i

**图 1-1**

EFC模块框图

**图 1-2**

S40FLASH结构框图

**图 1-3**

FlashPowerSwitch的连接关系图

**图1-4...FLASHEFC模块内时钟域说明图**

EFC CFG模块框图

**图 2-1**

ETCU uam 11

**图2-2**

EFC GFB模块框图

**图2-3**

GFBAXIM PROC模块框图

**图 2-4**

EFCPOWER状态转移图

**图 2-5**

EFCRESET状态转移图

**图 2-6**

GFB CTRL状态转移图

**图 2-7**

Cache状态转移图

**图 2-8**

EFC FCTRL模块框图

**图 2-9**

FlashPower状态转移图

**图 2-10**

FCTRL 状态转移图

**图 2-11**

Flash Write状态转移图

**图 2-12**

FlashSetConfig状态转移图


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图 2-13`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图2-14`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 2-15`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图2-16`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 3-1,`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 4-1,`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 4-2`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图 5-1...efc clk和 flash clk 时钟关系示意图`，完整结构与时序请查看原图 `GameViewer_vOtMQKhCkV.png`。


**图 2-13**

FlashErase状态转移图

**图2-14**

FlashRead状态转移图

**图 2-15**

ECC域段翻转写入图

**图2-16**

ECC域段翻转写入图

**图 3-1,**

ECC错误注入对应寄存器配置

**图 4-1,**

读数datapath示意图

**图 4-2**

写数datapath示意图

**图 5-1...efc clk和 flash clk 时钟关系示意图**

表目录

**表 1-1**

修订记录

**表 1-1.**

EFC接口信号说明

**表 2-1,**

EFC FCTRL 接口信号说明
532 I
2080F



---
## 原图：`GameViewer_vUFYITp5T4.png`

### 【左页】

# EFC 模块详细设计文档

设计：周玮玮  
评审：XXXXXXX

### 【右页】

批准：XXXXXXX
## 原图：`GameViewer_x2k55BuYBA.png`

## 第4章 系统评估

### 4.1 读性能评估

**图4-1 读数datapath示意图**

> 原图：`../images/GameViewer_x2k55BuYBA.png`

Cache 处为两级 pipeline 交互的点；

pipeline0，总线读取 Cache：

当数据连续访问时，latency=1 拍，且两次数据读取之间间隔 1cycle 的控制时间；

当数据不是连续时，根据不同的情况花费的时间会有区别。

pipeline1，Cache 到 Flash 读取数据，最少 1 拍发出一个读取申请，latency=2+3*Len+1+1=4+3*Len；

因此最终瓶颈体现在 Flash，正常情况下，可以得到 Flash 的满带宽性能（数据跳着访问的除外，可能还会因为 Flash 多读取数据，导致整体效率变差。当然，平均的 latency 会变小）；

---

## 图像编号 33 (原图: `GameViewer_xLTLahbgSa.png`)

### 【左页】

在ET6001 的基础上，完善了nvr、main sector的读写保护；
flashsector14的读、写/擦除保护并没有放到ROM/OTP中，
避免形成自锁；其读、写/擦除保护以带密码操作流程的方式
配置寄存器实现；
1、通过上电读取 NVR OB Sector 的 flash_main_wrp_n 和
testcode，MAIN保护区域自动屏蔽擦除操作，并且返回
CMD ERR;
2、 通过上电读取 NVR OB Sector 的 flash_nvr_wrp/rdp_n 和
test_code，NVRRSV保护区域自动屏蔽读写擦除操作，并且
返回 CMD_ERR;
3、通过上电读取 NVR USER OTP Sector 的 flash_nvr_otp_n,
用户OTP保护区域自动屏蔽擦除操作，并且返回
CMD ERR;
4、通过上电读取 NVR OTP Sector 的 flash_otp_gen_n，ROM
保护区域自动屏蔽写擦除操作，并且返回CMDERR，读访
问，受寄存器rom_rd_en控制；
5、通过上电读取 NVR OTP Sector 的 flash_otp_gen_n,OTP
保护区域自动屏蔽擦除操作，并且返回CMDERR，读写访


### 【右页】

问，受寄存器sysc_boot_exit lockj控制；
6、通过上电读取 NVR OTP Sector 的 nvr_cfg unlock，
NVRCFG区域自动屏蔽读写擦除操作，并且返回
CMD ERR;
7、21 通过上电读取 NVR ROM Sector 的 test code，RDN 区域
自动屏蔽读写擦除操作，并且返回CMD_ERR；
BTHCUan.J32026

#### 2.2.5.1只受bootrom访问说明

1.flash的全片擦除（main+RDN+NVR）触发擦除（flash
main+RDN+NVR-除 NVR sector0~3)，依次擦除:
1)flash main+RDN;
2)flash USER OPTION BYTES (nvr sector8)
3)flash USER OTP(nvr sector9~13) ;
4)flash OPTION BYTES (nvr sector 7、14、6);
5) flash OTP(nvr sector 4~5、nvr sector15);
a)命令格式：Mindcmd_subtype[23:20]=='h5,indcmd_ sub-
type[19:16]=='h2, indcmd_subtype[15:0]=='hAA55;
b）该命令保护寄存器受寄存器 sysc_boot_exit_lockj控制，该
4fp



---
## 图像编号 34 (原图: `GameViewer_xS9sUaBAU3.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图2-14FlashRead状态转移图`，完整结构与时序请查看原图 `GameViewer_xS9sUaBAU3.png`。

O1D μmpteRD_St_OuE
.Ti
RIMCU manz Ti

**图2-14FlashRead状态转移图**

FlashMainNormalRead时序优化方案见：
数字设计/03
/ET6601-DOC/05.
HAC/03
方案
LRS/EFC/V100/03.设计/02.LLD/《FLASH读时序分析.xlsx》
将读采样修改为efc_clk，提高读效率
心美86.630.5
efs_el
ETHCU Truan. 1i


### 【右页】

87Icu
FLASH读模式切换tMH/tMS时间优化：
tMS
Read Modes: RECALL/VREAD1 read (CLOCK rising edge @RDEN=1)
setup time
US
MH
Read Modes: RECALL/VREAD1 read (CLOCK rising edge @RDEN=1)
holdtime
a.132026-10-02-2139
工规FLASHMARCO一共三种读模式NormalRead、Recall
Read、Vreadl。
ET6601方案中存在以下问题：
1、ET6001、ET6601为了满足READMODE的RDEN使能后
的HOLD时序tMH，三种读模式在每次进行最后一个读操作之
后都进行了等待，降低了连续读的性能；
ETMCV
155 n
080F


## 原图：`GameViewer_Yg5PctElzk.png`

### 【左页】

# 目录（续）

- 2.2.1 GFB_AXIM_PROC
- 2.2.2 GFB_POWER_PROC
- 2.2.3 GFB_CFG_PROC
- 2.2.4 GFB_CTRL
- 2.2.5 GFB_IF
- 2.2.6 NVR_EFUSE_PROC
- 2.2.7 EFC_EFUSE_PPROC_ARB
- 2.2.8 EFC_CFG_PROT_PROC
- 2.3 EFC_FCTRL
  - 2.3.2 接口列表
  - 2.3.3 FCTRL_POWER_PROC
  - 2.3.4 FCTRL_GFB_CMD_IF
  - 2.3.5 FCTRL_GFB_FLASH_IF
- 第3章 DFX说明
  - 3.1 错误说明
  - 3.2 DFX设计
- 第4章 系统评估
  - 4.1 读性能评估
  - 4.2 写性能评估
  - 4.3 擦除性能评估

### 【右页】

# 参考文献

---

## 图像编号 36 (原图: `GameViewer_zQvGQlgTkE.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图2-8EFCFCTRL模块框图`，完整结构与时序请查看原图 `GameViewer_zQvGQlgTkE.png`。


#### 2.3 EFC FCTRL

该子模块是eFlash控制部分，连接SoC侧控制部分和eFlash，
其工作频率为25MHz~200MHz；本项目在系统启动过程中，可
能涉及到的工作频率分别为25MHz、200MHz;
EFC_FCTRL
CRG
FLASI
EFC_CFG

**图2-8EFCFCTRL模块框图**

该模块功能框图，主要功能模块概述；
FCTRL_POWER_PROC：根据电源和配置 DPD 进行Flash
Power状态跳转；
FCTRL_GFB _CMD_IF：从 GFB 接口分解出对应的 CMD 指
令和数据信息，来启动状态机的跳转；
FCTRL GFB FLASH IF：根据GFB CMD IF 接收的状态,
适配FLASH时序进行FLASH操作；


### 【右页】


#### 2.3.2接口列表


**表2-1EFCFCTRL接口信号说明**

信号
输入输
说明
efc_clk
输入
输入时钟，频率为25MHZ~100MHz
efc rst n
输入
输入复位信号，低电平有效
电源相关
输入
por_rst_n
硬件复位信号，低电平有效；
复位表示Flash电源关闭，由系统提供；
该复位有效时，efc rst n必然有效；
cfg_efc_dpd_r
输入
0：flashDPD模式关闭；
1：flashDPD模式打开；
TMCV han J3 2026-10-02-21-39
配置接口
详细参见《efc_cfg_dflash_nmanager》《efc_cfg_pflash_nmanager》
GFB接（GeneralFunctionBus）
gfb2fctrl_cmd_vld
输入
EFC发送的命令有效，高电平有效
gfb2fctrl_cmd[FLASH_DW-1:0]
输入
EFC发送的命令；
when cmd --
[15:0] -- A
[19:16] -- Type: Write, SecErase,
ChipErase, Read, SetConfig.
RECALL,VREAD,RETRY
[23:20] -- SubType: NVR_CFG, NVR,
Redundancy, Main / Main Array, All Main
Array + All Redundancy, All Main Array +
All Redundancy + All NVR
[27:24] - Len_m1
[71:28] -- reserved;
[72] 1'bo /means CMD
when wdata --
TMCV
[63:0] -- Wdata
[71:64] EccData
[72] - 1'b1 /means DATA
gfb2fctrl_cmd_rdy
输出
EFC命令反压信号，高电平有效
160 {
12080F

---

## 第二部分：截图明确标注的 ET6601 修改点

### Flash Main Normal Read 读采样优化

- **原始文字**：Flash Main Normal Read时序优化方案见：`/ET6601-DOC/05.数字设计/03 HAC/03 方案 LRS/EFC/V100/03.设计/02.LLD/《FLASH读时序分析.xlsx》`；将读采样修改为efc_clk，提高读效率
- **所在位置**：图2-14 Flash Read状态转移图之后
- **原图**：`../images/GameViewer_xS9sUaBAU3.png`
- **修改性质**：原图红字明确给出的 ET6601 读时序优化

### READ MODE 的 tMH/tMS 优化问题

- **原始文字**：ET6601方案中存在以下问题：1、ET6001、ET6601为了满足READMODE的RDEN使能后的HOLD时序tMH，三种读模式在每次进行最后一个读操作之后都进行了等待，降低了连续读的性能；
- **所在位置**：FLASH读模式切换tMH/tMS时间优化
- **原图**：`../images/GameViewer_xS9sUaBAU3.png`
- **修改性质**：原图明确点名 ET6601 方案存在的问题

### ET6601 READ MODE 优化方案

> 该组修改从“ET6601优化方案为：”开始，内容跨连续页面。

1. **原始文字**：ET6601中优化为只有Recall Read需要等待tMH，Normal Read、Vread1不等待，提升Normal Read、Vread1效率；
   - **原图**：`../images/GameViewer_isM3FELYfq.png`
2. **原始文字**：VREAD1在RETRY ERASE操作中提前拉高，在非RETRY ERASE和PROGRAM中保持不变，按照之前代码可能会出现Normal Read的tMH等待时间不够的违例，因此将VREAD1拉高时间修改为tNVS之后；
   - **原图**：`../images/GameViewer_isM3FELYfq.png`
3. **原始文字**：进入Program、ERASE时都将Recall拉低；（与ET6601方案保持一致）
   - **原图**：`../images/GameViewer_isM3FELYfq.png`
4. **原始文字**：进入READ模式时，只根据VREAD1和Recall信号的变化记录的READ MODE来决定是否要等待tMS，而不是每次ERASE/PROGRAM都认为READ MODE发生过变化；
   - **原图**：`../images/GameViewer_isM3FELYfq.png`

- **所在位置**：FCTRL_GFB_FLASH_IF 前的 READ MODE 优化说明；前一页以“ET6601优化方案为：”引出
- **关联原图**：`../images/GameViewer_SnGFBV0cqH.png`、`../images/GameViewer_isM3FELYfq.png`
- **修改性质**：截图红字明确给出的 ET6601 优化方案

### 修订记录 1.1

- **原始文字**：根据ET6601 OR-DR更新，新增64KX72=512KB的PFLASH，原有FLASH回退为DFLASH
- **所在位置**：表1-1 修订记录，版本 1.1
- **修订日期**：20260922
- **修订人员**：周玮玮
- **原图**：`../images/GameViewer_Ts8jfg57vy.png`
- **修改性质**：原图修订记录明确标注的 ET6601 更新
