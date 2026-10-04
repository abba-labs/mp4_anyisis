# EFC 模块 LRS 设计文档

> 来源：本仓库24张原始PNG截图。正文、表格及图中文字按真实章节和左右页阅读顺序转录；不使用其他芯片手册补齐。
> 本轮状态：24张均已进行首轮原图核对；图1-6有1处局部文字仍待复核，不能据此宣称整份文档“100%准确”。原文自身的编号、分区及保护粒度差异照录并单列说明。
> 正文中的“转录注”“图中文字转录”“原文差异已核实”是复核说明，不是原作者新增正文。复杂图的连线/时序以所链接原图为准。
> 来源固定于commit `db9422fd7345fb0b600c7ac6c9db25a3140344ed`；该次提交未改动截图。逐图清单见 `../../../RESTORE_PROGRESS.md`。

## 第一部分：原始文档精准还原

## 原图：`GameViewer_XujivZGdpN.png`

> [查看原始截图](../images/GameViewer_XujivZGdpN.png)

### 【左页】

# EFC 模块 LRS 设计文档

设计：周玮玮  
评审：XXXXXXX

### 【右页】

批准：XXXXXXX

---

## 原图：`GameViewer_fpb2HKWthL.png`

> [查看原始截图](../images/GameViewer_fpb2HKWthL.png)

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

## 原图：`GameViewer_tD5gCQa3Jp.png`

> [查看原始截图](../images/GameViewer_tD5gCQa3Jp.png)

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

## 原图：`GameViewer_bqG5XHiWOd.png`

> [查看原始截图](../images/GameViewer_bqG5XHiWOd.png)

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

## 原图：`GameViewer_jyfWngVZvO.png`

> [查看原始截图](../images/GameViewer_jyfWngVZvO.png)

### 【左页】

#### 1.2.1 Power On

**图1-1 Flash power on流程图**

> 图中文字转录（节点与消息名称；连线和时序以原图为准）：
> - 参与者：电源管理、Flash、CRG、EFC。
> - 产生VDD / VDD11；wait tRT；产生PORb；por_rst_n；flash_por_rst_n。
> - 执行POWER-ON过程，使用default时钟频率(25MHz)。
> - 1）读NVR_CFG；2）set config register，rdn寄存器更新；3）读取NVR OPTION BYTES域段；4）更新OPTION BYTES寄存器；5）输出nvr_shift_done高电平；6）读取NVR OTP域段；7）更新OTP寄存器；8）输出otp_shift_done高电平。
> - Flash上电结束(efc_otp_ready=efc_option_ready&otp_shift_done)。
>
> 原图：[图1-1，左页](../images/GameViewer_jyfWngVZvO.png)。

实现：

1. 子模块 S40_FCTRL 需要实现 POWER-ON 时序；
2. EFC_GFB 子模块需要实现（通过控制 S40_FCTRL）：
   1) 读取 NVR_CFG；
   2) Set config register；RDN 寄存器更新；

### 【右页】

   3) 读取 NVR OPTION BYTES 域段（DFLASH）；
   4) 输出 nvr_shift_done 高电平；
   5) 更新 OPTION BYTES 寄存器（DFLASH）；
   6) 读取 NVR OTP 域段（DFLASH）；
   7) 更新 OTP 寄存器（DFLASH）；
   8) 输出 otp_shift_done 高电平（DFLASH）。

#### 1.2.2 Power Off

**图1-2 Flash power off流程图（正常掉电）**

> 图中文字转录：
> - 参与者：电源管理、CRG、EFC、Flash。
> - 软件根据应用场景确定掉电的时间点，再配置电源管理断电。
> - 产生PORb=0；por_rst_n=0（图中向EFC和Flash的两条消息均如此标注）。
> - 根据CRG的设计进行延时。
> - 拉低VDD / VDD11，掉电。
>
> 原图：[图1-2，右页](../images/GameViewer_jyfWngVZvO.png)。

---

## 原图：`GameViewer_oT9ct4X3PL.png`

> [查看原始截图](../images/GameViewer_oT9ct4X3PL.png)

### 【左页】

#### 1.2.3 模块软复位

**图1-3 EFC软复位流程图**

> 图中文字转录：
> - 参与者：EFC、SoC软件、CRG。
> - 正在工作；不再对EFC操作；IDLE状态。
> - 配置cfg_efc_rstn为0；复位处理；EFC模块复位。
> - 配置cfg_efc_rstn为1；复位释放；释放EFC模块复位。
> - 进行复位后动作：1）读NVR；2）写回Option寄存器；
> - 复位完成，进行IDLE状态；重新对efc操作；继续工作。
>
> 原图：[图1-3，左页](../images/GameViewer_oT9ct4X3PL.png)。

上图表示的模块软复位流程中，Flash 没有切换到 DPD 模式，因此复位后可以直接工作；如果 Flash 切换到 DPD 模式，需参考下一章节中模块门控流程图（带复位）。其中 cfg_efc_rstn 由 SoC 软件看到，原因是 gating 时的处理需要分步骤，这里也就统一由 SoC 软件管理。

### 【右页】

> 转录注：右页首行已与上段连续合并。

#### 1.2.4 模块门控

模块门控通过系统控制 SYSC/CRG 模块来实现，执行 Flash 深度睡眠，需要由软件来管理控制顺序；（dpd 的配置，在 SYSC 模块内实现）

**图1-4 模块门控流程图（不带复位）**

> 图中文字转录：
> - 参与者：SoC软件、EFC、CRG。
> - 等待Flash不工作场景。
> - 配置Flash进行深度睡眠cfg_efc_dpd=1'b1；执行Flash睡眠；Flash睡眠完成。
> - 配置cfg_efc_gating为1；Gating处理；关闭EFC模块时钟(不复位)。
> - 等待EFC重新启用。
> - cfg_efc_gating为0；Gating处理；打开EFC模块时钟。
> - 配置Flash深度睡眠唤醒cfg_efc_dpd=1'b0；执行Flash睡眠唤醒；Flash睡眠唤醒完成。
> - 正在工作。
>
> 原图：[图1-4，右页](../images/GameViewer_oT9ct4X3PL.png)。

---

## 原图：`GameViewer_N4leDL0su5.png`

> [查看原始截图](../images/GameViewer_N4leDL0su5.png)

### 【左页】

**图1-5 模块门控流程图（带复位）**

> 图中文字转录：
> - 参与者：SoC软件、EFC、CRG。
> - 等待Flash不工作；配置Flash进行深度睡眠cfg_efc_dpd=1'b1；执行Flash睡眠；Flash睡眠完成。
> - 配置cfg_efc_gating为1，配置cfg_efc_rst_n为0；Gating处理，复位处理；关闭EFC模块时钟及复位。
> - 等待EFC重新启用；cfg_efc_gating为0；Gating处理；打开EFC模块时钟。
> - 配置Flash深度睡眠唤醒cfg_efc_dpd=1'b0；执行Flash睡眠唤醒；Flash睡眠唤醒完成。
> - 配置cfg_efc_rst_n为1；复位处理；释放EFC模块复位。
> - 进行复位后动作(读NVR，写回Option寄存器)；复位完成，进行IDLE状态；正在工作。
>
> 原图：[图1-5，左页](../images/GameViewer_N4leDL0su5.png)。

带复位的流程主要体现在 EFC 的复位信号需要在 Flash 睡眠唤醒后才能释放，然后 EFC 再执行复位后动作，动作完成后才能执行后续的正常功能。

> 转录注：以上段落在原图中为蓝色文字；仅记录颜色，不据此推断它属于哪次版本修改。

### 【右页】

#### 1.2.5 芯片系统启动

---

## 原图：`GameViewer_6F5qGwog2V.png`

> [查看原始截图](../images/GameViewer_6F5qGwog2V.png)

