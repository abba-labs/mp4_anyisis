# ET6601 XBAR模块需求规格与设计方案

> 独立XBAR原文；旧目录和文件名中的SARC仅为历史路径，不属于SARC正文，也不是总线矩阵规格。
> 2026-10-06，第2批。XBAR前11/27张已完成首轮原图核对；全仓135/200。25条修改来源位置记录，3组局部缺口；数量不是独立功能数或准确率。
> 一份原文一份Markdown。先左后右，按章节、跨页句与续表衔接；原文矛盾、拼写、空白和删除线保留。未核对区仅保留历史转录，不作为准确原文使用。
> 仅核对本目录原PNG；ET60157/ET6801手册、驱动、BootROM不用于补字。红色修改结合本原文明确ET6601段落判断；目录蓝色超链接和历史图配色不直接判为6601修改。
> 最新逐图台账：../../../reviews/XBAR_IMAGE_LEDGER_20261006.json；正式保存与回读见XBAR_ROUND2_REMOTE_SAVE_20261006.json。

## 第一部分：原始文档逐图还原

## 原图：`GameViewer_yUpAyoEWMN.png`

[查看原始PNG](../images/GameViewer_yUpAyoEWMN.png)

> 来源顺序1；已首轮核对。

<!-- xbar-block:start yUpAyoEWMN -->
### 【左页】

# ET6601 XBAR模块
# 需求规格与设计方案

> 转录注：封面公司标识保留在原PNG；账号水印、窗口和播放器文字不属于正文。

### 【右页】

设计：牛婷婷  
评审：  
批准：

> 转录注：评审、批准栏原文空白。
<!-- xbar-block:end yUpAyoEWMN -->

---

## 原图：`GameViewer_DjSL3rXWx4.png`

[查看原始PNG](../images/GameViewer_DjSL3rXWx4.png)

> 来源顺序2；已首轮核对。

<!-- xbar-block:start DjSL3rXWx4 -->
### 【左页】

> 转录注：本页没有可见正文；水印不转录。

### 【右页】

## 修订记录

| 版本号 | 修订内容 | 修订日期 | 修订人员 |
|---|---|---|---|
| V1.0 | 首次修订 | 2023.10.28 | 肖均 |
| V1.1 | OUTPUT XBAR输出位宽由8bit修改为14bit | 2023.11.7 | 肖均 |
| V1.2 | OUTPUT XBAR交换ERRORSTS和EXTSYNCOUT位置，与其他表格保持一致 | 2023.11.17 | 肖均 |
| V1.3 | 刷新支持锁定寄存器内容<br>增加INPUTXBAR滤波窗口配置分组描述<br>增加OUTPUTXBAR输出模式选择描述 | 2023.11.29 | 肖均 |
| V1.4 | 刷新接口信号列表<br>刷新接口信号特征表 | 2023.12.14 | 肖均 |
| V1.5 | 增加4.3节信号对应关系 | 2023.12.26 | 肖均 |
| V1.5 | 修改XBAR.SPEC<04>表格部分信号名后缀 | 2023.12.27 | 肖均 |
| V2.0 | 在6002的基础上修改3101和6003的xbar | 2024.08.20 | 袁云龙 |
| V2.1 | OPXB和COXB新增异步处理 | 2024.10.21 | 袁云龙 |
| V2.2 | 对inputxbar/pfxb/cbxb/cixb新增展宽处理以适应srpwm100M场景 | 2024.12 | 袁云龙 |
| V3.0 | ET6801 xbar: 信号源变化，对标p65x | 2025.11 | 袁云龙 |
| V3.1 | 修改DMA触发源描述 | 2025.11 | 袁云龙 |
| V4.0 | 更新ET6601 XBAR修改点 | 2026.09.23 | 牛婷婷 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

> 转录注：两个V1.5、日期格式及末6个空白行按原图保留；历史14bit说明不与后文6601的12→14bit统一。
<!-- xbar-block:end DjSL3rXWx4 -->

---

## 原图：`GameViewer_K9wJHSnqdx.png`

[查看原始PNG](../images/GameViewer_K9wJHSnqdx.png)

> 来源顺序3；已首轮核对。

<!-- xbar-block:start K9wJHSnqdx -->
### 【左页】

> 转录注：本页没有可见正文。

### 【右页】

## 目录

1. 概述  
2. 功能描述  
3. 需求规格  
3.1 整体  
3.2 INPUT XBAR  
3.3 PWM XBAR  
3.4 ETIM XBAR  
3.5 OUTPUT XBAR  
3.6 CLU  
3.7 XBAR约束  
4. 接口说明  
4.1 接口列表  
4.2 接口信号特征  
4.3 信号对应关系

> 转录注：目录蓝色下划线为超链接，不作为6601修改标记。
<!-- xbar-block:end K9wJHSnqdx -->

---

## 原图：`GameViewer_FilEyIUnoO.png`

[查看原始PNG](../images/GameViewer_FilEyIUnoO.png)

> 来源顺序4；已首轮核对。

<!-- xbar-block:start FilEyIUnoO -->
### 【左页】

5. 方案设计  
5.1 INPUT XBAR模块  
5.2 PWM XBAR模块  
5.3 ETIM XBAR模块  
5.4 OUTPUT XBAR模块  
5.5 XCSA/XCET/XCOX模块  
5.6 CLU逻辑处理模块  
5.7 CLU中断事件触发  
6. 寄存器设计  
7. 中断说明  
8. 遗留问题  
9. 参考文献

### 【右页】

## 1. 概述

XBAR（crossbar）模块主要功能，是为芯片的输入管脚、输出管脚和内部模块之间提供灵活的连接关系，这些连接关系可通过配置进行选择，同时可通过内部集成的CLU（configurable logic unit）对部分连接关系进行逻辑运算，以提供更大的灵活性和可能性。

ET3101:本文档为在6002xbar文档的基础上进行修改，主要修改包括

