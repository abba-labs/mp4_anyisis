"""Common utility functions for thin pipeline."""
from __future__ import annotations

import hashlib
import shutil
from pathlib import Path


def file_hash(path: Path | str) -> str:
    path = Path(path)
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def image_hash(image) -> str:
    data = f'{image.mode}:{image.size}'.encode() + image.tobytes()
    return hashlib.sha256(data).hexdigest()


def load_screenshots(source_dir: Path | str, output_frames_dir: Path | str) -> dict:
    """Load screenshots from a directory into standard frame manifest format."""
    source_dir = Path(source_dir)
    output_frames_dir = Path(output_frames_dir)
    output_frames_dir.mkdir(parents=True, exist_ok=True)

    images = sorted([p for p in source_dir.glob("*.png") if not p.name.startswith(".")], key=lambda p: p.name)
    frames = []
    for idx, img_path in enumerate(images):
        dest_name = f"frame_{idx:08d}.png"
        dest_path = output_frames_dir / dest_name
        if not dest_path.exists() or dest_path.stat().st_size != img_path.stat().st_size:
            shutil.copy2(img_path, dest_path)

        frames.append({
            "frame_index": idx,
            "image": dest_name,
            "file_sha256": file_hash(dest_path),
            "source_image": img_path.name
        })

    return {
        "frames": frames,
        "total_frames": len(frames),
        "source_directory": str(source_dir)
    }

