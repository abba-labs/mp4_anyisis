# CPLD_INTERFACE

> 来源：ET6601 原始截图精准还原。
> 本文件恢复原始文档边界：CPLD_INTERFACE 是一份文档；以下接口内容不再作为独立最终文档。
> 当前处于逐图精校阶段；无法确认的字符后续必须回到对应原图复核，禁止推测。


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

> 原图（按表格行号连续）：
> - `../../interface_cpld_cfg/images/GameViewer_DeXJCeTp8c.png`：1–32
> - `../../interface_cpld_cfg/images/GameViewer_DjmYAqFskT.png`：33–62
> - `../../interface_cpld_cfg/images/GameViewer_1AL3gcTZwO.png`：63–92
> - `../../interface_cpld_cfg/images/GameViewer_zJTLoUFpvE.png`：93–124
> - `../../interface_cpld_cfg/images/GameViewer_XN1mwSbZGj.png`：125–156
> - `../../interface_cpld_cfg/images/GameViewer_sB1DKm1Cn1.png`：157

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

### 截图编号 1 (`../../interface_efpga/images/GameViewer_2zddazPQIp.png`)

#### 【全页】

lint.foga_out
83|cpld.pad_oen[23]
eFPGA输出到PAD_OEN
472lint_fpga_out
cpld.pad_oen[22]
eFPGA输出到PAD.OEN
473int fpga out
cpld pad_oen[21]
eFPGA输出到PAD.OEN
474 int fpga out
cpldpad oen[20]
eFPGA输出到PADOEN
475int_fpga_out
cpld_pad_oen[19]
eFPGA输出到PAD.OEN
476int_fpga_out
cpld.pad_oen[18]
eFPGA输出到PAD_OEN
477lint fpga out
cpld pad oen[17]
eFPGA输出到PAD.OEN
478 int fpga out
cpldpadoen[16]
eFPGA输出到PADOEN
479int._fpga_out
cpld.pad_oen[15]
eFPGA输出到PAD.OEN
480intfpga_out
cpld_pad_oen[14]
eFPGA输出到PAD.OEN
481intfpga out
cpld.pad_oen[13]
eFPGA输出到PAD.OEN
482intfpga out
cpld pad oen[12]
eFPGA输出到PADOEN
483 int_fpga_out
cpld_pad_oen[11]
eFPGA输出到PAD.OEN
cpld._pad_oen[10]
484int_fpga_out
eFPGA输出到PAD_OEN
485int_fpga_out
cpld.pad
Loen[9]
eFPGA输出到PAD_OEN
486int fpga out
cpldpad oen[8]
eFPGA输出到PADOEN
487lint fpga.out
cpld_pad.oen[7]
eFPGA输出到PAD.OEN
488int_fpga_out
cpld.pad_oen[6]
eFPGA输出到PAD.OEN
489int.fpga_out
cpld_pad_oen[5]
eFPGA输出到PAD.OEN
490lint fpga out
cpldpadoen[4]
eFPGA输出到PADOEN
491int fpgaout
cpld_pad.oen[3]
eFPGA输出到PADOEN
492int_fpga_out
cpld_pad_oen[2]
eFPGA输出到PAD_OEN
493intfpga_out
cpld pad_oen[1]
eFPGA输出到PAD.OEN
494intfpga out
cpldpad.oenl01
eFPGA输出到PAD.OEN
495int fpga_out
cpld_pad_out[35]
eFPGA输出到PAD
496int.fpga_out
cpldpad_out|34]
eFPGA输出到PAD
497lint._fpga_out
cpld pad_out[33]
eFPGA输出到PAD
498 int fpga out
cpldpad.out/321
eFPGA输出到PAD
499 int fpga out
cpldpadout[31]
eFPGA输出到PAD
500int_fpga_out
cpld_pad_out[30]
eFPGA输出到PAD
501int._fpga_out
cpld_pad_out[29]
eFPGA输出到PAD
52|cpld pad out[28]
502lintfpga_out
eFPGA输出到PAD
503intfpga out
cpld pad out[27]
eFPGA输出到PAD
504int_fpga_out
cpld_pad_out[26]
eFPGA输出到PAD
505int._fpga_out
cpld_pad_out[25]
eFPGA输出到PAD
48 cpld pad_out[24]
506intfpga.out
eFPGA输出到PAD



### 截图编号 2 (`../../interface_efpga/images/GameViewer_3BoqyOeJgh.png`)

#### 【全页】

363int foga_out
191lppi data_out[3]
IPPI
364int_fpga_out
190 ppi_data_out[2]
PPL
365int fpga_out
189 ppi._data_out[1]
PPI
366int fpga out
188ppi data out[0]
PPI
367int_fpga_out
187c2s_rpt[14]
eFPGA到SYSC的保留上报
368int_fpga_out
186|c2s_rpt[13]
eFPGA到SYSC的保留上报
185c2s.rpt/12]
369int.fpga_out
eFPGA到SYSC的保留上报
370int fpga out
184|c2s rpt|11]
eFPGA到SYSC的保留上报
371 int_fpga_out
183 c2s.rpt10]
eFPGA到SYSC的保留上报
372int_fpga_out
182c2s.rpt/91
eFPGA到SYSC的保留上报
373int fpga_out
181c2s rpt[8]
eFPGA到SYSC的保留上报
374 int fpga out
180c2s rpt/7
eFPGA到SYSC的保留上报
375int_fpga_out
179c2s.rpt[6]
eFPGA到SYSC的保留上报
178 c2s.rpti5]
376int_fpga_out
eFPGA到SYSC的保留上报
377 lint fpga out
c2srpt[4]
eFPGA到SYSC的保留上报
378 int fpga out
176c2s rpt/3]
eFPGA到SYSC的保留上报
379int_fpga out
175c2s rpt[2]
eFPGA到SYSC的保留上报
380int_fpga_out
174|c2s.rpt11
eFPGA到SYSC的保留上报
381 int fpga_out
173c2srptiol
eFPGA到SYSC的保留上报
172efpga dma rea0
382intfpga_out
用户自定义DMA触发源
383int fpga out
171efpga dma real
用户自定义DMA触发源
384int_fpga_out
170efpga_c2s.rst.n
用户自定义复位源
385int_fpga_out
169efpga0_rpt[31]
eFPGA保留上报接口，与总线交互
168efpga0rpt[30]
386intfpga_out
eFPGA保留上报接口，与总线交互
387int fpga out
167|efpga0_rpt[29]
eFPGA保留上报接口，与总线交互
388int_fpga_out
166|efpga0_rpt[28]
eFPGA保留上报接口，与总线交互
389int_fpga_out
165efpga0.rpt/27]
eFPGA保留上报接口，与总线交互
390int fpga_out
164efpga0 rpt[26]
eFPGA保留上报接口，与总线交互
163efpga0 rpt25]
391 int fpga out
eFPGA保留上报接口，与总线交互
392int_fpga_out
162efpga0_rpt[24]
eFPGA保留上报接口，与总线交互
393int_fpga_out
161|efpga0_rpt[23]
eFPGA保留上报接口，与总线交互
394 int_fpgaout
160|efpga0_rpt[22]
eFPGA保留上报接口，与总线交互
395int fpga out
159|efpga0 rpt[21]
eFPGA保留上报接口，与总线交互
396int_fpga_out
158efoga0.rot201
eFPGA保留上报接口，与总线交互
397int_fpga_out
157|efpga0_rpt[19]
eFPGA保留上报接口，与总线交互
398int fpga out
156|efpga0_rpt[18]
eFPGA保留上报接口，与总线交互