1. 修改input-xbar，去除前处理模块（该部分被放在IOMUX处理）；
2. 对所有xbar加入了异步路径；
3. 加入了clb_inputxbar/clb_xbar/clb_output_xbar
4. 修改了opxb和coxb的结构，对上报和同步加入了异步处理jiraET3101-77；
5. GPIO的数量由84个变为80个。

ET6801修改点：

> 转录注：此标题的三项正文续至下一张左页；这里是历史ET3101/ET6801说明，不冒充ET6601新增。
<!-- xbar-block:end FilEyIUnoO -->

---

## 原图：`GameViewer_SMcbqY9aCU.png`

[查看原始PNG](../images/GameViewer_SMcbqY9aCU.png)

> 来源顺序5；已首轮核对。

<!-- xbar-block:start SMcbqY9aCU -->
### 【左页】

1. 信号列表变动；其中pfxb和opxb信号选择mux 32 >64；
2. 去除之前由于CLB工作在100M增加的展宽电路；
3. inputxbar中断数量4 > 5。

**ET6601修改点：**

1. 去除CLB INPUT_XBAR、CLB OUTPUT_XBAR和CLB_XBAR；
2. OUTPUT_XBAR输出从12位修改为14位；（up to final IOlist）
3. 寄存器配置接口从AMBA3 AHB Lite改为AMBA3 AHB，nManager改为APB接口生成ids文件。（xbar_cfg写pclk脉冲用hclk取沿，xbar_cfg读hclk脉冲需要展宽，有哪些信号？）
4. 复位可配置不受WDG和系统软复位影响。

> 转录注：以上标题及四项主体为红字；第2项括号和第3项问句为黑字原批注，不删掉问句、不推导信号列表。

### 【右页】

## 2. 功能描述

**图1 XBAR模块结构框图**

图中文字转录（连接和标记范围仍参看原图）：

| 区域 | 可辨原标签 |
|---|---|
| 外框 | SOURCE、XBAR、6601、DESTINATION |
| 输入源 | GPIO、SRPWM、ACMP、SARC、ETIM、Errorsts；红色删除的SDFM、CLB |
| 路由／逻辑 | INXB（INPUT XBAR）、XCSA（XCLU2SARC）、XCET（XCLU2ETIM）、XCOX（XCLU2OUT）；PFXB（SRPWM XBAR）、EFXB（ETIMER XBAR）、STIM TRIG SEL、OPXB（OUTPUT XBAR） |
| 被删模块 | CIXB（CLB INPUT XBAR）、CBXB（CLB XBAR）、COXB（CLB OUT XBAR），红色删除标记 |
| 事件及目标 | 两个cbb int gen块；SRPWM、SARC、ETIMER、STIMER、IOMUX；红色删除的CLB目标 |

> ⚠️ 原图待复核：XBAR-U01。图1中的各源和目标框底部数量／位宽细字、GPIO完整编号、两条中断输出完整标识及局部红线范围未逐字符确定。上表仅记可辨标签，不用后文数值反填图字。原图：GameViewer_SMcbqY9aCU.png右页上部。

XBAR支持对GPIO输入信号和来自内部模块的信号进行选择、逻辑计算等处理，处理后的信号可送往SRPWM、ADC、ETIMER、STIMER、~~CLB~~和IO，作为后级模块的信号输入、触发事件或故障处理信号。

XBAR主要由以下几个模块组成：

■INXB(INPUT XBAR)，输出送往各内部模块；  
■PFXB(PWM XBAR)，输出送往SRPWM；

> 转录注：模块列表续下一张左页；正文CLB为红色删除线。
<!-- xbar-block:end SMcbqY9aCU -->

---

## 原图：`GameViewer_Gg0PKIieqf.png`

[查看原始PNG](../images/GameViewer_Gg0PKIieqf.png)

> 来源顺序6；已首轮核对。

<!-- xbar-block:start Gg0PKIieqf -->
### 【左页】

■STIM_TRSEL(STIMER Triger Selection)，输出送往STIMER(6*32bit stimer)；  
■SAXB(ADC XBAR)，输出送往ADC；  
■EFXB(ETIMER Fault_in XBAR)，输出送往ETIMER；  
■OPXB(Output XBAR)，输出送往IOMUX；  
■CLU模块，输入信号来源为INPUT XBAR，输出到SARC、ETIM和Output XBAR。  
~~■CIXB(CLB INPUTXBAR)，输出送往CLB；~~  
~~■CBXB(CLB XBAR)，输出送往CLB~~  
~~■COXB(CLB OUTPUTXBAR)，输出送往IOMUX~~  
■cbb_int_gen中断处理模块

## 3. 需求规格

### 3.1 整体

**XBAR.SPEC【01】**　XBAR模块支持AMBA3 APB总线接口协议

> 转录注：APB为红色修改文字，左侧有修订竖线。与概述中的AHB/nManager两层表述分别照录，不擅自统一。

### 【右页】

**XBAR.SPEC【02】**　支持INPUT XBAR、PWM XBAR、ETIMER XBAR和OUTPUT XBAR~~，支持CLB INPUT XBAR、CLB_XBAR、CLB_OUTPUT XBAR~~

**XBAR.SPEC【03】**　支持STIMER紧急故障触发源输出

**XBAR.SPEC【04】**　XBAR支持输入故障使能和合并，通过配置Fault对应bit使能实现；支持将errorsts（flash|syserr|PT_err）发送到IO

