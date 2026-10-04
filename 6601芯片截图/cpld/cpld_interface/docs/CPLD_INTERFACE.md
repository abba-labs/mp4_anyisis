# CPLD_INTERFACE

> 来源：ET6601 原始截图还原  
> 状态：恢复中。本文件是 CPLD_INTERFACE 的唯一合并文档；历史 interface_* 目录仅作为原始截图来源，后续全部并入本文件。  
> CPLD 为 ET6601 新 IP，本文件不建立“ET6601 修改点”章节。

## 1. CPLD 顶层接口

原图：
- ../interface_cpld/images/GameViewer_atyH2wpPCk.png
- ../interface_cpld/images/GameViewer_BtApOlYWLK.png
- ../interface_cpld/images/GameViewer_hN7LUohFXY.png

| 信号类 | 来源 | 输出目的地 | Signal name | inout | pre-process | width | sync type | 说明 |
|---|---|---|---|---|---|---:|---|---|
| 时钟 | TOP_CRG | CPLD | soc_sys_clk | input |  | 1 |  | MCU系统时钟，对应eFPGA free_clk3 |
| 时钟 | TOP_CRG | CPLD | cpld_clk | input |  | 1 |  |  |
| 时钟 | TOP_CRG | CPLD | cpld_25m | input |  | 1 |  |  |
| 时钟 | TOP_CRG | CPLD | cfg_clk_div_freeclk0 | input |  | 8 |  |  |
| 时钟 | TOP_CRG | CPLD | cfg_clk_div_freeclk1 | input |  | 8 |  |  |
| 时钟 | TOP_CRG | CPLD | cfg_clk_div_freeclk3 | input |  | 8 |  |  |
| 时钟 | TOP_CRG | CPLD | cpld_pll_los_status | input | type1 | 1 |  |  |
| 门控 | TOP_CRG | CPLD | cpld_clk_gten | input |  | 5 |  |  |
| 复位 | TOP_CRG | CPLD | cpld_glb_rst_n | input |  | 1 |  | 在SOC系统SYSC模块的POR域配置，用于SOC系统复位eFPGA FCB和Fabric逻辑，复位配置写保护 |
| 复位 | TOP_CRG | CPLD | cpld_cfg_rst_n | input |  | 1 |  | 在SOC系统SYSC模块的POR域配置，仅复位CPLD子系统的寄存器配置电路，复位配置写保护 |
| 复位 | TOP_CRG | CPLD | cpld_lgc_rst_n | input |  | 1 |  | 在SOC系统SYSC模块的POR域配置，仅复位Fabric逻辑，不影响时钟及CPLD配置，是否关联SOC系统复位可配置，默认不关联；原截图右侧文字被截断，末尾待复核 |
| 复位 | TOP_CRG | CPLD | cpld_user_rst_n | input |  | 1 |  | 用户软复位输入，用户逻辑使用，连接到eFPGA的io_resetn，由SOC系统寄存器配置或IO输入（TBD） |
| 复位 | CRG | CPLD | soc_hard_rst_n | input | type1 | 1 |  | SOC硬复位 |
| 复位 | CRG | CPLD | soc_wdg0_rst_n | input | type1 | 1 |  | SOC看门狗0复位 |
| 复位 | CRG | CPLD | soc_wdg1_rst_n | input | type1 | 1 |  | SOC看门狗1复位 |
| 复位 | CRG | CPLD | soc_soft_rst_n | input | type1 | 1 |  | SOC软复位 |
| 复位 | eFPGA | SYSC/XBAR/CRG | c2s_rst_n | output |  | 2 |  | eFPGA用户逻辑到SOC系统的C2S_RSTN复位输出 |
| 中断 | eFPGA | SOC | cpld_usr_intr | output |  | 1 | 异步处理 | 中断；b0：用户中断0；b1：用户中断1；b2：PPI读水线； |
| DMA | eFPGA | SOC | cpld_usr_dma | output |  | 2 |  | 用户自定义逻辑产生的DMA触发源 |
| 总线 | SOC | CPLD | cpld_ahb0_hwrite | input |  | 1 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb0_haddr | input |  | 12 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb0_hwdata | input |  | 32 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb0_hready | input |  | 1 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb0_htrans | input |  | 2 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb0_hsize | input |  | 3 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb0_hprot | input |  | 4 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb0_hsel | input |  | 1 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb0_hburst | input |  | 3 | 总线桥 | AHB0 |
| 总线 | CPLD | SOC | cpld_ahb0_hrdata | output |  | 32 | 总线桥 | AHB0 |
| 总线 | CPLD | SOC | cpld_ahb0_hreadyout | output |  | 1 | 总线桥 | AHB0 |
| 总线 | CPLD | SOC | cpld_ahb0_hresp | output |  | 1 | 总线桥 | AHB0 |
| 总线 | SOC | CPLD | cpld_ahb1_hwrite | input |  | 1 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_haddr | input |  | 12 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hwdata | input |  | 32 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hready | input |  | 1 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_htrans | input |  | 2 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hsize | input |  | 3 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hprot | input |  | 4 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hsel | input |  | 1 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hburst | input |  | 3 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hrdata | output |  | 32 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hreadyout | output |  | 1 | 总线桥 | AHB1 |
| 总线 | SOC | CPLD | cpld_ahb1_hresp | output |  | 1 | 总线桥 | AHB1 |
| 互联 | eFPGA | SYSC | cpld_cfg_err_sync | output |  | 1 |  | CPLD配置错误信号，已同步在sys_clk时钟下 |
| 互联 | eFPGA | SYSC | cpld_cfg_done_sync | output |  | 1 |  | CPLD配置完成信号，已同步在sys_clk时钟下 |
| 互联 | SRPWM | CPLD | srpwm_cpld_pwm_a | input | type0 | 12 | SYNC | srpwm A相 |
| 互联 | SRPWM | CPLD | srpwm_cpld_pwm_b | input | type0 | 12 | SYNC | srpwm B相 |
| 互联 | SRPWM | CPLD | srpwm_cpld_pwma_oen | input | type0 | 12 | SYNC | srpwm A相 OEN |
| 互联 | SRPWM | CPLD | srpwm_cpld_pwmb_oen | input | type0 | 12 | SYNC | srpwm B相 OEN |
| 互联 | ETIM | CPLD | etim_cpld_pwm | input | type0 | 10 | SYNC | ETIM pwm输出 |
| 互联 | XBAR | CPLD | inxb_cpld_data | input | type2 | 16 | SYNC | inputxbar发送到cpld的数据 |
| 互联 | XBAR | CPLD | pfxb_cpld_data | input | type2 | 11 | SYNC | pwmxbar发送到cpld的数据 |
| 互联 | XBAR | CPLD | etxb_cpld_data | input | type2 | 10 | SYNC | etimxbar发送到cpld的数据 |
| 互联 | CPLD | XBAR | cpld_opxb_data | output |  | 10 |  | efpga发送给srpwm的封波信号 |
| 互联 | CPLD | SRPWM | cpld_srpwm_fault | output |  | 24 |  | eFPGA发送到SRPWM的FAULT信号，电平信号，高电平有效 |
| 互联 | ETIM | CPLD | etim_cpld_sync | input | type2 | 1 | SYNC | ETIM同步信号，脉冲信号，高有效； |
| 互联 | CMPC | CPLD | cmpc_cpld_evth | input | type2 | 10 | SYNC | CMPC高电平比较器事件，电平或脉冲信号，高有效 |
| 互联 | CMPC | CPLD | cmpc_cpld_evtl | input | type2 | 10 | SYNC | CMPC低电平比较器事件，电平或脉冲信号，高有效 |
| 互联 | ADC | CPLD | adc0_cpld_evth | input | type2 | 16 | SYNC | ADC0高事件，电平或脉冲信号，高有效 |
| 互联 | ADC | CPLD | adc0_cpld_evtl | input | type2 | 16 | SYNC | ADC0低事件，电平或脉冲信号，高有效 |
| 互联 | ADC | CPLD | adc1_cpld_evth | input | type2 | 16 | SYNC | ADC1高事件，电平或脉冲信号，高有效 |
| 互联 | ADC | CPLD | adc1_cpld_evtl | input | type2 | 16 | SYNC | ADC1低事件，电平或脉冲信号，高有效 |
| 互联 | GPIO | CPLD | pad_cpld_in1 | input | type1 | 4 |  | PAD直接输入到CPLD的事件 |
| 互联 | GPIO | CPLD | pad_cpld_in0 | input | type1 | 32 | SYNC | PAD直接输入到CPLD的事件 |
| 互联 | CPLD | PAD | cpld_pad_out | output |  | 36 |  | efpga直接输出到pad |
| 互联 | CPLD | PAD | cpld_pad_oen | output |  | 36 |  | efpga直接输出到pad oen端 |
| 互联 | CPLD | PAD | cpld_debug_out | output |  | 4 |  | efpga调试管脚输出 |
| 互联 | SYSC | CPLD | cpu0_lockup | input | type1 | 1 | SYNC | CPU0死锁错误 |
| 互联 | SYSC | CPLD | cpu1_lockup | input | type1 | 1 | SYNC | CPU1死锁错误 |
| 互联 | SYSC | CPLD | bus_timeout | input | type1 | 1 | SYNC | 总线错误 |
| 互联 | SYSC | CPLD | temp_warn | input | type1 | 1 | SYNC | 过温警告 |
| 互联 | SYSC | CPLD | power_err | input | type1 | 1 | SYNC | ldo_ocp |
| 互联 | SYSC | CPLD | por_uv_warn | input | type1 | 1 | SYNC | 欠压警告 |
| 互联 | SYSC | CPLD | por_ov_warn | input | type1 | 1 | SYNC | 过压警告 |
| 互联 | SYSC | CPLD | s2c_cfg_enb | input |  | 1 |  | 保留输入0配置寄存器使能 |
| 互联 | SYSC | CPLD | s2c_cfg | input |  | 14 |  | 保留输入0 |
| 互联 | eFPGA | SYSC | c2s_rpt | output |  | 16 |  | 保留输出 |
| 互联 | SYSC | CPLD | sysc_cpld_testpin0_sel | input |  | 8 |  | testpin选择 |
| 互联 | SYSC | CPLD | sysc_cpld_testpin1_sel | input |  | 8 |  | testpin选择 |
| 互联 | SYSC | CPLD | sysc_cpld_testpin2_sel | input |  | 8 |  | testpin选择 |
| 互联 | SYSC | CPLD | sysc_cpld_testpin3_sel | input |  | 8 |  | testpin选择 |
| 互联 | CPLD | SYSC | cpld_sysc_testpin | output |  | 4 |  | testpin |

