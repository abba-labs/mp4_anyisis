"""Geometry checks do not modify OCR, use a model, or infer missing cells."""
import copy
import pytest
from scripts.probe_grid_ocr import valid_box, iou, assess_geometry

@pytest.mark.parametrize('box', [None, [], [0, 0, 0, 4], [1, 0, 0, 4], [0, 2, 1, 2],
                                [0, 0, float('nan'), 3], [0, 0, float('inf'), 3], [0, 0, True, 3]])
def test_invalid_box_is_rejected(box):
    assert not valid_box(box)
    assert iou([0, 0, 3, 3], box) == 0


def test_exact_box_and_translation():
    assert iou([0, 0, 2, 2], [0, 0, 2, 2]) == 1
    assert iou([0, 0, 2, 2], [2, 0, 4, 2]) == 0


def test_valid_geometry_is_not_content_acceptance():
    tables = [{'cells': [[{'bbox': [0, 0, 3, 3], 'value': 'wrong'}]]}]
    original = copy.deepcopy(tables)
    result = assess_geometry(tables, {'A1': [0, 0, 3, 3]}, 1)
    assert result['geometry_passed'] and not result['complete_table_verified']
    assert tables == original


def test_nominal_column_count_does_not_allow_zero_width_cells():
    table = [{'cells': [[{'bbox': [0, 0, 1, 1]}, {'bbox': [1, 0, 1, 1]}]]}]
    result = assess_geometry(table, {'A1': [0, 0, 1, 1]}, 2)
    assert result['matrix_width_ok'] and not result['geometry_passed']
    assert result['invalid_cells'] == [{'table': 0, 'row': 1, 'column': 2}]


def test_unrelated_table_does_not_satisfy_source_anchor():
    table = [{'cells': [[{'bbox': [5, 5, 6, 6]}]]}, {'cells': [[{'bbox': [0, 0, 1, 1]}]]}]
    assert not assess_geometry(table, {'A1': [0, 0, 1, 1]}, 1)['geometry_passed']


def test_missing_table_is_not_a_pass():
    assert not assess_geometry([], {'A1': [0, 0, 1, 1]}, 1)['geometry_passed']


def test_merged_cells_are_not_flagged_as_duplicate_data():
    table = [{'cells': [[{'bbox': [0, 0, 2, 1]}, {'bbox': [0, 0, 2, 1]}]]}]
    assert not assess_geometry(table, {'A1': [0, 0, 2, 1]}, 2)['invalid_cells']
