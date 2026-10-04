# CPLD - CPLD_REG 设计与接口说明

> 提取说明：本文档由 AI Agent 严格按照原始截图提取，未作主观改动。
> 模糊或包含复杂波形处均已精确标明原截图文件索引。

---

## 第一部分：文档原始正文内容


### 截图编号 1 (`images/GameViewer_6BxAbFuaFj.png`)

#### 【全页】

Data_Width
Module Name
cpld cfg
32CFG IFAHB
新增域段
检查
新增寄存器
升级
Base_Addr
Addr_Width
Table/Register discription
Field discription
REG
field attribute
fileddefault
filed range
Regname
Discription
Fieldname
field discription
Field
offset addr
width
default value
Properties
s/W
H/W
P_reserved
Properties
value
每一bit对应相应通道：
CFG_ADCO_CPLD_EV
sel
1"b1：信号在soc时钟下展宽15
ro
TH_EXTEND
拍；
0-04-08·08
1' bo:bypass
每2bit对应相应通道：
第1bit:
1"bo：展宽后的信号；
huan.J3
CFG_ADCO_CPLD_EV
1"b1：异步处理后的信号；
sel
ro
第2bit：
TH_SYHC
1'b1：通过第1bit选择后的信
1'bo:bypassi
每2bit对应相应通道：
第1bit:
1"b0：展宽后的信号；
CFG_ADCO_CPLD_EV
sel
Ox000000Co
1"b1：异步处理后的信号；
ro
TH_EDGE
第2bit：
1"b1：通过第1bit选择后的信
号；
1'bo:bypass!
每一bit对应相应通道：
CFG_ADCO_CPLD_EV
sel
ro
1'b1：信号做打拍；
TH_PIPE
1'bo:bypass
每一bit对应相应通道：
CFG_ADCO_CPLD_EV
sel
1b1：信号在soc时钟下展宽15
ro
TL_EXTEND
拍；
1'bo:bypass
每2bit对应相应通道：
第1bit:
1"bo：展宽后的信号；
CFG_ADCO_CPLD_EV
sel
1"b1：异步处理后的信号；
ro
TL_SYNC
第2bit：
1"b1：通过第1bit选择后的信
1'bo:byassj



### 截图编号 2 (`images/GameViewer_ehusonHEeP.png`)

#### 【全页】

cpld cfg
Module Name
Data_Width
32CFGIFAHB
检查
新增寄存器
新增域段
升级
Base_Addr
Addr_Width
Table/Register discription
Field discription
REG
filed default
field attribute
Field name
filed range
Regname
width
field discription
Discription
offset addr
default value
Field
H/W
P_reserved
Properties
value
Properties
每2bit对应相应通道：
第1bit：
1"bo：展宽后的信号；
CFG_INXB_CPLD_DA
1'b1：异步处理后的信号；
76-10-04-07·59
sel
ro
TA_EDGE
第2bit：
1"b1：通过第1bit选择后的信
huan,
Tuan.Jj
buan.
1'bo:bypass;
CFG_INXB_CPLD_DA
每一bit对应相应通道：
sel
ro
1'b1：信号做打拍；
TA_PIPE
1'bo:bypass
每一bit对应相应通道：
CFG_PFXB_CPLD_DA
sel
1"b1：信号在soc时钟下展宽15
ro
TA_EXTEND
拍；
1'bo:bypass
每2bit对应相应通道：
第1bit：
1"bo：展宽后的信号；
Jhnan.Ji
nuan.Ji
CFG_PFXB_CPLD_DA
1"b1：异步处理后的信号；
sel
ro
TA_SYNC
第2bit：
1"b1：通过第1bit选择后的信
号；
1'bo:bypass]
每2bit对应相应通道：
第1bit:
1"bo：展宽后的信号；
CFG_PFXB_CPLD_DA
1"b1：异步处理后的信号；
sel
ro
TA_EDGE
第2bit:
huan.Ji 2026
huan.Ji
1"b1：通过第1bit选择后的信
号；
1'bo:bypass]
CFG_PFXB_CPLD_DA
每一bit对应相应通道：
sel
rv
ro
TA_PIPE
1"b1：信号做打拍；
1'bo:bypass



