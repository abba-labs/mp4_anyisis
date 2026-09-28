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
    """Orchestrate OpenCV's SCANS engines through public detail bindings.

    Same affine matcher/estimator/adjuster/warper as upstream Stitcher::SCANS.
    This avoids version-dependent Stitcher.component()/cameras() getters. There
    is no local registration solver. Full-resolution inputs and masks are kept;
    graph-cut selects seams, and NO blending avoids averaging technical text.
    The result is a review candidate, never proof of content completeness.
    """
    import cv2
    import numpy as np
    paths, target = [Path(p) for p in paths], Path(target)
    if not 2 <= len(paths) <= 8:
        raise ValueError('SCANS preview requires 2..8 images')
    if target.resolve() in {p.resolve() for p in paths}:
        raise ValueError('stitch output must not overwrite a source image')
    images = [cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_COLOR) for p in paths]
    if any(image is None for image in images):
        raise ValueError('cannot decode a stitch input')
    record = {'engine': 'OpenCV SCANS detail', 'opencv_version': cv2.__version__,
              'status': 'rejected', 'originals_retained': True, 'verified': False,
              'geometry_verified': False,
              'note': 'Native warp mappings locate observations; seams/content still require review.'}
    try:
        finder = cv2.ORB_create(nfeatures=2000)
        features = [cv2.detail.computeImageFeatures2(finder, im) for im in images]
        matcher = cv2.detail_AffineBestOf2NearestMatcher(False, False, 0.3)
        try:
            matches = matcher.apply2(features)
        finally:
            matcher.collectGarbage()
        included = [int(i) for i in cv2.detail.leaveBiggestComponent(features, matches, 1.0)]
        record['included_input_indices'] = included
        if sorted(included) != list(range(len(images))):
            record['error'] = 'upstream excluded one or more input images'
            return record
        ok, cameras = cv2.detail_AffineBasedEstimator().apply(features, matches, None)
        if not ok:
            raise ValueError('native affine estimation failed')
        for camera in cameras:
            camera.R = camera.R.astype(np.float32)
        adjuster = cv2.detail_BundleAdjusterAffinePartial()
        adjuster.setConfThresh(1.0)
        ok, cameras = adjuster.apply(features, matches, cameras)
        if not ok or len(cameras) != len(images):
            raise ValueError('native affine adjustment failed')
        record['native_affine_transforms'] = [c.R.tolist() for c in cameras]
        if not all(screen_transform_is_safe(c.R) for c in cameras):
            raise ValueError('scale/rotation/shear incompatible with scrolling')
        warper = cv2.PyRotationWarper('affine', 1.0)
        rois = [warper.warpRoi((im.shape[1], im.shape[0]), c.K().astype(np.float32), c.R)
                for im, c in zip(images, cameras)]
        corners = [(r[0], r[1]) for r in rois]
        sizes = [(r[2], r[3]) for r in rois]
        x, y, width, height = cv2.detail.resultRoi(corners=corners, sizes=sizes)
        if min(width, height) <= 0 or width * height > 32_000_000:
            raise ValueError('native canvas exceeds 32 megapixel safety limit')
        warped, masks, mappings = [], [], []
        basis = np.float32([[0, 0], [1, 0], [0, 1]])
        for im, camera in zip(images, cameras):
            intrinsic = camera.K().astype(np.float32)
            _, image = warper.warp(im, intrinsic, camera.R, cv2.INTER_NEAREST, cv2.BORDER_CONSTANT)
            _, mask = warper.warp(np.full(im.shape[:2], 255, np.uint8), intrinsic,
                                  camera.R, cv2.INTER_NEAREST, cv2.BORDER_CONSTANT)
            warped.append(image); masks.append(cv2.UMat(mask))
            # Query the SAME native warper used above; do not guess that camera.R
            # already maps source pixels into the origin-shifted output canvas.
            dst = np.float32([warper.warpPoint(tuple(map(float, p)), intrinsic, camera.R)
                              for p in basis]) - np.float32([x, y])
            matrix = np.vstack([cv2.getAffineTransform(basis, dst), [0, 0, 1]])
            if not screen_transform_is_safe(matrix):
                raise ValueError('native pixel mapping is incompatible with scrolling')
            mappings.append(matrix.tolist())
        cv2.detail_GraphCutSeamFinder('COST_COLOR').find(
            [im.astype(np.float32) for im in warped], corners, masks)
        blender = cv2.detail.Blender_createDefault(cv2.detail.Blender_NO, False)
        blender.prepare((x, y, width, height))
        for im, mask, corner in zip(warped, masks, corners):
            blender.feed(im.astype(np.int16), mask, corner)
        panorama, valid = blender.blend(None, None)
        if panorama is None or valid is None or not np.any(valid):
            raise ValueError('native composition returned an empty canvas')
        panorama = np.clip(panorama, 0, 255).astype(np.uint8)
        panorama[valid == 0] = 255  # blank outside observed source regions, not content repair
        target.parent.mkdir(parents=True, exist_ok=True)
        ok, encoded = cv2.imencode('.png', panorama)
        if not ok:
            raise ValueError('cannot encode native composite')
        encoded.tofile(target)
        record.update(status='candidate', status_code=0, image=str(target),
                      canvas_origin=[x, y], canvas_size=[width, height],
                      source_to_canvas_transforms=mappings,
                      compositing='native_graphcut_no_blending',
                      interpolation='nearest', source_pixels_rescaled=False)
    except (cv2.error, ValueError, AttributeError) as exc:
        record['error'] = str(exc)
    return record


