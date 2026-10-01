"""Validate external review data and publish a separate candidate; no model call."""
from __future__ import annotations

import copy
import hashlib
import json
import shutil
import tempfile
import uuid
from pathlib import Path

from .document_bundle import publish_candidate, read_bundle, require_delivery_target
from .document_format import checked_bbox, local_file
from .utils import checked_directory, json_hash, output_lock, require_disjoint, write_json

_OPERATIONS = {'replace_text', 'replace_cell', 'restore_fragment', 'exclude_overlay',
               'flag_structure', 'flag_image'}


def read_response(path):
    path = Path(path)
    if path.stat().st_size > 8_000_000:
        raise ValueError('Review response exceeds 8 MB; use bounded document batches')
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    def no_duplicate_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'Duplicate JSON key: {key}')
            result[key] = value
        return result
    response = json.loads(raw.decode('utf-8'), object_pairs_hook=no_duplicate_keys,
                          parse_constant=lambda x: (_ for _ in ()).throw(ValueError('Non-finite JSON number')))
    if not isinstance(response, dict) or response.get('schema') != 1:
        raise ValueError('Expected review response schema=1')
    if not isinstance(response.get('changes'), list) or len(response['changes']) > 10000:
        raise ValueError('Expected a bounded changes list')
    reviewer = response.get('reviewer', {})
    if not isinstance(reviewer, dict) or reviewer.get('mode') not in {'agent_image_tool', 'callable_vision_service', 'human'}:
        raise ValueError('Record the actual reviewer mode')
    if not isinstance(reviewer.get('name'), str) or not reviewer['name'].strip():
        raise ValueError('Record reviewer name, or explicit unknown if unavailable')
    return response, digest


def response_summary(path):
    response, digest = read_response(path)
    return {'response_sha256': digest, 'base_content_sha256': response.get('base_content_sha256'),
            'change_count': len(response['changes']), 'reviewer': response['reviewer'],
            'operations': [x.get('operation') for x in response['changes']],
            'instructions': 'Review this response; apply only with --accept-changes equal to response_sha256.',
            'applied': False}


def _index(document):
    targets = {}
    for unit in document['units']:
        for block in unit['blocks']:
            if block['id'] in targets:
                raise ValueError('Duplicate block identifier')
            targets[block['id']] = (unit, block, block)
            if block['kind'] == 'table':
                for cell in block['table']['cells']:
                    if cell['id'] in targets:
                        raise ValueError('Duplicate cell identifier')
                    targets[cell['id']] = (unit, block, cell)
    return targets


def _evidence_refs(change, unit, document):
    refs = change.get('evidence_refs')
    if not isinstance(refs, list) or not refs:
        raise ValueError('Every change needs explicit source-image evidence')
    checked = []
    for ref in refs:
        if not isinstance(ref, dict):
            raise ValueError('Invalid evidence reference')
        eid = ref.get('evidence_id')
        evidence = document['evidence'].get(eid)
        if not evidence or evidence['unit_id'] != unit['id']:
            raise ValueError('Change evidence must belong to the target screenshot unit')
        if ref.get('image_sha256') != evidence['sha256']:
            raise ValueError('Evidence image hash mismatch')
        box = checked_bbox(ref.get('bbox'), evidence['size'])
        checked.append({'evidence_id': eid, 'image_sha256': evidence['sha256'], 'bbox': box})
    return checked


