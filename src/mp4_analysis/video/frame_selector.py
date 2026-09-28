"""
video/frame_selector.py - 帧选择与质检器
包含拉普拉斯方差锐度计算与视频结束强制 flush 机制，确保最后一屏不丢失
"""

import cv2
import numpy as np
import os
from typing import List, Tuple, Optional

class FrameSelector:
    def __init__(self, stable_threshold: float = 0.6, min_stable_frames: int = 8):
        self.stable_threshold = stable_threshold
        self.min_stable_frames = min_stable_frames

    @staticmethod
    def calculate_sharpness(gray_img: np.ndarray) -> float:
        return float(cv2.Laplacian(gray_img, cv2.CV_64F).var())

    def extract_keyframes(self, video_path: str, output_dir: str) -> List[Tuple[int, float, str]]:
        os.makedirs(output_dir, exist_ok=True)
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise RuntimeError(f"Cannot open video: {video_path}")

        prev_gray = None
        stable_count = 0
        best_frame = None
        best_lap = -1.0
        best_idx = -1

        saved_grays = []
        results = []

        f_idx = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            small = cv2.resize(frame, (300, 180))
            gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
            diff = float(np.mean(cv2.absdiff(gray, prev_gray))) if prev_gray is not None else 0.0

            if diff < self.stable_threshold:
                stable_count += 1
                if stable_count == 1 or stable_count % 3 == 0:
                    gray_full = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    lap = self.calculate_sharpness(gray_full)
                    if lap > best_lap:
                        best_lap = lap
                        best_frame = frame.copy()
                        best_idx = f_idx
            else:
                # 运动发生，结算前一个静止区间
                self._save_candidate_if_valid(best_frame, best_lap, best_idx, stable_count, saved_grays, results, output_dir)
                stable_count = 0
                best_frame = None
                best_lap = -1.0
                best_idx = -1

            prev_gray = gray
            f_idx += 1

        # 【P0 修复】流结束强制 flush 最后一个稳定区间，确保最后一页不丢失
        if stable_count >= self.min_stable_frames and best_frame is not None:
            self._save_candidate_if_valid(best_frame, best_lap, best_idx, stable_count, saved_grays, results, output_dir)

        cap.release()
        return results

    def _save_candidate_if_valid(self, frame, lap, idx, count, saved_grays, results, output_dir):
        if count < self.min_stable_frames or frame is None:
            return

        small_best = cv2.resize(frame, (150, 90))
        best_g = cv2.cvtColor(small_best, cv2.COLOR_BGR2GRAY)

        is_distinct = True
        for sg in saved_grays[-6:]:
            if np.mean(cv2.absdiff(best_g, sg)) < 2.5:
                is_distinct = False
                break

        if is_distinct:
            saved_count = len(results) + 1
            out_filename = f"page_{saved_count:03d}_at_{idx}.png"
            out_path = os.path.join(output_dir, out_filename)
            cv2.imwrite(out_path, frame)
            saved_grays.append(best_g)
            results.append((idx, lap, out_path))
