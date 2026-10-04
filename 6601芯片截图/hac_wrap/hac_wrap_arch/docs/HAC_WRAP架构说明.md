# HAC_WRAP 顶层架构图

> 来源：原始截图精准还原  
> 原图：../images/GameViewer_tVxXq4JUXF.png  
> 说明：该截图同时给出了 6801 HAC_WRAP 与 6601 HAC_WRAP。复杂框图以原图为准；下文只转录截图中可明确辨认的文字与差异，不补充设计解释。

## 第一部分：原始文档正文

> 📌 【原图引用】HAC_WRAP 架构对比图：../images/GameViewer_tVxXq4JUXF.png

### 6801 HAC_WRAP

- AHB_BUS2, 32bit, 200MHz
- To CPUx_SUB
- SARC 0~2
- WAG
- QEP 0~5
- SDFM 0~3 (16ch)
- CMPC 0~10 (22ch)
- DACC 0~1
- AHB_BUS1, 32bit, 200MHz
- XBAR
- ETIM 12ch
- SRPWM
  - SuperPWM BC
  - spwm_wave_gen
  - SuperPWM 0~17
  - SuperPWM Com
- CLB

图内标题：6801 HAC_WRAP

### 6601 HAC_WRAP

- AHB_BUS2, 32bit, 200MHz
- To M7_WRAPx
- SARC 0~1
- WAG
- CMPC (2ch)
- CMPC_lite 0~9 (20ch)
- AHB_BUS1, 32bit, 200MHz
- ETIM 14ch
- SRPWM
  - SuperPWM BC
  - spwm_wave_gen
  - SuperPWM 0~11
  - SuperPWM Com
- ctrl
- AHB2to1
- cfg
- H2H(V/2)
- CPLD

截图中 XBAR、CLB 以及部分 6801 侧模块在 6601 图中以浅灰/淡化方式显示；其精确连接关系以原图为准。

图内标题：6601 HAC_WRAP

## 第二部分：截图中明确标出的 ET6601 修改点

以下差异均直接来自同一张截图对 6801 HAC_WRAP 与 6601 HAC_WRAP 的并列展示。

| 位置 | 6801 图中内容 | 6601 图中内容 | 原图 |
|---|---|---|---|
| 上层连接目标 | To CPUx_SUB | To M7_WRAPx | ../images/GameViewer_tVxXq4JUXF.png |
| SARC | SARC 0~2 | SARC 0~1 | ../images/GameViewer_tVxXq4JUXF.png |
| 比较器相关 | CMPC 0~10 (22ch) | CMPC (2ch) + CMPC_lite 0~9 (20ch) | ../images/GameViewer_tVxXq4JUXF.png |
| ETIM | ETIM 12ch | ETIM 14ch | ../images/GameViewer_tVxXq4JUXF.png |
| SuperPWM | SuperPWM 0~17 | SuperPWM 0~11 | ../images/GameViewer_tVxXq4JUXF.png |
| CPLD | 6801 图中无 CPLD 方框 | 6601 图中新增 CPLD，并显示 ctrl、AHB2to1、cfg、H2H(V/2) 连接 | ../images/GameViewer_tVxXq4JUXF.png |
| QEP / SDFM / DACC | 6801 图中明确显示 QEP 0~5、SDFM 0~3 (16ch)、DACC 0~1 | 6601 图中对应位置未以正常深色模块呈现，部分位置为淡化框 | ../images/GameViewer_tVxXq4JUXF.png |
| XBAR / CLB | 6801 图中正常显示 XBAR、CLB | 6601 图中以淡化方式显示 | ../images/GameViewer_tVxXq4JUXF.png |

> 注意：对于截图中仅以“淡化/灰显”体现的模块，上表只记录视觉事实，不进一步解释其含义。
