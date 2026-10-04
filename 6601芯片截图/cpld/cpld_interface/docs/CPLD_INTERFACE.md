# CPLD_INTERFACE

> 来源：ET6601 原始截图精准还原。
> 本文件恢复原始文档边界：CPLD_INTERFACE 是一份文档；以下接口内容不再作为独立最终文档。
> 已按对应原图逐张精校；连续表格按原始行号恢复。原图中的特殊拼写、留空和设计表述均按图保留，不做推测性修正。


---

## INTERFACE_CPLD

> 原图：
> - `../../interface_cpld/images/GameViewer_atyH2wpPCk.png`
> - `../../interface_cpld/images/GameViewer_BtApOlYWLK.png`
> - `../../interface_cpld/images/GameViewer_hN7LUohFXY.png`

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
| 复位 | TOP_CRG | CPLD | cpld_lgc_rst_n | input |  | 1 |  | 在SOC系统SYSC模块的POR域配置，仅复位Fabric逻辑，不影响时钟及CPLD配置，是否关联SOC系统复位可配置，默认不关联，复位配置写保护 |
| 复位 | TOP_CRG | CPLD | cpld_user_rst_n | input |  | 1 |  | 用户软复位输入，用户逻辑使用，连接到eFPGA的io_resetn，由SOC系统寄存器配置或IO输入（TBD） |
| 复位 | CRG | CPLD | soc_hard_rst_n | input | type1 | 1 |  | SOC硬复位 |
| 复位 | CRG | CPLD | soc_wdg0_rst_n | input | type1 | 1 |  | SOC看门狗0复位 |
| 复位 | CRG | CPLD | soc_wdg1_rst_n | input | type1 | 1 |  | SOC看门狗1复位 |
| 复位 | CRG | CPLD | soc_soft_rst_n | input | type1 | 1 |  | SOC软复位 |
| 复位 | eFPGA | SYSC/XBAR/CRG | c2s_rst_n | output |  | 2 |  | eFPGA用户逻辑到SOC系统的C2S_RSTN复位输出 |
| 中断 | eFPGA | SOC | cpld_usr_intr | output |  | 1 | 异步处理 | 中断；b0:用户中断0；b1:用户中断1；b2:PPI流水线； |
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
| 总线 | CPLD | SOC | cpld_ahb1_hrdata | output |  | 32 | 总线桥 | AHB1 |
| 总线 | CPLD | SOC | cpld_ahb1_hreadyout | output |  | 1 | 总线桥 | AHB1 |
| 总线 | CPLD | SOC | cpld_ahb1_hresp | output |  | 1 | 总线桥 | AHB1 |
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
| 互联 | CMPC | CPLD | cmpc_cpld_evtl | input | type2 | 10 | SYNC | CMPC高电平比较器事件，电平或脉冲信号，高有效 |
| 互联 | ADC | CPLD | adc0_cpld_evth | input | type2 | 16 | SYNC | ADC0 高事件，电平或脉冲信号，高有效 |
| 互联 | ADC | CPLD | adc0_cpld_evtl | input | type2 | 16 | SYNC | ADC0 低事件，电平或脉冲信号，高有效 |
| 互联 | ADC | CPLD | adc1_cpld_evth | input | type2 | 16 | SYNC | ADC1 高事件，电平或脉冲信号，高有效 |
| 互联 | ADC | CPLD | adc1_cpld_evtl | input | type2 | 16 | SYNC | ADC1 低事件，电平或脉冲信号，高有效 |
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
| 互联 | SYSC | CPLD | s2c_cfg | input |  | 14 |  | 保留输入 |
| 互联 | eFPGA | SYSC | c2s_rpt | output |  | 16 |  | 保留输出 |
| 互联 | SYSC | CPLD | sysc_cpld_testpin0_sel | input |  | 8 |  | testpin选择 |
| 互联 | SYSC | CPLD | sysc_cpld_testpin1_sel | input |  | 8 |  | testpin选择 |
| 互联 | SYSC | CPLD | sysc_cpld_testpin2_sel | input |  | 8 |  | testpin选择 |
| 互联 | SYSC | CPLD | sysc_cpld_testpin3_sel | input |  | 8 |  | testpin选择 |
| 互联 | CPLD | SYSC | cpld_sysc_testpin | output |  | 4 |  | testpin |

---

## INTERFACE_CPLD_CFG

> 原图（按表格行号连续顺序）：
> - `../../interface_cpld_cfg/images/GameViewer_DeXJCeTp8c.png`
> - `../../interface_cpld_cfg/images/GameViewer_DjmYAqFskT.png`
> - `../../interface_cpld_cfg/images/GameViewer_1AL3gcTZwO.png`
> - `../../interface_cpld_cfg/images/GameViewer_zJTLoUFpvE.png`
> - `../../interface_cpld_cfg/images/GameViewer_XN1mwSbZGj.png`
> - `../../interface_cpld_cfg/images/GameViewer_sB1DKm1Cn1.png`

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

---

## INTERFACE_CPLD_CRG

> 原图：`../../interface_cpld_crg/images/GameViewer_UipiANJp8o.png`

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

> 原图备注：`INSERT SIGNAL BEFORE THIS ROW`

---

## INTERFACE_CPLD_TCU

> 原图：`../../interface_cpld_tcu/images/GameViewer_W0SBPxoKtt.png`

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

---

## INTERFACE_DMA

> 原图：`../../interface_dma/images/GameViewer_VIiEW5kIvW.png`

| signal | inout | width | connect_sig |
|---|---|---:|---|
| efpga_dma_req0 | input | 1 | efpga_dma_req0 |
| efpga_dma_req1 | input | 1 | efpga_dma_req1 |
| cpld_dma_req | output | 2 | cpld_usr_dma |

---

## INTERFACE_EFPGA

