# EFC 模块 LRS 设计文档

> 本文档由大模型逐图逐页提取自原始截图，不作主观修饰，忠实还原原文。
> 图表、时序波形及模糊部分均标注对应截图原图文件名供查阅。


---
## 图像编号 1 (原图: `GameViewer_5UxkiNGtxh.png`)

### 【左页】

5.DFLASHnvr空间（nvrsector8）受rdp、wrp保护，可修改，
上电后自动生效；
6.DFLASH用户OTP空间（nvrsector9~13）受rdp、Wrp保护，
变成OTP后，擦除DFLASHnvrsector14，可恢复为无保护
DFLASH nvr sector;
7.DFLASHOB空间（nvrsector14）受rdp、wrp保护，通过密
码+流程配置寄存器修改并直接生效；
8.DFLASHmain空间，受rdp、wrp保护，可修改，上电后自
动生效；
9.PFLASHmain空间，不受rdp保护；受wrp保护，以整片为
单位;
ETMCV

#### 1.2.10.2 OTP需求

名称
作用
sector
dflash的8个空间（以16个sector为单位）的读保护
标识
1"b0：打开读保护，数据不能被读取；
1"b1：关闭读保护，数据能被读取；
注：TEST_CODEI=O时不做保护
ETMOI
dflash_main_wrp_n[7:0]
dflash的8个空间（以16个sector为单位）的写保护
标识
1"b0：打开写/擦除保护，数据不能被修改；
1"b1：关闭写/除保护，数据可以被修改；


### 【右页】

