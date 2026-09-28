"""Opt-in upstream table mode, with explicit cache isolation. No local table solver."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
from PIL import Image
from mp4_analysis.thin.parser import NativeParser


@pytest.fixture
def upstream(monkeypatch, tmp_path):
    calls = []
    class Result:
        def save_to_json(self, save_path):
            data = {'parsing_res_list': [{'block_label': 'text', 'block_content': 'unchanged'}]}
            Path(save_path, 'source_res.json').write_text(json.dumps(data))
        def save_to_markdown(self, save_path):
            Path(save_path, 'source.md').write_text('0x2800 | 0x2808 | 0 | 0')
        def save_to_html(self, save_path):
            pass
        def save_to_xlsx(self, save_path):
            pass
    class Engine:
        def __init__(self, **options):
            calls.append(options)
        def predict(self, path, **options):
            calls.append((path, options))
            yield Result()
    monkeypatch.setitem(sys.modules, 'paddleocr', SimpleNamespace(PPStructureV3=Engine))
    image = tmp_path/'source.png'
    Image.new('RGB', (80, 60), 'white').save(image)
    return image, calls


def test_native_table_mode_is_opt_in_and_part_of_cache_identity():
    default, cells = NativeParser(), NativeParser(table_mode='cells')
    assert default.predict_options == {}
    assert cells.predict_options == {'use_wired_table_cells_trans_to_html': True,
                                     'use_wireless_table_cells_trans_to_html': True}
    assert default.fingerprint != cells.fingerprint
    assert default.options == cells.options  # Same engine, different upstream strategy.


def test_native_table_mode_forwarded_without_rewriting(upstream, tmp_path):
    image, calls = upstream
    parser = NativeParser(table_mode='cells')
    meta = parser.parse(image, tmp_path/'native')
    assert calls[-1][1] == parser.predict_options
    assert meta['predict_options'] == parser.predict_options
    assert (tmp_path/'native/source.md').read_text() == '0x2800 | 0x2808 | 0 | 0'


def test_table_mode_switch_cannot_reuse_old_structure(upstream, tmp_path):
    image, calls = upstream
    NativeParser().parse(image, tmp_path/'native')
    count = len(calls)
    result = NativeParser(table_mode='cells').parse(image, tmp_path/'native')
    assert not result['cache_hit']
    assert len(calls) > count


@pytest.mark.parametrize('mode', ['guessed', '', None])
def test_invalid_native_table_mode_rejected(mode):
    with pytest.raises(ValueError, match='table_mode'):
        NativeParser(table_mode=mode)