def prepare_reconstructions(manifest, output, *, group_size=8, overlap=2):
    """Bounded native SCANS calls; every selected source retains an explicit route.

    Composites are derived, unverified parser inputs, not evidence replacements.
    Rejected batches fall back to original frames. No text is deleted.
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
    signature = {'schema': 3, 'opencv': cv2.__version__, 'group_size': group_size,
                 'overlap': overlap, 'frames': [(f['frame_index'],
                     file_hash(output/'frames'/f['image'])) for f in frames]}
    signature = json.loads(json.dumps(signature))
    cache_path = output/'reconstruction.json'
    if cache_path.exists():
        old = json.loads(cache_path.read_text(encoding='utf-8'))
        if old.get('signature') == signature and all(
                (output/name).is_file() and file_hash(output/name) == digest
                for name, digest in old.get('derived_files', {}).items()):
            return dict(old, cache_hit=True)
    batches, jobs, represented = [], [], set()
    def attempt(batch, key, split=False):
        if len(batch) < 2:
            return
        relative = f'reconstructed/group_{key}.png'
        result = stitch_preview([output/'frames'/f['image'] for f in batch], output/relative)
        source_indices = [f['frame_index'] for f in batch]
        result.update(source_frame_indices=source_indices, start_time=batch[0]['start_time'],
                      end_time=batch[-1]['end_time'])
        batches.append(result)
        if result['status'] == 'candidate':
            result['image'] = relative
            jobs.append({'id': f'group_{key}', 'input_image': relative,
                         'frame': batch[0], 'source_frames': batch,
                         'coordinate_system': 'reconstructed_pixels',
                         'source_to_canvas_transform': result.get('source_to_canvas_transforms'),
                         'geometry_verified': False, 'kind': 'unverified_composite'})
            represented.update(source_indices)
        elif split and len(batch) >= 4:
            middle = len(batch)//2
            attempt(batch[:middle], key+'_a')
            attempt(batch[middle:], key+'_b')
    for start in range(0, len(frames), group_size-overlap):
        batch = frames[start:start+group_size]
        attempt(batch, f'{start:06d}', split=True)
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


def screen_transform_is_safe(matrix, tolerance=0.02):
    """Reject distortions; does not establish that two images show the same text."""
    import numpy as np
    matrix = np.asarray(matrix)
    return (matrix.shape == (3,3) and bool(np.isfinite(matrix).all())
            and bool(np.allclose(matrix[2], [0,0,1], atol=1e-6, rtol=0))
            and bool(np.allclose(matrix[:2,:2], np.eye(2), atol=tolerance, rtol=0)))
