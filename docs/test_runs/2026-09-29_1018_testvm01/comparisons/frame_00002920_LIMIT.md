# 逐条对照：frame_00002920（LIMIT.05—08）

说明：raw = 本次用 PP-OCRv5_mobile_det/rec 实测的首轮 GeneralOCR；stored = 工件中 PP-Structure 管线存下的 overall_ocr_res（已含重组改写）；md = 同帧重组后的 markdown。检测参数三处一致（736/min/0.3/4000/0.6/1.5，rec_thresh 0.0）。

## LIMIT.05（frame_00002920）

| 阶段 | 框 | 分数 | 文字 |
|---|---|---|---|
| raw GeneralOCR（本次实测） | #8 [192,250,1079,274] | 0.9948 | LRS.SARC.LIMIT.SPEC【05】使用超过16阶FIR滤波时，系统时钟频率必须大于 |
| raw GeneralOCR（本次实测） | #10 [241,297,1080,322] | 0.9807 | ADC工作时钟频率的2倍以上：（2个连续需要FIR滤波处理的采样，需要最 |
| raw GeneralOCR（本次实测） | #12 [243,345,649,369] | 0.9930 | 小间隔FIR滤波阶数个系统时钟周期） |
| stored overall_ocr_res | #8 [192,250,1079,274] | 0.9948 | LRS.SARC.LIMIT.SPEC【05】使用超过16阶FIR滤波时，系统时钟频率必须大于 |
| stored overall_ocr_res | #10 [241,297,1080,322] | 0.9872 | ADC工作时钟频率的2倍以上：（2个连续需要FIR滤波处理的采样，需要最 |
| stored overall_ocr_res | #12 [243,345,649,369] | 0.9930 | 小间隔FIR滤波阶数个系统时钟周期） |
| reorganized md | — | — | ETMC LRS.SARC.LIMIT.SPEC【05】使用超过16阶FIR滤波时，系统时钟频率必须大于ADC工作时钟频率的2倍以上：（2个连续需要FIR滤波处理的采样，需要最小间隔FIR滤波阶数个系统时钟周期）-09-27-20:14101-2201 |

结论：三行文字 raw 与 stored 逐字一致；md 把三行按阅读顺序合并（“需要最”+“小间隔”→“需要最小间隔”正确），但混入水印碎片 ETMC/-09-27-20:14/101-2201。内容无丢失。

## LIMIT.06（frame_00002920）

| 阶段 | 框 | 分数 | 文字 |
|---|---|---|---|
| raw GeneralOCR（本次实测） | #15 [198,395,1081,418] | 0.9886 | LRS.SARC.LIMIT.SPEC【06】ADC校准时，要求软件关闭模拟ADC使能，待校 |
| raw GeneralOCR（本次实测） | #17 [242,442,663,466] | 0.9902 | 准流程完成后再打开模拟ADC使能； |
| stored overall_ocr_res | #15 [198,395,1081,418] | 0.9886 | LRS.SARC.LIMIT.SPEC【06】ADC校准时，要求软件关闭模拟ADC使能，待校 |
| stored overall_ocr_res | #17 [242,442,663,466] | 0.9902 | 准流程完成后再打开模拟ADC使能； |
| reorganized md | — | — | LRS.SARC.LIMIT.SPEC【06】ADC校准时，要求软件关闭模拟ADC使能，待校ETNCU 准流程完成后再打开模拟ADC使能；BTMCU  |

结论：两行文字 raw 与 stored 逐字一致；md 合并两行并混入水印 ETNCU/BTMCU。内容无丢失。

## LIMIT.07（frame_00002920）

| 阶段 | 框 | 分数 | 文字 |
|---|---|---|---|
| raw GeneralOCR（本次实测） | #19 [198,491,1082,514] | 0.9887 | LRS.SARC.LIMIT.SPEC【07】对虚拟通道vc的配置，需要将对应的vcen关闭后 |
| raw GeneralOCR（本次实测） | #21 [240,536,673,563] | 0.9797 | 进行配置，配置完成后再将vcen打开； |
| stored overall_ocr_res | #19 [198,491,1082,514] | 0.9887 | LRS.SARC.LIMIT.SPEC【07】对虚拟通道vc的配置，需要将对应的vcen关闭后 |
| stored overall_ocr_res | #21 [240,536,673,563] | 0.9797 | 进行配置，配置完成后再将vcen打开； |
| reorganized md | — | — | LRS.SARC.LIMIT.SPEC【07】对虚拟通道vc的配置，需要将对应的vcen关闭后进行配置，配置完成后再将vcen打开；12026-09-27-3 |

结论：两处 vcen 在 raw 中已是 vcen（s=0.989/0.980），stored 原样保留，重组未改动下划线；因此 vc_en→vcen 的变化发生在首次 OCR，不在重组阶段。md 合并两行并混入水印 12026-09-27-3。内容无丢失。

## LIMIT.08（frame_00002920）

| 阶段 | 框 | 分数 | 文字 |
|---|---|---|---|
| raw GeneralOCR（本次实测） | #23 [197,587,1080,610] | 0.9925 | LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的 |
| stored overall_ocr_res | #23 [197,587,1080,610] | 0.9926 | LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的 |
| reorganized md | — | — | LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的ETNC  |

结论：首行文字 raw 与 stored 逐字一致（s≈0.993）；md 保留首行并混入水印 ETNC。内容无丢失。
