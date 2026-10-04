# CPLD_REG

> 来源：ET6601 原始截图精准还原  
> CPLD 为 ET6601 新 IP，本文件不建立“ET6601 修改点”章节。  
> 原始表格中的水印、时间戳、Excel 选中框以及“新增寄存器 / 新增域段 / 检查 / 升级”等界面控件不计入正文。

## 1. 表头信息

| 项目 | 原文 |
|---|---|
| Module Name | cpld_cfg |
| Data_Width | 32 |
| CFG_IF | AHB |
| Base_Addr | 0x000 |
| Addr_Width | 12 |

原始表头：

- Table/Register discription
- Field discription
- Reg name
- Discription
- REG Properties
- offset addr
- width
- default value
- Field name
- filed range
- field attribute: S/W, H/W
- Field default value
- field discription
- Field Properties
- P_reserved

## 2. 寄存器表

截图按原始表格行号连续恢复：
- `images/GameViewer_Fi0vMedNfB.png`：源行 6–19
- `images/GameViewer_ZlKSgCi2AU.png`：源行 20–34
- `images/GameViewer_VyNqGG3Mj6.png`：源行 35–41
- `images/GameViewer_ehusonHEeP.png`：源行 42–47
- `images/GameViewer_er1i0CeSs6.png`：源行 48–53
- `images/GameViewer_lCjo9mFfHG.png`：源行 54–59
- `images/GameViewer_6BxAbFuaFj.png`：源行 60–65
- `images/GameViewer_lGL9ilGPp4.png`：源行 66–71
- `images/GameViewer_L2kHUqr7hq.png`：源行 72–82