### 截图编号 3 (`../../interface_efpga/images/GameViewer_8iXOmcDGE1.png`)

#### 【全页】

eFPGA interface
width
NO.
connect signal
inout
说明
input
efpga sys clk
Sys_clk
200M时钟，与SOC系统时钟同步
input
sys.resetn
efpga_sys_resetn
CPLDHARD_RST&S2C
wdt_sclk
input
fpga_sO_hrdata
output
cpld_ahb1_hrdata
AHB1
fpgaso hreadyout
output
cpld ahb1_hreadyout
AHB1
cpld_ahb1_hresp
fpga_s0_hresp
output
AHB1
fpga_so_hsel
input
cpld_ahb1_hsel
AHB1
fpga_so.haddr
input
[20'd0.cpld_ahb1_.haddr)
AHB1
10 fpga s0 htrans
input
cpldahb1_htrans
AHB1
11 fpga_s0_hwrite
input
cpld_ahb1_hwrite
AHB1
12 fpga_s0_hwdata
cpld_ahb1_hwdata
input
AHB1
13fpga_s0_hready
input
cpld_ahb1_hready
AHB1
14 efpga dec en
input
eFPGAbitstreamdecipherenable
15efpga_deckey
input
eFPGA bitstream decipherkey
16 fpga intr
efpga_intr3_nc
17 fpga_intr
efpgaintr2.nc
18 fpga intr
cpld usrintrsrc[1]
用户自定义中断，脉冲或电平
19 fpga intr
cpld_usrintrsrco]
用户自定义中断，脉冲或电平
output
20 fpga_cfg_done_sync
cpld_cfg_done_sync
bit流配置完成
21 fpga_cfo_err
cpld_cfg_err sync
output
bit流配置错误
22wdt rstn.o
output
wdt_rstn.o.nc
23 free clko
input
free_clko
24 free_clk1
input
free_clk1
25free_clk2
input
free_clk2
26 free_clk3
input
efpga.sys.clk
27 scan_in
dft _efpga_scan in
input
DFT
dft_efpga_scan.out
28 scan_out
output
DFT
29 scan_en
dft_efpga_scan_en
input
DFT
30 scan_mode
dft_mode
input
DFT
dft efpga scan clk
input
scan_clk
DFT
32scan_rstn
dft_efoga_scan.rstn
input
DFT
lio_resetn
efpga_io_resetnl
用户自定义逻辑用10
34lioresetn
input
efpga_io_resetno
用户自定义逻辑用10
319 s2ccfo esync/7
35int fpga in
SYSC到eFPGA的保留配置
int fpga in
s2c_cfg_esync[6]
SYSC到eFPGA的保留配置
int fpga in
s2c_cfa_esync[5]
SYSC到eFPGA的保留配置
int fpga in
316|s2c_cfg_esync[4]
SYSC到eFPGA的保留配置



### 截图编号 4 (`../../interface_efpga/images/GameViewer_bCW62ClcKC.png`)

#### 【全页】

intfpga_out
47|cpld.pad_out[23]
eFPGA输出到PAD
508int fpga_out
cpld_pad out[22]
eFPGA输出到PAD
509lint fpga out
cpld pad_out[21]
eFPGA输出到PAD
510int fpga_out
cpld pad out[20]
eFPGA输出到PAD
511 int_fpga_out
cpld_pad_out[19]
eFPGA输出到PAD
512int_fpga_out
cpld_pad_out[18]
eFPGA输出到PAD
513int_fpga_out
cpld_pad out[17]
eFPGA输出到PAD
514int fpga out
cpld pad out[16]
eFPGA输出到PAD
515int_fpga_out
cpld_pad_out[15]
eFPGA输出到PAD
516lint_fpga_out
cpld_pad.out[14]
eFPGA输出到PAD
517int fpga_out
cpld_pad_out[13]
eFPGA输出到PAD
518int fpga out
cpld pad out[12]
eFPGA输出到PAD
519int_fpga_out
cpld_pad_outl11]
eFPGA输出到PAD
520int_fpga_out
cpld_pad_out[10]
eFPGA输出到PAD
521intfpga_out
cpld pad.out/9]
eFPGA输出到PAD
522lint fpga out
cpld pad out[8]
eFPGA输出到PAD
523intfpga_out
cpld_pad out7l
eFPGA输出到PAD
524 int_fpga_out
cpld_pad.out6]
eFPGA输出到PAD
525int_fpga_out
cpld_pad_out[5]
eFPGA输出到PAD
526lint fpga out
cpld pad out[4]
eFPGA输出到PAD
527lint fpga_out
cpld_pad_out[3]
eFPGA输出到PAD
528int_fpga_out
cpld_pad_out[2]
eFPGA输出到PAD
529int.fpga_out
cpld pad_out[1]
eFPGA输出到PAD
530 int fpga out
cpld padout[0]
eFPGA输出到PAD
531 int fpga_out
cpld_srpwm_fault[23]
eFPGA输出到SRPWM用于封波
532int_fpga_out
cpld_srpwm_fault[22]
eFPGA输出到SRPWM用于封波
533int.fpga_out
cpld_srpwm_fault[21]
eFPGA输出到SRPWM用于封波
534intfpga_out
cpldsrpwm_fault[20]
eFPGA输出到SRPWM用于封波
535lint fpga out
cpldsrpwm_fault[19]
eFPGA输出到SRPWM用于封波
536int_fpga_out
cpld_srpwm_fault[18]
eFPGA输出到SRPWM用于封波
537int fpga_out
cpld_srpwm_fault[17]
eFPGA输出到SRPWM用于封波
538int.fpga_out
cpld_srpwm_fault[16]
eFPGA输出到SRPWM用于封波
539int fpga out
cpldsrpwmfault[15]
eFPGA输出到SRPWM用于封波
540int_fpga_out
cpld_srpwm_fault[14]
eFPGA输出到SRPWM用于封波
541 int.fpga_out
cpld_srpwm_fault[13]
eFPGA输出到SRPWM用于封波
542int fpga_out
cpld_srpwm_fault[12]
eFPGA输出到SRPWM用于封波



