"""Explicit document-region input, using Pillow crop and OpenCV selectROI.

The source directory is read-only. Crops, not screenshots, are the only images
published to OCR and review consumers. A prepared batch is content-addressed;
changing a source, order or region requires a new batch approval.
"""
from __future__ import annotations

import hashlib
import html
import io
import json
import math
import os
import re
import sys
import tempfile
import warnings
from pathlib import Path
from urllib.parse import quote

from PIL import Image, __version__ as pillow_version

from .utils import file_hash, image_hash, json_hash, output_lock, require_disjoint, write_json

SCHEMA = 1
COORDINATES = 'source_pixels_ltrb_exclusive'


def _read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def _name(value):
    if not isinstance(value, str) or not value or value.startswith('.'):
        raise ValueError('Expected a non-hidden screenshot filename')
    if '/' in value or '\\' in value or Path(value).suffix.lower() != '.png':
        raise ValueError(f'Expected a local PNG filename: {value!r}')
    return value


def discover_screenshots(source):
    """Honor the committed manifest; natural filename order only when absent."""
    source = Path(source).resolve()
    if not source.is_dir():
        raise ValueError(f'Choose ONE screenshot document directory: {source}')
    actual = {p.name for p in source.iterdir()
              if p.suffix.lower() == '.png' and not p.name.startswith('.')}
    if not actual:
        raise ValueError('No PNG screenshots; choose a document subdirectory, not its parent')
    if len({n.casefold() for n in actual}) != len(actual):
        raise ValueError('Case-insensitive duplicate filenames are not portable')
    manifest_file = source / 'manifest.json'
    if manifest_file.is_symlink():
        raise ValueError('Source manifest must not be a symlink')
    if manifest_file.exists():
        raw = _read_json(manifest_file)
        entries = raw.get('images') if isinstance(raw, dict) else None
        if not isinstance(entries, list) or not entries:
            raise ValueError('Source manifest requires a nonempty images list')
        names = [_name(entry['filename']) for entry in entries]
        if len(set(names)) != len(names) or set(names) != actual:
            raise ValueError(f'Manifest/file mismatch; missing={sorted(set(names)-actual)}, extra={sorted(actual-set(names))}')
        indices = [entry.get('index') for entry in entries]
        if any(type(i) is not int for i in indices) or sorted(indices) != list(range(1, len(entries)+1)):
            raise ValueError('Manifest indices must be unique consecutive integers starting at 1')
        if raw.get('total_images', len(entries)) != len(entries):
            raise ValueError('Manifest total_images disagrees with images list')
        entries = sorted(entries, key=lambda entry: entry['index'])
        metadata = {'document': str(raw.get('document', source.name)),
                    'source_manifest_sha256': file_hash(manifest_file), 'ordering': 'manifest_index'}
    else:
        def natural(name):
            return tuple((0, int(part)) if part.isdigit() else (1, part.casefold())
                         for part in re.split(r'(\d+)', name))
        names = sorted(actual, key=lambda name: (natural(name), name))
        entries = [{'index': index, 'filename': name} for index, name in enumerate(names, 1)]
        metadata = {'document': source.name, 'source_manifest_sha256': None,
                    'ordering': 'natural_filename_unverified_page_order'}
    metadata['entries'] = entries
    return metadata


def _profile(roi_config, full_image):
    if full_image and roi_config is not None:
        raise ValueError('Choose ROI configuration OR explicitly pre-cropped full images')
    if full_image:
        return {'schema': SCHEMA, 'coordinate_system': COORDINATES,
                'default': {'full_image': True}, 'overrides': {}}
    if roi_config is None:
        raise ValueError('Region required: select/save an ROI or explicitly use --full-image')
    profile = _read_json(roi_config) if isinstance(roi_config, (str, Path)) else roi_config
    if not isinstance(profile, dict) or profile.get('schema') != SCHEMA:
        raise ValueError('Unsupported ROI profile schema')
    if profile.get('coordinate_system') != COORDINATES:
        raise ValueError(f'ROI coordinates must use {COORDINATES}')
    if not isinstance(profile.get('overrides', {}), dict):
        raise ValueError('ROI overrides must be keyed by exact screenshot filename')
    if set(profile) - {'schema', 'coordinate_system', 'default', 'overrides'}:
        raise ValueError('Unknown ROI profile fields')
    return profile


