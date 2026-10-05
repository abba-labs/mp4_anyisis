# ET6601 截图还原接续入口

更新：2026-10-05，SARC第四轮。仓库`abba-labs/mp4_anyisis`；唯一工作分支`docs/restore-6601-screenshots`。

## 1. 当前接续摘要

**方案设计已累计前36/40张首轮核对，本批新增第32～36张5张。下一张第37张`GameViewer_cTDH1vvDLo.png`，接5.19 FIFO模式读取采样结果。** 第三轮前31张正文块保持，末4张保留历史稿未核对；不从封面、第15张或第32张重做，不恢复已发布的第三轮分片。

第四轮内容写回与完整字节回读以`6601芯片截图/reviews/SARC_LLD_ROUND4_REMOTE_SAVE_20261005.json`为准；该回执未形成时不能只凭本地VERIFY宣称已发布。

| 范围 | 首轮状态 | 未关闭问题 |
|---|---|---|
| EFC | LRS24/24、LLD36/36 | LLD5组，用户暂缓；未最终验收 |
| SARC LRS | 13/13 | 3组局部缺口，正文未改 |
| SARC模块方案设计 | 36/40 | U01～U15共15组局部缺口；另有来源连续性疑点S01；末4张未核对 |
| SARC辅助图 | 0/11整图 | 四张仅有历史局部对照；边界/版本需核实 |
| 独立XBAR | 0/27 | 不混入SARC正文或修改点 |
| CPLD／HAC_WRAP | 0/48、0/1 | CPLD_INTERFACE已合并，不重复拆合 |

全仓首轮109/200，余91＝LLD4＋辅助11＋XBAR27＋CPLD48＋HAC_WRAP1；SARC相关49/64。来源位置LRS32＋LLD41＝73条，LLD其他记录B01～B15另列。上述数值都不是准确率、独立功能数或硬件通过率。

## 2. 新对话阅读顺序

1. 根`AGENTS.md`、本文件，再读`6601芯片截图/AGENTS.md`和`RESTORE_PROGRESS.md`。子AGENTS第7节仅为历史优先级。
2. 最新`reviews/SARC_LLD_ROUND4_REMOTE_SAVE_20261005.json`、`SARC_LLD_ROUND4_REVIEW_20261005.md`、`SARC_LLD_ROUND4_IMAGE_LEDGER_20261005.json`及`SARC_LLD_ROUND4_VERIFY_20261005.json`（均在`6601芯片截图/`下）。
3. `6601芯片截图/sarc/SARC_提取与验收报告.md`、`SARC_6601修改点总览.md`和唯一完整正文`6601芯片截图/sarc/sarc_lld/docs/SARC_LLD设计文档.md`的续接位置。
4. 历史全会话地图为`6601芯片截图/reviews/CHAT_SESSION_HANDOFF_20261005.md`；U01～U07查ROUND2_REVIEW，U08～U12及前31张顺序查ROUND3_REVIEW/IMAGE_LEDGER。历史“下一张”不覆盖本入口。

## 3. 下一步直接做

`6601芯片截图/sarc/sarc_lld/images/GameViewer_cTDH1vvDLo.png`。

Git blob：`18e667e5bf6c9a4c4f68a02d90cf285c159ddbca`；SHA-256：`4c327d00f6bda1e28e2e1f1e0324e4caa497976c5ed99b6147fdcf22c74a8986`；1241578字节。

候选37～40为`cTDH1vvDLo → m4qMLaqKqw → u5JeUrg4ga → YbkCdqx6qz`（均为GameViewer_*.png），逐图核实顺序。本批保存回读后继续此4张，完成一个正式检查点；复杂图可更小批。随后核对11张辅助图，再用确认同源同版的局部回查SARC疑点。XBAR独立，EFC保持暂缓。

S01来源连续性疑点：第32张iSOJmCn28m界面为61–62，第33张HFc4FYW2ed为65–66，63–64未定位；界面屏幕号不是正文页码，不能仅由跳号断言漏失内容，也不能补出假页。它独立于15组局部字形缺口，后续继续核实。

## 4. 固定规则

一份原始文档＝一份最终Markdown；双页先左后右，按章节、跨页句和续表衔接，不按文件名排序。保留全文、表格空格/合并关系、字段/接口、公式、可辨代码、图名/标签、删除线和原文批注。清除播放器、水印和窗口UI噪声；无法确认处写原图、区域、片段及缺口，不猜补、不删掉、不假关闭。

原文错误、矛盾、编号和拼写照录。IIR“非线性”、s(16,0)/s(15,0)、重复From ids data均已按原处保留。ET60157/ET6801手册、驱动、BootROM和常识不能代替6601原图填字。

SARC浅蓝/清绿色按本文件原文声明归集；历史6001/6002/6801说明和原有图配色不机械当新增。每条来源保留原文、章节、原图及可确定性质；没有旧值不推断。CPLD是新IP，不做旧版变更总结。

每4～6张完成正式检查点：同一完整正文＋修改位置＋台账/缺口＋下一入口，写回并回读后再继续。复杂图可小批；不能只改管理文件、不改正文。写前读取最新blob，串行更新、冲突重读，不force、不写main。优先直接文本更新；大正文不得通过手工整份重发损坏保留区，限定补丁也必须有真实提交和回读。

## 5. 原图及保护锚点

先检查实际挂载，不假定旧sandbox永久有效。SARC源包`mp4_sarc_originals_d80a74e.zip`固定commit `d80a74e83e4bf942905844e61efd5d169e37c815`，源run `37255121805`、artifact `11321169896`（原记录有效期至2026-10-08，使用前检查）。本次已成功取回，含旧sarc目录91张PNG；旧Markdown不能覆盖最新分支。无原图时用已验证的私有Actions原始文件导出通路，不反复UTF-8读PNG、不以缩略图或OCR代替原图。

第三轮已发布：内容提交`1b4c21be8552e16bae915f4dc9aeb9aca0751710`，持久回执`SARC_LLD_ROUND3_REMOTE_SAVE_20261005.json`，发布run `37275692859`/artifact `11329683789`。本次输入HEAD为`11987dcacad0163512f10e22d020bfc41c42326b`；不要回退至交接基线，也不要重复恢复旧传输分片。

SARC LRS blob `8be5907f70ba32412ffff63d752b60c1af583089`；EFC LLD `1d8a31f2411d177c628d002e3af842a0456857a7`；EFC LRS `2d83890325cfcb5b262f51ce52434ba90aa2f72b`。原PNG、LRS、EFC、独立XBAR和辅助图正文保持。

辅助图既有结论：323Uh2DKeH/T5Wi63Rflj只对应第29张部分；9akceoHcVF校准offset为15bit、正文第24张5bit，不覆盖；抢占功能.png反馈路径不同，不直接代换。未取得更清晰同源字形时保持缺口。哈希、链接、图数及workflow通过只证明相应检查，不证明逐字准确或硬件通过。
