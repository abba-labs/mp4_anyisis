import importlib.util
from pathlib import Path
import pytest
spec = importlib.util.spec_from_file_location('ocr_audit', Path(__file__).parents[1]/'scripts/audit_post_layout_ocr.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def payload(text,score):
    return {'overall_ocr_res':{'rec_texts':[text],'rec_scores':[score],'rec_boxes':[[197,146,1082,169]]}}


def test_real_blank_score_symptom_is_not_accepted_as_recognizer_failure():
    findings = audit.inspect_payload(payload('',0.9918525815010071))
    assert len(findings) == 1
    assert findings[0]['stage'] == 'post_layout'
    assert findings[0]['recognizer_failure_proven'] is False
    assert findings[0]['missing_source_content_proven'] is False


@pytest.mark.parametrize('text,score',[('',0),('vcen',.99),('vc_en',.99)])
def test_audit_does_not_repair_or_invent_failures(text,score):
    assert audit.inspect_payload(payload(text,score)) == []


def test_rejects_unaligned_arrays():
    p = payload('',.9); p['overall_ocr_res']['rec_boxes'] = []
    with pytest.raises(ValueError,match='unaligned'): audit.inspect_payload(p)


def test_supports_native_res_wrapper():
    assert len(audit.inspect_payload({'res':payload('',.9)})) == 1
