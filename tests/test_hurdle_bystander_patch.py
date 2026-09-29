"""Unit tests for the hurdle-blanking bystander guard.

No models, no paddlex needed: the guarded list is exercised through fake
``standardized_data`` functions (the guard keys off the caller frame's
function name and its ``ocr_idx``/``overall_ocr_idx`` locals, exactly like
the upstream hurdles loop), and ``apply_bystander_guard`` is tested with a
faked ``pipeline_v2`` module plus a monkeypatched paddlex version.
"""
import importlib.util
import sys
import types
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
spec = importlib.util.spec_from_file_location(
    "layout_parsing_patch", ROOT / "src/mp4_analysis/thin/_layout_parsing_patch.py")
patch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(patch)


def standardized_data(guarded, writes):
    """Mimics the upstream hurdles blanking loop shape."""
    for overall_ocr_idx, _box_id in ((0, 3), (0, 7)):
        for ocr_idx in (0, 1):
            guarded[ocr_idx] = writes.get(ocr_idx, "")


def test_bystander_blank_is_vetoed():
    guarded = patch._GuardedRecTexts(["spanning line", "bystander line"])
    standardized_data(guarded, {0: "", 1: ""})
    assert list(guarded) == ["", "bystander line"]
    # two hurdle crops (boxes 3 and 7) each tried to blank the bystander
    assert [b["index"] for b in guarded.blocked] == [1, 1]
    assert all(b["preserved"] == "bystander line" for b in guarded.blocked)


def test_spanning_line_blank_then_replaced():
    def standardized_data(guarded):  # nested: co_name is still "standardized_data"
        overall_ocr_idx = 0
        for ocr_idx in (0, 1):
            guarded[ocr_idx] = ""            # hurdle blanking loop
        guarded[overall_ocr_idx] = "piece1"  # replacement site

    guarded = patch._GuardedRecTexts(["spanning line", "bystander line"])
    standardized_data(guarded)
    assert list(guarded) == ["piece1", "bystander line"]
    assert [b["index"] for b in guarded.blocked] == [1]


def standardized_data_replacement(guarded):  # noqa: F811 - intentional redefinition shape
    overall_ocr_idx = 0
    ocr_idx = 1  # stale inner-loop variable, as in upstream
    guarded[overall_ocr_idx] = "--"  # replacement site writes here
    guarded[overall_ocr_idx] = ""   # even an empty crop text must pass


def test_replacement_site_never_vetoed():
    guarded = patch._GuardedRecTexts(["spanning line", "bystander line"])
    standardized_data_replacement(guarded)
    assert list(guarded) == ["", "bystander line"]
    assert guarded.blocked == []


def other_function(guarded):
    ocr_idx = 1
    overall_ocr_idx = 0
    guarded[ocr_idx] = ""


def test_other_callers_never_vetoed():
    guarded = patch._GuardedRecTexts(["a", "b"])
    other_function(guarded)
    assert list(guarded) == ["a", ""]
    assert guarded.blocked == []


def test_append_recorded_and_applied():
    guarded = patch._GuardedRecTexts(["a"])
    guarded.append("")
    assert list(guarded) == ["a", ""]
    assert guarded.events[-1]["append"] is True


def test_numpy_index_coerced_and_report_json_safe():
    np = pytest.importorskip("numpy")
    import json

    def standardized_data(guarded):
        for overall_ocr_idx in (np.int64(0),):
            for ocr_idx in (np.int64(0), np.int64(1)):
                guarded[ocr_idx] = ""

    guarded = patch._GuardedRecTexts(["spanning", "bystander"])
    standardized_data(guarded)
    assert list(guarded) == ["", "bystander"]
    report = {"events": guarded.events, "blocked": guarded.blocked}
    text = json.dumps(report, ensure_ascii=False)  # must not raise
    assert json.loads(text)["blocked"][0]["preserved"] == "bystander"


def _install_fake_paddlex(monkeypatch, version):
    pkg = types.ModuleType("paddlex.inference.pipelines.layout_parsing")
    pv2 = types.ModuleType("paddlex.inference.pipelines.layout_parsing.pipeline_v2")

    class FakePipeline:
        def standardized_data(self, overall_ocr_res):
            for overall_ocr_idx in (0,):
                for ocr_idx in (0, 1):
                    overall_ocr_res["rec_texts"][ocr_idx] = ""

    pv2._LayoutParsingPipelineV2 = FakePipeline
    pkg.pipeline_v2 = pv2
    monkeypatch.setitem(sys.modules, "paddlex.inference.pipelines.layout_parsing", pkg)
    monkeypatch.setitem(sys.modules,
                        "paddlex.inference.pipelines.layout_parsing.pipeline_v2", pv2)
    monkeypatch.setattr(patch.importlib.metadata, "version", lambda name: version)
    monkeypatch.setattr(patch, "_applied", False)
    return FakePipeline


def test_apply_guards_bystander_end_to_end(monkeypatch):
    fake_cls = _install_fake_paddlex(monkeypatch, "3.7.2")
    assert patch.apply_bystander_guard() is True
    res = {"rec_texts": ["spanning", "bystander"]}
    fake_cls().standardized_data(res)
    assert res["rec_texts"] == ["", "bystander"]  # plain list again
    report = patch.get_last_guard_report()
    assert report["n_blocked"] == 1
    assert report["blocked"][0]["preserved"] == "bystander"


def test_apply_is_idempotent(monkeypatch):
    fake_cls = _install_fake_paddlex(monkeypatch, "3.7.2")
    assert patch.apply_bystander_guard() is True
    first = fake_cls.standardized_data
    assert patch.apply_bystander_guard() is True
    assert fake_cls.standardized_data is first  # not wrapped twice


def test_apply_skipped_on_version_mismatch(monkeypatch):
    fake_cls = _install_fake_paddlex(monkeypatch, "3.7.0")
    assert patch.apply_bystander_guard() is False
    assert not getattr(fake_cls.standardized_data, "_bystander_guard_wrapped", False)
    res = {"rec_texts": ["spanning", "bystander"]}
    fake_cls().standardized_data(res)
    assert res["rec_texts"] == ["", ""]  # upstream behavior untouched
