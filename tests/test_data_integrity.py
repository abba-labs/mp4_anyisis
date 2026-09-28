"""Data-integrity regressions. No OCR model, network or private video required."""

import json
import math
import pytest

from mp4_analysis.document.models import DocumentElement, DocumentIR, DocumentPage
from mp4_analysis.document.ocr import StreamTextDeduplicator, string_similarity
from mp4_analysis.quality.report import AuditReporter


@pytest.mark.parametrize("lines", [
    ["ADDR = 0x2800", "ADDR = 0x2808"],
    ["cfg_efc_timing_r[447:0]", "cfg_efc_timing_r[441:0]"],
    ["0", "0", "1", "1", "A", "A"],
    ["字段说明", "字段说明及取值范围"],
    ["第1章 系统架构", "第2章 系统架构"],
    ["enable = 1", "enable = 0"],
    ["    begin", "begin"],
])
def test_unlocated_content_is_never_deleted(lines):
    dedup = StreamTextDeduplicator()
    assert [dedup.is_duplicate(line) for line in lines] == [False] * len(lines)


@pytest.mark.parametrize("blank", ["", " ", "\t\n"])
def test_blank_lines_may_be_ignored(blank):
    assert StreamTextDeduplicator().is_duplicate(blank)


def test_only_identical_observation_at_same_source_can_be_deduplicated():
    dedup = StreamTextDeduplicator()
    assert not dedup.is_duplicate("0", source_key="segment1/row1/col1")
    assert not dedup.is_duplicate("0", source_key="segment1/row2/col1")
    assert dedup.is_duplicate("0", source_key="segment1/row1/col1")
    assert not dedup.is_duplicate("1", source_key="segment1/row1/col1")
    assert not dedup.is_duplicate("0", source_key="segment2/row1/col1")


def test_indentation_is_not_erased_even_at_the_same_source():
    dedup = StreamTextDeduplicator()
    assert not dedup.is_duplicate("    begin", source_key="block1")
    assert not dedup.is_duplicate("begin", source_key="block1")


def test_observation_cache_is_bounded():
    dedup = StreamTextDeduplicator(window_size=2)
    for n in range(3):
        assert not dedup.is_duplicate(str(n), source_key=str(n))
    assert len(dedup.history) == 2
    assert not dedup.is_duplicate("0", source_key="0")


def test_similarity_helper_still_available_but_not_deletion_authority():
    assert string_similarity("ADDR = 0x2800", "ADDR = 0x2808") > 0.85
    assert string_similarity("", "") == 1.0


def make_document(scores):
    elements = [DocumentElement(id=str(i), type="text", content="0", confidence=s)
                for i, s in enumerate(scores)]
    return DocumentIR(doc_id="test", pages=[DocumentPage(page_index=1, elements=elements)])


@pytest.mark.parametrize("doc", [DocumentIR(doc_id="empty"), make_document([])])
def test_empty_output_is_not_a_success(doc):
    report = AuditReporter().generate_report(doc)
    assert report["status"] == "NO_CONTENT"
    assert report["metrics"]["average_confidence"] is None
    assert report["metrics"]["pass_rate"] is None
    assert report["metrics"]["confidence_threshold_coverage"] is None
    assert report["audit_flags"]["requires_manual_inspection"] is True
    assert report["audit_flags"]["risk_level"] == "HIGH"


def test_high_ocr_confidence_is_not_accuracy_or_completeness():
    report = AuditReporter().generate_report(make_document([0.99]))
    assert report["metrics"]["confidence_threshold_coverage"] == 1.0
    assert report["audit_flags"]["accuracy_verified"] is False
    assert report["audit_flags"]["completeness_verified"] is False
    assert report["audit_flags"]["requires_manual_inspection"] is True
    assert report["metrics"]["missing_provenance_count"] == 1


def test_all_low_confidence_items_are_returned_not_only_first_100():
    report = AuditReporter().generate_report(make_document([0.5] * 111))
    assert report["metrics"]["low_confidence_count"] == 111
    assert len(report["low_confidence_items"]) == 111


@pytest.mark.parametrize("bad", [float("nan"), float("inf"), -0.1, 1.1, None, "0.99", True])
def test_invalid_confidence_cannot_be_counted_as_pass(bad):
    report = AuditReporter().generate_report(make_document([bad, 0.99]))
    assert report["metrics"]["invalid_confidence_count"] == 1
    assert report["metrics"]["confidence_threshold_coverage"] == 0.5
    assert report["audit_flags"]["risk_level"] == "HIGH"
    assert report["invalid_confidence_items"][0]["confidence"] is None
    json.dumps(report, allow_nan=False)


