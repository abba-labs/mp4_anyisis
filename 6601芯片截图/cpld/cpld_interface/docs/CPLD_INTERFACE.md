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

原始截图按表格行号恢复顺序：
- ../../interface_efpga/images/GameViewer_8iXOmcDGE1.png（行 1–38）
- ../../interface_efpga/images/GameViewer_cU12ydgZ8V.png（行 39–74）
- ../../interface_efpga/images/GameViewer_Vhor9olOSG.png（行 75–110）
- ../../interface_efpga/images/GameViewer_J6lAwKnIhm.png（行 111–146）
- ../../interface_efpga/images/GameViewer_Nbjags3WBm.png（行 147–182）
- ../../interface_efpga/images/GameViewer_xPU5bUtZ6p.png（行 183–218）
- ../../interface_efpga/images/GameViewer_S8SQhpMWC2.png（行 219–254）
- ../../interface_efpga/images/GameViewer_grCDK0KTgW.png（行 255–290）
- ../../interface_efpga/images/GameViewer_uxeRXbUM3q.png（行 291–326）
- ../../interface_efpga/images/GameViewer_P0NFLfV564.png（行 327–362）
- ../../interface_efpga/images/GameViewer_3BoqyOeJgh.png（行 363–398）
- ../../interface_efpga/images/GameViewer_I7FEkY4HxN.png（行 399–434）
- ../../interface_efpga/images/GameViewer_gvjimz0mF4.png（行 435–470）
- ../../interface_efpga/images/GameViewer_2zddazPQIp.png（行 471–506）
- ../../interface_efpga/images/GameViewer_bCW62ClcKC.png（行 507–542）
- ../../interface_efpga/images/GameViewer_qhGTBAxdTy.png（行 543–554）

### 10.1 eFPGA interface

