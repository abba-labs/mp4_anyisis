# SARC 功能框图及处理流程说明

> 本文档由大模型逐图逐页提取自原始截图，不作主观修饰，忠实还原原文。
> 图表、时序波形及模糊部分均标注对应截图原图文件名供查阅。


---
## 图像编号 1 (原图: `GameViewer_323Uh2DKeH.png`)

### 【全页】

(pre_data_in[15:0],3'd0]
({1(pre_data_in[15]}/,pre_data_in[15:0],2'd0)
flt_dat_in[15:0]
round
sat
19bit
17bit
(2(pre_data_in[15])/pre_data_in[15:0],1d0)
s(16,0)s(16,3)
{(3(pre_datain[15]},pre_data_in[15:0])
缩放之后数据范围
cfgpflt_idat_gain_adjli:0]
对输入数据进
定标指示一个示意表示，为了在原
flt_cal_st
行缩放
有的基础上改动小一点，在此重新
定标为s（16，15），实在不理解，可
以理解为把上面的16bit输入到下
面的一个滤波器系统中
26' do
s(16, 15)
s(26, 22)
flt_cal_dat[flt_idx][15:0]
补两位符号位
s(32,30)
s(24, 22)
s(26, 22)
flt_acc
fir
f1
s (27, 22)
flt_cal_en-
Jen
flt_coeff[flt_idx][15:0]
根据滤波器的系数
来确定乘加的次数
wrap
sat
s(26, 22)
flt_acc[26]
DD
fltovf
cfg_pflt_clip
f1+
s(26,22)



---
## 图像编号 2 (原图: `GameViewer_7ULdHnhXju.png`)

### 【全页】

(pre_data_in[15:0],3'd0]
,pre_data_in[150],2'd0]
flt_dat_in[15:0]
round
sat
19bit
17bit
,pre_data_in[15:0],1d0]
s(16,0)s(16,3)
[15],pre_data_in[15:0]]
缩放之后数据范围
cfg_pflt_idat_gain_adj[i:0]
定标指示一个示意表示，为了在原
fltcal_st
有的基础上改动小一点，在此重新
定标为s（16，15)，实在不理解，可
以理解为把上面的16bit输入到下
面的一个滤波器系统中
26' do
s(16, 15)
s(26, 22)
fIt_cal_dat[f]t_idx][15:0]
补两位符号位
(24, 22)
s(32,30)
+s(26,22)
flt_acc
flr
flt_cal_dat_o_pre[25:0]
s(27,22)
s (26, 22)
flt_cal_en-en
flt_coeff[flt_idx][15:0]
根据滤波器的系数
来确定乘加的次数
wrap
sat
s(26, 22)
f1t_acc[26]
fltovf
cfg_pflt_clip



---
## 图像编号 3 (原图: `GameViewer_9akceoHcVF.png`)

### 【全页】