注：TEST_CODE!=O时不做保护
[0
dflash的nvrsector8的读保护标识，
1"bo：打开读保护，数据不能被读取；
1'b1：关闭读保护，数据能被读取：
注：TEST_CODEI=D时不做保护
dflash的8个nvrsector8的写/擦除保护标识；
1'b0：打开写/擦除保护，数据不能被修改；
1'b1：关闭写/擦除保护，数据可以被修改：
注：TEST_CODEI=O时不做保护
dflash的mvr空间的5个sector确认变成用户otp
dflash_mvr_otp_n[7:0][4:0]
0x0：变为otp，数据不能被擦除，可将1写为0；
其他：正常nvr，数据能被写/禁除；
0~4分别表示sector9~13
dflashnvr空间的7个sector确认变成otp
dflash_otp_gen_n[7:0][6:0]
TMCUh/an.J1
0x0：变为otp，数据不能被擦除，可将1写为0；
其他：正常nvr，数据能被写/擦除；
0~5分别表示sectoro~5，6表示sector15
otp的读/写保护，由bootrom配置只写1的寄存器实
现；
otp的擦除保护，由bootrom配置只写1的寄存器实
现；
FLASHnvr_cig空间的读/写/擦除保护
nvrcfg_unlock[7:0]
TMCUan11 2026-10-02-21:
0x0：打开保护，数据不能被读/写/擦除；
其他：关闭保护，数据能誠读/写/擦除；
chip_ers_key[31:0]
整芯片擦除 key

#### 1.2.10.3读保护（RDP）和写保护(WRP)

FLASHNVR通过配置NVRprot实现NVR空间读写保护，避
dan
免在软件被恶意攻击或者注入的时候，恶意串改NVR内容。



---
## 原图：`GameViewer_6F5qGwog2V.png`

### 【左页】

**图1-6 芯片Boot流程图**

> 时序图参与者可确认：电源管理、CRG、EFC、CPU、BootRom。复杂时序图不自行重画。  
> 原图：`../images/GameViewer_6F5qGwog2V.png`

### 【右页】

### 1.2.6 Wafer Testing

1）Wafeter Testing，详见 SMIC 交付的 BIST 文档；  
2）LCK_CFG 信号在 TEST_EN 为 0 时，即为 1；  
3）正常工作；

参见 ET6601-DOC/05.数字设计/03 HAC/03 方案  
LRS/EFC/V100/03.设计/01.LRS/《FLASH 读写擦除保护.xlsx》

### 1.2.7 地址空间说明

| FLASH | 空间 | sector | 说明 |
|---|---|---|---|
| PFLASH | NVR_CFG | 0 | FLASH 相关信息，SMIC 提供 |
|  | NVR | 0~15 | 无用途 |
|  | Main+RDN | 0~511 | 程序数据 |
| DFLASH | NVR_CFG | 0 | FLASH 相关信息，SMIC 提供 |
|  | NVR | 0~1 | ROM 空间，共 4KB |
|  |  | 2、7 | OTP 空间 |
|  |  | 3、4、6 | OPTION BYTES 空间 |
|  |  | 5 | OPTION BYTES 用户空间，供用户使用 |

---

## 图像编号 3 (原图: `GameViewer_7Jsq6PhQM2.png`)

### 【左页】

LRS.EFC.FUNC.SEC【07】非 BOOTROM发起的所有OTP的
擦除操作都会被屏蔽；
LRS.EFC.FUNC.SEC【08】支持写OTP时通过key来验证写
权限，key验证通过后，才可以进行写操作；
LRS.EFC.FUNC.SEC【09】NVR FLASH 会输 出 32bit
TEST_CODE。TEST_CODE不为O的时候，默认所有芯片限权
/鉴权手段均不生效。
LRS.EFC.FUNC.SEC【1O】支持OTP空间信息防泄露功能，
禁止外部访问和修改；
LRS.EFC.FUNC.SEC【11】支持FLASH初始化结束指示输出
管脚用于CP测试控制使用，在任何非DFT模式下都需要确保
FLASH初始化结束指示能拉高，以保证安全启动；
LRS.EFC.FUNC.SEC【12】安全应用阶段提供3个sector的
OTP空间，芯片内部根据烧录情况使用对应空间作为OTP使用；
LRS.EFC.FUNC.SEC【13】FLASH读写保护：
1.dflashROM空间（nvrsector0~3）由DFLASH OTP GEN定
义，变成ROM后，仅BOOTROM可读，禁止写和擦除，芯
片回收才会修改；


### 【右页】

2.dflash OTP空间（nvr'sector 4~5，nvr sector15 ）由
DFLASH OTPGEN定义，变成OTP后，仅BOOTROM可
读可写，禁止擦除，芯片回收才会修改；BTICL
3.dflashOPTIONBYTES空间（nvrsector6）仅BOOTROM可
读可写可擦除，上电后自动生效，（nvrsector7）当
secure_level等于2'd2/2'd3时，用户可仅读，当securelevel
等于2'do/2'dl时，用户可读可写可擦除，（nvrsector14），
仅BOOTROM可写可擦除，用户可读，上电后自动生效；
4.dflash USER OPTION BYTES 空间（nvr sector8）受 rdp、wrp
保护，可修改，上电后自动生效；
5.dflash
用户OTP 2空间（nvr²sector9~13）由
USER_NVR_OTP_GEN_N 定义，变成OTP 后，"禁止擦除，
上电后自动生效；
6.dflashnvr空间（nvrsectorl4）受rdp、wrp保护，通过密码
+流程配置寄存器修改并直接生效；
7.pflashdflashNVR_CFG空间受nvr_cfg_unlock保护，保护锁
定后，禁止读写擦除，芯片回收才会修改；
8.dflashmain空间，受rdp、wrp保护，以sector/16KB为单位，



---
## 图像编号 4 (原图: `GameViewer_BG11R4KzQV.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图1-72个Flash地址空间说明`，完整结构与时序请查看原图 `GameViewer_BG11R4KzQV.png`。

> 📌 **【图表提示】**: 此处包含图表 `图1-8数据读操作流程（NVRCFG，NVR）`，完整结构与时序请查看原图 `GameViewer_BG11R4KzQV.png`。

Main+RDN
0~127
用户数据

**图1-72个Flash地址空间说明**

ETMCU huas, li

#### 1.2.8正常工作启动和结束（包含上报内容）

数据读操作（NVR_CFG，NVR）
配置master
FC
BTMCU man,
适过不网bit来表示：
MVR_CFG(wafertesting价段/上电阶段)。
NVR（上电阶投/EFC复位/正常阶段）
读NVR_CFG/MVR对应地址
对Flash进行读操作
状态机进入IDLE
反馈读国数据
DLE
ETMC han, 71 202F-10-02-77:4
等待EFC重新启用
配置master
EFC

**图1-8数据读操作流程（NVRCFG，NVR）**

对图中“配置master”的说明：
Waftertesting阶段：配置master为测试接口；
ETMOU
上电阶段：配置master为EFC_GFB中的电源管理部分；
EFC复位：表示只对EFC进行复位，对Flash没有断电。配


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图1-9数据写操作流程（NVR_CFG，NVR，Config Register）`，完整结构与时序请查看原图 `GameViewer_BG11R4KzQV.png`。

置master也为EFC_GFB中的电源管理部分;
正常阶段：配置master为系统CPU;
ETMO
ETHCU
NVR、NVR_CFG读取，需要进行间接寻址，避免总线ready
拉低挂住系统；
数据写操作
(NVR_CFG， NVR， Config Register)
配置master
EFC
遇过不网来表示
MVR_CFG(wafertesting价R/上电价起),
MR(上电阶段/正常价段）
ConfigRegister(上电视),
写NVR_CFG/Config RegisteniNVR对应地址
对Flash进行写接作
根弱配置写换作时间，状志机进入IDLE
JOLE
等特EFC蛋新启用
EFC
配置master

**图1-9数据写操作流程（NVR_CFG，NVR，Config Register）**

Waftertesting阶段：配置master为测试接口；
2026-10-02-21;47
上电阶段：配置master为EFCGFB中的电源管理部分；
正常阶段：配置master为系统CPU;
2080F



---
## 图像编号 5 (原图: `GameViewer_BiWjxKhdcj.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图1-18Main写保护流程`，完整结构与时序请查看原图 `GameViewer_BiWjxKhdcj.png`。

3）寄存器cfg_efc_nvr_wrprot_flg标记清零；（如果步骤2配
置错误，则lock标记不清零，后续动作也不会成功；如果操作
步骤不正确，会在下一次系统复位前锁定
cfg_efc_nvr_wrprot_flg，并返回总线错误）
4）软件启动写/擦除指令；
5）操作完成后，将cfg_efc_nvr_wrprot_flg寄存器配置为l;
efuse为NVR中的一部分，当前版本中不进行额外保护；

#### 1.2.9.4MainArray写保护

咨存器写操作
一确认寄存器写保护
一打开或关闲对应扇区写保护
软件配置寄存器
一每个扇区可独立管理
ETMCV hinan. i 2026-10
致件启动写操作推除操作
硬件check写/排降征含地址是否受保护
（根据配置寄存器的写保护配置）
硬件上报中断
(完成和写保护插递）
nan.11

**图1-18Main写保护流程**

ETMOI
1）软件启动写/擦除指令；


### 【右页】

2）硬件check写/擦除指令对应地址是否在保护扇区内（根据
配置寄存器里面的内容1打开或关闭对应扇区写保护，每个
sector可独立管理--flash可管理，pflahs不可管理），如果不被
保护则正常执行；如果被保护则不执行，并反馈a）完成；b)
上报写保护错误；

#### 1.2.10FLASHNVR地址空间划分与读写保护

参见ET6601-DOC/05.数字设计/03HAC/03
方案
LRS/EFC/V100/03.设计/01.LRS/《FLASH读写擦除保护.xlsx》

#### 1.2.10.1架构和功能

1.DFLASHROM空间（nvr sectoro-3）受rdp、wrp保护，变
成ROM后，芯片回收才会修改；
2.DFLASHOTP空间（nvr sector4、5，nvr sector15）受rdp、
wrp保护，变成OTP后，芯片回收才会修改；
3.DFLASHNVRCFG空间受lock保护，lock之后，芯片回收
才会修改；
4.DFLASHOB空间（nvrsector6、7）受rdp、wrp保护，可修
改，上电后自动生效；



---
## 原图：`GameViewer_BMgqvo1P0z.png`

### 【左页】

LRS.EFC.LIMIT.SPEC【07】：Flash 限制：不允许对同一个 flash 地址重复编程数据 ‘0’；

LRS.EFC.LIMIT.SPEC【08】：Flash DPD 限制：需要保证进入 DPD 模式时（配置 DPD 使能），AXI/APB 总线对 FLASH 无操作，并且已经发起的操作已结束，否则可能导致 AXI 总线超时，APB 间接命令一直 BUSY；

### 2.5 触发源说明

无。

### 【右页】

# 参考文献

[1] S40NEF64KX72_S0_Application_Notes.pdf  
[2] S40NEF64KX72_S0_Datasheet.pdf  
[3] ST_AN2606.pdf  
[4] STM32H7x3 参考手册.pdf  
[5] TMS320F28004x Real-Time Microcontrollers Technical Reference Manual

---

## 图像编号 9 (原图: `GameViewer_cQ0Ir7RHZa.png`)

### 【左页】

8bitECC，ECC可以纠正1bit错误，检测2bit及以上错误（即对
64bit数据做ECC，得到8bit的纠错数据。当数据进行非64bit操
作时-参见 LRS.EFC.SOC【08]，不使能ECC);
1）ECC出现1bit错误时，记录历史告警寄存器；
2）ECC出现2bit不可纠，上报中断；
3）ECC出现2bit不可纠，送入fault管理，同时可用于封波；
开启ECC和ECCWRRVS时，对于写入的ECC8bit内容的
第0、1、4-7bit进行取反，保证写数据为全1时，ECC计算结果
8"hC进行处理后也为8"hFF（全1），此时不会对FLASH内容进
行改写；
开启 ECC 和 ECC RD RVS 时，对于读出的 ECC 8bit 内容的
第0、1、4-7bit进行取反，保证ECC校验时ECC数据为写入前
未取反的数据。
MAIN/NVR/NVR_CFGECC使能配置均默认开启并且禁止配
置为关闭。
LRS.EFC.FUNC.SOC【10】PFLASH、DFLASH支持被DMA
直接访问；


### 【右页】

络环境，以改善远程控制体验。

#### 2.1.4 LRS.EFC.SEC

本次远程不再提醒
知道了
LRS.EFC.FUNC.SEC【O1】支持DFLASHNVR空间模拟OTP，
OTP空间大小为3个sector（3KB）；
LRS.EFC.FUNC.SEC【02】支持DFLASHOTP区域安全访问
机制;
LRS.EFC.FUNC.SEC03】支持DFLASHNVR空间模拟ROM,
ROM空间大小为4个 sector（4KB）；
LRS.EFC.FUNC.SEC【04】支持 PFLASH、DFLASH main 区
域安全访问机制；
LRS.EFC.FUNC.SEC【05】支持DFLASH上电复位释放后，
硬件自动使需要加载的OTP、ROM信息生效（包括AES、CPLD
和CPU使能），而需要加载的OPTIONS（包含secure_level）
需要在上电复位或硬复位释放后，都进行硬件自动生效；
支持上述硬件自动加载涉及到启动模式、安全等级和信息安
全的域段采用多bit域段多数判决进行校正保护，并且输出校正
后的域段值；
LRS.EFC.FUNC.SEC【06】安全级别只能由应用程序通过写
OTP的方式由低向高配置，由高向低配置会被屏蔽；
1 fp



---
## 图像编号 10 (原图: `GameViewer_cSaHi20ulN.png`)

### 【左页】

i.写入 cfg_efc_reg_keyl = 0x0123CDEF；-- flash
ii. 写入 cfg_efc_reg_key2 =0x89AB4567；--flash
2）寄存器cfg_efc_reg_wrprot_flg标记清零；（如果步骤2配
置错误，则lock标记不清零，后续动作也不会成功；如果操作
步骤不正确，会在下一次系统复位前锁定
cfg_efc_reg_wrprot_flg，并返回总线错误）
3）软件配置寄存器；
4）软件寄存器配置完成后，将cfg_efc_reg_wrprot_flg寄存器
配置为1；

#### 1.2.9.2NVR CFG 写保护

在CP测试过程中，可以对该区域进行读写访问；
LCKCFG在CP测试后即拉高，用户在使用过程中无法进行
读写；
实现中使用 nvrcfg_unlock==8"h00 做为LCK_CFG;
ETMOI


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图1-17NVR写保护流程`，完整结构与时序请查看原图 `GameViewer_cSaHi20ulN.png`。

NVR写保护
模处复位后，
释先疾行fgregprotag倍存静清程
orot_fig需存器款以为1
ETMCU hvan. 11
素性dfg_efc_nvr_key1 NVR_KEYI
&作dg_efc_mvr_key2 - NVR_KEY2-
并将cfg_n_arprot_fig量新配照力1
款件确认作完成
ETNCU muan.J1

**图1-17NVR写保护流程**

1）模块复位后，cfg_efc_nvr_wrprot_flg寄存器默认为1;
2）软件按顺序写cfg_efc_nvr_keyl、cfg_efc_nvr_key2寄存
器;
i.写入 cfg_efc_nvr_keyl= 0x45670123；--pflash
ii. 写入 cfg_efc_nvr_key2 = 0xCDEF89AB；--pflash
i.写入 cfg_efc_nvr_keyl=0xCDEF0123；--flash
ii.写入 cfg_efc_nvr_key2 = 0x456789AB；--flash
2080F



---
## 原图：`GameViewer_fpb2HKWthL.png`

### 【左页】

**表1-1 修订记录**

| 版本号 | 修订内容 | 修订日期 | 修订人员 |
|---|---|---|---|
| 1.0 | 从ET6003拷贝，参考ET6801 EFC LRS和ET6601 OR-DR修改刷新 | 20260715 | 周玮玮 |
| 1.1 | 根据ET6601 OR-DR更新，新增64KX72=512KB的PFLASH，原有FLASH回退为DFLASH | 20260920 | 周玮玮 |

### 【右页】

# 目录

Contents

- 目录
- 图目录
- 表目录
- 第1章 模块介绍
  - 1.1 模块简介
  - 1.2 应用说明
    - 1.2.1 Power On
    - 1.2.2 Power Off
    - 1.2.3 模块软复位
    - 1.2.4 模块门控
    - 1.2.5 芯片系统启动
    - 1.2.6 数据预取
    - 1.2.7 Wafer Testing

---

## 图像编号 12 (原图: `GameViewer_gLi3yEXagB.png`)

### 【左页】

挂死--若CPU读该模块（非配置寄存器），则返回为无效的0值，
且resp 返回ERR；若CPU操作该模块，则该操作被屏蔽，且
resp 返回 ERR;
LRS.EFC.RBST【03】：模块从正常功能切到软复位或
ClockGate模式，数据接口访问未完成时，按LRS.EFC.RBST
【01、02】方式处理；
STNCU

#### 2.2 中断管理

LRS.EFC.INTR.SPEC【O1】：功能完成，触发中断;
LRS.EFC.INTR.SPEC【02】：错误产生，触发中断；错误类型
参考LRS.EFC.DFX【02】；BTMC)