| eFPGA interface | inout | width | NO. | connect signal | 说明 |
|---|---|---:|---:|---|---|
| sys_clk | input | 1 |  | efpga_sys_clk | 200M时钟，与SOC系统时钟同步 |
| sys_resetn | input | 1 |  | efpga_sys_resetn | CPLD HARD_RST&S2C_ |
| wdt_sclk |  |  |  |  |  |
| fpga_s0_hrdata | output | 32 |  | cpld_ahb1_hrdata | AHB1 |
| fpga_s0_hreadyout | output | 1 |  | cpld_ahb1_hreadyout | AHB1 |
| fpga_s0_hresp | output | 1 |  | cpld_ahb1_hresp | AHB1 |
| fpga_s0_hsel | input | 1 |  | cpld_ahb1_hsel | AHB1 |
| fpga_s0_haddr | input | 32 |  | {20'd0,cpld_ahb1_haddr} | AHB1 |
| fpga_s0_htrans | input | 2 |  | cpld_ahb1_htrans | AHB1 |
| fpga_s0_hwrite | input | 1 |  | cpld_ahb1_hwrite | AHB1 |
| fpga_s0_hwdata | input | 32 |  | cpld_ahb1_hwdata | AHB1 |
| fpga_s0_hready | input | 1 |  | cpld_ahb1_hready | AHB1 |
| efpga_dec_en | input | 1 |  |  | eFPGA bitstream decipher enable |
| efpga_dec_key | input | 64 |  |  | eFPGA bitstream decipher key |
| fpga_intr | output | 4 | 3 | efpga_intr3_nc |  |
| fpga_intr | output | 4 | 2 | efpga_intr2_nc |  |
| fpga_intr | output | 4 | 1 | cpld_usr_intr_src[1] | 用户自定义中断，脉冲或电平 |
| fpga_intr | output | 4 | 0 | cpld_usr_intr_src[0] | 用户自定义中断，脉冲或电平 |
| fpga_cfg_done_sync | output | 1 |  | cpld_cfg_done_sync | bit流配置完成 |
| fpga_cfg_err | output | 1 |  | cpld_cfg_err_sync | bit流配置错误 |
| wdt_rstn_o | output | 1 |  | wdt_rstn_o_nc |  |
| free_clk0 | input | 1 |  | free_clk0 |  |
| free_clk1 | input | 1 |  | free_clk1 |  |
| free_clk2 | input | 1 |  | free_clk2 |  |
| free_clk3 | input | 1 |  | efpga_sys_clk |  |
| scan_in | input | 200 |  | dft_efpga_scan_in | DFT |
| scan_out | output | 200 |  | dft_efpga_scan_out | DFT |
| scan_en | input | 1 |  | dft_efpga_scan_en | DFT |
| scan_mode | input | 1 |  | dft_mode | DFT |
| scan_clk | input | 1 |  | dft_efpga_scan_clk | DFT |
| scan_rstn | input | 1 |  | dft_efpga_scan_rstn | DFT |
| io_resetn | input | 2 | 1 | efpga_io_resetn1 | 用户自定义逻辑用IO |
| io_resetn | input | 2 | 0 | efpga_io_resetn0 | 用户自定义逻辑用IO |

### 10.2 int_fpga_in

原表合并属性：inout = input，width = 320。

| NO. | connect signal | 说明 |
|---:|---|---|
| 319 | s2c_cfg_esync[7] | SYSC到eFPGA的保留配置 |
| 318 | s2c_cfg_esync[6] | SYSC到eFPGA的保留配置 |
| 317 | s2c_cfg_esync[5] | SYSC到eFPGA的保留配置 |
| 316 | s2c_cfg_esync[4] | SYSC到eFPGA的保留配置 |
| 315 | s2c_cfg_esync[3] | SYSC到eFPGA的保留配置 |
| 314 | s2c_cfg_esync[2] | SYSC到eFPGA的保留配置 |
| 313 | s2c_cfg_esync[1] | SYSC到eFPGA的保留配置 |
| 312 | s2c_cfg_esync[0] | SYSC到eFPGA的保留配置 |
| 311 | pad_cpld_in_esync[35] | PAD 直接输入eFPGA |
| 310 | pad_cpld_in_esync[34] | PAD 直接输入eFPGA |
| 309 | pad_cpld_in_esync[33] | PAD 直接输入eFPGA |
| 308 | pad_cpld_in_esync[32] | PAD 直接输入eFPGA |
| 307 | pad_cpld_in_esync[31] | PAD 直接输入eFPGA |
| 306 | pad_cpld_in_esync[30] | PAD 直接输入eFPGA |
| 305 | pad_cpld_in_esync[29] | PAD 直接输入eFPGA |
| 304 | pad_cpld_in_esync[28] | PAD 直接输入eFPGA |
| 303 | pad_cpld_in_esync[27] | PAD 直接输入eFPGA |
| 302 | pad_cpld_in_esync[26] | PAD 直接输入eFPGA |
| 301 | pad_cpld_in_esync[25] | PAD 直接输入eFPGA |
| 300 | pad_cpld_in_esync[24] | PAD 直接输入eFPGA |
| 299 | pad_cpld_in_esync[23] | PAD 直接输入eFPGA |
| 298 | pad_cpld_in_esync[22] | PAD 直接输入eFPGA |
| 297 | pad_cpld_in_esync[21] | PAD 直接输入eFPGA |
| 296 | pad_cpld_in_esync[20] | PAD 直接输入eFPGA |
| 295 | pad_cpld_in_esync[19] | PAD 直接输入eFPGA |
| 294 | pad_cpld_in_esync[18] | PAD 直接输入eFPGA |
| 293 | pad_cpld_in_esync[17] | PAD 直接输入eFPGA |
| 292 | pad_cpld_in_esync[16] | PAD 直接输入eFPGA |
| 291 | pad_cpld_in_esync[15] | PAD 直接输入eFPGA |
| 290 | pad_cpld_in_esync[14] | PAD 直接输入eFPGA |
| 289 | pad_cpld_in_esync[13] | PAD 直接输入eFPGA |
| 288 | pad_cpld_in_esync[12] | PAD 直接输入eFPGA |
| 287 | pad_cpld_in_esync[11] | PAD 直接输入eFPGA |
| 286 | pad_cpld_in_esync[10] | PAD 直接输入eFPGA |
| 285 | pad_cpld_in_esync[9] | PAD 直接输入eFPGA |
| 284 | pad_cpld_in_esync[8] | PAD 直接输入eFPGA |
| 283 | pad_cpld_in_esync[7] | PAD 直接输入eFPGA |
| 282 | pad_cpld_in_esync[6] | PAD 直接输入eFPGA |
| 281 | pad_cpld_in_esync[5] | PAD 直接输入eFPGA |
| 280 | pad_cpld_in_esync[4] | PAD 直接输入eFPGA |
| 279 | pad_cpld_in_esync[3] | PAD 直接输入eFPGA |
| 278 | pad_cpld_in_esync[2] | PAD 直接输入eFPGA |
| 277 | pad_cpld_in_esync[1] | PAD 直接输入eFPGA |
| 276 | pad_cpld_in_esync[0] | PAD 直接输入eFPGA |
| 275 | soc_hard_rst_n_esync | SOC HARD复位 |
| 274 | soc_wdg0_rst_n_esync | SOC看门狗0复位 |
| 273 | soc_wdg1_rst_n_esync | SOC看门狗1复位 |
| 272 | soc_soft_rst_n_esync | SOC 软复位 |
| 271 | cpld_pll_los_status_esync | CPLD PLL 频率状态；1'b1:无时钟或频率异常 |
| 270 | ppi_csn | PPI |
| 269 | ppi_data_bus_esync[11] | PPI |
| 268 | ppi_data_bus_esync[10] | PPI |
| 267 | ppi_data_bus_esync[9] | PPI |
| 266 | ppi_data_bus_esync[8] | PPI |
| 265 | ppi_data_bus_esync[7] | PPI |
| 264 | ppi_data_bus_esync[6] | PPI |
| 263 | ppi_data_bus_esync[5] | PPI |
| 262 | ppi_data_bus_esync[4] | PPI |
| 261 | ppi_data_bus_esync[3] | PPI |
| 260 | ppi_data_bus_esync[2] | PPI |
| 259 | ppi_data_bus_esync[1] | PPI |
| 258 | ppi_data_bus_esync[0] | PPI |
| 257 | ppi_addr_esync[4] | PPI |
| 256 | ppi_addr_esync[3] | PPI |
| 255 | ppi_addr_esync[2] | PPI |
| 254 | ppi_addr_esync[1] | PPI |
| 253 | ppi_addr_esync[0] | PPI |
| 252 | inxb_cpld_data_esync[15] | INPUTXBAR数据 |
| 251 | inxb_cpld_data_esync[14] | INPUTXBAR数据 |
| 250 | inxb_cpld_data_esync[13] | INPUTXBAR数据 |
| 249 | inxb_cpld_data_esync[12] | INPUTXBAR数据 |
| 248 | inxb_cpld_data_esync[11] | INPUTXBAR数据 |
| 247 | inxb_cpld_data_esync[10] | INPUTXBAR数据 |
| 246 | inxb_cpld_data_esync[9] | INPUTXBAR数据 |
| 245 | inxb_cpld_data_esync[8] | INPUTXBAR数据 |
| 244 | inxb_cpld_data_esync[7] | INPUTXBAR数据 |
| 243 | inxb_cpld_data_esync[6] | INPUTXBAR数据 |
| 242 | inxb_cpld_data_esync[5] | INPUTXBAR数据 |
| 241 | inxb_cpld_data_esync[4] | INPUTXBAR数据 |
| 240 | inxb_cpld_data_esync[3] | INPUTXBAR数据 |
| 239 | inxb_cpld_data_esync[2] | INPUTXBAR数据 |
| 238 | inxb_cpld_data_esync[1] | INPUTXBAR数据 |
| 237 | inxb_cpld_data_esync[0] | INPUTXBAR数据 |
| 236 | pfxb_cpld_data_esync[10] | PWMXBAR数据 |
| 235 | pfxb_cpld_data_esync[9] | PWMXBAR数据 |
| 234 | pfxb_cpld_data_esync[8] | PWMXBAR数据 |
| 233 | pfxb_cpld_data_esync[7] | PWMXBAR数据 |
| 232 | pfxb_cpld_data_esync[6] | PWMXBAR数据 |
| 231 | pfxb_cpld_data_esync[5] | PWMXBAR数据 |
| 230 | pfxb_cpld_data_esync[4] | PWMXBAR数据 |
| 229 | pfxb_cpld_data_esync[3] | PWMXBAR数据 |
| 228 | pfxb_cpld_data_esync[2] | PWMXBAR数据 |
| 227 | pfxb_cpld_data_esync[1] | PWMXBAR数据 |
| 226 | pfxb_cpld_data_esync[0] | PWMXBAR数据 |
| 225 | etxb_cpld_data_esync[9] | PWMXBAR数据 |
| 224 | etxb_cpld_data_esync[8] | PWMXBAR数据 |
| 223 | etxb_cpld_data_esync[7] | PWMXBAR数据 |
| 222 | etxb_cpld_data_esync[6] | PWMXBAR数据 |
| 221 | etxb_cpld_data_esync[5] | PWMXBAR数据 |
| 220 | etxb_cpld_data_esync[4] | PWMXBAR数据 |
| 219 | etxb_cpld_data_esync[3] | PWMXBAR数据 |
| 218 | etxb_cpld_data_esync[2] | PWMXBAR数据 |
| 217 | etxb_cpld_data_esync[1] | PWMXBAR数据 |
| 216 | etxb_cpld_data_esync[0] | PWMXBAR数据 |
| 215 | etim_cpld_sync_esync | ETIM PWM相位同步信号 |
| 214 | cmpc_cpld_evth_esync[10] | CMPC H事件 |
| 213 | cmpc_cpld_evth_esync[9] | CMPC H事件 |
| 212 | cmpc_cpld_evth_esync[8] | CMPC H事件 |
| 211 | cmpc_cpld_evth_esync[7] | CMPC H事件 |
| 210 | cmpc_cpld_evth_esync[6] | CMPC H事件 |
| 209 | cmpc_cpld_evth_esync[5] | CMPC H事件 |
| 208 | cmpc_cpld_evth_esync[4] | CMPC H事件 |
| 207 | cmpc_cpld_evth_esync[3] | CMPC H事件 |
| 206 | cmpc_cpld_evth_esync[2] | CMPC H事件 |
| 205 | cmpc_cpld_evth_esync[1] | CMPC H事件 |
| 204 | cmpc_cpld_evth_esync[0] | CMPC H事件 |
| 203 | cmpc_cpld_evtl_esync[10] | CMPC L事件 |
| 202 | cmpc_cpld_evtl_esync[9] | CMPC L事件 |
| 201 | cmpc_cpld_evtl_esync[8] | CMPC L事件 |
| 200 | cmpc_cpld_evtl_esync[7] | CMPC L事件 |
| 199 | cmpc_cpld_evtl_esync[6] | CMPC L事件 |
| 198 | cmpc_cpld_evtl_esync[5] | CMPC L事件 |
| 197 | cmpc_cpld_evtl_esync[4] | CMPC L事件 |
| 196 | cmpc_cpld_evtl_esync[3] | CMPC L事件 |
| 195 | cmpc_cpld_evtl_esync[2] | CMPC L事件 |
| 194 | cmpc_cpld_evtl_esync[1] | CMPC L事件 |
| 193 | cmpc_cpld_evtl_esync[0] | CMPC L事件 |
| 192 | adc0_cpld_evtl_esync[15] | ADC L事件 |
| 191 | adc0_cpld_evtl_esync[14] | ADC L事件 |
| 190 | adc0_cpld_evtl_esync[13] | ADC L事件 |
| 189 | adc0_cpld_evtl_esync[12] | ADC L事件 |
| 188 | adc0_cpld_evtl_esync[11] | ADC L事件 |
| 187 | adc0_cpld_evtl_esync[10] | ADC L事件 |
| 186 | adc0_cpld_evtl_esync[9] | ADC L事件 |
| 185 | adc0_cpld_evtl_esync[8] | ADC L事件 |
| 184 | adc0_cpld_evtl_esync[7] | ADC L事件 |
| 183 | adc0_cpld_evtl_esync[6] | ADC L事件 |
| 182 | adc0_cpld_evtl_esync[5] | ADC L事件 |
| 181 | adc0_cpld_evtl_esync[4] | ADC L事件 |
| 180 | adc0_cpld_evtl_esync[3] | ADC L事件 |
| 179 | adc0_cpld_evtl_esync[2] | ADC L事件 |
| 178 | adc0_cpld_evtl_esync[1] | ADC L事件 |
| 177 | adc0_cpld_evtl_esync[0] | ADC L事件 |
| 176 | adc0_cpld_evth_esync[15] | ADC H事件 |
| 175 | adc0_cpld_evth_esync[14] | ADC H事件 |
| 174 | adc0_cpld_evth_esync[13] | ADC H事件 |
| 173 | adc0_cpld_evth_esync[12] | ADC H事件 |
| 172 | adc0_cpld_evth_esync[11] | ADC H事件 |
| 171 | adc0_cpld_evth_esync[10] | ADC H事件 |
| 170 | adc0_cpld_evth_esync[9] | ADC H事件 |
| 169 | adc0_cpld_evth_esync[8] | ADC H事件 |
| 168 | adc0_cpld_evth_esync[7] | ADC H事件 |
| 167 | adc0_cpld_evth_esync[6] | ADC H事件 |
| 166 | adc0_cpld_evth_esync[5] | ADC H事件 |
| 165 | adc0_cpld_evth_esync[4] | ADC H事件 |
| 164 | adc0_cpld_evth_esync[3] | ADC H事件 |
| 163 | adc0_cpld_evth_esync[2] | ADC H事件 |
| 162 | adc0_cpld_evth_esync[1] | ADC H事件 |
| 161 | adc0_cpld_evth_esync[0] | ADC H事件 |
| 160 | adc1_cpld_evtl_esync[15] | ADC L事件 |
| 159 | adc1_cpld_evtl_esync[14] | ADC L事件 |
| 158 | adc1_cpld_evtl_esync[13] | ADC L事件 |
| 157 | adc1_cpld_evtl_esync[12] | ADC L事件 |
| 156 | adc1_cpld_evtl_esync[11] | ADC L事件 |
| 155 | adc1_cpld_evtl_esync[10] | ADC L事件 |
| 154 | adc1_cpld_evtl_esync[9] | ADC L事件 |
| 153 | adc1_cpld_evtl_esync[8] | ADC L事件 |
| 152 | adc1_cpld_evtl_esync[7] | ADC L事件 |
| 151 | adc1_cpld_evtl_esync[6] | ADC L事件 |
| 150 | adc1_cpld_evtl_esync[5] | ADC L事件 |
| 149 | adc1_cpld_evtl_esync[4] | ADC L事件 |
| 148 | adc1_cpld_evtl_esync[3] | ADC L事件 |
| 147 | adc1_cpld_evtl_esync[2] | ADC L事件 |
| 146 | adc1_cpld_evtl_esync[1] | ADC L事件 |
| 145 | adc1_cpld_evtl_esync[0] | ADC L事件 |
| 144 | adc1_cpld_evth_esync[15] | ADC H事件 |
| 143 | adc1_cpld_evth_esync[14] | ADC H事件 |
| 142 | adc1_cpld_evth_esync[13] | ADC H事件 |
| 141 | adc1_cpld_evth_esync[12] | ADC H事件 |
| 140 | adc1_cpld_evth_esync[11] | ADC H事件 |
| 139 | adc1_cpld_evth_esync[10] | ADC H事件 |
| 138 | adc1_cpld_evth_esync[9] | ADC H事件 |
| 137 | adc1_cpld_evth_esync[8] | ADC H事件 |
| 136 | adc1_cpld_evth_esync[7] | ADC H事件 |
| 135 | adc1_cpld_evth_esync[6] | ADC H事件 |
| 134 | adc1_cpld_evth_esync[5] | ADC H事件 |
| 133 | adc1_cpld_evth_esync[4] | ADC H事件 |
| 132 | adc1_cpld_evth_esync[3] | ADC H事件 |
| 131 | adc1_cpld_evth_esync[2] | ADC H事件 |
| 130 | adc1_cpld_evth_esync[1] | ADC H事件 |
| 129 | adc1_cpld_evth_esync[0] | ADC H事件 |
| 128 | cpu0_lockup_esync | CPU挂死 |
| 127 | cpu1_lockup_esync | CPU挂死 |
| 126 | bus_timeout_esync | 总线超时 |
| 125 | temp_warn_esync | 过温告警 |
| 124 | power_err_esync | 过流 |
| 123 | por_uv_warn_esync | 欠压 |
| 122 | por_ov_warn_esync | 过压 |
| 121 | cfg_efpga1_esync[31] | eFPGA保留配置接口，与总线交互 |
| 120 | cfg_efpga1_esync[30] | eFPGA保留配置接口，与总线交互 |
| 119 | cfg_efpga1_esync[29] | eFPGA保留配置接口，与总线交互 |
| 118 | cfg_efpga1_esync[28] | eFPGA保留配置接口，与总线交互 |
| 117 | cfg_efpga1_esync[27] | eFPGA保留配置接口，与总线交互 |
| 116 | cfg_efpga1_esync[26] | eFPGA保留配置接口，与总线交互 |
| 115 | cfg_efpga1_esync[25] | eFPGA保留配置接口，与总线交互 |
| 114 | cfg_efpga1_esync[24] | eFPGA保留配置接口，与总线交互 |
| 113 | cfg_efpga1_esync[23] | eFPGA保留配置接口，与总线交互 |
| 112 | cfg_efpga1_esync[22] | eFPGA保留配置接口，与总线交互 |
| 111 | cfg_efpga1_esync[21] | eFPGA保留配置接口，与总线交互 |
| 110 | cfg_efpga1_esync[20] | eFPGA保留配置接口，与总线交互 |
| 109 | cfg_efpga1_esync[19] | eFPGA保留配置接口，与总线交互 |
| 108 | cfg_efpga1_esync[18] | eFPGA保留配置接口，与总线交互 |
| 107 | cfg_efpga1_esync[17] | eFPGA保留配置接口，与总线交互 |
| 106 | cfg_efpga1_esync[16] | eFPGA保留配置接口，与总线交互 |
| 105 | cfg_efpga1_esync[15] | eFPGA保留配置接口，与总线交互 |
| 104 | cfg_efpga1_esync[14] | eFPGA保留配置接口，与总线交互 |
| 103 | cfg_efpga1_esync[13] | eFPGA保留配置接口，与总线交互 |
| 102 | cfg_efpga1_esync[12] | eFPGA保留配置接口，与总线交互 |
| 101 | cfg_efpga1_esync[11] | eFPGA保留配置接口，与总线交互 |
| 100 | cfg_efpga1_esync[10] | eFPGA保留配置接口，与总线交互 |
| 99 | cfg_efpga1_esync[9] | eFPGA保留配置接口，与总线交互 |
| 98 | cfg_efpga1_esync[8] | eFPGA保留配置接口，与总线交互 |
| 97 | cfg_efpga1_esync[7] | eFPGA保留配置接口，与总线交互 |
| 96 | cfg_efpga1_esync[6] | eFPGA保留配置接口，与总线交互 |
| 95 | cfg_efpga1_esync[5] | eFPGA保留配置接口，与总线交互 |
| 94 | cfg_efpga1_esync[4] | eFPGA保留配置接口，与总线交互 |
| 93 | cfg_efpga1_esync[3] | eFPGA保留配置接口，与总线交互 |
| 92 | cfg_efpga1_esync[2] | eFPGA保留配置接口，与总线交互 |
| 91 | cfg_efpga1_esync[1] | eFPGA保留配置接口，与总线交互 |
| 90 | cfg_efpga1_esync[0] | eFPGA保留配置接口，与总线交互 |
| 89 | cfg_efpga0_esync[31] | eFPGA保留配置接口，与总线交互 |
| 88 | cfg_efpga0_esync[30] | eFPGA保留配置接口，与总线交互 |
| 87 | cfg_efpga0_esync[29] | eFPGA保留配置接口，与总线交互 |
| 86 | cfg_efpga0_esync[28] | eFPGA保留配置接口，与总线交互 |
| 85 | cfg_efpga0_esync[27] | eFPGA保留配置接口，与总线交互 |
| 84 | cfg_efpga0_esync[26] | eFPGA保留配置接口，与总线交互 |
| 83 | cfg_efpga0_esync[25] | eFPGA保留配置接口，与总线交互 |
| 82 | cfg_efpga0_esync[24] | eFPGA保留配置接口，与总线交互 |
| 81 | cfg_efpga0_esync[23] | eFPGA保留配置接口，与总线交互 |
| 80 | cfg_efpga0_esync[22] | eFPGA保留配置接口，与总线交互 |
| 79 | cfg_efpga0_esync[21] | eFPGA保留配置接口，与总线交互 |
| 78 | cfg_efpga0_esync[20] | eFPGA保留配置接口，与总线交互 |
| 77 | cfg_efpga0_esync[19] | eFPGA保留配置接口，与总线交互 |
| 76 | cfg_efpga0_esync[18] | eFPGA保留配置接口，与总线交互 |
| 75 | cfg_efpga0_esync[17] | eFPGA保留配置接口，与总线交互 |
| 74 | cfg_efpga0_esync[16] | eFPGA保留配置接口，与总线交互 |
| 73 | cfg_efpga0_esync[15] | eFPGA保留配置接口，与总线交互 |
| 72 | cfg_efpga0_esync[14] | eFPGA保留配置接口，与总线交互 |
| 71 | cfg_efpga0_esync[13] | eFPGA保留配置接口，与总线交互 |
| 70 | cfg_efpga0_esync[12] | eFPGA保留配置接口，与总线交互 |
| 69 | cfg_efpga0_esync[11] | eFPGA保留配置接口，与总线交互 |
| 68 | cfg_efpga0_esync[10] | eFPGA保留配置接口，与总线交互 |
| 67 | cfg_efpga0_esync[9] | eFPGA保留配置接口，与总线交互 |
| 66 | cfg_efpga0_esync[8] | eFPGA保留配置接口，与总线交互 |
| 65 | cfg_efpga0_esync[7] | eFPGA保留配置接口，与总线交互 |
| 64 | cfg_efpga0_esync[6] | eFPGA保留配置接口，与总线交互 |
| 63 | cfg_efpga0_esync[5] | eFPGA保留配置接口，与总线交互 |
| 62 | cfg_efpga0_esync[4] | eFPGA保留配置接口，与总线交互 |
| 61 | cfg_efpga0_esync[3] | eFPGA保留配置接口，与总线交互 |
| 60 | cfg_efpga0_esync[2] | eFPGA保留配置接口，与总线交互 |
| 59 | cfg_efpga0_esync[1] | eFPGA保留配置接口，与总线交互 |
| 58 | cfg_efpga0_esync[0] | eFPGA保留配置接口，与总线交互 |
| 57 | etim_cpld_pwm_esync[9] | ETIM PWM |
| 56 | etim_cpld_pwm_esync[8] | ETIM PWM |
| 55 | etim_cpld_pwm_esync[7] | ETIM PWM |
| 54 | etim_cpld_pwm_esync[6] | ETIM PWM |
| 53 | etim_cpld_pwm_esync[5] | ETIM PWM |
| 52 | etim_cpld_pwm_esync[4] | ETIM PWM |
| 51 | etim_cpld_pwm_esync[3] | ETIM PWM |
| 50 | etim_cpld_pwm_esync[2] | ETIM PWM |
| 49 | etim_cpld_pwm_esync[1] | ETIM PWM |
| 48 | etim_cpld_pwm_esync[0] | ETIM PWM |
| 47 | srpwm_cpld_pwmb_oen_esync[11] | SRPWM PWM_OEN |
| 46 | srpwm_cpld_pwma_oen_esync[11] | SRPWM PWM_OEN |
| 45 | srpwm_cpld_pwm_b_esync[11] | SRPWM PWM |
| 44 | srpwm_cpld_pwm_a_esync[11] | SRPWM PWM |
| 43 | srpwm_cpld_pwmb_oen_esync[10] | SRPWM PWM_OEN |
| 42 | srpwm_cpld_pwma_oen_esync[10] | SRPWM PWM_OEN |
| 41 | srpwm_cpld_pwm_b_esync[10] | SRPWM PWM |
| 40 | srpwm_cpld_pwm_a_esync[10] | SRPWM PWM |
| 39 | srpwm_cpld_pwmb_oen_esync[9] | SRPWM PWM_OEN |
| 38 | srpwm_cpld_pwma_oen_esync[9] | SRPWM PWM_OEN |
| 37 | srpwm_cpld_pwm_b_esync[9] | SRPWM PWM |
| 36 | srpwm_cpld_pwm_a_esync[9] | SRPWM PWM |
| 35 | srpwm_cpld_pwmb_oen_esync[8] | SRPWM PWM_OEN |
| 34 | srpwm_cpld_pwma_oen_esync[8] | SRPWM PWM_OEN |
| 33 | srpwm_cpld_pwm_b_esync[8] | SRPWM PWM |
| 32 | srpwm_cpld_pwm_a_esync[8] | SRPWM PWM |
| 31 | srpwm_cpld_pwmb_oen_esync[7] | SRPWM PWM_OEN |
| 30 | srpwm_cpld_pwma_oen_esync[7] | SRPWM PWM_OEN |
| 29 | srpwm_cpld_pwm_b_esync[7] | SRPWM PWM |
| 28 | srpwm_cpld_pwm_a_esync[7] | SRPWM PWM |
| 27 | srpwm_cpld_pwmb_oen_esync[6] | SRPWM PWM_OEN |
| 26 | srpwm_cpld_pwma_oen_esync[6] | SRPWM PWM_OEN |
| 25 | srpwm_cpld_pwm_b_esync[6] | SRPWM PWM |
| 24 | srpwm_cpld_pwm_a_esync[6] | SRPWM PWM |
| 23 | srpwm_cpld_pwmb_oen_esync[5] | SRPWM PWM_OEN |
| 22 | srpwm_cpld_pwma_oen_esync[5] | SRPWM PWM_OEN |
| 21 | srpwm_cpld_pwm_b_esync[5] | SRPWM PWM |
| 20 | srpwm_cpld_pwm_a_esync[5] | SRPWM PWM |
| 19 | srpwm_cpld_pwmb_oen_esync[4] | SRPWM PWM_OEN |
| 18 | srpwm_cpld_pwma_oen_esync[4] | SRPWM PWM_OEN |
| 17 | srpwm_cpld_pwm_b_esync[4] | SRPWM PWM |
| 16 | srpwm_cpld_pwm_a_esync[4] | SRPWM PWM |
| 15 | srpwm_cpld_pwmb_oen_esync[3] | SRPWM PWM_OEN |
| 14 | srpwm_cpld_pwma_oen_esync[3] | SRPWM PWM_OEN |
| 13 | srpwm_cpld_pwm_b_esync[3] | SRPWM PWM |
| 12 | srpwm_cpld_pwm_a_esync[3] | SRPWM PWM |
| 11 | srpwm_cpld_pwmb_oen_esync[2] | SRPWM PWM_OEN |
| 10 | srpwm_cpld_pwma_oen_esync[2] | SRPWM PWM_OEN |
| 9 | srpwm_cpld_pwm_b_esync[2] | SRPWM PWM |
| 8 | srpwm_cpld_pwm_a_esync[2] | SRPWM PWM |
| 7 | srpwm_cpld_pwmb_oen_esync[1] | SRPWM PWM_OEN |
| 6 | srpwm_cpld_pwma_oen_esync[1] | SRPWM PWM_OEN |
| 5 | srpwm_cpld_pwm_b_esync[1] | SRPWM PWM |
| 4 | srpwm_cpld_pwm_a_esync[1] | SRPWM PWM |
| 3 | srpwm_cpld_pwmb_oen_esync[0] | SRPWM PWM_OEN |
| 2 | srpwm_cpld_pwma_oen_esync[0] | SRPWM PWM_OEN |
| 1 | srpwm_cpld_pwm_b_esync[0] | SRPWM PWM |
| 0 | srpwm_cpld_pwm_a_esync[0] | SRPWM PWM |

### 10.3 int_fpga_out

原表合并属性：inout = output，width = 200。

| NO. | connect signal | 说明 |
|---:|---|---|
| 199 | ppi_data_out[11] | PPI |
| 198 | ppi_data_out[10] | PPI |
| 197 | ppi_data_out[9] | PPI |
| 196 | ppi_data_out[8] | PPI |
| 195 | ppi_data_out[7] | PPI |
| 194 | ppi_data_out[6] | PPI |
| 193 | ppi_data_out[5] | PPI |
| 192 | ppi_data_out[4] | PPI |
| 191 | ppi_data_out[3] | PPI |
| 190 | ppi_data_out[2] | PPI |
| 189 | ppi_data_out[1] | PPI |
| 188 | ppi_data_out[0] | PPI |
| 187 | c2s_rpt[14] | eFPGA到SYSC的保留上报 |
| 186 | c2s_rpt[13] | eFPGA到SYSC的保留上报 |
| 185 | c2s_rpt[12] | eFPGA到SYSC的保留上报 |
| 184 | c2s_rpt[11] | eFPGA到SYSC的保留上报 |
| 183 | c2s_rpt[10] | eFPGA到SYSC的保留上报 |
| 182 | c2s_rpt[9] | eFPGA到SYSC的保留上报 |
| 181 | c2s_rpt[8] | eFPGA到SYSC的保留上报 |
| 180 | c2s_rpt[7] | eFPGA到SYSC的保留上报 |
| 179 | c2s_rpt[6] | eFPGA到SYSC的保留上报 |
| 178 | c2s_rpt[5] | eFPGA到SYSC的保留上报 |
| 177 | c2s_rpt[4] | eFPGA到SYSC的保留上报 |
| 176 | c2s_rpt[3] | eFPGA到SYSC的保留上报 |
| 175 | c2s_rpt[2] | eFPGA到SYSC的保留上报 |
| 174 | c2s_rpt[1] | eFPGA到SYSC的保留上报 |
| 173 | c2s_rpt[0] | eFPGA到SYSC的保留上报 |
| 172 | efpga_dma_req0 | 用户自定义DMA触发源 |
| 171 | efpga_dma_req1 | 用户自定义DMA触发源 |
| 170 | efpga_c2s_rst_n | 用户自定义复位源 |
| 169 | efpga0_rpt[31] | eFPGA保留上报接口，与总线交互 |
| 168 | efpga0_rpt[30] | eFPGA保留上报接口，与总线交互 |
| 167 | efpga0_rpt[29] | eFPGA保留上报接口，与总线交互 |
| 166 | efpga0_rpt[28] | eFPGA保留上报接口，与总线交互 |
| 165 | efpga0_rpt[27] | eFPGA保留上报接口，与总线交互 |
| 164 | efpga0_rpt[26] | eFPGA保留上报接口，与总线交互 |
| 163 | efpga0_rpt[25] | eFPGA保留上报接口，与总线交互 |
| 162 | efpga0_rpt[24] | eFPGA保留上报接口，与总线交互 |
| 161 | efpga0_rpt[23] | eFPGA保留上报接口，与总线交互 |
| 160 | efpga0_rpt[22] | eFPGA保留上报接口，与总线交互 |
| 159 | efpga0_rpt[21] | eFPGA保留上报接口，与总线交互 |
| 158 | efpga0_rpt[20] | eFPGA保留上报接口，与总线交互 |
| 157 | efpga0_rpt[19] | eFPGA保留上报接口，与总线交互 |
| 156 | efpga0_rpt[18] | eFPGA保留上报接口，与总线交互 |
| 155 | efpga0_rpt[17] | eFPGA保留上报接口，与总线交互 |
| 154 | efpga0_rpt[16] | eFPGA保留上报接口，与总线交互 |
| 153 | efpga0_rpt[15] | eFPGA保留上报接口，与总线交互 |
| 152 | efpga0_rpt[14] | eFPGA保留上报接口，与总线交互 |
| 151 | efpga0_rpt[13] | eFPGA保留上报接口，与总线交互 |
| 150 | efpga0_rpt[12] | eFPGA保留上报接口，与总线交互 |
| 149 | efpga0_rpt[11] | eFPGA保留上报接口，与总线交互 |
| 148 | efpga0_rpt[10] | eFPGA保留上报接口，与总线交互 |
| 147 | efpga0_rpt[9] | eFPGA保留上报接口，与总线交互 |
| 146 | efpga0_rpt[8] | eFPGA保留上报接口，与总线交互 |
| 145 | efpga0_rpt[7] | eFPGA保留上报接口，与总线交互 |
| 144 | efpga0_rpt[6] | eFPGA保留上报接口，与总线交互 |
| 143 | efpga0_rpt[5] | eFPGA保留上报接口，与总线交互 |
| 142 | efpga0_rpt[4] | eFPGA保留上报接口，与总线交互 |
| 141 | efpga0_rpt[3] | eFPGA保留上报接口，与总线交互 |
| 140 | efpga0_rpt[2] | eFPGA保留上报接口，与总线交互 |
| 139 | efpga0_rpt[1] | eFPGA保留上报接口，与总线交互 |
| 138 | efpga0_rpt[0] | eFPGA保留上报接口，与总线交互 |
| 137 | efpga1_rpt[31] | eFPGA保留上报接口，与总线交互 |
| 136 | efpga1_rpt[30] | eFPGA保留上报接口，与总线交互 |
| 135 | efpga1_rpt[29] | eFPGA保留上报接口，与总线交互 |
| 134 | efpga1_rpt[28] | eFPGA保留上报接口，与总线交互 |
| 133 | efpga1_rpt[27] | eFPGA保留上报接口，与总线交互 |
| 132 | efpga1_rpt[26] | eFPGA保留上报接口，与总线交互 |
| 131 | efpga1_rpt[25] | eFPGA保留上报接口，与总线交互 |
| 130 | efpga1_rpt[24] | eFPGA保留上报接口，与总线交互 |
| 129 | efpga1_rpt[23] | eFPGA保留上报接口，与总线交互 |
| 128 | efpga1_rpt[22] | eFPGA保留上报接口，与总线交互 |
| 127 | efpga1_rpt[21] | eFPGA保留上报接口，与总线交互 |
| 126 | efpga1_rpt[20] | eFPGA保留上报接口，与总线交互 |
| 125 | efpga1_rpt[19] | eFPGA保留上报接口，与总线交互 |
| 124 | efpga1_rpt[18] | eFPGA保留上报接口，与总线交互 |
| 123 | efpga1_rpt[17] | eFPGA保留上报接口，与总线交互 |
| 122 | efpga1_rpt[16] | eFPGA保留上报接口，与总线交互 |
| 121 | efpga1_rpt[15] | eFPGA保留上报接口，与总线交互 |
| 120 | efpga1_rpt[14] | eFPGA保留上报接口，与总线交互 |
| 119 | efpga1_rpt[13] | eFPGA保留上报接口，与总线交互 |
| 118 | efpga1_rpt[12] | eFPGA保留上报接口，与总线交互 |
| 117 | efpga1_rpt[11] | eFPGA保留上报接口，与总线交互 |
| 116 | efpga1_rpt[10] | eFPGA保留上报接口，与总线交互 |
| 115 | efpga1_rpt[9] | eFPGA保留上报接口，与总线交互 |
| 114 | efpga1_rpt[8] | eFPGA保留上报接口，与总线交互 |
| 113 | efpga1_rpt[7] | eFPGA保留上报接口，与总线交互 |
| 112 | efpga1_rpt[6] | eFPGA保留上报接口，与总线交互 |
| 111 | efpga1_rpt[5] | eFPGA保留上报接口，与总线交互 |
| 110 | efpga1_rpt[4] | eFPGA保留上报接口，与总线交互 |
| 109 | efpga1_rpt[3] | eFPGA保留上报接口，与总线交互 |
| 108 | efpga1_rpt[2] | eFPGA保留上报接口，与总线交互 |
| 107 | efpga1_rpt[1] | eFPGA保留上报接口，与总线交互 |
| 106 | efpga1_rpt[0] | eFPGA保留上报接口，与总线交互 |
| 105 | cpld_opxb_data[9] | eFPGA 输出到OUTPUTXBAR |
| 104 | cpld_opxb_data[8] | eFPGA 输出到OUTPUTXBAR |
| 103 | cpld_opxb_data[7] | eFPGA 输出到OUTPUTXBAR |
| 102 | cpld_opxb_data[6] | eFPGA 输出到OUTPUTXBAR |
| 101 | cpld_opxb_data[5] | eFPGA 输出到OUTPUTXBAR |
| 100 | cpld_opxb_data[4] | eFPGA 输出到OUTPUTXBAR |
| 99 | cpld_opxb_data[3] | eFPGA 输出到OUTPUTXBAR |
| 98 | cpld_opxb_data[2] | eFPGA 输出到OUTPUTXBAR |
| 97 | cpld_opxb_data[1] | eFPGA 输出到OUTPUTXBAR |
| 96 | cpld_opxb_data[0] | eFPGA 输出到OUTPUTXBAR |
| 95 | cpld_pad_oen[35] | eFPGA 输出到PAD_OEN |
| 94 | cpld_pad_oen[34] | eFPGA 输出到PAD_OEN |
| 93 | cpld_pad_oen[33] | eFPGA 输出到PAD_OEN |
| 92 | cpld_pad_oen[32] | eFPGA 输出到PAD_OEN |
| 91 | cpld_pad_oen[31] | eFPGA 输出到PAD_OEN |
| 90 | cpld_pad_oen[30] | eFPGA 输出到PAD_OEN |
| 89 | cpld_pad_oen[29] | eFPGA 输出到PAD_OEN |
| 88 | cpld_pad_oen[28] | eFPGA 输出到PAD_OEN |
| 87 | cpld_pad_oen[27] | eFPGA 输出到PAD_OEN |
| 86 | cpld_pad_oen[26] | eFPGA 输出到PAD_OEN |
| 85 | cpld_pad_oen[25] | eFPGA 输出到PAD_OEN |
| 84 | cpld_pad_oen[24] | eFPGA 输出到PAD_OEN |
| 83 | cpld_pad_oen[23] | eFPGA 输出到PAD_OEN |
| 82 | cpld_pad_oen[22] | eFPGA 输出到PAD_OEN |
| 81 | cpld_pad_oen[21] | eFPGA 输出到PAD_OEN |
| 80 | cpld_pad_oen[20] | eFPGA 输出到PAD_OEN |
| 79 | cpld_pad_oen[19] | eFPGA 输出到PAD_OEN |
| 78 | cpld_pad_oen[18] | eFPGA 输出到PAD_OEN |
| 77 | cpld_pad_oen[17] | eFPGA 输出到PAD_OEN |
| 76 | cpld_pad_oen[16] | eFPGA 输出到PAD_OEN |
| 75 | cpld_pad_oen[15] | eFPGA 输出到PAD_OEN |
| 74 | cpld_pad_oen[14] | eFPGA 输出到PAD_OEN |
| 73 | cpld_pad_oen[13] | eFPGA 输出到PAD_OEN |
| 72 | cpld_pad_oen[12] | eFPGA 输出到PAD_OEN |
| 71 | cpld_pad_oen[11] | eFPGA 输出到PAD_OEN |
| 70 | cpld_pad_oen[10] | eFPGA 输出到PAD_OEN |
| 69 | cpld_pad_oen[9] | eFPGA 输出到PAD_OEN |
| 68 | cpld_pad_oen[8] | eFPGA 输出到PAD_OEN |
| 67 | cpld_pad_oen[7] | eFPGA 输出到PAD_OEN |
| 66 | cpld_pad_oen[6] | eFPGA 输出到PAD_OEN |
| 65 | cpld_pad_oen[5] | eFPGA 输出到PAD_OEN |
| 64 | cpld_pad_oen[4] | eFPGA 输出到PAD_OEN |
| 63 | cpld_pad_oen[3] | eFPGA 输出到PAD_OEN |
| 62 | cpld_pad_oen[2] | eFPGA 输出到PAD_OEN |
| 61 | cpld_pad_oen[1] | eFPGA 输出到PAD_OEN |
| 60 | cpld_pad_oen[0] | eFPGA 输出到PAD_OEN |
| 59 | cpld_pad_out[35] | eFPGA 输出到PAD |
| 58 | cpld_pad_out[34] | eFPGA 输出到PAD |
| 57 | cpld_pad_out[33] | eFPGA 输出到PAD |
| 56 | cpld_pad_out[32] | eFPGA 输出到PAD |
| 55 | cpld_pad_out[31] | eFPGA 输出到PAD |
| 54 | cpld_pad_out[30] | eFPGA 输出到PAD |
| 53 | cpld_pad_out[29] | eFPGA 输出到PAD |
| 52 | cpld_pad_out[28] | eFPGA 输出到PAD |
| 51 | cpld_pad_out[27] | eFPGA 输出到PAD |
| 50 | cpld_pad_out[26] | eFPGA 输出到PAD |
| 49 | cpld_pad_out[25] | eFPGA 输出到PAD |
| 48 | cpld_pad_out[24] | eFPGA 输出到PAD |
| 47 | cpld_pad_out[23] | eFPGA 输出到PAD |
| 46 | cpld_pad_out[22] | eFPGA 输出到PAD |
| 45 | cpld_pad_out[21] | eFPGA 输出到PAD |
| 44 | cpld_pad_out[20] | eFPGA 输出到PAD |
| 43 | cpld_pad_out[19] | eFPGA 输出到PAD |
| 42 | cpld_pad_out[18] | eFPGA 输出到PAD |
| 41 | cpld_pad_out[17] | eFPGA 输出到PAD |
| 40 | cpld_pad_out[16] | eFPGA 输出到PAD |
| 39 | cpld_pad_out[15] | eFPGA 输出到PAD |
| 38 | cpld_pad_out[14] | eFPGA 输出到PAD |
| 37 | cpld_pad_out[13] | eFPGA 输出到PAD |
| 36 | cpld_pad_out[12] | eFPGA 输出到PAD |
| 35 | cpld_pad_out[11] | eFPGA 输出到PAD |
| 34 | cpld_pad_out[10] | eFPGA 输出到PAD |
| 33 | cpld_pad_out[9] | eFPGA 输出到PAD |
| 32 | cpld_pad_out[8] | eFPGA 输出到PAD |
| 31 | cpld_pad_out[7] | eFPGA 输出到PAD |
| 30 | cpld_pad_out[6] | eFPGA 输出到PAD |
| 29 | cpld_pad_out[5] | eFPGA 输出到PAD |
| 28 | cpld_pad_out[4] | eFPGA 输出到PAD |
| 27 | cpld_pad_out[3] | eFPGA 输出到PAD |
| 26 | cpld_pad_out[2] | eFPGA 输出到PAD |
| 25 | cpld_pad_out[1] | eFPGA 输出到PAD |
| 24 | cpld_pad_out[0] | eFPGA 输出到PAD |
| 23 | cpld_srpwm_fault[23] | eFPGA 输出到SRPWM用于封波 |
| 22 | cpld_srpwm_fault[22] | eFPGA 输出到SRPWM用于封波 |
| 21 | cpld_srpwm_fault[21] | eFPGA 输出到SRPWM用于封波 |
| 20 | cpld_srpwm_fault[20] | eFPGA 输出到SRPWM用于封波 |
| 19 | cpld_srpwm_fault[19] | eFPGA 输出到SRPWM用于封波 |
| 18 | cpld_srpwm_fault[18] | eFPGA 输出到SRPWM用于封波 |
| 17 | cpld_srpwm_fault[17] | eFPGA 输出到SRPWM用于封波 |
| 16 | cpld_srpwm_fault[16] | eFPGA 输出到SRPWM用于封波 |
| 15 | cpld_srpwm_fault[15] | eFPGA 输出到SRPWM用于封波 |
| 14 | cpld_srpwm_fault[14] | eFPGA 输出到SRPWM用于封波 |
| 13 | cpld_srpwm_fault[13] | eFPGA 输出到SRPWM用于封波 |
| 12 | cpld_srpwm_fault[12] | eFPGA 输出到SRPWM用于封波 |
| 11 | cpld_srpwm_fault[11] | eFPGA 输出到SRPWM用于封波 |
| 10 | cpld_srpwm_fault[10] | eFPGA 输出到SRPWM用于封波 |
| 9 | cpld_srpwm_fault[9] | eFPGA 输出到SRPWM用于封波 |
| 8 | cpld_srpwm_fault[8] | eFPGA 输出到SRPWM用于封波 |
| 7 | cpld_srpwm_fault[7] | eFPGA 输出到SRPWM用于封波 |
| 6 | cpld_srpwm_fault[6] | eFPGA 输出到SRPWM用于封波 |
| 5 | cpld_srpwm_fault[5] | eFPGA 输出到SRPWM用于封波 |
| 4 | cpld_srpwm_fault[4] | eFPGA 输出到SRPWM用于封波 |
| 3 | cpld_srpwm_fault[3] | eFPGA 输出到SRPWM用于封波 |
| 2 | cpld_srpwm_fault[2] | eFPGA 输出到SRPWM用于封波 |
| 1 | cpld_srpwm_fault[1] | eFPGA 输出到SRPWM用于封波 |
| 0 | cpld_srpwm_fault[0] | eFPGA 输出到SRPWM用于封波 |
