# SARC 辅助图原始文字还原

> 本标题为资料组索引，不声称是原始文档标题。11张图片不是已经证实连续的同一份原始文档；保留各自图界、批注和版本边界，不拼入SARC方案正文作为新页面。
> 2026-10-05第六轮：5/11张完成整图首轮；其余6张未整图核对，旧稿区明确标识。完整源码图使用原始PNG，不使用OCR结果替代核对。
> 本批确认四张预处理滤波取景的重叠区域；q40的绿色有“模拟电路”图例。没有以缺少版本声明的辅助图颜色擅增确定6601修改项。
> 主文档LRS3组、LLD19组与S01本批未关闭。裁切边界与图内无法辨字不同：画外内容不写成本图原文。正式保存见`../../../reviews/SARC_AUX_ROUND6_REMOTE_SAVE_20261005.json`。

## 第一部分：逐来源还原（索引次序，不是原文页序）

## 来源A01：`GameViewer_323Uh2DKeH.png`

[查看原始PNG](../images/GameViewer_323Uh2DKeH.png)

### 输入缩放局部

选择输入0～3的可见原式如下（括号按图内拼接形式转录）：

```text
0  {pre_data_in[15:0],3'd0}
1  {{1{pre_data_in[15]}},pre_data_in[15:0],2'd0}
2  {{2{pre_data_in[15]}},pre_data_in[15:0],1'd0}
3  {{3{pre_data_in[15]}},pre_data_in[15:0]}
cfg_pflt_idat_gain_adj[1:0]
```

图内链路标签：`19bit` → `round` → `17bit` → `sat` → `flt_dat_in[15:0]`；输出旁红字`s(16,0)~s(16,3)`、`缩放之后数据范围`。

红色批注（属于原图）：

> 对输入数据进行缩放
>
> 定标指示一个示意表示，为了在原有的基础上改动小一点，在此重新定标为s(16,15)，实在不理解，可以理解为把上面的16bit输入到下面的一个滤波器系统中

### 乘加、累加局部

| 原图区域 | 可辨原标签及图形连接索引 |
|---|---|
| 乘法输入 | `flt_cal_dat[flt_idx][15:0]`、`s(16,15)`；另一输入`flt_coeff[flt_idx][15:0]`；圆圈乘号 |
| 乘法输出及截位 | `s(32,30)` → `flr` → `s(24,22)`；红字`补两位符号位`；`s(26,22)`到圆圈加号 |
| 累加反馈选择 | 选择端`flt_cal_st`；输入0为上方反馈线，输入1为`26'd0`；反馈线标`s(26,22)` |
| 加法输出 | `flt_acc`、`s(27,22)`；分向`wrap`、`sat` |
| 裁剪选择 | `wrap`到输入0，`sat`到输入1；选择端`cfg_pflt_clip`；输出`s(26,22)` |
| 结果寄存器 | `D`、`Q`、`en`；使能端`flt_cal_en`；Q端接上方反馈 |
| 底部可见片段 | `flt_acc[26]`、`flt_acc[25]`（后者下沿截断）、异或/与门图形、`flt_ovf`；右下`s(26,22)` |

原图红色批注：

> 根据滤波器的系数来确定乘加的次数

> 取景边界：右缘Q输出网名截断，仅见起始`fl…`，底边亦切到后续逻辑；不按其它图把画外文字写成本图已拍到。右侧完整网名在下一来源7ULdHnhXju中可见。这里`flr`是图内标签，不改成`fir`；原图没有标题、图号或版本声明。

## 来源A02：`GameViewer_7ULdHnhXju.png`

[查看原始PNG](../images/GameViewer_7ULdHnhXju.png)

### 本图上部与左缘

上方输入0～3的左端被截图边界切掉。可辨片段依次为`pre_data_in[15:0],3'd0`、`pre_data_in[15:0],2'd0`、`pre_data_in[15:0],1'd0`、`15]}},pre_data_in[15:0]}`；不从323图补写本图边界外的字。

可见标签：`cfg_pflt_idat_gain_adj[1:0]`、`19bit`、`round`、`17bit`、`sat`、`flt_dat_in[15:0]`、`s(16,0)~s(16,3)`、`缩放之后数据范围`；选择器0、1、2、3。

原图红色批注：

