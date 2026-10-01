"""Reuse existing native exports inside ONE screenshot project; no new engine.

Only exact source/ROI/crop/model identities and the same native implementation
qualify. Files are copied, never linked or rewritten. Original inference timings
remain historical provenance, not elapsed work of the new attempt.
"""
from __future__ import annotations

import json
import shutil
import tempfile
import uuid
from pathlib import Path

from .document_format import local_file
from .utils import checked_directory, file_hash, json_hash, write_json


def page_key(item, fingerprint, word):
    return json_hash({'source_sha256': item['source_sha256'], 'roi': item['roi'],
                      'crop_sha256': item['crop_sha256'], 'crop_size': item['crop_size'],
                      'parser': fingerprint, 'word': bool(word)})


def validate_native(directory, signature):
    """Check exact native identity, every output hash and the JSON payload."""
    directory = checked_directory(directory)
    adapter_path = local_file(directory, 'adapter.json')
    before = file_hash(adapter_path)
    adapter = json.loads(adapter_path.read_text(encoding='utf-8'))
    if adapter.get('signature') != signature or adapter.get('errors'):
        raise ValueError('Native cache has another signature or recorded errors')
    files = adapter.get('files')
    if not isinstance(files, dict) or not files or adapter.get('native_json') not in files:
        raise ValueError('Native cache lacks its hashed result inventory')
    for name, digest in files.items():
        local_file(directory, name, digest)
    # No symlink or unrelated file is carried into a new result directory.
    actual = set()
    for path in directory.rglob('*'):
        if path.is_symlink():
            raise ValueError('Native cache contains a symlink')
        if path.is_file():
            actual.add(path.relative_to(directory).as_posix())
    if actual != set(files) | {'adapter.json'}:
        raise ValueError('Native cache contains untracked or missing resources')
    if file_hash(adapter_path) != before:
        raise ValueError('Native cache changed during validation')
    return adapter


def find_candidates(project, fingerprint, implementation, word, *, exclude):
    """Index old successful jobs once. Verification happens before actual reuse.

    The native parser and its patch implement inference/export semantics. The
    orchestration code may change directory layout without invalidating those
    semantics. Its original hash remains in the source run's receipt.
    """
    project, exclude = checked_directory(project), Path(exclude).resolve()
    result = {}
    diagnostics = []
    for report_path in sorted((project / 'batches').glob('*/runs/*/report.json')):
        run = report_path.parent
        if run == exclude:
            continue
        try:
            checked_directory(run)
            approval = json.loads(local_file(run, 'crop_approval.json').read_text(encoding='utf-8'))
            report = json.loads(local_file(run, 'report.json').read_text(encoding='utf-8'))
            manifest = json.loads(local_file(run.parent.parent, 'manifest.json').read_text(encoding='utf-8'))
            if (approval.get('parser_fingerprint') != fingerprint
                    or approval.get('native_word_requested') != bool(word)
                    or approval.get('acknowledgement') != 'caller_acknowledged'
                    or report.get('approval_id') != approval.get('approval_id')
                    or manifest.get('approval_id') != approval.get('approval_id')
                    or report.get('batch_id') != manifest.get('batch_id')):
                continue
            old_impl = approval.get('implementation', {})
            keys = ('parser.py', '_layout_parsing_patch.py')
            if any(not implementation.get(k) or old_impl.get(k) != implementation[k] for k in keys):
                continue
            frames = {f'screenshot_{f["frame_index"]+1:04d}': f for f in manifest.get('frames', [])}
            for item in report.get('items', []):
                frame = frames.get(item.get('id'), {})
                if item.get('status') != 'PARSED_UNVERIFIED' or frame.get('status') != 'READY':
                    continue
                if (frame.get('source_sha256') != item.get('source_sha256')
                        or frame.get('roi') != item.get('roi')
                        or frame.get('file_sha256') != item.get('crop_sha256')
                        or frame.get('crop_size') != item.get('crop_size')):
                    continue
                name = item.get('directory', '')
                path = local_file(run, name + '/adapter.json').parent
                if path.parent != (run/'native').resolve():
                    continue
                key = page_key(item, fingerprint, word)
                result.setdefault(key, []).append(path)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            diagnostics.append({'run': str(run.relative_to(project)), 'error': str(exc)})
    return result, diagnostics


def preserve_attempt(target, run, reason):
    """Archive the entire invalid/unfinished target before the parser can rebuild."""
    target, run = checked_directory(target), checked_directory(run)
    if not target.exists():
        return None
    archive = run/'failed_attempts'/(target.name+'_'+uuid.uuid4().hex[:12])
    checked_directory(archive.parent).mkdir(parents=True, exist_ok=True)
    shutil.move(str(target), str(archive))
    write_json(archive.parent/(archive.name+'.reason.json'), {'reason': reason,
               'original_target': str(target.relative_to(run)), 'files_preserved': True})
    return archive


def restore_candidate(candidates, key, target, signature, project):
    """Materialize one verified cache; unavailable/corrupt candidates are skipped."""
    target, project = checked_directory(target), checked_directory(project)
    if target.exists():
        raise FileExistsError('Reuse target must be absent')
    rejected = []
    for source in candidates.get(key, []):
        work = None
        try:
            adapter = validate_native(source, signature)
            source_adapter_hash = file_hash(source/'adapter.json')
            target.parent.mkdir(parents=True, exist_ok=True)
            work = Path(tempfile.mkdtemp(prefix='.reuse-', dir=target.parent))
            for name, digest in adapter['files'].items():
                src = local_file(source, name, digest)
                dst = work/name
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
            shutil.copyfile(source/'adapter.json', work/'adapter.json')
            validate_native(work, signature)
            validate_native(source, signature)
            if file_hash(source/'adapter.json') != source_adapter_hash:
                raise ValueError('Reuse source changed while copying')
            if target.exists():
                raise FileExistsError('Reuse target appeared while copying')
            work.rename(target)
            return adapter, {'kind': 'cross_batch_exact_cache',
                'source_native': str(source.relative_to(project)),
                'adapter_sha256': source_adapter_hash, 'rejected_candidates': rejected}
        except (OSError, ValueError, KeyError, TypeError) as exc:
            rejected.append({'source': str(source.relative_to(project)), 'error': str(exc)})
        finally:
            if work is not None and work.exists():
                # Only our unpublished temporary copy, never the source cache.
                shutil.rmtree(work)
    return None, {'kind': 'miss', 'rejected_candidates': rejected}
