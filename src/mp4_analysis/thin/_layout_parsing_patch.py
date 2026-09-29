"""Version-pinned guard against PP-StructureV3 hurdle-blanking data loss.

Upstream bug (paddlex==3.7.2,
``paddlex/inference/pipelines/layout_parsing/pipeline_v2.py``,
``_LayoutParsingPipelineV2.standardized_data``, section
"Replace the OCR information of the hurdles"):

when one OCR text line spans more than one layout box, the pipeline re-crops
each box/line intersection and re-recognizes it.  Before re-recognition it
blanks ``rec_texts[i] = ""`` for EVERY OCR line whose box overlaps the crop
region with IoU > 0.8 -- including unrelated "bystander" lines that merely
pass through the crop.  Only the spanning line itself is ever restored
(replaced by the first crop's text, or appended pieces).  Bystanders keep
their box and score but lose their text, so the line silently disappears
from the Markdown export.

Observed 2026-09-29 on frame 2950, LIMIT.08 first line
(box [197, 146, 1082, 169], score 0.9919): blanked twice as a bystander by
two spanning lines' hurdle crops (IoU 0.90 / 0.96), never restored.

Fix (minimal, version-pinned): guard ``overall_ocr_res["rec_texts"]`` for the
duration of ``standardized_data`` so the hurdle blanking only applies to the
spanning line itself (``ocr_idx == overall_ocr_idx``); bystander texts are
preserved.  No model change, no frame/keyword/index special-casing, no
hand-filled text, no rewriting of the OCR or layout engines.

The guard is installed by wrapping
``_LayoutParsingPipelineV2.standardized_data`` in-process -- the same
pattern paddleocr itself uses in ``_patch_layout_parsing.py``.  It activates
only when the installed paddlex version is exactly the pinned one;
otherwise it logs a warning and leaves the pipeline untouched.
"""

from __future__ import annotations

import functools
import importlib.metadata
import inspect
import logging

logger = logging.getLogger(__name__)

_PINNED_PADDLEX = "3.7.2"

_applied = False
_LAST_REPORT = None


class _GuardedRecTexts(list):
    """A list that records indexed writes and vetoes hurdle-blanking of
    bystander lines.

    The veto fires only when ALL of these hold, which uniquely identifies
    the upstream blanking statement
    ``overall_ocr_res["rec_texts"][ocr_idx] = ""`` in the hurdles loop:

    * the written value is ``""``;
    * the caller is ``standardized_data``;
    * the write targets the loop variable (``index == ocr_idx``) -- this
      distinguishes the blanking site from the replacement site, which
      writes to ``overall_ocr_idx``;
    * ``ocr_idx != overall_ocr_idx`` -- i.e. the blanked line is a
      bystander, not the spanning line the hurdle logic is splitting.
    """

    def __init__(self, iterable=()):
        super().__init__(iterable)
        self.events = []   # every indexed write observed
        self.blocked = []  # bystander blanks that were vetoed (text preserved)

    def __setitem__(self, index, value):
        # Upstream indexes with numpy integers (from block_to_ocr_map); coerce
        # to plain int so the diagnostic report stays JSON-serializable.
        index = int(index)
        frame = inspect.currentframe().f_back
        try:
            loc = frame.f_locals
            is_bystander_blank = (
                value == ""
                and frame.f_code.co_name == "standardized_data"
                and "overall_ocr_idx" in loc
                and loc.get("ocr_idx") == index
                and loc.get("overall_ocr_idx") != index
            )
        finally:
            del frame  # never keep frames alive
        old = list.__getitem__(self, index)
        self.events.append({
            "index": index,
            "old": old,
            "new": value,
            "vetoed": bool(is_bystander_blank),
        })
        if is_bystander_blank:
            self.blocked.append({"index": index, "preserved": old})
            return
        list.__setitem__(self, index, value)

    def append(self, value):
        self.events.append({"index": len(self), "old": None,
                            "new": value, "vetoed": False, "append": True})
        list.append(self, value)


def _wrap_standardized_data(orig):
    @functools.wraps(orig)
    def wrapper(self, *args, **kwargs):
        global _LAST_REPORT
        target = kwargs.get("overall_ocr_res")
        if target is None:
            for arg in args:
                if isinstance(arg, dict) and "rec_texts" in arg:
                    target = arg
                    break
        if target is None:
            return orig(self, *args, **kwargs)
        guarded = _GuardedRecTexts(target["rec_texts"])
        target["rec_texts"] = guarded
        try:
            return orig(self, *args, **kwargs)
        finally:
            target["rec_texts"] = list(guarded)
            _LAST_REPORT = {
                "n_events": len(guarded.events),
                "n_blocked": len(guarded.blocked),
                "blocked": list(guarded.blocked),
                "events": list(guarded.events),
            }
            if guarded.blocked:
                preview = [str(b["preserved"])[:48] for b in guarded.blocked]
                logger.info(
                    "hurdle-blanking guard preserved %d bystander OCR text(s) "
                    "that upstream would have blanked: %s",
                    len(guarded.blocked), preview)

    return wrapper


def apply_bystander_guard():
    """Install the guard on the pinned paddlex version.  Idempotent.

    Returns True when the guard is (now) active, False otherwise.
    """
    global _applied
    if _applied:
        return True
    try:
        installed = importlib.metadata.version("paddlex")
    except importlib.metadata.PackageNotFoundError:
        installed = None
    if installed != _PINNED_PADDLEX:
        logger.warning(
            "bystander guard skipped: requires paddlex==%s, found %s",
            _PINNED_PADDLEX, installed)
        return False
    try:
        from paddlex.inference.pipelines.layout_parsing import (
            pipeline_v2 as pipeline_v2_mod,
        )
    except ImportError as exc:
        logger.warning("bystander guard skipped: cannot import pipeline_v2: %s",
                       exc)
        return False
    cls = pipeline_v2_mod._LayoutParsingPipelineV2
    if getattr(cls.standardized_data, "_bystander_guard_wrapped", False):
        _applied = True
        return True
    wrapped = _wrap_standardized_data(cls.standardized_data)
    wrapped._bystander_guard_wrapped = True
    cls.standardized_data = wrapped
    _applied = True
    logger.info("bystander guard applied to %s.standardized_data (paddlex %s)",
                cls.__name__, installed)
    return True


def get_last_guard_report():
    """Diagnostics for the most recent guarded ``standardized_data`` call."""
    return _LAST_REPORT