### 截图编号 3 (`images/GameViewer_er1i0CeSs6.png`)

#### 【全页】

ModuleName
cpld_cfg
Data_Width
32CFGIFAHB
新增域段
检查
新增寄存器
Base_Addr
Addr_Width
Table/Registerdiscription
Field discription
REG
field attribute
filed default
offset addr
filedrange
field discription
Regname
width
Fieldname
Discription
default value
Field
Properties
H/W
value
Properties
P_reserved
每一bit对应相应通道：
CFG_ETXB_CPLD_DA
sel
1"b1：信号在soc时钟下展宽15
ro
TA_EXTEND
拍；
1' bo:bypass
每2bit对应相应通道：
第1bit:
1"bo：展宽后的信号；
huan.Ji
huan.Ji
CFG_ETXB_CPLD_DA
1"b1：异步处理后的信号；
sel
ro
第2bit：
TA_SYNC
1'b1：通过第1bit选择后的信
1'bo:bypass;
每2bit对应相应通道：
第1bit：
1"bo：展宽后的信号；
CFG_ETXB_CPLD_DA
sel
1"b1：异步处理后的信号；
ro
TA_EDGE
第2bit：
1"b1：通过第1bit选择后的信
huan.Ji2
号：
1'bo:bypass]
CFG_ETXB_CPLD_DA
每一bit对应相应通道：
ro
sel
TA_PIPE
1'b1：信号做打拍；
1' bo:bypass
每一bit对应相应通道：
CFG_CIPC_CPLD_EV
1'b1：信号在soc时钟下展宽15
sel
ro
TH_EXTEND
拍；
i'bo:bypass
每2bit对应相应通道：
第1bit：
1"bo：展宽后的信号；
CFG_CIPC_CPLD_EV
sel
1"b1：异步处理后的信号；
ro
TH_SYNC
第2bit：
1"b1：通过第1bit选择后的信
号：
1'bo:bypass;



### 截图编号 4 (`images/GameViewer_Fi0vMedNfB.png`)

#### 【全页】

ModuleName
cpld_cfg
Data_Width
32CFG_IFAHB
检查
新增寄存器
新增域段
升级
Addr_Width
Base_Addr
Table/Registerdiscription
Field discription
REG
filed default
field attribute
Discription
filed range
field discription
Field
offset addr
width
Regname
Fieldname
default value
P_resen
Properties
s/W
H/W
value
Properties
val
CFG_EFPGAO
ro
eFPGA配置信号
val
CFG_EFPGA1
ro
eFPGA配置信号
eFPGA配置信号屏蔽使能
CFG_EFPGA_MASK
en
ro
1*b1：屏蔽配置信号
1“bo:配置正常输出
val
eFPGA上报信号
ox00000000
registere
EFPGA_RPTO
ro
d=false
eFPGA上报信号
val
EFPGA_RPT1
ro
registere
d=false
CFG_CPLD_PLL_LOS
1"b1：信号做异步处理；
sync_sel
STATUS
1'bo:bypass
CFG_SRPWM_CPLD_P
每一bit对应相应通道：
pipe_sel
rv
ro
1"b1：信号做打拍；
WI_A
1'bo:bypass
每一bit对应相应通道：
sync_sel
ro
1"b1：信号做异步处理；
1'bo:bypass
CFG_SRPWM_CPLD_P
每一bit对应相应通道：
1"b1：信号做打拍；
pipe_sel
ro
WI_B
1'bo:bypass.
每一bit对应相应通道：
sync_sel
ro
1'b1：信号做异步处理；
1'bo:bypass
CFG_SRPWM_CPLD_P
每一bit对应相应通道：
pipe_sel
ro
WIA_OEN
1"b1：信号做打拍；
1'bo:bypass
每一bit对应相应通道：
sync_sel
ro
1"b1：信号做异步处理；
1'bo:bypass
CFG_SRPWM_CPLD_P
每一bit对应相应通道：
pipe_sel
ro
1"b1：信号做打拍；
WIB_OEN
1' bo:bypass
每一bit对应相应通道：
sync_sel
ro
1"b1：信号做异步处理；
1'bo:byoass



