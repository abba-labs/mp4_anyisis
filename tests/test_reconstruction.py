"""Retained parser/output checks from the retired reconstruction test module.

Video extraction and stitching were removed in db5a956. Their tests remain in
Git history; do not restore a video shim merely to collect those old tests.
These two still-applicable assertions are preserved. Not executed by this change.
"""
import pytest

from mp4_analysis.thin.parser import NativeParser


def test_mobile_uses_upstream_models_and_distinct_cache_key():
    default = NativeParser()
    mobile = NativeParser(ocr_models='mobile')
    assert mobile.options['text_detection_model_name'] == 'PP-OCRv5_mobile_det'
    assert mobile.options['text_recognition_model_name'] == 'PP-OCRv5_mobile_rec'
    assert default.fingerprint != mobile.fingerprint
    assert 'text_detection_model_name' not in default.options
    with pytest.raises(ValueError):
        NativeParser(ocr_models='unknown')


def test_incomplete_parse_has_visible_pending_count(tmp_path):
    from mp4_analysis.thin.output import write_index
    manifest = {'frames': [{'frame_index': i, 'image': f'{i}.png'} for i in range(3)]}
    item = {'frame': manifest['frames'][0], 'directory': 'none'}
    result = write_index(tmp_path, manifest, [item])
    assert result['status'] == 'PARTIAL_FAILURE'
    assert result['pending_parser_inputs'] == 2