### 【左页】

> 图1-6图中文字转录（图名位于右页顶部）：
> - 参与者：电源管理、CRG、EFC、CPU、BootRom。
> - PORb；por_rst_n。
> - 把CPU启动Hold住；EFC复位撤销，启动EFC操作。
> - ⚠️ 原图待复核：CRG旁首个黄色框第一行的前两个字不能从当前像素100%确认；疑似“拉低芯片复位”，不写作确定正文。原图：`../images/GameViewer_6F5qGwog2V.png`。
> - 执行POWER-ON过程，使用default时钟频率(256KHz)：1）读NVR_CFG(RECALL)；2）set config register；3）读取NVR(RECALL)；4）更新到Option寄存器。
> - EFC上电结束；撤销CPU复位；复位撤销。
> - CPU从启动地址开始启动程序；返回程序内容。
> - 读Option寄存器；返回数据；根据返回的Option寄存器内容，选择后续启动模式等。
> - 配置EFC工作时钟选择(25MHz)；1）读取NVR(RECALL)；2）更新timing寄存器。
> - 配置CRG等待EFC状态完成；option_ready；切换EFC工作时钟。
> - CPU从程序地址读取程序内容；返回程序内容。
> - 厂商加载程序执行，等待PLL启动完成等芯片其他准备，然后开始执行用户程序。
> - 配置EFC工作时钟选择(100MHz)；1）读取NVR(RECALL)；2）更新timing寄存器。
> - 配置CRG等待EFC状态完成；option_ready；切换EFC工作时钟。
> - CPU从用户程序地址读取程序内容；返回程序内容；执行用户程序。
>
> 原图：[图1-6，左页图与右页图名](../images/GameViewer_6F5qGwog2V.png)。

### 【右页】

**图1-6 芯片Boot流程图**

#### 1.2.6 Wafer Testing

1）Wafeter Testing，详见 SMIC 交付的 BIST 文档；  
2）LCK_CFG 信号在 TEST_EN 为 0 时，即为 1；  
3）正常工作；

参见 ET6601-DOC/05.数字设计/03 HAC/03 方案 LRS/EFC/V100/03.设计/01.LRS/《FLASH 读写擦除保护.xlsx》

#### 1.2.7 地址空间说明

| FLASH | 空间 | sector | 说明 |
|---|---|---|---|
| PFLASH | NVR_CFG | 0 | FLASH相关信息，SMIC提供 |
|  | NVR | 0~15 | 无用途 |
|  | Main+RDN | 0~511 | 程序数据 |
| DFLASH | NVR_CFG | 0 | FLASH相关信息，SMIC提供 |
|  | NVR | 0~1 | ROM空间，共4KB |
|  |  | 2、7 | OTP空间 |
|  |  | 3、4、6 | OPTION BYTES空间 |
|  |  | 5 | OPTION BYTES用户空间，供用户使用 |

> 转录注：本表与后文需求条目的NVR分区描述不完全一致；各处按原图保留，不合并、不自行选择一个版本替换其他内容。

---

## 原图：`GameViewer_BG11R4KzQV.png`

> [查看原始截图](../images/GameViewer_BG11R4KzQV.png)

### 【左页】

| FLASH | 空间 | sector | 说明 |
|---|---|---|---|
|  | Main+RDN | 0~127 | 用户数据 |

**图1-7 2个Flash地址空间说明**

> 上表为前一原图中地址空间表的末行续表。原图：[左页顶部](../images/GameViewer_BG11R4KzQV.png)。

#### 1.2.8 正常工作启动和结束（包含上报内容）

##### 1.2.8.1 数据读操作（NVR_CFG，NVR）

**图1-8 数据读操作流程（NVR_CFG，NVR）**

> 图中文字转录：
> - 参与者：配置master、EFC。
> - 通过不同bit来表示：NVR_CFG(wafer testing阶段/上电阶段)，NVR(上电阶段/EFC复位/正常阶段)。
> - 读NVR_CFG/NVR对应地址；对Flash进行读操作；状态机进入IDLE；反馈读回数据；IDLE；等待EFC重新启用。
>
> 原图：[图1-8，左页](../images/GameViewer_BG11R4KzQV.png)。

对图中“**配置 master**”的说明：

Wafter testing 阶段：配置 master 为测试接口；

上电阶段：配置 master 为 EFC_GFB 中的电源管理部分；

EFC 复位：表示只对 EFC 进行复位，对 Flash 没有断电。配置 master 也为 EFC_GFB 中的电源管理部分；

### 【右页】

> 转录注：右页首行已与上段连续合并。

正常阶段：配置 master 为系统 CPU；

**NVR、NVR_CFG读取，需要进行间接寻址，避免总线ready拉低挂住系统；**

> 转录注：上一段在原图中为红字。

##### 1.2.8.2 数据写操作（NVR_CFG，NVR，Config Register）

**图1-9 数据写操作流程（NVR_CFG，NVR，Config Register）**

> 图中文字转录：
> - 参与者：配置master、EFC。
> - 通过不同bit来表示：NVR_CFG(wafer testing阶段/上电阶段)，Config Register(上电阶段)，NVR(上电阶段/正常阶段)。
> - 写NVR_CFG/Config Register/NVR对应地址；对Flash进行写操作；根据配置写操作时间，状态机进入IDLE；IDLE；等待EFC重新启用。
>
> 原图：[图1-9，右页](../images/GameViewer_BG11R4KzQV.png)。

Wafter testing 阶段：配置 master 为测试接口；

上电阶段：配置 master 为 EFC_GFB 中的电源管理部分；

正常阶段：配置 master 为系统 CPU；

---

## 原图：`GameViewer_u7x2KWkvm5.png`

> [查看原始截图](../images/GameViewer_u7x2KWkvm5.png)

### 【左页】

##### 1.2.8.3 数据读操作（Main Array，Redundancy）

**图1-10 数据读操作流程（Main Array，Redundancy）**

> 图中文字转录：
> - 参与者：SoC软件、master、EFC。
> - 通过不同bit来表示：Redundancy、Main。
> - 配置启动读数据；开始数据传输循环。
> - 通过AXI总线，发送读命令；对Flash进行读操作；通过AXI总线，反馈rdata和resp。
> - 结束数据传输循环；状态机进入IDLE；IDLE；数据处理完成中断；等待EFC重新启用。
>
> 原图：[图1-10，左页](../images/GameViewer_u7x2KWkvm5.png)。

EFC 只与 Master（CPU 或者系统 DMA）产生数据交换；

1）总线上接收到来自 master 的读命令（软件先启动 Master）；  
2）EFC 对 Flash 进行读操作；（如果不受 lock 限制）  
3）反馈给总线 rdata 和 resp；（如果不受 lock 限制，则反馈 OK；如果受 lock 限制，则反馈 ERR）  
4）1~3 循环，一直到数据处理完成；

### 【右页】

5）EFC 转移状态到 IDLE；（最后是 master 给 CPU 中断表示数据处理完成）

##### 1.2.8.4 数据写操作（Main Array，Redundancy）

**图1-11 数据写操作流程（Main Array，Redundancy）**

> 图中文字转录：
> - 参与者：SoC软件、EFC、master。
> - 配置cfg_efc_write_en为1。
> - 通过不同bit来表示：Redundancy、Main。
> - 配置启动写数据；开始数据传输循环。
> - 通过AXI总线，发送写命令和写数据；对Flash进行写操作；通过AXI总线，反馈resp。
> - 结束数据传输循环；数据处理完成中断；配置cfg_efc_write_en为0；状态机进入IDLE；IDLE；等待EFC重新启用。
>
> 原图：[图1-11，右页](../images/GameViewer_u7x2KWkvm5.png)。

