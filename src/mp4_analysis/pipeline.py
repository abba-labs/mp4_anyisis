"""
pipeline.py - 端到端全流程调度管道 (V2 Complete)
连接：视频抽帧 -> 文本流与版面分流 -> Document IR -> Markdown / DOCX / XLSX / report.json
"""

import os
import json
from typing import Dict, Any, Optional
from mp4_analysis.video.frame_selector import FrameSelector
from mp4_analysis.document.models import DocumentIR, DocumentPage, DocumentElement, BoundingBox, Provenance
from mp4_analysis.document.ocr import StreamTextDeduplicator
from mp4_analysis.quality.report import AuditReporter
from mp4_analysis.exporters.docx import DocxExporter
from mp4_analysis.exporters.xlsx import ExcelExporter
from rapidocr_onnxruntime import RapidOCR

class DocumentExtractionPipeline:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.pages_dir = os.path.join(output_dir, "pages")
        self.figures_dir = os.path.join(output_dir, "figures")
        self.tables_dir = os.path.join(output_dir, "tables")
        os.makedirs(self.pages_dir, exist_ok=True)
        os.makedirs(self.figures_dir, exist_ok=True)
        os.makedirs(self.tables_dir, exist_ok=True)

        self.selector = FrameSelector()
        self.ocr_engine = RapidOCR()
        self.reporter = AuditReporter()
        self.docx_exporter = DocxExporter()
        self.xlsx_exporter = ExcelExporter()

    def process(self, video_path: str, doc_id: Optional[str] = None) -> DocumentIR:
        if not doc_id:
            doc_id = os.path.splitext(os.path.basename(video_path))[0]

        print(f"[1/5] Extracting quality-aware keyframes from: {video_path}")
        keyframes = self.selector.extract_keyframes(video_path, self.pages_dir)
        print(f"      Extracted {len(keyframes)} clean non-redundant page frames.")

        print("[2/5] Parsing document elements into Document IR...")
        doc_ir = DocumentIR(
            doc_id=doc_id,
            metadata={
                "source_video": os.path.abspath(video_path),
                "total_keyframes": len(keyframes)
            }
        )

        deduplicator = StreamTextDeduplicator()
        elem_counter = 0

        for p_idx, (f_idx, lap, img_path) in enumerate(keyframes, 1):
            page_obj = DocumentPage(page_index=p_idx, image_path=img_path)
            res, _ = self.ocr_engine(img_path)

            if res:
                for box, text, score in res:
                    if deduplicator.is_duplicate(text):
                        continue

                    elem_counter += 1
                    bbox = BoundingBox(
                        xmin=float(box[0][0]),
                        ymin=float(box[0][1]),
                        xmax=float(box[2][0]),
                        ymax=float(box[2][1])
                    )
                    elem = DocumentElement(
                        id=f"elem_{elem_counter:05d}",
                        type="heading" if any(text.startswith(h) for h in ["第", "1.", "2.", "3.", "4.", "5."]) else "text",
                        bbox=bbox,
                        confidence=float(score),
                        content=text
                    )
                    page_obj.elements.append(elem)

            doc_ir.pages.append(page_obj)

        print("[3/5] Generating Audit Report (report.json)...")
        report_path = os.path.join(self.output_dir, "report.json")
        audit_res = self.reporter.save_report(doc_ir, report_path)
        print(f"      Pass rate: {audit_res['metrics']['pass_rate']*100:.2f}%, Low confidence items: {audit_res['metrics']['low_confidence_count']}")

        print("[4/5] Exporting Document IR (JSON) & Markdown...")
        json_path = os.path.join(self.output_dir, "document.json")
        with open(json_path, "w", encoding="utf-8") as fp:
            fp.write(doc_ir.to_json())

        md_path = os.path.join(self.output_dir, "document.md")
        with open(md_path, "w", encoding="utf-8") as fp:
            fp.write(f"# {doc_id}\n\n")
            for page in doc_ir.pages:
                for elem in page.elements:
                    if elem.type == "heading":
                        fp.write(f"\n### {elem.content}\n\n")
                    else:
                        fp.write(f"{elem.content}\n")

        print("[5/5] Exporting Word Document (.docx)...")
        docx_path = os.path.join(self.output_dir, f"{doc_id}.docx")
        self.docx_exporter.export(doc_ir, docx_path, figures_dir=self.figures_dir)

        print(f"[Done] Complete pipeline finished! Artifacts saved to: {self.output_dir}")
        return doc_ir