#### 2.3事件管理

无。
87MC) ;4)
ETMCU man. li

#### 2.4约束说明



### 【右页】

LRS.EFC.LIMIT.SPEC【O1】：对该模块配置为ClockGate 模
式时，只能关闭内部工作时钟，接口时钟必须常开，否则可能导
致接口总线挂死；
LRS.EFC.LIMIT.SPEC【02】：对该模块配置为ClockGate模
式时，若CPU读该模块（非配置寄存器），则返回为无效的0值；
若CPU操作该模块，则该操作被屏蔽；
LRS.EFC.LIMIT.SPEC【03】：该模块软复位过程中，若CPU
读该模块（非配置寄存器），则返回为无效的0值；若CPU操作
该模块，则该操作被屏蔽；
LRS.EFC.LIMIT.SPEC【O4】：模块从软复位或ClockGate模
式切到正常功能时，CPU需等待模块idle状态才能开始正常命
令的工作；否则模块的处理方式和仍然在软复位或Clock_Gate
模式的过程中一样；
LRS.EFC.LIMIT.SPEC【05】：在Flash工作过程中，不能变换
bit操作位宽（64bit与非64bit之间），否则可能导致一直上报
ECC错误，并且建议一直开启MAIN/NVR/NVR_CFG的ECC使
能，只进行64bit的写操作（否则可能导致一直上报ECC错误），
防止出现单bit失效无法校验；
LRS.EFC.LIMIT.SPEC【06】：总线不支持跨4Kbyte;



