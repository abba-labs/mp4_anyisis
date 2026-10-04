# CPLD - INTERFACE_EFPGA_CFG 设计与接口说明

> 提取说明：本文档由 AI Agent 严格按照原始截图提取，未作主观改动。
> 模糊或包含复杂波形处均已精确标明原截图文件索引。

---

## 第一部分：文档原始正文内容


### 截图编号 1 (`images/GameViewer_MLLzggVIdI.png`)

#### 【全页】

signal
inout
width
connectsig
sys_clk
input
1 efpga_sys_clk
sys_rstn
input
1 cpld_sys_rst_n
input
efpga_clk
1free_clko
efpga_rstn
input
cpld_fOesync_rst_n
cfg_efpga_mask_en
input
1cfg_efpga_mask_en
cfg_efpgao_enb
input
1cfg_efpga0_enb_nc
cfg_efpgao_val
input
32cfg_efpga0_val
cfg_efpga1_enb
input
1 cfg_efpga1_enb_nc
32cfg_efpga1_val
cfo_efpgal_val
input
cfg_efpga0_esync
output
32 cfg_efpga0_esync
cfg_efpga1_esync
output
32 cfg_efpga1_esync
efpga0_rpt
input
32efpga0_rpt
input
efpga1_rpt
32efpga1_rpt
output
efpga0_rpt_valin
32 efpga_rpt0_val_in
output
efpga1_rpt_val_in
32 efpga_rpt1_val_in
s2c_cfg_enb
input
1s2c_cfg_enb
s2c_cfg
input
32s2c_cfg
s2c_cfa_esync
output
32s2c_cfa_esync



---
## 第二部分：ET6601 专项修改点提取

> 经全页视觉文本检索，本组截图中未出现显式的 'ET6601' 特殊字色修改标注或修订记录文本，整体属于该模块标准基线配置。