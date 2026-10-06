# ET6601截图还原接续入口

2026-10-06，独立XBAR第5批。仓库abba-labs/mp4_anyisis；唯一工作分支`docs/restore-6601-screenshots`。

## 当前任务

用户已确认SARC主体交付收尾，并明确要求处理XBAR。XBAR前27/27张已完成首轮原图核对；全仓151/200。43条修改来源位置记录，6组局部缺口；数量不是独立功能数或准确率。

XBAR原文封面为《ET6601 XBAR模块需求规格与设计方案》，不是“SARC XBAR总线互联”。保留历史路径`6601芯片截图/sarc/sarc_xbar/docs/SARC_XBAR设计文档.md`作为唯一完整正文；不混入SARC，不拿总线矩阵或其他芯片手册补写。

下一入口：XBAR主体还原和阅读交付已至文末，27张顺序均已按原图内容确认，NY/BJ接口续表已纠正；不重复从封面或旧候选图序重做。先读XBAR导读，取得清晰同版来源后只补对应的6组局部缺口。原图全文逐字最终验收仍未通过。

## 阅读地图

根AGENTS→本交接→6601芯片截图/AGENTS→RESTORE_PROGRESS顶部XBAR当前检查点→XBAR导读／报告／修改总览／逐图台账→对应完整原文章节。

- 6601芯片截图/sarc/sarc_xbar/XBAR_阅读入口与6601修改导读.md
- 6601芯片截图/sarc/sarc_xbar/XBAR_提取与验收报告.md
- 6601芯片截图/sarc/sarc_xbar/XBAR_6601修改点总览.md
- 6601芯片截图/reviews/XBAR_IMAGE_LEDGER_20261006.json
- 6601芯片截图/reviews/XBAR_ROUND5_REMOTE_SAVE_20261006.json

第5批内容提交`34edbb3a269d7456490182d54fc4dd7e4c227f0c`；实际远端回读的9个目标文件已下载并与准备稿逐字节比较一致。原文33～42等内容没有另拆文档；本次发布的临时传输文件和工作流均已删除。本入口收尾更新只澄清已确认图序，不改变原图正文或缺口状态。

## 保存与来源

每4～6张或更小批实际补正文、修改位置、缺口及下一入口，正式写回并回读再继续。写前读最新blob，串行写此分支，冲突重读，不force、不写main。不恢复已发布旧分片；输入head只是来源基线，不据此回退后续修改。

原PNG源包mp4_sarc_originals_d80a74e.zip内sources.zip含独立XBAR27张；源commit d80a74e83e4bf942905844e61efd5d169e37c815。先检查实际挂载，旧ZIP Markdown不得覆盖最新正文。XBAR原图目录Git树91682624c59903a7c29145d22acdd62e20b0bd8e已与源包PNG重建值对齐。无原图走私有Actions导出，不反复UTF-8读PNG，不用OCR替代原图。

一份原文一份Markdown；双页先左后右；保留正文、全表、空白、图标签、删除线及原批注。原文矛盾与拼写照留。不根据常识、ET60157/ET6801手册、驱动或BootROM补字。XBAR红色标记按本原文语境，不机械套用SARC配色。

## 已交付保护范围

SARC三份原始正文、工作链路导读及78条修改来源位置保持；23组局部缺口＋S01仍开放，AUX-U02关闭；主体阅读已交付不等于逐字最终验收。最新回执SARC_DELIVERY_ROUND13_REMOTE_SAVE_20261006.json，交付head 3e8a48de67290bcc02cd66c0e64714e33be40c92。EFC60张首轮、5组缺口暂缓。CPLD48、HAC_WRAP1尚未本任务首轮，CPLD_INTERFACE已合并不重复拆合；CPLD是新IP不编造旧版修改总结。

## XBAR主体阅读交付

现有27张已首轮至文末，先读`6601芯片截图/sarc/sarc_xbar/XBAR_阅读入口与6601修改导读.md`。6组局部缺口留档，不作为主体阅读的统一阻塞；不再从封面或旧候选顺序重做。全仓151/200，剩CPLD48及HAC_WRAP1。用户本轮只要求XBAR，不自动开展下一IP。