EFC 只与 Master（CPU 或者系统 DMA）产生数据交换；

---

## 原图：`GameViewer_RIxO2iF81c.png`

> [查看原始截图](../images/GameViewer_RIxO2iF81c.png)

### 【左页】

1）CPU 配置 EFC cfg_efc_write_en，允许进行写操作；  
2）CPU 配置 master，启动数据写；  
3）总线上接收到来自 master 的写命令和写数据（软件先启动 Master）；  
4）EFC 对 Flash 进行写操作；（如果不受 lock 限制）  
5）反馈给总线 resp；（如果不受 lock 限制，则反馈 OK；如果受 lock 限制，则反馈 ERR）  
6）1~3 循环，一直到数据处理完成；  
7）EFC 转移状态到 IDLE；（最后是 master 给 CPU 中断表示数据处理完成）  
8）CPU 配置 EFC cfg_efc_write_en=0，不允许进行写操作；

##### 1.2.8.5 擦除操作

**图1-12 擦除分类及介绍**

| 图中分类 | 图中文字 |
|---|---|
| 擦除 → 片擦除 | 对整片Flash进行擦除，耗时8~20ms |
| 擦除 → Sector擦除 → 正常擦除 | 对当前Sector进行擦除，耗时8~20ms，不需要再次读取即可保证擦除成功 |
| 擦除 → Sector擦除 → Retry擦除 | 对当前Sector进行擦除，每次耗时0.8~1ms，但是单次擦除并不能保证擦除成功；因此每次Retry擦除后都需要进行一次Verify Read读取数据确认是否擦除成功，确认成功后就不再继续擦除。这种方法可以一定程度上提升擦除性能。 |

> 原图：[图1-12，左页](../images/GameViewer_RIxO2iF81c.png)。

### 【右页】

**图1-13 擦除操作流程**

> 图中文字转录：
> - 参与者：SoC软件、EFC、Flash。
> - 配置indirect_cmd为擦除；接收擦除指令到命令队列；启动Flash进行擦除操作；Flash进行擦除操作。
> - 根据配置时间确定擦除完成；状态机进入IDLE；擦除完成中断（同时indirect_sts也填完成）；等待EFC重新启用。
>
> 原图：[图1-13，右页](../images/GameViewer_RIxO2iF81c.png)。

1）软件启动擦除指令（间接访问的其中一种）；  
2）EFC 接收擦除指令；  
3）EFC 对 Flash 进行擦除操作；（如果受 lock 限制，则直接跳到3，并反馈写保护错误）  
4）EFC 根据配置时间确定擦除完成；（如果不受 lock 限制）  
5）EFC 转移状态到 IDLE；  
6）EFC 上报擦除完成中断，以及更新间接访问完成寄存器；

Sector Erase 和 Retry Erase 操作过程基本一致。

> 转录注：“直接跳到3”及前页“1~3循环”均按原文保留，未按流程含义修订编号。

---

## 原图：`GameViewer_nD3eu17L6q.png`

> [查看原始截图](../images/GameViewer_nD3eu17L6q.png)

### 【左页】

| 序号 | 配置 | 默认值 | 说明 |
|---:|---|---|---|
| 1 | cfg_efc_indirect_cmd_r | 16'd0 | 间接寻址命令，由IDS产生脉冲启动：<br>bit[15:13] -- 指令类型：<br>0: Read;<br>1: Write;<br>2: 正常擦除;<br>3: retry擦除;<br>4: vread;<br>default: NA;<br>bit[12:10] -- 选择类型：<br>0: NVR_CFG;<br>1: NVR;<br>2: Main;<br>3: Redundancy;<br>4: 整片;<br>default: Main<br>bit[9:0] -- 地址选择：<br>sector选择；<br>选择类型NVR时，低4bit有效；<br>选择类型Main时，9bit有效；<br>选择类型Redundancy时，低1bit有效；<br>选择类型整片时，低2bit有效，表示含义为：<br>0: All Main Array;<br>1: All Main Array + All Redundancy;<br>2: All Main Array + All Redundancy + All NVR;<br>other: reserved. |
| 2 | cfg_efc_indirect_sts_rpt | 2'b0 | 读写状态寄存器，只读：<br>0: 正在操作；<br>1: 操作完成(OK)；<br>2: 操作完成(ERR)；<br>other: Reserved. |
| 3 | cfg_efc_indirect_wdata0_r | 32'b0 | 间接写数据0，低32bit； |
| 4 | cfg_efc_indirect_wdata1_r | 32'b0 | 间接写数据1，高32bit；<br>**如果涉及到byte级的操作，软件写入该寄存器时，不操作部分置1** |
| 5 | cfg_efc_indirect_rdata0_rpt | 32'b0 | 间接数据0返回，低32bit； |
| 6 | cfg_efc_indirect_rdata1_rpt | 32'b0 | 间接数据1返回，高32bit； |

### 【右页】

##### 1.2.8.6 Redundancy 处理

同正常的读、写操作流程，区别只是是否使用 RDN 替代。

**图1-14 Redundancy读操作流程**

> 图中文字转录：
> - 参与者：机台、SoC软件、master、EFC；阶段：CP阶段。
> - 检测Main array中sector缺陷；检测RDN sector缺陷；如果RDN sector没缺陷，将Main array中有缺陷的sector使用RDN sector替换；将NVR_CFG中PR0、PR1写入对应替换信息。
> - 配置启动读数据；开始数据传输循环；通过AXI总线，发送读命令。
> - 对Flash进行读操作；判断读取地址是否需要RDN替换的地址，如果是，则访问RDN sector来代替。
> - 通过AXI总线，反馈rdata和resp；结束数据传输循环；状态机进入IDLE；IDLE；数据处理完成中断；等待EFC重新启用。
>
> 原图：[图1-14，右页](../images/GameViewer_nD3eu17L6q.png)。

##### 1.2.8.7 RECALL 读取

由于在上电初始阶段，VREF 不稳定，Flash 工作也就不稳定，需要使用 RECALL 花更长时间以及内部特殊的处理，才能正常读取数据。

---

## 原图：`GameViewer_bTZBDjzsW4.png`

> [查看原始截图](../images/GameViewer_bTZBDjzsW4.png)

### 【左页】

**NVR_CFG / NVR 的读取，SMIC 建议都使用 RECALL 读取方式。**

> 转录注：上一句在原图中为蓝色加粗文字。

##### 1.2.8.8 Retry Erase 处理

**图1-15 Retry擦除操作流程**

> 图中文字转录：
> - 参与者：SoC软件、EFC、Flash。
> - 配置indirect_cmd为retry擦除；接收retry擦除到命令队列；启动Flash进行擦除操作。
> - Flash进行擦除操作；EFC根据配置时间确定擦除完成；自动执行VREAD判断擦除结果是否正确；VREAD判断错误，继续擦除；VREAD判断错误超过20次，也返回；VREAD判断正确，擦除完成。
> - 状态机进入IDLE；擦除完成中断；等待EFC重新启用。
>
> 原图：[图1-15，左页](../images/GameViewer_bTZBDjzsW4.png)。

### 【右页】

#### 1.2.9 写保护（参考 STM32，3.3.12 扇区写保护部分）

##### 1.2.9.1 寄存器写保护

**图1-16 寄存器写保护流程**

> 图中文字转录：
> - 模块复位后，cfg_reg_wrprot_flg寄存器默认为1。
> - 软件写cfg_efc_reg_key1 = REG_KEY1；Yes / No。
> - 软件写cfg_efc_reg_key2 = REG_KEY2；Yes / No。
> - cfg_reg_wrprot_flg被清零。
> - 软件配置寄存器，执行擦除、编程等操作。
> - cfg_reg_wrprot_flg寄存器重新配置为1。
>
> 原图：[图1-16，右页](../images/GameViewer_bTZBDjzsW4.png)。

