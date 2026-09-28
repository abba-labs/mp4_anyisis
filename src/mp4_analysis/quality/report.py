"""Audit observed OCR output without claiming reconstruction accuracy."""

import json
import math
from numbers import Real
from typing import Any, Dict

from mp4_analysis.document.models import DocumentIR


class AuditReporter:
    def __init__(self, confidence_threshold: float = 0.85):
        if not self._valid_confidence(confidence_threshold):
            raise ValueError("confidence_threshold must be finite and between 0 and 1")
        self.confidence_threshold = float(confidence_threshold)

    @staticmethod
    def _valid_confidence(value: Any) -> bool:
        return (isinstance(value, Real) and not isinstance(value, bool)
                and math.isfinite(value) and 0 <= value <= 1)

    def generate_report(self, doc_ir: DocumentIR) -> Dict[str, Any]:
        total_elements = 0
        low_confidence_items = []
        invalid_confidence_items = []
        confidences = []
        element_types = {}
        missing_provenance_count = 0
        empty_page_indices = []

        for page in doc_ir.pages:
            if not page.elements:
                empty_page_indices.append(page.page_index)
            for elem in page.elements:
                total_elements += 1
                element_types[elem.type] = element_types.get(elem.type, 0) + 1
                if elem.provenance is None:
                    missing_provenance_count += 1
                valid = self._valid_confidence(elem.confidence)
                item = {
                    "id": elem.id,
                    "page_index": page.page_index,
                    "type": elem.type,
                    "content": elem.content,
                    "confidence": round(float(elem.confidence), 4) if valid else None,
                    "bbox": vars(elem.bbox).copy() if elem.bbox else None,
                }
                if not valid:
                    item["reason"] = "invalid_or_missing_confidence"
                    invalid_confidence_items.append(item)
                    continue
                confidences.append(float(elem.confidence))
                if elem.confidence < self.confidence_threshold:
                    low_confidence_items.append(item)

        above_threshold = sum(c >= self.confidence_threshold for c in confidences)
        coverage = round(above_threshold / total_elements, 4) if total_elements else None
        has_issues = bool(low_confidence_items or invalid_confidence_items
                          or empty_page_indices or missing_provenance_count)
        status = "NO_CONTENT" if not total_elements else "REVIEW_REQUIRED" if has_issues else "UNVERIFIED"
        risk = "HIGH" if (not total_elements or invalid_confidence_items or empty_page_indices
                           or len(low_confidence_items) >= 30) else "MEDIUM" if has_issues else "UNKNOWN"

        return {
            "document_id": doc_ir.doc_id,
            "metadata": doc_ir.metadata,
            "status": status,
            "metrics": {
                # Compatibility: these are IR containers, not verified original pages.
                "total_pages": len(doc_ir.pages),
                "total_elements": total_elements,
                "element_distribution": element_types,
                "average_confidence": round(sum(confidences) / len(confidences), 4) if confidences else None,
                "low_confidence_count": len(low_confidence_items),
                "invalid_confidence_count": len(invalid_confidence_items),
                "missing_provenance_count": missing_provenance_count,
                "empty_page_count": len(empty_page_indices),
                "confidence_threshold": self.confidence_threshold,
                "confidence_threshold_coverage": coverage,
                # Deprecated alias: OCR confidence fraction, NEVER an accuracy rate.
                "pass_rate": coverage,
            },
            "audit_flags": {
                "requires_manual_inspection": True,
                "risk_level": risk,
                "accuracy_verified": False,
                "completeness_verified": False,
                "original_page_count_verified": False,
            },
            "metric_notes": {
                "pass_rate": "Deprecated alias of confidence_threshold_coverage; not accuracy or completeness.",
                "total_pages": "Number of IR containers; may be keyframes rather than original document pages.",
            },
            "empty_page_indices": empty_page_indices,
            "low_confidence_items": low_confidence_items,
            "invalid_confidence_items": invalid_confidence_items,
        }

    def save_report(self, doc_ir: DocumentIR, output_path: str):
        report = self.generate_report(doc_ir)
        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(report, fp, ensure_ascii=False, indent=2, allow_nan=False)
        return report