ADC校准参数处理
用户配置参数处理
15bit signed
14bit unsigned
16bit signed
15bit signed
[-2^14~2^14-1) /(22)
0~4
-4~4
cal_gain/4096
cal_offset
pre_offset
pre_gain/4096
s(16,2)/s(16,0)可选择
u(12,0)
s(16,2)
s(15,2)
u(14,12)
s(15,12)
Is(16,2)
s(16,2)
s(18,2)
s(19,2)
预处理滤
s(16,2)
s(16,2)
s(16,
result reg 1
a2d_data_out
cal_data_out
signed
round
sat
sat
round
pre_data_out
波通道
s(16,2)
s(16,2)
16*16bit
s(30,14)
s(31,14)
dig_cal
pre_process
s(1b0,(12.0）-52048取（低12bit为s(12,0)
电平超门限检测
整数小数位各扩展2bit为s(16,2)，以此作
EVTOUT
为后续计算基础，得到结果定点s(16,2)
滤波处理
limitlolimit hi
s(16,2) signed
s(13,12) signed
ifilter_coeff
s(16,2) signed
5(16,2)/u(12,0)可选择
s(22,2)
s(16,2)
s(34,14)
s(29,14)
result reg 2
round
sat
filter_data_out
16*16bit
32个×
filter



---
## 图像编号 4 (原图: `GameViewer_lHuv0AHt75.png`)

### 【全页】

(pre_data in[15:0],3'd0
((1 (pre_data_in[15])), pre_data in[15:0], 2' d0)
flt dat in[15:0]
round
sat
19bit
17bit
((2(pre data in[15],pre_data in[15:0],1'd0)
s(16,0)s(16,3)
[(3 (pre_data_in[15]}}, pre_data in[15:0])
缩放之后数据范围
cfglpflt_idat gain adj[l:0]
对输入数据进
定标指示一个示意表示，为了在原
行缩放
有的基础上改动小一点，在此重新
定标为s（16，15），实在不理解，可
以理解为把上面的16bit输入到下
面的一个滤波器系统中
s(16, 15)
s(2
flt cal dat[flt idx][15:0]



---
## 图像编号 5 (原图: `GameViewer_q40E10cbND.png`)

### 【全页】

Chan 0
SARADC
CALC
预处理滤波通道
预处理通道
缓存通道1
PChan0
PFChan0
BChano
Chan1
readyl
校准通道
PChan 1
PFChan1
data
BChan1
SH
SARCORE
CAL
PChanM
PFChanM
BChanM
busy
滤波通道
Chan N
done
trigger
缓存通道2
CPU/DMA
FChan0
BChan0
采样通
FChan 1
BChan1
道选择
SARADC
CTRL
校准、预处理、滤波、缓存控制
FChanK
BChanM
模拟电路
触发信号管理
数字电路



---
## 图像编号 6 (原图: `GameViewer_T5Wi63Rflj.png`)

### 【全页】

f1t_acc[26]
DD
fltlovf
cfg_pflt clip
f1t_acc[25]
s(26, 22)
flt_cal_en
<<R
s (26, 22-R)
合并
(flt_cal_dat_opre[25:0]
[(1(flt_cal_dat_o_pre[25])),flt_cal_dato_pre[25:1])
s (26, 15)4
{{2flt_caldat_o_pre[25]}),flt_cal_dat_o_pre[25:2]]
{(3(f1t_cal_dat_0_pre[25])),flt_cal_dat_opre[25:3])
s(26,15)
sat
{(4{flt_cal dat_o_pre[25]}),flt_cal_dat_o_pre[25:4]]
flt_cal_dat_o[15:0]
{(5(flt_caldat_o_pre[25]]),f1t_cal_dat|o_pre[25:5]]
wrap
s(16, 15)
{{6(f1t_cal|dat_0_pre[25]]),flt_cal_dat_o_pre[25:6])
((7{flt_caldat_o_pre[25]]),flt_cal_dat_o_pre[25:7]]
cfgpfltacc_out_wrap_sel
cfg_pflt_r_arg[2:0]
定标指示一个示意表示，为了在原有的基础
上改动小一点，在此重新定标为s（16，2），
TAC
实在不理解，可以理解为从滤波器系统中输
出一个16bit数据



---
## 图像编号 7 (原图: `抢占功能.png`)

### 【全页】

vc_flag_ctrl
-ready
vc_f1ag[15:0]
none_flag
priority_cnflt→
sarc_smaple_ctrl
start
vc_queue
-vc_num_req
模拟ADC
vc_num/val-



---
## 图像编号 8 (原图: `过采求和功能.png`)

### 【全页】

寄存器表单
sumo sum7
intr/dma处理
vc_flag_ctrl
sum_ctrl
ovs_ctrl
sarc_pflt
sumcho7
(pfc_cho~7)
data
ve_flag[15:0]
priority_cflt
sarc_sample_ctrl
vc_queue
vc_num-
-start-
模拟ADC

