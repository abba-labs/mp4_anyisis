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
        if final_candidate is not None:
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
        stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
        stitcher.setCompositingResol(-1)  # Keep original pixel scale.
        status, panorama = stitcher.stitch(images)
    except cv2.error as exc:
        return {'engine': 'OpenCV SCANS', 'status': 'rejected', 'error': str(exc),
                'originals_retained': True, 'verified': False}
    record = {'engine': 'OpenCV SCANS', 'status_code': int(status),
              'status': 'candidate' if status == cv2.Stitcher_OK else 'rejected',
              'originals_retained': True, 'verified': False,
              'note': 'Native composite is unverified; source-coordinate transform is unavailable.'}
    if status == cv2.Stitcher_OK:
        component = [int(i) for i in stitcher.component()]
        record['included_input_indices'] = component
        if sorted(component) != list(range(len(images))):
            record.update(status='rejected', error='upstream excluded one or more input images')
            return record
        target = Path(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        ok, data = cv2.imencode('.png', panorama)
        if not ok:
            raise RuntimeError('cannot encode SCANS preview')
        data.tofile(target)
        record['image'] = str(target)
    return record


def prepare_reconstructions(manifest, output, *, group_size=8, overlap=2):
    """Bounded native SCANS calls; every selected source retains an explicit route.

    Composites are *derived, unverified* parser inputs, not evidence replacements.
    Rejected batches fall back to original frames. Overlapping batches can repeat
    content; no text is deleted to hide that. No geometric solver is implemented.
    """
    import cv2
    import json
    if (isinstance(group_size, bool) or not isinstance(group_size, int)
            or not 2 <= group_size <= 8 or isinstance(overlap, bool)
            or not isinstance(overlap, int) or not 0 <= overlap < group_size):
        raise ValueError('require 2 <= group_size <= 8 and 0 <= overlap < group_size')
    output = Path(output)
    frames = manifest['frames']
    indices = [f['frame_index'] for f in frames]
    if len(indices) != len(set(indices)) or indices != sorted(indices):
        raise ValueError('source frame indices must be unique and ordered')
    signature = {'schema': 1, 'opencv': cv2.__version__, 'group_size': group_size,
                 'overlap': overlap, 'frames': [(f['frame_index'],
                     file_hash(output/'frames'/f['image'])) for f in frames]}
    # JSON round-trip normalizes tuples before comparing persistent signatures.
    signature = json.loads(json.dumps(signature))
    cache_path = output/'reconstruction.json'
    if cache_path.exists():
        old = json.loads(cache_path.read_text(encoding='utf-8'))
        if old.get('signature') == signature and all(
                (output/name).is_file() and file_hash(output/name) == digest
                for name, digest in old.get('derived_files', {}).items()):
            return dict(old, cache_hit=True)
    batches, jobs, represented = [], [], set()
    for start in range(0, len(frames), group_size-overlap):
        batch = frames[start:start+group_size]
        if len(batch) < 2:
            continue
        relative = f'reconstructed/group_{start:06d}.png'
        result = stitch_preview([output/'frames'/f['image'] for f in batch], output/relative)
        source_indices = [f['frame_index'] for f in batch]
        result.update(source_frame_indices=source_indices, start_time=batch[0]['start_time'],
                      end_time=batch[-1]['end_time'])
        if result['status'] == 'candidate':
            result['image'] = relative
            jobs.append({'id': f'group_{start:06d}', 'input_image': relative,
                         'frame': batch[0], 'source_frames': batch,
                         'coordinate_system': 'reconstructed_pixels',
                         'source_to_canvas_transform': None, 'geometry_verified': False,
                         'kind': 'unverified_composite'})
            represented.update(source_indices)
        batches.append(result)
        if start + group_size >= len(frames):
            break
    for frame in frames:
        if frame['frame_index'] not in represented:
            jobs.append({'id': f"frame_{frame['frame_index']:08d}",
                         'input_image': f"frames/{frame['image']}", 'frame': frame,
                         'source_frames': [frame], 'kind': 'source_frame',
                         'coordinate_system': frame['coordinate_system']})
    jobs.sort(key=lambda j: j['frame']['frame_index'])
    routed = {f['frame_index'] for j in jobs for f in j['source_frames']}
    if routed != set(indices):
        raise RuntimeError('unrouted source observations; refusing partial input plan')
    result = {'signature': signature, 'jobs': jobs, 'batches': batches,
              'selected_observations': len(frames), 'parser_inputs': len(jobs),
              'candidate_count': sum(j['kind']=='unverified_composite' for j in jobs),
              'unrouted_selected_frames': sorted(set(indices)-routed),
              'all_selected_frames_routed': routed == set(indices),
              'content_completeness_verified': False, 'geometry_verified': False,
              'cache_hit': False,
              'derived_files': {j['input_image']: file_hash(output/j['input_image'])
                                for j in jobs if j['kind']=='unverified_composite'}}
    cache_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return result