| signal name of input | bit width | bit order |  |
|---|---|---|---|
| pflash_ecc_err | 1 | 22 | 合并为FLASH_ERR |
| pflash_bus_err | 1 | 21 |  |
| dflash_ecc_err | 1 | 20 |  |
| dflash_bus_err | 1 | 19 |  |
| wdt0_req_rec | 1 | 18 | 合并为SYS_ERR |
| wdt1_req_rec | 1 | 17 |  |
| cpu0_rst_rec | 1 | 16 |  |
| cpu0_lockup | 1 | 15 |  |
| cpu0_ecc_err | 1 | 14 |  |
| cpu1_rst_rec | 1 | 13 |  |
| cpu1_lockup | 1 | 12 |  |
| cpu1_ecc_err | 1 | 11 |  |
| sram_ecc_err | 1 | 10 |  |
| can_ecc_err | 1 | 9 |  |
| bus_timeout | 1 | 8 |  |
| cpu0_bus_err | 1 | 7 |  |
| cpu1_bus_err | 1 | 6 |  |
| clock_fault | 1 | 5 |  |
| por_uv_warn | 1 | 4 | 合并为PT_ERR |
| por_ov_warn | 1 | 3 |  |
| pwr_ocp_warn | 1 | 2 |  |
| power_err | 1 | 1 |  |

> 转录注：最后一列表头原为空白；FLASH_ERR跨22～19、SYS_ERR跨18～5、PT_ERR跨4～1，在本张为纵向合并单元格。末行后续表见下一原图，不把本张底部当表格结束。绿色表头本身不判为6601新增。
<!-- xbar-block:end Gg0PKIieqf -->

---

## 原图：`GameViewer_m38yfM9SyS.png`

[查看原始PNG](../images/GameViewer_m38yfM9SyS.png)

> 来源顺序7；已首轮核对。

<!-- xbar-block:start m38yfM9SyS -->
### 【左页】

XBAR.SPEC【04】表尾续行：

| signal name of input | bit width | bit order |  |
|---|---|---|---|
| temp_warn | 1 | 0 |  |

> 转录注：列名沿用上一张表头以标明续表；末列接上一页PT_ERR合并区，本页没有重复文字。

**XBAR.SPEC【05】**　支持XCSA、XCET和XCOX三个CLU可配置逻辑组合功能

**XBAR.SPEC【06】**　支持XBAR中断上报。INPUTXBAR支持5个中断独立输出，CLU模块支持中断合并输出，对每个中断源，可配置中断使能、中断屏蔽、中断清除、强制中断．可查询原始中断和中断状态

**XBAR.SPEC【07】**　支持XBAR配置锁定，通过配置一个16bit KEY实现寄存器写保护，支持写保护的寄存器包括：Fault使能配置、Stimer紧急触发源配置、CLU相关配置、滤波窗口、滤波使能配置、输入输出极性配置、MUX-OR配置、输入输出使能配置、输出选择配置、软件信号源配置、输出脉宽扩展配置、输出模式选择

~~XBAR.SPEC【08】　支持触发源状态上报（待定？——暂不实现）~~

> 转录注：08整条带删除线，内容为绿色，编号黑色；没有明确归属6601的文字，保留为原文被删事项而非确定新增。

### 【右页】

### 3.2 INPUT XBAR

**XBAR.SPEC【09】**　INPUT XBAR支持输入信号源来自芯片IO cell C端经过处理后的信号(bypass/sync/3sample/6sample)，覆盖80个GPIO输入

> 转录注：80为红字；概述历史ET3101也写84→80，本处没有独立版本说明，不另推断一次6601数量变更。

图中文字转录（原图没有图号/图名）：`gpio_xbar_*`（红字）、`gpio_in_mod0`、`gpio_in_mod1`、省略点、`gpio_in_modN`；`gpio_out_mod0`、`gpio_out_mod1`、省略点、`gpio_out_modN`；`IOMUX & IOCTRL`；选择支路`同步`、`3 sample`、`6 sample`及直通支路；`IE`、`ST`、`C`、`I`、`OEN`、`DS0`、`DS1`、`PU`、`PD`；`CMOS`、`PAD`。C端接选择输入，gpio_xbar_*支路由该输入节点引出；下方PU/PD支路及反相点保持原图。

**XBAR.SPEC【10】**　INPUT XBAR支持对信号进行4bit分组并进行mux-or选通

**XBAR.SPEC【11】**　INPUT XBAR支持对选通信号进行高电平锁存操作，或上下沿检测操作，锁存信号可配置清零

**XBAR.SPEC【12】**　INPUT XBAR支持输出使能和输出极性配置
<!-- xbar-block:end m38yfM9SyS -->

---

## 原图：`GameViewer_CpOsnywQhu.png`

[查看原始PNG](../images/GameViewer_CpOsnywQhu.png)

> 来源顺序8；已首轮核对。

<!-- xbar-block:start CpOsnywQhu -->
### 【左页】

**XBAR.SPEC【13】**　INPUT XBAR支持送出5个中断源

**XBAR.SPEC【14】**　INPUT XBAR支持异步路径，以减小封波延迟及其它用应用场景，输出端通过WARP_MUX2配置选择；

**XBAR.SPEC【15】**　INPUT XBAR输出连接到中断模块、SRPWM、ETIMER、SARC、PWM XBAR、ETIM XBAR、OUTPUT XBAR，及ETIM & SARC & OUTPUT CLU

> 转录注：“其它用应用场景”及WARP_MUX2按原文，不改成推测的术语。

### 【右页】

图中文字及连接索引（原图无图号/图名）：

| 起点 | 中间模块 | 目标 | 原图可辨标记 |
|---|---|---|---|
| GPIO0 … GPION | INPUT XBAR | 公共输出干线 |  |
| 公共干线 |  | INT | 细字待复核 |
| 公共干线 |  | SRPWM | 6 |
| 公共干线 | PWM XBAR | SRPWM | 16；12 |
| 公共干线 | ETIM XBAR | ETIMER | 16；14 |
| 公共干线 |  | ETIMER | 16 capture |
| 公共干线 | ETIM CLU | ETIMER | 16；4 capture |
| 公共干线 | SARCCLU | SARC | 16；4 |
| 公共干线 |  | SARC | 细字待复核 |
| 公共干线 | OUTPUT CLU | OUTPUT XBAR | 16；4 |
| 公共干线 |  | OUTPUT XBAR | 16 |