### 截图编号 5 (`images/GameViewer_L2kHUqr7hq.png`)

#### 【全页】

cpld_cfg
Data_Width
ModuleName
32CFGIFAHB
检查
新增域段
新增寄存器
升级
Base_Addr
Addr_Width
Table/Registerdiscription
Field discription
field attribute
REG
filed default
filedrange
Reg name
width
field discription
Discription
offset addr
default value
Field name
Field
Properties
Properties
H/W
P_reserved
value
每一bit对应相应通道：
CFG_ADC1_CPLD_EV
sel
1b1：信号在soc时钟下展宽15
ro
TL_EXTEND
拍；
1'bo:bypass
每2bit对应相应通道：
第1bit：
1"bo：展宽后的信号；
huan
ouanJi
CFG_ADC1_CPLD_EV
sel
1"b1：异步处理后的信号；
第2bit：
TL_SYNC
1"b1：通过第1bit选择后的信
号；
1'bo:bypass;
每2bit对应相应通道：
第1bit
1"bo：展宽后的信号；
CFG_ADC1_CPLD_EV
sel
1"b1：异步处理后的信号；
0x000000F0
ro
TL_EDGE
第2bit：
1b1：通过第1bit选择后的信
号：
1'bo:bypassj
CFG_ADC1_CPLD_EV
每一bit对应相应通道：
0x000000F4
sel
ro
1"b1：信号做打拍；
TL_PIPE
1'bo:bypass
0x000000F8
PPI_BUS
dout
reserved
registere
10~04
ro
d=false
din
ro
PPI地址
addr
ro
PPI输入数据
PPI_FIFO
waterline
ro
reserved
wptr_rpt
ro
PPI写FIFO指针
full_rpt
ro
PPI写FIFO满信号
enpty_rpt
ro
wo
PPI写FIFO空信号



### 截图编号 6 (`images/GameViewer_lCjo9mFfHG.png`)

#### 【全页】