### 截图编号 5 (`../../interface_efpga/images/GameViewer_cU12ydgZ8V.png`)

#### 【全页】

int_fpga_in
315|s2c_cfa_esvnc[3]
SYSC到eFPGA的保留配置
lint fpga in
314|s2c_cfg_esync/2]
SYSC到eFPGA的保留配置
313|s2c_cf_esync[1]
lint_fpga_in
SYSC到eFPGA的保留配置
312 s2c.cfg esync[0]
int fpga in
SYSC到eFPGA的保留配置
lint fpga in
311|pad_cpld.in_esync[35]
PAD直接输入eFPGA
310|pad_cpld in_esync[34]
int_fpgain
PAD直接输入eFPGA
int fpga in
pad_cpldin_esync[33]
PAD直接输入eFPGA
308 padcpldinesync[32]
int fpga in
PAD直接输入eFPGA
int fpga in
pad_cpld_in_esync[31]
PAD直接输入eFPGA
lint fpgain
pad_cpld_in_esync[30]
PAD直接输入eFPGA
int fpga in
pad_cpld.in.esync29]
PAD直接输入eFPGA
304padcpld in esync[28]
int fpga in
PAD直接输入eFPGA
int fpga in
pad.cpld.in_esync[27]
PAD直接输入eFPGA
int fpga_in
pad_cpld.in_esync[26]
PAD直接输入eFPGA
lint fpga in
pad_cpld_in_esync[25]
PAD直接输入eFPGA
int fpga in
pad.cpld in esync[24]
PAD直接输入eFPGA
int fpga_in
pad_cpldin_esync[23]
PAD直接输入eFPGA
lint.fpga_in
pad_cpld_in_esync[22]
PAD直接输入eFPGA
int fpga in
pad_cpld.in_esyncl21]
PAD直接输入eFPGA
int fpga in
pad.cpldin_esync[20]
PAD直接输入eFPGA
int fpga in
pad_cpld_in_esync[19]
PAD直接输入eFPGA
int_fpga_in
pad_cpld.in_esync[18]
PAD直接输入eFPGA
int fpga in
pad_cpld_in_esync[17]
PAD直接输入eFPGA
292 pad.cpld in esync[16]
int fpga in
PAD直接输入eFPGA
intfpga in
291|pad_cpldin_esync[15]
PAD直接输入eFPGA
lint_fpga_in
pad_cpld_in_esync[14]
PAD直接输入eFPGA
int fpga in
289 pad.cpld in_esync[13]
PAD直接输入eFPGA
288pad cpld in esync[12]
lint fpga in
PAD直接输入eFPGA
int fpga in
287 pad cpld in esync[11]
PAD直接输入eFPGA
lint_fpga_in
pad_cpld.in_esync[10]
PAD直接输入eFPGA
int fpga in
285pad.cpld.in_esync/91
PAD直接输入eFPGA
int fpga in
284pad cpld in_esync[8]
PAD直接输入eFPGA
283padcpld.inesync71
int foga in
PAD直接输入eFPGA
282 pad_cpld.in_esync[6]
int_fpga_in
PAD直接输入eFPGA
3lint_fpga_in
281pad_.cpld.in_esync[5]
PAD直接输入eFPGA
74lint foga in
280pad.cpld.in_esync[4]
PAD直接输入eFPGA



### 截图编号 6 (`../../interface_efpga/images/GameViewer_grCDK0KTgW.png`)

#### 【全页】

255lint.fpga_in
99|cfa_efpga1_esync[9]
eFPGA保留配置接口，与总线交互
256int.fpgain
98 cfg_efpgal_esync[8]
eFPGA保留配置接口，与总线交互
257int fpga in
97cfg_efpgal_esync/7]
eFPGA保留配置接口，与总线交互
258 int fpga in
96cfg efpgal esync[6]
eFPGA保留配置接口，与总线交互
259 int.fpga in
95cfg_efpga1_esync[5]
eFPGA保留配置接口，与总线交互
260int.fpga in
94cfg_efpga1_esync[4]
eFPGA保留配置接口，与总线交互
261 int fpga in
93|cfo_efpgal_esync[3]
eFPGA保留配置接口，与总线交互
262lint fpga in
92 cfg efpga1 esync[2]
eFPGA保留配置接口，与总线交互
263int.fpga_in
91 cfg_efpga1_esync[]
eFPGA保留配置接口，与总线交互
90|cfg_efpgal_esync[0]
264lint_fpga_in
eFPGA保留配置接口，与总线交互
265 int fpga.in
89cfg_efpga0_esync[31]
eFPGA保留配置接口，与总线交互
266lint fpgain
88cfg_efpga0esync[30]
eFPGA保留配置接口，与总线交互
87|cfg_efpga0_esync[29]
267lint_fpga_in
eFPGA保留配置接口，与总线交互
268 int.fpga.in
86|cfq_efpga0_esync[28]
eFPGA保留配置接口，与总线交互
269lint_fpga.in
85|cfg_efpga0_esync[27]
eFPGA保留配置接口，与总线交互
270 int fpga in
84cfg efpga0 esync[26]
eFPGA保留配置接口，与总线交互
271int_fpga in
83cfo.efoga0_esync[25]
eFPGA保留配置接口，与总线交互
272 int_fpga.in
82|cfg_efpga0_esync[24]
eFPGA保留配置接口，与总线交互
273int_fpga_in
81|cfg_efpga0_esync[23]
eFPGA保留配置接口，与总线交互
274lint fpga in
80 cfg.efpga0 esync[22]
eFPGA保留配置接口，与总线交互
79cfg_efpga0 esync[21]
275int fpga in
eFPGA保留配置接口，与总线交互
276int_fpga.in
78|cfg_efpga0_esync[20]
eFPGA保留配置接口，与总线交互
77|cfq_efpga0_esync[19]
int_fpga in
eFPGA保留配置接口，
与总线交互
278 lint fpga in
76 cfg_efpga0 esync[18]
eFPGA保留配置接口，
与总线交互
279 int fpga in
75 cfg_efpga0 esync[17]
eFPGA保留配置接口，与总线交互
74|cfg_efpga0_esync[16]
280int_fpga_in
eFPGA保留配置接口，与总线交互
73|cfa_efpga0_esync[15]
int_fpga in
eFPGA保留配置接口，与总线交互
282int fpga in
72|cfg_efpga0_esync[14]
eFPGA保留配置接口，与总线交互
71 cfa efpga0 esync[13]
283int fpga in
eFPGA保留配置接口，与总线交互
70|cfa_efpga0_esync[12]
284int_fpga_in
eFPGA保留配置接口，与总线交互
285int_fpga.in
69|cfg_efpga0_esync[11]
eFPGA保留配置接口，与总线交互
286 int fpga.in
68cfg_efpga0_esync[10]
eFPGA保留配置接口，与总线交互
287 int fpga in
67cfg efpga0 esync[9]
eFPGA保留配置接口，与总线交互
288 int.fpgain
66|cfa_efpga0_esync[8]
eFPGA保留配置接口，与总线交互
289lint.fpga in
65cfg_efpga0_esync7]
eFPGA保留配置接口，与总线交互
290int.fpga in
64|cfa_efpga0_esync[6]
eFPGA保留配置接口，与总线交互