def _merge_coverage(previous, reviewed, reported_ids, response_digest):
    """Accumulate claims for unchanged evidence/content; never grant accuracy.

    Coverage is bound to both source pixels and the resulting unit content.
    Modifying a previously covered unit without a new review claim invalidates
    it. Pending entries are regenerated once; all other unresolved issues stay.
    """
    evidence = reviewed['evidence']
    if (not isinstance(reported_ids, list)
            or any(not isinstance(eid, str) or eid not in evidence for eid in reported_ids)):
        raise ValueError('Unknown reviewed evidence ID')
    reported = set(reported_ids)
    old_units = {u['id']: u for u in previous['units']}
    units = {u['id']: u for u in reviewed['units']}
    old_records = copy.deepcopy(previous.get('review_coverage', {}))
    # Legacy bundles only stored a list. Import claims against their sealed
    # source/content identity; do not invent independent acceptance records.
    if not old_records:
        for eid in previous.get('reviewed_evidence_ids_reported', []):
            old_e = previous.get('evidence', {}).get(eid)
            if old_e and old_e['unit_id'] in old_units:
                old_records[eid] = {'image_sha256': old_e['sha256'],
                    'unit_content_sha256': json_hash(old_units[old_e['unit_id']]['blocks']),
                    'origin': 'legacy_reported_claim', 'source_accuracy_verified': False}
    coverage = {}
    history = reviewed.setdefault('review_coverage_history', [])
    for eid, image in evidence.items():
        identity = {'image_sha256': image['sha256'],
                    'unit_content_sha256': json_hash(units[image['unit_id']]['blocks'])}
        old = old_records.get(eid)
        if eid in reported:
            coverage[eid] = dict(identity, response_sha256=response_digest,
                                origin='reviewer_reported', source_accuracy_verified=False)
            history.append({'evidence_id': eid, 'event': 'REVIEW_REPORTED',
                            'response_sha256': response_digest, **identity})
        elif old and all(old.get(k) == v for k,v in identity.items()):
            coverage[eid] = old
        elif old:
            history.append({'evidence_id': eid, 'event': 'COVERAGE_INVALIDATED',
                            'response_sha256': response_digest, 'previous_claim': old})
    active = []
    for issue in reviewed.get('unresolved', []):
        if isinstance(issue, dict) and issue.get('type') == 'source_review_pending':
            history.append({'event': 'PENDING_CLOSED' if issue.get('evidence_id') in coverage else 'PENDING_REBUILT',
                            'evidence_id': issue.get('evidence_id'), 'response_sha256': response_digest})
        else:
            active.append(issue)
    active.extend({'type': 'source_review_pending', 'evidence_id': eid}
                  for eid in evidence if eid not in coverage)
    reviewed['unresolved'] = active
    reviewed['review_coverage'] = coverage
    reviewed['reviewed_evidence_ids_reported'] = sorted(coverage)
    reviewed['accuracy_verified'] = False
    reviewed['content_completeness_verified'] = False