> 原图（按原表行号连续顺序）：
> - `../../interface_efpga/images/GameViewer_8iXOmcDGE1.png`（原表行 1–38）
> - `../../interface_efpga/images/GameViewer_cU12ydgZ8V.png`（原表行 39–74）
> - `../../interface_efpga/images/GameViewer_Vhor9olOSG.png`（原表行 75–110）
> - `../../interface_efpga/images/GameViewer_J6lAwKnIhm.png`（原表行 111–146）
> - `../../interface_efpga/images/GameViewer_Nbjags3WBm.png`（原表行 147–182）
> - `../../interface_efpga/images/GameViewer_xPU5bUtZ6p.png`（原表行 183–218）
> - `../../interface_efpga/images/GameViewer_S8SQhpMWC2.png`（原表行 219–254）
> - `../../interface_efpga/images/GameViewer_grCDK0KTgW.png`（原表行 255–290）
> - `../../interface_efpga/images/GameViewer_uxeRXbUM3q.png`（原表行 291–326）
> - `../../interface_efpga/images/GameViewer_P0NFLfV564.png`（原表行 327–362）
> - `../../interface_efpga/images/GameViewer_3BoqyOeJgh.png`（原表行 363–398）
> - `../../interface_efpga/images/GameViewer_I7FEkY4HxN.png`（原表行 399–434）
> - `../../interface_efpga/images/GameViewer_gvjimz0mF4.png`（原表行 435–470）
> - `../../interface_efpga/images/GameViewer_2zddazPQIp.png`（原表行 471–506）
> - `../../interface_efpga/images/GameViewer_bCW62ClcKC.png`（原表行 507–542）
> - `../../interface_efpga/images/GameViewer_qhGTBAxdTy.png`（原表行 543–554）

