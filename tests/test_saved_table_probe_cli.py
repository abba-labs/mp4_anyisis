"""Selected repair commands return a failing exit status on export rejection."""
import sys
import pytest
from test_saved_table_probe import baseline, probe


def test_cli_selected_export_failure_exits_nonzero(baseline, tmp_path, monkeypatch):
    root, parser = baseline
    def stop(*a, **k): raise ValueError('table text loss')
    monkeypatch.setattr(probe, 'export_saved_word', stop)
    monkeypatch.setattr(sys, 'argv', ['probe', str(root), '-o', str(tmp_path/'out'), '--job', 'job_007'])
    with pytest.raises(SystemExit) as caught:
        probe.main()
    assert caught.value.code == 1
    assert (tmp_path/'out/summary.json').exists()