1）模块复位后，cfg_efc_reg_wrprot_flg 寄存器默认为1；  
2）软件按顺序写 cfg_efc_reg_key1、cfg_efc_reg_key2 寄存器；

i. 写入 cfg_efc_reg_key1 = 0x01234567； -- pflash  
ii. 写入 cfg_efc_reg_key2 = 0x89ABCDEF； --pflash

或

---

## 原图：`GameViewer_cSaHi20ulN.png`

> [查看原始截图](../images/GameViewer_cSaHi20ulN.png)

### 【左页】

i. 写入 cfg_efc_reg_key1 = 0x0123CDEF； -- flash  
ii. 写入 cfg_efc_reg_key2 = 0x89AB4567； --flash

2）寄存器 cfg_efc_reg_wrprot_flg 标记清零；（如果步骤2配置错误，则lock标记不清零，后续动作也不会成功；如果操作步骤不正确，会在下一次系统复位前锁定cfg_efc_reg_wrprot_flg，并**返回总线错误**）  
3）软件配置寄存器；  
4）软件寄存器配置完成后，将 cfg_efc_reg_wrprot_flg 寄存器配置为1；

##### 1.2.9.2 NVR_CFG 写保护

在 CP 测试过程中，可以对该区域进行读写访问；

LCK_CFG 在 CP 测试后即拉高，用户在使用过程中无法进行读写；

实现中使用 nvrcfg_unlock==8'h00 做为 LCK_CFG；

### 【右页】

##### 1.2.9.3 NVR 写保护

**图1-17 NVR写保护流程**

> 图中文字转录：
> - 模块复位后，cfg_nvr_wrprot_flg寄存器默认为1；软件先执行cfg_reg_wrprot_flg寄存器清零过程。
> - 软件写cfg_efc_nvr_key1 = NVR_KEY1；Yes / No。
> - 软件写cfg_efc_nvr_key2 = NVR_KEY2；Yes / No。
> - cfg_nvr_wrprot_flg被清零；软件启动写操作/擦除操作。
> - 软件确认操作完成，并将cfg_nvr_wrprot_flg重新配置为1。
>
> 原图：[图1-17，右页](../images/GameViewer_cSaHi20ulN.png)。

1）模块复位后，cfg_efc_nvr_wrprot_flg 寄存器默认为1；  
2）软件按顺序写 cfg_efc_nvr_key1、cfg_efc_nvr_key2 寄存器；

i. 写入 cfg_efc_nvr_key1 = 0x45670123； --pflash  
ii. 写入 cfg_efc_nvr_key2 = 0xCDEF89AB； --pflash

或

i. 写入 cfg_efc_nvr_key1 = 0xCDEF0123； --flash  
ii. 写入 cfg_efc_nvr_key2 = 0x456789AB； --flash

> 转录注：原图中的步骤序号及“flash”字样均保留，不自行改成新的步骤号或“dflash”。

---

## 原图：`GameViewer_BiWjxKhdcj.png`

> [查看原始截图](../images/GameViewer_BiWjxKhdcj.png)

### 【左页】

3）寄存器 cfg_efc_nvr_wrprot_flg 标记清零；（如果步骤2配置错误，则lock标记不清零，后续动作也不会成功；如果操作步骤不正确，会在下一次系统复位前锁定cfg_efc_nvr_wrprot_flg，并**返回总线错误**）  
4）软件启动写/擦除指令；  
5）操作完成后，将 cfg_efc_nvr_wrprot_flg 寄存器配置为1；

**efuse 为 NVR 中的一部分，当前版本中不进行额外保护；**

> 转录注：上一句在原图中为蓝色文字。

##### 1.2.9.4 Main Array 写保护

**图1-18 Main写保护流程**

> 图中文字转录：
> - 寄存器写操作；--确认寄存器写保护；软件配置寄存器；--打开或关闭对应扇区写保护；--每个扇区可独立管理。
> - 软件启动写操作/擦除操作。
> - 硬件check写/擦除指令地址是否受保护（根据配置寄存器的写保护配置）。
> - 硬件上报中断（完成和写保护错误）。
>
> 原图：[图1-18，左页](../images/GameViewer_BiWjxKhdcj.png)。

1）软件启动写/擦除指令；

### 【右页】

2）硬件check写/擦除指令对应地址是否在保护扇区内（根据配置寄存器里面的内容--打开或关闭对应扇区写保护，每个sector可独立管理--flash可管理，pflash不可管理），如果不被保护则正常执行；如果被保护则不执行，并反馈 a）完成；b）上报写保护错误；

#### 1.2.10 FLASH NVR 地址空间划分与读写保护

参见 ET6601-DOC/05.数字设计/03 HAC/03 方案 LRS/EFC/V100/03.设计/01.LRS/《FLASH读写擦除保护.xlsx》

##### 1.2.10.1 架构和功能

1. DFLASH ROM空间（nvr sector0-3）受rdp、wrp保护，变成ROM后，芯片回收才会修改；
2. DFLASH OTP空间（nvr sector4、5，nvr sector15）受rdp、wrp保护，变成OTP后，芯片回收才会修改；
3. DFLASH NVR_CFG空间受lock保护，lock之后，芯片回收才会修改；
4. DFLASH OB空间（nvr sector6、7）受rdp、wrp保护，可修改，上电后自动生效；

---

## 原图：`GameViewer_5UxkiNGtxh.png`

> [查看原始截图](../images/GameViewer_5UxkiNGtxh.png)

### 【左页】

5. DFLASH nvr空间（nvr sector8）受rdp、wrp保护，可修改，上电后自动生效；
6. **DFLASH用户OTP空间（nvr sector9~13）受rdp、wrp保护，变成OTP后，擦除DFLASH nvr sector14，可恢复为无保护DFLASH nvr sector；**
7. DFLASH OB空间（nvr sector14）受rdp、wrp保护，通过密码+流程配置寄存器修改并直接生效；
8. DFLASH main空间，受rdp、wrp保护，可修改，上电后自动生效；
9. **PFLASH main空间，不受rdp保护；受wrp保护，以整片为单位；**

> 转录注：第6、9条在原图中为红字；其余条目为黑字。第9条与后文LRS.EFC.FUNC.SEC【13】的保护粒度表述不同，均按各自原图保留。

##### 1.2.10.2 OTP需求

| 名称 | 作用 | sector |
|---|---|---|
| dflash_main_rdp_n[7:0] | dflash的8个空间（以16个sector为单位）的读保护标识<br>1'b0：打开读保护，数据不能被读取；<br>1'b1：关闭读保护，数据能被读取；<br>注：TEST_CODE!=0时不做保护 | 14 |
| dflash_main_wrp_n[7:0] | dflash的8个空间（以16个sector为单位）的写保护标识<br>1'b0：打开写/擦除保护，数据不能被修改；<br>1'b1：关闭写/擦除保护，数据可以被修改；<br>注：TEST_CODE!=0时不做保护 | 14 |
| dflash_nvr_rdp_n[0] | dflash的nvr sector8的读保护标识，<br>1'b0：打开读保护，数据不能被读取；<br>1'b1：关闭读保护，数据能被读取；<br>注：TEST_CODE!=0时不做保护 | 14 |
| dflash_nvr_wrp_n[0] | dflash的8个nvr sector8的写/擦除保护标识；<br>1'b0：打开写/擦除保护，数据不能被修改；<br>1'b1：关闭写/擦除保护，数据可以被修改；<br>注：TEST_CODE!=0时不做保护 | 14 |
| dflash_nvr_otp_n[7:0][4:0] | dflash的nvr空间的5个sector确认变成用户otp<br>0x0：变为otp，数据不能被擦除，可将1写为0；<br>其他：正常nvr，数据能被写/擦除；<br>0~4分别表示sector9~13 | 14 |
| dflash_otp_gen_n[7:0][6:0] | dflash nvr空间的7个sector确认变成otp<br>0x0：变为otp，数据不能被擦除，可将1写为0；<br>其他：正常nvr，数据能被写/擦除；<br>0~5分别表示sector0~5，6表示sector15<br><br>otp的读/写保护，由bootrom配置只写1的寄存器实现；<br>otp的擦除保护，由bootrom配置只写1的寄存器实现； | 15 |
| nvrcfg_unlock[7:0] | FLASH nvr_cfg空间的读/写/擦除保护<br>0x0：打开保护，数据不能被读/写/擦除；<br>其他：关闭保护，数据能被读/写/擦除； | 15 |
| chip_ers_key[31:0] | 整芯片擦除key | 2 |