### 截图编号 7 (`../../interface_efpga/images/GameViewer_gvjimz0mF4.png`)

#### 【全页】

435int_fpga_qut
efpga1_rpt[13]
eFPGA保留上报接口，与总线交互
436lint.fpga.ou
efpga1_rpt[12]
eFPGA保留上报接口，与总线交互
437int_fpgaout
efpgal_rpt[11]
eFPGA保留上报接口，与总线交互
438int fpga out
efpgal rpt[10]
eFPGA保留上报接口，与总线交互
439lint_fpga_out
efpgal_rpt[9]
eFPGA保留上报接口，与总线交互
440int_fpga_.out
efpgal_rpt[8]
eFPGA保留上报接口，与总线交互
441intfpga_out
efpgal_rpt[7]
eFPGA保留上报接口，与总线交互
442int fpga out
efpgal rpt[6]
eFPGA保留上报接口，与总线交互
443int_fpga_out
efpgal_rpt[5]
eFPGA保留上报接口，与总线交互
444lint_fpga_out
efpgal_rpt[4]
eFPGA保留上报接口，与总线交互
445intfpgaout
efpgal_rpt[3]
eFPGA保留上报接口，与总线交互
446int fpgaout
efpgal rpt[2]
eFPGA保留上报接口，与总线交互
447int_fpga_out
efpgal_rpt[1]
eFPGA保留上报接口，与总线交互
448int.fpga_out
efpgal_rpt[0]
eFPGA保留上报接口，与总线交互
449intfpga.out
cpld_opxb_data[9]
eFPGA输出到OUTPUTXBAR
450int fpgaout
cpldopxb_data[8]
eFPGA输出到OUTPUTXBAR
451 lint_fpga_out
cpldopxbdata7
eFPGA输出到OUTPUTXBAR
452lint_fpga_out
cpld_opxb_data[6]
eFPGA输出到OUTPUTXBAR
453intfpga_out
cpld_opxb_data[5]
eFPGA输出到OUTPUTXBAR
454int fpga out
cpld_opxb_data[4]
eFPGA输出到OUTPUTXBAR
output
455int fpga_out
cpld_opxb_data[3]
eFPGA输出到OUTPUTXBAR
456int_fpga_out
cpld._opxb_data[2]
eFPGA输出到OUTPUTXBAR
457int_fpga_out
cpld_opxb_data[1]
eFPGA输出到OUTPUTXBAR
458int fpgaout
cpld_opxb_data[0]
eFPGA输出到OUTPUTXBAR
459intfpga_out
cpld_pad_oen[35]
eFPGA输出到PADOEN
460lint_fpga_out
cpld_pad_oen[34]
eFPGA输出到PAD_OEN
461int_fpga_out
cpld_pad_oen[33]
eFPGA输出到PAD.OEN
462int fpga.out
cpldpad_oen[32]
eFPGA输出到PAD.OEN
463intfpga_out
cpldpadoen[31]
eFPGA输出到PADOEN
464 int_fpga_out
cpld_pad_oen[30]
eFPGA输出到PAD.OEN
465int_fpga.out
cpld.pad_oen[29]
eFPGA输出到PAD.OEN
466intfpga_out
cpld.pad_oen[28]
eFPGA输出到PADOEN
467int fpgaout
cpldpadoen[27]
eFPGA输出到PADOEN
468int_fpga_out
cpld_pad_oen[26]
eFPGA输出到PAD_OEN
469int_fpga_out
cpld_pad_oen[25]
eFPGA输出到PAD.OEN
470intfpga_out
cpldpad_oen[24]
eFPGA输出到PAD_OEN



### 截图编号 8 (`../../interface_efpga/images/GameViewer_I7FEkY4HxN.png`)

#### 【全页】

