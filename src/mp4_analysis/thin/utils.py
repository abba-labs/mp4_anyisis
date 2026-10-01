"""Small local file helpers; no OCR, video decoding or implicit selection."""
from __future__ import annotations

import hashlib
import json
import os
import re
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
    return hashlib.sha256(f'{image.mode}:{image.size}'.encode() + image.tobytes()).hexdigest()


def json_hash(value) -> str:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False).encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def checked_directory(directory: Path | str) -> Path:
    """Reject redirected output ancestors before resolving them."""
    path = Path(directory).absolute()
    for part in (path, *path.parents):
        if part.is_symlink() or (hasattr(part, 'is_junction') and part.is_junction()):
            raise ValueError(f'Redirected directory is not supported: {part}')
    return path.resolve()


def write_json(path: Path | str, value) -> None:
    """Publish complete JSON atomically, not a partially overwritten manifest."""
    path = Path(path)
    checked_directory(path.parent).mkdir(parents=True, exist_ok=True)
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
    source, target = Path(source).resolve(), checked_directory(target)
    if source == target or source in target.parents or target in source.parents:
        raise ValueError('Input and output directories must be disjoint')


def identity_directory(parent, identity, *, prefix):
    """Short disk names, FULL hash collision checking; reuse legacy long paths.

    The caller holds the project output lock. Existing data is not renamed or
    deleted. The 16-digit path is only a locator, never the identity check.
    """
    if not isinstance(identity, str) or not re.fullmatch(r'[0-9a-f]{64}', identity):
        raise ValueError('Directory identity must be a complete SHA256')
    if prefix not in {'b_', 'r_'}:
        raise ValueError('Unsupported identity directory prefix')
    parent = checked_directory(parent)
    legacy = parent / identity
    target = legacy if legacy.exists() else parent / (prefix + identity[:16])
    checked_directory(target)
    marker = target / '.identity.json'
    if marker.exists():
        if marker.is_symlink() or json.loads(marker.read_text(encoding='utf-8')) != {'sha256': identity}:
            raise ValueError('Short directory identity collision or corrupted marker')
    elif target.exists() and target != legacy and any(target.iterdir()):
        raise ValueError('Unmanaged short directory; refusing to overwrite it')
    target.mkdir(parents=True, exist_ok=True)
    if not marker.exists():
        write_json(marker, {'sha256': identity})
    return target


@contextmanager
def output_lock(directory: Path | str):
    """One writer. Never auto-remove a stale lock; inspect its recorded PID."""
    directory = checked_directory(directory)
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
    """Compatibility entry; explicit ROI or explicitly pre-cropped input only."""
    from .screenshots import prepare_screenshots
    return prepare_screenshots(source_dir, Path(output_frames_dir).parent,
                               roi_config=roi_config, full_image=full_image)
