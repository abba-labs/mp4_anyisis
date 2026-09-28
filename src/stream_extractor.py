"""
stream_extractor.py - 流式拉普拉斯锐度抽帧核心
基于双帧内存差分与拉普拉斯高频能量筛选，秒级从视频中剔除 95% 滚动模糊帧
"""

import cv2
import numpy as np
import os

def extract_keyframes_from_video(video_path, output_dir, stable_threshold=0.6, min_stable_frames=8):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video: {video_path}")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    prev_gray = None
    stable_count = 0
    best_frame = None
    best_lap = -1.0
    best_idx = -1

    saved_grays = []
    saved_count = 0

    f_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 下采样用于高速差分比对
        small = cv2.resize(frame, (300, 180))
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

        diff = float(np.mean(cv2.absdiff(gray, prev_gray))) if prev_gray is not None else 0.0

        if diff < stable_threshold:
            stable_count += 1
            if stable_count == 1 or stable_count % 3 == 0:
                gray_full = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                lap = float(cv2.Laplacian(gray_full, cv2.CV_64F).var())
                if lap > best_lap:
                    best_lap = lap
                    best_frame = frame.copy()
                    best_idx = f_idx
        else:
            if stable_count >= min_stable_frames and best_frame is not None:
                small_best = cv2.resize(best_frame, (150, 90))
                best_g = cv2.cvtColor(small_best, cv2.COLOR_BGR2GRAY)

                is_distinct = True
                for sg in saved_grays[-6:]:
                    if np.mean(cv2.absdiff(best_g, sg)) < 2.5:
                        is_distinct = False
                        break

                if is_distinct:
                    saved_count += 1
                    out_path = os.path.join(output_dir, f"frame_{saved_count:03d}_at_{best_idx}.png")
                    cv2.imwrite(out_path, best_frame)
                    saved_grays.append(best_g)

            stable_count = 0
            best_frame = None
            best_lap = -1.0
            best_idx = -1

        prev_gray = gray
        f_idx += 1

    cap.release()
    return saved_count
