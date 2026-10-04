# CPLD - PPI_DOC 设计与接口说明

> 提取说明：本文档由 AI Agent 严格按照原始截图提取，未作主观改动。
> 模糊或包含复杂波形处均已精确标明原截图文件索引。

---

## 第一部分：文档原始正文内容


### 截图编号 1 (`images/GameViewer_0MSje0n5n8.png`)

#### 【左页】

> 📌 **【图表引用】**: 此处包含图表 `图1-1CPLDPPI整体示意图`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`

> 📌 **【图表引用】**: 此处包含图表 `图2-1 CPLD PPI写操作示意图`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`

> 📌 **【图表引用】**: 此处包含图表 `图2-2 CPLD写操作自动更新模式`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`

> 📌 **【图表引用】**: 此处包含图表 `图 2-3 CPLD 写操作自动更新模式时序`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`

> 📌 **【图表引用】**: 此处包含图表 `图2-4 CPLD 写操作非自动更新模式`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`

> 📌 **【图表引用】**: 此处包含图表 `图2-5CPLD写操作非自动更新模式时序`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`

> 📌 **【图表引用】**: 此处包含图表 `图2-6CPLD读操作示意图`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`

> 📌 **【图表引用】**: 此处包含图表 `图 2-7 CPLD 读操作时序`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`

图目录
BICU huan Ji

**图1-1CPLDPPI整体示意图**


**图2-1 CPLD PPI写操作示意图**


**图2-2 CPLD写操作自动更新模式**


**图 2-3 CPLD 写操作自动更新模式时序**


**图2-4 CPLD 写操作非自动更新模式**

BJMCU jmuan. Ji

**图2-5CPLD写操作非自动更新模式时序**


**图2-6CPLD读操作示意图**


**图 2-7 CPLD 读操作时序**

表目录

**表 1-1修订记录**

99:20-F0-01-9202


#### 【右页】

> 📌 **【图表引用】**: 此处包含图表 `图1-1CPLDPPI整体示意图`，完整拓扑/波形请参见原始截图: `images/GameViewer_0MSje0n5n8.png`


### 第1章

说明
K7CVhuan2 1i2026-10-04-07:55
ppi_csn-
pp:_date_ busl11:0J
PPI_CORE
ppi_ de te_addr[4:0]
CPU
CPLD
ahb总线
缓存
Ppi_ de ta_out11:0]

**图1-1CPLDPPI整体示意图**

图中：1）PPI_CORE包含缓存以及时序处理逻辑；
2）CPLD中为PPI逻辑代码；
用户定义的PPI逻辑与CPU，通过PPI_CORE处理后完成数
据交互;
Q026
rel
4fp

#### 1.6 Mbp

4Kauto
190%



### 截图编号 2 (`images/GameViewer_3CpEhzKnYr.png`)

#### 【左页】

> 📌 **【图表引用】**: 此处包含图表 `图2-4CPLD写操作非自动更新模式`，完整拓扑/波形请参见原始截图: `images/GameViewer_3CpEhzKnYr.png`

> 📌 **【图表引用】**: 此处包含图表 `图2-5CPLD写操作非自动更新模式时序`，完整拓扑/波形请参见原始截图: `images/GameViewer_3CpEhzKnYr.png`


**图2-4CPLD写操作非自动更新模式**

首先，需要配置ppi_wr_en=1ru表明PPI执行写操作;
配置ppi_wr_start_mode=0，表明ppi写操作在非自动更新模
式下;
该模式下，用户需要配置ppi_fifo_waterline表明需要配置寄存
器的数量，再配置ppi_data_bus和ppi_addr存入缓存中，当配置
数量达到ppi_fifo_waterline时，需要配置ppi_wr_start将缓存中
的数据通过PPI接口连续写入用户逻辑中；
Cloc
Pi_w_stat
ppi_csn
snqelep~idd
2i

**图2-5CPLD写操作非自动更新模式时序**

图中ppi_csn拉低的周期数为需要写入寄存器数量周期数；