## 2. CPLD_CRG 接口

原图：../interface_cpld_crg/images/GameViewer_UipiANJp8o.png

| interface | inout | width | connect signal |
|---|---|---:|---|
| dft_mode | input | 1 | dft_mode |
| dft_crg_rst_n | input | 1 | dft_crg_rst_n |
| dft_lgc_rst_n | input | 1 | dft_lgc_rst_n |
| dft_glb_gt_se | input | 1 | dft_glb_gt_se |
| dft_div_freeclk0 | input | 8 | dft_div_freeclk0 |
| dft_div_freeclk1 | input | 8 | dft_div_freeclk1 |
| dft_div_freeclk3 | input | 8 | dft_div_freeclk3 |
| soc_sys_clk | input | 1 | soc_sys_clk |
| cpld_25m | input | 1 | cpld_25m |
| cpld_clk | input | 1 | cpld_clk |
| cfg_clk_div_freeclk0 | input | 8 | cfg_clk_div_freeclk0 |
| cfg_clk_div_freeclk1 | input | 8 | cfg_clk_div_freeclk1 |
| cfg_clk_div_freeclk3 | input | 8 | cfg_clk_div_freeclk3 |
| cpld_clk_gten | input | 5 | cpld_clk_gten |
| efpga_sys_clk | output | 1 | efpga_sys_clk |
| freeclk0 | output | 1 | free_clk0 |
| freeclk1 | output | 1 | free_clk1 |
| freeclk2 | output | 1 | free_clk2 |
| freeclk3 | output | 1 | free_clk3 |
| cpld_glb_rst_n | input | 1 | cpld_glb_rst_n |
| cpld_cfg_rst_n | input | 1 | cpld_cfg_rst_n |
| cpld_lgc_rst_n | input | 1 | cpld_lgc_rst_n |
| cpld_user_rst_n | input | 1 | cpld_user_rst_n |
| efpga_io_resetn0 | output | 1 | efpga_io_resetn0 |
| efpga_io_resetn1 | output | 1 | efpga_io_resetn1 |
| efpga_sys_resetn | output | 1 | efpga_sys_resetn |
| efpga_c2s_rst_n | input | 1 | efpga_c2s_rst_n |
| c2s_rst_n | output | 1 | c2s_rst_n |
| cpld_f0esync_rst_n | output | 1 | cpld_f0esync_rst_n |
| cpld_syscfg_rst_n | output | 1 | cpld_syscfg_rst_n |
| cpld_sys_rst_n | output | 1 | cpld_sys_rst_n |

