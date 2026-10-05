# ET6601 截图还原接续入口

2026-10-05，第七轮。仓库`abba-labs/mp4_anyisis`；唯一分支`docs/restore-6601-screenshots`。

## 当前断点

SARC辅助11/11整图首轮已完成；先第六轮5张实际保存回读，再第七轮6张。旧稿缺少的c74、qNBg、Wb2三张已补正文。不要再从辅助首图、方案32/37或封面重做。

下一任务是定点缺口回查：从`6601芯片截图/sarc/sarc_lld/images/GameViewer_v6tUVs7H0k.png`右页表1（LLD-U01）开始。逐项处理LLD U01～U19、LRS U01～U03、辅助U01/U02及来源连续性S01；看不到就保留具体缺口。每4～6张完成实际正文修订/缺口记录/入口保存回读，不只写管理文件。

当前SARC64/64首轮，全仓124/200；余76＝XBAR27＋CPLD48＋HAC_WRAP1。LLD19组＋S01、LRS3组、辅助2组未闭合；EFC5组暂缓。78条确定来源位置，辅助标记另列；不是功能数或最终验收率。

## 读取入口和已保存状态

根AGENTS、本交接、6601芯片截图/AGENTS、RESTORE_PROGRESS；最新`SARC_AUX_ROUND7_REVIEW_20261005.md`、IMAGE_LEDGER、REMOTE_SAVE位于reviews；再读SARC报告/总览及相应完整正文。第六轮内容`817fae5db0e783779962fb98faacce4eacb3418d`、回执`6d1df94a0e4050f762a77ef2b5bee47efd4003c2`；8文件已下载字节比较通过，run37295395216/artifact11338177558。第七轮实际提交及回读见ROUND7_REMOTE_SAVE，不恢复旧传输。

LLD缺口详细位置：U01～U07看ROUND2、U08～U12看ROUND3、U13～U15与S01看ROUND4、U16～U19看ROUND5。辅助U01：qNBg左中系数红色限定字；U02：Wb2下中“同时作为滤波…输入yBUF”中段。三组LRS缺口看报告第一轮。

辅助完整载体仍`6601芯片截图/sarc/sarc_diagrams/docs/SARC功能框图说明.md`。A01～A11仅来源索引，不是原文页序。不能将四幅重叠预滤波图推定整个源文件同版；15bit/5bit、cal_os/cal_offset、抢占ready路径差异均保留。本批未动主LRS/LLD技术正文或PNG。

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