#### 【右页】

> 📌 **【图表引用】**: 此处包含图表 `图2-6CPLD读操作示意图`，完整拓扑/波形请参见原始截图: `images/GameViewer_3CpEhzKnYr.png`


#### 2.3PPI读操作

ian.71 2026-10-04-07:55
rouan.11 2026-10-04-07:55
CPU
CFLD用户自定义PPI逻辑
配置ppi_rr_en=0表示读操作
配置地址ppi_addr
ppi_data_out
ETNCU huan Ji 2026-20-04-07:55
配置地址ppi_addr
ppi_data_out

**图2-6CPLD读操作示意图**

PPI读操作从CPLD用户自定义逻辑读取数据到MCU。
需要配置ppi_wr_en=0表明PPI执行读操作；
该模式下，用户需要配置ppi_addr，读取ppi_data_out；°牟
每配
置一次 ppi_addr，读取一次ppi_data_out。
ETNCU hue
rel

#### 22.7Mb

4Kauto
190%



### 截图编号 3 (`images/GameViewer_gB3mSlMiNI.png`)

#### 【左页】


**表1-1修订记录**

修订日
修订
修订内容
本号
人员
&TMCU
BJMCU jhuan. 3i
BIMCU
ETMCU hua2.1i 2026-10-04-07:5
BTMCU hu. 13 2026-10-04-073
ETMGU muan. li


#### 【右页】

目录
Contents
且录
图且录
表且录

### 第1章

说明
ETNCU huan2 1i 2026-10-04-07:55
第2 章
PPI

#### 2.1 PPI 接口


#### 2.2 PPI写操作

muan. li 2026-10-04
自动更新模式
非自动更新模式

#### 2.3 PPI 读操作

参考文献
ETMOU hua. 1i 2026-10-04-07
ETNCU hua2 1i 2026-10-04-07:55
rel

#### 0.0%

4Kauto
190%



### 截图编号 4 (`images/GameViewer_iRqqD2fwbl.png`)

#### 【左页】


### 第2章 PPI


#### 2.1 PPI 接口

B7MCU huan.
ppi定义总线接口如下
输入输出
信号
位宽
说明
输入
ppi data bus
PPI输入数据
输入
ppi_csn
PPI数据有效信号，
ITMO!
低有效
输入
ppi addr
PPI地址信号
输出
ppi data out
PPI数据输出信号
后文涉及的配置相关信号说明如下信号
位宽
信号
说明
ppi_wr_en
1：PPI执行写操作
0：PPI执行读操作
ppi_wr_start_mode
PPI写操作更新模式
1：自动更新模式
0：非自动更新模式
ppi_fifo_waterline
配置的缓存水线，表明ppi
需要写入数据的数量
ppi data out vld
为1表明ppi data_out有效
ppi_wr_start
PPI写操作非自动更新模式
下，更新触发信号。


#### 【右页】

> 📌 **【图表引用】**: 此处包含图表 `图2-1uCPLDPPI写操作示意图`，完整拓扑/波形请参见原始截图: `images/GameViewer_iRqqD2fwbl.png`


#### 2.2 PPI写操作

TMCU huan. 21 2026-10-04-07:55
PPI_CORDE
CPLD用户自定义PPT逻辑
配置相关状态
配置数据
tan.11
huarn 11 2026-10-04-07:55
缓存数据
达到判定状态
数据写入

**图2-1uCPLDPPI写操作示意图**

PPI写操作从MCU总线配置数据，先写入缓存，再传输到
CPLD。包含两种模式：自动更新模式和非自动更新模式；
先写入缓存的目的是可以在CPU空闲周期或使用DMA取搬
移提前搬移数据，然后在合适的实际一次性把数据通过PPI接口
rel
写入用户逻辑。

#### 16.9Mb

94msf
4Kauto
190%



### 截图编号 5 (`images/GameViewer_mIx7O7sTug.png`)

#### 【左页】

