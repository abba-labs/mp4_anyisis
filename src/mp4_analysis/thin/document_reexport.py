"""Retry only existing exporters from an immutable candidate bundle."""
from __future__ import annotations

import shutil
import tempfile
import uuid
from pathlib import Path

from .document_bundle import publish_candidate, read_bundle, require_delivery_target
from .document_format import local_file
from .utils import checked_directory, output_lock, require_disjoint, write_json


def reexport_bundle(bundle_directory, target_directory, *, word=True, xlsx=True,
                    pandoc='pandoc', timeout=180):
    """Keep frozen content; no OCR, review replay or overwrite of older versions."""
    source = checked_directory(bundle_directory)
    target = checked_directory(target_directory)
    require_disjoint(source, target)
    if target.exists():
        raise FileExistsError('Choose a new re-export version directory')
    document, receipt = read_bundle(source)
    require_delivery_target(document, target)
    resources = {entry['image'] for entry in document.get('evidence', {}).values()}
    resources.update(block['image'] for unit in document['units'] for block in unit['blocks']
                     if block['kind'] == 'image')
    target.parent.mkdir(parents=True, exist_ok=True)
    with output_lock(target.parent):
        work = Path(tempfile.mkdtemp(prefix='.reexport-', dir=target.parent))
        try:
            for name in sorted(resources):
                if name not in receipt['files']:
                    raise ValueError('Candidate references an unsealed image')
                src = local_file(source, name, receipt['files'][name])
                dst = work/name
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
            for name in ('review_response.json', 'applied_changes.json'):
                if name in receipt['files']:
                    shutil.copyfile(local_file(source, name, receipt['files'][name]), work/name)
            write_json(work/'reexport_origin.json', {
                'schema':1, 'parent_bundle_id':receipt['bundle_id'],
                'frozen_content_sha256':receipt['content_sha256'],
                'content_modified':False, 'inference_performed':False,
                'reason':'new export attempt; previous candidate and errors retained'})
            result = publish_candidate(work, document, word=word, xlsx=xlsx,
                                       pandoc=pandoc, timeout=timeout)
            _, current = read_bundle(source)
            if current['bundle_id'] != receipt['bundle_id']:
                raise ValueError('Source candidate changed during re-export')
            if target.exists():
                raise FileExistsError('Re-export target appeared during export')
            work.rename(target)
            return dict(result, directory=str(target), content_modified=False)
        except BaseException as exc:
            write_json(work/'FAILED_BUILD.json', {'error':f'{type(exc).__name__}: {exc}'})
            work.rename(target.parent/(target.name+'.failed-'+uuid.uuid4().hex[:8]))
            raise
