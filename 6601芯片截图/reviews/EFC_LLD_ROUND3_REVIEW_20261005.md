# EFC LLD 第三轮原图核对记录

日期：2026-10-05。分支：`docs/restore-6601-screenshots`。

## 1. 结果与范围

本批核对第13～24张原始PNG，共12张。连同第二轮前12张，EFC LLD累计24/36张首轮核对；余下12张保留历史正文，尚未核对。正文保持一份原始文档，不拆成独立最终片段。

正文：[EFC详细设计文档](../efc/efc_lld/docs/EFC详细设计文档.md)。正文提交：`5ebf63883ab20d5bd97fd2fc01bbda7ae10c4679`；blob：`f1d78519289d23f9b8833ba9f02de1cf07fdc20f`，91310字节。已通过GitHub回读确认与本地完整文件一致。

原图来源固定于`db9422fd7345fb0b600c7ac6c9db25a3140344ed`。36张PNG的SHA-256、Git blob和字节数均重新校验，并与当前分支`cca5e7e61c52e6ea01a2801b0ebc1d30dd2a9bc0`的Git清单一致。本批使用原始分辨率图片及局部裁切，不做OCR猜补，不读取其他芯片规格替代原图。

第二轮当时仅本地保存的正文blob`20e4ab07407afae8315a0e2ab3f8151a8b9cef08`已并入本次远端正文。原前12张的内容保留，仅更新范围说明与跨页断点注；未核对的第25～36张正文逐字节保持不变。

## 2. 实质修订

| 范围 | 本批结果 |
|---|---|
| 上电、复位与OTP | 恢复左右页两组`~~nSWBOOT1,nBOOT1~~`删除线；保留31、0等红色下标和双重下标；补回2.2.3.1/2.2.3.2编号及全部ROM/OTP输出信号 |
| 访问保护 | 恢复七条读写/擦除保护规则、全片擦除五步及indcmd_subtype三个字段；标清rom_rd_en和sysc_boot_exit_lockj的红字来源 |
| Cache/ECC | 衔接Cache七项说明与ECC/RD_DMUX跨页句；READ/RECALL与VREAD_CHK青蓝字单列，不冒充明确新增功能 |
| FCTRL接口 | 表2-1共34个信号行，命令/数据字段完整保留；正文25～200MHz与接口表25～100MHz分别照录 |
| 图中文字 | 补充图2-3～2-14的可辨文字、状态、条件和原图链接；另转录无编号电源时序图标签。不以“图号覆盖”宣称所有小字已完整 |
| Read优化 | 核对第24张明确的读采样修改与tMH/tMS问题；两行时序表按5列恢复并保留空列，不擅自定义min/max列 |
| 修改点 | 新增C16～C41共26条来源出现位置记录，累计41条；另有B01～B05共5条蓝字说明。证据数不是独立功能修改数 |

## 3. 第13～24张逐图来源与结果