---
## 图像编号 13 (原图: `GameViewer_gYLpTulBVN.png`)

### 【左页】


#### 2.1.3 LRS.EFC.SOC

LRS.EFC.SOC【O1】：外部控制功能包含：IDLE、READ、
VREAD、WRITE、ROWWRITE、NORMALSECTORERASE、
RETRYSECTORERASE、CHIPERASE、低功耗（模块时钟门
控、Flash DPD 功能);
其中VREAD支持：
1）APB接口支持VREAD检查FLASH地址数据是否为全1
（是否擦除成功），并且返回检查结果进行上报；
2）通过配置使AXI、APB接口的FLASH读操作切换为
VREAD 读;
LRS.EFC.SOC02】支持PFLASH双BANK地址映射,PFLASH
Main区域共计512KB，AXI总线访问PFLASH内部地址划分
为:
BANK0:0x000000-0x03FFFF
BANK1:0x040000-0x07FFFF
根据SYSCSWAP配置交换两块BANK的读写访问地址；
APB间接命令读写擦除访问不做交换；
LRS.EFC.SOC【03】：配置接口APB3.0：地址位宽12bit、数


### 【右页】

据位宽32bit;
LRS.EFC.SOC【04]:数据接口AXI4.0，一个 PFLASH、一
个DFLASH分别独立使用一个AXI接口，支持并行操作，即分
别对一个PFLASH和一个DFLASH的MainArray和开启替换的
RDN区域执行读取、编程操作，地址位宽32、数据位宽64、最
大BurstLen为16、读写ID位宽 6bit、burst类型（只支持INCR1~16,
WRAP 4/8且非 narrow）、outstanding（最大3)、narrow、resp、
wstrb;
LRS.EFC.SOC【05】：支持中断（高电平）产生：外部控制功
能（LRS.EFC.SOC【06】）完成中断、错误中断;
LRS.EFC.SOC【06】：与CPU交互方式：寄存器配置，中断；
LRS.EFC.SOC【07】：支持紧急撤销（由软件管理，硬件不做
额外逻辑）；
LRS.EFC.SOC【08】：数据侧支持Byte操作（即数据总线Wstrb
功能);
FLASH支持双字、字、半字和字节进行读操作；
FLASH支持双字、字、半字和字节进行编程操作；
LRS.EFC.SOC【09】支持PFLASH、DFLASH
数据对应
2fp



