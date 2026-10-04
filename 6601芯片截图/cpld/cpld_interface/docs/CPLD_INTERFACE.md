# CPLD_INTERFACE

> 来源：ET6601 原始截图还原  
> 状态：恢复中。本文件是 CPLD_INTERFACE 的唯一合并文档；历史 interface_* 目录仅作为原始截图来源，后续全部并入本文件。  
> CPLD 为 ET6601 新 IP，本文件不建立“ET6601 修改点”章节。

## 1. CPLD 顶层接口

原图：
- ../../interface_cpld/images/GameViewer_atyH2wpPCk.png
- ../../interface_cpld/images/GameViewer_BtApOlYWLK.png
- ../../interface_cpld/images/GameViewer_hN7LUohFXY.png

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

原图：../../interface_cpld_crg/images/GameViewer_UipiANJp8o.png

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

原图：../../interface_cpld_tcu/images/GameViewer_W0SBPxoKtt.png

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

原图：../../interface_dma/images/GameViewer_VIiEW5kIvW.png

| signal | inout | width | connect_sig |
|---|---|---:|---|
| efpga_dma_req0 | input | 1 | efpga_dma_req0 |
| efpga_dma_req1 | input | 1 | efpga_dma_req1 |
| cpld_dma_req | output | 2 | cpld_usr_dma |

## 5. EFPGA_CFG 接口

原图：../../interface_efpga_cfg/images/GameViewer_MLLzggVIdI.png

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

原图：../../interface_int/images/GameViewer_UdwODJm0Oy.png

| signal | inout | width | connect_sig |
|---|---|---:|---|
| clk | input | 1 | soc_sys_clk |
| rst_n | input | 1 | efpga_sys_resetn |
| int_src_pulse | input | 2 | cpld_usr_intr_src |
| cpld_usr_intr | output | 2 | cpld_usr_intr |

## 7. PPI 接口

原图：../../interface_ppi/images/GameViewer_E5Lo6kLaVW.png

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

原图：../../interface_test_pin/images/GameViewer_aGuTuqYiQP.png

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

原图：
- ../../../interface_cpld_cfg/images/GameViewer_DeXJCeTp8c.png
- ../../../interface_cpld_cfg/images/GameViewer_DjmYAqFskT.png
- ../../../interface_cpld_cfg/images/GameViewer_1AL3gcTZwO.png
- ../../../interface_cpld_cfg/images/GameViewer_zJTLoUFpvE.png
- ../../../interface_cpld_cfg/images/GameViewer_XN1mwSbZGj.png
- ../../../interface_cpld_cfg/images/GameViewer_sB1DKm1Cn1.png