> 转录注：本表前两行位于左页，其余六行位于右页；表格跨页连续恢复。原图中`dflash_nvr_otp_n[7:0][4:0]`整行是红字；`dflash_otp_gen_n`的`[6:0]`及两项`0x0`是红字；`TEST_CODE!=0时不做保护`各注为红字。`dflash_nvr_wrp_n[0]`说明中的“8个nvr sector8”按原图保留，没有改写。

##### 1.2.10.3 读保护（RDP）和写保护(WRP)

FLASH NVR通过配置NVR prot实现NVR空间读写保护，避免在软件被恶意攻击或者注入的时候，恶意串改NVR内容。

---

## 原图：`GameViewer_MMRNU2QuKX.png`

> [查看原始截图](../images/GameViewer_MMRNU2QuKX.png)

### 【左页】

其方案示意图如下：

**图1-19 FLASH NVR读写保护示意图**

> 图中文字转录：
> - 写侧：`test_code!=32'd0`、`wrp_flag[n]==1'b0`、OR、`wr_op`、选择器`1`/`0`。
> - 读侧：`test_code!=32'd0`、`rdp_flag[n]==1'b0`、OR、`rd_op`、选择器`1`/`0`。
> - 存储块标签：`SECTOR[n]`。
>
> 原图：[图1-19，左页](../images/GameViewer_MMRNU2QuKX.png)。

在TEST_CODE为全零的情况下，当NVR prot对应读写控制位为0时，禁止读写操作进入sector。

想要解除该操作，只能使test_code!=0x0或者NVR prot!=0，只能通过擦除flash实现，因此可以实现对芯片数字资产保护。

#### 1.2.11 紧急撤销

在EFC硬件上没有额外处理，软件只需要对1.2.11.3/1.2.11.4中的master进行操作，EFC即可实现；

> 原文差异已核实：本截图正文标题确为“1.2.11 紧急撤销”；目录截图`GameViewer_tD5gCQa3Jp.png`确为“1.2.12 紧急撤销”。两处均照录，不将原文差异误判为转录错误，也不改写正文的`1.2.11.3/1.2.11.4`交叉引用。首句“在EFC硬件上没有额外处理”在原图中为蓝字。

### 【右页】

## 第2章 需求规格

### 2.1 功能需求

#### 2.1.1 LRS.EFC.CLK

LRS.EFC.CLK【01】：数据总线为AXI4.0，时钟频率最高200MHz；

LRS.EFC.CLK【02】：配置总线为APB 3.0，时钟频率最高200MHz，与数据总线同频同源；

LRS.EFC.CLK【03】：功能模块工作频率25MHz~200MHz

--S40 eFlash工作的最高频率为100MHz；

#### 2.1.2 LRS.EFC.RST

LRS.EFC.RST【01】：上电复位（POR），低电平有效；

LRS.EFC.RST【02】：DFT_MODE切换复位，低电平有效；

LRS.EFC.RST【03】：硬复位（PAD），低电平有效；

---

## 原图：`GameViewer_gYLpTulBVN.png`

> [查看原始截图](../images/GameViewer_gYLpTulBVN.png)

### 【左页】

#### 2.1.3 LRS.EFC.SOC

LRS.EFC.SOC【01】：外部控制功能包含：IDLE、READ、VREAD、WRITE、ROW WRITE、NORMAL SECTOR ERASE、RETRY SECTOR ERASE、CHIP ERASE、低功耗（模块时钟门控、Flash DPD功能）；

其中VREAD支持：

1）APB接口支持VREAD检查FLASH地址数据是否为全1（是否擦除成功），并且返回检查结果进行上报；  
2）通过配置使AXI、APB接口的FLASH读操作切换为VREAD读；

LRS.EFC.SOC【02】支持PFLASH双BANK地址映射，PFLASH Main区域共计512KB，AXI总线访问PFLASH内部地址划分为：

```text
BANK0: 0x000000-0x03FFFF
BANK1: 0x040000-0x07FFFF
```

根据SYSC SWAP配置交换两块BANK的读写访问地址；

APB间接命令读写擦除访问不做交换；

> 转录注：LRS.EFC.SOC【02】编号之后的上述内容在原图中均为红字。

LRS.EFC.SOC【03】：配置接口APB 3.0：地址位宽12bit、数据位宽32bit；

### 【右页】

> 转录注：右页首行已与上段连续合并。

LRS.EFC.SOC【04】：数据接口AXI 4.0，一个PFLASH、一个DFLASH分别独立使用一个AXI接口，支持并行操作，即分别对一个PFLASH和一个DFLASH的Main Array和开启替换的RDN区域执行读取、编程操作，地址位宽32、数据位宽64、最大BurstLen为16、读写ID位宽6bit、burst类型（只支持INCR1~16，WRAP 4/8且非narrow）、outstanding（最大3）、narrow、resp、wstrb；

LRS.EFC.SOC【05】：支持中断（高电平）产生：外部控制功能（LRS.EFC.SOC【06】）完成中断、错误中断；

LRS.EFC.SOC【06】：与CPU交互方式：寄存器配置，中断；

LRS.EFC.SOC【07】：支持紧急撤销（由软件管理，硬件不做额外逻辑）；

LRS.EFC.SOC【08】：数据侧支持Byte操作（即数据总线wstrb功能）；

FLASH支持双字、字、半字和字节进行读操作；

FLASH支持双字、字、半字和字节进行编程操作；

LRS.EFC.SOC【09】支持PFLASH、DFLASH数据对应8bit ECC，ECC可以纠正1bit错误，检测2bit及以上错误（即对64bit数据做ECC，得到8bit的纠错数据。~~当数据进行非64bit操作时--参见LRS.EFC.SOC【08】，不使能ECC~~）；

> 续行来源：[下一截图](../images/GameViewer_cQ0Ir7RHZa.png)。

> 转录注：【04】中两处位于PFLASH之前的“一个”及【09】中的“PFLASH、DFLASH”在原图中为红字。

---

## 原图：`GameViewer_cQ0Ir7RHZa.png`

> [查看原始截图](../images/GameViewer_cQ0Ir7RHZa.png)

### 【左页】

> 转录注：本页首段续行已与前一截图的同一条目合并；原文内容未删减。

1）ECC出现1bit错误时，记录历史告警寄存器；  
2）ECC出现2bit不可纠，上报中断；  
3）ECC出现2bit不可纠，送入fault管理，同时可用于封波；

开启ECC和ECC_WR_RVS时，对于写入的ECC 8bit内容的第0、1、4-7bit进行取反，保证写数据为全1时，ECC计算结果8'hC进行处理后也为8'hFF（全1），此时不会对FLASH内容进行改写；

开启ECC和ECC_RD_RVS时，对于读出的ECC 8bit内容的第0、1、4-7bit进行取反，保证ECC校验时ECC数据为写入前未取反的数据。

**MAIN/NVR/NVR_CFG ECC使能配置均默认开启并且禁止配置为关闭。**