---
## 图像编号 14 (原图: `GameViewer_jyfWngVZvO.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图1-1Flashpoweron流程图`，完整结构与时序请查看原图 `GameViewer_jyfWngVZvO.png`。


#### 1.2.1 Power On

Flash
CRG
电源管理
EFC
wait tRT
产生PORb
.por.rst.n.
.flash.por.rst.n.
执行POWER-ON过程，
使用default时中频率(25MHz)
1）读NVR_CFG
2) set config register,
3）读取NVROPTIONBYTES城股
rdn高存器更新
4）更新OPTIONBYTES寄存器
5）输出invr_shiftdone高电平
6）读取NVROTP域段
7）更新OTP寄存器
8）输出otp_shiftdone高电平
.Flash.上电洁康(efc.otp.readyefc.option.ready&otp.shiftdone)
Flash
CRG
电源管理
EFC

**图1-1Flashpoweron流程图**

实现：
1.子模块S40_FCTRL需要实现POWER-ON时序；
2.EFCGFB子模块需要实现（通过控制S40FCTRL）：
1)读取 NVR_CFG;
2) Set config register;
RDN寄存器更新；


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图1-2Flashpoweroff流程图`，完整结构与时序请查看原图 `GameViewer_jyfWngVZvO.png`。

3）读取NVROPTION BYTES 域段（DFLASH）；
4)输出nvr_shift_done高电平；
5）更新OPTION BYTES寄存器（DFLASH）；
6)读取NVROTP域段（DFLASH);
7）更新OTP寄存器（DFLASH）；
8)输出 otp_shift_done高电平（DFLASH)。

#### 1.2.2 Power Off

TMCU hoan 1i
CRG
EFC
电源管理
Flash
软件根据应用场景
确定掉电的时间点
再配置电源管理断电
产生PORb=0
ETMCUTman.12028-10-02-21:
por_rst_n=0
.porrst n=0
根据CRG的设计进行延时
拉低VDD/VDD11.掉电
;47
电源管理
CRG
EFC
Flash

**图1-2Flashpoweroff流程图**

（正常掉电）
2D26-10-02-21:47
2080F



---
## 图像编号 15 (原图: `GameViewer_LLELUTfGM7.png`)

### 【左页】

可修改，上电后自动生效；
对AXI总线访问MAIN空间读写保护区域，自动屏蔽写操
ETMCO
作，读操作数据返回全0,并且根据配置使能决定是否返回
总线错误；
对APB总线对于MAIN空间读取保护区域的擦除命令，自
动屏蔽擦除操作，并且返回CMD ERR;
9.pflashmain空间，不受rdp保护；受wrp保护，以sector/32KB
为单位；
LRS.EFC.FUNC.SEC【14】BOOTROM发起的DFLASH的全
片擦除（main+RDN+NVR）触发整芯片擦除，依次擦除：
1)pflashmain+RDN；（包含软件直接下发PFLASHmain+RDN
擦除命令);
2)dflash main+RDN;
3)dflash USER OPTION BYTES (nvr sector8) ;
4)dflash USER OTP (nvr sector9~13)0;
5)flash OPTION BYTES (nvr sector 7、14、6);
BTMCU han.
6)flash OTP(nvr sector 4~5、 nvr sector15);
LRS.EFC.FUNC.SEC【15】支持PFLASH和DFLASH


### 【右页】

redundancy功能，最多可替换两个MainSector;
LRS.EFC.FUNC.SECa【16】DFLASH支持5KBUSEROTP空
间（NVRsector9~13);

#### 2.1.5 LRS.EFC.FLASH

LRS.EFC.FLASH【O1】：支持读操作：MainArrayRead、NVR
Read、NVR CFG Read、Redundancy Read、Recall Read、Verify
Read;
LRS.EFC.FLASH【02】：支持写操作：Main Array Program、
NVR Sector Program、NVR CFG sector Program （ATE 阶段)、
Redundancy Program;
LRS.EFC.FLASH【03]：支持 sector 擦除：Main Array Erase、
NVR Sector Erase、NVR CFG Erase （ATE 阶段）、Redundancy
Erase，sector大小为1KB;
LRS.EFC.FLASH【04】：支持整片擦除：Main Array,All Main
Array + All Redundancy, All Main Array + All Redundancy + All
NVR;
LRS.EFC.FLASH【05】：支持写 Config Register;
LRS.EFC.FLASH【06]：支持 Retry 擦除：Main Array Retry
1 fp!
8'1



---
## 图像编号 16 (原图: `GameViewer_MMRNU2QuKX.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图1-19FLASHNVR读写保护示意图`，完整结构与时序请查看原图 `GameViewer_MMRNU2QuKX.png`。

其方案示意图如下：
09,T=[u]eμ_d.m
.Ji
wr_op
test_code!±32d0
SECTOR[n]
09,t -[u]m]f dp]
an112026-11
rd_op

**图1-19FLASHNVR读写保护示意图**

在TESTCODE为全零的情况下，当NVRprot对应读写控制
位为o时，禁止读写操作进入sector。
想要解除该操作，只能使test code!=Oxo或者NVR prot!=O,
只能通过擦除flash实现，因此可以实现对芯片数字资产保护。

#### 1.2.11紧急撤销

在EFC硬件上没有额外处理，软件只需要对1.2.11.3/1.2.11.4
中的master进行操作，EFC即可实现；


### 【右页】

Q026-10-02-21:47
han,11

### 第2章 需求规格

ETICU hua7. 1

#### 2.1 功能需求


#### 2.1.1 LRS.EFC.CLK

muan.1i
LRS.EFC.CLK【01】：数据总线为AXI4.0，时钟频率最高
200MHz;
LRS.EFC.CLK【02】：配置总线为APB3.0，时钟频率最高
200MHz，与数据总线同频同源；
LRS.EFC.CLK【03】：功能模块工作频率25MHz~200MHz
--S40eFlash工作的最高频率为100MHz;

#### 2.1.2 LRS.EFC.RST

6-10-02-21;42
LRS.EFC.RST【O1】：上电复位（POR），低电平有效；
LRS.EFC.RST【02】：DFTMODE切换复位，低电平有效；
LRS.EFC.RST【03】：硬复位（PAD），低电平有效；



---
## 原图：`GameViewer_N4leDL0su5.png`

### 【左页】

**图1-5 模块门控流程图（带复位）**

> 时序图参与者可确认：SoC软件、EFC、CRG。复杂时序图不自行重画。  
> 原图：`../images/GameViewer_N4leDL0su5.png`

带复位的流程主要体现在 EFC 的复位信号需要在 Flash 睡眠唤醒后才能释放，然后 EFC 再执行复位后动作，动作完成后才能执行后续的正常功能。

### 【右页】

### 1.2.5 芯片系统启动
## 原图：`GameViewer_nD3eu17L6q.png`

### 【左页】

| 序号 | 配置 | 默认值 | 说明 |
|---:|---|---|---|
| 1 | cfg_efc_indirect_cmd_r | 16'd0 | 间接寻址命令，由 IDS 产生脉冲启动；bit[15:13] - 指令类型：0：Read；1：Write；2：正常擦除；3：retry擦除；4：vread；default：NA；bit[12:10] - 选择类型：0：NVR_CFG；1：NVR；2：Main；3：Redundancy；4：整片；default：Main；bit[9:0] - 地址选择：sector选择；选择类型 NVR 时，低4bit有效；选择类型 Main 时，9bit有效；选择类型 Redundancy 时，低1bit有效；选择类型整片时，低2bit有效，表示含义为：0：All Main Array；1：All Main Array + All Redundancy；2：All Main Array + All Redundancy + All NVR；other：reserved。 |
| 2 | cfg_efc_indirect_sts_rpt | 2'b0 | 读取状态寄存器，只读：0：正在操作；1：操作完成(OK)；2：操作完成(ERR)；other：Reserved。 |
| 3 | cfg_efc_indirect_wdata0_r | 32'b0 | 间接写数据0，低32bit； |
| 4 | cfg_efc_indirect_wdata1_r | 32'b0 | 间接写数据1，高32bit；如果涉及到byte级的操作，软件写入该寄存器时，不操作部分置1 |
| 5 | cfg_efc_indirect_rdata0_rpt | 32'b0 | 间接数据0返回，低32bit； |
| 6 | cfg_efc_indirect_rdata1_rpt | 32'b0 | 间接数据1返回，高32bit； |

### 【右页】

#### 1.2.8.6 Redundancy 处理

同正常的读、写操作流程，区别只是是否使用 RDN 替代。

**图1-14 Redundancy读操作流程**

> 复杂流程图按原图保留，不自行重画。  
> 原图：`../images/GameViewer_nD3eu17L6q.png`

#### 1.2.8.7 RECALL 读取

由于在上电初始阶段，VREF 不稳定，Flash 工作也就不稳定，需要使用 RECALL 花更长时间以及内部特殊的处理，才能正常读取数据。

---

## 图像编号 19 (原图: `GameViewer_oT9ct4X3PL.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图1-3EFC软复位流程图`，完整结构与时序请查看原图 `GameViewer_oT9ct4X3PL.png`。


#### 1.2.3模块软复位

, 1i
SoC软件
EFC
CRG
正在工作
不再对EFC操作
LIDLE状态
配置cfg_efc_rstn为0
复位处理
EFC模块复
配置cfg_efc_rstn为1
复位释放
释效EFC模块复位
进行复位后动作：
1）读NVR;
2)写同Option寄存器：
复位完成，进行IDLE状态
重新对efc操作
ETMO/ han, 7i 202F-10-02-27:41
避续工作
EFC
SoC软件
CRG

**图1-3EFC软复位流程图**

上图表示的模块软复位流程中，Flash没有切换到DPD模式，
因此复位后可以直接工作；如果Flash切换到DPD模式，T需参
考下一章节中模块门控流程图（带复位）。其中cfgefcrstn由
SoC软件看到，原因是gating时的处理需要分步骤，这里也就统


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图1-4模块门控流程图`，完整结构与时序请查看原图 `GameViewer_oT9ct4X3PL.png`。