> 定标指示一个示意表示，为了在原有的基础上改动小一点，在此重新定标为s(16,15)，实在不理解，可以理解为把上面的16bit输入到下面的一个滤波器系统中

### 本图完整可见的乘加与寄存器区

| 原图区域 | 可辨原标签及图形连接索引 |
|---|---|
| 乘法输入 | `flt_cal_dat[flt_idx][15:0]`、`s(16,15)`；另一输入`flt_coeff[flt_idx][15:0]` |
| 乘法输出 | `s(32,30)` → `flr` → `s(24,22)`；红字`补两位符号位`；`s(26,22)`到加号 |
| 反馈选择 | `flt_cal_st`；0为反馈线，1为`26'd0`；`s(26,22)` |
| 累加 | `flt_acc`、`s(27,22)`；分别进入`wrap`与`sat` |
| 输出选择 | `wrap`到0，`sat`到1；`cfg_pflt_clip`；输出`s(26,22)` |
| 结果寄存器及输出 | `D`、`Q`、`en`、`flt_cal_en`；Q端`flt_cal_dat_o_pre[25:0]`，下方`s(26,22)`；同一Q线向上反馈 |
| 左下取景边缘 | `flt_acc[26]`、`flt_ovf`及部分异或/与门；下部输入和后续路径未拍全 |

原图红色批注：

> 根据滤波器的系数来确定乘加的次数

> 来源关系：本图与323图的输入缩放/红色批注/乘加/反馈选择重叠区域文字和拓扑一致；本图向右拍全了结果网名。但没有页码、文件标题或版本号，不能凭重叠区域宣布整份资料同版。

## 来源A03：`GameViewer_lHuv0AHt75.png`

[查看原始PNG](../images/GameViewer_lHuv0AHt75.png)

### 输入缩放（放大取景）

```text
0  {pre_data_in[15:0],3'd0}
1  {{1{pre_data_in[15]}},pre_data_in[15:0],2'd0}
2  {{2{pre_data_in[15]}},pre_data_in[15:0],1'd0}
3  {{3{pre_data_in[15]}},pre_data_in[15:0]}
cfg_pflt_idat_gain_adj[1:0]
```

输出链路可见标签：`19bit`、`round`、`17bit`、`sat`、`flt_dat_in[15:0]`；原图红字`s(16,0)~s(16,3)`、`缩放之后数据范围`。

原图两处红色批注：

> 对输入数据进行缩放
>
> 定标指示一个示意表示，为了在原有的基础上改动小一点，在此重新定标为s(16,15)，实在不理解，可以理解为把上面的16bit输入到下面的一个滤波器系统中

底边可见`flt_cal_dat[flt_idx][15:0]`、`s(16,15)`及其箭头；右缘仅剩另一处`s(2…`，不补齐。

> 来源关系：与323图输入缩放和红色批注相同局部的放大视图；当前截图没有拍到完整乘加器。所有图号、原文页码、标题在本图均未见，不能编造。

## 来源A04：`GameViewer_T5Wi63Rflj.png`

[查看原始PNG](../images/GameViewer_T5Wi63Rflj.png)

### 溢出与输出移位

左上可见`flt_acc[26]`、`flt_acc[25]`进入异或图形，其输出和`flt_cal_en`进入与门，输出名`flt_ovf`。上边缘可见上一选择局部的`sat`、`1`、`s(26,22)`和`cfg_pflt_clip`，其余在画外。

右上另有图示：`s(26,22)` → `<<R` → `s(26,22-R)` → `s(26,15)`；旁边红字`合并`及弯箭头。

八路移位选择的全部原式：

```text
7  {flt_cal_dat_o_pre[25:0]}
6  {{1{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:1]}
5  {{2{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:2]}
4  {{3{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:3]}
3  {{4{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:4]}
2  {{5{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:5]}
1  {{6{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:6]}
0  {{7{flt_cal_dat_o_pre[25]}},flt_cal_dat_o_pre[25:7]}
cfg_pflt_r_arg[2:0]
```

选择输出`s(26,15)`分向浅蓝`sat`和`wrap`；`sat`对应0、`wrap`对应1；浅蓝选择端`cfg_pflt_acc_out_wrap_sel`；输出`flt_cal_dat_o[15:0]`，下方`s(16,15)`。

原图红色批注：

