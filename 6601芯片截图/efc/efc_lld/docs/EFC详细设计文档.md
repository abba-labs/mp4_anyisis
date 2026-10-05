# EFC 模块详细设计文档

> 来源：本仓库36张原始PNG截图；只依据截图转录，不用其他芯片资料补缺。
> 提取范围：36/36张原始截图均已完成首轮逐图核对；本轮补完第25～36张，并回查既有9组疑点。LLD-U02/U03/U04/U05/U07/U08已核实补入；仍有U01/U06/U09/U10/U11共5组局部字形待更清晰同源资料确认。可读内容已转录，未辨明区域保留原图和明确定位；不将源图覆盖等同于全文逐字符验收。
> 本文件保持一份原始文档边界。按左右页、原文顺序保存；“转录注”和“图中文字转录”用于区分复核说明与原作者正文。
> 删除线以`~~删除内容~~`保留；颜色/下划线的证据另列，不将普通目录链接、签名横线视为6601修改。复杂图仍保留原图，不凭空重画。
> 原始图片来源commit：`db9422fd7345fb0b600c7ac6c9db25a3140344ed`；本轮基于第三轮已保存正文精校，原图未改写。统一入口：[EFC提取与验收报告](../../EFC_提取与验收报告.md)；两份文档的修改点见[EFC_6601修改点总览](../../EFC_6601修改点总览.md)。

## 第一部分：原始文档精准还原

## 原图：[GameViewer_vUFYITp5T4.png](../images/GameViewer_vUFYITp5T4.png)

### 【左页】

# EFC 模块详细设计文档

设计：周玮玮  
评审：XXXXXXX

### 【右页】

批准：XXXXXXX

---

## 原图：[GameViewer_Ts8jfg57vy.png](../images/GameViewer_Ts8jfg57vy.png)

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

## 原图：[GameViewer_Yg5PctElzk.png](../images/GameViewer_Yg5PctElzk.png)

### 【左页】

> 转录注：以下为目录续页，不是详细设计正文。

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

- 参考文献

---

## 原图：[GameViewer_vOtMQKhCkV.png](../images/GameViewer_vOtMQKhCkV.png)

### 【左页】

# 图目录

| 图号 | 图名 |
|---|---|
| 图1-1 | EFC模块框图 |
| 图1-2 | S40 FLASH结构框图 |
| 图1-3 | Flash Power Switch的连接关系图 |
| 图1-4 | FLASH_EFC模块内时钟域说明图 |
| 图2-1 | EFC_CFG模块框图 |
| 图2-2 | EFC_GFB模块框图 |
| 图2-3 | GFB_AXIM_PROC模块框图 |
| 图2-4 | EFC_POWER状态转移图 |
| 图2-5 | EFC_RESET状态转移图 |
| 图2-6 | GFB_CTRL状态转移图 |
| 图2-7 | Cache状态转移图 |
| 图2-8 | EFC_FCTRL模块框图 |
| 图2-9 | Flash Power状态转移图 |
| 图2-10 | FCTRL状态转移图 |
| 图2-11 | Flash Write状态转移图 |
| 图2-12 | Flash Set Config状态转移图 |

### 【右页】

| 图号 | 图名 |
|---|---|
| 图2-13 | Flash Erase状态转移图 |
| 图2-14 | Flash Read状态转移图 |
| 图2-15 | ECC域段翻转写入图 |
| 图2-16 | ECC域段翻转写入图 |
| 图3-1 | ECC错误注入对应寄存器配置 |
| 图4-1 | 读数datapath示意图 |
| 图4-2 | 写数datapath示意图 |
| 图5-1 | efc_clk和flash_clk时钟关系示意图 |

# 表目录

| 表号 | 表名 |
|---|---|
| 表1-1 | 修订记录 |
| 表1-1 | EFC接口信号说明 |
| 表2-1 | EFC_FCTRL接口信号说明 |

> 转录注：此图为图/表目录，不包含上述结构图本身。表1-1重复编号、图2-15与图2-16同名，均按原目录保留；蓝色下划线目录链接不作为6601修改证据。

---

## 原图：[GameViewer_oiTQxKdn2v.png](../images/GameViewer_oiTQxKdn2v.png)

### 【左页，含右页续文】

## 第1章 概要设计

### 1.1 功能框图

**图1-1 EFC模块框图**

> 图中文字转录：EFC；EFC_CFG；EFC_GFB；EFC_FCTRL；FLASH；CRG；FLASH_POWER；APB_MASTER；AXI_MASTER。
> 图形及连线：[查看原图左页](../images/GameViewer_oiTQxKdn2v.png)。

该模块功能框图，主要功能模块概述；

EFC_CFG模块：通过APB总线，接收APB Master来的配置；

EFC_GFB模块：接收外部CRG信号，对Flash进行开关控制（电源打开时，需要对Flash进行读NVR_CFG，再写Flash CFG的动作；然后才能进行正常工作）；通过AXI总线，接收AXI Master来的数据传输；

EFC_FCTRL模块：接收来自EFC_GFB、EFC_CFG的数据和配置，产生Flash操作对应的时序处理，以达到控制Flash的目的；

> 转录注：EFC_GFB段落从左页末尾“再写Flash”连续到右页顶部“CFG的动作”；以上已接成连续正文，EFC_FCTRL段落在原图右页。

### 【右页：续文后的结构图】

### 1.1.2 Flash结构框图

**图1-2 S40 FLASH结构框图**

> 图中文字转录（可确认部分）：左右两个结构均含Memory Address、Address Buffers、X-Decoder、Y-decoders and SA、I/O Buffers and Data Latches、Control Logic；分区可辨名称为NVR、NVR_CFG、RDN、Main Array。左图阵列标注64K×72，右图标注16K×72。
> 左右控制端可确认文字：RDEN、RECALL、CONFEN、WEB、TMEN、PORB、CEB、DPD、NVR、NVR_CFG、VREF、PROG、PROG2、ERASE、CHIP、CLOCK；可确认输出/数据前缀TMO、DIN、DOUT。
> 完整图形、连线和全部原始小字：[查看原图右页](../images/GameViewer_oiTQxKdn2v.png)。

> 第四轮局部补录（图1-2两组Control Logic周围可确认的无下标标签）：RDEN、RECALL、CONFEN、WEb、TMEN、PORb、CEb、DPD、NVR、NVR_CFG、LCK_CFG、VREF、PROG、PROG2、ERASE、CHIP、CLOCK、VREAD1、PREPG、TDO。两组分别照原图布置；未确认的容量和总线下标不从另一组类推。
> ⚠️ 原图待复核（LLD-U01）：图1-2的NVR/NVR_CFG/RDN分区容量小字，以及部分控制引脚名和总线下标，当前1920×1080截图无法逐字符确认。已保留可辨文字和完整原图，不依据后文或其他芯片规格反推这些字符。

---

## 原图：[GameViewer_ix7GnZKXn3.png](../images/GameViewer_ix7GnZKXn3.png)

### 【左页】

### 1.1.3 Flash Power Switch的连接关系

**图1-3 Flash Power Switch的连接关系图**

> 图中文字转录：芯片硬复位；Flash_Power & POR；PORb；CRG；EFC；EFC_GFB；S40_FCTRL；FLASH；VDD11；VDD；por_rst_n（图中多条复位连线上重复出现）。
> 图形及连线：[查看原图左页](../images/GameViewer_ix7GnZKXn3.png)。

### 【右页】

### 1.1.4 时钟域说明

**图1-4 FLASH_EFC模块内时钟域说明图**

> 图中文字转录：AXI_MASTER；APB_MASTER；EFC；EFC_GFB；AXIM_IF；EFC_GFB_MAIN；EFC_CFG；EFC_CFG_IDS；EFC_CFG_MAIN；EFC_FCTRL；FLASH。
> 图例：APB CLOCK DOMAIN（绿色）；AXI CLOCK DOMAIN（橙色）；EFC CLOCK DOMAIN（黄色）；FLASH CLOCK DOMAIN（紫色）。
> 图形及连线：[查看原图右页](../images/GameViewer_ix7GnZKXn3.png)。

整个EFC模块使用了5个时钟，apb时钟、axi时钟、EFC内部core时钟、EFSUE时钟以及Flash时钟；

3个时钟（apb时钟、axi时钟、EFC内部core时钟）在系统上都是给的同一个时钟（如果有异步处理，也是在NOC总线上实现）；

Flash时钟与EFC内部core时钟同源，时钟频率比为1:1、1:2或1:6；

> 转录注：本段末尾“或1:6”在[下一张原图左页](../images/GameViewer_kreeGdjIJX.png)顶部，已连续衔接。正文原词为EFSUE，照录，不改成其他拼写。目录写“1.1.3时钟域说明”，本页正文写“1.1.4时钟域说明”，保留原文差异。

---

## 原图：[GameViewer_kreeGdjIJX.png](../images/GameViewer_kreeGdjIJX.png)

### 【左页：时钟域说明续文】

EFC内的3个时钟（apb时钟、axi时钟、EFC内部core时钟），在CRG内分开进行时钟门控，避免APB、AXI总线被挂死；Flash时钟与EFC内部core时钟门控一致。

EFSUE时钟与EFC内部core时钟在OSC25MHz下同频同源。

### 1.2 接口列表和接口时序

**表1-1 EFC_DFLASH接口信号说明**

> 转录注：原表列名为“时钟信号／输入输出／说明”，并以灰底行区分各组。下表增加“类别”列以保留灰底分组，不增加信号或修改原说明；左、右页连续列出。

| 类别 | 信号名 | 输入输出 | 说明 |
|---|---|---|---|
| 时钟信号 | efc_clk | 输入 | 输入时钟，频率为25MHz~200MHz |
| 时钟信号 | efc_rst_n | 输入 | 输入复位信号，低电平有效 |
| 时钟信号 | efc_gclken | 输入 | flash工作时钟与efc_clk之间的分频使能 |
| 时钟信号 | flash_clk | 输入 | 输入时钟，flash工作时钟 |
| 电源相关 | por_rst_n | 输入 | 硬件复位信号，低电平有效；<br>复位表示Flash电源关闭，由POR提供；<br>该复位有效时，efc_rst_n必然有效，由CRG实现； |
| 电源相关 | flash_por_rst_n | 输入 | flash硬件por复位信号，低电平有效 |
| 测试相关 | TEST_EN | 输入 | 测试使能信号<br>0：测试不使能，正常工作；<br>1：测试使能，可执行ATE、wafer testing等动作； |
| 测试相关（右页续） | EFC_VREF | 输入 | Flash参考电压输入 |
| 测试相关 | EFC_TM0 | 输入输出 | Flash测试模式 |
| 测试相关 | EFC_VPP0 | 输入输出 | Flash VPP0 |
| 测试相关 | EFC_VPP1 | 输入输出 | Flash VPP1 |
| 中断 | efc_int | 输出 | Flash产生的中断信号，高电平有效 |
| OTP相关 | clk_otp | 输入 | otp时钟，晶振时钟 |
| OTP相关 | otp_rst_n | 输入 | otp复位信号，低电平有效 |
| OTP相关 | rom_rd_en | 输入 | ROM SECTOR读保护信号有效指示，由sysc模块送出 |
| OTP相关 | sysc_boot_exit_lockj | 输入 | BOOT退出锁定，控制OTP寄存器读写权限，由SYSC模块配置下发 |
| OTP相关 | otp_shift_done | 输出 | otp shift完成指示信号，输出给SYSC，DEBUG_AUTH模块使用 |
| OTP相关 | nvr_test_code[31:0] | 输出 | 芯片调试码，输出给SYSC，DEBUG_AUTH模块使用 |
| OTP相关 | uid[255:0] | 输出 | 芯片唯一ID，输出给DEBUG_AUTH模块使用 |
| OTP相关 | secure_level[1:0] | 输出 | 鉴权等级，输出给DEBUG_AUTH模块使用 |
| OTP相关 | secure_key[127:0] | 输出 | 鉴权密码，输出给DEBUG_AUTH模块使用 |
| OTP相关 | cpu_limit_n | 输出 | CPU1限定使能 |
| OTP相关 | cpld_limit_n | 输出 | CPLD限定使能 |
| OTP相关 | cpld_dbg_dis_n | 输出 | CPLD JTAG接口调试禁止 |
| OTP相关 | nvrcfg_unlock[7:0] | 输出 | pflash1/dflash nvr_cfg空间的读/写/擦除保护<br>0x00：打开保护，数据不能被读/写/擦除；<br>其他：关闭保护，数据能被读/写/擦除； |
| PFLASH相关 | secure_erase_main_done_pf | 输入 | PFLASH MAIN擦除结束标志 |
| PFLASH相关 | secure_erase_main | 输出 | DFLASH强制擦除PFLASH MAIN指示 |
| CRG | nvr_shift_done | 输出 | Option寄存器准备好，高电平有效；<br>SYSC模块可以根据该信号，锁定启动模式；<br>CRG可以根据该信号，撤销CPU的复位，让CPU开始进行Boot动作；<br>内部增加超时机制，超时后拉高； |

> 转录注：nvr_shift_done后两条说明在[U3Lm9vj4H7左页顶部](../images/GameViewer_U3Lm9vj4H7.png)，已接入该单元格。

> 原图标红：rom_rd_en整行；sysc_boot_exit_lockj整行；uid[255:0]中的“255”；cpld_limit_n整行；cpld_dbg_dis_n整行；nvrcfg_unlock[7:0]整行；secure_erase_main说明中的“DFLASH”。这些标记在第二部分逐条登记，不能推断未给出的旧值。
> 转录注：sysc_boot_exit_lockj末尾j按本页原表保留；nvr_shift_done与otp_shift_done是原表不同的两行，不合并。

---

## 原图：[GameViewer_U3Lm9vj4H7.png](../images/GameViewer_U3Lm9vj4H7.png)

### 【左页：表1-1 EFC_DFLASH接口信号说明续表】

> 转录注：左页顶端是上一张nvr_shift_done说明的续文，已接入上一张对应单元格。此处的CRG解除复位及超时说明为黑字；不要与后续PFLASH表的红字混为一条来源。

