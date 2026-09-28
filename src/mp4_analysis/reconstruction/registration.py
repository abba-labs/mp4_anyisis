"""
reconstruction/registration.py - 画面配准与高精度位移计算
采用动态自适应搜索窗，移除硬编码像素与静默盲猜回退，提供置信度评估
"""

import cv2
import numpy as np
from typing import Tuple, Optional

class FrameRegistrar:
    def __init__(self, min_confidence: float = 0.80):
        self.min_confidence = min_confidence

    def estimate_vertical_displacement(
        self,
        img1: np.ndarray,
        img2: np.ndarray,
        search_band_y_ratio: Tuple[float, float] = (0.40, 0.65),
        search_band_x_ratio: Tuple[float, float] = (0.20, 0.80)
    ) -> Tuple[int, float]:
        """
        计算两帧在纯垂直滚动下的位移量 dy 及置信度 score。
        若置信度过低，拒绝返回猜测值，返回 dy=0, score=0。
        """
        h, w = img1.shape[:2]
        y1 = int(h * search_band_y_ratio[0])
        y2 = int(h * search_band_y_ratio[1])
        x1 = int(w * search_band_x_ratio[0])
        x2 = int(w * search_band_x_ratio[1])

        strip = img1[y1:y2, x1:x2]
        search_region = img2[:, x1:x2]

        res = cv2.matchTemplate(search_region, strip, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        if max_val < self.min_confidence:
            # 【P0 修复】严禁盲目猜值，明确返回未对准
            return 0, float(max_val)

        dy = y1 - max_loc[1]
        return max(0, dy), float(max_val)
