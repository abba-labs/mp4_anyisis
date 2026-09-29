"""Interpreter-policy tests, using simulated metadata, NOT cross-version OCR."""
import builtins
import importlib.util
import json
import re
import types
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
spec = importlib.util.spec_from_file_location('python_policy_probe', ROOT/'scripts/probe_saved_text_recognition.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def metadata(monkeypatch, version, packages=None):
    monkeypatch.setattr(probe, 'sys', types.SimpleNamespace(
        version=version+' (simulated)', version_info=tuple(map(int, version.split('.')))))
    values = probe.REQUIRED_VERSIONS if packages is None else packages
    def installed(name):
        if name not in values:
            raise probe.importlib.metadata.PackageNotFoundError(name)
        return values[name]
    monkeypatch.setattr(probe.importlib.metadata, 'version', installed)


@pytest.mark.parametrize('version,allowed,same', [
    ('3.9.25', False, False), ('3.10.21', True, False),
    ('3.11.9', True, False), ('3.11.16', True, True),
    ('3.12.3', True, False), ('3.12.14', True, False),
    ('3.13.15', False, False), ('3.14.0', False, False),
])
def test_python_acceptance_is_distinct_from_baseline_identity(monkeypatch, version, allowed, same):
    metadata(monkeypatch, version)
    status = probe.runtime_status()
    assert status['ready'] is allowed
    assert status['python_supported'] is allowed
    assert status['baseline_python_match'] is same
    assert status['python'] == version
    assert status['baseline_python'] == '3.11.16'
    assert bool(status['warnings']) is (not same)
    assert status['model_cache_checked'] is False
    assert status['dependencies_import_checked'] is False


def test_policy_matches_project_metadata():
    text = (ROOT/'pyproject.toml').read_text(encoding='utf-8')
    declared = re.search(r'^requires-python\s*=\s*"([^"]+)"', text, re.M).group(1)
    assert probe.PYTHON_REQUIREMENT == declared == '>=3.10,<3.13'


@pytest.mark.parametrize('packages', [{}, {**probe.REQUIRED_VERSIONS, 'paddlex': '3.7.1'}])
def test_relaxing_python_does_not_relax_model_dependencies(monkeypatch, packages):
    metadata(monkeypatch, '3.12.3', packages)
    assert probe.runtime_status()['ready'] is False


def test_metadata_check_never_imports_paddle(monkeypatch):
    metadata(monkeypatch, '3.12.3')
    real_import = builtins.__import__
    def guarded(name, *args, **kwargs):
        if name.split('.')[0] in {'paddle', 'paddleocr', 'paddlex'}:
            raise AssertionError('preflight must not load inference libraries')
        return real_import(name, *args, **kwargs)
    monkeypatch.setattr(builtins, '__import__', guarded)
    assert probe.runtime_status()['ready'] is True


def test_cross_python_runtime_is_recorded_in_run_summary(tmp_path, monkeypatch):
    """Exercise the wrapper with one fake result; no real model or image is used."""
    source = tmp_path/'source'; native = source/'native/frame_00002950'
    native.mkdir(parents=True)
    image = source/'frame_00002950.png'; image.write_bytes(b'unit-test-only')
    params = {'limit_side_len': 736, 'limit_type': 'min', 'thresh': .3,
              'max_side_limit': 4000, 'box_thresh': .6, 'unclip_ratio': 1.5}
    (native/'result.json').write_text(json.dumps({'overall_ocr_res': {
        'text_det_params': params, 'text_rec_score_thresh': 0.0}}))
    (native/'adapter.json').write_text(json.dumps({
        'signature': {'input_sha256': probe.file_hash(image)}, 'errors': [],
        'files': {'result.json': probe.file_hash(native/'result.json')}, 'native_json': 'result.json'}))
    (source/'report.json').write_text(json.dumps({'parser_attempts': 57, 'pending_parser_inputs': 0,
        'items': [{'id': 'frame_00002950', 'kind': 'source_frame', 'input_image': image.name,
                   'directory': 'native/frame_00002950', 'frame': {'frame_index': 2950}}]}))
    evidence = tmp_path/'evidence.json'; evidence.write_text(json.dumps({'limit_clauses': {'records': []}}))
    metadata(monkeypatch, '3.12.3')
    class FakeResult:
        def save_to_json(self, path):
            Path(path).write_text(json.dumps({'text_det_params': params,
                'text_rec_score_thresh': 0.0, 'rec_texts': ['vc_en；']}))
    class FakeEngine:
        def __init__(self, **options):
            assert options['text_recognition_model_name'] == 'PP-OCRv5_mobile_rec'
        def predict(self, image):
            yield FakeResult()
    import sys
    monkeypatch.setitem(sys.modules, 'paddleocr', types.SimpleNamespace(PaddleOCR=FakeEngine))
    pre = probe.preflight(source, (2950,), ('mobile',))
    assert pre['status'] == 'RUNTIME_READY' and pre['executed'] == 0
    assert pre['runtime']['baseline_python_match'] is False
    result = probe.run(source, tmp_path/'output', evidence, (2950,), recognizers=('mobile',))
    saved = json.loads((tmp_path/'output/summary.json').read_text())
    assert saved['runtime'] == pre['runtime'] == result['runtime']
    assert saved['native_files_unchanged'] is True
    assert saved['content_acceptance'] == 'NOT_ACCEPTED'
    assert saved['pending'] == 0
