"""Small local file helpers; no OCR, video decoding or implicit image selection."""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path


def file_hash(path: Path | str) -> str:
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def image_hash(image) -> str:
    data = f'{image.mode}:{image.size}'.encode() + image.tobytes()
    return hashlib.sha256(data).hexdigest()


def json_hash(value) -> str:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False).encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path | str, value) -> None:
    """Publish complete JSON atomically; never leave a half-written manifest."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise ValueError(f'Refusing symlink output: {path}')
    text = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    fd, temporary = tempfile.mkstemp(prefix='.json-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def require_disjoint(source: Path | str, target: Path | str) -> None:
    source, target = Path(source).resolve(), Path(target).resolve()
    if source == target or source in target.parents or target in source.parents:
        raise ValueError('Input and output directories must be disjoint')


@contextmanager
def output_lock(directory: Path | str):
    """One writer per output. A stale lock requires explicit operator inspection."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    lock = directory / '.screenshot.lock'
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise RuntimeError(f'Output is locked: {lock}; do not remove an active lock') from exc
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8') as stream:
            stream.write(f'pid={os.getpid()}\n')
        yield
    finally:
        lock.unlink(missing_ok=True)


def load_screenshots(source_dir, output_frames_dir, *, roi_config=None, full_image=False):
    """Compatibility entry: explicit region required; only cropped images copied.

    New production callers use screenshots.prepare_screenshots to obtain a
    content-addressed batch and its approval identity. This entry never falls
    back to whole-screen OCR when a region is missing.
    """
    from .screenshots import prepare_screenshots
    result = prepare_screenshots(source_dir, Path(output_frames_dir).parent,
                                 roi_config=roi_config, full_image=full_image)
    return result
