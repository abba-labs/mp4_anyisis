# HAC_WRAP 顶层架构设计说明

> 本文档由大模型逐图逐页提取自原始截图，不作主观修饰，忠实还原原文。
> 图表、时序波形及模糊部分均标注对应截图原图文件名供查阅。


---
## 图像编号 1 (原图: `GameViewer_tVxXq4JUXF.png`)

### 【全页】

AHB_BUS2, 32bit, 200MHz
SDFM 0~3
CMPC 0-10
SARC 0~2
WAG
ToCPUX_SUB4
(22ch)
DACC
(16ch)
0~1
AHB_BUS1,32bit, 200MHz
202F-10-02-27-20
ETIM
SuperPWM
XBAR
SuperPWM
12ch
Com
SuperPWM
CLB1
spwm_wave
0~17
gen
SRPWM
6801HAC_WRAP
AHB_BUS2, 32bit, 200MHz
to M7_WRAPx
ctr
CMPC
SARC 0~1
WAG
CMPClite0-9
(2ch)
(20ch)
AHB2to1
H2H(V/2)
AHB_BUS1, 32bit, 200MHz
CPLD
SuperPWM
ETIM
SuperPWM
14ch
SuperPWM
Com
0~11
gen
SRPWM
6601HAC_WRAP

