"""No-model tests of explicit saved-job retries and truthful interruption records."""
import importlib.util
import json
from pathlib import Path
import pytest

spec = importlib.util.spec_from_file_location('saved_table_probe', Path(__file__).parents[1]/'scripts/probe_saved_table_cells.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

@pytest.fixture
def baseline(tmp_path, monkeypatch):
    root = tmp_path/'baseline'
    root.mkdir()
    image = root/'image.png'
    image.write_bytes(b'not decoded by mocked engine')
    items = []
    for i in range(57):
        job = f'job_{i:03d}'
        directory = root/'native'/job
        directory.mkdir(parents=True)
        (directory/'page.md').write_text('unchanged')
        cache = {'signature': {'parser': probe.BASE_FINGERPRINT, 'input_sha256': probe.file_hash(image)},
                 'files': {'page.md': probe.file_hash(directory/'page.md')}, 'errors': []}
        (directory/'adapter.json').write_text(json.dumps(cache))
        items.append({'id': job, 'directory': f'native/{job}', 'input_image': 'image.png'})
    (root/'report.json').write_text(json.dumps({'parser_attempts': 57, 'pending_parser_inputs': 0, 'items': items}))
    class Parser:
        calls = []
        fingerprint = probe.BASE_FINGERPRINT
        def __init__(self, **kwargs): self.engine = None
        def parse(self, image, target, **kwargs):
            self.calls.append(str(target))
            target.mkdir(parents=True)
            (target/'page.md').write_text('candidate')
            self.engine = object()
            return {'errors': []}
    monkeypatch.setattr(probe, 'NativeParser', Parser)
    monkeypatch.setattr(probe, 'export_saved_word', lambda *a, **k: {'status': 'REVIEW_REQUIRED'})
    return root, Parser


def test_one_job_does_not_retry_the_whole_plan(baseline, tmp_path):
    root, parser = baseline
    result = probe.run_saved_probe(root, tmp_path/'out', job_ids=['job_007'])
    assert len(parser.calls) == 1 and result['planned'] == 1 and result['pending'] == 0
    assert result['native_outputs_modified'] is False
    assert result['cases'][0]['completed'] is True


@pytest.mark.parametrize('jobs', [[], ['missing'], ['job_000', 'job_000']])
def test_invalid_selection_does_not_write_or_parse(baseline, tmp_path, jobs):
    root, parser = baseline
    with pytest.raises(ValueError, match='select unique'):
        probe.run_saved_probe(root, tmp_path/'out', job_ids=jobs)
    assert not parser.calls and not (tmp_path/'out').exists()


def test_corrupt_cache_fails_before_inference(baseline, tmp_path):
    root, parser = baseline
    (root/'native/job_000/page.md').write_text('corrupt')
    with pytest.raises(ValueError, match='resource changed'):
        probe.run_saved_probe(root, tmp_path/'out', job_ids=['job_007'])
    assert not parser.calls and not (tmp_path/'out').exists()


def test_interrupted_call_remains_pending(baseline, tmp_path, monkeypatch):
    root, parser = baseline
    def stop(*a, **k): raise KeyboardInterrupt()
    monkeypatch.setattr(parser, 'parse', stop)
    out = tmp_path/'out'
    with pytest.raises(KeyboardInterrupt):
        probe.run_saved_probe(root, out, job_ids=['job_007'])
    result = json.loads((out/'summary.json').read_text())
    assert result['pending'] == 1 and result['cases'][0]['completed'] is False
    assert 'interruption' in result['cases'][0] and result['native_outputs_modified'] is False


def test_export_failure_is_not_hidden(baseline, tmp_path, monkeypatch):
    root, parser = baseline
    def stop(*a, **k): raise ValueError('table text loss')
    monkeypatch.setattr(probe, 'export_saved_word', stop)
    result = probe.run_saved_probe(root, tmp_path/'out', job_ids=['job_007'])
    assert result['word_failures'] == 1 and result['pending'] == 0
    assert 'word_error' in result['cases'][0] and result['native_outputs_modified'] is False