399int_fpga_out
155|efpqa0_rpt[17]
eFPGA保留上报接口，与总线交互
400int_fpga.out
154efpga0_rpt[16]
eFPGA保留上报接口，与总线交互
401lint_fpga_out
153|efpga0_rpt[15]
eFPGA保留上报接口，与总线交互
152efpga0rpt[14]
402intfpga_out
eFPGA保留上报接口，与总线交互
403int.fpga_out
151efpga0_rpt[13]
eFPGA保留上报接口，与总线交互
404intfpga.out
150 efpga0_rpt[12]
eFPGA保留上报接口，与总线交互
149efpga0_rpt[11]
405int_fpga_out
eFPGA保留上报接口，与总线交互
148efpga0 rpt[10]
406intfpgaout
eFPGA保留上报接口，与总线交互
407int._fpga.out
efoga0_rpt9]
eFPGA保留上报接口，与总线交互
408intfpga_out
146 efpga0_rpt[8]
eFPGA保留上报接口，与总线交互
145efpgaorot/7
409 int fpga_out
eFPGA保留上报接口，与总线交互
410int fpgaout
144efpga0 rpt[6]
eFPGA保留上报接口，与总线交互
411int.fpga_out
143efoga0_rpt[5]
eFPGA保留上报接口，与总线交互
412int_fpga_out
142efpga0_rpt[4]
eFPGA保留上报接口，与总线交互
413int_fpga.out
141efpga0rpt[3]
eFPGA保留上报接口，与总线交互
414intfpga out
140 efpga0 rpt[2]
eFPGA保留上报接口，与总线交互
415int fpga out
efpgao_.rpt[1]
eFPGA保留上报接口，与总线交互
416int_fpga_out
efpga0_rpt[0]
eFPGA保留上报接口，与总线交互
137efpgal rpt/31]
417int_fpga_out
eFPGA保留上报接口，与总线交互
418 int fpga out
136efpgal rpt[30]
eFPGA保留上报接口，与总线交互
135|efpga1_rpt[29]
419 int fpga_out
eFPGA保留上报接口，与总线交互
134efpgal_rpt[28]
420int.fpga_out
eFPGA保留上报接口，与总线交互
421int.fpga_out
133efpgal_rpt/27]
eFPGA保留上报接口，与总线交互
422lint fpga out
132efpgal rpt26]
eFPGA保留上报接口，与总线交互
423int.fpga out
131efpga1_rpt[25]
eFPGA保留上报接口，与总线交互
424int_fpga_out
efpgal_rpt[24]
eFPGA保留上报接口，与总线交互
425int fpga._out
efpgal_rpt[23]
eFPGA保留上报接口，与总线交互
128efpgal rpt/22]
426intfpga_out
eFPGA保留上报接口，与总线交互
427lint fpga out
efpgal_rpt[21]
eFPGA保留上报接口，与总线交互
428int_fpga_out
efpgal_rpt[20]
eFPGA保留上报接口，与总线交互
125|efpgal_rpt[19]
429int_fpga_out
eFPGA保留上报接口，与总线交互
430int_fpgaout
124|efpga1_rpt[18]
eFPGA保留上报接口，与总线交互
123efpgal rot(17]
431int fpga out
eFPGA保留上报接口，与总线交互
432int_fpga_out
efpgal_rpt[16]
eFPGA保留上报接口，与总线交互
433int_fpga_out
efpgal_rpt[15]
eFPGA保留上报接口，与总线交互
434lint_fpga_out
120|efpga1_rpt[14]
eFPGA保留上报接口，与总线交互



### 截图编号 9 (`../../interface_efpga/images/GameViewer_J6lAwKnIhm.png`)

#### 【全页】

int foga in
243|inxb_cpld_data_esync[6]
INPUTXBAR数据
112int fpga.in
242|inxb.cpld_data_esync[5]
INPUTXBAR数据
241linxb_cpld_data esync4]
113int fpgain
INPUTXBAR数据
114int fpga in
240inxb.cpld dataesync[3]
INPUTXBAR数据
115int_fpga_in
239 inxb_cpld_data_esync[2]
INPUTXBAR数据
116int_fpga_in
238inxb_cpld_data_esync[1]
INPUTXBAR数据
117int fpga in
237 inxb.cpld_data_esync[0]
INPUTXBAR数据
118 int fpga in
236 pfxb cpld dataesync[10]
PWMXBAR数据
119int.fpgain
235pfxb_cpld_data esync[9]
PWMXBAR数据
120 int_fpga_in
234pfxb.cpld.data_esyncl8
PWMXBAR数据
121int.fpgain
233pfxb.cplddata_esync71
PWMXBAR数据
122int fpga in
232pfxb cpld dataesync[6]
PWMXBAR数据
123int.fpgain
231pfxb.cplddataesync15]
PWMXBAR数据
124intfpga in
230pfxb_cpld_data_esync[4]
PWMXBAR数据
int fpga in
pfxb_cpld_data_esync3]
PWMXBAR数据
126 int fpga in
pfxbcplddata esync[2]
PWMXBAR数据
127 lint fpga_in
pfxb.cpld_data_esync[1]
PWMXBAR数据
128int_fpga_in
pfxb_cpld_data_esyncl0]
PWMXBAR数据
129 int fpga in
etxb_cpld_data_esync[9]
PWMXBAR数据
130 int fpga in
etxb.cplddata esync[8]
PWMXBAR数据
etxb.cplddata_esync7
131int fpga_in
PWMXBAR数据
132int_fpga_in
etxb_cpld_data_esync[6]
PWMXBAR数据
133int_fpgain
etxb.cpld_data_esyncl5]
PWMXBAR数据
134int fpga in
etxb_cpld_data_esync[4]
PWMXBAR数据
etxbcplddata_esync[3]
135intfpga_in
PWMXBAR数据
136int_fpga_in
etxb_cpld_data_esyncl2]
PWMXBAR数据
137lint.fpga.in
etxb.cpld_data_esync[1]
PWMXBAR数据
138 int fpga in
etxb.cpld_data_esyncl0]
PWMXBAR数据
int foga in
etim.cpldsyncesync
ETIMPWM相位同步信号
140 lint fpga_in
cmpc_cpld_evth_esync[10]
CMPCH事件
lint fpga in
cmpc_cpld_evth_esync[9]
CMPCH事件
142int fpga in
cmpc.cpld_evth_esync[8]
CMPCH事件
143 int foga in
cmpc.cpldevthesync7
CMPCH事件
144int_fpga_in
cmpc_cpld_evth_esync[6]
CMPCH事件
145lint.fpga.in
cmpc_cpld_evth_esync[5]
CMPCH事件
208cmpc.cpld_evth.esync[4]
146int.fpga.in
CMPCH事件



### 截图编号 10 (`../../interface_efpga/images/GameViewer_Nbjags3WBm.png`)

#### 【全页】

