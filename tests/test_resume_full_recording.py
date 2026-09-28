"""Fail closed before resuming; no OCR or acceptance claims from these tests."""
import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location('resume_full_recording', Path(__file__).parents[1]/'scripts/resume_full_recording.py')
resume = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resume)


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding='utf-8')


@pytest.fixture
def saved(tmp_path):
    image = tmp_path/'frames/a.png'
    image.parent.mkdir()
    image.write_bytes(b'unchanged encoded image fixture')
    target = tmp_path/'native/a'
    target.mkdir(parents=True)
    result = target/'a.md'
    result.write_text('0x0000_0000', encoding='utf-8')
    evidence = {'completed_cache_job_ids': ['a'], 'pending_job_ids_in_plan_order': ['b'],
                'parser_identity': {'fingerprint': 'fixed'},
                'source': {'sha256': 'video-hash', 'options': {'start': 0.0}}}
    signature = {'source_sha256': 'video-hash', 'options': {'start': 0.0}, 'schema': 1}
    write(tmp_path/'video.json', {'signature': signature, 'frames': [{'image': 'a.png', 'file_sha256': resume.file_hash(image)}]})
    write(tmp_path/'reconstruction.json', {'jobs': [{'id': 'a', 'input_image': 'frames/a.png'}, {'id': 'b'}], 'derived_files': {}})
    write(tmp_path/'report.json', {'items': [{'id': 'a'}]})
    write(target/'adapter.json', {'signature': {'input_sha256': resume.file_hash(image), 'parser': 'fixed', 'word': True},
                                 'errors': [], 'files': {'a.md': resume.file_hash(result)}})
    return tmp_path, evidence


def test_read_only_validation_preserves_cache(saved):
    root, evidence = saved
    before = {str(p): p.read_bytes() for p in root.rglob('*') if p.is_file()}
    plan, hashes = resume.validate_saved(root, evidence, 'fixed')
    assert len(plan['jobs']) == 2 and len(hashes) == 2
    assert before == {str(p): p.read_bytes() for p in root.rglob('*') if p.is_file()}


@pytest.mark.parametrize('mutation,match', [
    ('fingerprint', 'fingerprint'), ('frame', 'frame hash'), ('export', 'export hash'),
    ('order', 'job order'), ('errors', 'invalid successful cache'), ('word', 'invalid successful cache'),
    ('empty', 'invalid successful cache'), ('config', 'video signature')])
def test_corruption_stops_before_parse(saved, mutation, match):
    root, evidence = saved
    fingerprint = 'changed' if mutation == 'fingerprint' else 'fixed'
    if mutation == 'frame': (root/'frames/a.png').write_bytes(b'corrupt')
    if mutation == 'export': (root/'native/a/a.md').write_text('changed')
    if mutation == 'order':
        plan = resume.load(root/'reconstruction.json'); plan['jobs'].reverse(); write(root/'reconstruction.json', plan)
    if mutation in {'errors', 'word', 'empty'}:
        path = root/'native/a/adapter.json'; adapter = resume.load(path)
        if mutation == 'errors': adapter['errors'] = [{'stage': 'export'}]
        if mutation == 'word': adapter['signature']['word'] = False
        if mutation == 'empty': adapter['files'] = {}
        write(path, adapter)
    if mutation == 'config': evidence['source']['options']['start'] = 49.0
    with pytest.raises(ValueError, match=match): resume.validate_saved(root, evidence, fingerprint)
    assert (root/'native/a/adapter.json').exists()


@pytest.mark.parametrize('relative', ['../escape', '/tmp/outside', '.'])
def test_artifact_paths_cannot_escape(tmp_path, relative):
    with pytest.raises(ValueError, match='unsafe'): resume.checked_path(tmp_path, relative)