> ⚠️ 原图待复核：XBAR-U02。INT支路文字及直接到SARC支路标记未能逐字符确认；SARC支路可辨似有“1(16)”，仅为候选。原图：GameViewer_CpOsnywQhu.png右页。不能将正文5个中断源反填为图内标记。

### 3.3 PWM XBAR

ET6801修改点：

> 转录注：下面15项历史说明在下一张左页。
<!-- xbar-block:end CpOsnywQhu -->

---

## 原图：`GameViewer_Z7r3yKz86a.png`

[查看原始PNG](../images/GameViewer_Z7r3yKz86a.png)

> 来源顺序9；已首轮核对。

<!-- xbar-block:start Z7r3yKz86a -->
### 【左页】

1）新增CMPC通道CMP_EVT7 >21；去除CMP_EVT*_OR_EVT*（TI无）

2）新增SDFM通道SD2/3FLT*_EVT*；去除SD*FLT*_EVT0_OR_EVT1（TI无）

3）新增CLB4/5_OUT*

4）新增EPWM_TRIPOUT/~~DE_TRIP/DE_ACTIVE~~

~~5）新增CPU*_ADCCHECK_EVT~~

6）新增ETIM_TRIPOUT

7）对比TI，无MACN_FEVT

8）对比TI，无FSI

9）对比TI，无ECAT_SYNC

10）ECAP 1-7(TI) > ETIM0-11

11）INPUTXBAR1-14(TI) > INXB0-15

12）CLB_INPUTXBAR7-14 > CBXB0-15

13）新增CPU1_HALT

14）TI无SYS_ERR/PT_ERR/FLASH_ERR

15）PIEVECTERR（中断扩展模块错误）/UNCERR(内存访问错误)

> 转录注：本页接ET6801标题，非6601新增清单；删除线分别保留。

### 【右页】

**ET6601修改点：**

1）去除SDFM通道SD*FLT*_EVT*

2）去除CLB*_OUT*和CLB_INPUTXBAR*

3）去除ADCC_EVT*

4）去除EPWM12~17_FAULTREAL

5）

> 原屏局部另显示：`Delete / 6 (0#~5#)`，其中Delete为红色。XBAR-U03：此处未出现可确定的第5项功能语句，尚不能确定显示文字与原文修订浮层的边界；不猜补第5项、不将Delete解释成某个功能删除。

6）新增ETIMOUT12/13和ETIM12/13_FAULTREAL

> 转录注：标题及1～4、6项为红字；编号5的特殊显示按上注保留。

**XBAR.SPEC【16】**　PWM XBAR支持对输入信号源进行4bit分组并进行mux-or选通，信号源选择如下表所示：

> 表内**加粗**表示原图红字，仅为转录颜色标记；空格是真实空白，不补Reserved。绿色表头不计修改。

| MUX | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | CMP_EVT0 | **Reserved** | ADCA_EVT0 | ETIMOUT0 |
| 1 | CMP_EVT1 | INPUTXBAR0 | **Reserved** |  |
| 2 | CMP_EVT2 | **Reserved** | ADCA_EVT1 | ETIMOUT1 |
| 3 | CMP_EVT3 | INPUTXBAR1 | **Reserved** |  |
| 4 | CMP_EVT4 | **Reserved** | ADCA_EVT2 | ETIMOUT2 |
| 5 | CMP_EVT5 | INPUTXBAR2 | **Reserved** |  |
| 6 | CMP_EVT6 | **Reserved** | ADCA_EVT3 | ETIMOUT3 |
| 7 | CMP_EVT7 | INPUTXBAR3 | **Reserved** |  |
| 8 | CMP_EVT8 | **Reserved** | ADCB_EVT0 | ETIMOUT4 |
| 9 | CMP_EVT9 | INPUTXBAR4 | **Reserved** | Reserved |
| 10 | CMP_EVT10 | **Reserved** | ADCB_EVT1 | ETIMOUT5 |
| 11 | CMP_EVT11 | INPUTXBAR5 | **Reserved** | Reserved |
| 12 | CMP_EVT12 | **Reserved** | ADCB_EVT2 | ETIMOUT6 |
| 13 | CMP_EVT13 | ADCSOCA0 | **Reserved** | SYS_ERR |
| 14 | CMP_EVT14 | **Reserved** | ADCB_EVT3 | EXTSYNCOUT |
| 15 | CMP_EVT15 | ADCSOCB0 | **Reserved** | PT_ERR |
| 16 | **Reserved** | **Reserved** | **Reserved** | ERRORSTS |

> 转录注：表跨下一张左右页继续，本处仅0～16。
<!-- xbar-block:end Z7r3yKz86a -->

---

## 原图：`GameViewer_CqeT5pUL1x.png`

[查看原始PNG](../images/GameViewer_CqeT5pUL1x.png)

> 来源顺序10；已首轮核对。

<!-- xbar-block:start CqeT5pUL1x -->
### 【左页】

XBAR.SPEC【16】PWM XBAR信号源选择续表，原图本页17～57；为方便衔接沿用上一张表头。表内**加粗**表示红字。

