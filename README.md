# MP4 Analysis: Technical Screen Recording to Structured Document Engine

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-V2%20Refactoring-orange.svg)](REFACTOR_PLAN.md)

> 面向授权技术录屏、工程规格白皮书与寄存器映射表的**高质量视频转结构化文档重构系统**。

---

## 📌 项目定位与架构原则

在工程研发与技术归档场景中，很多核心技术文档以屏幕演示、视频录屏形式留存。从高密度长视频（包含滚动文本、复杂表格、跨屏长流程图、电路架构与波形图）中无损恢复出结构化工程资料，具有极高的工程价值。

经过 V1 原型的实践与深度复盘，系统确立了**“做精视频时序重建，善用成熟文档解析”**的 V2 架构体系：

```
MP4 Video
   │
   ▼
[视频时序与场景切分] (Timeline & Scene Segmentation)
   │
   ▼
[动态锐度筛选] (Laplacian Sharpness Quality Filter)
   │
   ▼
[高精度位移注册与页面重构] (Registration & Page Reconstruction)
   │
   ▼
Reconstructed Clean Page Images (去重高清页面流)
   │
   ▼
[工业级文档解析引擎] (PP-StructureV3 / Docling / MinerU)
   │
   ▼
[统一中间表示层 Document IR] (包含数据溯源 Provenance & Bounding Box)
   │
   ▼
[多格式导出层与审计] (Markdown / JSON / DOCX / XLSX / report.json)
```

---

## 🛠️ 模块架构设计

本项目采用高度模块化的分层设计：

```
src/mp4_analysis/
│
├── cli.py                     # 统一命令行入口
├── pipeline.py                # 端到端全流程调度管道
│
├── video/                     # 视频时序与帧处理
│   ├── decoder.py             # 视频解码与元数据解析
│   ├── timeline.py            # 时间戳与帧映射
│   ├── scene_detector.py      # 静止/滚动/翻页/跳转场景识别
│   └── frame_selector.py      # 拉普拉斯方差流式锐度优选
│
├── reconstruction/            # 画面配准与页面重构 (核心壁垒)
│   ├── registration.py        # 1D 归一化互相关位移计算
│   ├── scroll_detector.py     # 滚动物理连续性检测
│   ├── stitcher.py            # 跨帧长图无缝自适应缝合
│   └── page_builder.py        # 去重页面集合组装
│
├── document/                  # 文档模型与处理
│   ├── models.py              # Document IR 统一中间表示 (Pydantic)
│   ├── layout.py              # 版面元素识别与分流
│   ├── ocr.py                 # 字符级高精识别与置信度计算
│   └── table.py               # 跨屏长表格结构与表头对齐
│
├── backends/                  # 成熟开源解析后端适配器
│   ├── rapidocr_backend.py    # 本地轻量化 RapidOCR / RapidLayout 后端
│   ├── docling_backend.py     # Docling 统一文档模型适配器
│   └── ppstructure_backend.py # PP-StructureV3 工业级结构化解析后端
│
├── exporters/                 # 结构化导出器
│   ├── markdown.py            # 纯净结构化 Markdown 导出
│   ├── json.py                # 包含完整溯源信息的 Document IR JSON
│   ├── xlsx.py                # 寄存器与数据表格 Excel 导出
│   └── docx.py                # Word 工业级排版与高清图回嵌
│
└── quality/                   # 准确率审计与可追溯性
    ├── verifier.py            # 数据一致性校验器
    └── report.py              # report.json 审计报告生成器
```

---

## 📋 研发任务与重构路线

本项目目前正按 **`REFACTOR_PLAN.md`** 进行标准化重构，任务优先级详见 **`TASKS.md`**：

* **Phase 1 (P0)**: 修复抽帧流尾部丢失缺陷，移除不合理的字符黑名单，实现最小闭环：`MP4 → Page Images → Document IR → Markdown / JSON`。
* **Phase 2 (P1)**: 攻坚跨屏长表格矩阵重建，接入 `xlsx` 导出与 `report.json` 数据溯源审计报告。
* **Phase 3 (P2)**: 完善 `docx` 高保真排版与针对低置信度数据的靶向多模态复核。

---

## 📄 规范与免责声明

本项目仅用于技术研究与有合法授权的录屏资料分析、文档恢复与无损归档。严禁用于规避任何计算机安全控制或未经授权的数据复制。
