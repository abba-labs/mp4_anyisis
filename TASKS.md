> **历史清单，非当前执行计划（2026-09-28交接说明）**
>
> 以下保留早期任务原文用于追溯，勾选状态没有跟随薄适配版本更新。用户已确认采用三个模块、一个默认开源解析后端，不再推进自建多层IR、通用Office排版器、常驻任务服务等原计划；不得用编辑距离或包含关系直接删除技术文字。当前状态、已完成事项和下一步优先级请读根目录 [NEXT_CHAT_HANDOFF.md](NEXT_CHAT_HANDOFF.md)，特别是第0、6、8节。下一轮先恢复现有SARC缓存并完成剩余26个解析输入，不机械执行下面的历史任务。

# 开发任务清单 (TASKS)

---

## Phase 1: 核心最小闭环 MVP (P0 任务群)
> **目标目标**：跑通 `MP4 → 去重页面图片 → 结构化解析 → Document IR → Markdown / JSON` 真实可用链路。

- [ ] **Task 1.1: 修复抽帧流尾部丢失问题** (`video/frame_selector.py`)
  - [ ] 实现显式 `flush()` 机制，在视频流读取完毕时，必须将最后一个未结算的稳定区间强制输出为关键帧，解决最后一页丢失问题。
- [ ] **Task 1.2: 建立端到端 Pipeline 调度器与 CLI** (`pipeline.py`, `cli.py`)
  - [ ] 编写统一命令行入口：`mp4-analysis input.mp4 -o output/`。
  - [ ] 编排 Video Decoder → Motion Segmentation → Registration → Parsing → IR 整体调用链。
- [ ] **Task 1.3: 废除硬编码字符过滤与单字符丢弃** (`document/ocr.py`, `reconstruction/dedup.py`)
  - [ ] 彻底移除 `'第'`、`'ETMCU'` 等粗暴关键字黑名单；
  - [ ] 废除 `len(clean) < 2` 逻辑，确保单字符寄存器值（`0`, `1`, `A`, `R`, `W`）完整保留；
  - [ ] 实现真正的 Levenshtein 编辑距离算法用于行相似度判定。
- [ ] **Task 1.4: 重构位移注册与拼接容错** (`reconstruction/registration.py`, `reconstruction/stitcher.py`)
  - [ ] 替换固定剪裁坐标（如 `x=200:1000`），采用基于画面相对比例（如 `0.2W ~ 0.8W`）的自适应搜索窗；
  - [ ] 移除匹配失败时盲加 220px 的危险逻辑；匹配失败时输出为独立切片并标记 `confidence=low`。
- [ ] **Task 1.5: 定义统一 Document IR 数据结构** (`document/models.py`)
  - [ ] 基于 Pydantic / dataclass 定义 `Document`, `Page`, `Block`, `Table`, `Figure`, `Provenance` 标准结构；
  - [ ] 实现 Document IR 序列化与反序列化为 `document.json`。
- [ ] **Task 1.6: 接入标准化结构化解析后端** (`backends/`)
  - [ ] 提供基于 PP-StructureV3 / Docling / RapidOCR 的结构化提取适配器；
  - [ ] 输出清晰的 Markdown（`document.md`）。

---

## Phase 2: 表格重构、多格式导出与溯源审计 (P1 任务群)
> **目标**：解决芯片寄存器表等复杂表格的无损重建，提供数据级溯源与质检报告。

- [ ] **Task 2.1: 跨屏长表格矩阵对齐与表头继承** (`document/table.py`)
  - [ ] 识别表格跨屏滚动连续性，跨帧继承首屏表头定义；
  - [ ] 组装标准化三线表矩阵，保留单元格对齐属性。
- [ ] **Task 2.2: Excel 导出引擎** (`exporters/xlsx.py`)
  - [ ] 基于 Document IR 自动生成 `tables/table_xxx.xlsx`；
  - [ ] 保持十六进制地址（`0x0000_0000`）纯文本格式，防止数值截断或科学计数法变形。
- [ ] **Task 2.3: 数据可溯源性与审计报告** (`quality/report.py`, `quality/verifier.py`)
  - [ ] 在提取元素时记录视频起止时间戳（`start_time`, `end_time`）和原始帧坐标 bbox；
  - [ ] 自动生成 `report.json`，主动提取并列出低置信度字符与潜在异常，供人工精准核对。
- [ ] **Task 2.4: 单元测试与基准测试集** (`tests/`)
  - [ ] 编写核心位移计算、文字去重、IR 序列化的单元测试；
  - [ ] 建立基于公开测试视频的准确率与耗时 Benchmark 记录。

---

## Phase 3: 高级多模态审校与复杂排版 (P2 任务群)
> **目标**：追求工业级发布格式与针对低置信度数据的智能微调。

- [ ] **Task 3.1: Word 工业级排版导出器** (`exporters/docx.py`)
  - [ ] 支持等宽代码块高亮封装、三线表规范边框底色、高清自适应满宽插图回嵌。
- [ ] **Task 3.2: 靶向 VLM 增量复核机制** (`backends/vlm_verifier.py`)
  - [ ] 仅针对 `report.json` 中标记的低置信度单元格或模态存疑区域，切出局部微缩图调用多模态大模型进行靶向确认，杜绝全篇长文本幻觉。
- [ ] **Task 3.3: 文件夹静默监听常驻服务** (`cli.py --watch`)
  - [ ] 支持监视指定录屏文件夹，自动排队异步处理新增视频。
