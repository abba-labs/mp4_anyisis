# ET6601截图还原接续入口

更新：2026-10-05。唯一工作分支：`docs/restore-6601-screenshots`。

## 当前接续摘要

**SARC第三轮完成第15～31张17张新核对，方案设计累计31/40张首轮原图核对；末9张未核对。下一张第32张GameViewer_iSOJmCn28m.png。** 正文和记录已形成发布稿；实际入库与完整字节回读以本轮REMOTE_SAVE回执为准，不能仅依靠该句称已提交。

- 正文：`6601芯片截图/sarc/sarc_lld/docs/SARC_LLD设计文档.md`，保持一份原始文档《SARC模块方案设计》。
- 输出106097字节，blob `dfe3dc2a6f70183888289d96c8768517be107c56`；SHA-256 `1190fc86ce592af28f4258511a8c0d530469eb9d59637d0ae8310ffc1b7578e6`。
- 来源PNG固定于`d80a74e83e4bf942905844e61efd5d169e37c815`；输入head `3d8da927cc13d4f8b6edd4d48001f2769f8365b7`，输入正文blob `064e09e52bfdb767785d2be156619fec1463628a`。
- 新增25条C16～C40，LLD累计40条；其它标记B01～B13。LRS32＋LLD40共72条是原图位置数，不是独立功能数。
- 原U01～U07未关闭，本批新增U08～U12；已核对区12组局部缺口，不是12个字，也不是整份LLD只有这些问题。
- 全仓首轮104/200；SARC相关44/64。辅助图四张中的局部同源比对不增加整图完成数；XBAR27独立管理。

## 必读与下一入口

先读根AGENTS与`6601芯片截图/AGENTS.md`；然后读本交接、RESTORE_PROGRESS及：

- `6601芯片截图/reviews/SARC_LLD_ROUND3_REVIEW_20261005.md`
- `6601芯片截图/reviews/SARC_LLD_ROUND3_IMAGE_LEDGER_20261005.json`
- `6601芯片截图/reviews/SARC_LLD_ROUND3_VERIFY_20261005.json`
- `6601芯片截图/sarc/SARC_提取与验收报告.md`、`SARC_6601修改点总览.md`

第32张路径：`6601芯片截图/sarc/sarc_lld/images/GameViewer_iSOJmCn28m.png`。衔接第31张5.17滤波通道，不重新从第15张或封面开始；剩余32～40张暂排顺序仍须看图确认。

## 已确认的顺序和不能重做/猜补的事项

本轮已确认：`UFTfaW6Wm8 → Ef2CwLAmR0 → vZO2NlUXdv → PecSuT1xBB → SeEx4da40l → pVe1evLu6f → NaDPGTeO6W`。NaDP为阈值6002续页，不得插入FIR段；Pec末句“乘法起的位宽为”必须接SeEx首句“16bit*16bit”。前31张的顺序以ROUND3台账为准，不再使用ROUND2候选顺序。

抢占说明“包含blanking情况的冲突”是删除线；preemtive_md、各处priority变体、sarc_smaple_ctrl、SOFT_TRIGER/soft_trigger、cfg_pflt_p_num/cfg_pflt_num等照录。27bit/36bit、重复5.14.1/5-18/5-19/5-20和5-x不自行统一。6001/6002历史功能不冒充6601新增；浅蓝/清绿按原文件声明处理。

辅助图323Uh2DKeH中央乘加、T5Wi63Rflj底部输出选择与第29张对应局部相符，仅用于局部辨字；外围附加红字不并入正文。9akceoHcVF滤波框对应，但其校准offset为15bit、正文第24张5bit，不相互覆盖；抢占功能.png与正文图反馈路径不同，也不能直接代换。

## 来源与保存规则

源包`mp4_sarc_originals_d80a74e.zip`及历轮交付包含sarc目录91张原始PNG。源Actions run37255121805、artifact11321169896有过期时间；先检查当前实际挂载，不能假定路径永久存在。源包里的Markdown可能过时，不能覆盖最新分支正文。

所有写入只在本分支；先核对当前blob，冲突重读，不force。先正文和来源/状态同批保存，再逐字节回读并记录REMOTE_SAVE。原图哈希、链接、表格列数及工作流成功不是字符准确率证明。不能为消除待办而猜字或删除缺口。

EFC两份正文及5组缺口保持；SARC LRS13张与3组缺口保持。原LRS blob `8be5907f70ba32412ffff63d752b60c1af583089`，EFC LLD `1d8a31f2411d177c628d002e3af842a0456857a7`、EFC LRS `2d83890325cfcb5b262f51ce52434ba90aa2f72b`。CPLD_INTERFACE已经统一，不重复拆合。
