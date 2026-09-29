"""Read-only OCR experiment guards, not OCR accuracy tests."""
import importlib.util
import json
from pathlib import Path
import pytest

spec = importlib.util.spec_from_file_location('text_probe', Path(__file__).parents[1]/'scripts/probe_saved_text_recognition.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def test_compact_keeps_identifier_and_punctuation():
    assert probe.compact('vc_en \n；') == 'vc_en；'
    assert probe.compact('vc_en') != probe.compact('vcen')
    assert probe.compact('以上；') != probe.compact('以上：')


def test_disjoint_before_any_dependency_import(tmp_path):
    with pytest.raises(ValueError, match='disjoint'):
        probe.run(tmp_path, tmp_path/'derived', tmp_path/'missing.json')


@pytest.mark.parametrize('count,pending', [(31,26), (57,1), (0,0)])
def test_rejects_incomplete_baseline(tmp_path,count,pending):
    (tmp_path/'report.json').write_text(json.dumps({'parser_attempts':count,'pending_parser_inputs':pending}))
    with pytest.raises(ValueError, match='completed'):
        probe.validate_source(tmp_path,[2920])


@pytest.mark.parametrize('frames', [[], [2920,2920]])
def test_rejects_empty_and_repeated_frame_selection(tmp_path,frames):
    (tmp_path/'report.json').write_text(json.dumps({'parser_attempts':57,'pending_parser_inputs':0,'items':[]}))
    with pytest.raises(ValueError, match='unique'):
        probe.validate_source(tmp_path,frames)


def test_rejects_unknown_source_frame(tmp_path):
    (tmp_path/'report.json').write_text(json.dumps({'parser_attempts':57,'pending_parser_inputs':0,'items':[]}))
    with pytest.raises(ValueError, match='existing source-frame'):
        probe.validate_source(tmp_path,[12345])