> 原表备注：INSERT SIGNAL BEFORE THIS ROW

## 3. CPLD_TCU 接口

原图：../interface_cpld_tcu/images/GameViewer_W0SBPxoKtt.png

| interface | inout | width | connect signal |
|---|---|---:|---|
| dft_mode | output | 1 | dft_mode |
| dft_crg_rst_n | output | 1 | dft_crg_rst_n |
| dft_lgc_rst_n | output | 1 | dft_lgc_rst_n |
| dft_glb_gt_se | output | 1 | dft_glb_gt_se |
| dft_div_freeclk0 | output | 8 | dft_div_freeclk0 |
| dft_div_freeclk1 | output | 8 | dft_div_freeclk1 |
| dft_div_freeclk3 | output | 8 | dft_div_freeclk3 |
| dft_efpga_scan_in | output | 200 | dft_efpga_scan_in |
| dft_efpga_scan_out | input | 200 | dft_efpga_scan_out |
| dft_efpga_scan_en | output | 1 | dft_efpga_scan_en |
| dft_efpga_scan_clk | output | 1 | dft_efpga_scan_clk |
| dft_efpga_scan_rstn | output | 1 | dft_efpga_scan_rstn |

## 4. DMA 接口

原图：../interface_dma/images/GameViewer_VIiEW5kIvW.png