EIMCU 3 2026-10-04-07:55
BIMCU
8TMCU muan 11 2026-10-04-07:55
CPLD PPI说明文档
BIMC
EINCU S
hua3. 13 2026-10-04-07.56
设计：—
ETCU hua2.1i 2026-10-04-07:55
袁云龙
评审：XXXXXXX
huan


#### 【右页】

批准：
ETNOU huan Ji 2026-10-04-07:55
BTMCU muan.1i 2026-10-04-07:55
ETNCU hun 11 2026-10-04-07:55
ETMOU hua.11 2026-10-04-07:55
rel
fps
ms
auto
190%



### 截图编号 6 (`images/GameViewer_vh7163qEPi.png`)

#### 【左页】

> 📌 **【图表引用】**: 此处包含图表 `图2-7 CPLD`，完整拓扑/波形请参见原始截图: `images/GameViewer_vh7163qEPi.png`

pi_csn
Ppi_adar
de_FRAME,LEN
Ppi_data_oot
XLERAME LEN
daa9ut1
B7MCU huan. Ji

**图2-7 CPLD**

读操作时序
EJMCU han. 1i
.Ji 2026-10-04-07:56
ETMCUuan.132026-10-04-07:55


#### 【右页】

参考文献
[1]
B7MCU huan. 71 2026-10-04-07:55
文栏结尾
BTMCU muan. 11 2026-10-04-07:55
EINCU
BTMOU
BIMCU
rel

#### 30.4Mb

ms
4Kauto
190%



### 截图编号 7 (`images/GameViewer_y7pMiLcW2a.png`)

#### 【左页】

> 📌 **【图表引用】**: 此处包含图表 `图2-2CPLD写操作自动更新模式`，完整拓扑/波形请参见原始截图: `images/GameViewer_y7pMiLcW2a.png`


#### 2.2.2自动更新模式

CPLD用户自定义PPI逐辑
配置ppi_r_en表示写操作
BIMCU
配置ppi_wr_start_mode=-
表示自动更新模式
配置ppi_fifo_waterline
表示需要配置的寄存器数量
配置数据
缓存数据
BTMO/uan 1i
BTMCU huan. Ji
可读取己配置数量
配暨的数量达到
数据写入
ppi_fifo_raterl ine
->

**图2-2CPLD写操作自动更新模式**

首先，需要配置ppi_wr_en=1表明PPI执行写操作；
配置ppi_wr_start_mode=1，表明ppi写操作在自动更新模式
下;
该模式下，用户需要配置ppi_fifo_waterline表明需要配置寄存
器的数量，再配置ppi_data_bus和ppi_addr存入缓存中，当配置
数量达到ppi_fifo_waterline时，MCU硬件自动触发将缓存中的
数据通过PPI接口连续写入用户逻辑中；


#### 【右页】

> 📌 **【图表引用】**: 此处包含图表 `图2-3CPLD写操作自动更新模式时序`，完整拓扑/波形请参见原始截图: `images/GameViewer_y7pMiLcW2a.png`

Clock
须存数量
ppi_csn
Ppi_databus

**图2-3CPLD写操作自动更新模式时序**

图中ppi_csn拉低的周期数为需要写入寄存器数量；

#### 2.2.3非自动更新模式

ETNCU hua2 11 2026-10-04-07:56
CPU
PPI_CORDE
CPLD用户自定义PPT逻辑
配置ppi_r_en=1表示写操作
配置ppi_wr_start_mode-0
表示非自动更新模式
配置ppi_fifo_vaterline
ETNG
表示需要配置的寄存器数量
配置数据
微存数据
可读取己配置数量
配置的数量达到
ppi_fifo_raterline
数据写入
配置ppi_r_start触发更新
rel

#### 38.8Mb

SS:20-t0-0T-9202
auto
190%



---
## 第二部分：ET6601 专项修改点提取

> 经全页视觉文本检索，本组截图中未出现显式的 'ET6601' 特殊字色修改标注或修订记录文本，整体属于该模块标准基线配置。