| 类别 | 信号名 | 输入输出 | 说明 |
|---|---|---|---|
| CRG | cfg_efc_core_gate_en | 输入 | 0：EFC未被门控；<br>1：EFC被门控，需避免总线被挂死； |
| APB总线 | efc_pclk | 输入 | APB时钟 |
| APB总线 | efc_presetn | 输入 | APB复位信号，低电平有效 |
| APB总线 | efc_psel | 输入 | APB选择信号 |
| APB总线 | efc_penable | 输入 | APB使能信号 |
| APB总线 | efc_paddr[31:0] | 输入 | APB地址信号 |
| APB总线 | efc_pwrite | 输入 | APB写指示信号<br>0：读操作；<br>1：写操作； |
| APB总线 | efc_pwdata[31:0] | 输入 | APB写数据 |
| APB总线 | efc_prdata[31:0] | 输出 | APB读数据 |
| APB总线 | efc_pready | 输出 | APB准备好信号，高电平有效 |
| APB总线 | efc_pslverr | 输出 | APB错误信号，高电平有效 |
| AXI总线 | efc_aclk | 输入 | AXI时钟 |
| AXI总线 | efc_aresetn | 输入 | AXI复位，低电平有效 |
| AXI总线 | efc_awid[5:0] | 输入 | AXI写命令通道ID |
| AXI总线 | efc_awaddr[31:0] | 输入 | AXI写地址 |
| AXI总线 | efc_awlen[3:0] | 输入 | AXI写burstlen |
| AXI总线 | efc_awsize[2:0] | 输入 | AXI写数据宽度 |
| AXI总线 | efc_awburst[1:0] | 输入 | AXI写类型 |
| AXI总线 | efc_awvalid | 输入 | AXI写有效指示，高电平有效 |
| AXI总线 | efc_awready | 输出 | AXI写准备好指示，高电平有效 |
| AXI总线 | efc_awlock | 输入 | AXI锁 |
| AXI总线 | efc_awcache | 输入 | AXI cache |
| AXI总线 | efc_awprot | 输入 | AXI保护 |
| AXI总线 | efc_wid[5:0] | 输入 | AXI写数据通道ID |
| AXI总线 | efc_wdata[63:0] | 输入 | AXI写数据 |
| AXI总线 | efc_wstrb[7:0] | 输入 | AXI写数据byte有效指示 |
| AXI总线 | efc_wlast | 输入 | AXI写last指示 |
| AXI总线 | efc_wvalid | 输入 | AXI写数据有效 |

### 【右页：表1-1续表及表1-2开始】