| MUX | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 17 | **Reserved** | INPUTXBAR6 | **Reserved** | CPU0_HALT |
| 18 | **Reserved** | **Reserved** | **Reserved** | FLASH_ERR |
| 19 | **Reserved** | INPUTXBAR7 | **Reserved** | ETIMOUT7 |
| 20 | **Reserved** | **Reserved** | **Reserved** | CPU1_HALT |
| 21 | **Reserved** | INPUTXBAR8 | **Reserved** | ETIMOUT8 |
| 22 | **Reserved** | **Reserved** | **Reserved** | Reserved |
| 23 | **Reserved** | INPUTXBAR9 | **Reserved** | ETIMOUT9 |
| 24 | **Reserved** | **Reserved** | **Reserved** | **ETIMOUT10** |
| 25 | **Reserved** | INPUTXBAR10 | Reserved | **ETIMOUT11** |
| 26 | **Reserved** | **Reserved** | **Reserved** | **ETIMOUT12** |
| 27 | **Reserved** | INPUTXBAR11 | Reserved | **ETIMOUT13** |
| 28 | **Reserved** | **Reserved** | **Reserved** | SRPWM_XBAR_SYNC0 |
| 29 | **Reserved** | INPUTXBAR12 | Reserved | SRPWM_XBAR_SYNC1 |
| 30 | **Reserved** | **Reserved** | **Reserved** | SRPWM_XBAR_SYNC2 |
| 31 | **Reserved** | INPUTXBAR13 | ERRORSTS | SRPWM_XBAR_SYNC3 |
| 32 | EPWM0_FAULTREAL | Reserved | **Reserved** | ETIM0_FAULTREAL |
| 33 | EPWM1_FAULTREAL | INPUTXBAR14 | Reserved | ETIM1_FAULTREAL |
| 34 | EPWM2_FAULTREAL | Reserved | **Reserved** | ETIM2_FAULTREAL |
| 35 | EPWM3_FAULTREAL | INPUTXBAR15 | Reserved | ETIM3_FAULTREAL |
| 36 | EPWM4_FAULTREAL | Reserved | **Reserved** | ETIM4_FAULTREAL |
| 37 | EPWM5_FAULTREAL | Reserved | Reserved | ETIM5_FAULTREAL |
| 38 | EPWM6_FAULTREAL | Reserved | **Reserved** | ETIM6_FAULTREAL |
| 39 | EPWM7_FAULTREAL | Reserved | Reserved | ETIM7_FAULTREAL |
| 40 | EPWM8_FAULTREAL | Reserved | **Reserved** | ETIM8_FAULTREAL |
| 41 | EPWM9_FAULTREAL | Reserved | Reserved | ETIM9_FAULTREAL |
| 42 | EPWM10_FAULTREAL | Reserved | **Reserved** | ETIM10_FAULTREAL |
| 43 | EPWM11_FAULTREAL | Reserved | Reserved | ETIM11_FAULTREAL |
| 44 | **Reserved** | Reserved | **Reserved** | **ETIM12_FAULTREAL** |
| 45 | **Reserved** | Reserved | Reserved | **ETIM13_FAULTREAL** |
| 46 | **Reserved** | Reserved | **Reserved** | Reserved |
| 47 | **Reserved** | Reserved | Reserved | Reserved |
| 48 | **Reserved** | Reserved | **Reserved** | Reserved |
| 49 | **Reserved** | Reserved | Reserved | Reserved |
| 50 | Reserved | Reserved | Reserved | Reserved |
| 51 | Reserved | Reserved | Reserved | Reserved |
| 52 | Reserved | Reserved | Reserved | Reserved |
| 53 | Reserved | Reserved | Reserved | Reserved |
| 54 | Reserved | Reserved | Reserved | Reserved |
| 55 | Reserved | Reserved | Reserved | Reserved |
| 56 | Reserved | Reserved | Reserved | Reserved |
| 57 | Reserved | Reserved | Reserved | Reserved |

### 【右页】

同一表58～63：

| MUX | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 58 | CMP_EVT16 | Reserved | Reserved | Reserved |
| 59 | CMP_EVT17 | Reserved | Reserved | Reserved |
| 60 | CMP_EVT18 | Reserved | Reserved | Reserved |
| 61 | CMP_EVT19 | Reserved | Reserved | Reserved |
| 62 | CMP_EVT20 | Reserved | Reserved | Reserved |
| 63 | CMP_EVT21 | Reserved | Reserved | Reserved |

**XBAR.SPEC【17】**　PWM XBAR支持对选通信号进行高电平锁存操作，锁存信号可配置清零

**XBAR.SPEC【18】**　PWM XBAR支持输出使能和输出极性配置

**XBAR.SPEC【19】**　PWM XBAR支持异步路径，以减小封波延迟，输出端通过WARP_MUX2配置选择

**XBAR.SPEC【20】**　支持PWM XBAR输出16bit，顶层选择后分别连接到12个PWM通道

> 转录注：12为红字；原文16bit输出不改成12bit。

### 3.4 ETIM XBAR

ET6801修改点：

16）新增CMPC通道CMP_EVT7 >21；新增CMP_EVT*_OR_EVT*

17）新增SDFM通道SD2/3FLT*_EVT*；新增SD*FLT*_EVT0_OR_EVT1

18）新增CPU1_HALT

> 转录注：16～18为原编号，且这里写“新增”合并事件；不据PWM历史列表的“去除”改写。
<!-- xbar-block:end CqeT5pUL1x -->

---

## 原图：`GameViewer_x1UNjKA5fU.png`

[查看原始PNG](../images/GameViewer_x1UNjKA5fU.png)

> 来源顺序11；已首轮核对。

<!-- xbar-block:start x1UNjKA5fU -->
### 【左页】

**ET6601修改点：**

1）去除SDFM通道SD*FLT*_EVT*和SD*FLT*_EVT0_OR_EVT1

2）去除EPWM12~17_FAULTREAL

**XBAR.SPEC【21】**　ETIM XBAR支持对输入信号源进行4bit分组并进行mux-or选通，信号源选择如下表所示：

> 表内**加粗**表示原图红字；左页0～20，右页21～31，同一张截图的同一张表先左后右。

