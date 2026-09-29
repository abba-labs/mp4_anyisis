# 2950 同次 PP-Structure 轨迹观测（P0）

- RUN_ID: 2026-09-29_1215_testvm01_2920
- 输入帧: frame_00002920.png sha256=567bd31e2447165c93aaee349869edf4c0eb28b16d0137db70799214fb083cb7
- 配置: NativeParser(mobile, threads=2, table_mode=default, cpu, mkldnn)
- fingerprint: 95722b9b5f3239f4acdb605007ff6ed4c06d4eb47526d7eeddf2b2760c186e91
- 版本: {"paddleocr": "3.7.0", "paddlepaddle": "3.2.2", "paddlex": "3.7.2", "python-docx": "1.2.0"}
- 总耗时: 47.3s（含模型下载/初始化）
- hook 命中: standardized_data x1
- GeneralOCR 返回行数(入口): 32；出口行数: 33
- 轨迹事件数: 0

## 首行 [197,146,1082,169] 的命运
- 入口索引: None
- 入口文字: None
- 入口分数: None
- 出口文字: None
- 是否被置空: None

## 置空事件（rec_texts 按索引写入）

## 入口->出口被置空的行（入口非空、出口为空）
- idx=14 score=0.9247 box=[978.0, 320.0, 1095.0, 399.0] text=26-09-27-20:14

## 与首行框相交的布局框（入口）
- box_idx=4 label=text coord=[186.59005737304688, 0.7673721313476562, 1082.27734375, 225.72213745117188] score=0.6184247136116028

## 最终产物
- native json: adapter.json
- 最终索引: None 文字: None
- 首行是否在 md(全文): False
- 首行是否在 md(核心子串): True
- 续行是否在 md: False

## bystander guard 上报
- 拦截的旁观者置空: 0
- 详情: []
