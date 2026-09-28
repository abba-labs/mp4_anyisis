"""Video decoding via PyAV/FFmpeg, optional OpenCV SCANS previews.

Default selection drops only consecutive pixel-identical observations. Sampling
is explicit and never reported as complete coverage. Originals are never replaced
by an unverified stitched image.
"""
from __future__ import annotations

import hashlib
import math
from pathlib import Path


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def image_hash(image) -> str:
    data = f'{image.mode}:{image.size}'.encode() + image.tobytes()
    return hashlib.sha256(data).hexdigest()


def extract_video(source, output, *, sample_seconds=0.0, start=0.0, end=None,
                  max_frames=None, roi=None):
    """Write selected full-resolution images and a PTS-based source manifest."""
    import av
    source, output = Path(source).resolve(), Path(output)
    if not source.is_file():
        raise FileNotFoundError(source)
    if not math.isfinite(sample_seconds) or sample_seconds < 0:
        raise ValueError('sample_seconds must be finite and nonnegative')
    if not math.isfinite(start) or start < 0 or (end is not None and (not math.isfinite(end) or end <= start)):
        raise ValueError('invalid start/end time')
    if max_frames is not None and max_frames < 1:
        raise ValueError('max_frames must be positive')
    output.mkdir(parents=True, exist_ok=True)
    records, previous_hash, previous_time = [], None, None
    decoded = selected = identical = skipped = 0
    next_time, final_candidate = start, None
    stopped_early = False
    with av.open(str(source)) as container:
        if not container.streams.video:
            raise ValueError('input contains no video stream')
        stream = container.streams.video[0]
        for index, frame in enumerate(container.decode(stream)):
            decoded += 1
            if frame.pts is None or frame.time_base is None:
                raise ValueError(f'frame {index}: no presentation timestamp; refusing to invent one')
            timestamp = float(frame.pts * frame.time_base)
            if previous_time is not None and timestamp < previous_time:
                raise ValueError('non-monotonic presentation timestamps')
            previous_time = timestamp
            if timestamp < start:
                continue
            if end is not None and timestamp >= end:
                stopped_early = True
                break
            image = frame.to_image().convert('RGB')
            if roi is not None:
                x, y, width, height = roi
                if min(x, y) < 0 or min(width, height) < 1 or x+width > image.width or y+height > image.height:
                    raise ValueError('ROI outside video frame')
                image = image.crop((x, y, x+width, y+height))
            digest = image_hash(image)
            if digest == previous_hash:
                identical += 1
                if records and final_candidate is None:
                    records[-1]['end_time'] = timestamp
                    records[-1]['last_frame_index'] = index
                continue
            previous_hash = digest
            candidate = (index, timestamp, image, digest)
            if sample_seconds and timestamp < next_time:
                skipped += 1
                final_candidate = candidate
                continue
            if max_frames is not None and len(records) >= max_frames:
                stopped_early = True
                break
            records.append(_save(candidate, output, roi))
            selected += 1
            next_time = timestamp + sample_seconds
            final_candidate = None
        # The last changed observation is retained even if it misses a sampling tick.
        if final_candidate is not None and not stopped_early:
            if max_frames is None or len(records) < max_frames:
                records.append(_save(final_candidate, output, roi))
                selected += 1
            else:
                stopped_early = True
    if not records:
        raise ValueError('no video frames in requested interval')
    return {
        'source': str(source), 'source_sha256': file_hash(source),
        'decoder': 'PyAV/FFmpeg', 'decoded_frames': decoded,
        'selected_frames': selected, 'identical_observations': identical,
        'sampling_skips': skipped, 'sample_seconds': sample_seconds,
        'start': start, 'end': end, 'max_frames': max_frames, 'roi': roi,
        'limited_run': bool(start or end is not None or max_frames is not None or stopped_early),
        'selection_complete': sample_seconds == 0 and not stopped_early and start == 0 and end is None,
        'content_completeness_verified': False, 'frames': records,
    }


def _save(candidate, output, roi):
    index, timestamp, image, digest = candidate
    filename = f'frame_{index:08d}.png'
    image.save(output / filename)
    return {'frame_index': index, 'last_frame_index': index,
            'start_time': timestamp, 'end_time': timestamp,
            'image': filename, 'image_sha256': digest,
            'width': image.width, 'height': image.height,
            'coordinate_system': 'roi_pixels' if roi else 'source_frame_pixels',
            'source_offset': list(roi[:2]) if roi else [0, 0]}


def stitch_preview(paths, target):
    """Delegate a bounded group to upstream SCANS; preview only, never evidence replacement."""
    import cv2
    import numpy as np
    paths = [Path(p) for p in paths]
    if not 2 <= len(paths) <= 8:
        raise ValueError('SCANS preview requires 2..8 images')
    images = [cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_COLOR) for p in paths]
    if any(image is None for image in images):
        raise ValueError('cannot decode a stitch input')
    try:
        status, panorama = cv2.Stitcher_create(cv2.Stitcher_SCANS).stitch(images)
    except cv2.error as exc:
        return {'engine': 'OpenCV SCANS', 'status': 'rejected', 'error': str(exc),
                'originals_retained': True, 'verified': False}
    record = {'engine': 'OpenCV SCANS', 'status_code': int(status),
              'status': 'candidate' if status == cv2.Stitcher_OK else 'rejected',
              'originals_retained': True, 'verified': False,
              'note': 'No source-coordinate transform supplied by high-level Stitcher; not used for OCR.'}
    if status == cv2.Stitcher_OK:
        target = Path(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        ok, data = cv2.imencode('.png', panorama)
        if not ok:
            raise RuntimeError('cannot encode SCANS preview')
        data.tofile(target)
        record['image'] = str(target)
    return record