| eFPGA interface | inout | width | NO. | connect signal | 说明 |
|---|---|---:|---:|---|---|
| sys_clk | input | 1 |  | efpga_sys_clk | 200M时钟，与SOC系统时钟同步 |
| sys_resetn | input | 1 |  | efpga_sys_resetn | CPLD HARD_RST&S2C_ |
| wdt_sclk | input | 1 |  |  |  |
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
| int_fpga_in | input | 320 | 319 | s2c_cfg_esync[7] | SYSC到eFPGA的保留配置 |
| int_fpga_in | input | 320 | 318 | s2c_cfg_esync[6] | SYSC到eFPGA的保留配置 |
| int_fpga_in | input | 320 | 317 | s2c_cfg_esync[5] | SYSC到eFPGA的保留配置 |
| int_fpga_in | input | 320 | 316 | s2c_cfg_esync[4] | SYSC到eFPGA的保留配置 |
| int_fpga_in | input | 320 | 315 | s2c_cfg_esync[3] | SYSC到eFPGA的保留配置 |
| int_fpga_in | input | 320 | 314 | s2c_cfg_esync[2] | SYSC到eFPGA的保留配置 |
| int_fpga_in | input | 320 | 313 | s2c_cfg_esync[1] | SYSC到eFPGA的保留配置 |
| int_fpga_in | input | 320 | 312 | s2c_cfg_esync[0] | SYSC到eFPGA的保留配置 |
| int_fpga_in | input | 320 | 311 | pad_cpld_in_esync[35] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 310 | pad_cpld_in_esync[34] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 309 | pad_cpld_in_esync[33] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 308 | pad_cpld_in_esync[32] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 307 | pad_cpld_in_esync[31] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 306 | pad_cpld_in_esync[30] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 305 | pad_cpld_in_esync[29] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 304 | pad_cpld_in_esync[28] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 303 | pad_cpld_in_esync[27] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 302 | pad_cpld_in_esync[26] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 301 | pad_cpld_in_esync[25] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 300 | pad_cpld_in_esync[24] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 299 | pad_cpld_in_esync[23] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 298 | pad_cpld_in_esync[22] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 297 | pad_cpld_in_esync[21] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 296 | pad_cpld_in_esync[20] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 295 | pad_cpld_in_esync[19] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 294 | pad_cpld_in_esync[18] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 293 | pad_cpld_in_esync[17] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 292 | pad_cpld_in_esync[16] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 291 | pad_cpld_in_esync[15] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 290 | pad_cpld_in_esync[14] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 289 | pad_cpld_in_esync[13] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 288 | pad_cpld_in_esync[12] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 287 | pad_cpld_in_esync[11] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 286 | pad_cpld_in_esync[10] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 285 | pad_cpld_in_esync[9] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 284 | pad_cpld_in_esync[8] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 283 | pad_cpld_in_esync[7] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 282 | pad_cpld_in_esync[6] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 281 | pad_cpld_in_esync[5] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 280 | pad_cpld_in_esync[4] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 279 | pad_cpld_in_esync[3] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 278 | pad_cpld_in_esync[2] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 277 | pad_cpld_in_esync[1] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 276 | pad_cpld_in_esync[0] | PAD 直接输入eFPGA |
| int_fpga_in | input | 320 | 275 | soc_hard_rst_n_esync | SOC HARD复位 |
| int_fpga_in | input | 320 | 274 | soc_wdg0_rst_n_esync | SOC 看门狗复位 |
| int_fpga_in | input | 320 | 273 | soc_wdg1_rst_n_esync | SOC 看门狗复位 |
| int_fpga_in | input | 320 | 272 | soc_soft_rst_n_esync | SOC 软复位 |
| int_fpga_in | input | 320 | 271 | cpld_pll_los_status_esync | CPLD PLL 频率状态，1'b1:无时钟或频率异常 |
| int_fpga_in | input | 320 | 270 | ppi_csn | PPI |
| int_fpga_in | input | 320 | 269 | ppi_data_bus_esync[11] | PPI |
| int_fpga_in | input | 320 | 268 | ppi_data_bus_esync[10] | PPI |
| int_fpga_in | input | 320 | 267 | ppi_data_bus_esync[9] | PPI |
| int_fpga_in | input | 320 | 266 | ppi_data_bus_esync[8] | PPI |
| int_fpga_in | input | 320 | 265 | ppi_data_bus_esync[7] | PPI |
| int_fpga_in | input | 320 | 264 | ppi_data_bus_esync[6] | PPI |
| int_fpga_in | input | 320 | 263 | ppi_data_bus_esync[5] | PPI |
| int_fpga_in | input | 320 | 262 | ppi_data_bus_esync[4] | PPI |
| int_fpga_in | input | 320 | 261 | ppi_data_bus_esync[3] | PPI |
| int_fpga_in | input | 320 | 260 | ppi_data_bus_esync[2] | PPI |
| int_fpga_in | input | 320 | 259 | ppi_data_bus_esync[1] | PPI |
| int_fpga_in | input | 320 | 258 | ppi_data_bus_esync[0] | PPI |
| int_fpga_in | input | 320 | 257 | ppi_addr_esync[4] | PPI |
| int_fpga_in | input | 320 | 256 | ppi_addr_esync[3] | PPI |
| int_fpga_in | input | 320 | 255 | ppi_addr_esync[2] | PPI |
| int_fpga_in | input | 320 | 254 | ppi_addr_esync[1] | PPI |
| int_fpga_in | input | 320 | 253 | ppi_addr_esync[0] | PPI |
| int_fpga_in | input | 320 | 252 | inxb_cpld_data_esync[15] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 251 | inxb_cpld_data_esync[14] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 250 | inxb_cpld_data_esync[13] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 249 | inxb_cpld_data_esync[12] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 248 | inxb_cpld_data_esync[11] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 247 | inxb_cpld_data_esync[10] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 246 | inxb_cpld_data_esync[9] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 245 | inxb_cpld_data_esync[8] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 244 | inxb_cpld_data_esync[7] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 243 | inxb_cpld_data_esync[6] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 242 | inxb_cpld_data_esync[5] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 241 | inxb_cpld_data_esync[4] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 240 | inxb_cpld_data_esync[3] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 239 | inxb_cpld_data_esync[2] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 238 | inxb_cpld_data_esync[1] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 237 | inxb_cpld_data_esync[0] | INPUTXBAR数据 |
| int_fpga_in | input | 320 | 236 | pfxb_cpld_data_esync[10] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 235 | pfxb_cpld_data_esync[9] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 234 | pfxb_cpld_data_esync[8] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 233 | pfxb_cpld_data_esync[7] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 232 | pfxb_cpld_data_esync[6] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 231 | pfxb_cpld_data_esync[5] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 230 | pfxb_cpld_data_esync[4] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 229 | pfxb_cpld_data_esync[3] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 228 | pfxb_cpld_data_esync[2] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 227 | pfxb_cpld_data_esync[1] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 226 | pfxb_cpld_data_esync[0] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 225 | etxb_cpld_data_esync[9] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 224 | etxb_cpld_data_esync[8] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 223 | etxb_cpld_data_esync[7] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 222 | etxb_cpld_data_esync[6] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 221 | etxb_cpld_data_esync[5] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 220 | etxb_cpld_data_esync[4] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 219 | etxb_cpld_data_esync[3] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 218 | etxb_cpld_data_esync[2] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 217 | etxb_cpld_data_esync[1] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 216 | etxb_cpld_data_esync[0] | PWMXBAR数据 |
| int_fpga_in | input | 320 | 215 | etim_cpld_sync_esync | ETIM PWM相位同步信号 |
| int_fpga_in | input | 320 | 214 | cmpc_cpld_evth_esync[10] | CMPC H事件 |
| int_fpga_in | input | 320 | 213 | cmpc_cpld_evth_esync[9] | CMPC H事件 |
| int_fpga_in | input | 320 | 212 | cmpc_cpld_evth_esync[8] | CMPC H事件 |
| int_fpga_in | input | 320 | 211 | cmpc_cpld_evth_esync[7] | CMPC H事件 |
| int_fpga_in | input | 320 | 210 | cmpc_cpld_evth_esync[6] | CMPC H事件 |
| int_fpga_in | input | 320 | 209 | cmpc_cpld_evth_esync[5] | CMPC H事件 |
| int_fpga_in | input | 320 | 208 | cmpc_cpld_evth_esync[4] | CMPC H事件 |
| int_fpga_in | input | 320 | 207 | cmpc_cpld_evth_esync[3] | CMPC H事件 |
| int_fpga_in | input | 320 | 206 | cmpc_cpld_evth_esync[2] | CMPC H事件 |
| int_fpga_in | input | 320 | 205 | cmpc_cpld_evth_esync[1] | CMPC H事件 |
| int_fpga_in | input | 320 | 204 | cmpc_cpld_evth_esync[0] | CMPC H事件 |
| int_fpga_in | input | 320 | 203 | cmpc_cpld_evtl_esync[10] | CMPC L事件 |
| int_fpga_in | input | 320 | 202 | cmpc_cpld_evtl_esync[9] | CMPC L事件 |
| int_fpga_in | input | 320 | 201 | cmpc_cpld_evtl_esync[8] | CMPC L事件 |
| int_fpga_in | input | 320 | 200 | cmpc_cpld_evtl_esync[7] | CMPC L事件 |
| int_fpga_in | input | 320 | 199 | cmpc_cpld_evtl_esync[6] | CMPC L事件 |
| int_fpga_in | input | 320 | 198 | cmpc_cpld_evtl_esync[5] | CMPC L事件 |
| int_fpga_in | input | 320 | 197 | cmpc_cpld_evtl_esync[4] | CMPC L事件 |
| int_fpga_in | input | 320 | 196 | cmpc_cpld_evtl_esync[3] | CMPC L事件 |
| int_fpga_in | input | 320 | 195 | cmpc_cpld_evtl_esync[2] | CMPC L事件 |
| int_fpga_in | input | 320 | 194 | cmpc_cpld_evtl_esync[1] | CMPC L事件 |
| int_fpga_in | input | 320 | 193 | cmpc_cpld_evtl_esync[0] | CMPC L事件 |
| int_fpga_in | input | 320 | 192 | adc0_cpld_evtl_esync[15] | ADC L事件 |
| int_fpga_in | input | 320 | 191 | adc0_cpld_evtl_esync[14] | ADC L事件 |
| int_fpga_in | input | 320 | 190 | adc0_cpld_evtl_esync[13] | ADC L事件 |
| int_fpga_in | input | 320 | 189 | adc0_cpld_evtl_esync[12] | ADC L事件 |
| int_fpga_in | input | 320 | 188 | adc0_cpld_evtl_esync[11] | ADC L事件 |
| int_fpga_in | input | 320 | 187 | adc0_cpld_evtl_esync[10] | ADC L事件 |
| int_fpga_in | input | 320 | 186 | adc0_cpld_evtl_esync[9] | ADC L事件 |
| int_fpga_in | input | 320 | 185 | adc0_cpld_evtl_esync[8] | ADC L事件 |
| int_fpga_in | input | 320 | 184 | adc0_cpld_evtl_esync[7] | ADC L事件 |
| int_fpga_in | input | 320 | 183 | adc0_cpld_evtl_esync[6] | ADC L事件 |
| int_fpga_in | input | 320 | 182 | adc0_cpld_evtl_esync[5] | ADC L事件 |
| int_fpga_in | input | 320 | 181 | adc0_cpld_evtl_esync[4] | ADC L事件 |
| int_fpga_in | input | 320 | 180 | adc0_cpld_evtl_esync[3] | ADC L事件 |
| int_fpga_in | input | 320 | 179 | adc0_cpld_evtl_esync[2] | ADC L事件 |
| int_fpga_in | input | 320 | 178 | adc0_cpld_evtl_esync[1] | ADC L事件 |
| int_fpga_in | input | 320 | 177 | adc0_cpld_evtl_esync[0] | ADC L事件 |
| int_fpga_in | input | 320 | 176 | adc0_cpld_evth_esync[15] | ADC H事件 |
| int_fpga_in | input | 320 | 175 | adc0_cpld_evth_esync[14] | ADC H事件 |
| int_fpga_in | input | 320 | 174 | adc0_cpld_evth_esync[13] | ADC H事件 |
| int_fpga_in | input | 320 | 173 | adc0_cpld_evth_esync[12] | ADC H事件 |
| int_fpga_in | input | 320 | 172 | adc0_cpld_evth_esync[11] | ADC H事件 |
| int_fpga_in | input | 320 | 171 | adc0_cpld_evth_esync[10] | ADC H事件 |
| int_fpga_in | input | 320 | 170 | adc0_cpld_evth_esync[9] | ADC H事件 |
| int_fpga_in | input | 320 | 169 | adc0_cpld_evth_esync[8] | ADC H事件 |
| int_fpga_in | input | 320 | 168 | adc0_cpld_evth_esync[7] | ADC H事件 |
| int_fpga_in | input | 320 | 167 | adc0_cpld_evth_esync[6] | ADC H事件 |
| int_fpga_in | input | 320 | 166 | adc0_cpld_evth_esync[5] | ADC H事件 |
| int_fpga_in | input | 320 | 165 | adc0_cpld_evth_esync[4] | ADC H事件 |
| int_fpga_in | input | 320 | 164 | adc0_cpld_evth_esync[3] | ADC H事件 |
| int_fpga_in | input | 320 | 163 | adc0_cpld_evth_esync[2] | ADC H事件 |
| int_fpga_in | input | 320 | 162 | adc0_cpld_evth_esync[1] | ADC H事件 |
| int_fpga_in | input | 320 | 161 | adc0_cpld_evth_esync[0] | ADC H事件 |
| int_fpga_in | input | 320 | 160 | adc1_cpld_evtl_esync[15] | ADC L事件 |
| int_fpga_in | input | 320 | 159 | adc1_cpld_evtl_esync[14] | ADC L事件 |
| int_fpga_in | input | 320 | 158 | adc1_cpld_evtl_esync[13] | ADC L事件 |
| int_fpga_in | input | 320 | 157 | adc1_cpld_evtl_esync[12] | ADC L事件 |
| int_fpga_in | input | 320 | 156 | adc1_cpld_evtl_esync[11] | ADC L事件 |
| int_fpga_in | input | 320 | 155 | adc1_cpld_evtl_esync[10] | ADC L事件 |
| int_fpga_in | input | 320 | 154 | adc1_cpld_evtl_esync[9] | ADC L事件 |
| int_fpga_in | input | 320 | 153 | adc1_cpld_evtl_esync[8] | ADC L事件 |
| int_fpga_in | input | 320 | 152 | adc1_cpld_evtl_esync[7] | ADC L事件 |
| int_fpga_in | input | 320 | 151 | adc1_cpld_evtl_esync[6] | ADC L事件 |
| int_fpga_in | input | 320 | 150 | adc1_cpld_evtl_esync[5] | ADC L事件 |
| int_fpga_in | input | 320 | 149 | adc1_cpld_evtl_esync[4] | ADC L事件 |
| int_fpga_in | input | 320 | 148 | adc1_cpld_evtl_esync[3] | ADC L事件 |
| int_fpga_in | input | 320 | 147 | adc1_cpld_evtl_esync[2] | ADC L事件 |
| int_fpga_in | input | 320 | 146 | adc1_cpld_evtl_esync[1] | ADC L事件 |
| int_fpga_in | input | 320 | 145 | adc1_cpld_evtl_esync[0] | ADC L事件 |
| int_fpga_in | input | 320 | 144 | adc1_cpld_evth_esync[15] | ADC H事件 |
| int_fpga_in | input | 320 | 143 | adc1_cpld_evth_esync[14] | ADC H事件 |
| int_fpga_in | input | 320 | 142 | adc1_cpld_evth_esync[13] | ADC H事件 |
| int_fpga_in | input | 320 | 141 | adc1_cpld_evth_esync[12] | ADC H事件 |
| int_fpga_in | input | 320 | 140 | adc1_cpld_evth_esync[11] | ADC H事件 |
| int_fpga_in | input | 320 | 139 | adc1_cpld_evth_esync[10] | ADC H事件 |
| int_fpga_in | input | 320 | 138 | adc1_cpld_evth_esync[9] | ADC H事件 |
| int_fpga_in | input | 320 | 137 | adc1_cpld_evth_esync[8] | ADC H事件 |
| int_fpga_in | input | 320 | 136 | adc1_cpld_evth_esync[7] | ADC H事件 |
| int_fpga_in | input | 320 | 135 | adc1_cpld_evth_esync[6] | ADC H事件 |
| int_fpga_in | input | 320 | 134 | adc1_cpld_evth_esync[5] | ADC H事件 |
| int_fpga_in | input | 320 | 133 | adc1_cpld_evth_esync[4] | ADC H事件 |
| int_fpga_in | input | 320 | 132 | adc1_cpld_evth_esync[3] | ADC H事件 |
| int_fpga_in | input | 320 | 131 | adc1_cpld_evth_esync[2] | ADC H事件 |
| int_fpga_in | input | 320 | 130 | adc1_cpld_evth_esync[1] | ADC H事件 |
| int_fpga_in | input | 320 | 129 | adc1_cpld_evth_esync[0] | ADC H事件 |
| int_fpga_in | input | 320 | 128 | cpu0_lockup_esync | CPU挂死 |
| int_fpga_in | input | 320 | 127 | cpu1_lockup_esync | CPU挂死 |
| int_fpga_in | input | 320 | 126 | bus_timeout_esync | 总线超时 |
| int_fpga_in | input | 320 | 125 | temp_warn_esync | 过温告警 |
| int_fpga_in | input | 320 | 124 | power_err_esync | 过流 |
| int_fpga_in | input | 320 | 123 | por_uv_warn_esync | 欠压 |
| int_fpga_in | input | 320 | 122 | por_ov_warn_esync | 过压 |
| int_fpga_in | input | 320 | 121 | cfg_efpga1_esync[31] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 120 | cfg_efpga1_esync[30] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 119 | cfg_efpga1_esync[29] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 118 | cfg_efpga1_esync[28] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 117 | cfg_efpga1_esync[27] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 116 | cfg_efpga1_esync[26] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 115 | cfg_efpga1_esync[25] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 114 | cfg_efpga1_esync[24] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 113 | cfg_efpga1_esync[23] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 112 | cfg_efpga1_esync[22] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 111 | cfg_efpga1_esync[21] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 110 | cfg_efpga1_esync[20] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 109 | cfg_efpga1_esync[19] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 108 | cfg_efpga1_esync[18] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 107 | cfg_efpga1_esync[17] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 106 | cfg_efpga1_esync[16] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 105 | cfg_efpga1_esync[15] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 104 | cfg_efpga1_esync[14] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 103 | cfg_efpga1_esync[13] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 102 | cfg_efpga1_esync[12] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 101 | cfg_efpga1_esync[11] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 100 | cfg_efpga1_esync[10] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 99 | cfg_efpga1_esync[9] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 98 | cfg_efpga1_esync[8] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 97 | cfg_efpga1_esync[7] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 96 | cfg_efpga1_esync[6] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 95 | cfg_efpga1_esync[5] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 94 | cfg_efpga1_esync[4] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 93 | cfg_efpga1_esync[3] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 92 | cfg_efpga1_esync[2] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 91 | cfg_efpga1_esync[1] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 90 | cfg_efpga1_esync[0] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 89 | cfg_efpga0_esync[31] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 88 | cfg_efpga0_esync[30] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 87 | cfg_efpga0_esync[29] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 86 | cfg_efpga0_esync[28] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 85 | cfg_efpga0_esync[27] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 84 | cfg_efpga0_esync[26] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 83 | cfg_efpga0_esync[25] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 82 | cfg_efpga0_esync[24] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 81 | cfg_efpga0_esync[23] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 80 | cfg_efpga0_esync[22] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 79 | cfg_efpga0_esync[21] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 78 | cfg_efpga0_esync[20] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 77 | cfg_efpga0_esync[19] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 76 | cfg_efpga0_esync[18] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 75 | cfg_efpga0_esync[17] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 74 | cfg_efpga0_esync[16] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 73 | cfg_efpga0_esync[15] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 72 | cfg_efpga0_esync[14] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 71 | cfg_efpga0_esync[13] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 70 | cfg_efpga0_esync[12] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 69 | cfg_efpga0_esync[11] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 68 | cfg_efpga0_esync[10] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 67 | cfg_efpga0_esync[9] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 66 | cfg_efpga0_esync[8] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 65 | cfg_efpga0_esync[7] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 64 | cfg_efpga0_esync[6] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 63 | cfg_efpga0_esync[5] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 62 | cfg_efpga0_esync[4] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 61 | cfg_efpga0_esync[3] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 60 | cfg_efpga0_esync[2] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 59 | cfg_efpga0_esync[1] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 58 | cfg_efpga0_esync[0] | eFPGA保留配置接口，与总线交互 |
| int_fpga_in | input | 320 | 57 | etim_cpld_pwm_esync[9] | ETIM PWM |
| int_fpga_in | input | 320 | 56 | etim_cpld_pwm_esync[8] | ETIM PWM |
| int_fpga_in | input | 320 | 55 | etim_cpld_pwm_esync[7] | ETIM PWM |
| int_fpga_in | input | 320 | 54 | etim_cpld_pwm_esync[6] | ETIM PWM |
| int_fpga_in | input | 320 | 53 | etim_cpld_pwm_esync[5] | ETIM PWM |
| int_fpga_in | input | 320 | 52 | etim_cpld_pwm_esync[4] | ETIM PWM |
| int_fpga_in | input | 320 | 51 | etim_cpld_pwm_esync[3] | ETIM PWM |
| int_fpga_in | input | 320 | 50 | etim_cpld_pwm_esync[2] | ETIM PWM |
| int_fpga_in | input | 320 | 49 | etim_cpld_pwm_esync[1] | ETIM PWM |
| int_fpga_in | input | 320 | 48 | etim_cpld_pwm_esync[0] | ETIM PWM |
| int_fpga_in | input | 320 | 47 | srpwm_cpld_pwmb_oen_esync[11] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 46 | srpwm_cpld_pwma_oen_esync[11] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 45 | srpwm_cpld_pwm_b_esync[11] | SRPWM PWM |
| int_fpga_in | input | 320 | 44 | srpwm_cpld_pwm_a_esync[11] | SRPWM PWM |
| int_fpga_in | input | 320 | 43 | srpwm_cpld_pwmb_oen_esync[10] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 42 | srpwm_cpld_pwma_oen_esync[10] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 41 | srpwm_cpld_pwm_b_esync[10] | SRPWM PWM |
| int_fpga_in | input | 320 | 40 | srpwm_cpld_pwm_a_esync[10] | SRPWM PWM |
| int_fpga_in | input | 320 | 39 | srpwm_cpld_pwmb_oen_esync[9] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 38 | srpwm_cpld_pwma_oen_esync[9] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 37 | srpwm_cpld_pwm_b_esync[9] | SRPWM PWM |
| int_fpga_in | input | 320 | 36 | srpwm_cpld_pwm_a_esync[9] | SRPWM PWM |
| int_fpga_in | input | 320 | 35 | srpwm_cpld_pwmb_oen_esync[8] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 34 | srpwm_cpld_pwma_oen_esync[8] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 33 | srpwm_cpld_pwm_b_esync[8] | SRPWM PWM |
| int_fpga_in | input | 320 | 32 | srpwm_cpld_pwm_a_esync[8] | SRPWM PWM |
| int_fpga_in | input | 320 | 31 | srpwm_cpld_pwmb_oen_esync[7] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 30 | srpwm_cpld_pwma_oen_esync[7] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 29 | srpwm_cpld_pwm_b_esync[7] | SRPWM PWM |
| int_fpga_in | input | 320 | 28 | srpwm_cpld_pwm_a_esync[7] | SRPWM PWM |
| int_fpga_in | input | 320 | 27 | srpwm_cpld_pwmb_oen_esync[6] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 26 | srpwm_cpld_pwma_oen_esync[6] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 25 | srpwm_cpld_pwm_b_esync[6] | SRPWM PWM |
| int_fpga_in | input | 320 | 24 | srpwm_cpld_pwm_a_esync[6] | SRPWM PWM |
| int_fpga_in | input | 320 | 23 | srpwm_cpld_pwmb_oen_esync[5] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 22 | srpwm_cpld_pwma_oen_esync[5] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 21 | srpwm_cpld_pwm_b_esync[5] | SRPWM PWM |
| int_fpga_in | input | 320 | 20 | srpwm_cpld_pwm_a_esync[5] | SRPWM PWM |
| int_fpga_in | input | 320 | 19 | srpwm_cpld_pwmb_oen_esync[4] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 18 | srpwm_cpld_pwma_oen_esync[4] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 17 | srpwm_cpld_pwm_b_esync[4] | SRPWM PWM |
| int_fpga_in | input | 320 | 16 | srpwm_cpld_pwm_a_esync[4] | SRPWM PWM |
| int_fpga_in | input | 320 | 15 | srpwm_cpld_pwmb_oen_esync[3] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 14 | srpwm_cpld_pwma_oen_esync[3] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 13 | srpwm_cpld_pwm_b_esync[3] | SRPWM PWM |
| int_fpga_in | input | 320 | 12 | srpwm_cpld_pwm_a_esync[3] | SRPWM PWM |
| int_fpga_in | input | 320 | 11 | srpwm_cpld_pwmb_oen_esync[2] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 10 | srpwm_cpld_pwma_oen_esync[2] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 9 | srpwm_cpld_pwm_b_esync[2] | SRPWM PWM |
| int_fpga_in | input | 320 | 8 | srpwm_cpld_pwm_a_esync[2] | SRPWM PWM |
| int_fpga_in | input | 320 | 7 | srpwm_cpld_pwmb_oen_esync[1] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 6 | srpwm_cpld_pwma_oen_esync[1] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 5 | srpwm_cpld_pwm_b_esync[1] | SRPWM PWM |
| int_fpga_in | input | 320 | 4 | srpwm_cpld_pwm_a_esync[1] | SRPWM PWM |
| int_fpga_in | input | 320 | 3 | srpwm_cpld_pwmb_oen_esync[0] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 2 | srpwm_cpld_pwma_oen_esync[0] | SRPWM PWM_OEN |
| int_fpga_in | input | 320 | 1 | srpwm_cpld_pwm_b_esync[0] | SRPWM PWM |
| int_fpga_in | input | 320 | 0 | srpwm_cpld_pwm_a_esync[0] | SRPWM PWM |
| int_fpga_out | output | 200 | 199 | ppi_data_out[11] | PPI |
| int_fpga_out | output | 200 | 198 | ppi_data_out[10] | PPI |
| int_fpga_out | output | 200 | 197 | ppi_data_out[9] | PPI |
| int_fpga_out | output | 200 | 196 | ppi_data_out[8] | PPI |
| int_fpga_out | output | 200 | 195 | ppi_data_out[7] | PPI |
| int_fpga_out | output | 200 | 194 | ppi_data_out[6] | PPI |
| int_fpga_out | output | 200 | 193 | ppi_data_out[5] | PPI |
| int_fpga_out | output | 200 | 192 | ppi_data_out[4] | PPI |
| int_fpga_out | output | 200 | 191 | ppi_data_out[3] | PPI |
| int_fpga_out | output | 200 | 190 | ppi_data_out[2] | PPI |
| int_fpga_out | output | 200 | 189 | ppi_data_out[1] | PPI |
| int_fpga_out | output | 200 | 188 | ppi_data_out[0] | PPI |
| int_fpga_out | output | 200 | 187 | c2s_rpt[14] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 186 | c2s_rpt[13] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 185 | c2s_rpt[12] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 184 | c2s_rpt[11] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 183 | c2s_rpt[10] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 182 | c2s_rpt[9] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 181 | c2s_rpt[8] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 180 | c2s_rpt[7] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 179 | c2s_rpt[6] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 178 | c2s_rpt[5] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 177 | c2s_rpt[4] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 176 | c2s_rpt[3] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 175 | c2s_rpt[2] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 174 | c2s_rpt[1] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 173 | c2s_rpt[0] | eFPGA到SYSC的保留上报 |
| int_fpga_out | output | 200 | 172 | efpga_dma_req0 | 用户自定义DMA触发源 |
| int_fpga_out | output | 200 | 171 | efpga_dma_req1 | 用户自定义DMA触发源 |
| int_fpga_out | output | 200 | 170 | efpga_c2s_rst_n | 用户自定义复位源 |
| int_fpga_out | output | 200 | 169 | efpga0_rpt[31] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 168 | efpga0_rpt[30] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 167 | efpga0_rpt[29] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 166 | efpga0_rpt[28] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 165 | efpga0_rpt[27] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 164 | efpga0_rpt[26] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 163 | efpga0_rpt[25] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 162 | efpga0_rpt[24] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 161 | efpga0_rpt[23] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 160 | efpga0_rpt[22] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 159 | efpga0_rpt[21] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 158 | efpga0_rpt[20] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 157 | efpga0_rpt[19] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 156 | efpga0_rpt[18] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 155 | efpga0_rpt[17] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 154 | efpga0_rpt[16] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 153 | efpga0_rpt[15] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 152 | efpga0_rpt[14] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 151 | efpga0_rpt[13] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 150 | efpga0_rpt[12] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 149 | efpga0_rpt[11] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 148 | efpga0_rpt[10] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 147 | efpga0_rpt[9] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 146 | efpga0_rpt[8] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 145 | efpga0_rpt[7] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 144 | efpga0_rpt[6] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 143 | efpga0_rpt[5] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 142 | efpga0_rpt[4] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 141 | efpga0_rpt[3] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 140 | efpga0_rpt[2] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 139 | efpga0_rpt[1] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 138 | efpga0_rpt[0] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 137 | efpga1_rpt[31] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 136 | efpga1_rpt[30] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 135 | efpga1_rpt[29] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 134 | efpga1_rpt[28] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 133 | efpga1_rpt[27] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 132 | efpga1_rpt[26] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 131 | efpga1_rpt[25] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 130 | efpga1_rpt[24] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 129 | efpga1_rpt[23] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 128 | efpga1_rpt[22] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 127 | efpga1_rpt[21] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 126 | efpga1_rpt[20] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 125 | efpga1_rpt[19] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 124 | efpga1_rpt[18] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 123 | efpga1_rpt[17] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 122 | efpga1_rpt[16] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 121 | efpga1_rpt[15] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 120 | efpga1_rpt[14] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 119 | efpga1_rpt[13] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 118 | efpga1_rpt[12] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 117 | efpga1_rpt[11] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 116 | efpga1_rpt[10] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 115 | efpga1_rpt[9] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 114 | efpga1_rpt[8] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 113 | efpga1_rpt[7] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 112 | efpga1_rpt[6] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 111 | efpga1_rpt[5] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 110 | efpga1_rpt[4] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 109 | efpga1_rpt[3] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 108 | efpga1_rpt[2] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 107 | efpga1_rpt[1] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 106 | efpga1_rpt[0] | eFPGA保留上报接口，与总线交互 |
| int_fpga_out | output | 200 | 105 | cpld_opxb_data[9] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 104 | cpld_opxb_data[8] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 103 | cpld_opxb_data[7] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 102 | cpld_opxb_data[6] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 101 | cpld_opxb_data[5] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 100 | cpld_opxb_data[4] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 99 | cpld_opxb_data[3] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 98 | cpld_opxb_data[2] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 97 | cpld_opxb_data[1] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 96 | cpld_opxb_data[0] | eFPGA 输出到OUTPUTXBAR |
| int_fpga_out | output | 200 | 95 | cpld_pad_oen[35] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 94 | cpld_pad_oen[34] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 93 | cpld_pad_oen[33] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 92 | cpld_pad_oen[32] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 91 | cpld_pad_oen[31] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 90 | cpld_pad_oen[30] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 89 | cpld_pad_oen[29] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 88 | cpld_pad_oen[28] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 87 | cpld_pad_oen[27] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 86 | cpld_pad_oen[26] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 85 | cpld_pad_oen[25] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 84 | cpld_pad_oen[24] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 83 | cpld_pad_oen[23] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 82 | cpld_pad_oen[22] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 81 | cpld_pad_oen[21] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 80 | cpld_pad_oen[20] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 79 | cpld_pad_oen[19] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 78 | cpld_pad_oen[18] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 77 | cpld_pad_oen[17] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 76 | cpld_pad_oen[16] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 75 | cpld_pad_oen[15] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 74 | cpld_pad_oen[14] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 73 | cpld_pad_oen[13] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 72 | cpld_pad_oen[12] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 71 | cpld_pad_oen[11] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 70 | cpld_pad_oen[10] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 69 | cpld_pad_oen[9] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 68 | cpld_pad_oen[8] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 67 | cpld_pad_oen[7] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 66 | cpld_pad_oen[6] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 65 | cpld_pad_oen[5] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 64 | cpld_pad_oen[4] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 63 | cpld_pad_oen[3] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 62 | cpld_pad_oen[2] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 61 | cpld_pad_oen[1] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 60 | cpld_pad_oen[0] | eFPGA 输出到PAD_OEN |
| int_fpga_out | output | 200 | 59 | cpld_pad_out[35] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 58 | cpld_pad_out[34] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 57 | cpld_pad_out[33] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 56 | cpld_pad_out[32] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 55 | cpld_pad_out[31] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 54 | cpld_pad_out[30] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 53 | cpld_pad_out[29] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 52 | cpld_pad_out[28] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 51 | cpld_pad_out[27] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 50 | cpld_pad_out[26] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 49 | cpld_pad_out[25] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 48 | cpld_pad_out[24] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 47 | cpld_pad_out[23] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 46 | cpld_pad_out[22] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 45 | cpld_pad_out[21] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 44 | cpld_pad_out[20] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 43 | cpld_pad_out[19] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 42 | cpld_pad_out[18] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 41 | cpld_pad_out[17] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 40 | cpld_pad_out[16] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 39 | cpld_pad_out[15] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 38 | cpld_pad_out[14] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 37 | cpld_pad_out[13] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 36 | cpld_pad_out[12] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 35 | cpld_pad_out[11] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 34 | cpld_pad_out[10] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 33 | cpld_pad_out[9] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 32 | cpld_pad_out[8] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 31 | cpld_pad_out[7] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 30 | cpld_pad_out[6] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 29 | cpld_pad_out[5] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 28 | cpld_pad_out[4] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 27 | cpld_pad_out[3] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 26 | cpld_pad_out[2] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 25 | cpld_pad_out[1] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 24 | cpld_pad_out[0] | eFPGA 输出到PAD |
| int_fpga_out | output | 200 | 23 | cpld_srpwm_fault[23] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 22 | cpld_srpwm_fault[22] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 21 | cpld_srpwm_fault[21] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 20 | cpld_srpwm_fault[20] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 19 | cpld_srpwm_fault[19] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 18 | cpld_srpwm_fault[18] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 17 | cpld_srpwm_fault[17] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 16 | cpld_srpwm_fault[16] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 15 | cpld_srpwm_fault[15] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 14 | cpld_srpwm_fault[14] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 13 | cpld_srpwm_fault[13] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 12 | cpld_srpwm_fault[12] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 11 | cpld_srpwm_fault[11] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 10 | cpld_srpwm_fault[10] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 9 | cpld_srpwm_fault[9] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 8 | cpld_srpwm_fault[8] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 7 | cpld_srpwm_fault[7] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 6 | cpld_srpwm_fault[6] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 5 | cpld_srpwm_fault[5] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 4 | cpld_srpwm_fault[4] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 3 | cpld_srpwm_fault[3] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 2 | cpld_srpwm_fault[2] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 1 | cpld_srpwm_fault[1] | eFPGA 输出到SRPWM用于封波 |
| int_fpga_out | output | 200 | 0 | cpld_srpwm_fault[0] | eFPGA 输出到SRPWM用于封波 |