147lint_fopqa_in
207|cmpc_cpld_evth_esync[3]
CMPCH事件
148int_fpga in
206cmpc.cpld_evth_esync[2]
CMPCH事件
205cmpc_cpld_evth.esync[1]
149int fpga in
CMPCH事件
150int fpga in
204cmpccpld evthesync[0]
CMPCH事件
151lint_fpga in
cmpc_cpld_evtl_esync[10]
CMPCL事件
152 lint.fpga_in
cmpc_cpld_evtl.esync[9]
CMPCL事件
153int fpga in
cmpc_cpld_evtl_esync[8]
CMPCL事件
154 int foga in
cmpccpldevtlesync7l
CMPCL事件
155int_fpga_in
cmpc_cpld_evtl_esync[6]
CMPCL事件
156int.fpga_in
cmpc_cpld_evtl_esync[5]
CMPCL事件
157lint fpga in
cmpc_cpld_evtlesync[4]
CMPCL事件
158 int fpga in
cmpccpldevtlesync[3]
CMPCL事件
159lint_fpga in
cmpc_cpld_evtl_esync[2]
CMPCL事件
160int.fpga_in
cmpc.cpld_evtl_esync[]]
CMPCL事件
161int fpga in
cmpc_cpld_evtl_esync[0]
CMPCL事件
162int fpga in
adc0_cpldevtl esync[15]
ADCL事件
163int_fpga_in
adc0_cpld_evtl_esync[14]
ADCL事件
164int_fpga in
adc0_cpld_evtl_esync[13]
ADCL事件
165int.fpga_in
adc0_cpld_evtl_esync[12]
ADCL事件
166int fpga in
adc0_cpld evtl esync[11]
ADCL事件
167lint fpgain
adc0_cpld_evtl_esync[10]
ADCL事件
adc0_.cpld_evtl_esync[9]
168int_fpga_in
ADCL事件
169lint fpga in
adco.cpld_evtl esync[8]
ADCL事件
170lint fpgain
adco_.cpld_evtl._esync[7]
ADCL事件
171 lint fpga in
adco cpld _evtl esync[6]
ADCL事件
172 lint_fpga_in
adc0_cpld_evtl_esync[5]
ADCL事件
173int_fpga.in
adc0_cpld_evtl_esync[4]
ADCL事件
174lint fpga in
adco_cpld_evtl_esync[3]
ADCL事件
175intfpgain
adcocpld evtl esync[2]
ADCL事件
176int_fpgain
adco_cpld_evtl_esync[1]
ADCL事件
177int fpga in
adco_.cpld_evtl_esync[0]
ADCL事件
178intfpgain
adc0_cpld_evth_esync[15]
ADCH事件
179 int fpga in
adc0cpldevth_esync[14]
ADCH事件
adc0_cpld_evth_esync[13]
180int.fpga_in
ADCH事件
181 int_fpga_in
adc0_cpld_evth_esync[12]
ADCH事件
182int fpga in
adc0_.cpld_evth_esync[11]
ADCH事件



### 截图编号 11 (`../../interface_efpga/images/GameViewer_P0NFLfV564.png`)

#### 【全页】

int foga in
27|srpwm_cpld_pwmb_oen_esync[6]
SRPWMPWM_OEN
srpwm_cpld_pwma_oen_esync[6]
int fpgain
SRPWM PWM_OEN
int fpga in
srpwm_.cpld.pwm_b_esync[6]
SRPWM PWM
330 int fpga in
srpwm_cpldpwma_esync[6]
SRPWM PWM
331int fpga in
srpwm_cpld_pwmb_oen_esync[5]
SRPWM PWM_OEN
332 lint fpga.in
srpwm_cpld_pwma_oen_esync[5]
SRPWM PWM_OEN
333lint.fpgain
srpwm_cpld.pwmb_esync[5]
SRPWM PWM
334 int fpga in
srpwmcpldpwmaesync[5]
SRPWM PWM
lint fpga in
srpwm_cpld_pwmb_oen_esync[4]
SRPWM PWM_OEN
int_fpga_in
srpwm_cpld
_pwma_oen_esync[4]
SRPWMPWM_OEN
int fpga in
srpwm_cpld_pwm.b_esync[4]
SRPWM PWM
int fpga in
srpwmcpldpwm_a.esync[4]
SRPWM PWM
intfpga in
srpwm_cpld.pwmb_oen_esync[3]
SRPWM PWM_OEN
intfpgain
srpwm_cpld_pwma_oen_esync[3]
SRPWM PWM_OEN
intfpga in
srpwm_cpld_pwm_b_esync[3]
SRPWM PWM
int fpga in
srpwmcpldpwmaesync[3]
SRPWM PWM
343 int fpga in
srpwm_cpld_pwmb_oen_esync[2]
SRPWM PWM OEN
344int fpga in
srpwm_cpld_pwma_oen_esync[2]
SRPWM PWM_OEN
345int.fpga.in
srpwm_cpld_pwm_b_esync2]
SRPWM PWM
int fpga in
srpwm_.cpld.pwm_a_esync[2]
SRPWM PWM
lint fpga in
srpwm_cpld_pwmb_oen_esync[1]
SRPWM PWM_OEN
int_fpga_in
srpwm_cpld_pwma_oen_esync[1]
SRPWM PWM_OEN
lintfpga in
srpwm_cpld.pwm_b_esync[1]
SRPWM PWM
lint fpga in
srpwm_.cpld.pwm_a_esync[1]
SRPWM PWM
intfpga in
srpwm_cpld_pwmb_oen_esync[0]
SRPWMPWMOEN
int fpga in
srpwm_cpld_pwma_oen_esync[0]
SRPWM PWM_OEN
353int.fpga.in
srpwm_cpld_pwm_b_esync[0]
SRPWM PWM
354int_fpga.in
srpwm_cpld_pwm_a_esync[0]
SRPWM PWM
355int fpgaout
ppi data out[11]
PPI
356int_fpga_out
ppi_data_out[10]
PPI
357lint_fpga_out
ppi_data_out[9]
PPI
358intfpgaout
ppi data_out8]
PPI
359int fpga out
ppi data out7
PPI
360int_fpga_out
ppi_data_out[6]
PPI
361int_fpga_out
ppi_data_out[5]
PPI
362int fpga_out
192 ppi data out[4]
PPI



### 截图编号 12 (`../../interface_efpga/images/GameViewer_qhGTBAxdTy.png`)

#### 【全页】

543int_fpaa_out
11|cpldsrpwm_fault/11
eFPGA输出到SRPWM用于封波
10|cpld_srpwm_fault[10]
544int_fpga_out
eFPGA
输出到SRPWM用于封波
9cpld_srpwm_fault[9]
545int_fpga_out
eFPGA
输出到SRPWM用于封波
546int_fpga_out
8cpld_srpwm_fault[8]
eFPGA输出到SRPWM用于封波
7|cpld_srpwm_fault[7]
547int_fpga_out
eFPGA输出到SRPWM用于封波
6cpld_srpwm_fault[6]
548int_fpga_out
eFPGA输出到SRPWM用于封波
5cpld_srpwm_fault[5]
549int_fpga_out
eFPGA
输出到SRPWM用于封波
4cpld_srpwm_fault[4]
eFPGA
550intfpga_out
输出到SRPWM用于封波
551int_fpga_out
3|cpld_srpwm_fault[3]
eFPGA输出到SRPWM用于封波
2|cpld_srpwm_fault[2]
552intfpgaout
eFPGA输出到SRPWM用于封波
1cpld_srpwm_fault[1]
553int_fpga_out
eFPGA输出到SRPWM用于封波
554int_fpga_out
O0cpld_srpwm_fault[0]
eFPGA
输出到SRPWM用于封波