def region_box(profile, filename, size):
    """Do not clamp, pad, rescale or fall back to the full image."""
    spec = profile.get('overrides', {}).get(filename, profile.get('default'))
    if not isinstance(spec, dict):
        raise ValueError(f'No document region configured for {filename}')
    if spec == {'full_image': True}:
        return [0, 0, size[0], size[1]]
    if set(spec) != {'image_size', 'box'}:
        raise ValueError('Region requires image_size and box, or full_image=true')
    expected, box = spec['image_size'], spec['box']
    if not isinstance(expected, list) or len(expected) != 2 or any(type(x) is not int for x in expected):
        raise ValueError('image_size must be [width,height] in original image pixels')
    if tuple(expected) != tuple(size):
        raise ValueError(f'Size changed for {filename}: expected {expected}, found {list(size)}; configure an override')
    if not isinstance(box, list) or len(box) != 4 or any(type(x) is not int for x in box):
        raise ValueError('box must contain four integer pixel coordinates')
    left, top, right, bottom = box
    if not (0 <= left < right <= size[0] and 0 <= top < bottom <= size[1]):
        raise ValueError(f'Empty or out-of-bounds region for {filename}: {box}')
    return list(box)


def _open_pixels(data):
    with warnings.catch_warnings():
        warnings.simplefilter('error', Image.DecompressionBombWarning)
        with Image.open(io.BytesIO(data)) as image:
            if image.format != 'PNG' or getattr(image, 'n_frames', 1) != 1:
                raise ValueError('Only static PNG screenshots are supported')
            if image.getexif().get(274, 1) != 1:
                raise ValueError('Nontrivial EXIF orientation: normalize explicitly before selecting the ROI')
            image.load()
            rgba = image.convert('RGBA')
            background = Image.new('RGBA', image.size, (255, 255, 255, 255))
            result = Image.alpha_composite(background, rgba).convert('RGB')
            result.info.clear()
            return result


def _save_crop(image, path):
    path = Path(path)
    if path.is_symlink():
        raise ValueError('Refusing symlink crop output')
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    data = buffer.getvalue()
    digest = hashlib.sha256(data).hexdigest()
    if path.is_file() and file_hash(path) == digest:
        return digest
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.crop-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return digest