ModuleName
cpld cfg
Data_Width
32CFG_IFAHB
检查
新增寄存器
新增域段
升级
Base_Addr
Addr_Width
Table/Registerdiscription
Field discription
REG
field attribute
filed default
Field name
Discription
filed range
field discription
Regname
width
offsetaddr
default value
Field
Properties
Properties
H/W
P_reserved
value
每2bit对应相应通道：
第1bit:
1"bo：展宽后的信号；
CFG_CIPC_CPLD_EV
26-10-04-08·90
sel
1"b1：异步处理后的信号；
0x000000A0
ro
TH_EDGE
第2bit：
1"b1：通过第1bit选择后的信
buar.
huanj3
uan
[1'bo:bypass]
CFG_CIPC_CPLD_EV
每一bit对应相应通道：
sel
0x000000A4
ro
1'b1：信号做打拍；
TH_PIPE
1'bo:bypass.
每一bit对应相应通道：
CFG_CIPC_CPLD_EV
sel
1'b1：信号在soc时钟下展宽15
0x000000A8
ro
TL_EXTEND
1'bo:bypass
每2bit对应相应通道：
第1bit：
1"bo：展宽后的信号；
CFG_CIPC_CPLD_EV
1"b1：异步处理后的信号；
sel
Ox000000AC
ro
TL_SYNC
第2bit:
1"b1：通过第1bit选择后的信
1'bo:bypassj
每2bit对应相应通道：
第1bit:
1"bo：展宽后的信号；
CFG_CIPC_CPLD_EV
1"b1：异步处理后的信号；
0x000000BO
sel
ro
TL_EDGE
第2bit:
muan.li 29
1"b1：通过第1bit选择后的信
号；
ETMOU
1'bo:bypass;
CFG_CIPC_CPLD_EV
每一bit对应相应通道：
sel
rv
ro
TL_PIPE
1"b1：信号做打拍；
1' bo:bypass



### 截图编号 7 (`images/GameViewer_lGL9ilGPp4.png`)

#### 【全页】

cpld cfg
Data_Width
ModuleName
32CFGIFAHB
检查
新增寄存器
新增域段
升级
Base_Addr
Addr_Width
Table/Register discription
VField discription
REG
field attribute
filed default
Discription
Field name
filed range
field discription
Regname
offset addr
width
default value
Field
Properties
s/W
H/W
Properties
P_reserved
value
每2bit对应相应通道：
第1bit：
1"bo：展宽后的信号；
CFG_ADCO_CPLD_EV
26-10-04-08·00
sel
1"b1：异步处理后的信号；
0x000000D0
ro
TL_EDGE
第2bit:
1"b1：通过第1bit选择后的信
huan
buan
huanj
[1'bo:bypass]
CFG_ADCO_CPLD_EV
每一bit对应相应通道：
sel
0x000000D4
ro
1"b1：信号做打拍；
TL_PIPE
1'bo:bypass
每一bit对应相应通道：
CFG_ADC1_CPLD_EV
sel
1"b1：信号在soc时钟下展宽15
0x000000D8
ro
TH_EXTEND
拍；
1'bo:bypass
每2bit对应相应通道：
第1bit:
hnan.J
1"bo：展宽后的信号；
CFG_ADC+CPLD_EV
1'b1：异步处理后的信号；
sel
Ox000000DC
ro
TH_SYNC
第2bit:
1"b1：通过第1bit选择后的信
[1'bo:bypass.;
每2bit对应相应通道：
第1bit:
1"bo：展宽后的信号；
1"b1：异步处理后的信号；
CFG_ADC1_CPLD_EV
sel
OX00000OEO
ro
TH_EDGE
第2bit:
muan.Ji
1"b1：通过第1bit选择后的信
号：
ETMOU
1'bo:bypass]
CFG_ADC1_CPLD_EV
每一bit对应相应通道：
sel
rv
ro
TH_PIPE
1"b1：信号做打拍；
1'bo:bypass



### 截图编号 8 (`images/GameViewer_VyNqGG3Mj6.png`)

#### 【全页】

ModuleName
cpld_cfg
Data_Width
32CFGIFAHB
检查
新增寄存器
新增域段
升级
Base_Addr
Addr_Width
Table/Register discription
Field discription
REG
field attribute
filed default
filed range
Field name
width
Field
Reg name
Discription
offset addr
default value
field discription
Properties
s/W
H/W
Properties
value
P_reserved
CFG_SOC_SOFT_RST
1"b1：信号做异步处理；
sync_sel
ro
1'bo:bypass
CFG_ETIM_CPLD_SY
pipe_sel
1"b1：信号做打拍；
rv
ro
1'bo:bypass
2'bo:bypass
2"b1:上升沿
edge_sel
ro
2"b2:下降沿
nuan.Ji
2"b3:双沿
第1bit：
1"bo：展宽后的信号；
1"b1：异步处理后的信号；
symc_sel
ro
第2bit：
1'b1：通过第1bit选择后的信
1'bo:bypass;
1"b1：信号在soc时钟下展宽15
extend_sel
ro
拍；
huan, 11 2o06-10-04-07:b8
huan.J3
1'bo:bypass
uan.Ji
每一bit对应相应通道：
CFG_INXB_CPLD_DA
sel
1"b1：信号在soc时钟下展宽15
ro
TA_EXTEND
拍；
1'b:bypass
每2bit对应相应通道：
第1bit：
1bo：展宽后的信号；
CFG_INXB_CPLD_DA
sel
1"b1：异步处理后的信号；
ro
TA_SYNC
第2bit：
1"b1：通过第1bit选择后的信
ETMChuan.
1"bo:bypass;



### 截图编号 9 (`images/GameViewer_ZlKSgCi2AU.png`)

#### 【全页】

ModuleName
cpld cfg
Data_Width
32CFGIFAHB
检查
新增寄存器
新增域段
升级
Base_Addr
Addr_Width
Table/Register discription
WField discription
REG
field attribute
filed default
Field name
filed range
field discription
width
Regname
Discription
offset addr
default value
Field
Properties
H/W
Properties
P_reserved
value
CFG_ETIM_CPLD_PW
每一bit对应相应通道：
pipe_sel
ro
1b1：信号做打拍；
1'bo:bypass
每一bit对应相应通道：
sync_sel
rv
ro
1'b1：信号做异步处理；
1'bo:bypass.
每一bit对应相应通道：
CFG_PAD_CPLD_IN1
reserved
rv
ro
1"b1：信号做异步处理；
1'bo:bypass
WTMCI
每一bit对应相应通道：
CFG_PAD_CPLD_INO
symc_sel
rv
ro
1"b1：信号做异步处理；
1'bo:bypass.
CFG_CPUO_LOCKUP
1"b1：信号做异步处理；
sync_sel
ro
1"bo:bypass
sync_sel
CFG_CPU1_LOCKUP
1"b1：信号做异步处理；
ro
1'bo:bypass
sync_sel
CFG_BUS_TIMEOUT
1"b1：信号做异步处理；
ro
1'bo:bypass.
1'b1：信号做异步处理；
CFG_TEMP_VARN
ro
sync_sel
1'bo:bypass
CFG_POWER_ERR
1"b1：信号做异步处理；
symc_sel
rv
ro
1'bo:bypass
CFG_PVR_OCP_WARN
symc_sel
ro
1"b1：信号做异步处理；
1'bo:bypass
CFG_POR_UV_WARN
1"b1：信号做异步处理；
sync_sel
ro
1'bo:bypass
sync_sel
1"b1：信号做异步处理；
CFG_POR_OV_WARN
ro
1'bo:bypass.
CFG_SOC_HARD_RST
ro
1"b1：信号做异步处理；
symc_sel
1'bo:bypass
ETMO
CFG_SOC_WDGO_RST
1"b1：信号做异步处理；
symc_sel
ro
1'bo:bypass
CFG_SOC_WDG1_RST
1"b1：信号做异步处理；
symc_sel
ro
34H
1'bo:bypass



---
## 第二部分：ET6601 专项修改点提取

> 以下条目为从原始截图中精确检索到的关于 ET6601 芯片的专项说明、变更标注与修订记录：

- `images/GameViewer_6BxAbFuaFj.png` (全页): 新增域段
- `images/GameViewer_6BxAbFuaFj.png` (全页): 新增寄存器
- `images/GameViewer_ehusonHEeP.png` (全页): 新增寄存器
- `images/GameViewer_ehusonHEeP.png` (全页): 新增域段
- `images/GameViewer_er1i0CeSs6.png` (全页): 新增域段
- `images/GameViewer_er1i0CeSs6.png` (全页): 新增寄存器
- `images/GameViewer_Fi0vMedNfB.png` (全页): 新增寄存器
- `images/GameViewer_Fi0vMedNfB.png` (全页): 新增域段
- `images/GameViewer_L2kHUqr7hq.png` (全页): 新增域段
- `images/GameViewer_L2kHUqr7hq.png` (全页): 新增寄存器
- `images/GameViewer_lCjo9mFfHG.png` (全页): 新增寄存器
- `images/GameViewer_lCjo9mFfHG.png` (全页): 新增域段
- `images/GameViewer_lGL9ilGPp4.png` (全页): 新增寄存器
- `images/GameViewer_lGL9ilGPp4.png` (全页): 新增域段
- `images/GameViewer_VyNqGG3Mj6.png` (全页): 新增寄存器
- `images/GameViewer_VyNqGG3Mj6.png` (全页): 新增域段
- `images/GameViewer_ZlKSgCi2AU.png` (全页): 新增寄存器
- `images/GameViewer_ZlKSgCi2AU.png` (全页): 新增域段