---

## INTERFACE_EFPGA_CFG

> 原图：`../../interface_efpga_cfg/images/GameViewer_MLLzggVIdI.png`

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
| efpga0_rpt_val_in | output | 32 | efpga_rpt0_val_in |
| efpga1_rpt_val_in | output | 32 | efpga_rpt1_val_in |
| s2c_cfg_enb | input | 1 | s2c_cfg_enb |
| s2c_cfg | input | 32 | s2c_cfg |
| s2c_cfg_esync | output | 32 | s2c_cfg_esync |

---

## INTERFACE_INT

> 原图：`../../interface_int/images/GameViewer_UdwODJm0Oy.png`

| signal | inout | width | connect_sig |
|---|---|---:|---|
| clk | input | 1 | soc_sys_clk |
| rst_n | input | 1 | efpga_sys_resetn |
| int_src_pulse | input | 2 | cpld_usr_intr_src |
| cpld_usr_intr | output | 2 | cpld_usr_intr |

---

## INTERFACE_PPI

> 原图：`../../interface_ppi/images/GameViewer_E5Lo6kLaVW.png`

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

---

## INTERFACE_TEST_PIN

> 原图：`../../interface_test_pin/images/GameViewer_aGuTuqYiQP.png`

| signal | inout | width | connect_sig | list number |
|---|---|---:|---|---|
| sysc_cpld_testpin0_sel | input | 8 | sysc_cpld_testpin0_sel | |
| sysc_cpld_testpin1_sel | input | 8 | sysc_cpld_testpin1_sel | |
| sysc_cpld_testpin2_sel | input | 8 | sysc_cpld_testpin2_sel | |
| sysc_cpld_testpin3_sel | input | 8 | sysc_cpld_testpin3_sel | |
| cpld_sysc_testpin | output | 4 | cpld_sysc_testpin | |
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
