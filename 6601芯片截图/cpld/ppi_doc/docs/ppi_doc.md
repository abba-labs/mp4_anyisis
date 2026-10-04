# CPLD PPI 说明文档

> 来源：ET6601 原始截图精准还原  
> CPLD 为 ET6601 新 IP，本文件不建立“ET6601 修改点”章节。  
> 截图中的录屏水印、时间戳、播放器控件、网络状态、缩放比例等非文档内容已剔除。

## 封面

**CPLD PPI 说明文档**

- 设计：袁云龙
- 评审：XXXXXXX
- 批准：XXXXXXX

原图：`images/GameViewer_mIx7O7sTug.png`

## 表1-1 修订记录

| 版本号 | 修订内容 | 修订日期 | 修订人员 |
|---|---|---|---|
| 1.0 |  | 20210831 |  |

原图：`images/GameViewer_gB3mSlMiNI.png`

## 目录

- 目录
- 图目录
- 表目录
- 第1章 说明
- 第2章 PPI
  - 2.1 PPI 接口
  - 2.2 PPI 写操作
    - 2.2.2 自动更新模式
    - 2.2.3 非自动更新模式
  - 2.3 PPI 读操作
- 参考文献

## 图目录

- 图1-1 CPLD PPI 整体示意图
- 图2-1 CPLD PPI 写操作示意图
- 图2-2 CPLD 写操作自动更新模式
- 图2-3 CPLD 写操作自动更新模式时序
- 图2-4 CPLD 写操作非自动更新模式
- 图2-5 CPLD 写操作非自动更新模式时序
- 图2-6 CPLD 读操作示意图
- 图2-7 CPLD 读操作时序

## 表目录

- 表1-1 修订记录

原图：`images/GameViewer_gB3mSlMiNI.png`、`images/GameViewer_0MSje0n5n8.png`

# 第1章 说明

> 📌 【原图引用】图1-1《CPLD PPI整体示意图》：`images/GameViewer_0MSje0n5n8.png`

**图1-1 CPLD PPI整体示意图**

图中：

1）PPI_CORE 包含缓存以及时序处理逻辑；  
2）CPLD 中为 PPI 逻辑代码；  
用户定义的 PPI 逻辑与 CPU，通过 PPI_CORE 处理后完成数据交互；

# 第2章 PPI

## 2.1 PPI 接口

ppi 定义总线接口如下

| 信号 | 输入输出 | 位宽 | 说明 |
|---|---|---:|---|
| ppi_data_bus | 输入 | 12 | PPI 输入数据 |
| ppi_csn | 输入 | 1 | PPI 数据有效信号，低有效 |
| ppi_addr | 输入 | 5 | PPI 地址信号 |
| ppi_data_out | 输出 | 12 | PPI 数据输出信号 |

后文涉及的配置相关信号说明如下

| 信号 | 位宽 | 说明 |
|---|---:|---|
| ppi_wr_en | 1 | 1：PPI 执行写操作<br>0：PPI 执行读操作 |
| ppi_wr_start_mode | 1 | PPI 写操作更新模式<br>1：自动更新模式<br>0：非自动更新模式 |
| ppi_fifo_waterline | 5 | 配置的缓存水线，表明 ppi 需要写入数据的数量 |
| ppi_data_out_vld | 1 | 为 1 表明 ppi_data_out 有效 |
| ppi_wr_start | 1 | PPI 写操作非自动更新模式下，更新触发信号。 |

原图：`images/GameViewer_iRqqD2fwbl.png`

## 2.2 PPI 写操作

> 📌 【原图引用】图2-1《CPLD PPI写操作示意图》：`images/GameViewer_iRqqD2fwbl.png`

**图2-1 CPLD PPI写操作示意图**

PPI 写操作从 MCU 总线配置数据，先写入缓存，再传输到 CPLD。包含两种模式：自动更新模式和非自动更新模式；  
先写入缓存的目的是可以在 CPU 空闲周期或使用 DMA 取搬移提前搬移数据，然后在合适的实际一次性把数据通过 PPI 接口写入用户逻辑。

## 2.2.2 自动更新模式

> 📌 【原图引用】图2-2《CPLD 写操作自动更新模式》：`images/GameViewer_y7pMiLcW2a.png`

**图2-2 CPLD 写操作自动更新模式**

首先，需要配置 ppi_wr_en = 1 表明 PPI 执行写操作；  
配置 ppi_wr_start_mode = 1，表明 ppi 写操作在自动更新模式下；  
该模式下，用户需要配置 ppi_fifo_waterline 表明需要配置寄存器的数量，再配置 ppi_data_bus 和 ppi_addr 存入缓存中，当配置数量达到 ppi_fifo_waterline 时，**MCU 硬件自动**触发将缓存中的数据通过 PPI 接口连续写入用户逻辑中；

> 📌 【原图引用】图2-3《CPLD 写操作自动更新模式时序》：`images/GameViewer_y7pMiLcW2a.png`

**图2-3 CPLD 写操作自动更新模式时序**

图中 ppi_csn 拉低的周期数为需要写入寄存器数量；

## 2.2.3 非自动更新模式

> 📌 【原图引用】图2-4《CPLD 写操作非自动更新模式》：`images/GameViewer_y7pMiLcW2a.png`、`images/GameViewer_3CpEhzKnYr.png`

**图2-4 CPLD 写操作非自动更新模式**

首先，需要配置 ppi_wr_en = 1 表明 PPI 执行写操作；  
配置 ppi_wr_start_mode = 0，表明 ppi 写操作在非自动更新模式下；  
该模式下，用户需要配置 ppi_fifo_waterline 表明需要配置寄存器的数量，再配置 ppi_data_bus 和 ppi_addr 存入缓存中，当配置数量达到 ppi_fifo_waterline 时，**需要配置 ppi_wr_start** 将缓存中的数据通过 PPI 接口连续写入用户逻辑中；

> 📌 【原图引用】图2-5《CPLD 写操作非自动更新模式时序》：`images/GameViewer_3CpEhzKnYr.png`

**图2-5 CPLD 写操作非自动更新模式时序**

图中 ppi_csn 拉低的周期数为需要写入寄存器数量周期数；

## 2.3 PPI 读操作

> 📌 【原图引用】图2-6《CPLD 读操作示意图》：`images/GameViewer_3CpEhzKnYr.png`

**图2-6 CPLD 读操作示意图**

PPI 读操作从 CPLD 用户自定义逻辑读取数据到 MCU。  
需要配置 ppi_wr_en = 0 表明 PPI 执行读操作；  
该模式下，用户需要配置 ppi_addr，读取 ppi_data_out；每配置一次 ppi_addr，读取一次 ppi_data_out。

> 📌 【原图引用】图2-7《CPLD 读操作时序》：`images/GameViewer_vh7163qEPi.png`

**图2-7 CPLD 读操作时序**

# 参考文献

[1]