def prepare_screenshots(source, output, *, roi_config=None, full_image=False):
    """Build a crop-only preview without importing or initializing Paddle.

    Batch-level manifest errors fail before OCR. Individual bad images or bad
    regions are recorded as INPUT_ERROR; other independent images remain usable.
    """
    source, output = Path(source).resolve(), Path(output).resolve()
    require_disjoint(source, output)
    discovered = discover_screenshots(source)
    profile = _profile(roi_config, full_image)
    filenames = {entry['filename'] for entry in discovered['entries']}
    if set(profile.get('overrides', {})) - filenames:
        raise ValueError('ROI override references a screenshot not in this document')
    records = []
    for entry in discovered['entries']:
        record = {'frame_index': entry['index']-1, 'source_image': entry['filename']}
        path = source / entry['filename']
        try:
            if path.is_symlink() or not path.is_file():
                raise ValueError('Source must be a regular, non-symlink PNG')
            record['source_sha256'] = file_hash(path)
        except OSError as exc:
            record['input_error'] = f'{type(exc).__name__}: {exc}'
        except ValueError as exc:
            record['input_error'] = str(exc)
        records.append(record)
    identity = {'schema': SCHEMA, 'source_directory': str(source),
                'source_manifest_sha256': discovered['source_manifest_sha256'],
                'profile': profile, 'images': records, 'pillow': pillow_version,
                'normalization': 'static_png_exif1_rgba_on_white_rgb_v1'}
    batch_id = json_hash(identity)
    with output_lock(output):
        owner_path = output / '.screenshot_project.json'
        owner = {'schema': SCHEMA, 'source_directory': str(source)}
        if owner_path.exists():
            if _read_json(owner_path) != owner:
                raise ValueError('Output belongs to another screenshot document')
        elif any(p.name != '.screenshot.lock' for p in output.iterdir()):
            raise ValueError('Unmanaged nonempty output directory; choose a new output')
        else:
            write_json(owner_path, owner)
        batch = output / 'batches' / batch_id
        if batch.is_symlink() or (output / 'batches').is_symlink():
            raise ValueError('Refusing symlink batch output')
        batch.mkdir(parents=True, exist_ok=True)
        frames = []
        for entry, original in zip(discovered['entries'], records):
            record = dict(original, status='INPUT_ERROR')
            if 'input_error' not in record:
                try:
                    data = (source / entry['filename']).read_bytes()
                    if hashlib.sha256(data).hexdigest() != record['source_sha256']:
                        raise ValueError('Source changed during preparation; prepare a new snapshot')
                    pixels = _open_pixels(data)
                    for field, observed in [('width', pixels.width), ('height', pixels.height), ('size_bytes', len(data))]:
                        if field in entry and entry[field] != observed:
                            raise ValueError(f'Stale source manifest {field} for {entry["filename"]}')
                    if entry.get('sha256') and entry['sha256'] != record['source_sha256']:
                        raise ValueError('Source checksum disagrees with manifest')
                    box = region_box(profile, entry['filename'], pixels.size)
                    cropped = pixels.crop(tuple(box))
                    cropped.info.clear()
                    name = f'frame_{record["frame_index"]:08d}.png'
                    crop_path = batch / 'frames' / name
                    if (batch / 'frames').is_symlink():
                        raise ValueError('Refusing symlink crop directory')
                    record.update(status='READY', image=name, source_size=list(pixels.size),
                                  roi=box, source_offset=box[:2], crop_size=list(cropped.size),
                                  coordinate_system='crop_pixels',
                                  file_sha256=_save_crop(cropped, crop_path),
                                  pixel_sha256=image_hash(cropped))
                except (OSError, ValueError, Image.DecompressionBombError, Image.DecompressionBombWarning) as exc:
                    record['input_error'] = f'{type(exc).__name__}: {exc}'
            frames.append(record)
        manifest = {'schema': SCHEMA, 'batch_id': batch_id, 'document': discovered['document'],
                    'source_directory': str(source), 'ordering': discovered['ordering'],
                    'source_manifest_sha256': discovered['source_manifest_sha256'],
                    'roi_profile': profile, 'frames': frames, 'total_frames': len(frames),
                    'ready': sum(f['status'] == 'READY' for f in frames),
                    'failed': sum(f['status'] != 'READY' for f in frames),
                    'outside_region_sent': False, 'accuracy_verified': False}
        # Bind approval to actual crop hashes and failures, not just configuration.
        manifest['approval_id'] = json_hash(manifest)
        write_json(batch / 'manifest.json', manifest)
        _write_preview(batch, manifest)
        write_json(output / 'latest.json', {'batch': f'batches/{batch_id}',
                                          'approval_id': manifest['approval_id']})
        link = f'batches/{batch_id}/preview.html'
        (output / 'preview.html').write_text(
            '<!doctype html><meta charset="utf-8"><title>Document crops</title>'
            f'<a href="{link}">打开当前批次裁剪预览 / Open current crop preview</a>', encoding='utf-8')
    return dict(manifest, batch_directory=str(batch))