def test_empty_page_is_flagged_even_with_other_valid_text():
    doc = make_document([0.99])
    doc.pages.append(DocumentPage(page_index=2))
    report = AuditReporter().generate_report(doc)
    assert report["empty_page_indices"] == [2]
    assert report["status"] == "REVIEW_REQUIRED"
    assert report["audit_flags"]["risk_level"] == "HIGH"


def test_confidence_fraction_denominator_is_all_elements():
    report = AuditReporter().generate_report(make_document([0.9, 0.84, 0.85]))
    assert report["metrics"]["confidence_threshold_coverage"] == 0.6667
    assert report["metrics"]["low_confidence_count"] == 1


def test_saved_report_uses_strict_json_and_preserves_full_issue_list(tmp_path):
    path = tmp_path / "report.json"
    report = AuditReporter().save_report(make_document([0.5] * 111), str(path))
    assert json.loads(path.read_text(encoding="utf-8")) == report
    assert len(report["low_confidence_items"]) == 111


@pytest.mark.parametrize("threshold", [-0.1, 1.1, math.nan])
def test_invalid_threshold_is_rejected(threshold):
    with pytest.raises(ValueError):
        AuditReporter(threshold)


@pytest.fixture
def pipeline_with_fakes(monkeypatch):
    """Exercise real orchestration; mock video/OCR/Word/Excel, not report or IR."""
    import importlib.util
    from pathlib import Path
    import sys
    from types import ModuleType, SimpleNamespace
    import mp4_analysis

    state = {"keyframes": [(47, 12.0, "fixture.png")], "lines": [], "exports": []}

    class FakeSelector:
        def extract_keyframes(self, *_args):
            return state["keyframes"]

    class FakeOCR:
        def __call__(self, _path):
            box = [[0, 0], [100, 0], [100, 10], [0, 10]]
            return [(box, text, 0.99) for text in state["lines"]], None

    class FakeDocx:
        def export(self, doc_ir, output_path, **_kwargs):
            state["exports"].append(output_path)

    dependencies = {
        "mp4_analysis.video.frame_selector": {"FrameSelector": FakeSelector},
        "rapidocr_onnxruntime": {"RapidOCR": FakeOCR},
        "mp4_analysis.exporters.docx": {"DocxExporter": FakeDocx},
        "mp4_analysis.exporters.xlsx": {"ExcelExporter": SimpleNamespace},
    }
    for name, members in dependencies.items():
        module = ModuleType(name)
        module.__dict__.update(members)
        monkeypatch.setitem(sys.modules, name, module)
    path = Path(next(iter(mp4_analysis.__path__))) / "pipeline.py"
    spec = importlib.util.spec_from_file_location("_integrity_pipeline_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.DocumentExtractionPipeline, state


@pytest.mark.parametrize("no_frames", [False, True])
def test_pipeline_empty_result_writes_report_then_fails(pipeline_with_fakes, tmp_path, no_frames):
    pipeline_cls, state = pipeline_with_fakes
    if no_frames:
        state["keyframes"] = []
    pipeline = pipeline_cls(str(tmp_path))
    with pytest.raises(RuntimeError, match="No OCR content"):
        pipeline.process("fixture.mp4")
    report = json.loads((tmp_path / "report.json").read_text(encoding="utf-8"))
    assert report["status"] == "NO_CONTENT"
    assert report["metrics"]["pass_rate"] is None
    assert not state["exports"]
    assert not (tmp_path / "document.md").exists()


def test_pipeline_preserves_address_changes_and_repeated_cells(pipeline_with_fakes, tmp_path, capsys):
    pipeline_cls, state = pipeline_with_fakes
    state["lines"] = ["ADDR = 0x2800", "ADDR = 0x2808", "0", "0"]
    result = pipeline_cls(str(tmp_path)).process("fixture.mp4")
    assert [e.content for p in result.pages for e in p.elements] == state["lines"]
    saved = json.loads((tmp_path / "document.json").read_text(encoding="utf-8"))
    assert len(saved["pages"][0]["elements"]) == 4
    md = (tmp_path / "document.md").read_text(encoding="utf-8")
    assert all(line in md for line in state["lines"])
    assert len(state["exports"]) == 1
    output = capsys.readouterr().out
    assert "Pass rate:" not in output
    assert "not accuracy" in output
