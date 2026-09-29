"""Runtime/planning tests with a fake recognizer. No OCR accuracy claims."""
import importlib.util
import json
import sys
import types
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location('text_preflight_probe', Path(__file__).parents[1]/'scripts/probe_saved_text_recognition.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)
PARAMS = {'limit_side_len': 736, 'limit_type': 'min', 'thresh': .3,
          'max_side_limit': 4000, 'box_thresh': .6, 'unclip_ratio': 1.5}


@pytest.fixture
def data(tmp_path):
    source = tmp_path/'source'; source.mkdir()
    items = []
    for index in (2920, 2950):
        key = f'frame_{index:08d}'
        native = source/'native'/key; native.mkdir(parents=True)
        image = source/f'{key}.png'; image.write_bytes(b'fake image; no decoding in unit test')
        payload = native/'result.json'
        payload.write_text(json.dumps({'overall_ocr_res': {'text_det_params': PARAMS,
                                                         'text_rec_score_thresh': 0.0}}))
        (native/'adapter.json').write_text(json.dumps({
            'signature': {'input_sha256': probe.file_hash(image)}, 'errors': [],
            'files': {'result.json': probe.file_hash(payload)}, 'native_json': 'result.json'}))
        items.append({'id': key, 'kind': 'source_frame', 'input_image': image.name,
                      'directory': f'native/{key}', 'frame': {'frame_index': index}})
    (source/'report.json').write_text(json.dumps({'parser_attempts': 57,
                                                'pending_parser_inputs': 0, 'items': items}))
    evidence = tmp_path/'evidence.json'
    evidence.write_text(json.dumps({'limit_clauses': {'records': []}}))
    return source, evidence


def ready(monkeypatch):
    monkeypatch.setattr(probe, 'runtime_status', lambda: {
        'python': '3.11.16', 'versions': probe.REQUIRED_VERSIONS, 'ready': True,
        'model_cache_checked': False})


@pytest.mark.parametrize('models', [(), ('mobile', 'mobile'), ('other',)])
def test_reject_invalid_recognizers(models):
    with pytest.raises(ValueError, match='unique'):
        probe.validate_recognizers(models)


def test_preflight_is_two_unexecuted_inputs_without_import(data, monkeypatch):
    source, _ = data
    monkeypatch.setattr(probe, 'runtime_status', lambda: {'ready': False})
    result = probe.preflight(source, recognizers=('mobile',))
    assert result['planned'] == result['pending'] == 2
    assert result['executed'] == 0 and result['inference_performed'] is False
    assert result['status'] == 'BLOCKED_RUNTIME'


def test_runtime_failure_creates_no_output(data, tmp_path, monkeypatch):
    source, evidence = data
    monkeypatch.setattr(probe, 'runtime_status', lambda: {'ready': False})
    target = tmp_path/'result'
    with pytest.raises(RuntimeError, match='runtime unavailable'):
        probe.run(source, target, evidence, recognizers=('mobile',))
    assert not target.exists()


def test_different_source_settings_rejected(data):
    source, _ = data
    native = source/'native/frame_00002950'
    p = native/'result.json'; payload = json.loads(p.read_text())
    payload['overall_ocr_res']['text_det_params']['limit_side_len'] = 960
    p.write_text(json.dumps(payload))
    a = native/'adapter.json'; cache = json.loads(a.read_text())
    cache['files'][p.name] = probe.file_hash(p); a.write_text(json.dumps(cache))
    with pytest.raises(ValueError, match='different saved'):
        probe.preflight(source, recognizers=('mobile',))


@pytest.mark.parametrize('drift', [False, True])
def test_only_selected_model_and_returned_parameter_guard(data, tmp_path, monkeypatch, drift):
    source, evidence = data
    ready(monkeypatch)
    loaded = []
    class FakeResult:
        def save_to_json(self, path):
            params = dict(PARAMS)
            if drift:
                params['max_side_limit'] = 3000
            Path(path).write_text(json.dumps({'text_det_params': params,
                 'text_rec_score_thresh': 0.0, 'rec_texts': ['vc_en；']}))
    class FakeEngine:
        def __init__(self, **options):
            loaded.append(options['text_recognition_model_name'])
        def predict(self, image):
            yield FakeResult()
    monkeypatch.setitem(sys.modules, 'paddleocr', types.SimpleNamespace(PaddleOCR=FakeEngine))
    target = tmp_path/'result'
    if drift:
        with pytest.raises(ValueError, match='parameters differ'):
            probe.run(source, target, evidence, recognizers=('mobile',))
        result = json.loads((target/'summary.json').read_text())
        assert result['cases'] == [] and result['pending'] == 2 and result['error']
        assert (target/'frame_00002920_mobile/raw_ocr.json').is_file()
    else:
        result = probe.run(source, target, evidence, recognizers=('mobile',))
        assert result['planned'] == len(result['cases']) == 2 and result['pending'] == 0
        assert result['native_files_unchanged'] is True
    assert loaded == ['PP-OCRv5_mobile_rec']