#### 1.2.4模块门控

模块门控通过系统控制
SYSC/CRG模块来实现，执行Flash
深度睡眠，需要由软件来管理控制顺序；（dpd的配置，在SYSC
模块内实现）
SoC收件
CRG
等格Flash不工作场架
配瓶Flash进行保度cy_elcdpd=1bl
执行Flash联
Ncmtcfg_efc_gating71
Gating
美斯EFC根换时钟(不复位）
cfgfc.gating60
Gating处理
打开EFC程块时件
配低Flash保度维联唤mctg__dpd=1b0
执行Flashte联换照
正在工作
SoC钛件
EFC
CRG

**图1-4模块门控流程图**

（不带复位）
;47
2D26-10-02-21:47



---
## 图像编号 20 (原图: `GameViewer_RIxO2iF81c.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图1-12`，完整结构与时序请查看原图 `GameViewer_RIxO2iF81c.png`。

1）CPU配置EFCcfg_efc_write_en，允许进行写操作；
2）arCPU配置master，启动数据写；
TC3）总线上接收到来自master的写命令和写数据（软件先启动
Master) ;
4）EFC对Flash进行写操作；（如果不受lock限制）
5）反馈给总线resp；（如果不受lock限制，则反馈OK；如
果受lock限制，则反馈ERR)
6）1~3循环，一直到数据处理完成；
7）EFC转移状态到IDLE；（最后是master给CPU中断表示
数据处理完成）
8）CPU配置EFC cfg_efc_write en=0，不允许进行写操作；
擦除操作
片擦除
对整片Flash进行换除，耗时8~
擦除
对当前Sector进行换除，耗时8-，不需要再火读联即可保证据除成功
Sector擦除
对当前Sector进行换除，每次其时0.8~，但是单次原脉并不能保证
Retryi家
质动：因此每次Retry除眉需要进行一次VerifyRead读取数费
确认是否换象或功，确认成功后就不再继续排踪。这种方法可以一定程
度上提升续脉性膜，
ETMO