def _write_preview(batch, manifest):
    cards = []
    for record in manifest['frames']:
        name = html.escape(record['source_image'])
        if record['status'] == 'READY':
            image = quote('frames/' + record['image'], safe='/')
            body = f'<a href="{image}"><img loading="lazy" src="{image}" alt="Document crop"></a>'
            body += f'<p>原图区域 {record["roi"]}；裁图大小 {record["crop_size"]}</p>'
        else:
            body = f'<p>INPUT_ERROR: {html.escape(record.get("input_error", "unknown"))}</p>'
        cards.append(f'<section><h2>{record["frame_index"]+1}. {name}</h2>{body}</section>')
    (batch / 'preview.html').write_text(
        '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>裁剪预览</title>'
        '<style>body{max-width:1150px;margin:24px auto;font:16px sans-serif}img{max-width:100%}'
        'section{border-top:1px solid #aaa;margin:24px 0}code{overflow-wrap:anywhere}</style>'
        '<h1>仅文档区域：批量裁剪预览</h1><p>未运行OCR。请检查所有图片的区域、顺序和边缘。</p>'
        f'<p>确认参数：<code>--accept-crops {manifest["approval_id"]}</code></p>'
        f'<p>READY {manifest["ready"]} / INPUT_ERROR {manifest["failed"]}</p>'
        + ''.join(cards) + '</html>', encoding='utf-8')


def select_region(source, target, *, filename=None, override=False):
    """Save a profile using the installed OpenCV mouse selector, not a new GUI."""
    source, target = Path(source).resolve(), Path(target).resolve()
    discovered = discover_screenshots(source)
    filename = filename or discovered['entries'][0]['filename']
    if filename not in {entry['filename'] for entry in discovered['entries']}:
        raise ValueError('Selected screenshot is not in the document manifest')
    if target == source / 'manifest.json' or target.suffix.lower() != '.json':
        raise ValueError('Choose a separate ROI .json file, not the source manifest')
    if target.exists() and not override:
        raise FileExistsError('ROI file exists; choose a new file or use --override-image')
    if override and not target.is_file():
        raise ValueError('Create the default ROI profile before a single-image override')
    if (source / filename).is_symlink():
        raise ValueError('Source must not be a symlink')
    image = _open_pixels((source / filename).read_bytes())
    if sys.platform.startswith('linux') and not (os.environ.get('DISPLAY') or os.environ.get('WAYLAND_DISPLAY')):
        raise RuntimeError('No desktop display. Select ROI on the capture computer or supply a JSON profile')
    import cv2
    import numpy as np
    scale = min(1.0, 1280 / image.width, 800 / image.height)
    preview_size = (max(1, round(image.width*scale)), max(1, round(image.height*scale)))
    preview = image.resize(preview_size, Image.Resampling.LANCZOS)
    window = 'Document region: drag, ENTER accept, C cancel'
    try:
        x, y, width, height = cv2.selectROI(window, cv2.cvtColor(np.asarray(preview), cv2.COLOR_RGB2BGR),
                                         showCrosshair=True, fromCenter=False)
    except cv2.error as exc:
        raise RuntimeError('OpenCV GUI unavailable; use --roi-config from a desktop machine') from exc
    finally:
        try:
            cv2.destroyWindow(window)
        except cv2.error:
            pass
    if width <= 0 or height <= 0:
        raise ValueError('Selection cancelled; no profile saved and no full-image fallback')
    sx, sy = image.width/preview_size[0], image.height/preview_size[1]
    box = [math.floor(x*sx), math.floor(y*sy), math.ceil((x+width)*sx), math.ceil((y+height)*sy)]
    profile = (_profile(target, False) if override else
               {'schema': SCHEMA, 'coordinate_system': COORDINATES, 'overrides': {}})
    spec = {'image_size': [image.width, image.height], 'box': box}
    if override:
        profile.setdefault('overrides', {})[filename] = spec
    else:
        profile['default'] = spec
    region_box(profile, filename, image.size)
    write_json(target, profile)
    return profile
