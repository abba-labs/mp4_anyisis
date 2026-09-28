"""The candidate evaluator must not pass on shape or text presence alone."""
from copy import deepcopy
import pytest
from scripts.probe_docling_tables import evaluate_table


def sample():
    data = {'num_rows': 2, 'num_cols': 2, 'table_cells': [
        {'start_row_offset_idx': 0, 'end_row_offset_idx': 1,
         'start_col_offset_idx': 0, 'end_col_offset_idx': 1, 'text': '0x0000_0000'},
        {'start_row_offset_idx': 1, 'end_row_offset_idx': 2,
         'start_col_offset_idx': 1, 'end_col_offset_idx': 2, 'text': '0'}]}
    fixture = {'required_columns': 2, 'cells': {'A1': '0x0000_0000', 'B2': '0'}}
    return data, fixture


def test_source_slots_pass_but_never_claim_full_table_verified():
    data, fixture = sample()
    result = evaluate_table(data, fixture)
    assert result['acceptance_passed']
    assert not result['complete_table_verified']


def test_empty_native_table_fails():
    _, fixture = sample()
    assert not evaluate_table({}, fixture)['acceptance_passed']


def test_right_words_in_wrong_positions_fail():
    data, fixture = sample()
    data['table_cells'][0]['text'], data['table_cells'][1]['text'] = '0', '0x0000_0000'
    assert evaluate_table(data, fixture)['matched_anchors'] == 0


def test_correct_anchors_with_wrong_width_fail():
    data, fixture = sample()
    data['num_cols'] = 3
    result = evaluate_table(data, fixture)
    assert result['matched_anchors'] == 2
    assert not result['acceptance_passed']


@pytest.mark.parametrize('value', [0, -1, 3, None, True])
def test_invalid_native_span_fails(value):
    data, fixture = sample()
    data['table_cells'][0]['end_row_offset_idx'] = value
    assert not evaluate_table(data, fixture)['acceptance_passed']


def test_multiple_owners_of_same_slot_fail():
    data, fixture = sample()
    data['table_cells'].append(deepcopy(data['table_cells'][0]))
    assert not evaluate_table(data, fixture)['acceptance_passed']


def test_missing_slot_is_not_filled_from_another_cell():
    data, fixture = sample()
    data['table_cells'].pop()
    assert not evaluate_table(data, fixture)['acceptance_passed']


def test_whitespace_is_ignored_but_address_punctuation_is_not():
    data, fixture = sample()
    data['table_cells'][0]['text'] = ' 0x0000_\n0000 '
    assert evaluate_table(data, fixture)['acceptance_passed']
    data['table_cells'][0]['text'] = '0x00000000'
    assert not evaluate_table(data, fixture)['acceptance_passed']


def test_evaluation_never_mutates_native_payload():
    data, fixture = sample()
    original = deepcopy(data)
    evaluate_table(data, fixture)
    assert data == original