| MUX | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | CMP_EVT0 | **Reserved** | ADCA_EVT0 | **Reserved** |
| 1 | CMP_EVT1 | INPUTXBAR0 | ADCA_EVT1 | **Reserved** |
| 2 | CMP_EVT2 | **Reserved** | ADCA_EVT2 | **Reserved** |
| 3 | CMP_EVT3 | INPUTXBAR1 | ADCA_EVT3 | **Reserved** |
| 4 | CMP_EVT4 | **Reserved** | ADCB_EVT0 | **Reserved** |
| 5 | CMP_EVT5 | INPUTXBAR2 | ADCB_EVT1 | **Reserved** |
| 6 | CMP_EVT6 | **Reserved** | ADCB_EVT2 | **Reserved** |
| 7 | CMP_EVT7 | INPUTXBAR3 | ADCB_EVT3 | **Reserved** |
| 8 | CMP_EVT8 | ERRORSTS | ADCC_EVT0 | **Reserved** |
| 9 | CMP_EVT9 | INPUTXBAR4 | ADCC_EVT1 | **Reserved** |
| 10 | CMP_EVT10 | EXTSYNCOUT | ADCC_EVT2 | **Reserved** |
| 11 | CMP_EVT11 | INPUTXBAR5 | ADCC_EVT3 | **Reserved** |
| 12 | CMP_EVT12 | CMP_EVT0_OR_EVT1 | EPWM0_FAULTREAL | **Reserved** |
| 13 | CMP_EVT13 | INPUTXBAR6 | EPWM1_FAULTREAL | **Reserved** |
| 14 | CMP_EVT14 | CFG_ETXB_SWx | EPWM2_FAULTREAL | **Reserved** |
| 15 | CMP_EVT15 | INPUTXBAR7 | EPWM3_FAULTREAL | **Reserved** |
| 16 | CMP_EVT16 | **Reserved** | EPWM4_FAULTREAL | **Reserved** |
| 17 | CMP_EVT17 | INPUTXBAR8 | EPWM5_FAULTREAL | **Reserved** |
| 18 | CMP_EVT18 | **Reserved** | EPWM6_FAULTREAL | **Reserved** |
| 19 | CMP_EVT19 | INPUTXBAR9 | EPWM7_FAULTREAL | **Reserved** |
| 20 | CMP_EVT20 | **Reserved** | EPWM8_FAULTREAL | **Reserved** |

### 【右页】

XBAR.SPEC【21】续表：

| MUX | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 21 | CMP_EVT21 | INPUTXBAR10 | EPWM9_FAULTREAL | **Reserved** |
| 22 | CMP_EVT2_OR_EVT3 | **Reserved** | EPWM10_FAULTREAL | **Reserved** |
| 23 | CMP_EVT4_OR_EVT5 | INPUTXBAR11 | EPWM11_FAULTREAL | **Reserved** |
| 24 | CMP_EVT6_OR_EVT7 | **Reserved** | **Reserved** | **Reserved** |
| 25 | CMP_EVT8_OR_EVT9 | INPUTXBAR12 | **Reserved** | **Reserved** |
| 26 | CMP_EVT10_OR_EVT11 | **Reserved** | **Reserved** | **Reserved** |
| 27 | CMP_EVT12_OR_EVT13 | INPUTXBAR13 | **Reserved** | **Reserved** |
| 28 | CMP_EVT14_OR_EVT15 | **Reserved** | **Reserved** | **Reserved** |
| 29 | CMP_EVT16_OR_EVT17 | INPUTXBAR14 | **Reserved** | **Reserved** |
| 30 | CMP_EVT18_OR_EVT19 | **Reserved** | CFG_ETXB_SWx | **Reserved** |
| 31 | CMP_EVT20_OR_EVT21 | INPUTXBAR15 | ERRORSTS | **Reserved** |

**XBAR.SPEC【22】**　ETIM XBAR支持对选通信号进行高电平锁存操作，锁存信号可配置清零

**XBAR.SPEC【23】**　ETIM XBAR支持输出使能和输出极性配置

**XBAR.SPEC【24】**　ETIM XBAR支持异步路径，输出端通过WARP_MUX2配置选择

**XBAR.SPEC【25】**　支持ETIM XBAR输出14bit，分别连接到14个ETIMER通道

**XBAR.SPEC【26】**　支持软件可配置14bit CFG_ETXB_SWx寄存器，分别对应14个ETIMER通道XBAR选择

> 转录注：25的14bit及14、26的14及14为红字；其他值仍照原文。

<!-- xbar-block:end x1UNjKA5fU -->

---

## 原图：`GameViewer_qZ6VVLkkSM.png`

[查看原始PNG](../images/GameViewer_qZ6VVLkkSM.png)

> 来源顺序12；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start qZ6VVLkkSM -->

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

<!-- xbar-block:end qZ6VVLkkSM -->

---

## 原图：`GameViewer_064VlD8fJy.png`

[查看原始PNG](../images/GameViewer_064VlD8fJy.png)

> 来源顺序13；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start 064VlD8fJy -->

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

<!-- xbar-block:end 064VlD8fJy -->

---

## 原图：`GameViewer_yl5bEptpgs.png`

[查看原始PNG](../images/GameViewer_yl5bEptpgs.png)

> 来源顺序14；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start yl5bEptpgs -->

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

<!-- xbar-block:end yl5bEptpgs -->

---

## 原图：`GameViewer_7vrsONkjgD.png`

[查看原始PNG](../images/GameViewer_7vrsONkjgD.png)

> 来源顺序15；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start 7vrsONkjgD -->

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

<!-- xbar-block:end 7vrsONkjgD -->

---

## 原图：`GameViewer_BJDG1Zjxti.png`

[查看原始PNG](../images/GameViewer_BJDG1Zjxti.png)

> 来源顺序16；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start BJDG1Zjxti -->

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

<!-- xbar-block:end BJDG1Zjxti -->

---

## 原图：`GameViewer_NY8OuaK0XB.png`

[查看原始PNG](../images/GameViewer_NY8OuaK0XB.png)

> 来源顺序17；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start NY8OuaK0XB -->

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

<!-- xbar-block:end NY8OuaK0XB -->

---

## 原图：`GameViewer_XqmNqCU6Lw.png`