def apply_review(bundle_directory, response_file, target_directory, *, accept_changes,
                 word=True, xlsx=True, pandoc='pandoc', timeout=180):
    source, target = checked_directory(bundle_directory), checked_directory(target_directory)
    require_disjoint(source, target)
    if target.exists():
        raise FileExistsError('Reviewed target already exists; use a new version')
    document, receipt = read_bundle(source)
    require_delivery_target(document, target)
    response, digest = read_response(response_file)
    if accept_changes != digest:
        raise ValueError('Response approval is missing/stale; acknowledge its exact SHA256')
    if response.get('base_content_sha256') != receipt['content_sha256']:
        raise ValueError('Review belongs to another candidate version')
    reviewed = copy.deepcopy(document)
    reviewed.update(variant='reviewed', parent_bundle_id=receipt['bundle_id'],
                    response_sha256=digest, reviewer=response['reviewer'],
                    accuracy_verified=False, content_completeness_verified=False)
    reviewed.setdefault('unresolved', [])
    targets = _index(reviewed)
    seen_issues, changed_targets, applied = set(), set(), []
    for change in response['changes']:
        if not isinstance(change, dict):
            raise ValueError('A review change must be an object')
        issue = change.get('issue_id')
        if not isinstance(issue, str) or not issue.strip() or issue in seen_issues:
            raise ValueError('Every issue needs a unique nonempty issue_id')
        seen_issues.add(issue)
        operation = change.get('operation')
        if operation not in _OPERATIONS:
            raise ValueError(f'Unsupported operation: {operation!r}')
        target_id = change.get('target_id')
        if target_id not in targets:
            raise ValueError(f'Unknown target: {target_id}')
        unit, block, node = targets[target_id]
        if block.get('excluded'):
            raise ValueError('Cannot change an already excluded block')
        if not isinstance(change.get('reason'), str) or not change['reason'].strip():
            raise ValueError('A change must include a source-based reason')
        refs = _evidence_refs(change, unit, reviewed)
        log = {'issue_id': issue, 'operation': operation, 'target_id': target_id,
               'reason': change['reason'], 'evidence_refs': refs, 'source_accuracy_verified': False}
        if operation in {'flag_structure', 'flag_image'}:
            reviewed['unresolved'].append(log)
            continue
        if target_id in changed_targets:
            raise ValueError('Conflicting changes to the same target; combine them before applying')
        changed_targets.add(target_id)
        before = node.get('text')
        if before is None:
            before = node
        if change.get('before') != before or change.get('target_before_hash') != json_hash(before):
            raise ValueError(f'Stale or incorrect modification precondition: {target_id}')
        log['before'] = copy.deepcopy(before)
        if operation == 'replace_text' and (block['kind'] != 'text' or node is not block):
            raise ValueError('replace_text requires a text block')
        if operation == 'replace_cell' and (block['kind'] != 'table' or node is block):
            raise ValueError('replace_cell requires a physical cell; geometry is immutable')
        if operation in {'replace_text', 'replace_cell', 'restore_fragment'}:
            text = change.get('text')
            if not isinstance(text, str) or len(text) > 100000 or '\x00' in text:
                raise ValueError('Replacement text must be a bounded literal string')
            if operation != 'replace_cell' and not text.strip():
                raise ValueError('Text removal requires explicit exclude_overlay')
            if operation == 'restore_fragment':
                if node is not block:
                    raise ValueError('A restored paragraph must be anchored after a block')
                new_id = unit['id']+'.restored_'+json_hash({'issue': issue, 'response': digest})[:12]
                new_block = {'id': new_id, 'kind': 'text', 'label': 'restored_text', 'text': text,
                             'bbox': refs[0]['bbox'], 'evidence_id': refs[0]['evidence_id'],
                             'before_hash': json_hash(text), 'restored_by': issue}
                unit['blocks'].insert(unit['blocks'].index(block)+1, new_block)
                log['created_id'] = new_id
            else:
                node['text'] = text
                node['before_hash'] = json_hash(text)
            log['after'] = text
        elif operation == 'exclude_overlay':
            if block['kind'] != 'text' or node is not block:
                raise ValueError('Only text overlays can be excluded; no table/figure deletion')
            block['excluded'] = True
            block['exclusion_reason'] = change['reason']
            log['after'] = None
        critical = change.get('critical', True)
        if not isinstance(critical, bool):
            raise ValueError('critical must be boolean')
        log['critical'] = critical
        log['independent_read_record'] = change.get('independent_read')
        if critical:
            reviewed['unresolved'].append({'type': 'critical_source_acceptance_required',
                                          'issue_id': issue, 'target_id': target_id,
                                          'independent_record_supplied': bool(change.get('independent_read'))})
        applied.append(log)
    extra = response.get('unresolved', [])
    if not isinstance(extra, list):
        raise ValueError('unresolved must be a list')
    reviewed['unresolved'].extend({'type': 'reviewer_unresolved', 'detail': x} for x in extra)
    _merge_coverage(document, reviewed, response.get('reviewed_evidence_ids', []), digest)
    target.parent.mkdir(parents=True, exist_ok=True)
    with output_lock(target.parent):
        work = Path(tempfile.mkdtemp(prefix='.reviewed-', dir=target.parent))
        try:
            resources = {e['image'] for e in document['evidence'].values()}
            resources.update(b['image'] for u in document['units'] for b in u['blocks'] if b['kind'] == 'image')
            for relative in resources:
                if relative not in receipt['files']:
                    raise ValueError('Unsealed document image')
                src = local_file(source, relative, receipt['files'][relative])
                dst = work / relative
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
            response_bytes = Path(response_file).read_bytes()
            if hashlib.sha256(response_bytes).hexdigest() != digest:
                raise ValueError('Review response changed during application')
            (work/'review_response.json').write_bytes(response_bytes)
            write_json(work/'applied_changes.json', {'schema': 1, 'parent_bundle_id': receipt['bundle_id'],
                'response_sha256': digest, 'changes': applied,
                'approval': 'caller_acknowledged_exact_response', 'source_accuracy_verified': False})
            result = publish_candidate(work, reviewed, word=word, xlsx=xlsx, pandoc=pandoc, timeout=timeout)
            _, again = read_bundle(source)
            if again['bundle_id'] != receipt['bundle_id']:
                raise ValueError('Base bundle changed during application')
            if target.exists():
                raise FileExistsError('Reviewed destination appeared during application')
            work.rename(target)
            return dict(result, directory=str(target), applied_changes=len(applied))
        except BaseException as exc:
            write_json(work/'FAILED_BUILD.json', {'error': f'{type(exc).__name__}: {exc}'})
            work.rename(target.parent/(target.name+'.failed-'+uuid.uuid4().hex[:8]))
            raise