**图1-12**

擦除分类及介绍


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图1-13`，完整结构与时序请查看原图 `GameViewer_RIxO2iF81c.png`。

SoC款件
EFC
Flash
配画indirect_cmd为擦除
接收察除指令到命令队列
启动Flash进行擦除操作
Flash进行擦除操作
根据配面时间确定擦除完成
状态机进入IDLE
繁除完成中断（同时indirect_sts也机完成）
等待EFC重新启用
SoC款件
EFC
Flash

**图1-13**

擦除操作流程
1）软件启动擦除指令（间接访问的其中一种）；
2）EFC接收擦除指令；
3n.12026-10-02-21:
3）EFC对Flash进行擦除操作；
（如果受lock限制，则直接
跳到3，并反馈写保护错误）
4）EFC根据配置时间确定擦除完成；
（如果不受lock限制）
5）EFC转移状态到IDLE;
6）EFC上报擦除完成中断，以及更新间接访问完成寄存器；
SectorErase和RetryErase操作过程基本一致。
2080F



---
## 原图：`GameViewer_tD5gCQa3Jp.png`

### 【左页】

- 1.2.8 NVR 地址空间划分说明
- 1.2.9 正常工作启动和结束（包含上报内容）
- 1.2.10 写保护（参考 STM32，3.3.12 扇区写保护部分）
- 1.2.11 FLASH NVR 读写保护
- 1.2.12 紧急撤销
- 第2章 需求规格
  - 2.1 功能需求
    - 2.1.1 LRS.EFC.CLK
    - 2.1.2 LRS.EFC.RST
    - 2.1.3 LRS.EFC.SOC
    - 2.1.4 LRS.EFC.SEC
    - 2.1.5 LRS.EFC.FLASH
    - 2.1.6 LRS.EFC.DFT
    - 2.1.7 LRS.EFC.DFX
    - 2.1.8 LRS.EFC.RBST
  - 2.2 中断管理
  - 2.3 事件管理
  - 2.4 约束说明
  - 2.5 触发源说明

### 【右页】

# 参考文献

---

## 图像编号 22 (原图: `GameViewer_u7x2KWkvm5.png`)

### 【左页】

> 📌 **【图表提示】**: 此处包含图表 `图1-10`，完整结构与时序请查看原图 `GameViewer_u7x2KWkvm5.png`。

数据读操作（MainArray，
Redundancy)
SoC软件
master
EFC
通过不同bt来表示
Redundancy.
ETMCU huas, li
Main
配置启动读数据
开始数需传输新环
通过AX总线，发透读命
对Flash进行读操作
通过AX总线，反情rdata和resp
结束数据传输新环
, 1i
欢态机进入IDLE
数据处理充成中断
等特EFC质新自用
SoC软件
master
EFC
202F-10-02-27:47

**图1-10**

数据读操作流程（MainArray，
Redundancy)
ETMOU
EFC只与Master（CPU或者系统DMA）产生数据交换；
1）总线上接收到来自master的读命令（软件先启动Master）；
2）EFC对Flash进行读操作；（如果不受lock限制）
3）反馈给总线rdata和resp；m（如果不受lock限制，则反馈
OK；如果受lock限制，则反馈ERR）
4）1~3循环，一直到数据处理完成；


### 【右页】

> 📌 **【图表提示】**: 此处包含图表 `图1-11`，完整结构与时序请查看原图 `GameViewer_u7x2KWkvm5.png`。

5）EFC转移状态到IDLE；1（最后是master给CPU中断表示
数据处理完成）
数据写操作
(Main Array,
Redundancy)
SoC软件
EFC
master
配置cfg efcwrite_en为
通过不同bit来表示：
Redundancy,
Main
配置启动写数据
开始数据传输暂环
遵过AX总线，发送写命令和写数据
对Flash进行写换作
通过AX总线，反绩resp
结束数据传输暂环
数据处理完成中断
配置cfg_efc_wite_en0
状态机进入IDLE
IDLE
等待EFC重新启用
SoC软件
master

**图1-11**

数据写操作流程
(Main Array，Redundancy)
EFC只与Master（CPU或者系统DMA）产生数据交换；
12080F



---
## 图像编号 23 (原图: `GameViewer_Umv4eQVy3N.png`)

### 【左页】

Erase. NVR Sector Retry Erase.NVR CFG Retry Erase.Redundancy
Retry Erase;
LRS.EFC.FLASH【07】：支持Flash的Byte操作（对不相关的
Byte通过对应bit=1来实现mask);
LRS.EFC.FLASH【08】：FLASH整芯片容量:
支持1个64K*72b=512KB空间的 PFLASH；支持1个
16K*72b=128KB空间的DFLASH;
LRS.EFC.FLASH【9】适配 SMICFLASHMACRO编程时,
72bit数据分两次写入：
1、AXI、APB总线写拆分两次写入；
2、AXI、APB总线单独写入高/低36bit，由配置选择；
&TMC3、保留一次性写入72bit能力；
LRS.EFC.FLASH【10】FLASH支持进入低功耗模式；
LRS.EFC.FLASH【11】FLASH有2Redundancy Sectors，用于
替换 MAIN Sector;

#### 2.1.6 LRS.EFC.DFT

RTMC) 2
BTMC han.
LRS.EFC.DFT【O1】：支持BIST自检;


### 【右页】

LRS.EFC.DFT【02】：支持TestMode（包含在BIST功能中）;
LRS.EFC.DFT【03】:ar支持LCK CFG在 wafer testing 后置 1;

#### 2.1.7 LRS.EFC.DFX

LRS.EFC.DFX【O1】支持PFLASH、FLASH记录并上报DFX
信息;
LRS.EFC.DFX【02】：模块工作状态上报；
LRS.EFC.DFX【03】：错误上报：写保护错误、1编程顺序错误、
选通错误、不一致错误、ECC1bit错误、ECC2bit错误；
LRS.EFC.DFX【04】RDP、WRP错误上报，总线错误返回数
据为0;
LRS.EFC.DFX【05】:Retry Erase结果上报;

#### 2.1.8 LRS.EFC.RBST

LRS.EFC.RBST【O1】：若该模块配置为ClockGate模式时，
不会导致CPU挂死--若CPU读该模块（非配置寄存器）,°则返
回为无效的0值，且resp返回ERR；若CPU操作该模块，则该
操作被屏蔽，且resp返回ERR;
LRS.EFC.RBST【02】：若该模块进行软复位时，不会导致CPU
1 fp!



---
## 原图：`GameViewer_XujivZGdpN.png`

### 【左页】

# EFC 模块 LRS 设计文档

设计：周玮玮  
评审：XXXXXXX

### 【右页】

批准：XXXXXXX

---

---

## 原图：`GameViewer_bqG5XHiWOd.png`

### 【左页】

# 图目录

- 图 2-1：XXXX

# 表目录

- 表 1-1：修订记录
- 表 2-1：基带板卡详细指标

### 【右页】

## 第1章 模块介绍

### 1.1 模块简介

EFC(eFlash Controller)模块是嵌入式 eFlash 控制器，对 eFlash 的读、写、擦除操作进行控制管理。

数据接口为 AXI Salve 接口，挂接在 AXI 4.0 总线上；

配置接口为 APB Slave 接口，挂接在 APB3.0 总线上；

外部电源信号，打开或者关闭 Flash 电源；（这里的外部电源，就是芯片内部的模拟部分--Flash Power Switch）

### 1.2 应用说明

> 原图：`../images/GameViewer_bqG5XHiWOd.png`

---

## 原图：`GameViewer_bTZBDjzsW4.png`

### 【左页】

NVR_CFG/NVR 的读取，SMIC 建议都使用 RECALL 读取方式。

#### 1.2.8.8 Retry Erase 处理

**图1-15 Retry擦除操作流程**

> 原图：`../images/GameViewer_bTZBDjzsW4.png`

### 【右页】

#### 1.2.9 写保护（参考 STM32，3.3.12 扇区写保护部分）

##### 1.2.9.1 寄存器写保护

**图1-16 寄存器写保护流程**

> 原图：`../images/GameViewer_bTZBDjzsW4.png`

1）模块复位后，`cfg_efc_reg_wrprot_flg` 寄存器默认为 1；  
2）软件按顺序写 `cfg_efc_reg_key1`、`cfg_efc_reg_key2` 寄存器；

i. 写入 `cfg_efc_reg_key1 = 0x01234567`； -- pflash  
ii. 写入 `cfg_efc_reg_key2 = 0x89ABCDEF`； --pflash

或

---

## 第二部分：截图明确标注的 ET6601 修改点

### 修订记录 1.1

- **原始文字**：根据ET6601 OR-DR更新，新增64KX72=512KB的PFLASH，原有FLASH回退为DFLASH
- **所在位置**：表1-1 修订记录，版本 1.1
- **修订日期**：20260920
- **修订人员**：周玮玮
- **原图**：`../images/GameViewer_fpb2HKWthL.png`
- **修改性质**：原图修订记录明确标注的 ET6601 更新