| 源行 | Reg name | offset addr | width | default value | Field name | filed range | S/W | H/W | Field default value | field discription | Field Properties | P_reserved |
|---:|---|---|---:|---|---|---|---|---|---|---|---|---|
| 6 | CFG_EFPGA0 | 0x00000000 | 32 | 0x00000000 | val | 31:0 | rw | ro | 0x00000000 | eFPGA配置信号 |  |  |
| 7 | CFG_EFPGA1 | 0x00000004 | 32 | 0x00000000 | val | 31:0 | rw | ro | 0x00000000 | eFPGA配置信号 |  |  |
| 8 | CFG_EFPGA_MASK | 0x00000008 | 32 | 0x00000000 | en | 0 | rw | ro | 0x00000000 | eFPGA配置信号屏蔽使能<br>1'b1：屏蔽配置信号<br>1'b0：配置正常输出 |  |  |
| 9 | EFPGA_RPT0 | 0x0000000C | 32 | 0x00000000 | val | 31:0 | ro | wo | 0x00000000 | eFPGA上报信号 | registered=false |  |
| 10 | EFPGA_RPT1 | 0x00000010 | 32 | 0x00000000 | val | 31:0 | ro | wo | 0x00000000 | eFPGA上报信号 | registered=false |  |
| 11 | CFG_CPLD_PLL_LOS_STATUS | 0x00000014 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 12 | CFG_SRPWM_CPLD_PWM_A | 0x00000018 | 32 | 0x00000000 | pipe_sel | 26:16 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 13 |  |  |  |  | sync_sel | 10:0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 14 | CFG_SRPWM_CPLD_PWM_B | 0x0000001C | 32 | 0x00000000 | pipe_sel | 26:16 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 15 |  |  |  |  | sync_sel | 10:0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 16 | CFG_SRPWM_CPLD_PWMA_OEN | 0x00000020 | 32 | 0x00000000 | pipe_sel | 26:16 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 17 |  |  |  |  | sync_sel | 10:0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 18 | CFG_SRPWM_CPLD_PWMB_OEN | 0x00000024 | 32 | 0x00000000 | pipe_sel | 26:16 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 19 |  |  |  |  | sync_sel | 10:0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 20 | CFG_ETIM_CPLD_PWM | 0x00000028 | 32 | 0x00000000 | pipe_sel | 25:16 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 21 |  |  |  |  | sync_sel | 9:0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 22 | CFG_PAD_CPLD_IN1 | 0x0000002C | 32 | 0x00000000 | reserved | 3:0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 23 | CFG_PAD_CPLD_IN0 | 0x00000030 | 32 | 0x00000000 | sync_sel | 31:0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 24 | CFG_CPU0_LOCKUP | 0x00000034 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 25 | CFG_CPU1_LOCKUP | 0x00000038 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 26 | CFG_BUS_TIMEOUT | 0x0000003C | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 27 | CFG_TEMP_WARN | 0x00000040 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 28 | CFG_POWER_ERR | 0x00000044 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 29 | CFG_PWR_OCP_WARN | 0x00000048 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 30 | CFG_POR_UV_WARN | 0x0000004C | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 31 | CFG_POR_OV_WARN | 0x00000050 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 32 | CFG_SOC_HARD_RST_N | 0x00000054 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 33 | CFG_SOC_WDG0_RST_N | 0x00000058 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 34 | CFG_SOC_WDG1_RST_N | 0x0000005C | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 35 | CFG_SOC_SOFT_RST_N | 0x00000060 | 32 | 0x00000000 | sync_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号做异步处理；<br>1'b0：bypass |  |  |
| 36 | CFG_ETIM_CPLD_SYNC | 0x00000064 | 32 | 0x00000000 | pipe_sel | 16 | rw | ro | 0x00000000 | 1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 37 |  |  |  |  | edge_sel | 9:8 | rw | ro | 0x00000000 | 2'b0：bypass<br>2'b1：上升沿<br>2'b2：下降沿<br>2'b3：双沿 |  |  |
| 38 |  |  |  |  | sync_sel | 5:4 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 39 |  |  |  |  | extend_sel | 0 | rw | ro | 0x00000000 | 1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 40 | CFG_INXB_CPLD_DATA_EXTEND | 0x00000068 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 41 | CFG_INXB_CPLD_DATA_SYNC | 0x0000006C | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 42 | CFG_INXB_CPLD_DATA_EDGE | 0x00000070 | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 43 | CFG_INXB_CPLD_DATA_PIPE | 0x00000074 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 44 | CFG_PFXB_CPLD_DATA_EXTEND | 0x00000078 | 32 | 0x00000000 | sel | 10:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 45 | CFG_PFXB_CPLD_DATA_SYNC | 0x0000007C | 32 | 0x00000000 | sel | 21:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 46 | CFG_PFXB_CPLD_DATA_EDGE | 0x00000080 | 32 | 0x00000000 | sel | 21:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 47 | CFG_PFXB_CPLD_DATA_PIPE | 0x00000084 | 32 | 0x00000000 | sel | 10:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 48 | CFG_ETXB_CPLD_DATA_EXTEND | 0x00000088 | 32 | 0x00000000 | sel | 9:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 49 | CFG_ETXB_CPLD_DATA_SYNC | 0x0000008C | 32 | 0x00000000 | sel | 19:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 50 | CFG_ETXB_CPLD_DATA_EDGE | 0x00000090 | 32 | 0x00000000 | sel | 19:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 51 | CFG_ETXB_CPLD_DATA_PIPE | 0x00000094 | 32 | 0x00000000 | sel | 9:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 52 | CFG_CMPC_CPLD_EVTH_EXTEND | 0x00000098 | 32 | 0x00000000 | sel | 9:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 53 | CFG_CMPC_CPLD_EVTH_SYNC | 0x0000009C | 32 | 0x00000000 | sel | 19:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 54 | CFG_CMPC_CPLD_EVTH_EDGE | 0x000000A0 | 32 | 0x00000000 | sel | 19:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 55 | CFG_CMPC_CPLD_EVTH_PIPE | 0x000000A4 | 32 | 0x00000000 | sel | 9:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 56 | CFG_CMPC_CPLD_EVTL_EXTEND | 0x000000A8 | 32 | 0x00000000 | sel | 9:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 57 | CFG_CMPC_CPLD_EVTL_SYNC | 0x000000AC | 32 | 0x00000000 | sel | 19:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 58 | CFG_CMPC_CPLD_EVTL_EDGE | 0x000000B0 | 32 | 0x00000000 | sel | 19:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 59 | CFG_CMPC_CPLD_EVTL_PIPE | 0x000000B4 | 32 | 0x00000000 | sel | 9:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 60 | CFG_ADC0_CPLD_EVTH_EXTEND | 0x000000B8 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 61 | CFG_ADC0_CPLD_EVTH_SYNC | 0x000000BC | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 62 | CFG_ADC0_CPLD_EVTH_EDGE | 0x000000C0 | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 63 | CFG_ADC0_CPLD_EVTH_PIPE | 0x000000C4 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 64 | CFG_ADC0_CPLD_EVTL_EXTEND | 0x000000C8 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 65 | CFG_ADC0_CPLD_EVTL_SYNC | 0x000000CC | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 66 | CFG_ADC0_CPLD_EVTL_EDGE | 0x000000D0 | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 67 | CFG_ADC0_CPLD_EVTL_PIPE | 0x000000D4 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 68 | CFG_ADC1_CPLD_EVTH_EXTEND | 0x000000D8 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 69 | CFG_ADC1_CPLD_EVTH_SYNC | 0x000000DC | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 70 | CFG_ADC1_CPLD_EVTH_EDGE | 0x000000E0 | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 71 | CFG_ADC1_CPLD_EVTH_PIPE | 0x000000E4 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 72 | CFG_ADC1_CPLD_EVTL_EXTEND | 0x000000E8 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号在soc时钟下展宽15拍；<br>1'b0：bypass |  |  |
| 73 | CFG_ADC1_CPLD_EVTL_SYNC | 0x000000EC | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 74 | CFG_ADC1_CPLD_EVTL_EDGE | 0x000000F0 | 32 | 0x00000000 | sel | 31:0 | rw | ro | 0x00000000 | 每2bit对应相应通道：<br>第1bit：<br>1'b0：展宽后的信号；<br>1'b1：异步处理后的信号；<br>第2bit：<br>1'b1：通过第1bit选择后的信号；<br>1'b0：bypass； |  |  |
| 75 | CFG_ADC1_CPLD_EVTL_PIPE | 0x000000F4 | 32 | 0x00000000 | sel | 15:0 | rw | ro | 0x00000000 | 每一bit对应相应通道：<br>1'b1：信号做打拍；<br>1'b0：bypass |  |  |
| 76 | PPI_BUS | 0x000000F8 | 32 | 0x00000000 | dout | 31:20 | ro | wo | 0x00000000 | reserved | registered=false |  |
| 77 |  |  |  |  | din | 16:5 | rw | ro | 0x00000000 | PPI 地址 |  |  |
| 78 |  |  |  |  | addr | 4:0 | rw | ro | 0x00000000 | PPI 输入数据 |  |  |
| 79 | PPI_FIFO |  | 32 | 0x00000000 | waterline | 20:16 | rw | ro | 0x00000000 | reserved |  |  |
| 80 |  |  |  |  | wptr_rpt | 12:8 | ro | wo | 0x00000000 | PPI写FIFO指针 |  |  |
| 81 |  |  |  |  | full_rpt | 4 | ro | wo | 0x00000000 | PPI写FIFO满信号 |  |  |
| 82 |  |  |  |  | empty_rpt | 0 | ro | wo | 0x00000000 | PPI写FIFO空信号 |  |  |


> ⚠️ 【待人工复核】源行 79 的 `PPI_FIFO` 在截图中未显示可确认的 `offset addr`，因此保持为空，不按地址连续性自行补值。  
> ⚠️ 【待人工复核】源行 76–78 的 `PPI_BUS` 字段说明按截图可见行位置原样恢复；其中 `dout` 对应“reserved”、`din` 对应“PPI 地址”、`addr` 对应“PPI 输入数据”，未按字段名推断或调换。