> 定标指示一个示意表示，为了在原有的基础上改动小一点，在此重新定标为s(16,2)，实在不理解，可以理解为从滤波器系统中输出一个16bit数据

> 转录注：图内输出定标`s(16,15)`与批注重定标`s(16,2)`各自保留，不调和。浅蓝输出选择作为本图标记记录；本图没有6601颜色声明或版本号，不单凭颜色增加一项确定6601功能修改。上下左右画外路径不补画。

## 来源A05：`GameViewer_q40E10cbND.png`

[查看原始PNG](../images/GameViewer_q40E10cbND.png)

### 全图文字与连接索引

| 原图区域 | 原始文字 |
|---|---|
| 左侧模拟通道 | `Chan 0`、`Chan 1`、点列、`Chan N`；`采样通道选择` |
| 模拟相关块 | `SARADC CALC`；`SH`；`SARCORE` |
| 模拟/数字交互信号 | `ready`、`data`、`busy`、`done`、`trigger` |
| 左下数字控制 | `SARADC CTRL`；`触发信号管理`；`校准、预处理、滤波、缓存控制` |
| 校准 | `校准通道`；`CAL` |
| 预处理 | `预处理通道`；`PChan 0`、`PChan 1`、点列、`PChan M` |
| 预处理滤波 | `预处理滤波通道`；`PFChan 0`、`PFChan 1`、点列、`PFChan M` |
| 上方缓存 | `缓存通道1`；`BChan 0`、`BChan 1`、点列、`BChan M` |
| 下方滤波 | `滤波通道`；`FChan 0`、`FChan 1`、点列、`FChan K` |
| 下方缓存 | `缓存通道2`；`BChan 0`、`BChan 1`、点列、`BChan M` |
| 最右输出 | `To CPU/DMA` |
| 原图图例 | 绿色块`模拟电路`；浅灰蓝块`数字电路` |

原图主链的连线索引：SARCORE的数据线到CAL；CAL后接预处理通道，随后接预处理滤波通道，再接缓存通道1；预处理输出另分向下方滤波通道，再接缓存通道2；两组缓存均向最右`To CPU/DMA`。控制线、双向箭头、无字端口、虚线边框及点列仍以本张PNG为准，不给无字箭头自造信号名。

> 转录注：原图无封面标题、页码或图号；当前小节标题只是来源索引，不是原作者文档标题。颜色有明确“模拟电路／数字电路”图例，不能将绿色模拟块当成6601新增标记。

## 第二部分：本批辅助图标记索引

| 来源位置 | 原文／标记 | 可确定的性质与限制 |
|---|---|---|
| A01、A03输入 | `对输入数据进行缩放`；`缩放之后数据范围`；`19bit`、`17bit`、`s(16,0)~s(16,3)` | 红色批注/定标；各原式在对应来源正文完整保留，原始版本未明，不冒充6601新增 |
| A01～A03重定标 | `定标指示一个示意表示……一个滤波器系统中` | 完整原句见各来源；相同局部多次截图，不计为多项功能 |
| A01、A02乘加 | `补两位符号位`；`根据滤波器的系数来确定乘加的次数` | 红色解释性批注；原文字照录 |
| A04输出 | 浅蓝`sat`、`wrap`、0/1、`cfg_pflt_acc_out_wrap_sel`；红字`合并`和重定标批注 | 与原定标同时保存；版本归属未由本图声明，不能机械认定新增功能 |
| A05图例 | 绿色`模拟电路`；浅灰蓝`数字电路` | 电路类别图例，不是变更图例 |

## 第三部分：尚未整图核对的旧稿（仅历史暂存，不作为准确正文）

以下保留旧稿三张的字节，明确不作本轮验收；另外三张旧稿没有来源块，列为缺失待转录。后续直接在本文件相应区域更新，不另造最终稿。

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


## 旧稿缺失的三张来源（待整图核对）

- [GameViewer_c74Kardt0X.png](../images/GameViewer_c74Kardt0X.png)：本批未整图核对，不能从文件名推断内容。
- [GameViewer_qNBgXqkj5C.png](../images/GameViewer_qNBgXqkj5C.png)：本批未整图核对，不能从文件名推断内容。
- [GameViewer_Wb2pLAEGMa.png](../images/GameViewer_Wb2pLAEGMa.png)：本批未整图核对，不能从文件名推断内容。