| signal | inout | width | connect_sig |
|---|---|---:|---|
| CFG_EFPGA0_val_r | output | 32 | cfg_efpga0_val |
| CFG_EFPGA0_enb | output | 1 | cfg_efpga0_enb_nc |
| CFG_EFPGA1_val_r | output | 32 | cfg_efpga1_val |
| CFG_EFPGA1_enb | output | 1 | cfg_efpga1_enb_nc |
| CFG_EFPGA_MASK_en_r | output | 1 | cfg_efpga_mask_en |
| CFG_EFPGA_MASK_enb | output | 1 | cfg_efpga_mask_enb_nc |
| EFPGA_RPT0_val_in | input | 32 | efpga_rpt0_val_in |
| EFPGA_RPT1_val_in | input | 32 | efpga_rpt1_val_in |
| CFG_CPLD_PLL_LOS_STATUS_sync_sel_r | output | 1 | cfg_cpld_pll_los_status_sync_sel |
| CFG_CPLD_PLL_LOS_STATUS_enb | output | 1 | cfg_cpld_pll_los_status_enb_nc |
| CFG_SRPWM_CPLD_PWM_A_pipe_sel_r | output | 11 | cfg_srpwm_cpld_pwm_a_pipe_sel |
| CFG_SRPWM_CPLD_PWM_A_sync_sel_r | output | 11 | cfg_srpwm_cpld_pwm_a_sync_sel |
| CFG_SRPWM_CPLD_PWM_A_enb | output | 1 | cfg_srpwm_cpld_pwm_a_enb_nc |
| CFG_SRPWM_CPLD_PWM_B_pipe_sel_r | output | 11 | cfg_srpwm_cpld_pwm_b_pipe_sel |
| CFG_SRPWM_CPLD_PWM_B_sync_sel_r | output | 11 | cfg_srpwm_cpld_pwm_b_sync_sel |
| CFG_SRPWM_CPLD_PWM_B_enb | output | 1 | cfg_srpwm_cpld_pwm_b_enb_nc |
| CFG_SRPWM_CPLD_PWMA_OEN_pipe_sel_r | output | 11 | cfg_srpwm_cpld_pwma_oen_pipe_sel |
| CFG_SRPWM_CPLD_PWMA_OEN_sync_sel_r | output | 11 | cfg_srpwm_cpld_pwma_oen_sync_sel |
| CFG_SRPWM_CPLD_PWMA_OEN_enb | output | 1 | cfg_srpwm_cpld_pwma_oen_enb_nc |
| CFG_SRPWM_CPLD_PWMB_OEN_pipe_sel_r | output | 11 | cfg_srpwm_cpld_pwmb_oen_pipe_sel |
| CFG_SRPWM_CPLD_PWMB_OEN_sync_sel_r | output | 11 | cfg_srpwm_cpld_pwmb_oen_sync_sel |
| CFG_SRPWM_CPLD_PWMB_OEN_enb | output | 1 | cfg_srpwm_cpld_pwmb_oen_enb_nc |
| CFG_ETIM_CPLD_PWM_pipe_sel_r | output | 10 | cfg_etim_cpld_pwm_pipe_sel |
| CFG_ETIM_CPLD_PWM_sync_sel_r | output | 10 | cfg_etim_cpld_pwm_sync_sel |
| CFG_ETIM_CPLD_PWM_enb | output | 1 | cfg_etim_cpld_pwm_enb_nc |
| CFG_PAD_CPLD_IN_sync_sel_r | output | 4 | cfg_pad_cpld_in_sync_sel |
| CFG_PAD_CPLD_IN_enb | output | 1 | cfg_pad_cpld_in_enb |
| CFG_CPU0_LOCKUP_sync_sel_r | output | 1 | cfg_cpu0_lockup_sync_sel |
| CFG_CPU0_LOCKUP_enb | output | 1 | cfg_cpu0_lockup_enb_nc |
| CFG_CPU1_LOCKUP_sync_sel_r | output | 1 | cfg_cpu1_lockup_sync_sel |
| CFG_CPU1_LOCKUP_enb | output | 1 | cfg_cpu1_lockup_enb_nc |
| CFG_BUS_TIMEOUT_sync_sel_r | output | 1 | cfg_bus_timeout_sync_sel |
| CFG_BUS_TIMEOUT_enb | output | 1 | cfg_bus_timeout_enb_nc |
| CFG_TEMP_WARN_sync_sel_r | output | 1 | cfg_temp_warn_sync_sel |
| CFG_TEMP_WARN_enb | output | 1 | cfg_temp_warn_enb_nc |
| CFG_POWER_ERR_sync_sel_r | output | 1 | cfg_power_err_sync_sel |
| CFG_POWER_ERR_enb | output | 1 | cfg_power_err_enb_nc |
| CFG_PWR_OCP_WARN_sync_sel_r | output | 1 | cfg_pwr_ocp_warn_sync_sel |
| CFG_PWR_OCP_WARN_enb | output | 1 | cfg_pwr_ocp_warn_enb_nc |
| CFG_POR_UV_WARN_sync_sel_r | output | 1 | cfg_por_uv_warn_sync_sel |
| CFG_POR_UV_WARN_enb | output | 1 | cfg_por_uv_warn_enb_nc |
| CFG_POR_OV_WARN_sync_sel_r | output | 1 | cfg_por_ov_warn_sync_sel |
| CFG_POR_OV_WARN_enb | output | 1 | cfg_por_ov_warn_enb_nc |
| CFG_SOC_HARD_RST_N_sync_sel_r | output | 1 | cfg_soc_hard_rst_n_sync_sel |
| CFG_SOC_HARD_RST_N_enb | output | 1 | cfg_soc_hard_rst_n_enb_nc |
| CFG_SOC_WDG0_RST_N_sync_sel_r | output | 1 | cfg_soc_wdg0_rst_n_sync_sel |
| CFG_SOC_WDG0_RST_N_enb | output | 1 | cfg_soc_wdg0_rst_n_enb_nc |
| CFG_SOC_WDG1_RST_N_sync_sel_r | output | 1 | cfg_soc_wdg1_rst_n_sync_sel |
| CFG_SOC_WDG1_RST_N_enb | output | 1 | cfg_soc_wdg1_rst_n_enb_nc |
| CFG_SOC_SOFT_RST_N_sync_sel_r | output | 1 | cfg_soc_soft_rst_n_sync_sel |
| CFG_SOC_SOFT_RST_N_enb | output | 1 | cfg_soc_soft_rst_n_enb_nc |
| CFG_ETIM_CPLD_SYNC_pipe_sel_r | output | 1 | cfg_etim_cpld_sync_pipe_sel |
| CFG_ETIM_CPLD_SYNC_edge_sel_r | output | 2 | cfg_etim_cpld_sync_edge_sel |
| CFG_ETIM_CPLD_SYNC_sync_sel_r | output | 2 | cfg_etim_cpld_sync_sync_sel |
| CFG_ETIM_CPLD_SYNC_extend_sel_r | output | 1 | cfg_etim_cpld_sync_extend_sel |
| CFG_ETIM_CPLD_SYNC_enb | output | 1 | cfg_etim_cpld_sync_enb_nc |
| CFG_INXB_CPLD_DATA_EXTEND_sel_r | output | 16 | cfg_inxb_cpld_data_extend_sel |
| CFG_INXB_CPLD_DATA_EXTEND_enb | output | 1 | cfg_inxb_cpld_data_extend_enb_nc |
| CFG_INXB_CPLD_DATA_SYNC_sel_r | output | 32 | cfg_inxb_cpld_data_sync_sel |
| CFG_INXB_CPLD_DATA_SYNC_enb | output | 1 | cfg_inxb_cpld_data_sync_enb_nc |
| CFG_INXB_CPLD_DATA_EDGE_sel_r | output | 32 | cfg_inxb_cpld_data_edge_sel |
| CFG_INXB_CPLD_DATA_EDGE_enb | output | 1 | cfg_inxb_cpld_data_edge_enb_nc |
| CFG_INXB_CPLD_DATA_PIPE_sel_r | output | 16 | cfg_inxb_cpld_data_pipe_sel |
| CFG_INXB_CPLD_DATA_PIPE_enb | output | 1 | cfg_inxb_cpld_data_pipe_enb_nc |
| CFG_PFXB_CPLD_DATA_EXTEND_sel_r | output | 11 | cfg_pfxb_cpld_data_extend_sel |
| CFG_PFXB_CPLD_DATA_EXTEND_enb | output | 1 | cfg_pfxb_cpld_data_extend_enb_nc |
| CFG_PFXB_CPLD_DATA_SYNC_sel_r | output | 22 | cfg_pfxb_cpld_data_sync_sel |
| CFG_PFXB_CPLD_DATA_SYNC_enb | output | 1 | cfg_pfxb_cpld_data_sync_enb_nc |
| CFG_PFXB_CPLD_DATA_EDGE_sel_r | output | 22 | cfg_pfxb_cpld_data_edge_sel |
| CFG_PFXB_CPLD_DATA_EDGE_enb | output | 1 | cfg_pfxb_cpld_data_edge_enb_nc |
| CFG_PFXB_CPLD_DATA_PIPE_sel_r | output | 11 | cfg_pfxb_cpld_data_pipe_sel |
| CFG_PFXB_CPLD_DATA_PIPE_enb | output | 1 | cfg_pfxb_cpld_data_pipe_enb_nc |
| CFG_ETXB_CPLD_DATA_EXTEND_sel_r | output | 10 | cfg_etxb_cpld_data_extend_sel |
| CFG_ETXB_CPLD_DATA_EXTEND_enb | output | 1 | cfg_etxb_cpld_data_extend_enb_nc |
| CFG_ETXB_CPLD_DATA_SYNC_sel_r | output | 20 | cfg_etxb_cpld_data_sync_sel |
| CFG_ETXB_CPLD_DATA_SYNC_enb | output | 1 | cfg_etxb_cpld_data_sync_enb_nc |
| CFG_ETXB_CPLD_DATA_EDGE_sel_r | output | 20 | cfg_etxb_cpld_data_edge_sel |
| CFG_ETXB_CPLD_DATA_EDGE_enb | output | 1 | cfg_etxb_cpld_data_edge_enb_nc |
| CFG_ETXB_CPLD_DATA_PIPE_sel_r | output | 10 | cfg_etxb_cpld_data_pipe_sel |
| CFG_ETXB_CPLD_DATA_PIPE_enb | output | 1 | cfg_etxb_cpld_data_pipe_enb_nc |
| CFG_CMPC_CPLD_EVTH_EXTEND_sel_r | output | 10 | cfg_cmpc_cpld_evth_extend_sel |
| CFG_CMPC_CPLD_EVTH_EXTEND_enb | output | 1 | cfg_cmpc_cpld_evth_extend_enb_nc |
| CFG_CMPC_CPLD_EVTH_SYNC_sel_r | output | 20 | cfg_cmpc_cpld_evth_sync_sel |
| CFG_CMPC_CPLD_EVTH_SYNC_enb | output | 1 | cfg_cmpc_cpld_evth_sync_enb_nc |
| CFG_CMPC_CPLD_EVTH_EDGE_sel_r | output | 20 | cfg_cmpc_cpld_evth_edge_sel |
| CFG_CMPC_CPLD_EVTH_EDGE_enb | output | 1 | cfg_cmpc_cpld_evth_edge_enb_nc |
| CFG_CMPC_CPLD_EVTH_PIPE_sel_r | output | 10 | cfg_cmpc_cpld_evth_pipe_sel |
| CFG_CMPC_CPLD_EVTH_PIPE_enb | output | 1 | cfg_cmpc_cpld_evth_pipe_enb_nc |
| CFG_CMPC_CPLD_EVTL_EXTEND_sel_r | output | 10 | cfg_cmpc_cpld_evtl_extend_sel |
| CFG_CMPC_CPLD_EVTL_EXTEND_enb | output | 1 | cfg_cmpc_cpld_evtl_extend_enb_nc |
| CFG_CMPC_CPLD_EVTL_SYNC_sel_r | output | 20 | cfg_cmpc_cpld_evtl_sync_sel |
| CFG_CMPC_CPLD_EVTL_SYNC_enb | output | 1 | cfg_cmpc_cpld_evtl_sync_enb_nc |
| CFG_CMPC_CPLD_EVTL_EDGE_sel_r | output | 20 | cfg_cmpc_cpld_evtl_edge_sel |
| CFG_CMPC_CPLD_EVTL_EDGE_enb | output | 1 | cfg_cmpc_cpld_evtl_edge_enb_nc |
| CFG_CMPC_CPLD_EVTL_PIPE_sel_r | output | 10 | cfg_cmpc_cpld_evtl_pipe_sel |
| CFG_CMPC_CPLD_EVTL_PIPE_enb | output | 1 | cfg_cmpc_cpld_evtl_pipe_enb_nc |
| CFG_ADC0_CPLD_EVTH_EXTEND_sel_r | output | 16 | cfg_adc0_cpld_evth_extend_sel |
| CFG_ADC0_CPLD_EVTH_EXTEND_enb | output | 1 | cfg_adc0_cpld_evth_extend_enb_nc |
| CFG_ADC0_CPLD_EVTH_SYNC_sel_r | output | 32 | cfg_adc0_cpld_evth_sync_sel |
| CFG_ADC0_CPLD_EVTH_SYNC_enb | output | 1 | cfg_adc0_cpld_evth_sync_enb_nc |
| CFG_ADC0_CPLD_EVTH_EDGE_sel_r | output | 32 | cfg_adc0_cpld_evth_edge_sel |
| CFG_ADC0_CPLD_EVTH_EDGE_enb | output | 1 | cfg_adc0_cpld_evth_edge_enb_nc |
| CFG_ADC0_CPLD_EVTH_PIPE_sel_r | output | 16 | cfg_adc0_cpld_evth_pipe_sel |
| CFG_ADC0_CPLD_EVTH_PIPE_enb | output | 1 | cfg_adc0_cpld_evth_pipe_enb_nc |
| CFG_ADC0_CPLD_EVTL_EXTEND_sel_r | output | 16 | cfg_adc0_cpld_evtl_extend_sel |
| CFG_ADC0_CPLD_EVTL_EXTEND_enb | output | 1 | cfg_adc0_cpld_evtl_extend_enb_nc |
| CFG_ADC0_CPLD_EVTL_SYNC_sel_r | output | 32 | cfg_adc0_cpld_evtl_sync_sel |
| CFG_ADC0_CPLD_EVTL_SYNC_enb | output | 1 | cfg_adc0_cpld_evtl_sync_enb_nc |
| CFG_ADC0_CPLD_EVTL_EDGE_sel_r | output | 32 | cfg_adc0_cpld_evtl_edge_sel |
| CFG_ADC0_CPLD_EVTL_EDGE_enb | output | 1 | cfg_adc0_cpld_evtl_edge_enb_nc |
| CFG_ADC0_CPLD_EVTL_PIPE_sel_r | output | 16 | cfg_adc0_cpld_evtl_pipe_sel |
| CFG_ADC0_CPLD_EVTL_PIPE_enb | output | 1 | cfg_adc0_cpld_evtl_pipe_enb_nc |
| CFG_ADC1_CPLD_EVTH_EXTEND_sel_r | output | 16 | cfg_adc1_cpld_evth_extend_sel |
| CFG_ADC1_CPLD_EVTH_EXTEND_enb | output | 1 | cfg_adc1_cpld_evth_extend_enb_nc |
| CFG_ADC1_CPLD_EVTH_SYNC_sel_r | output | 32 | cfg_adc1_cpld_evth_sync_sel |
| CFG_ADC1_CPLD_EVTH_SYNC_enb | output | 1 | cfg_adc1_cpld_evth_sync_enb_nc |
| CFG_ADC1_CPLD_EVTH_EDGE_sel_r | output | 32 | cfg_adc1_cpld_evth_edge_sel |
| CFG_ADC1_CPLD_EVTH_EDGE_enb | output | 1 | cfg_adc1_cpld_evth_edge_enb_nc |
| CFG_ADC1_CPLD_EVTH_PIPE_sel_r | output | 16 | cfg_adc1_cpld_evth_pipe_sel |
| CFG_ADC1_CPLD_EVTH_PIPE_enb | output | 1 | cfg_adc1_cpld_evth_pipe_enb_nc |
| CFG_ADC1_CPLD_EVTL_EXTEND_sel_r | output | 16 | cfg_adc1_cpld_evtl_extend_sel |
| CFG_ADC1_CPLD_EVTL_EXTEND_enb | output | 1 | cfg_adc1_cpld_evtl_extend_enb_nc |
| CFG_ADC1_CPLD_EVTL_SYNC_sel_r | output | 32 | cfg_adc1_cpld_evtl_sync_sel |
| CFG_ADC1_CPLD_EVTL_SYNC_enb | output | 1 | cfg_adc1_cpld_evtl_sync_enb_nc |
| CFG_ADC1_CPLD_EVTL_EDGE_sel_r | output | 32 | cfg_adc1_cpld_evtl_edge_sel |
| CFG_ADC1_CPLD_EVTL_EDGE_enb | output | 1 | cfg_adc1_cpld_evtl_edge_enb_nc |
| CFG_ADC1_CPLD_EVTL_PIPE_sel_r | output | 16 | cfg_adc1_cpld_evtl_pipe_sel |
| CFG_ADC1_CPLD_EVTL_PIPE_enb | output | 1 | cfg_adc1_cpld_evtl_pipe_enb_nc |
| PPI_BUS_dout_in | input | 12 | ppi_bus_dout_in |
| PPI_BUS_din_r | output | 12 | ppi_bus_din |
| PPI_BUS_addr_r | output | 5 | ppi_bus_addr |
| PPI_BUS_enb | output | 1 | ppi_bus_enb_nc |
| CFG_CPLD_INT_EN_val_r | output | 2 | cfg_cpld_int_en_val |
| CFG_CPLD_INT_EN_enb | output | 1 | cfg_cpld_int_en_enb_nc |
| CFG_CPLD_INT_MASK_val_r | output | 2 | cfg_cpld_int_mask_val |
| CFG_CPLD_INT_MASK_enb | output | 1 | cfg_cpld_int_mask_enb_nc |
| CFG_CPLD_INT_FORCE_IND_val_r | output | 2 | cfg_cpld_int_force_ind_val |
| CFG_CPLD_INT_FORCE_IND_enb | output | 1 | cfg_cpld_int_force_ind_enb_nc |
| CFG_CPLD_INT_CLR_val_r | output | 2 | cfg_cpld_int_clr_val |
| CFG_CPLD_INT_CLR_enb | output | 1 | cfg_cpld_int_clr_enb_nc |
| CPLD_INT_RAW_RPT_val_in | input | 2 | cpld_int_raw_rpt_val_in |
| CPLD_INT_STATUS_RPT_val_in | input | 2 | cpld_int_status_rpt_val_in |
| hclk | input | 1 | efpga_sys_clk |
| hresetn | input | 1 | cpld_sys_rst_n |
| haddr | input | 32 | cpld_ahb0_haddr |
| hwrite | input | 1 | cpld_ahb0_hwrite |
| hwdata | input | 32 | cpld_ahb0_hwdata |
| hrdata | output | 32 | cpld_ahb0_hrdata |
| hreadyout | output | 1 | cpld_ahb0_hreadyout |
| hresp | output | 1 | cpld_ahb0_hresp |
| hready | input | 1 | cpld_ahb0_hready |
| htrans | input | 2 | cpld_ahb0_htrans |
| hsize | input | 3 | cpld_ahb0_hsize |
| hprot | input | 4 | cpld_ahb0_hprot |
| hsel | input | 1 | cpld_ahb0_hsel |
| hburst | input | 3 | cpld_ahb0_hburst |

## 10. EFPGA 接口

> 恢复中：原始长表跨 16 张截图，必须按原始行号连续合并，不使用旧 OCR 文本直接充当最终正文。

原图来源：../../../interface_efpga/images/