[查看原始PNG](../images/GameViewer_XqmNqCU6Lw.png)

> 来源顺序18；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start XqmNqCU6Lw -->

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

<!-- xbar-block:end XqmNqCU6Lw -->

---

## 原图：`GameViewer_LS0PAMbqAJ.png`

[查看原始PNG](../images/GameViewer_LS0PAMbqAJ.png)

> 来源顺序19；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start LS0PAMbqAJ -->

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

<!-- xbar-block:end LS0PAMbqAJ -->

---

## 原图：`GameViewer_nneQMiNCGh.png`

[查看原始PNG](../images/GameViewer_nneQMiNCGh.png)

> 来源顺序20；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start nneQMiNCGh -->

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

<!-- xbar-block:end nneQMiNCGh -->

---

## 原图：`GameViewer_b4H5jcq6ED.png`

[查看原始PNG](../images/GameViewer_b4H5jcq6ED.png)

> 来源顺序21；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start b4H5jcq6ED -->

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

<!-- xbar-block:end b4H5jcq6ED -->

---

## 原图：`GameViewer_V3t3Z6WQYi.png`

[查看原始PNG](../images/GameViewer_V3t3Z6WQYi.png)

> 来源顺序22；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start V3t3Z6WQYi -->

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

<!-- xbar-block:end V3t3Z6WQYi -->

---

## 原图：`GameViewer_qPba5rmgGl.png`

[查看原始PNG](../images/GameViewer_qPba5rmgGl.png)

> 来源顺序23；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start qPba5rmgGl -->

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

<!-- xbar-block:end qPba5rmgGl -->

---

## 原图：`GameViewer_nYxX2xZgHL.png`

[查看原始PNG](../images/GameViewer_nYxX2xZgHL.png)

> 来源顺序24；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start nYxX2xZgHL -->

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

<!-- xbar-block:end nYxX2xZgHL -->

---

## 原图：`GameViewer_7jsvVSVHdw.png`

[查看原始PNG](../images/GameViewer_7jsvVSVHdw.png)

> 来源顺序25；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start 7jsvVSVHdw -->

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

<!-- xbar-block:end 7jsvVSVHdw -->

---

## 原图：`GameViewer_tikzmykACG.png`

[查看原始PNG](../images/GameViewer_tikzmykACG.png)

> 来源顺序26；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start tikzmykACG -->

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

<!-- xbar-block:end tikzmykACG -->

---

## 原图：`GameViewer_3njiF8SofL.png`

[查看原始PNG](../images/GameViewer_3njiF8SofL.png)

> 来源顺序27；候选顺序，以下为历史转录，尚未首轮原图核对。

<!-- xbar-block:start 3njiF8SofL -->

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

<!-- xbar-block:end 3njiF8SofL -->

---

## 第二部分：截图明确标出的ET6601修改位置