| 顺序 | 原图 | Git blob | 本批核对范围 |
|---:|---|---|---|
| 13 | [GameViewer_9TPJx3syGF.png](../efc/efc_lld/images/GameViewer_9TPJx3syGF.png) | `225b0867a37eaece511475b3849f65253824af2a` | 续接NVR_EFUSE_PROC；图2-3；AXIM两级FIFO说明；POWER/RESET黄色框；LLD-U02 |
| 14 | [GameViewer_Fio2eDanFe.png](../efc/efc_lld/images/GameViewer_Fio2eDanFe.png) | `c61d27c3033a8cbbf38772f59dcf271f17675ad5` | 图2-4/2-5；恢复左右页两组nSWBOOT1,nBOOT1删除线；C16～C23；LLD-U03 |
| 15 | [GameViewer_AUvuEbreZL.png](../efc/efc_lld/images/GameViewer_AUvuEbreZL.png) | `d89b88139e32283155af59bc2e43563b26dfb8c0` | 2.2.3.1/2.2.3.2编号、ROM/OTP全部输出；仲裁与保护模块原文差异；C24～C27 |
| 16 | [GameViewer_xLTLahbgSa.png](../efc/efc_lld/images/GameViewer_xLTLahbgSa.png) | `6a4799749ed4b3c6e201eb0794ae622286ecc2cc` | 七条保护规则、全片擦除五步、indcmd_subtype三个字段；C28～C33 |
| 17 | [GameViewer_QiBBFQjMG4.png](../efc/efc_lld/images/GameViewer_QiBBFQjMG4.png) | `597dd04ddd88ea1cc988e94f31590985ded434b4` | bootrom限制续句；图2-6六状态；Cache第1～5项；C34～C35；LLD-U04 |
| 18 | [GameViewer_Pi2p76SFY0.png](../efc/efc_lld/images/GameViewer_Pi2p76SFY0.png) | `fc329d8945a80d675f277049ff07a0424733bffb` | Cache第6～7项；图2-7五状态；ECC路径完整段；B03～B04；LLD-U05 |
| 19 | [GameViewer_zQvGQlgTkE.png](../efc/efc_lld/images/GameViewer_zQvGQlgTkE.png) | `d454ad8595024b8ad57b7f1b003a2b73bc548bda` | 图2-8；表2-1前7行、命令全部位段；C36；25～200与25～100MHz差异保留 |
| 20 | [GameViewer_GsJtl9ctbU.png](../efc/efc_lld/images/GameViewer_GsJtl9ctbU.png) | `754c9fa78f07913f9e8b07ee9363e8831747694b` | 表2-1续27行，合计34信号行；无编号电源时序图信号和时间标签 |
| 21 | [GameViewer_ceValKI1oj.png](../efc/efc_lld/images/GameViewer_ceValKI1oj.png) | `76784d103bf9072de2c5a4d5ffb42793cb8674b0` | 图2-9四状态；B05；图2-10可辨内容；LLD-U06 |
| 22 | [GameViewer_l6EdkNy5JN.png](../efc/efc_lld/images/GameViewer_l6EdkNy5JN.png) | `581f4925be8a1dbba4f89b4e4222a2564f2107c1` | 三段正文；图2-11十三状态与可辨条件；LLD-U07 |
| 23 | [GameViewer_Apm6lwGGlA.png](../efc/efc_lld/images/GameViewer_Apm6lwGGlA.png) | `1c243a0373572c5196ce48699c3a3b0658f47aac` | 36bit两次写说明；图2-12六状态/图2-13七状态；LLD-U08 |
| 24 | [GameViewer_xS9sUaBAU3.png](../efc/efc_lld/images/GameViewer_xS9sUaBAU3.png) | `5dd382a5922b4c9411c130b89cd223486a9e40ab` | 图2-14四状态与小字登记；五列表格tMS/tMH；C37～C41；LLD-U09 |

## 4. 未解决项

目前LLD共9组未解决项，其中U01继承第二轮，U02～U09本批登记。每组可能包含多个字符/条件，不能说成仅剩9个字。看不清处均保留原图及可辨片段，不用状态机常识猜补，不阻塞其他页面。

| 编号 | 具体位置 | 仍待确认内容 |
|---|---|---|
| LLD-U01 | 第5张，图1-2 | 分区容量、部分引脚名及总线下标；继承第二轮未解决项 |
| LLD-U02 | 第13张，右页下方黄色框首行 | 复位修饰文字不清 |
| LLD-U03 | 第14张，左页图2-4条件 | _fctrl_state前缀l/1不可区分 |
| LLD-U04 | 第17张，图2-6 | WAITING→IDLE条件前缀及WR框局部文字 |
| LLD-U05 | 第18张，图2-7 ST_UPT_STS | 最后一行英文小字 |
| LLD-U06 | 第21张，图2-10 | 状态名前缀、自环条件及retry判断操作符 |
| LLD-U07 | 第22张，图2-11 | PROG0/PROG1/PRE1/PROG3括号内时序名 |
| LLD-U08 | 第23张，图2-12/2-13 | START/RLS等状态括号内的细小时序名 |
| LLD-U09 | 第24张，图2-14及两幅波形/参数表 | 复合条件、部分细小数据值与参数表；不是只有一个字符 |

原文自身差异另行保留，不算待识别字符：第13/15张仲裁源和选择信号不同；GFB_PWR_WORKING与GFB_RST_WORKING、hard_arst_n与正文por_rst_n不同；EFC_CFG_PROC_PROT/GFB_CFG_PROC_PROT、FCTRL_FLASH_IF/FCTRL_GFB_FLASH_IF不同；图中ERAERS、RD_ST_CHANGED、tmh_cnt/mh_cnt按原图保留。不得因技术理解自动统一。

## 5. 保存与验收边界

36个图片锚点顺序、来源链接、表格列数、34行接口表、41条证据编号、5条蓝字编号、删除线、未核对正文保留及完整文件blob检查已执行。机器检查只能证明对应范围和保存完整性，不能证明逐字符100%准确。

首次远端保存时全文比对发现未处理尾段一处AXI被误转写为APB，未予通过；已定点恢复原尾段并回读到预期blob。修复工作流完成后已删除自身；该次额外artifact上传因隐藏目录排除而失败，未将其标为成功，正文提交和后续GitHub回读已独立成功。具体证据见同目录`EFC_LLD_ROUND3_SAVE_VERIFY_20261005.json`。

整份LLD和全仓均未最终验收。本轮没有硬件测试。下一张固定为第25张`GameViewer_Jv14xpHsSC.png`：问题单、READ MODE CHANGE等待tMH批注与代码截图；之后继续26～36张。不要重新从封面开始。