### 截图编号 13 (`../../interface_efpga/images/GameViewer_S8SQhpMWC2.png`)

#### 【全页】

219lint.foga_in
135|adc1_cpld_evth_esync[6]
ADCH事件
220lint_fpga in
adc1_cpldevth_esync[5]
ADCH事件
221 int fpga in
adc1_cpld_evth_esync[4]
ADCH事件
222int fpga in
adc1 cpldevth_esync[3]
ADCH事件
223 int fpga in
adc1_cpldevth_esync[2]
ADCH事件
224 lint_fpgain
adc1_cpld_evth_esync[]]
ADCH事件
225int.fpgain
adc1_cpld_evth_esync[0]
ADCH事件
226int fpga in
cpuolockupesync
CPU挂死
227int_fpga in
cpul_lockup_esync
CPU挂死
228 int fpga in
bus_timeout_esync
总线超时
229 int fpga in
temp_warn_esync
过温告警
230 int fpga in
powererresync
过流
231 int fpga in
por_uv_warn_esync
次压
232lint fpga in
por_ov_warn_esync
过压
233lint.fpgain
cfg_efpga1_esync(31]
eFPGA保留配置接口，与总线交互
234 int fpga in
cfa._efpgal_esync[30]
eFPGA保留配置接口，与总线交互
235int fpga in
cfg_efpga1_esync[29]
eFPGA保留配置接口，与总线交互
236int.fpgain
cfg_efpga1_esync28]
eFPGA保留配置接口，与总线交互
237lint_fpga in
cfq_efpga1_esync27]
eFPGA保留配置接口，与总线交互
238 int fpga in
cfg_efpgal_esync[26]
eFPGA保留配置接口，与总线交互
239 int fpga in
cfg_efpgal_esync[25]
eFPGA保留配置接口，与总线交互
240 int fpga in
cfg_efpgal_esync[24]
eFPGA保留配置接口，与总线交互
241 int fpga in
cfg_efpga1_esync[23]
eFPGA保留配置接口，与总线交互
242lint fpga in
cfg_efpgal esync[22]
eFPGA保留配置接口，与总线交互
243lint fpga in
cfg_efpga1 _esync[21]
eFPGA保留配置接口，与总线交互
244 int.fpgain
cfg_efpga1_esync[20]
eFPGA保留配置接口，与总线交互
245 int fpga in
cfg_efpga1._esync[19]
eFPGA保留配置接口，与总线交互
246int.fpga in
cfg_efpga1_esync[18]
eFPGA保留配置接口，与总线交互
247int fpgain
cfg efpga1 esync[17]
eFPGA保留配置接口，与总线交互
248 int_fpga_in
cfg_efpga1_esync[16]
eFPGA保留配置接口，与总线交互
249 int_fpga in
cfg_efpga1_esync[15]
eFPGA保留配置接口，与总线交互
250 lint_fpga in
cfg_efpga1_esync[14]
eFPGA保留配置接口，与总线交互
251int fpga in
cfg efpgal esync[13]
eFPGA保留配置接口，与总线交互
252int_fpga in
cfg_efpga1_esync[12]
eFPGA保留配置接口，与总线交互
253 int_fpga in
cfg_efpga1_esync[1]]
eFPGA保留配置接口，与总线交互
254lint_fpgain
cfg_efpga1_esync[10]
eFPGA保留配置接口，与总线交互



### 截图编号 14 (`../../interface_efpga/images/GameViewer_uxeRXbUM3q.png`)

#### 【全页】

291int.foga_in
63|cfg_efpga0_esync[5]
eFPGA保留配置接口，与总线交互
292int_fpga in
cfg_efpga0_esync[4]
eFPGA保留配置接口，与总线交互
293int fpga in
61|cfq_efpga0_esync[3]
eFPGA保留配置接口，与总线交互
294 int fpga in
60 cfg efpga0 esync[2]
eFPGA保留配置接口，与总线交互
59|cfq_efpga0_esync[1]
295int_fpga_in
eFPGA保留配置接口，与总线交互
58|cfg_efpga0_esync[0]
296int.fpga_in
eFPGA保留配置接口，与总线交互
297lint.fpga in
etim_cpld_pwm_esync[9]
ETIM PWM
etim.cpldpwmesync[8]
298 int fpga in
ETIM PWM
299 lint.fpga in
etim.cpld.pwm.esync7
ETIM PWM
300lint_fpga.in
etim_cpld_pwm_esync[6]
ETIM PWM
301 int fpga in
etim_cpld_pwm._esync[5]
ETIM PWM
302lint fpga in
etim.cpldpwm.esync[4]
ETIMPWM
303 intfpgain
etim_cpld_pwm_esync[3]
ETIM PWM
304 int_fpga.in
etim_cpld_pwm_esync[2]
ETIM PWM
etim.cpld.pwm_esyncl1]
305int_fpga in
ETIM PWM
306 int fpga in
etim.cpld_pwm.esync[0]
ETIM PWM
307lint fpga in
srpwm_cpld_pwmb_oen_esync[11]
SRPWMPWM OEN
308 int+ga.in
srpwm_cpld_pwma_oen_esync[11]
SRPWM PWM_OEN
309int_fpga.in
srpwm_cpld._pwm_b_esync[11]
SRPWM PWM
310 int fpga in
srpwm_cpld.pwm_a_esync[11]
SRPWM PWM
311 int fpga in
srpwm_cpld_pwmb_oen_esync[10]
SRPWMPWM_OEN
312int_fpga_in
srpwm_cpld_pwma_oen_esync[10]
SRPWM PWM_OEN
313int fpga in
srpwm_cpld_pwm_b_esync[10]
SRPWMPWM
314 int fpga in
srpwm_cpld.pwm_a_esync[10]
SRPWM PWM
315int fpga in
srpwm_cpld_pwmb_oen_esync[9]
SRPWM PWM_OEN
316int_fpga_in
srpwm_cpld_pwma_oen_esync[9]
SRPWM PWM_OEN
317lint_fpga.in
srpwm_cpld_pwm_b_esync[9]
SRPWM PWM
318 int fpga in
srpwm_.cpld.pwm_a_esync[9]
SRPWM PWM
319 int fpga in
srpwm_cpld_pwmb_oen_esync[8]
SRPWM PWM_OEN
320 int_fpga.in
srpwm_cpld_pwma_oen_esync[8]
SRPWMPWM_OEN
321 int. fpga.in
srpwm_cpld_pwm_b_esync[8]
SRPWM PWM
322int fpga in
srpwm_.cpld.pwm_a_esync[8]
SRPWM PWM
323int fpga in
srpwmcpldpwmboenesync[7]
SRPWM PWM OEN
324int_fpga_in
srpwm_cpld_pwma_oen_esync7l
SRPWM PWM_OEN
325lint.fpga.in
srpwm_cpld.pwm.b_esync7l
SRPWM PWM
326int.fpgain
srpwm_.cpld_pwm_a_esync7l
SRPWM PWM