| signal | inout | width | connect_sig |
|---|---|---:|---|
| efpga_dma_req0 | input | 1 | efpga_dma_req0 |
| efpga_dma_req1 | input | 1 | efpga_dma_req1 |
| cpld_dma_req | output | 2 | cpld_usr_dma |

## 5. EFPGA_CFG 接口

原图：../interface_efpga_cfg/images/GameViewer_MLLzggVIdI.png

| signal | inout | width | connect_sig |
|---|---|---:|---|
| sys_clk | input | 1 | efpga_sys_clk |
| sys_rstn | input | 1 | cpld_sys_rst_n |
| efpga_clk | input | 1 | free_clk0 |
| efpga_rstn | input | 1 | cpld_f0esync_rst_n |
| cfg_efpga_mask_en | input | 1 | cfg_efpga_mask_en |
| cfg_efpga0_enb | input | 1 | cfg_efpga0_enb_nc |
| cfg_efpga0_val | input | 32 | cfg_efpga0_val |
| cfg_efpga1_enb | input | 1 | cfg_efpga1_enb_nc |
| cfg_efpga1_val | input | 32 | cfg_efpga1_val |
| cfg_efpga0_esync | output | 32 | cfg_efpga0_esync |
| cfg_efpga1_esync | output | 32 | cfg_efpga1_esync |
| efpga0_rpt | input | 32 | efpga0_rpt |
| efpga1_rpt | input | 32 | efpga1_rpt |
| efpga0_rpt_val_in | output | 32 | efpga0_rpt_val_in |
| efpga1_rpt_val_in | output | 32 | efpga1_rpt_val_in |
| s2c_cfg_enb | input | 1 | s2c_cfg_enb |
| s2c_cfg | input | 32 | s2c_cfg |
| s2c_cfg_esync | output | 32 | s2c_cfg_esync |

