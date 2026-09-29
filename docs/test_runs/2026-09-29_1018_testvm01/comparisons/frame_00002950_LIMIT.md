# 逐条对照：frame_00002950（LIMIT.07—08）

说明同 frame_00002920。

## LIMIT.07（frame_00002950）

| 阶段 | 框 | 分数 | 文字 |
|---|---|---|---|
| raw GeneralOCR（本次实测） | #1 [197,48,1080,74] | 0.9934 | LRS.SARC.LIMIT.SPEC【07】对虚拟通道vc的配置，需要将对应的vcen关闭后 |
| raw GeneralOCR（本次实测） | #3 [241,97,697,121] | 0.9811 | 进配置，配置完成后再将vcen打开； |
| stored overall_ocr_res | #1 [197,48,1080,74] | 0.9934 | LRS.SARC.LIMIT.SPEC【07】对虚拟通道vc的配置，需要将对应的vcen关闭后 |
| stored overall_ocr_res | #3 [241,97,697,121] | 0.9811 | 进配置，配置完成后再将vcen打开； |
| reorganized md | — | — | LRS.SARC.LIMIT.SPEC【07】对虚拟通道vc的配置，需要将对应的vcen关闭后ETNGI 进配置，配置完成后再将vcen打开；CTWCU  |

结论：raw 与 stored 一致，均为“进配置”（缺“行”字，s=0.981），vcen 两处与 2920 相同；因此缺字与下划线变化都发生在首次 OCR，不在重组阶段。md 合并两行并混入水印 ETNGI/CTWCU。

## LIMIT.08（frame_00002950）

| 阶段 | 框 | 分数 | 文字 |
|---|---|---|---|
| raw GeneralOCR（本次实测） | #6 [197,146,1082,169] | 0.9919 | LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的 |
| raw GeneralOCR（本次实测） | #40 [238,585,673,612] | 0.9866 | 其他使能信号（比如vcen等）打开； |
| stored overall_ocr_res | #6 [197,146,1082,169] | 0.9919 |  |
| stored overall_ocr_res | #40 [238,585,673,612] | 0.9866 | 其他使能信号（比如vcen等）打开； |
| reorganized md | — | — | （整条缺失） |

结论：关键差异：raw #6 在框 [197,146,1082,169] 以 s=0.992 正确识别出首行“LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的”；stored 同框 s=0.9919 但文字被置空；md 中整条 LIMIT.08 缺失（含续行 #40“其他使能信号（比如vcen等）打开；”也未进入 md）。结论：首行文字丢失发生在重组/后处理阶段，不是首次 OCR 识别失败（同模型同参数下复测可正确识别）。