LRS.EFC.FUNC.SOC【10】PFLASH、DFLASH支持被DMA直接访问；

> 转录注：首段被删除线划去的条件仍以删除线保留，不作为当前生效正文；强制开启ECC的整句及【10】中的“PFLASH、DFLASH”在原图中为红字。

### 【右页】

#### 2.1.4 LRS.EFC.SEC

LRS.EFC.FUNC.SEC【01】支持DFLASH NVR空间模拟OTP，OTP空间大小为3个sector（3KB）；

LRS.EFC.FUNC.SEC【02】支持DFLASH OTP区域安全访问机制；

LRS.EFC.FUNC.SEC【03】支持DFLASH NVR空间模拟ROM，ROM空间大小为4个sector（4KB）；

LRS.EFC.FUNC.SEC【04】支持PFLASH、DFLASH main区域安全访问机制；

LRS.EFC.FUNC.SEC【05】支持DFLASH上电复位释放后，硬件自动使需要加载的OTP、ROM信息生效（包括AES、CPLD和CPU1使能），而需要加载的OPTIONS（包含secure_level）需要在上电复位或硬复位释放后，都进行硬件自动生效；

支持上述硬件自动加载涉及到启动模式、安全等级和信息安全的域段采用多bit域段多数判决进行校正保护，并且输出校正后的域段值；

LRS.EFC.FUNC.SEC【06】安全级别只能由应用程序通过写OTP的方式由低向高配置，由高向低配置会被屏蔽；

> 转录注：【01】的“DFLASH”、【04】的“PFLASH、DFLASH”、【05】的“包括AES、CPLD和CPU1使能”在原图中为红字。右上远程连接提示是软件弹窗，不属于原文。

---

## 原图：`GameViewer_7Jsq6PhQM2.png`

> [查看原始截图](../images/GameViewer_7Jsq6PhQM2.png)

### 【左页】

LRS.EFC.FUNC.SEC【07】非BOOTROM发起的所有OTP的擦除操作都会被屏蔽；

LRS.EFC.FUNC.SEC【08】支持写OTP时通过key来验证写权限，key验证通过后，才可以进行写操作；

LRS.EFC.FUNC.SEC【09】NVR FLASH会输出32bit TEST_CODE。TEST_CODE不为0的时候，默认所有芯片限权/鉴权手段均不生效。

LRS.EFC.FUNC.SEC【10】支持OTP空间信息防泄露功能，禁止外部访问和修改；

LRS.EFC.FUNC.SEC【11】支持FLASH初始化结束指示输出管脚用于CP测试控制使用，在任何非DFT模式下都需要确保FLASH初始化结束指示能拉高，以保证安全启动；

LRS.EFC.FUNC.SEC【12】安全应用阶段提供3个sector的OTP空间，芯片内部根据烧录情况使用对应空间作为OTP使用；

LRS.EFC.FUNC.SEC【13】FLASH读写保护：

1. dflash ROM空间（nvr sector0~3）由DFLASH_OTP_GEN定义，变成ROM后，仅BOOTROM可读，禁止写和擦除，芯片回收才会修改；

### 【右页】

2. dflash OTP空间（nvr sector4~5，nvr sector15）由DFLASH_OTP_GEN定义，变成OTP后，仅BOOTROM可读可写，禁止擦除，芯片回收才会修改；
3. dflash OPTION BYTES空间（nvr sector6）仅BOOTROM可读可写可擦除，上电后自动生效，（nvr sector7）当secure_level等于2'd2/2'd3时，用户可仅读，当secure_level等于2'd0/2'd1时，用户可读可写可擦除，（nvr sector14），仅BOOTROM可写可擦除，用户可读，上电后自动生效；
4. dflash USER OPTION BYTES空间（nvr sector8）受rdp、wrp保护，可修改，上电后自动生效；
5. **dflash用户OTP空间（nvr sector9~13）由USER_NVR_OTP_GEN_N定义，变成OTP后，禁止擦除，上电后自动生效；**
6. dflash nvr空间（nvr sector14）受rdp、wrp保护，通过密码+流程配置寄存器修改并直接生效；
7. pflash dflash NVR_CFG空间受nvr_cfg_unlock保护，保护锁定后，禁止读写擦除，芯片回收才会修改；
8. dflash main空间，受rdp、wrp保护，以sector/16KB为单位，可修改，上电后自动生效；

> 续行来源：[下一截图](../images/GameViewer_LLELUTfGM7.png)。

> 转录注：第5条整条，以及第8条中的“以sector/16KB为单位”在原图中为红字。

---

## 原图：`GameViewer_LLELUTfGM7.png`

> [查看原始截图](../images/GameViewer_LLELUTfGM7.png)

### 【左页】

> 转录注：本页首段续行已与前一截图的同一条目合并；原文内容未删减。

对AXI总线访问MAIN空间读写保护区域，自动屏蔽写操作，读操作数据返回全0，并且根据配置使能决定是否返回总线错误；

对APB总线对于MAIN空间读取保护区域的擦除命令，自动屏蔽擦除操作，并且返回CMD_ERR；

9. pflash main空间，不受rdp保护；受wrp保护，以sector/32KB为单位；

LRS.EFC.FUNC.SEC【14】BOOTROM发起的DFLASH的全片擦除（main+RDN+NVR）触发整芯片擦除，依次擦除：

1）pflash main+RDN；（包含软件直接下发PFLASH main+RDN擦除命令）；  
2）dflash main+RDN；  
3）dflash USER OPTION BYTES（nvr sector8）；  
4）dflash USER OTP（nvr sector9~13）；  
5）flash OPTION BYTES（nvr sector7、14、6）；  
6）flash OTP（nvr sector4~5、nvr sector15）；

LRS.EFC.FUNC.SEC【15】支持PFLASH和DFLASH的redundancy功能，最多可替换两个Main Sector；

> 转录注：【14】中“pflash main+RDN”和第4项，以及【15】中的“PFLASH”和“DFLASH”在原图中为红字。

### 【右页】

> 转录注：右页首行已与上段LRS.EFC.FUNC.SEC【15】连续合并。

LRS.EFC.FUNC.SEC【16】DFLASH支持5KB USER OTP空间（NVR sector9~13）；

> 转录注：【16】编号之后的内容在原图中为红字。

#### 2.1.5 LRS.EFC.FLASH

LRS.EFC.FLASH【01】：支持读操作：Main Array Read、NVR Read、NVR CFG Read、Redundancy Read、Recall Read、Verify Read；

LRS.EFC.FLASH【02】：支持写操作：Main Array Program、NVR Sector Program、NVR CFG sector Program（ATE阶段）、Redundancy Program；

LRS.EFC.FLASH【03】：支持sector擦除：Main Array Erase、NVR Sector Erase、NVR CFG Erase（ATE阶段）、Redundancy Erase，sector大小为1KB；

LRS.EFC.FLASH【04】：支持整片擦除：Main Array，All Main Array + All Redundancy，All Main Array + All Redundancy + All NVR；

LRS.EFC.FLASH【05】：支持写Config Register；

LRS.EFC.FLASH【06】：支持Retry擦除：Main Array Retry Erase、NVR Sector Retry Erase、NVR CFG Retry Erase、Redundancy Retry Erase；

> 续行来源：[下一截图](../images/GameViewer_Umv4eQVy3N.png)。

---

## 原图：`GameViewer_Umv4eQVy3N.png`

> [查看原始截图](../images/GameViewer_Umv4eQVy3N.png)

### 【左页】

> 转录注：本页首段续行已与前一截图的同一条目合并；原文内容未删减。

LRS.EFC.FLASH【07】：支持Flash的Byte操作（对不相关的Byte通过对应bit=1来实现mask）；

LRS.EFC.FLASH【08】：FLASH整芯片容量：