## 6. INT 接口

原图：../interface_int/images/GameViewer_UdwODJm0Oy.png

| signal | inout | width | connect_sig |
|---|---|---:|---|
| clk | input | 1 | soc_sys_clk |
| rst_n | input | 1 | efpga_sys_resetn |
| int_src_pulse | input | 2 | cpld_usr_intr_src |
| cpld_usr_intr | output | 2 | cpld_usr_intr |

## 7. PPI 接口

原图：../interface_ppi/images/GameViewer_E5Lo6kLaVW.png

| signal | inout | width | connect_sig |
|---|---|---:|---|
| sys_clk | input | 1 | efpga_sys_clk |
| sys_rstn | input | 1 | cpld_sys_rst_n |
| efpga_clk | input | 1 | free_clk0 |
| efpga_rstn | input | 1 | cpld_f0esync_rst_n |
| ppi_data_bus | input | 12 | ppi_bus_din |
| ppi_csn | output | 1 | ppi_csn |
| ppi_bus_enb | input | 1 | ppi_bus_enb_nc |
| ppi_addr | input | 5 | ppi_bus_addr |
| ppi_data_out | input | 12 | ppi_data_out |
| ppi_data_bus_esync | output | 12 | ppi_data_bus_esync |
| ppi_addr_esync | output | 5 | ppi_addr_esync |
| ppi_data_out_rpt | output | 12 | ppi_bus_dout_in |
| ppi_fifo_waterline | input | 5 | cfg_ppi_fifo_waterline |

## 8. TEST_PIN 接口

原图：../interface_test_pin/images/GameViewer_aGuTuqYiQP.png

| signal | inout | width | connect_sig | list number |
|---|---|---:|---|---|
| sysc_cpld_testpin0_sel | input | 8 | sysc_cpld_testpin0_sel |  |
| sysc_cpld_testpin1_sel | input | 8 | sysc_cpld_testpin1_sel |  |
| sysc_cpld_testpin2_sel | input | 8 | sysc_cpld_testpin2_sel |  |
| sysc_cpld_testpin3_sel | input | 8 | sysc_cpld_testpin3_sel |  |
| cpld_sysc_testpin | output | 4 | cpld_sysc_testpin |  |
| freeclk0 | input | 1 | free_clk0 | 5 |
| freeclk1 | input | 1 | free_clk1 | 6 |
| freeclk2 | input | 1 | free_clk2 | 7 |
| freeclk3 | input | 1 | free_clk3 | 8 |
| efpga_io_resetn0 | input | 1 | efpga_io_resetn0 | 10 |
| efpga_io_resetn1 | input | 1 | efpga_io_resetn1 | 11 |
| efpga_sys_resetn | input | 1 | efpga_sys_resetn | 12 |
| c2s_rst_n | input | 1 | c2s_rst_n | 13 |
| cpld_f0esync_rst_n | input | 1 | cpld_f0esync_rst_n | 14 |
| cpld_syscfg_rst_n | input | 1 | cpld_syscfg_rst_n | 15 |
| cpld_sys_rst_n | input | 1 | cpld_sys_rst_n | 16 |
| cpld_usr_intr_src | input | 2 | cpld_usr_intr_src | 17/18 |
| cpld_cfg_done_sync | input | 1 | cpld_cfg_done_sync | 19 |
| cpld_cfg_err_sync | input | 1 | cpld_cfg_err_sync | 20 |

## 9. CPLD_CFG 接口

> 恢复中：原始长表共至少 157 行，必须逐行从原截图合并，不使用旧 OCR 文本直接充当最终正文。

原图来源：../interface_cpld_cfg/images/

## 10. EFPGA 接口

> 恢复中：原始长表跨 16 张截图，必须按原始行号连续合并，不使用旧 OCR 文本直接充当最终正文。

原图来源：../interface_efpga/images/