| 类别 | 信号名 | 输入输出 | 说明 |
|---|---|---|---|
| AXI总线 | efc_wready | 输出 | AXI写数据准备好指示，高电平有效 |
| AXI总线 | efc_bid[5:0] | 输出 | AXI反馈通道ID |
| AXI总线 | efc_bresp[1:0] | 输出 | AXI反馈内容 |
| AXI总线 | efc_bvalid | 输出 | AXI反馈有效指示，高电平有效 |
| AXI总线 | efc_bready | 输入 | AXI反馈准备好指示，高电平有效 |
| AXI总线 | efc_arid[5:0] | 输入 | AXI读命令通道ID |
| AXI总线 | efc_araddr[31:0] | 输入 | AXI读地址 |
| AXI总线 | efc_arlen[3:0] | 输入 | AXI读burstlen |
| AXI总线 | efc_arsize[2:0] | 输入 | AXI读数据宽度 |
| AXI总线 | efc_arburst[1:0] | 输入 | AXI读类型 |
| AXI总线 | efc_arvalid | 输入 | AXI读有效指示，高电平有效 |
| AXI总线 | efc_arready | 输出 | AXI读准备好指示，高电平有效 |
| AXI总线 | efc_arlock | 输入 | AXI锁 |
| AXI总线 | efc_arcache | 输入 | AXI cache |
| AXI总线 | efc_arprot | 输入 | AXI保护 |
| AXI总线 | efc_rid[5:0] | 输出 | AXI读数据通道ID |
| AXI总线 | efc_rdata[63:0] | 输出 | AXI读数据 |
| AXI总线 | efc_rresp[1:0] | 输出 | AXI读数据反馈指示 |
| AXI总线 | efc_rlast | 输出 | AXI读数据last指示 |
| AXI总线 | efc_rvalid | 输出 | AXI读数据有效指示，高电平有效 |
| AXI总线 | efc_rready | 输入 | AXI读数据准备好指示，高电平有效 |
| AXI GS相关信号 | efc_awlock[1:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_awcache[3:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_awprot[2:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_arlock[1:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_arcache[3:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_arprot[2:0] | 输入 | 外部可固定连接0 |
| Option输出 | cfg_efc_timing_r[447:0] | 输出 | Flash使用的timing信息； |

**表1-2 EFC_PFLASH接口信号说明**

| 类别 | 信号名 | 输入输出 | 说明 |
|---|---|---|---|
| 时钟信号 | efc_clk | 输入 | 输入时钟，频率为25MHz~200MHz |

> 转录注：表1-2从本页底部开始，下接[GameViewer_kpuE7cPAm8.png](../images/GameViewer_kpuE7cPAm8.png)的efc_rst_n行。原有Markdown把两张图前后放反，本轮依据明确表题和续行恢复为kreeGdjIJX→U3Lm9vj4H7→kpuE7cPAm8→nCyHpYzZqG。

---

## 原图：[GameViewer_kpuE7cPAm8.png](../images/GameViewer_kpuE7cPAm8.png)

### 【左页】

**表1-2 EFC_PFLASH接口信号说明（续表）**

> 转录注：表题、表头和efc_clk行位于[上一张U3Lm9vj4H7右页底部](../images/GameViewer_U3Lm9vj4H7.png)；本页继续efc_rst_n。两张原图中可见的行均保留，不猜补或错接至DFLASH表。

| 类别 | 信号名 | 输入输出 | 说明 |
|---|---|---|---|
| 时钟信号 | efc_rst_n | 输入 | 输入复位信号，低电平有效 |
| 时钟信号 | efc_gclken | 输入 | flash工作时钟与efc_clk之间的分频使能 |
| 时钟信号 | flash_clk | 输入 | 输入时钟，Flash工作时钟 |
| 电源相关 | por_rst_n | 输入 | 硬件复位信号，低电平有效；<br>复位表示Flash电源关闭，由POR提供；<br>该复位有效时，efc_rst_n必然有效，由CRG实现； |
| 电源相关 | flash_por_rst_n | 输入 | flash硬件por复位信号，低电平有效 |
| 测试相关 | TEST_EN | 输入 | 测试使能信号<br>0：测试不使能，正常工作；<br>1：测试使能，可执行ATE、wafer testing等动作； |
| 测试相关 | EFC_VREF | 输入 | Flash参考电压输入 |
| 测试相关 | EFC_TM0 | 输入输出 | Flash测试模式 |
| 测试相关 | EFC_VPP0 | 输入输出 | Flash VPP0 |
| 测试相关 | EFC_VPP1 | 输入输出 | Flash VPP1 |
| 中断 | efc_int | 输出 | Flash产生的中断信号，高电平有效 |
| SECURE_ERASE/OTP相关 | nvrcfg_unlock[7:0] | 输入 | pflash0/pflash1/dflash nvr_cfg空间的读/写/擦除保护<br>0x5A：打开保护，数据不能被读/写/擦除；<br>其他：关闭保护，数据能被读/写/擦除； |
| SECURE_ERASE/OTP相关 | secure_erase_main_df | 输入 | PFLASH收到DFLASH0强制擦除FLASH MAIN指示 |
| SECURE_ERASE/OTP相关 | secure_erase_main_done_pf | 输出 | PFLASH MAIN擦除结束指示 |
| CRG | nvr_shift_done | 输出 | Option寄存器准备好，高电平有效；<br>CRG可以根据该信号，撤销CPU的复位，让CPU开始进行Boot动作；<br>内部增加超时机制，超时后拉高； |
| CRG | cfg_efc_core_gate_en | 输入 | 0：EFC未被门控；<br>1：EFC被门控，需避免总线被挂死； |

### 【右页：续表】

| 类别 | 信号名 | 输入输出 | 说明 |
|---|---|---|---|
| timing信息 | cfg_efc_timing_r[447:0] | 输入 | Flash使用的timing信息； |
| APB总线 | efc_pclk | 输入 | APB时钟 |
| APB总线 | efc_presetn | 输入 | APB复位信号，低电平有效 |
| APB总线 | efc_psel | 输入 | APB选择信号 |
| APB总线 | efc_penable | 输入 | APB使能信号 |
| APB总线 | efc_paddr[31:0] | 输入 | APB地址信号 |
| APB总线 | efc_pwrite | 输入 | APB写指示信号<br>0：读操作；<br>1：写操作； |
| APB总线 | efc_pwdata[31:0] | 输入 | APB写数据 |
| APB总线 | efc_prdata[31:0] | 输出 | APB读数据 |
| APB总线 | efc_pready | 输出 | APB准备好信号，高电平有效 |
| APB总线 | efc_pslverr | 输出 | APB错误信号，高电平有效 |
| AXI总线 | efc_aclk | 输入 | AXI时钟 |
| AXI总线 | efc_aresetn | 输入 | AXI复位，低电平有效 |
| AXI总线 | efc_awid[5:0] | 输入 | AXI写命令通道ID |
| AXI总线 | efc_awaddr[31:0] | 输入 | AXI写地址 |
| AXI总线 | efc_awlen[3:0] | 输入 | AXI写burstlen |
| AXI总线 | efc_awsize[2:0] | 输入 | AXI写数据宽度 |
| AXI总线 | efc_awburst[1:0] | 输入 | AXI写类型 |
| AXI总线 | efc_awvalid | 输入 | AXI写有效指示，高电平有效 |
| AXI总线 | efc_awready | 输出 | AXI写准备好指示，高电平有效 |
| AXI总线 | efc_awlock | 输入 | AXI锁 |
| AXI总线 | efc_awcache | 输入 | AXI cache |
| AXI总线 | efc_awprot | 输入 | AXI保护 |
| AXI总线 | efc_wid[5:0] | 输入 | AXI写数据通道ID |
| AXI总线 | efc_wdata[63:0] | 输入 | AXI写数据 |
| AXI总线 | efc_wstrb[7:0] | 输入 | AXI写数据byte有效指示 |
| AXI总线 | efc_wlast | 输入 | AXI写last指示 |
| AXI总线 | efc_wvalid | 输入 | AXI写数据有效 |
| AXI总线 | efc_wready | 输出 | AXI写数据准备好指示，高电平有效 |
| AXI总线 | efc_bid[5:0] | 输出 | AXI反馈通道ID |
| AXI总线 | efc_bresp[1:0] | 输出 | AXI反馈内容 |

> 原图标红：por_rst_n说明中的“复位表示Flash电源关闭，由POR提供；该复位有效时，efc_rst_n必然有效，由CRG实现；”；flash_por_rst_n的说明；secure_erase_main_df说明中的“PFLASH”；nvr_shift_done信号名及其说明后两条（CRG撤销复位、增加超时）。
> 原文差异：前文DFLASH表的nvrcfg_unlock为输出、保护值0x00；本页为输入、保护值0x5A。分别照录，不自行统一。表中未写位宽的awlock/awcache/awprot等信号，不按AXI常识补位宽。

---

## 原图：[GameViewer_nCyHpYzZqG.png](../images/GameViewer_nCyHpYzZqG.png)

### 【左页：表1-2 EFC_PFLASH接口信号说明续表】

| 类别 | 信号名 | 输入输出 | 说明 |
|---|---|---|---|
| AXI总线 | efc_bvalid | 输出 | AXI反馈有效指示，高电平有效 |
| AXI总线 | efc_bready | 输入 | AXI反馈准备好指示，高电平有效 |
| AXI总线 | efc_arid[5:0] | 输入 | AXI读命令通道ID |
| AXI总线 | efc_araddr[31:0] | 输入 | AXI读地址 |
| AXI总线 | efc_arlen[3:0] | 输入 | AXI读burstlen |
| AXI总线 | efc_arsize[2:0] | 输入 | AXI读数据宽度 |
| AXI总线 | efc_arburst[1:0] | 输入 | AXI读类型 |
| AXI总线 | efc_arvalid | 输入 | AXI读有效指示，高电平有效 |
| AXI总线 | efc_arready | 输出 | AXI读准备好指示，高电平有效 |
| AXI总线 | efc_arlock | 输入 | AXI锁 |
| AXI总线 | efc_arcache | 输入 | AXI cache |
| AXI总线 | efc_arprot | 输入 | AXI保护 |
| AXI总线 | efc_rid[5:0] | 输出 | AXI读数据通道ID |
| AXI总线 | efc_rdata[63:0] | 输出 | AXI读数据 |
| AXI总线 | efc_rresp[1:0] | 输出 | AXI读数据反馈指示 |
| AXI总线 | efc_rlast | 输出 | AXI读数据last指示 |
| AXI总线 | efc_rvalid | 输出 | AXI读数据有效指示，高电平有效 |
| AXI总线 | efc_rready | 输入 | AXI读数据准备好指示，高电平有效 |
| AXI GS相关信号 | efc_awlock[1:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_awcache[3:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_awprot[2:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_arlock[1:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_arcache[3:0] | 输入 | 外部可固定连接0 |
| AXI GS相关信号 | efc_arprot[2:0] | 输入 | 外部可固定连接0 |

### 【右页】

## 第2章 详细设计

### 2.1 EFC_CFG

**图2-1 EFC_CFG模块框图**

> 图中文字转录：SOC_CORE_MISC；EFC_CFG；INT_GEN_MRG；EFC_INT_PARSE；CFG_REGPROT；EFC_CMN_WRPROT(REG)；CFG_FLASH_IDS*；APB_MASTER；EFC_GFB；EFC_FCTRL。
> 转录注：保护模块在原图中以重叠框表示，只转录前层完整可见名称，不猜补被遮挡的后层文字。CFG_FLASH_IDS后的小星号照录；本图未出现EFC_CFG_MAN，不沿用旧转录中的该标签。
> 图形及连线：[查看原图右页](../images/GameViewer_nCyHpYzZqG.png)。

该模块功能框图，主要功能模块概述；

CFG_REGPROT：当EFC时钟gating或者复位后FLASH未进入working状态时，禁止APB总线对IDS寄存器进行读写操作；寄存器写保护未解除前，除了寄存器、NVR解除写保护操作外，禁止APB总线对IDS寄存器进行写操作；产生APB总线的各类错误告警。

---

## 原图：[GameViewer_MhzCnwHL7y.png](../images/GameViewer_MhzCnwHL7y.png)

### 【左页：2.1 EFC_CFG续文】

EFC_CMN_WRPPROT(REG)：寄存器写保护模块，解除写保护流程参考《EFC模块LRS设计文档》第1.2.10.1寄存器写保护章节；

EFC_CMN_WRPPROT(NVR)：NVR写保护模块，解除写保护流程参考《EFC模块LRS设计文档》第1.2.10.3 NVR写保护章节；

CFG_FLASH_IDS：该模块使用工具自动生成，PFLASH/DFLASH需求分别生成，具体的配置参见《efc_cfg_dflash_nmanager》/《efc_cfg_pflash_nmanager》，里面包含：

1. Flash的timing参数，空间大小信息；

特别说明：在STM32、TI设计中，都是基于几个固定频率来配置Flash接口的timing参数；在当前设计中，是对所有timing参数都进行了配置（目的：a. 支持任意频率；b. 对Flash时序有更大的容错空间）

default参数为25MHz频率下参数，当EFC内部CORE工作频率变化时，FLASH时钟频率也随之变化，软件配置timing参数来进行适配，可根据各timing参数自动计算对应的ids寄存器值。

> 原图颜色标记：“特别说明”整段为蓝字。default段中“EFC内部CORE工作频率变化时，FLASH时钟频率也随之变化”和“可根据各timing参数自动计算对应的ids寄存器值。”为红字，其余为蓝字。蓝字说明不自动认定为6601新增功能。
> 原文差异：本页正文写EFC_CMN_WRPPROT，图2-1前层框写EFC_CMN_WRPROT；分别照录，不擅自统一标识符或交叉引用章节号。

### 【右页：配置内容续项】

2. 写保护：寄存器写保护、key1/2，NVR写保护、key3/4；
3. 写保护：main array的各个sector保护标记；
4. ECC：使能纯寄存器
5. 正常操作：读、写、擦除，类型
6. 中断相关：使能、状态、清零
7. 上报：中断状态、Flash状态、DFX信息

EFC_INT_PARSE、INT_GEN_MRG：中断上报、汇聚模块，将中断上报给CFG_FLASH_IDS并且汇聚后上报给SOC_CORE。

---

## 原图：[GameViewer_hMzpsucGw1.png](../images/GameViewer_hMzpsucGw1.png)

### 【左页，含右页续文】

### 2.2 EFC_GFB

**图2-2 EFC_GFB模块框图**

> 图中文字转录：EFC_GFB；GFB_AXIM_PROC；AXIM_IF；CMD_MERGE；AXI_MASTER；GFB_CTRL；CACHE；CTRL_STATE；ECC_CORR；CMD_MUX；RD_MUX；ECC_GEN_W；GFB_IF；EFC_FCTRL；EFC_EFUSE_PPROC_ARB；EFC_CFG_PROC；NVR_EFUSE_PROC；GFB_POWER_PROC；PR_STATE；POWER_CMD；EFC_CFG；POR。
> 图形及连线：[查看原图左页](../images/GameViewer_hMzpsucGw1.png)。

该模块功能框图，主要功能模块概述；

GFB_AXIM_PROC：接收AXI总线读写FLASH命令，分别进行总线保护、WRAP命令整合、命令size调整、命令合并，读取FLASH数据、返回RESP信息发送到总线上；

GFB_POWER_PROC：执行上电与复位时对Flash的操作，读取NVR_CFG，SetConfigReg，读取OTP/OB域段；上述硬件自动加载涉及到启动模式、安全等级和信息安全的域段采用多bit域段多数判决进行校正保护，并且输出校正后的域段值；

> 转录注：GFB_POWER_PROC段落的“自动加载”跨左右页，以上已连续衔接。

### 【右页】

GFB_CFG_PROC：接收并处理EFC_CFG过来的指令，根据指令格式组合是否正确，访问区域是否有读写保护进行屏蔽检查；

GFB_CTRL：子模块分别接收APB间接命令、POWER上电、复位命令和AXI总线命令，进行MUX选择，写数据增加ECC后，产生对应的命令给GFB_IF模块，接收GFB_IF模块返回的命令，检查ECC后分别返回给命令来源；预取数据提高AXI总线读访问效率；

GFB_IF：将ECC_GEN_W的数据，从接口发送给EFC_FCTRL；接收EFC_FCTRL返回的数据和RESP，发送给下级模块；

NVR_EFUSE_PROC：上电时发生上电解复位，GFB_POWER_PROC完成nvr_shift_done后，该模块发起flash的NVR ROM/OTP SECTOR（ROM Sector0~3，OTP Sector4~5，15）区域信息的读，将读取的内容用寄存器寄存下来，输出给SYSC模块和EFC内部保护逻辑使用，并输出otp_shift_done；上述硬件自动加载涉及到启动模式、安全等级和信息安全的域段

> 转录注：最后一句在本页以“域段”结束，续文位于下一张[GameViewer_9TPJx3syGF.png](../images/GameViewer_9TPJx3syGF.png)。续文已在第三轮核对并保留于下一张来源段，不改写原句。
> 原文差异：图2-2框名为EFC_CFG_PROC，正文小节名称为GFB_CFG_PROC；分别照录。

---

## 原图：[GameViewer_9TPJx3syGF.png](../images/GameViewer_9TPJx3syGF.png)

### 【左页】

采用多bit域段多数判决进行校正保护，并且输出校正后的域段值；

> 转录注：上句接上一张右页NVR_EFUSE_PROC末句“上述硬件自动加载涉及到启动模式、安全等级和信息安全的域段”，不是新增段落。

EFC_EFUSE_PPROC_ARB：根据efc_option_ready仲裁GFB_POWER_PROC与NVR_EFUSE_PROC执行的命令，发送给GFB_CTRL模块；

#### 2.2.1 GFB_AXIM_PROC

**图2-3 GFB_AXIM_PROC模块框图**

> 图中文字转录：AXI_MASTER；GFB_AXIM_PROC；AXI_GS；GFB_MPROC_PROT；GFB_MPROC_WRAP；GFB_MPROC_ASIZE；GFB_MPROC_MERGE；GFB_CTRL。
> 图形及连线：[查看原图左页](../images/GameViewer_9TPJx3syGF.png)。

该模块功能框图，主要功能模块概述；

AXI_GS：由Synopsys提供的AXI请求转换到GIF(Generic Interface)请求，GIF响应转换到AXI响应的DW IP；

GFB_MPROC_PROT：总线保护模块，实时监控总线的反馈情况，当gating或复位产生时，将总线未完成的交互模拟完成，避免总线挂死；同时产生门控AXI总线保护错误上报、复位AXI总线保护错误上报；

通过上电读取NVR ROM Sector的flash_main_wrp/rdp_n，对AXI总线访问MAIN空间读写保护区域，自动屏蔽写操作，读操作数据返回全0，并且根据配置使能决定是否返回总线错误；

> 转录注：“读操作数据返回全0……”在右页开头，以上衔接为原句。

### 【右页】

GFB_MPROC_WRAP：将WRAP4/8读访问命令进行转换，当到达Upper wrap boundary的读命令地址转换到Lower wrap boundary；

GFB_MPROC_ASIZE：将读写命令转换为8B格式；

GFB_MPROC_MERGE：将写命令按Flash Row进行拆分(Flash编程可以在同一个Row内一次性完成)；接收读取返回的数据，存放到AXIM_R_FIFO（Depth=16，outstanding * burstlen）中，然后发送到总线上；接收GFB_CTRL返回的RESP信息，存放到AXIM_RESP_FIFO（Depth=2）中，然后发送到总线上；

#### 2.2.2 GFB_POWER_PROC

根据外部电源信号，进行状态的跳转；

在上电阶段需要执行：

> 图中文字转录（上方黄色框）：执行POWER-ON过程，使用default时钟频率；1）读NVR_CFG；2）set config register；3）读取NVR；4）更新到Option寄存器。

在复位阶段需要执行：

> 图中文字转录（下方黄色框）：如果需要做复位，Flash需要做：1）读取NVR；2）更新到Option寄存器。
> 转录注：第四轮按原图局部重新核对，首行“如果需要做复位”已确认；不改写成软复位或硬复位。
> 原图：[GameViewer_9TPJx3syGF.png右页下方黄色框](../images/GameViewer_9TPJx3syGF.png)。

因此将动作拆分为两个子过程：

1）EFC_POWER -- 读NVR_CFG，set Config register；见图2-4；

> 转录注：“2-4；”位于下一张左页开头，已按原文续接。

---

## 原图：[GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png)

### 【左页】

2）EFC_RESET -- 读取NVR，更新OTP/OB（NVR Sector5/6/7/14）寄存器：flash_main_rdp_n[31:0],flash_main_wrp_n[31:0],flash_nvr_rdp_n[0],flash_nvr_wrp_n[0]；securelevel[16:0],~~nSWBOOT1,nBOOT1~~,flash_nvr_otp_n[7:0][4:0]进行多数判决；见图2-5；

那么上电阶段执行1）和2）子过程，并使用por_rst_n复位；复位阶段只执行2）子过程；

**图2-4 EFC_POWER状态转移图**

| 图中状态 | 框内文字 |
|---|---|
| GFB_POWER_OFF | in this state；state to initial Flash；reset use hard_arst_n |
| GFB_RD_NVRC | read NVR_CFG |
| GFB_SETC | set config register |
| GFB_PWR_WORKING | 原图无附加框内说明 |

> 图中条件文字：`s12_fctrl_state==GFB_PWR_WORKING`；`read_done`；`write_done`；`hard_arst_n=1'b0`；`hard_arst_n=1'b1`。
> 转录注：第四轮局部核实前缀为`s12`，按图保留数字1；图中的GFB_PWR_WORKING与其他位置的状态名不做统一。
> 图形、箭头及原字形：[查看原图左页](../images/GameViewer_Fio2eDanFe.png)。

### 【右页】

**图2-5 EFC_RESET状态转移图**

| 图中状态 | 框内文字 |
|---|---|
| GFB_RST_IDLE | in this state；reset use efc_arst_n |
| GFB_RD_NVR | read NVR |
| GFB_UPT_OPTION | update option registers |
| GFB_RST_WORKING | 原图无附加框内说明 |

> 图中条件文字：`efc_power_state==GFB_RST_WORKING`；`read_done`；`write_done = next cycle`；`efc_arst_n=1'b0`；`efc_arst_n=1'b1`。
> 图形及连线：[查看原图右页](../images/GameViewer_Fio2eDanFe.png)。
> 原文差异已核实：图2-5条件使用GFB_RST_WORKING；图2-4状态名使用GFB_PWR_WORKING。图内hard_arst_n/efc_arst_n与下方正文por_rst_n/efc_rst_n分别照录，不自行统一名称。

根据状态，POWER_CMD产生对应的Flash读、写命令和数据，发送给下级模块；

到达GFB_RST_WORKING状态时，即对外输出nvr_shift_done信号；从复位释放（por_rst_n和efc_rst_n），到进入GFB_RST_WORKING状态，有超时机制，超过门限后也会输出nvr_shift_done信号，但同时会上报超时状态；

当上电复位时，需要读NVR_CFG；

硬复位时，需要读取OTP/OB（NVR Sector5/6/7/14）寄存器：flash_main_rdp_n[31:0],flash_main_wrp_n[31:0],flash_nvr_rdp_n[0],flash_nvr_wrp_n[0]；securelevel[16:0],~~nSWBOOT1,nBOOT1~~,flash_nvr_otp_n[7:0][4:0]进行多数判决；

> 转录注：左右页两处清单均保留删除线。两处flash_main_rdp_n/flash_main_wrp_n中的31、flash_nvr_rdp_n/flash_nvr_wrp_n中的0及flash_nvr_otp_n[7:0][4:0]为红字；未据此猜测旧位宽。

---

## 原图：[GameViewer_AUvuEbreZL.png](../images/GameViewer_AUvuEbreZL.png)

### 【左页】

#### 2.2.3 NVR_EFUSE_PROC

这个模块主要实现上电时发生上电解复位，GFB_POWER_PROC完成nvr_shift_done后，该模块发起flash的NVR ROM/OTP SECTOR区域的读，将其内容全部读出来返回到其内部寄存器锁存下来。

##### 2.2.3.1 模块接口说明

该模块主要包含下面接口：

- 时钟复位接口：时钟为晶振时钟；复位源为上电复位和硬复位；
- nvr_shift_done接口：该信号用指示GFB_POWER_PROC解复位完成，NVR_CFG区域上电操作完成；
- 输出ROM/OTP锁存信息，并进行多数判决：具体那些需要输出按照硬件需求定，部分ROM/OTP信息送到EFC_CFG模块作为软件可读状态：

nvr_testcode[31:0]、sec_boot_dis[31:0]、cpu_limit_n[7:0]、flash_otp_gen_n[55:0]、nvr_cfg_unlock[7:0]、cpld_limit_n[7:0]、cpld_dbg_dis_n[7:0]；

uid[255:0]、Securekey[127:0]；

> 转录注：“并进行多数判决”、cpld_limit_n[7:0]、cpld_dbg_dis_n[7:0]及uid下标中的255为红字。原文“那些”及Securekey大小写保留。

### 【右页】

- 送出otp_shift_done用于指示flash的NVR ROM/OTP区域已锁存完毕，系统可根据ROM/OTP信息进行下一步流程；
- 送出RDP/WRP信息到EFC_CFG_PROC_PROT模块，用于该模块做flash读保护和写保护判断依据；

##### 2.2.3.2 模块状态跳转

当发生上电复位，GFB_POWER_PROC完成NVR_CFG读取和Flash配置和Option读取，即完成nvr_shift_done后，读取NVR ROM/OTP（ROM Sector0~3，OTP Sector4~5，15）信息。

#### 2.2.4 EFC_EFUSE_PPROC_ARB

将NVR_EFUSE_PROC与GFB_CFG_PROC的输入输出根据nvr_shift_done信号进行二选一仲裁；

#### 2.2.5 GFB_CFG_PROC_PROT

本子模块接收EFC_CFG过来的指令，如读NVR、写NVR、擦除，产生对应的Flash读、写命令和数据，产生Flash擦除命令，发送给下级模块；

> 原文差异已核实：2.2.3.1正文为EFC_CFG_PROC_PROT，2.2.5标题为GFB_CFG_PROC_PROT；本页仲裁输入和控制信号也与第13张概述不同，各处照录，不擅自改成同一套模块关系。

---

## 原图：[GameViewer_xLTLahbgSa.png](../images/GameViewer_xLTLahbgSa.png)

### 【左页，含右页第5条续文】

在ET6001的基础上，完善了nvr、main sector的读写保护；

flash sector14的读、写/擦除保护并没有放到ROM/OTP中，避免形成自锁；其读、写/擦除保护以带密码操作流程的方式，配置寄存器实现；

1、通过上电读取NVR OB Sector的flash_main_wrp_n和test_code，MAIN保护区域自动屏蔽擦除操作，并且返回CMD_ERR；

2、通过上电读取NVR OB Sector的flash_nvr_wrp/rdp_n和test_code，NVR RSV保护区域自动屏蔽读写擦除操作，并且返回CMD_ERR；

3、通过上电读取NVR USER OTP Sector的flash_nvr_otp_n，用户OTP保护区域自动屏蔽擦除操作，并且返回CMD_ERR；

4、通过上电读取NVR OTP Sector的flash_otp_gen_n，ROM保护区域自动屏蔽写擦除操作，并且返回CMD_ERR，读访问，受寄存器rom_rd_en控制；

5、通过上电读取NVR OTP Sector的flash_otp_gen_n，OTP保护区域自动屏蔽擦除操作，并且返回CMD_ERR，读写访问，受寄存器sysc_boot_exit_lockj控制；

### 【右页】

6、通过上电读取NVR OTP Sector的nvr_cfg_unlock，NVR_CFG区域自动屏蔽读写擦除操作，并且返回CMD_ERR；

7、通过上电读取NVR ROM Sector的test_code，RDN区域自动屏蔽读写擦除操作，并且返回CMD_ERR；

##### 2.2.5.1 只受bootrom访问说明

1.flash的全片擦除（main+RDN+NVR）触发擦除（flash main+RDN+NVR－除NVR sector0~3），依次擦除：

1)flash main+RDN；

2)flash USER OPTION BYTES (nvr sector8)；

3)flash USER OTP(nvr sector9~13)；

4)flash OPTION BYTES(nvr sector 7、14、6)；

5)flash OTP(nvr sector 4~5、nvr sector15)；

a)命令格式：`indcmd_subtype[23:20]=='h5`，`indcmd_subtype[19:16]=='h2`，`indcmd_subtype[15:0]=='hAA55`；

b）该命令保护寄存器受寄存器sysc_boot_exit_lockj控制，该

> 转录注：b）句末“该”续下一张左页；原文换行处indcmd_sub-type已作为同一信号indcmd_subtype续接。第3条保护说明、rom_rd_en、sysc_boot_exit_lockj，以及擦除顺序中的sector8数字8和USER OTP条目为红字，详见第二部分证据表。

---

## 原图：[GameViewer_QiBBFQjMG4.png](../images/GameViewer_QiBBFQjMG4.png)

### 【左页】

寄存器复位默认为0且只受软件写控制，在bootrom退出时将该寄存器写1，软件就无法进行该操作；（保证该操作只在bootrom有权限）；

> 转录注：上句接上一张末尾“该命令保护寄存器受寄存器sysc_boot_exit_lockj控制，该”。

2.《ET6601可信安全硬件详细设计说明》5.3.2章节对应寄存器在EFC实现；

otp的读写访问，受寄存器sysc_boot_exit_lockj控制；

rom的读访问，受寄存器rom_rd_en控制；

> 转录注：sysc_boot_exit_lockj、rom_rd_en为原图红字。这里只保留原作者引用，没有另行读取被引用文档补充正文。

#### 2.2.6 GFB_CTRL

**图2-6 GFB_CTRL状态转移图**

| 图中状态 | 可辨框内文字 |
|---|---|
| GFB_CTRL_WAITING | waiting power & reset done |
| GFB_CTRL_IDLE | 得到当前cmd_len_m1，下一拍寄存；当前状态才可接受cmd，并把cmd发送到下级模块 |
| GFB_CTRL_WR | 所有数据已根据锁存后的cmd_len_m1发送完成 |
| GFB_CTRL_RD | 下一拍返回GFB_CTRL_IDLE |
| GFB_CTRL_BRESP | 等待Flash的resp返回并握手，确认已完全擦除Flash或者VREAD命令已下发 |
| GFB_CTRL_WRESP | 等待Flash的resp返回并握手，确认已完全写入Flash |

> 图中条件文字：`rst_curst_working==1'b1`；`gfb_cmd_write==1'b1`；`gfb_cmd_read==1'b1`；`gfb_cmd_erase==1'b1 || gfb_cmd_vread==1'b1`；`resp_done_p==1'b1`；`wdata_vld_last==1'b1`；`write_done_p==1'b1`；`other`（多条自环）。
> 转录注：第四轮核实WAITING到IDLE条件为`rst_curst_working==1'b1`，WR框的“根据”已补回。
> 图形及连线：[查看原图左页](../images/GameViewer_QiBBFQjMG4.png)。

### 【右页】

CMD_MUX接收从CACHE/POWER_PROC/CFG_PROC来的命令，并从中选择（绝度优先级，POWER_PROC > CFG_PROC > CACHE）。

CACHE接收AXIM_PROC的读命令，并返回数据；

对于AXIM_PROC相关的取数：

1）如果AXIM_PROC读取burst数据，所有都包含在CACHE中，则不往Flash产生命令，直接从CACHE中取数返回。

2）如果AXIM_PROC读取burst数据，所有都不包含在CACHE中，则往Flash产生命令，从Flash读取后返回数据；

3）如果AXIM_PROC读取burst数据，部分在CACHE中，部分不在CACHE中，按顺序返回数据，没在cache的就直接读取flash；

4）AXIM_PROC第一次读取数据，CACHE产生读取指令并返回完数据后，自动增加地址，对Flash进行读取，填满CACHE空间；

5）AXIM_PROC后续发送的地址，正常情况下是和CACHE中的首地址是一致的，则按1）处理即可；

> 转录注：原文“绝度优先级”照录，不自动润色。CMD_MUX、CACHE词头为蓝色，用于模块说明，不因此判定版本修改。

---

## 原图：[GameViewer_Pi2p76SFY0.png](../images/GameViewer_Pi2p76SFY0.png)

### 【左页】

6）AXIM_PROC后续发送的地址，如果大于CACHE中某些地址，CACHE先释放小于AXIM_PROC地址的数据，再填满CACHE空间；

7）AXIM_PROC后续发送的地址，如果小于CACHE首地址，CACHE自动清空后，再和4）做同样动作；

**图2-7 Cache状态转移图**

| 图中状态 | 可辨框内文字 |
|---|---|
| ST_CACHE_IDLE | waiting cache work；if reset, first_mproc_rdflg=1b1；if to ST_MPROC_JUDGE, mproc_rd_flag = 1b1；if to ST_MPROC_JUDGE, first_mproc_rdflg = 1b0 |
| ST_MPROC_JUDGE | 1. when currd_in_cache==1'b0 && cache_cnt!=0：update cache first, then read, then get data from cache；2. when currd_in_cache==1'b0 && cache_cnt==0：read first, then get data from cache；3. when currd_in_cache==1'b1 && currd_in_cache_first==1'b1：get data from cache；4. when currd_in_cache==1'b1 && currd_in_cache_first==1'b0：update cache first, then get data from cache |
| ST_CACHE_BACK | read data out, then cache_cnt minus 1；this read proc is over, mproc_rd_flag = 1'b0 |
| ST_WAIT_RD | read data from flash (neighbor module is CORR)；then cache_cnt add 1 |
| ST_UPT_STS | from ST_WAIT_RD, add 1；from ST_CACHE_BACK, minus 1；from ST_MPROC_JUDGE, currd_in_cache==1'b0 && cache_cnt!=0, minus cache_cnt；from ST_MPROC_JUDGE, currd_in_cache==1'b1 && currd_in_cache_first==1'b0, minus first to valid cnt |

> 图中条件文字：`mproc2ctrl_cmd_hs==1'b1 || mproc_rd_vld==1'b1`；`first_mproc_rdflg==1'b0 && cache_full==1'b0`；`currd_in_cache==1'b1 && currd_in_cache_first==1'b1`；`currd_in_cache==1'b0 && cache_cnt==0`；`currd_in_cache==1'b0 && cache_cnt!=0`；`currd_in_cache==1'b1 && currd_in_cache_first==1'b0`；`corr2cache_data_vld==1'b1`；`mproc_rd_flag==1'b1`；`next cycle`；`other`。
> 转录注：第四轮核实ST_UPT_STS末行英文为“minus first to valid cnt”，照录原英文，不润色。IDLE框中的1b1/1b0仍按可见字形保留。
> 图形及连线：[查看原图左页](../images/GameViewer_Pi2p76SFY0.png)。

CMD_MUX将命令和数据都发送到ECC_GEN_W中，如果是写操作则添加ECC信息后送往下级模块；如果是读、擦除等操作，则直接送往下级模块，无延迟；

ECC_CORR将返回的数据进行ECC检测和纠错，然后送往RD_DMUX；

> 转录注：上句RD_DMUX位于右页开头，已接入原句。

### 【右页】

1）如果一致，则表明没有错误；

2）如果有1bit错误，则产生中断并纠错；

3）如果有2bit及以上错误，则产生中断，并原始数据返回；

RD_DMUX将返回的数据，分发给AXIM_PROC/POWER_PROC/CFG_PROC；

READ、RECALL操作，会经过ECC_CORR，进行ECC检测和纠错；

VREAD_CHK（含Retry的VREAD_CHK）操作，直接检测GFB_IF进来的数据是否全1，不经过ECC_CORR，目的是检查擦除操作是否擦干净，ECC域段和DATA域段都必须为全1,；

> 转录注：READ/RECALL段和VREAD_CHK段在原图为青蓝色，单列来源说明，不擅自定性为6601新增功能。“2bit及以上”的原文说法及末尾重复标点照录，不进行ECC技术纠错。

#### 2.2.7 GFB_IF

将ECC_GEN_W的数据，从接口发送给EFC_FCTRL；

接收EFC_FCTRL返回的数据和RESP，发送给下级模块；

---

## 原图：[GameViewer_zQvGQlgTkE.png](../images/GameViewer_zQvGQlgTkE.png)

### 【左页】

### 2.3 EFC_FCTRL

该子模块是eFlash控制部分，连接SoC侧控制部分和eFlash，其工作频率为25MHz~200MHz；本项目在系统启动过程中，可能涉及到的工作频率分别为25MHz、200MHz；

**图2-8 EFC_FCTRL模块框图**

> 图中文字转录：EFC_FCTRL；CRG；FCTRL_POWER_PROC；FCTRL_GFB_CMD_IF；FCTRL_FLASH_IF；FLASH；EFC_CFG；EFC_GFB。
> 图形及连线：[查看原图左页](../images/GameViewer_zQvGQlgTkE.png)。

该模块功能框图，主要功能模块概述；

FCTRL_POWER_PROC：根据电源和配置DPD进行Flash Power状态跳转；

FCTRL_GFB_CMD_IF：从GFB接口分解出对应的CMD指令和数据信息，来启动状态机的跳转；

FCTRL_GFB_FLASH_IF：根据GFB_CMD_IF接收的状态，适配FLASH时序进行FLASH操作；

> 原文差异已核实：图2-8的框名为FCTRL_FLASH_IF，正文为FCTRL_GFB_FLASH_IF；正文25MHz~200MHz与右页接口表25MHz~100MHz并存，分别保留。

### 【右页】

#### 2.3.2 接口列表

**表2-1 EFC_FCTRL接口信号说明**

| 信号 | 输入输出 | 说明 |
|---|---|---|
| efc_clk | 输入 | 输入时钟，频率为25MHz~100MHz |
| efc_rst_n | 输入 | 输入复位信号，低电平有效 |

**电源相关**

| 信号 | 输入输出 | 说明 |
|---|---|---|
| por_rst_n | 输入 | 硬件复位信号，低电平有效；<br>复位表示Flash电源关闭，由系统提供；<br>该复位有效时，efc_rst_n必然有效； |
| cfg_efc_dpd_r | 输入 | 0：flash DPD模式关闭；<br>1：flash DPD模式打开； |

**配置接口**

详细参见《efc_cfg_dflash_nmanager》《efc_cfg_pflash_nmanager》

**GFB接口（General Function Bus）**

| 信号 | 输入输出 | 说明 |
|---|---|---|
| gfb2fctrl_cmd_vld | 输入 | EFC发送的命令有效，高电平有效 |
| gfb2fctrl_cmd[FLASH_DW-1:0] | 输入 | EFC发送的命令；<br>**when cmd --**<br>[15:0] -- A<br>[19:16] -- Type: Write, SecErase, ChipErase, Read, SetConfig, RECALL,VREAD,RETRY<br>[23:20] -- SubType: NVR_CFG, NVR, Redundancy, Main / Main Array, All Main Array + All Redundancy, All Main Array + All Redundancy + All NVR<br>[27:24] -- Len_m1<br>[71:28] -- reserved;<br>[72] -- 1'b0 //means CMD<br>**when wdata --**<br>[63:0] -- Wdata<br>[71:64] -- EccData<br>[72] -- 1'b1 //means DATA |
| gfb2fctrl_cmd_rdy | 输出 | EFC命令反压信号，高电平有效 |

> 转录注：por_rst_n说明的后两句为红字；配置接口文档名为蓝色引用。GFB接口续表在下一张左页，不把它拆成独立文档。

---

## 原图：[GameViewer_GsJtl9ctbU.png](../images/GameViewer_GsJtl9ctbU.png)

### 【左页】

**表2-1 EFC_FCTRL接口信号说明（接上页GFB接口）**

| 信号 | 输入输出 | 说明 |
|---|---|---|
| fctrl2gfb_rdata_vld | 输出 | Flash读数据有效，高电平有效 |
| fctrl2gfb_rdata[FLASH_DW-1:0] | 输出 | Flash读数据 |
| fctrl2gfb_resp_vld | 输出 | Flash反馈有效，高电平有效 |
| fctrl2gfb_resp | 输出 | Flash反馈信号<br>0：成功；<br>1：失败； |
| efc_pwr_working | 输出 | Flash Power状态信号 |
| efc_fctrl_idle | 输出 | Flash未执行指令空闲信号 |

**Flash接口**

| 信号 | 输入输出 | 说明 |
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

> 图中文字转录（本页电源时序图未显示独立图号/图名，不编造）：
> 信号：VDD/VDD11、PORb、DPD、CEb、RDEN、CLOCK、PROG、ERASE。
> 操作分组：READ OPERATION、PROGRAM OPERATION、ERASE OPERATION。
> 时间标记：tRT、tRHR、tDPDH（两处）、tDPDSR、tDPDSW、tFT。
> 原始波形、时间箭头及对应边沿：[查看原图右页](../images/GameViewer_GsJtl9ctbU.png)。不自行重绘或解释其时序。

---

## 原图：[GameViewer_ceValKI1oj.png](../images/GameViewer_ceValKI1oj.png)

### 【左页】

**图2-9 Flash Power状态转移图**

| 图中状态 | 框内文字 |
|---|---|
| IDLE | reset is por_rst_n |
| POWER_ON | do counter until；cnt==tRHR |
| WORKING | when cfg_efc_dpd==1'b1, do counter until；cnt==tDPDSR |
| DPD | when cfg_efc_dpd==1'b0, do counter until；cnt==tDPDH |

> 图中条件文字：`cfg_efc_dpd==1'b0`；`cfg_efc_dpd==1'b1`；`cnt==tRHR`；`por_rst_n==1'b0`（两处）；`cfg_efc_dpd==1'b1 & cnt==tDPDSR`；`cfg_efc_dpd==1'b0 & cnt==tDPDH`。
> 图形及连线：[查看原图左页](../images/GameViewer_ceValKI1oj.png)。图中单个&按原图保留。

状态会提供到GFB_PPROC模块，GFB_PPROC模块在WORKING状态时才会正常工作；

> 转录注：“WORKING状态时才会正常工作；”位于右页开头，已衔接。

### 【右页】

上电过程和下电过程的时序，由系统（Flash Power Switch& POR）来实现；

**注意：在power_off状态下，需要将Flash所有的输入接0；**

（S40NEF64KX72_S0_Application_Notes.pdf -- 1.2 POWER OFF）

> 转录注：注意事项在原图为蓝字；只转录原作者引用，不从被引用PDF补文。

#### 2.3.4 FCTRL_GFB_CMD_IF

**图2-10 FCTRL状态转移图**

> 图中文字转录：五个蓝色状态的可辨后缀分别为ST_IDLE、ST_WRITE、ST_SETCFG、ST_ERASE、ST_READ；状态名前缀仍待逐字符复核。
> 可辨命令/条件片段：`Cmd&cmd_type`、`WRITE`、`SETCFG`、`SECERASE`、`RETRY`、`CHIPERASE`、`READ`、`RECALL`、`VREAD`；`WRITE结束`、`SETCFG结束`；`ERASE结束`、`retry_erase_flag=0`；`Erase_done`、`retry_erase_flag=1`；`Nrmlrd || DPD_R`。
> 可辨框内条目：
> 1. retry_read结束时，vread_pass且retry_cnt>=cfg_efc_retry_main_r；
> 2. retry_read结束时retry_cnt超过最大值19；
> 3. recall正常读结束。
> 另一框：1、Retry_read结束时vread_pass=0；2、retry_read结束时虽然vread_pass了，但是retry_cnt小于配置的值。
> ⚠️ 原图待复核（LLD-U06，范围已缩小）：中央判断框的“且”和“>=”及自环“读操作未结束”已重新辨明；蓝色状态名完整前缀和底部retry条件框部分细字仍不能逐字符确认，不能用常见命名习惯补为某个前缀；可辨片段照留，准确字形仍以原图为准。
> 图形及连线：[查看原图右页](../images/GameViewer_ceValKI1oj.png)。

---

## 原图：[GameViewer_l6EdkNy5JN.png](../images/GameViewer_l6EdkNy5JN.png)

### 【左页】

从GFB接口分解出对应的CMD指令和数据信息，根据指令类型进行状态跳转，并将状态发送给FCTRL_GFB_FLASH_IF模块；

将写数据信息存放到寄存器阵列中，然后将数据发送到FLASH_IF发送到Flash；

将从Flash读取的数据，根据命令类型，进行擦除校验或者发送给EFC_GFB模块。

### 【右页】

**图2-11 Flash Write状态转移图**

| 图中状态 | 可辨框内文字 |
|---|---|
| WR_ST_IDLE | 原图框内无附加说明 |
| WR_ST_RCVWD | receive len_m1 wdata；these data for preprog & prog |
| WR_ST_PROG0 | CEb=0, PREPG=1, A=Ax；NVR_CFG, NVR, ARRDN[1:0]；get mass_write_flag；do counter until；cnt==maxprg0(tWS) |
| WR_ST_PROG1 | do counter until；cnt==maxprg1(tNVS) |
| WR_ST_WEB | WEb=0, A=Ay, DIN=DIN；do counter until；cnt==maxwe(tADS,tPDS) |
| WR_ST_PRE0 | PROG2=1；do counter until；cnt==maxpre0(tPREPROG) |
| WR_ST_PRE1 | PROG2=0；do counter until；cnt==maxpre1(tADH,tPREPGH) |
| WR_ST_PRE2 | PREPG=0, Ay=Ay, DIN=DIN；do counter until；cnt==maxpre2(tPREPGS) |
| WR_ST_PROG2 | PROG2=1；do counter until；cnt==maxprg2(tPROG) |
| WR_ST_PROG3 | PROG2=0；do counter until；cnt==maxprg3(tPGH) |
| WR_ST_RLS0 | WEb=1；do counter until；cnt==maxrls0(tRCV) |
| WR_ST_RLS1 | PROG=0；do counter until；cnt==maxrls1(tMH) |
| WR_ST_RLS2 | CEb=1；do counter until；cnt==maxrls2(tRW) |

> 图中单项条件：`flash_write`；`rcv_data_done_p`；`cnt==maxprg0`；`cnt==maxprg1`；`cnt==maxwe`；`cnt==maxpre2`；`cnt==maxprg3`；`cnt==maxrls0`；`cnt==maxrls1`；`cnt==maxrls2`。
> 图中复合条件（单个&和竖线按图保留，不改写为HDL）：

```text
cnt==maxpre0 & mass_write_flag==1'b1 & mass_cnt<mass_max
cnt==maxprg2 & mass_write_flag==1'b1 & mass_cnt<mass_max
(cnt==maxprg2 & mass_write_flag==1'b0) |
(cnt==maxprg2 & mass_write_flag==1'b1 & mass_cnt==mass_max)
```

> 转录注：第四轮重新核实四个括号内时序名：tWS、tNVS、tADH/tPREPGH、tPGH，已补入原状态表。
> 图形及连线：[查看原图右页](../images/GameViewer_l6EdkNy5JN.png)。原图中的PROG/PROG2和A/Ay各处写法分别保留。

---

## 原图：[GameViewer_Apm6lwGGlA.png](../images/GameViewer_Apm6lwGGlA.png)

### 【左页】

Flash Write根据SMIC要求，最多只能一次翻转36bit，因此将写入的数据分成高低36bit，分两次分别写入，第一次写入低36bit，高36bit置1，第二次写入高36bit，低36bit置1；

**图2-12 Flash Set Config状态转移图**

| 图中状态 | 可辨框内文字 |
|---|---|
| SETC_ST_IDLE | 原图框内无附加说明 |
| SETC_ST_START | A=AIN, DIN=DIN, CEb=0, WEb=0；get cfg_len_m1；do counter until；cnt==maxs(tCFS,tWFS) |
| SETC_ST_CONF | do counter until；cnt==maxcfg(tCONFEN) |
| SETC_ST_RLS0 | do counter until；cnt==maxwh(tWFH,tCFH), when cfg_len_m1==0；cnt==maxwh(tWFH), when cfg_len_m1>0 |
| SETC_ST_WAIT | WEb=1 |
| SETC_ST_RLS1 | do counter until；cnt==maxcf(tCFL) |

> 图中条件：`flash_set_cfg`；`cnt==maxs`；`cnt==maxcfg`；`cnt==maxcf`；`cfg_len_m1>0 & cnt==maxwh & mass_cnt<cfg_len_m1`；`(cfg_len_m1>0 & cnt==maxwh & mass_cnt==cfg_len_m1) | (cfg_len_m1==0)`。
> 图形及连线：[查看原图左页](../images/GameViewer_Apm6lwGGlA.png)。

### 【右页】

**图2-13 Flash Erase状态转移图**

| 图中状态 | 可辨框内文字 |
|---|---|
| ERS_ST_IDLE | 原图框内无附加说明 |
| ERS_ST_START | get chip_erase_flag；A=Ax, CEb=0, CHIP=chip_erase_flag；NVR_CFG, NVR, ARRDN[1:0]；do counter until；cnt==maxs(tWS) |
| ERS_ST_GETCMD | ERAERS=1；do counter until；cnt==maxe(tNVS) |
| ERS_ST_WEB | WEb=0；do counter until；cnt==maxse(tERAERS) when chip_erase_flag==1'b0；cnt==maxse(tSCE) when chip_erase_flag==1'b1 |
| ERS_ST_RLS0 | WEb=1；do counter until；cnt==maxrcv(tRCV) |
| ERS_ST_RLS1 | ERAERS=0, others keep；do counter until；cnt==maxwh(tMH) |
| ERS_ST_RLS2 | CEb=1, CHIP=0；do counter until；cnt==maxrw(tRW) |

> 图中条件：`flash_erase`；`cnt==maxs`；`cnt==maxe`；`cnt==maxse`；`cnt==maxrcv`；`cnt==maxwh`；`cnt==maxrw`。
> 转录注：第四轮重新核实SETC的tCFS/tWFS、tWFH/tCFH、tCFL及ERS的tWS/tNVS，已补入；ERAERS等原图拼写照留。
> 图形及连线：[查看原图右页](../images/GameViewer_Apm6lwGGlA.png)。原图“ERAERS”保留原拼写，不自动改成ERASE。

---

## 原图：[GameViewer_xS9sUaBAU3.png](../images/GameViewer_xS9sUaBAU3.png)

### 【左页】

**图2-14 Flash Read状态转移图**

| 图中状态 | 可辨框内文字 |
|---|---|
| RD_ST_IDLE | when jump to RD_ST_GETCMD；gen RDEN=1, A=AIN, CEb=0, WEb=1；gen NVR_CFG, NVR, ARRDN[1:0]；VREAD=0, RECALL=0；get mass_read_flag；get tck_le_trc_flag(tCK<=tRC) |
| RD_ST_CHANGE | do counter until；cnt==maxs(tMS)；when jump to RD_ST_GETCMD；gen RDEN=1, A=AIN, CEb=0, WEb=1；gen NVR_CFG, NVR, ARRDN[1:0]；VREAD=0, RECALL=0；get mass_read_flag；get tck_le_trc_flag(tCK<=tRC) |
| RD_ST_GETCMD | do counter until；cnt==maxh(tAH)；when mass_read_flag & tck_le_trc_flag；when cnt==maxh, change next Ax/Ay；when jump to RD_ST_IDLE：RDEN=0, others keep |
| RD_ST_WAIT | RDEN=0, others keep；do counter until；cnt==maxrc(tRC) |

> 图中可辨条件文字：`flash_read==1'b1 && read_cmd_lat!=read_cmd`；`flash_read==1'b1 && read_cmd_lat==read_cmd`；`cnt==maxs && tmh_reached==1'b1`；`cnt==maxrc`；`other`。
> 复合条件补录（按原图分组，不简化运算符）：GETCMD回到IDLE：`(cnt==maxh & mass_read_flag==1'b0) | (cnt==maxh && mass_read_flag==1'b1 && mass_cnt==mass_max)`；GETCMD自环：`cnt==maxh && mass_read_flag==1'b1 && tck_le_trc_flag==1'b0 && mass_cnt!=mass_max`；GETCMD进入WAIT：`cnt==maxh && mass_read_flag==1'b1 && tck_le_trc_flag==1'b1`。
> 黄色注释框可辨文字：tmh counter；when RD_ST_GETCMD jump to RD_ST_IDLE；do counter until；`tmh_cnt==maxmh(tMH)`；until cnt==maxmh, tmh_reached=1'b1；other tmh_reached=1'b0；when RD_ST_IDLE or RD_ST_CHANGED jump to RD_ST_GETCMD, then mh_cnt clear；RD_ST_IDLE jump to other state, get read_cmd_lat<=read_cmd。
> 转录注：黄色框中的RD_ST_CHANGED与状态框RD_ST_CHANGE、tmh_cnt与mh_cnt分别保留；这些文字按框内可辨片段分隔，复合条件在第四轮按原图补录。
> ⚠️ 原图待复核（LLD-U09，范围已缩小）：图2-14复合条件和tMS/tMH五列表格已回查；下方两幅波形中的部分微小数值、最后一路信号名及右页波形左下参数名称仍无法逐字确认。保留原图，不将微小数值猜写成正文。
> 图形及连线：[查看原图左页](../images/GameViewer_xS9sUaBAU3.png)。

Flash Main Normal Read时序优化方案见：

`/ET6601-DOC/05.数字设计/03 HAC/03 方案 LRS/EFC/V100/03.设计/02.LLD/《FLASH读时序分析.xlsx》`

将读采样修改为efc_clk，提高读效率

> 转录注：以上方案路径及读采样说明均为原图红字；只恢复路径文字，没有借用该表格或其他芯片资料补充。
> 波形图可辨信号名：efc_clk、flash_clk、RDEN、A[13:0]、read_count[2:0]、efc_tck_ge_trc、cfg_efc_tck_le_trc、DOUT[71:0]。细小数值未猜写，原始波形及数值见[原图左页下方](../images/GameViewer_xS9sUaBAU3.png)。

### 【右页】

> 上方波形图可辨文字：flash_clk@25MHz、efc_clk@200MHz、RDEN、DOUT；时间刻度0ns、5ns、10ns、15ns、20ns、25ns、30ns、35ns、40ns。最后一路信号名及左下参数表的逐行文字仍在LLD-U09范围；原始波形与参数表见[原图右页上方](../images/GameViewer_xS9sUaBAU3.png)。

FLASH读模式切换tMH/tMS时间优化：

> 转录注：以下两行表格未显示列标题，使用“转录列1～5”仅定位原图列，不推断第3、4列的min/typ/max属性；空列照留。

| 转录列1 | 转录列2 | 转录列3 | 转录列4 | 转录列5 |
|---|---|---|---|---|
| tMS | Read Modes: RECALL/VREAD1 read (CLOCK rising edge @RDEN=1)<br>setup time | 5 |  | us |
| tMH | Read Modes: RECALL/VREAD1 read (CLOCK rising edge @RDEN=1)<br>hold time | 100 |  | ns |

工规FLASH MARCO一共三种读模式Normal Read、Recall Read、Vread1。

ET6601方案中存在以下问题：

1、ET6001、ET6601为了满足READMODE的RDEN使能后的HOLD时序tMH，三种读模式在每次进行最后一个读操作之后都进行了等待，降低了连续读的性能；

> 转录注：本页优化标题、三种读模式说明及ET6601问题段为原图红字。“MARCO”和Vread1按原文保留；问题单、代码和完整优化方案已在后续三张原页中核对衔接。

---


## 原图：[GameViewer_Jv14xpHsSC.png](../images/GameViewer_Jv14xpHsSC.png)

### 【左页】

**原页嵌入问题单：[EFC-BT] APB与AXI同时对NVR和MAIN进行访问时功能出错**

> 转录注：以下为原文内嵌问题单，不是本轮新建的问题单。可辨的字段逐项保留；缩小在原页内的文字不作猜补。

| 原字段 | 可辨原文 |
|---|---|
| 标题 | [EFC-BT] APB与AXI同时对NVR和MAIN进行访问时功能出错 |
| 添加/更新时间 | 将近2年之前添加；更新于将近2年之前 |
| 状态 | 可辨片段“设计经理”“已解决”；完整状态文字待复核，见LLD-U10 |
| 优先级 | 严重 |
| 指派给 | 姓名字形待复核，见LLD-U10 |
| 问题模块 | 数字HAC |
| 验证阶段 | BT |
| 计划完成日期 | 原截图留空 |
| 模块 | 原截图留空 |
| 描述 | 可辨片段：APB接口、AXI接口、NVR和MAIN地址空间、基本读写功能出错、请设计修改代码、谢谢～；完整逐字文本见LLD-U10 |
| 文件 | 两个PNG附件；大小分别为97.6 KB、155 KB；时间分别为2022-08-08 12:31、2022-08-08 12:45；完整文件名后缀待复核 |
| 抄送人员 | 原截图有姓名列表，当前像素不足以逐个确认 |
| 子任务 | 原截图未显示条目 |
| 相关的问题 | 原截图未显示条目 |

> ⚠️ 原图待复核（LLD-U10）：本页问题单的部分姓名、状态末字、完整描述、附件完整文件名，以及右页代码图上方的缩小文字无法逐字符确认。以上“可辨片段”不是完整原文句子，不能拼接成确定正文。保留[完整原页](../images/GameViewer_Jv14xpHsSC.png)，本轮不再用“不是正文”为理由丢弃整个问题单。

### 【右页】

**Figure 2: Synchronous Read Cycle Timing Diagram**

Notes: (1) READ MODE is a group signals to enable read modes, including RECALL, VREAD1.

> 图中文字转录：DOUT、READMODE；D0、D1、D2、D3；tACC、tOH、tMS、tMH。图中tMH区域有红圈。波形边沿和红圈位置以[原图](../images/GameViewer_Jv14xpHsSC.png)为准。

> 转录注：下列为代码截图中可辨的diff片段；保留删除/增加行，不补齐截图外代码，不作为可编译源文件。页面中的代码行号18～38仅用于定位。

```diff
-assign cfg_efc_tol     = 2'd2;
+//modify bug #434, start
+//assign cfg_efc_tol   = 2'd2;
+assign cfg_efc_tol     = cfg_efc_tmh[4:0];
+//modify bug #434, end
 assign cfg_efc_tcrc    = 2'd1;
 assign cfg_efc_tas     = 2'd0;
 assign cfg_efc_tah     = 2'd0;
@@ -878,11 +881,11 @@
 always @(*) begin
     if (recall_flag==1'b1 || vread_flag==1'b1) begin
         maxrc  =    {    cfg_efc_trc_1};
-        maxacc =    {1'b0,cfg_efc_tacc_1} + {4'd0,cfg_efc_tol};
+        maxacc =    {1'b0,cfg_efc_tacc_1} + {1'd0,cfg_efc_tol};
     end
     else begin
         maxrc  =    {2'd0,cfg_efc_trc_0};
-        maxacc =    {2'd0,cfg_efc_tacc_0} + {4'd0,cfg_efc_tol};
+        maxacc =    {2'd0,cfg_efc_tacc_0} + {1'd0,cfg_efc_tol};
     end
 end
```

并且进入READ MODE CHANGE阶段本身应该等待tMH时间逻辑也未生效，实际在等待之前READ MODE就切换了；

> 转录注：上一段为原图红色批注。代码diff记录的是原文中已有问题处理，不自动等同于新增的6601功能。

---

## 原图：[GameViewer_SnGFBV0cqH.png](../images/GameViewer_SnGFBV0cqH.png)

### 【左页】

> 代码截图转录（一）：红框圈出`tmh_reached==1'b1`。缩进只为阅读，不修改可辨的变量、条件和常量。

```verilog
RD_ST_IDLE : begin
    if ((nrmrd_cmdfifo_empty==1'b0 && efc_gclken==1'b1 && read_cmd_lat!=read_cmd) ||
        (ctrl_is_rd_p==1'b1       && efc_gclken==1'b1 && read_cmd_lat!=read_cmd)) begin
        read_nxtst = RD_ST_CHANGE;
    end
    else if ((nrmrd_cmdfifo_empty==1'b0 && efc_gclken==1'b1 && read_cmd_lat==read_cmd) ||
             (ctrl_is_rd_p==1'b1       && efc_gclken==1'b1 && read_cmd_lat==read_cmd)) begin
        read_nxtst = RD_ST_GETCMD;
    end
    else begin
        read_nxtst = RD_ST_IDLE;
    end
end
RD_ST_CHANGE : begin
    if (cnt>={12'd0,maxs} && tmh_reached==1'b1 && efc_gclken==1'b1) begin
        read_nxtst = RD_ST_GETCMD;
    end
    else begin
        read_nxtst = RD_ST_CHANGE;
    end
end
```

> 代码截图转录（二）：对应原代码行381～395；高亮`VREAD1`。

```verilog
always @(posedge efc_clk or negedge por_rst_n) begin
    if (por_rst_n==1'b0) begin
        VREAD1 <= 1'b0;
    end
    else begin
        //fix bug #258 begin, make vread pull up when first retry erase operation
        //if (read_curst==RD_ST_IDLE && read_nxtst!=RD_ST_IDLE) begin
        if ((cmd2flash_if_a_load==1'b1              ) || //apb access, axi write, axi read
            (read_curst==RD_ST_IDLE && read_nxtst!=RD_ST_IDLE)) begin
            //fix bug #258 end
            VREAD1 <= cmd2flash_if_vread;
        end
        else ;
    end
end
```

**2、READ MODE寄存分命令（包含写和擦除）：**

> 代码截图转录（三）：红框和高亮位置包括`fctrl_cmd[CMD_TYPE]`、`read_cmd_lat`及寄存条件。

```verilog
assign read_cmd = (nrmrd_cmdfifo_empty==1'b0) ? (cfg_efc_vread_debug_en ? TYPE_VREAD : nrmrd_cmdfifo_pop_dout[CMD_TYPE]) :
                  fctrl_cmd[CMD_TYPE];
assign efc_tck_gt_trc = (cfg_efc_tck_le_trc==1'b0 && read_cmd_lat==IND_CMD_READ);

always @(posedge efc_clk or negedge efc_rst_n) begin
    if (efc_rst_n==1'b0) begin
        read_cmd_lat <= 4'd0;
    end
    else begin
        if ((ctrl_is_rd_p==1'b1 || ctrl_is_wr_p==1'b1 ||
             ctrl_is_ers_p==1'b1 || nrmrd_cmdfifo_pop==1'b1) && efc_gclken==1'b1) begin
            read_cmd_lat <= read_cmd;
        end
        else ;
    end
end
```

但根据DATASHEET，只需要保证写和擦除时，Recall信号拉低即可，Normal Read、VREAD1和写擦除交叉操作并不需要发生Read Mode切换：

> 转录注：上句为原图红字，末尾“生Read Mode切换：”跨到右页顶部，已连续衔接。

### 【右页】

> 转录注：以下为原页内嵌数据手册表，10个模式行、15列全部转录。红框位于Program/Sector Erase/Chip Erase的RECALL与VREAD1两列；未根据表格推断原文以外的设计。

| MODE | CEb | WEb | DIN | PROG/PROG2 | ERASE | CHIP | DOUT | PORb | CONFEN | ADDR | DPD | RECALL | VREAD1 | RETRY[1:0] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Read | 0 | 1 | X | 0 | 0 | 0 | DOUT | 1 | 0 | AIN | 0 | 0 | 0 | X |
| Program | 0 | 0 | DIN | 1 | 0 | 0 | X | 1 | 0 | AIN | 0 | 0 | X | X |
| Sector Erase | 0 | 0 | X | 0 | 1 | 0 | X | 1 | 0 | AIN | 0 | 0 | X | Note 5 |
| Chip Erase | 0 | 0 | X | 0 | 1 | 1 | X | 1 | 0 | X | 0 | 0 | X | 11 |
| Standby | 1 | 1 | X | 0 | 0 | X | All Zero | 1 | 0 | X | 0 | 0 | X | X |
| Set Config. | 0 | 0 | CBD | 0 | 0 | X | X | 1 | 1 | CBA | 0 | X | X | X |
| Deep Power Down | 1 | 1 | X | 0 | 0 | X | All Zero | 1 | 0 | X | 1 | X | X | X |
| Power On Reset | X | X | X | X | X | X | All Zero | 0 | X | X | X | X | X | X |
| Recall Read | 0 | 1 | X | 0 | 0 | 0 | DOUT | 1 | 0 | AIN | 0 | 1 | 0 | X |
| Verify Read 1 | 0 | 1 | X | 0 | 0 | 0 | DOUT | 1 | 0 | AIN | 0 | 0 | 1 | X |

Notes:

(1) X means either '0' or '1', not other value.  
(2) TMEN=1 to enable test modes. In other cases, it should be 0.  
(3) CBA is the word number of configuration data, using `A<2:0>`, CBD is the configuration data corresponding to the CBA.  
(4) ADDR column includes Address, NVR and NVR_CFG, and ARRDN pins.  
(5) RETRY[1:0] are '11' for single pulse sector erase, or changed regarding to retry order.

**ET6601优化方案为：**

> 转录注：优化方案标题为红字，正文续于下一张；表内X照录，不自行补0或1。

---

## 原图：[GameViewer_isM3FELYfq.png](../images/GameViewer_isM3FELYfq.png)

### 【左页】

> 图中文字转录（本图原页未编号）：`Normal Read`、`Recall Read`、`Vread1`、`Program Or not retry Erase / VREAD1==1'b0`、`Program Or Erase(inc retry) / VREAD1==1'b1`。连线旁有`RD MODE Change`、`RD MODE No Change`、`RD MODE Change Only to Retry`，分别按原图红色/绿色保留含义，不另作版本推断。完整连线见[原图](../images/GameViewer_isM3FELYfq.png)。

1、ET6601中优化为只有Recall Read需要等待tMH，Normal Read、Vread1不等待，提升Normal Read、、Vread1效率；

2、VREAD1在RETRY ERASE操作中提前拉高，在非RETRY ERASE和PROGRAM中保持不变，按照之前代码可能会出现Normal Read的tMH等待时间不够的违例，因此将VREAD1拉高时间修改为tNVS之后：

> 转录注：以下为原图单行参数表；未出现表头，转录列名仅用来定位，不臆定min/max。`A²⁾`中上标是原图脚注，不是位宽。

| 转录列1 | 转录列2 | 转录列3 | 转录列4 | 转录列5 |
|---|---|---|---|---|
| tNVS | PROG/ERASE/CEb/ARRDN/NVR/NVR_CFG/CHIP/A²⁾ to WEb setup time | 4 |  | us |

### 【右页】

**Figure 4: Sector Erase Timing Diagram**

Notes: (1) Ax is X address, means `A<14:7>`.

> 图中文字转录：Ax、WEb、ERASE、CEb、NVR/ARRDN/NVR_CFG、CHIP、RDEN、CLOCK、PROG；tWS、tNVS、tERASE、tRCV、tRW、tWH、tAS；NEXT ERASE、NEXT READ、NEXT PROGRAM。原图红框圈出tNVS；波形边沿和间隔按原图保留，不换算成推断时序。

3、进入Program、ERASE时都将Recall拉低；（与ET6601方案保持一致）

4、进入READ模式时，只根据VREAD1和Recall信号的变化记录的READ MODE来决定是否要等待tMS，而不是每次ERASE/PROGRAM都认为READ MODE发生过变化；

> 转录注：本图四项方案正文均为红字，“Normal Read、、Vread1”的重复顿号以及第3项“与ET6601方案保持一致”均按原文保留。

#### 2.3.5 FCTRL_GFB_FLASH_IF

根据状态机信息进行具体接口信号的生成；

---

## 原图：[GameViewer_98qp0YcXAk.png](../images/GameViewer_98qp0YcXAk.png)

### 【左页】

开启ECC和ECC_WR_RVS时，对于写入的ECC 8bit内容的第0、1、4-7bit进行取反，保证写数据为全1时，ECC计算结果8’hC进行处理后也为8’hFF（全1），此时不会对FLASH内容进行改写；

开启ECC和ECC_RD_RVS时，对于读出的ECC 8bit内容的第0、1、4-7bit进行取反，保证ECC校验时ECC数据为写入前未取反的数据。

> 转录注：以上两段为红字；正文`RVS`与图中`rsv`的次序差异照录，不自动统一。

**图2-15 ECC域段翻转写入图**

> 图中文字转录：DFF / 72bit；DIN[71:68],DIN[65:64]；DFT_WRAP；FLASH；PROG；NVR；NVR_CFG；cfg_efc_ecc_wr_rsv；NOT、AND、OR、XOR。左侧另有写分拆/全1判定与ECC使能控制信号，完整字形待LLD-U11复核，不按其他段落补名。
> 图形及连线：[原图左页上图](../images/GameViewer_98qp0YcXAk.png)。

**图2-16 ECC域段翻转写入图**

> 图中文字转录：FLASH；DFT_WRAP；DFF / 72bit；flash_out[71:68],flash_out[65:64]；VREAD1；cfg_efc_ecc_rd_rsv；NOT、AND、XOR。
> 转录注：图2-16图名也写“写入图”，没有因图内读出路径而擅自改为“读出图”。
> ⚠️ 原图待复核（LLD-U11）：图2-15左侧若干控制信号完整拼写在原1920×1080截图中太小；可辨末尾包含`split`、`full`及`ecc_en_r`。只记录这些片段，不将未辨明的字符补成完整信号名。图2-16已按可辨原字形补充，不与正文RVS统一。

### 【右页】

## 第3章 DFX说明

### 3.1 错误说明

1. 写保护错误(wrperr)：

当配置接口/数据接口尝试对受保护区域进行写/擦除操作时，该信号置1．当信号置1后，写/擦除动作终止，不会对数据产生任何改变；

该状态受对应的清零标志清零；

该状态必须清零才能执行新的写/擦除操作，否则会产生编程顺序错误，下一次写/擦除操作也会被终止；（配置接口和数据接口相同）

2. 编程顺序错误(pgserr)：

当编程顺序不正确时，该信号置1．满足以下条件时，即表示编程顺序不正确：

A）数据总线发出了写请求，但cfg_efc_write_en并没有置1．

B）写保护错误标记还未清零，又发出了新的写/擦除操作；

---

## 原图：[GameViewer_bJ7d9eVqlF.png](../images/GameViewer_bJ7d9eVqlF.png)

### 【左页】

C）不一致错误标记还未清零，又发出了新的写/擦除操作；

D）配置ECC 2bit错误标记还未清零，又发出了新的写/擦除操作；

E）数据ECC 2bit错误标记还未清零，又发出了新的写/擦除操作；

该状态受对应的清零标志清零；

该状态必须清零才能执行新的写/擦除操作，否则会产生编程顺序错误，下一次写/擦除操作也会被终止，读操作会返回总线ERROR；（配置接口和数据接口相同）

3. 选通错误(strberr)：

当数据接口连续2次以上向同一个地址写同一字节时，该信号置1．当信号置1后，写动作不会终止，应用程序可忽略该错误，继续执行当前写操作，并可以继续执行新的写/擦除操作；

该状态受对应的清零标志清零；

该状态不须清零也可以执行新的写/擦除操作；

4. 不一致错误(incerr)：

当配置接口上一笔命令还未执行完成，配置接口再次发出新的命令，就发生不一致错误，并且新的命令不会被执行；

> 转录注：上一句跨左右页连续。选通错误段中的“不会终止”及“不须清零”句为青蓝字，另列蓝字记录，不冒充6601新增要求。

### 【右页】

该状态受对应的清零标志清零；

对于配置接口，该状态必须清零才能执行新的写/擦除操作，否则会产生编程顺序错误，下一次写/擦除操作也会被终止；

数据接口不受该错误影响；

5. 配置ECC1bit错误：

配置接口读取NVR / NVR_CFG时，发生ECC1bit错误，并纠错，该信号置1．当信号置1后，读取返回数据正确，应用程序可忽略该错误，继续执行当前读操作，以及下一步操作（不需要对当前地址进行retry处理）；

该状态受对应的清零标志清零；

该状态不须清零也可以执行新的读/写/擦除操作；

6. 配置ECC2bit错误：

配置接口读取NVR / NVR_CFG时，发生ECC2bit错误，该信号置1．当信号置1后，读取返回数据不正确，应用程序无法忽略该错误，需要对当前地址进行retry处理或其他动作；

该状态受对应的清零标志清零；

对于配置接口，该状态必须清零才可以执行新的读/写/擦除操作；

> 转录注：最后一句的“操作；”在下一张左页顶部，已衔接，下一张不重复。原图中的青蓝色清零要求与蓝色“不正确”另列来源标记。

---

## 原图：[GameViewer_hoWrmQ3kyX.png](../images/GameViewer_hoWrmQ3kyX.png)

### 【左页】

数据接口不受该错误影响；

7. 数据ECC1bit错误：

数据接口读取Main/RDN时，发生ECC1bit错误，并纠错，该信号置1．当信号置1后，读取返回数据正确，应用程序可忽略该错误，继续执行当前读操作，以及下一步操作（不需要对当前操作进行retry处理）；

该状态受对应的清零标志清零；

该状态不须清零也可以执行新的读/写/擦除操作；

8. 数据ECC2bit错误：

数据接口读取Main/RDN时，发生ECC2bit错误，该信号置1．当信号置1后，读取返回数据不正确，应用程序无法忽略该错误，需要对当前操作进行retry处理或其他动作；

该状态受对应的清零标志清零；

对于配置接口，该状态必须清零才能执行新的擦除操作，否则会产生编程顺序错误，下一次擦除操作也会被终止；

对于数据接口，该状态必须清零才能执行新的写/擦除操作，否则会产生编程顺序错误，下一次写/擦除操作也会被终止；

### 【右页】

在该错误未清零前，新的读操作也不再执行，总线数据返回0，RESP返回ERROR；

9. 门控APB总线访问错误：

当EFC的gating产生时，APB总线上还有数据交互未完成或来了新的总线命令；

该状态不须清零也可以执行新的读/写/擦除操作；

上报中断，总线数据返回0，RESP返回ERROR；

10. 复位APB总线访问错误：

当EFC的复位产生时，APB总线上还有数据交互未完成或来了新的总线命令；

该状态不须清零也可以执行新的读/写/擦除操作；

上报中断，总线数据返回0，RESP返回ERROR；

11. 门控AXI总线保护错误：

当EFC的gating产生时，AXI总线上还有数据交互未完成或来了新的总线命令，总线保护模块将总线未完成的交互模拟完成，避免总线挂死；

该状态不须清零也可以执行新的读/写/擦除操作；

上报中断，总线数据返回0，RESP返回ERROR；

> 转录注：第7项及第9～11项的“不须清零”句为青蓝色，第8项“不正确”为蓝色。全部分别照录，没有把数据接口与配置接口的要求统一。

---

## 原图：[GameViewer_OCJBCUSbNK.png](../images/GameViewer_OCJBCUSbNK.png)

### 【左页】

12. 复位AXI总线保护错误：

当EFC的复位产生时，AXI总线上还有数据交互未完成或来了新的总线命令，总线保护模块将总线未完成的交互模拟完成，避免总线挂死；

该状态不须清零也可以执行新的读/写/擦除操作；

上报中断，总线数据返回0，RESP返回ERROR；

13. FLASH配置总线发生读写保护记录：

当FLASH通过apb通路读写flash颗粒时发生违反读写保护时，分别记录违反的第一个地址。

### 3.2 DFX设计

1. ECC错误注入（模拟ECC错误产生）：

由于Flash的特殊性（写入数据后无法直接更新，需要擦除后再写入，并且Flash本身有擦除寿命），因此尽量减少对Flash的写入动作，ECC错误注入在读取时进行模拟；因此，该功能在EFC_GFB/GFB_IF模块内实现；

### 【右页】

**图3-1 ECC错误注入对应寄存器配置**

| 序号 | 配置 | 默认值 | 说明 |
|---:|---|---|---|
| 1 | cfg_efc_ecc_errgen_en_r | 1'b0 | ECC错误注入使能&lt;br&gt;<br>1'b0：不打开ECC错误注入；&lt;br&gt;<br>1'b1：打开ECC错误注入； |
| 2 | cfg_efc_ecc_errgen_type_r | 2'd0 | ECC错误注入类型：&lt;br&gt;<br>0：单bit错误；&lt;br&gt;<br>1：2bit错误；&lt;br&gt;<br>other：更多bit错误； |
| 3 | cfg_efc_ecc_errgen_addr_r | 16'd0 | ECC错误注入对应地址 |
| 4 | cfg_efc_ecc_errgen_sec_r |  | 地址对应sector范围：&lt;br/&gt;<br>0: NVR_CFG；&lt;br/&gt;<br>1: NVR；&lt;br/&gt;<br>2: RDN；&lt;br/&gt;<br>3: Main； |

> 转录注：第4项默认值在图中留空，不按位宽或枚举推断。图内说明显示的`<br>`/`<br/>`作为原始标记保留；表格真正的换行仅用于阅读。原图图号仍是图3-1，未擅改为表3-1。

---

## 原图：[GameViewer_x2k55BuYBA.png](../images/GameViewer_x2k55BuYBA.png)

### 【左页】

## 第4章 系统评估

### 4.1 读性能评估

**图4-1 读数datapath示意图**

> 图中文字转录：EFC；EFC_pipe1；EFC_GFB1；ECC_CORR (1D)；CMD_MUX (0D)；GFB_IF (0D)；RD_MUX (0D)；S40_FCTRL (2D)；FLASH (3*Len+1)；EFC_pipe0；EFC_GFB0；AXIM_PROC (1D)；CACHE (7+Len)；AXI_MASTER；1pluse per 7 ck。
> 连线及层级保留[原图](../images/GameViewer_x2k55BuYBA.png)。`1pluse`按图中拼写照录，不自动修正为pulse。

Cache处为两级pipeline交互的点；

pipeline0，总线读取Cache：

当数据连续访问时，latency=1拍，且两次数据读取之间间隔1cycle的控制时间；

### 【右页】

当数据不是连续时，根据不同的情况花费的时间会有区别。

pipeline1，Cache到Flash读取数据，最少1拍发出一个读取申请，latency=2+3*Len+1+1=4+3*Len；

因此最终瓶颈体现在Flash，正常情况下，可以得到Flash的满带宽性能（数据跳着访问的除外，可能还会因为Flash多读取数据，导致整体效率变差。当然，平均的latency会变小）；

---

## 原图：[GameViewer_b5AJYTEhY1.png](../images/GameViewer_b5AJYTEhY1.png)

### 【左页】

### 4.2 写性能评估

**图4-2 写数datapath示意图**

> 图中文字转录：EFC；EFC_GFB；AXI_MASTER；AXIM_PROC (1D)；CACHE (1D)；CMD_MUX (0D)；ECC_GEN (1D)；GFB_CTRL (0D)；GFB_IF (1D)；S40_FCTRL (2D)；FLASH (xMS)。图形及连线保留[原图](../images/GameViewer_b5AJYTEhY1.png)。

写数据时，性能瓶颈在FLASH处，可以提升的地方就只在连续编程上；

单次（72bit）编程大概39us -- 约1.85Mbps；

分两次36bit编程大概78us—约0.925Mbps；

### 【右页】

连续编程，那么72bit在Burst16下可以缩到31us左右 -- 约2.32Mbps；

连续编程，那么72bit分两次写入在Burst16下可以缩到60us左右 -- 约1.21Mbps；

与SMIC交流后，不能实现更长的Burst编程--有预编程和编程两个阶段，都需要对应的地址和数据，也就意味着需要数据缓存，这一版确定缓存16个数据；

> 转录注：上一段为原图青蓝色文字；性能数值均为原文评估，不是本轮实测。

### 4.3 擦除性能评估

数据擦除时，datasheet中给出的典型擦除时间是8~20ms，根据SMIC回复，可以直接使用8ms：

1）sector擦除性能=1KB/8ms=125KBps；

2）整片擦除性能=512KB/8ms=64MBps；

块擦除时，使用RETRY模式可能会有一定的时间节省，单次sector RETRY擦除是0.8ms~1ms + VREAD读取200ns*128=26us，需要RETRY擦除多少次不确定；如果只擦除一次，那么sector擦除性能可以提升到：1KB/1ms=1MBps；

> 转录注：原图此处为VREAD，没有末尾数字2；KB、MB、Mbps和近似计算分别照录，不按计算结果或其他芯片参数改写。

---

## 原图：[GameViewer_f9t1x50Gvk.png](../images/GameViewer_f9t1x50Gvk.png)

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
| ~~10~~ | ~~BOOTROM~~ | ~~NVR_CFG 的 PR0、PR1 信息，需要 bootrom 中进行读取，并配置这个替换内容到 efc 对应寄存器上，保证程序功能的正确性；~~ |
| 11 | 软件 | OTA 切换时，cpu cache 需要被 disable，保证进行 OTA 切换时软件不会访问 Flash； |

**注：要求确认后，添加到钉钉共享文档，做为系统待办，便于统一跟踪。**

> 转录注：该表横跨左右页，第5行的复位撤销顺序已连续衔接；第10行整行删除线按原图保留，其中为`PR0`（数字0），不是`PRO`（字母O）。底部注为蓝字；本轮没有执行其提及的钉钉操作。

---

## 原图：[GameViewer_vC7gPIngZA.png](../images/GameViewer_vC7gPIngZA.png)

### 【左页】

**图5-1 efc_clk和flash_clk时钟关系示意图**

> 图中文字转录：三组时钟关系波形，每组均为efc_clk、flash_clk、efc_gclken、por_rst_n、efc_rst_n；两复位撤销之间标注T>0。原始边沿、阴影区和三组相位分别保留[原图](../images/GameViewer_vC7gPIngZA.png)，不据时钟常识重画。

## 第6章 测试相关

> 转录注：原表“内部接口／内部FIFO”是一个单元格内的两行字，SVA列为一个勾；“性能／BOOT”也是一个单元格内的两行字，FPGA列为一个勾。下面保持这两组单元格，不能拆成六个独立测试行再将勾分配给某个子项。续表在右页顶部。

| 测试点 | UT | SVA | IT | FPGA |
|---|---|---|---|---|
| 正常功能 | √ |  |  |  |
| 内部接口<br>内部FIFO |  | √ |  |  |
| 连接关系 |  |  | √ |  |
| 性能<br>BOOT |  |  |  | √ |

### 【右页】

为FPGA测试，编写verilog代码eflash_fpga.v用于模拟eFlash的功能行为（可综合）；那么EFC的整个功能都可得到测试，也可测试到EFC在系统中的行为（不可测试eFlash的时序，因为时序需要在UT测试保证）；

---

## 原图：[GameViewer_V6W79lgJB6.png](../images/GameViewer_V6W79lgJB6.png)

### 【左页】

# 参考文献

[1] 《ET6001 EFC模块需求规格书》  
[2] 《Pegasus EFC模块修改方案》  
[3] S40NEF64KX72_S0_Application_Notes.pdf  
[4] S40NEF64KX72_S0_Datasheet.pdf  
[5] ST_AN2606.pdf  
[6] STM32H7x3 参考手册.pdf  
[7] TMS320F28004x Real-Time Microcontrollers Technical Reference Manual

### 【右页】

> 转录注：原图右页无文档正文。以上仅转录原作者列出的文献，不代表本轮读取或以这些文献补充正文。

---

## 第二部分：截图明确标注的 ET6601 修改点

### A. 已对原图核对的修订与标记证据

覆盖36张原图。C01～C41保留既有核对记录；本轮新增C42～C52共11条原图出现位置记录。**52条是来源记录数，不是52项独立功能新增**。C01为修订基线，C02为明确ET6601修订；红字、删除线、标题与路径的性质逐条区分。旧值未写明时不编造“旧值→新值”；第25张代码中的历史bug编号不能自动归属于ET6601新增功能。

| 编号 | 原图文字 | 原文位置 | 原图标记／可确定的修改性质 | 原图 |
|---|---|---|---|---|
| C01 | 从ET6003 EFC模块详细设计文档复制，参考ET6801进行修改 | 表1-1修订记录，1.0；20260715；周玮玮 | 修订基线说明，不是独立功能修改 | [GameViewer_Ts8jfg57vy.png](../images/GameViewer_Ts8jfg57vy.png) |
| C02 | 根据ET6601 OR-DR更新，新增64KX72=512KB的PFLASH，原有FLASH回退为DFLASH | 表1-1修订记录，1.1；20260922；周玮玮 | 明确写出新增PFLASH、原有FLASH回退为DFLASH | [GameViewer_Ts8jfg57vy.png](../images/GameViewer_Ts8jfg57vy.png) |
| C03 | rom_rd_en；输入；ROM SECTOR读保护信号有效指示，由sysc模块送出 | 表1-1 EFC_DFLASH接口信号说明／OTP相关 | 整行红字；不推断旧信号或旧权限 | [GameViewer_kreeGdjIJX.png](../images/GameViewer_kreeGdjIJX.png) |
| C04 | sysc_boot_exit_lockj；输入；BOOT退出锁定，控制OTP寄存器读写权限，由SYSC模块配置下发 | 表1-1 EFC_DFLASH／OTP相关 | 整行红字；信号末尾j按图保留 | [GameViewer_kreeGdjIJX.png](../images/GameViewer_kreeGdjIJX.png) |
| C05 | uid[255:0] | 表1-1 EFC_DFLASH／OTP相关 | 仅255标红；原图未给旧位宽 | [GameViewer_kreeGdjIJX.png](../images/GameViewer_kreeGdjIJX.png) |
| C06 | cpld_limit_n；输出；CPLD限定使能 | 表1-1 EFC_DFLASH／OTP相关 | 整行红字 | [GameViewer_kreeGdjIJX.png](../images/GameViewer_kreeGdjIJX.png) |
| C07 | cpld_dbg_dis_n；输出；CPLD JTAG接口调试禁止 | 表1-1 EFC_DFLASH／OTP相关 | 整行红字 | [GameViewer_kreeGdjIJX.png](../images/GameViewer_kreeGdjIJX.png) |
| C08 | nvrcfg_unlock[7:0]；输出；pflash1/dflash nvr_cfg空间的读/写/擦除保护<br>0x00：打开保护，数据不能被读/写/擦除；<br>其他：关闭保护，数据能被读/写/擦除； | 表1-1 EFC_DFLASH／OTP相关 | 整行红字；保留0x00，不与PFLASH表的0x5A统一 | [GameViewer_kreeGdjIJX.png](../images/GameViewer_kreeGdjIJX.png) |
| C09 | DFLASH强制擦除PFLASH MAIN指示 | 表1-1 EFC_DFLASH／PFLASH相关／secure_erase_main | 其中DFLASH标红；该行方向为输出 | [GameViewer_kreeGdjIJX.png](../images/GameViewer_kreeGdjIJX.png) |
| C10 | 复位表示Flash电源关闭，由POR提供；<br>该复位有效时，efc_rst_n必然有效，由CRG实现； | 表1-2 EFC_PFLASH／电源相关／por_rst_n | 说明中这两句标红，前一句低电平有效为黑字 | [GameViewer_kpuE7cPAm8.png](../images/GameViewer_kpuE7cPAm8.png) |
| C11 | flash硬件por复位信号，低电平有效 | 表1-2 EFC_PFLASH／电源相关／flash_por_rst_n | 说明标红；信号名未标红 | [GameViewer_kpuE7cPAm8.png](../images/GameViewer_kpuE7cPAm8.png) |
| C12 | PFLASH收到DFLASH0强制擦除FLASH MAIN指示 | 表1-2 EFC_PFLASH／SECURE_ERASE/OTP相关／secure_erase_main_df | 其中PFLASH标红；原文DFLASH0照录 | [GameViewer_kpuE7cPAm8.png](../images/GameViewer_kpuE7cPAm8.png) |
| C13 | nvr_shift_done<br>CRG可以根据该信号，撤销CPU的复位，让CPU开始进行Boot动作；<br>内部增加超时机制，超时后拉高； | 表1-2 EFC_PFLASH／CRG | 信号名及所列两条说明标红；Option准备好说明为黑字 | [GameViewer_kpuE7cPAm8.png](../images/GameViewer_kpuE7cPAm8.png) |
| C14 | EFC内部CORE工作频率变化时，FLASH时钟频率也随之变化 | 2.1 EFC_CFG／CFG_FLASH_IDS／timing说明 | 红字；不是本轮推导的时钟设计结论 | [GameViewer_MhzCnwHL7y.png](../images/GameViewer_MhzCnwHL7y.png) |
| C15 | 可根据各timing参数自动计算对应的ids寄存器值。 | 2.1 EFC_CFG／CFG_FLASH_IDS／timing说明 | 红字 | [GameViewer_MhzCnwHL7y.png](../images/GameViewer_MhzCnwHL7y.png) |
| C16 | flash_main_rdp_n[31:0],flash_main_wrp_n[31:0] | 左页EFC_RESET子过程清单 | 两处31标红；未给旧位宽 | [GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png) |
| C17 | flash_nvr_rdp_n[0],flash_nvr_wrp_n[0] | 左页EFC_RESET子过程清单 | 两处0标红；未给旧下标 | [GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png) |
| C18 | ~~nSWBOOT1,nBOOT1~~ | 左页EFC_RESET子过程清单 | 原图删除线；保留被删除内容，不作为未删除的有效条目 | [GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png) |
| C19 | flash_nvr_otp_n[7:0][4:0] | 左页EFC_RESET子过程清单 | 红字；双重下标照录 | [GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png) |
| C20 | flash_main_rdp_n[31:0],flash_main_wrp_n[31:0] | 右页硬复位读取清单 | 两处31标红；未给旧位宽 | [GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png) |
| C21 | flash_nvr_rdp_n[0],flash_nvr_wrp_n[0] | 右页硬复位读取清单 | 两处0标红；未给旧下标 | [GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png) |
| C22 | ~~nSWBOOT1,nBOOT1~~ | 右页硬复位读取清单 | 原图删除线；保留被删除内容，不作为未删除的有效条目 | [GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png) |
| C23 | flash_nvr_otp_n[7:0][4:0] | 右页硬复位读取清单 | 红字；双重下标照录 | [GameViewer_Fio2eDanFe.png](../images/GameViewer_Fio2eDanFe.png) |
| C24 | 并进行多数判决 | 2.2.3.1 输出ROM/OTP锁存信息 | 红字 | [GameViewer_AUvuEbreZL.png](../images/GameViewer_AUvuEbreZL.png) |
| C25 | cpld_limit_n[7:0] | 2.2.3.1 ROM/OTP输出清单 | 红字 | [GameViewer_AUvuEbreZL.png](../images/GameViewer_AUvuEbreZL.png) |
| C26 | cpld_dbg_dis_n[7:0] | 2.2.3.1 ROM/OTP输出清单 | 红字 | [GameViewer_AUvuEbreZL.png](../images/GameViewer_AUvuEbreZL.png) |
| C27 | uid[255:0] | 2.2.3.1 ROM/OTP输出清单 | 仅255标红；不推断旧位宽 | [GameViewer_AUvuEbreZL.png](../images/GameViewer_AUvuEbreZL.png) |
| C28 | 3、通过上电读取NVR USER OTP Sector的flash_nvr_otp_n，用户OTP保护区域自动屏蔽擦除操作，并且返回CMD_ERR； | 2.2.5 保护说明第3条 | 整条红字 | [GameViewer_xLTLahbgSa.png](../images/GameViewer_xLTLahbgSa.png) |
| C29 | rom_rd_en | 2.2.5 保护说明第4条 | 寄存器名红字 | [GameViewer_xLTLahbgSa.png](../images/GameViewer_xLTLahbgSa.png) |
| C30 | sysc_boot_exit_lockj | 2.2.5 保护说明第5条 | 寄存器名红字；第5条跨左右页 | [GameViewer_xLTLahbgSa.png](../images/GameViewer_xLTLahbgSa.png) |
| C31 | flash USER OPTION BYTES (nvr sector8) | 2.2.5.1 全片擦除顺序第2步 | 仅8标红 | [GameViewer_xLTLahbgSa.png](../images/GameViewer_xLTLahbgSa.png) |
| C32 | 3)flash USER OTP(nvr sector9~13)； | 2.2.5.1 全片擦除顺序第3步 | 整条红字 | [GameViewer_xLTLahbgSa.png](../images/GameViewer_xLTLahbgSa.png) |
| C33 | sysc_boot_exit_lockj | 2.2.5.1 命令保护寄存器说明b） | 寄存器名红字；后续句在下一张 | [GameViewer_xLTLahbgSa.png](../images/GameViewer_xLTLahbgSa.png) |
| C34 | sysc_boot_exit_lockj | 2.2.5.1 otp读写访问说明 | 寄存器名红字 | [GameViewer_QiBBFQjMG4.png](../images/GameViewer_QiBBFQjMG4.png) |
| C35 | rom_rd_en | 2.2.5.1 rom读访问说明 | 寄存器名红字 | [GameViewer_QiBBFQjMG4.png](../images/GameViewer_QiBBFQjMG4.png) |
| C36 | 复位表示Flash电源关闭，由系统提供；<br>该复位有效时，efc_rst_n必然有效； | 表2-1 电源相关／por_rst_n | 两句红字；前一句黑字未混入 | [GameViewer_zQvGQlgTkE.png](../images/GameViewer_zQvGQlgTkE.png) |
| C37 | /ET6601-DOC/05.数字设计/03 HAC/03 方案 LRS/EFC/V100/03.设计/02.LLD/《FLASH读时序分析.xlsx》 | 图2-14后 Flash Main Normal Read方案路径 | 红字来源路径；不等于独立功能修改，未读取所引用文件 | [GameViewer_xS9sUaBAU3.png](../images/GameViewer_xS9sUaBAU3.png) |
| C38 | 将读采样修改为efc_clk，提高读效率 | 图2-14后 Flash Main Normal Read优化说明 | 红字明确写出读采样修改 | [GameViewer_xS9sUaBAU3.png](../images/GameViewer_xS9sUaBAU3.png) |
| C39 | FLASH读模式切换tMH/tMS时间优化： | 右页优化说明标题 | 红字标题；不等于独立功能修改 | [GameViewer_xS9sUaBAU3.png](../images/GameViewer_xS9sUaBAU3.png) |
| C40 | 工规FLASH MARCO一共三种读模式Normal Read、Recall Read、Vread1。 | 右页tMH/tMS说明 | 红字；MARCO原拼写照录 | [GameViewer_xS9sUaBAU3.png](../images/GameViewer_xS9sUaBAU3.png) |
| C41 | ET6601方案中存在以下问题：<br>1、ET6001、ET6601为了满足READMODE的RDEN使能后的HOLD时序tMH，三种读模式在每次进行最后一个读操作之后都进行了等待，降低了连续读的性能； | 右页tMH/tMS优化问题 | 红字明确点名ET6601问题；后续方案见C42～C49 | [GameViewer_xS9sUaBAU3.png](../images/GameViewer_xS9sUaBAU3.png) |
| C42 | 并且进入READ MODE CHANGE阶段本身应该等待tMH时间逻辑也未生效，实际在等待之前READ MODE就切换了； | READ MODE CHANGE批注 | 红字明确指出时序逻辑问题 | [GameViewer_Jv14xpHsSC.png](../images/GameViewer_Jv14xpHsSC.png) |
| C43 | 2、READ MODE寄存分命令（包含写和擦除）： | 代码截图（三）标题 | 红字标题，具体寄存代码保持原图 | [GameViewer_SnGFBV0cqH.png](../images/GameViewer_SnGFBV0cqH.png) |
| C44 | 但根据DATASHEET，只需要保证写和擦除时，Recall信号拉低即可，Normal Read、VREAD1和写擦除交叉操作并不需要发生Read Mode切换： | 跨左右页批注 | 红字作者说明；没有外查DATASHEET | [GameViewer_SnGFBV0cqH.png](../images/GameViewer_SnGFBV0cqH.png) |
| C45 | ET6601优化方案为： | 右页模式表后 | 明确点名ET6601的红字引导标题 | [GameViewer_SnGFBV0cqH.png](../images/GameViewer_SnGFBV0cqH.png) |
| C46 | 1、ET6601中优化为只有Recall Read需要等待tMH，Normal Read、Vread1不等待，提升Normal Read、、Vread1效率； | 优化方案第1项 | 红字明确给出优化；重复顿号保留 | [GameViewer_isM3FELYfq.png](../images/GameViewer_isM3FELYfq.png) |
| C47 | 2、VREAD1在RETRY ERASE操作中提前拉高，在非RETRY ERASE和PROGRAM中保持不变，按照之前代码可能会出现Normal Read的tMH等待时间不够的违例，因此将VREAD1拉高时间修改为tNVS之后： | 优化方案第2项 | 红字明确给出VREAD1拉高时刻修改 | [GameViewer_isM3FELYfq.png](../images/GameViewer_isM3FELYfq.png) |
| C48 | 3、进入Program、ERASE时都将Recall拉低；（与ET6601方案保持一致） | 优化方案第3项 | 红字；原文注明保持一致，不包装成新增 | [GameViewer_isM3FELYfq.png](../images/GameViewer_isM3FELYfq.png) |
| C49 | 4、进入READ模式时，只根据VREAD1和Recall信号的变化记录的READ MODE来决定是否要等待tMS，而不是每次ERASE/PROGRAM都认为READ MODE发生过变化； | 优化方案第4项 | 红字明确给出模式判定方式 | [GameViewer_isM3FELYfq.png](../images/GameViewer_isM3FELYfq.png) |
| C50 | 开启ECC和ECC_WR_RVS时，对于写入的ECC 8bit内容的第0、1、4-7bit进行取反，保证写数据为全1时，ECC计算结果8’hC进行处理后也为8’hFF（全1），此时不会对FLASH内容进行改写； | 2.3.5 FCTRL_GFB_FLASH_IF后 | 红字；保留8’hC原字面，不做ECC推导 | [GameViewer_98qp0YcXAk.png](../images/GameViewer_98qp0YcXAk.png) |
| C51 | 开启ECC和ECC_RD_RVS时，对于读出的ECC 8bit内容的第0、1、4-7bit进行取反，保证ECC校验时ECC数据为写入前未取反的数据。 | 图2-15之前 | 红字；不推断旧实现 | [GameViewer_98qp0YcXAk.png](../images/GameViewer_98qp0YcXAk.png) |
| C52 | ~~10~~；~~BOOTROM~~；~~NVR_CFG的PR0、PR1信息，需要bootrom中进行读取，并配置这个替换内容到efc对应寄存器上，保证程序功能的正确性；~~ | 第5章 对外要求表第10行 | 原图整行删除线；删除内容仍保留定位 | [GameViewer_f9t1x50Gvk.png](../images/GameViewer_f9t1x50Gvk.png) |

### B. 原图蓝字说明，单列不冒充确定修改

| 编号 | 原图文字 | 位置及颜色说明 | 原图 |
|---|---|---|---|
| B01 | 特别说明：在STM32、TI设计中，都是基于几个固定频率来配置Flash接口的timing参数；在当前设计中，是对所有timing参数都进行了配置（目的：a. 支持任意频率；b. 对Flash时序有更大的容错空间） | 2.1 CFG_FLASH_IDS，整段蓝字；这是作者说明，不是在本轮做外部厂商比较 | [GameViewer_MhzCnwHL7y.png](../images/GameViewer_MhzCnwHL7y.png) |
| B02 | “default参数为25MHz频率下参数，当”<br>“，软件配置timing参数来进行适配，” | 2.1 CFG_FLASH_IDS，同一段的两段蓝字；之间及之后的红字分别见C14、C15，未把不连续文字拼成原句 | [GameViewer_MhzCnwHL7y.png](../images/GameViewer_MhzCnwHL7y.png) |
| B03 | READ、RECALL操作，会经过ECC_CORR，进行ECC检测和纠错； | ECC/RD_DMUX说明；原图青蓝色，不推断新增性质 | [GameViewer_Pi2p76SFY0.png](../images/GameViewer_Pi2p76SFY0.png) |
| B04 | VREAD_CHK（含Retry的VREAD_CHK）操作，直接检测GFB_IF进来的数据是否全1，不经过ECC_CORR，目的是检查擦除操作是否擦干净，ECC域段和DATA域段都必须为全1,； | ECC/RD_DMUX说明；原图青蓝色；重复标点照留 | [GameViewer_Pi2p76SFY0.png](../images/GameViewer_Pi2p76SFY0.png) |
| B05 | 注意：在power_off状态下，需要将Flash所有的输入接0； | 2.3.3 FCTRL_POWER_PROC，原图蓝字；仅恢复作者说明，不外查引用PDF | [GameViewer_ceValKI1oj.png](../images/GameViewer_ceValKI1oj.png) |
| B06 | 当信号置1后，写动作不会终止，应用程序可忽略该错误，继续执行当前写操作，并可以继续执行新的写/擦除操作；<br>该状态不须清零也可以执行新的写/擦除操作； | 3.1 选通错误，青蓝字片段；两处分别引用 | [GameViewer_bJ7d9eVqlF.png](../images/GameViewer_bJ7d9eVqlF.png) |
| B07 | 该状态不须清零也可以执行新的读/写/擦除操作； | 3.1 配置ECC1bit错误，青蓝字 | [GameViewer_bJ7d9eVqlF.png](../images/GameViewer_bJ7d9eVqlF.png) |
| B08 | 不正确<br>对于配置接口，该状态必须清零才可以执行新的读/写/擦除操作； | 3.1 配置ECC2bit错误；蓝色词及青蓝色句，非连续文字，末句跨到下一张 | [GameViewer_bJ7d9eVqlF.png](../images/GameViewer_bJ7d9eVqlF.png) |
| B09 | 该状态不须清零也可以执行新的读/写/擦除操作； | 3.1 数据ECC1bit错误，青蓝字 | [GameViewer_hoWrmQ3kyX.png](../images/GameViewer_hoWrmQ3kyX.png) |
| B10 | 不正确 | 3.1 数据ECC2bit错误，原词蓝色 | [GameViewer_hoWrmQ3kyX.png](../images/GameViewer_hoWrmQ3kyX.png) |
| B11 | 该状态不须清零也可以执行新的读/写/擦除操作； | 3.1 门控APB总线访问错误，青蓝字 | [GameViewer_hoWrmQ3kyX.png](../images/GameViewer_hoWrmQ3kyX.png) |
| B12 | 该状态不须清零也可以执行新的读/写/擦除操作； | 3.1 复位APB总线访问错误，青蓝字 | [GameViewer_hoWrmQ3kyX.png](../images/GameViewer_hoWrmQ3kyX.png) |
| B13 | 该状态不须清零也可以执行新的读/写/擦除操作； | 3.1 门控AXI总线保护错误，青蓝字 | [GameViewer_hoWrmQ3kyX.png](../images/GameViewer_hoWrmQ3kyX.png) |
| B14 | 该状态不须清零也可以执行新的读/写/擦除操作； | 3.1 复位AXI总线保护错误，青蓝字 | [GameViewer_OCJBCUSbNK.png](../images/GameViewer_OCJBCUSbNK.png) |
| B15 | 与SMIC交流后，不能实现更长的Burst编程--有预编程和编程两个阶段，都需要对应的地址和数据，也就意味着需要数据缓存，这一版确定缓存16个数据； | 4.2 写性能评估，青蓝色作者说明；不作为本轮测试结果 | [GameViewer_b5AJYTEhY1.png](../images/GameViewer_b5AJYTEhY1.png) |
| B16 | 要求确认后，添加到钉钉共享文档，做为系统待办，便于统一跟踪。 | 第5章表格下，蓝字；只转录原文，不执行钉钉操作 | [GameViewer_f9t1x50Gvk.png](../images/GameViewer_f9t1x50Gvk.png) |

> 普通目录链接的蓝色下划线、签名栏横线、图中用于区分时钟域或模块名称的颜色均不计作6601版本修改。蓝字按出现位置单列，不混入C编号数量。

### C. 来源适用边界

第25～36张已完成首轮原图核对，旧“历史记录待核对”区已由C42～C52取代，不再保留两套相互竞争的修改清单。第25张问题单/代码为原文引用的历史材料，不因出现在本文件中就认定为6601新增。模式表中的X、代码diff的增加/删除行、原图色块和删除线均按来源保存。

原图未给出的旧值、需求动机和实现细节不补写。原文相互矛盾的容量、位宽、模块名或时钟范围不在此处强行裁定；统一待确认位置见[EFC提取与验收报告](../../EFC_提取与验收报告.md)。