| 编号 | 原文章节 | 原文／可辨标记 | 原图 | 性质与边界 |
|---|---|---|---|---|
| XBAR-C01 | 修订记录V4.0 | 更新ET6601 XBAR修改点；2026.09.23；牛婷婷 | [GameViewer_DjSL3rXWx4.png](../images/GameViewer_DjSL3rXWx4.png) | 明确ET6601版本记录；非独立功能项 |
| XBAR-C02 | 1.概述／ET6601修改点1 | 去除CLB INPUT_XBAR、CLB OUTPUT_XBAR和CLB_XBAR； | [GameViewer_SMcbqY9aCU.png](../images/GameViewer_SMcbqY9aCU.png) | 红字明确删除 |
| XBAR-C03 | 1.概述／ET6601修改点2 | OUTPUT_XBAR输出从12位修改为14位；（up to final IOlist） | [GameViewer_SMcbqY9aCU.png](../images/GameViewer_SMcbqY9aCU.png) | 红字修改；黑色原批注保留 |
| XBAR-C04 | 1.概述／ET6601修改点3 | 寄存器配置接口从AMBA3 AHB Lite改为AMBA3 AHB，nManager改为APB接口生成ids文件。（xbar_cfg写pclk脉冲用hclk取沿，xbar_cfg读hclk脉冲需要展宽，有哪些信号？） | [GameViewer_SMcbqY9aCU.png](../images/GameViewer_SMcbqY9aCU.png) | 红字接口修改；黑字原问题未擅自回答 |
| XBAR-C05 | 1.概述／ET6601修改点4 | 复位可配置不受WDG和系统软复位影响。 | [GameViewer_SMcbqY9aCU.png](../images/GameViewer_SMcbqY9aCU.png) | 红字明确修改 |
| XBAR-C06 | 2.功能描述／图1 | SDFM、CLB输入；CIXB/CBXB/COXB及CLB目标的红色删除标记 | [GameViewer_SMcbqY9aCU.png](../images/GameViewer_SMcbqY9aCU.png) | 图内删除位置；精细标线和部分小字挂XBAR-U01 |
| XBAR-C07 | 2.功能描述／正文 | 送往SRPWM、ADC、ETIMER、STIMER、~~CLB~~和IO | [GameViewer_SMcbqY9aCU.png](../images/GameViewer_SMcbqY9aCU.png) | CLB红色删除线 |
| XBAR-C08 | 2.功能描述／模块列表 | ~~CIXB(CLB INPUTXBAR)，输出送往CLB；~~ | [GameViewer_Gg0PKIieqf.png](../images/GameViewer_Gg0PKIieqf.png) | 红色删除线 |
| XBAR-C09 | 2.功能描述／模块列表 | ~~CBXB(CLB XBAR)，输出送往CLB~~ | [GameViewer_Gg0PKIieqf.png](../images/GameViewer_Gg0PKIieqf.png) | 红色删除线 |
| XBAR-C10 | 2.功能描述／模块列表 | ~~COXB(CLB OUTPUTXBAR)，输出送往IOMUX~~ | [GameViewer_Gg0PKIieqf.png](../images/GameViewer_Gg0PKIieqf.png) | 红色删除线 |
| XBAR-C11 | 3.1／XBAR.SPEC【01】 | XBAR模块支持AMBA3 APB总线接口协议 | [GameViewer_Gg0PKIieqf.png](../images/GameViewer_Gg0PKIieqf.png) | APB红字及修订线；不统一概述两层接口表述 |
| XBAR-C12 | 3.1／XBAR.SPEC【02】 | ~~，支持CLB INPUT XBAR、CLB_XBAR、CLB_OUTPUT XBAR~~ | [GameViewer_Gg0PKIieqf.png](../images/GameViewer_Gg0PKIieqf.png) | 红色删除线 |
| XBAR-C13 | 3.3／ET6601修改点 | 去除SDFM通道SD*FLT*_EVT* | [GameViewer_Z7r3yKz86a.png](../images/GameViewer_Z7r3yKz86a.png) | 明确6601红字；原第5项另挂U03 |
| XBAR-C14 | 3.3／ET6601修改点 | 去除CLB*_OUT*和CLB_INPUTXBAR* | [GameViewer_Z7r3yKz86a.png](../images/GameViewer_Z7r3yKz86a.png) | 明确6601红字；原第5项另挂U03 |
| XBAR-C15 | 3.3／ET6601修改点 | 去除ADCC_EVT* | [GameViewer_Z7r3yKz86a.png](../images/GameViewer_Z7r3yKz86a.png) | 明确6601红字；原第5项另挂U03 |
| XBAR-C16 | 3.3／ET6601修改点 | 去除EPWM12~17_FAULTREAL | [GameViewer_Z7r3yKz86a.png](../images/GameViewer_Z7r3yKz86a.png) | 明确6601红字；原第5项另挂U03 |
| XBAR-C17 | 3.3／ET6601修改点 | 新增ETIMOUT12/13和ETIM12/13_FAULTREAL | [GameViewer_Z7r3yKz86a.png](../images/GameViewer_Z7r3yKz86a.png) | 明确6601红字；原第5项另挂U03 |
| XBAR-C18 | 3.3／SPEC16源表0～16 | 红色Reserved位于(0～14偶数行,列1)、(1～15奇数行,列2)、(16,列0/1/2)；空白列3的1/3/5/7不补值 | [GameViewer_Z7r3yKz86a.png](../images/GameViewer_Z7r3yKz86a.png) | 表内红字及左修订线；坐标是转录定位，不推断旧源名 |
| XBAR-C19 | 3.3／SPEC16源表17～63 | 红色Reserved逐格保留；ETIMOUT10/11/12/13及ETIM12/13_FAULTREAL红字 | [GameViewer_CqeT5pUL1x.png](../images/GameViewer_CqeT5pUL1x.png) | 红字来源位置；完整坐标与文字在正文续表，旧值未明不补 |
| XBAR-C20 | 3.3／SPEC20 | 支持PWM XBAR输出16bit，顶层选择后分别连接到12个PWM通道 | [GameViewer_CqeT5pUL1x.png](../images/GameViewer_CqeT5pUL1x.png) | 12红字；原16bit黑字保留 |
| XBAR-C21 | 3.4／ET6601修改点1 | 去除SDFM通道SD*FLT*_EVT*和SD*FLT*_EVT0_OR_EVT1 | [GameViewer_x1UNjKA5fU.png](../images/GameViewer_x1UNjKA5fU.png) | 明确6601红字 |
| XBAR-C22 | 3.4／ET6601修改点2 | 去除EPWM12~17_FAULTREAL | [GameViewer_x1UNjKA5fU.png](../images/GameViewer_x1UNjKA5fU.png) | 明确6601红字 |
| XBAR-C23 | 3.4／SPEC21源表 | 列3的0～31全为红色Reserved；列1及列2的红色Reserved逐格见正文 | [GameViewer_x1UNjKA5fU.png](../images/GameViewer_x1UNjKA5fU.png) | 表内红字及修订线；ADC C等黑字项不随PWM表删除 |
| XBAR-C24 | 3.4／SPEC25 | 支持ETIM XBAR输出14bit，分别连接到14个ETIMER通道 | [GameViewer_x1UNjKA5fU.png](../images/GameViewer_x1UNjKA5fU.png) | 14bit/14红字 |
| XBAR-C25 | 3.4／SPEC26 | 支持软件可配置14bit CFG_ETXB_SWx寄存器，分别对应14个ETIMER通道XBAR选择 | [GameViewer_x1UNjKA5fU.png](../images/GameViewer_x1UNjKA5fU.png) | 两处14红字 |

## 第三部分：局部缺口与原文差异

### XBAR-U01

图1源／目标底部位宽、GPIO完整编号、两条中断输出完整标识及局部红线范围尚不清；已保留可辨源、模块、目的标签和删除位置。需同版原图清晰局部；不以正文数值反填。

原图：[GameViewer_SMcbqY9aCU.png](../images/GameViewer_SMcbqY9aCU.png)。状态：开放。

### XBAR-U02

INPUT XBAR连接图的INT支路与直接到SARC支路细标记尚未逐字符确认；其余可辨连线和16/12/14/4等各自保存，不以正文数量补图字。

原图：[GameViewer_CpOsnywQhu.png](../images/GameViewer_CpOsnywQhu.png)。状态：开放。

### XBAR-U03

PWM ET6601清单第5项位置可见5）及Delete / 6 (0#~5#)，未见可确定功能语句；原文内容与修订浮层边界待同版原件确认。其余五项按原编号保存。

原图：[GameViewer_Z7r3yKz86a.png](../images/GameViewer_Z7r3yKz86a.png)。状态：开放。

原文所述AMBA3 AHB Lite→AHB、nManager APB与XBAR.SPEC【01】的APB分别保留；历史8→14位和6601的12→14位不统一。历史版本事项不转为6601新增。
