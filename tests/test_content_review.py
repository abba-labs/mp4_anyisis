"""Acceptance bookkeeping does not promote execution/file counts to accuracy."""
import importlib.util
import json
from pathlib import Path
import pytest

spec = importlib.util.spec_from_file_location('content_review', Path(__file__).parents[1]/'scripts/build_content_review.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def unit(**updates):
    result = {'id': '1', 'title': 'Test', 'source_frames': [0], 'reason': 'Unreviewed',
              'gates': {k: 'NOT_REVIEWED' for k in m.GATES}, 'acceptance_evidence': []}
    result.update(updates)
    return result


def fixture(tmp_path):
    source = tmp_path/'source'; (source/'frames').mkdir(parents=True)
    image = source/'frames/f.png'; image.write_bytes(b'original saved evidence')
    frame = {'frame_index': 0, 'start_time': 0.0, 'image': 'f.png', 'file_sha256': m.file_hash(image)}
    (source/'video.json').write_text(json.dumps({'source_sha256': 'video', 'frames': [frame]}))
    (source/'report.json').write_text(json.dumps({'parser_attempts': 57, 'pending_parser_inputs': 0, 'items': []}))
    ledger = tmp_path/'ledger.json'
    ledger.write_text(json.dumps({'scope': 'fixture', 'source_sha256': 'video', 'units': [unit()]}))
    return source, ledger


def test_completed_execution_never_automatically_accepts(tmp_path):
    source, ledger = fixture(tmp_path)
    result = m.build(source, ledger, tmp_path/'review')
    assert result['execution']['processed'] == 57
    assert result['accepted'] == 0 and result['not_reviewed'] == 1
    assert result['project_completion_percent'] is None
    assert not result['full_video_coverage_verified']


def test_failure_is_not_counted_as_unreviewed():
    u = unit(); u['gates']['text'] = 'FAIL'
    assert m.unit_state(u) == 'FAIL'


@pytest.mark.parametrize('change', ['state', 'gate', 'empty', 'fake_pass'])
def test_invalid_or_unsubstantiated_acceptance_rejected(change):
    u = unit()
    if change == 'state': u['gates']['text'] = 'GENERATED'
    elif change == 'gate': u['gates'].pop('office')
    elif change == 'empty': u['gates'] = {k: 'NOT_APPLICABLE' for k in m.GATES}
    else: u['gates'] = {k: 'PASS' for k in m.GATES}
    with pytest.raises(ValueError): m.unit_state(u)


@pytest.mark.parametrize('change', ['wrong_video', 'corrupt_frame', 'duplicate_id', 'no_anchor'])
def test_invalid_source_or_inventory_rejected(tmp_path, change):
    source, ledger = fixture(tmp_path)
    d = json.loads(ledger.read_text())
    if change == 'wrong_video': d['source_sha256'] = 'other'
    elif change == 'corrupt_frame': (source/'frames/f.png').write_bytes(b'changed')
    elif change == 'duplicate_id': d['units'].append(d['units'][0])
    else: d['units'][0]['source_frames'] = []
    ledger.write_text(json.dumps(d))
    with pytest.raises(ValueError): m.build(source, ledger, tmp_path/'review')
    assert not (tmp_path/'review').exists()


def test_output_never_overwrites_evidence(tmp_path):
    source, ledger = fixture(tmp_path)
    with pytest.raises(ValueError): m.build(source, ledger, source/'review')


def test_seed_inventory_has_fixed_source_based_units():
    path = Path(__file__).parent/'fixtures/sarc_review_units_v1.json'
    d = json.loads(path.read_text(encoding='utf-8'))
    assert len(d['units']) == 11
    assert sum(m.unit_state(u) == 'FAIL' for u in d['units']) == 4
    assert not any(m.unit_state(u) == 'PASS' for u in d['units'])
    assert d['catalog_evidence_frames'] == [271, 301]