支持1个64K*72b=512KB空间的PFLASH；支持1个16K*72b=128KB空间的DFLASH；

LRS.EFC.FLASH【9】适配SMIC FLASH MACRO编程时，72bit数据分两次写入：

1、AXI、APB总线写拆分两次写入；  
2、AXI、APB总线单独写入高/低36bit，由配置选择；  
3、保留一次性写入72bit能力；

LRS.EFC.FLASH【10】FLASH支持进入低功耗模式；

LRS.EFC.FLASH【11】FLASH有2 Redundancy Sectors，用于替换MAIN Sector；

> 转录注：【08】中的“支持1个64K*72b=512KB”和“支持1个16K*72b=128KB”在原图中为红字；【9】按原图保留为一位编号。

#### 2.1.6 LRS.EFC.DFT

LRS.EFC.DFT【01】：支持BIST自检；

### 【右页】

LRS.EFC.DFT【02】：支持TestMode（包含在BIST功能中）；

LRS.EFC.DFT【03】：支持LCK_CFG在wafer testing后置1；

#### 2.1.7 LRS.EFC.DFX

LRS.EFC.DFX【01】支持PFLASH、FLASH记录并上报DFX信息；

LRS.EFC.DFX【02】：模块工作状态上报；

LRS.EFC.DFX【03】：错误上报：写保护错误、编程顺序错误、选通错误、不一致错误、ECC1bit错误、ECC2bit错误；

LRS.EFC.DFX【04】RDP、WRP错误上报，总线错误返回数据为0；

LRS.EFC.DFX【05】：Retry Erase结果上报；

#### 2.1.8 LRS.EFC.RBST

LRS.EFC.RBST【01】：若该模块配置为Clock_Gate模式时，不会导致CPU挂死--若CPU读该模块（非配置寄存器），则返回为无效的0值，且resp返回ERR；若CPU操作该模块，则该操作被屏蔽，且resp返回ERR；

LRS.EFC.RBST【02】：若该模块进行软复位时，不会导致CPU挂死--若CPU读该模块（非配置寄存器），则返回为无效的0值，且resp返回ERR；若CPU操作该模块，则该操作被屏蔽，且resp返回ERR；

> 续行来源：[下一截图](../images/GameViewer_gLi3yEXagB.png)。

---

## 原图：`GameViewer_gLi3yEXagB.png`

> [查看原始截图](../images/GameViewer_gLi3yEXagB.png)

### 【左页】

> 转录注：本页首段续行已与前一截图的同一条目合并；原文内容未删减。

LRS.EFC.RBST【03】：模块从正常功能切到软复位或Clock_Gate模式，数据接口访问未完成时，按LRS.EFC.RBST【01、02】方式处理；

### 2.2 中断管理

LRS.EFC.INTR.SPEC【01】：功能完成，触发中断；

LRS.EFC.INTR.SPEC【02】：错误产生，触发中断；错误类型参考LRS.EFC.DFX【02】；

### 2.3 事件管理

无。

### 2.4 约束说明

### 【右页】

LRS.EFC.LIMIT.SPEC【01】：对该模块配置为Clock_Gate模式时，只能关闭内部工作时钟，接口时钟必须常开，否则可能导致接口总线挂死；

LRS.EFC.LIMIT.SPEC【02】：对该模块配置为Clock_Gate模式时，若CPU读该模块（非配置寄存器），则返回为无效的0值；若CPU操作该模块，则该操作被屏蔽；

LRS.EFC.LIMIT.SPEC【03】：该模块软复位过程中，若CPU读该模块（非配置寄存器），则返回为无效的0值；若CPU操作该模块，则该操作被屏蔽；

LRS.EFC.LIMIT.SPEC【04】：模块从软复位或Clock_Gate模式切到正常功能时，CPU需等待模块idle状态才能开始正常命令的工作；否则模块的处理方式和仍然在软复位或Clock_Gate模式的过程中一样；

LRS.EFC.LIMIT.SPEC【05】：在Flash工作过程中，不能变换bit操作位宽（64bit与非64bit之间），否则可能导致一直上报ECC错误，并且建议一直开启MAIN/NVR/NVR_CFG的ECC使能，只进行64bit的写操作（否则可能导致一直上报ECC错误），防止出现单bit失效无法校验；

LRS.EFC.LIMIT.SPEC【06】：总线不支持跨4Kbyte；

---

## 原图：`GameViewer_BMgqvo1P0z.png`

> [查看原始截图](../images/GameViewer_BMgqvo1P0z.png)

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

## 第二部分：截图明确标注的 ET6601 修改点

> 本部分只归集截图中的修订记录、红字、删除线和其他可见标记。红字未明确写出“新增/修改/删除”时，只标为“原图红字”，不推断其相对哪个旧版本发生变化。相同内容在不同位置出现时保留各自证据，不把出现次数当作独立功能修改数量。目录超链接、封面签名下划线不作为修改点。

### 2.1 明确写出 ET6601 的修订记录

| 编号 | 原始文字 | 所在位置 | 修订日期 | 原图 | 修改性质 |
|---|---|---|---|---|---|
| EFC-LRS-C01 | 从ET6003拷贝，参考ET6801 EFC LRS和ET6601 OR-DR修改刷新 | 表1-1，版本1.0；修订人员：周玮玮 | 20260715 | [GameViewer_fpb2HKWthL.png](../images/GameViewer_fpb2HKWthL.png) | 明确说明依据ET6601 OR-DR修改刷新 |
| EFC-LRS-C02 | 根据ET6601 OR-DR更新，新增64KX72=512KB的PFLASH，原有FLASH回退为DFLASH | 表1-1，版本1.1；修订人员：周玮玮 | 20260920 | [GameViewer_fpb2HKWthL.png](../images/GameViewer_fpb2HKWthL.png) | 原文明确“新增”“回退” |

### 2.2 原图红字和删除线条目