### 截图编号 15 (`../../interface_efpga/images/GameViewer_Vhor9olOSG.png`)

#### 【全页】

5int_fpga_in
279pad_cpld_in_esync[3]
PAD直接输入eFPGA
76lint fpga in
278pad.cpld in_esync[2]
PAD直接输入eFPGA
int foga in
277 pad.cpld in esync[1]
PAD直接输入eFPGA
78 int fopga in
pad_cpld inesync[0]
PAD直接输入eFPGA
sochard.rstn_esync
lint_fpga_in
SOCHARD复位
int fpga in
soc_wdgo_rst.n_esync
SOC看门狗复位
int fpga in
socwdalrstn esync
SOC看门狗复位
int foga in
soc soft rst n esync
SOC软复位
cpld_plllos_status_esync
int_fpga_in
CPLDPLL频率状态，1'b1:无时钟或频率异常
int.fpgain
ppi_csn
PPI
int fpga in
ppi_data_bus_esync[11]
PPI
int fpga in
ppi data busesync[10]
PPL
intfpga in
ppi.data_bus esync9]
PPI
lint.fpga_in
266|ppi_data_bus_esync[8]
PPI
int fpga in
ppidata_bus_esync7
PPL
264ppi data bus esync[6]
int fpga in
PPL
int fpga in
ppi data_bus esync[5]
PPI
intfpga in
ppi_data_bus_esync[4]
PPI
int_fpga in
ppi_data_bus_esync[3]
PPI
int fpga in
ppi databusesync[2]
PPI
int foga in
ppidata_bus_esync[1]
PPI
int fpga in
ppi_data_bus_esyncl0]
PPI
lint fpga_in
ppi_addr_esync/4]
PPI
98 int fpga in
ppiaddresync[3]
PPI
99 int fpga in
ppiaddr_esync[2]
PPI
254ppi_addr_esync[1]
100 int_fpga_in
PPL
101 intfpga.in
ppi_addresync0]
PPI
102int fpga in
inxb_cpld_data_esync[15]
INPUTXBAR数据
103 int foga in
inxbcplddataesync[14]
INPUTXBAR数据
104int.fpga_in
inxb_cpld_data_esync[13]
INPUTXBAR数据
105int.fpga.in
inxb_cpld_data_esync[12]
INPUTXBAR数据
106intfpgain
248inxb cplddata_esync[11]
INPUTXBAR数据
107int fpga in
247inxb cpld data esync[10]
INPUTXBAR数据
108int_fpga_in
246inxb_cpld_data_esync[9]
INPUTXBAR数据
109 int fpga.in
245inxb_cpld_data_esync[8]
INPUTXBAR数据
110 int foga.in
244inxb.cpld_data_esync/7]
INPUTXBAR数据



### 截图编号 16 (`../../interface_efpga/images/GameViewer_xPU5bUtZ6p.png`)

#### 【全页】

183int fpaa_in
adc0_cpld_evth_esync[10]
ADCH事件
184lint_fpga in
adc0_cpld_evth_esync(9]
ADCH事件
185lint fpga in
adco_cpld_evth_esync[8]
ADCH事件
186int fpga in
adco.cpld evth_esync[7]
ADCH事件
187intfpga in
adco_cpld_evth_esync[6]
ADCH事件
188int fpgain
adc0_cpld_evth_esync[5]
ADC H事件
189int.fpga.in
adc0_cpld_evth_esync[4]
ADC H事件
190lint fpga in
adco cpld evthesync[3]
ADCH事件
191int_fpgain
adc0_cpld_evth_esync[2]
ADCH事件
192int_fpga in
adco_cpld_evth_esync[1]]
ADCH事件
193 lint fpga_in
adco_cpld evth_esync[0]
ADCH事件
194 int fpga in
adc1_cpld evtl esync[15]
input
ADCL事件
195int_fpga_in
adc1 cpld_evtl_esync[14]
ADCL事件
196int_fpgain
adc1_cpld_evtl_esync[13]
ADCL事件
197lint fpga in
adc1_cpld_evtl_esync[12]
ADCL事件
198 int fpga in
adc1_cpld_evtl esync[11]
ADCL事件
199lint.fpga in
adc1_cpld evtl_esync[10]
ADCL事件
200 int.fpga_in
adc1_.cpld_evtl.esync[9]
ADCL事件
201 lint.fpga_in
adc1_cpld_evtl_esync[8]
ADCL事件
202 int fpga in
adc1_cpldevtlesync[7]
ADCL事件
203int fpga in
adc1_cpld_evtl_esync[6]
ADCL事件
204 lint_fpga_in
adc1_cpld_evtl_esync[5]
ADCL事件
205int.fpga_in
adc1_cpld_evtl_esync[4]
ADCL事件
206int fpga in
adc1_cpld_evtl_esync[3]
ADCL事件
207lint fpga in
adc1_cpld_evtl_esync[2]
ADCL事件
208 int_fpgain
adc1_cpld_evtl_esync[1]
ADCL事件
209 int fpga in
adc1_cpldevtl.esync[0]
ADCL事件
adc1.cpld_evth_esync[15]
210 int fpga in
ADCH事件
211 int fpga in
adc1 cpld evth_esync[14]
ADCH事件
212lint_fpga in
adc1_cpld_evth_esync[13]
ADCH事件
213int_fpgain
adc1_cpldevth_esyncl12]
ADCH事件
214lint fpga in
adc1_cpld_evth_esync[11]
ADCH事件
215int fpga in
adc1 cpld evth esync[10]
ADCH事件
216int_fpga_in
adc1_cpld_evth_esync[9]
ADCH事件
217lint_fpga_in
adc1_cpld_evth_esync[8]
ADCH事件
218int.fpga.in
adc1_cpldevth_esync7]
ADCH事件

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
