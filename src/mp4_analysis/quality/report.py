"""
quality/report.py - 质量审计与数据可追溯性报告生成器
生成 report.json，主动暴露低置信度字符、边界异常与潜在需复核项
"""

import json
from typing import Dict, Any, List
from mp4_analysis.document.models import DocumentIR

class AuditReporter:
    def __init__(self, confidence_threshold: float = 0.85):
        self.confidence_threshold = confidence_threshold

    def generate_report(self, doc_ir: DocumentIR) -> Dict[str, Any]:
        total_elements = 0
        total_pages = len(doc_ir.pages)
        low_confidence_items = []
        confidences = []
        element_types = {}

        for page in doc_ir.pages:
            for elem in page.elements:
                total_elements += 1
                confidences.append(elem.confidence)
                element_types[elem.type] = element_types.get(elem.type, 0) + 1

                if elem.confidence < self.confidence_threshold:
                    low_confidence_items.append({
                        "id": elem.id,
                        "page_index": page.page_index,
                        "type": elem.type,
                        "content": elem.content,
                        "confidence": round(elem.confidence, 4),
                        "bbox": {
                            "xmin": elem.bbox.xmin if elem.bbox else 0,
                            "ymin": elem.bbox.ymin if elem.bbox else 0,
                            "xmax": elem.bbox.xmax if elem.bbox else 0,
                            "ymax": elem.bbox.ymax if elem.bbox else 0,
                        } if elem.bbox else None
                    })

        avg_conf = sum(confidences) / len(confidences) if confidences else 1.0

        report = {
            "document_id": doc_ir.doc_id,
            "metadata": doc_ir.metadata,
            "metrics": {
                "total_pages": total_pages,
                "total_elements": total_elements,
                "element_distribution": element_types,
                "average_confidence": round(avg_conf, 4),
                "low_confidence_count": len(low_confidence_items),
                "pass_rate": round((total_elements - len(low_confidence_items)) / total_elements, 4) if total_elements else 1.0
            },
            "audit_flags": {
                "requires_manual_inspection": len(low_confidence_items) > 0,
                "risk_level": "LOW" if len(low_confidence_items) < 10 else "MEDIUM" if len(low_confidence_items) < 30 else "HIGH"
            },
            "low_confidence_items": low_confidence_items[:100]  # top items for review
        }
        return report

    def save_report(self, doc_ir: DocumentIR, output_path: str):
        report = self.generate_report(doc_ir)
        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(report, fp, ensure_ascii=False, indent=2)
        return report