| 编号 | 原图标出的文字及必要上下文 | 所在位置 | 原图 | 标记/修改性质 |
|---|---|---|---|---|
| EFC-LRS-C03 | NVR、NVR_CFG读取，需要进行间接寻址，避免总线ready拉低挂住系统； | 1.2.8.1之后 | [GameViewer_BG11R4KzQV.png](../images/GameViewer_BG11R4KzQV.png) | 整句红字；未注明新增/修改性质 |
| EFC-LRS-C04 | DFLASH用户OTP空间（nvr sector9~13）受rdp、wrp保护，变成OTP后，擦除DFLASH nvr sector14，可恢复为无保护DFLASH nvr sector； | 1.2.10.1第6条 | [GameViewer_5UxkiNGtxh.png](../images/GameViewer_5UxkiNGtxh.png) | 整条红字 |
| EFC-LRS-C05 | PFLASH main空间，不受rdp保护；受wrp保护，以整片为单位； | 1.2.10.1第9条 | [GameViewer_5UxkiNGtxh.png](../images/GameViewer_5UxkiNGtxh.png) | 整条红字；与后文sector/32KB描述不同，不自行调和 |
| EFC-LRS-C06 | 注：TEST_CODE!=0时不做保护 | 1.2.10.2；dflash_main_rdp_n、dflash_main_wrp_n、dflash_nvr_rdp_n、dflash_nvr_wrp_n各行 | [GameViewer_5UxkiNGtxh.png](../images/GameViewer_5UxkiNGtxh.png) | 四处表内红字注释 |
| EFC-LRS-C07 | dflash_nvr_otp_n[7:0][4:0]；dflash的nvr空间的5个sector确认变成用户otp；0x0：变为otp，数据不能被擦除，可将1写为0；其他：正常nvr，数据能被写/擦除；0~4分别表示sector9~13；sector=14 | 1.2.10.2 OTP需求表 | [GameViewer_5UxkiNGtxh.png](../images/GameViewer_5UxkiNGtxh.png) | 整行红字 |
| EFC-LRS-C08 | dflash_otp_gen_n[7:0][6:0]中的[6:0]；0x0：变为otp，数据不能被擦除，可将1写为0； | 1.2.10.2 OTP需求表；dflash_otp_gen_n行 | [GameViewer_5UxkiNGtxh.png](../images/GameViewer_5UxkiNGtxh.png) | [6:0]和0x0为红字；完整行见正文，不推断旧值 |
| EFC-LRS-C09 | 0x0：打开保护，数据不能被读/写/擦除； | 1.2.10.2 OTP需求表；nvrcfg_unlock[7:0]行 | [GameViewer_5UxkiNGtxh.png](../images/GameViewer_5UxkiNGtxh.png) | 0x0为红字 |
| EFC-LRS-C10 | 支持PFLASH双BANK地址映射，PFLASH Main区域共计512KB，AXI总线访问PFLASH内部地址划分为：BANK0: 0x000000-0x03FFFF；BANK1: 0x040000-0x07FFFF；根据SYSC SWAP配置交换两块BANK的读写访问地址；APB间接命令读写擦除访问不做交换； | LRS.EFC.SOC【02】 | [GameViewer_gYLpTulBVN.png](../images/GameViewer_gYLpTulBVN.png) | 编号后的整项红字 |
| EFC-LRS-C11 | “一个PFLASH、一个DFLASH分别独立使用一个AXI接口”以及“分别对一个PFLASH和一个DFLASH的Main Array和开启替换的RDN区域执行读取、编程操作” | LRS.EFC.SOC【04】 | [GameViewer_gYLpTulBVN.png](../images/GameViewer_gYLpTulBVN.png) | 两处PFLASH前的“一个”为红字；不是整项都标红 |
| EFC-LRS-C12 | 支持PFLASH、DFLASH数据对应8bit ECC | LRS.EFC.SOC【09】，跨页 | [GameViewer_gYLpTulBVN.png](../images/GameViewer_gYLpTulBVN.png)、[GameViewer_cQ0Ir7RHZa.png](../images/GameViewer_cQ0Ir7RHZa.png) | PFLASH、DFLASH为红字 |
| EFC-LRS-C13 | 当数据进行非64bit操作时--参见LRS.EFC.SOC【08】，不使能ECC | LRS.EFC.SOC【09】 | [GameViewer_cQ0Ir7RHZa.png](../images/GameViewer_cQ0Ir7RHZa.png) | 原图明确删除线；正文以删除线保留 |
| EFC-LRS-C14 | MAIN/NVR/NVR_CFG ECC使能配置均默认开启并且禁止配置为关闭。 | LRS.EFC.SOC【09】之后 | [GameViewer_cQ0Ir7RHZa.png](../images/GameViewer_cQ0Ir7RHZa.png) | 整句红字 |
| EFC-LRS-C15 | PFLASH、DFLASH支持被DMA直接访问； | LRS.EFC.FUNC.SOC【10】 | [GameViewer_cQ0Ir7RHZa.png](../images/GameViewer_cQ0Ir7RHZa.png) | PFLASH、DFLASH为红字 |
| EFC-LRS-C16 | 支持DFLASH NVR空间模拟OTP，OTP空间大小为3个sector（3KB）； | LRS.EFC.FUNC.SEC【01】 | [GameViewer_cQ0Ir7RHZa.png](../images/GameViewer_cQ0Ir7RHZa.png) | DFLASH为红字 |
| EFC-LRS-C17 | 支持PFLASH、DFLASH main区域安全访问机制； | LRS.EFC.FUNC.SEC【04】 | [GameViewer_cQ0Ir7RHZa.png](../images/GameViewer_cQ0Ir7RHZa.png) | PFLASH、DFLASH为红字 |
| EFC-LRS-C18 | 包括AES、CPLD和CPU1使能 | LRS.EFC.FUNC.SEC【05】；OTP、ROM信息硬件自动生效的括号说明 | [GameViewer_cQ0Ir7RHZa.png](../images/GameViewer_cQ0Ir7RHZa.png) | 括号内文字为红字；原图是CPU1，不是CPU |
| EFC-LRS-C19 | dflash用户OTP空间（nvr sector9~13）由USER_NVR_OTP_GEN_N定义，变成OTP后，禁止擦除，上电后自动生效； | LRS.EFC.FUNC.SEC【13】第5条 | [GameViewer_7Jsq6PhQM2.png](../images/GameViewer_7Jsq6PhQM2.png) | 整条红字 |
| EFC-LRS-C20 | 以sector/16KB为单位 | LRS.EFC.FUNC.SEC【13】第8条，dflash main空间 | [GameViewer_7Jsq6PhQM2.png](../images/GameViewer_7Jsq6PhQM2.png) | 保护粒度短语为红字 |
| EFC-LRS-C21 | pflash main+RDN | LRS.EFC.FUNC.SEC【14】整芯片擦除次序第1项 | [GameViewer_LLELUTfGM7.png](../images/GameViewer_LLELUTfGM7.png) | 对应文字为红字；完整擦除次序见正文 |
| EFC-LRS-C22 | 4）dflash USER OTP（nvr sector9~13）； | LRS.EFC.FUNC.SEC【14】整芯片擦除次序第4项 | [GameViewer_LLELUTfGM7.png](../images/GameViewer_LLELUTfGM7.png) | 整项红字 |
| EFC-LRS-C23 | 支持PFLASH和DFLASH的redundancy功能，最多可替换两个Main Sector； | LRS.EFC.FUNC.SEC【15】，跨页 | [GameViewer_LLELUTfGM7.png](../images/GameViewer_LLELUTfGM7.png) | PFLASH和DFLASH为红字 |
| EFC-LRS-C24 | DFLASH支持5KB USER OTP空间（NVR sector9~13）； | LRS.EFC.FUNC.SEC【16】 | [GameViewer_LLELUTfGM7.png](../images/GameViewer_LLELUTfGM7.png) | 编号后的整项红字 |
| EFC-LRS-C25 | 支持1个64K*72b=512KB空间的PFLASH；支持1个16K*72b=128KB空间的DFLASH； | LRS.EFC.FLASH【08】 | [GameViewer_Umv4eQVy3N.png](../images/GameViewer_Umv4eQVy3N.png) | 两处“支持1个…”及容量表达为红字 |

### 2.3 其他可见标记，不冒充确定的版本差异

| 原图文字 | 所在位置及来源 | 可见标记 | 归类限制 |
|---|---|---|---|
| 带复位的流程主要体现在EFC的复位信号需要在Flash睡眠唤醒后才能释放，然后EFC再执行复位后动作，动作完成后才能执行后续的正常功能。 | 图1-5后；[GameViewer_N4leDL0su5.png](../images/GameViewer_N4leDL0su5.png) | 蓝字 | 原图未点明相对版本或新增/修改性质 |
| NVR_CFG / NVR的读取，SMIC建议都使用RECALL读取方式。 | 1.2.8.7后；[GameViewer_bTZBDjzsW4.png](../images/GameViewer_bTZBDjzsW4.png) | 蓝色加粗 | 原图未点明相对版本或新增/修改性质 |
| efuse为NVR中的一部分，当前版本中不进行额外保护； | 1.2.9.3后；[GameViewer_BiWjxKhdcj.png](../images/GameViewer_BiWjxKhdcj.png) | 蓝字 | 保留“当前版本”原句，不推断旧版行为 |
| 在EFC硬件上没有额外处理 | 1.2.11紧急撤销；[GameViewer_MMRNU2QuKX.png](../images/GameViewer_MMRNU2QuKX.png) | 蓝字 | 仅该短语标蓝，不补充硬件设计推理 |
