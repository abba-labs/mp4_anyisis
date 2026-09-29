# 2950 同次 PP-Structure 轨迹观测（P0）

- RUN_ID: 2026-09-29_1215_testvm01_p3
- 输入帧: frame_00002950.png sha256=d2fe16ef0d8c919e3ed9d48cce4d9920f3e95c420a26bc5e1a28802953b86770
- 配置: NativeParser(mobile, threads=2, table_mode=default, cpu, mkldnn)
- fingerprint: 95722b9b5f3239f4acdb605007ff6ed4c06d4eb47526d7eeddf2b2760c186e91
- 版本: {"paddleocr": "3.7.0", "paddlepaddle": "3.2.2", "paddlex": "3.7.2", "python-docx": "1.2.0"}
- 总耗时: 48.0s（含模型下载/初始化）
- hook 命中: standardized_data x1
- GeneralOCR 返回行数(入口): 48；出口行数: 50
- 轨迹事件数: 0

## 首行 [197,146,1082,169] 的命运
- 入口索引: 6
- 入口文字: LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的
- 入口分数: 0.9918525815010071
- 出口文字: 'LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的'
- 是否被置空: False

## 置空事件（rec_texts 按索引写入）

## 入口->出口被置空的行（入口非空、出口为空）

## 与首行框相交的布局框（入口）
- box_idx=3 label=text coord=[192.37451171875, 143.7149200439453, 1087.383056640625, 169.32872009277344] score=0.7425137758255005

## 最终产物
- native json: adapter.json
- 最终索引: None 文字: None
- 首行是否在 md(全文): False
- 首行是否在 md(核心子串): True
- 续行是否在 md: True

## bystander guard 上报
- 拦截的旁观者置空: 3
- 详情: [{"index": 6, "preserved": "LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的"}, {"index": 10, "preserved": "2022年12月22日"}, {"index": 6, "preserved": "LRS.SARC.LIMIT.SPEC【08】ADC数字控制器的使能信号需要早于控制器内的"}]
