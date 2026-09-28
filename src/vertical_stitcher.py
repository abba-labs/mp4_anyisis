"""
vertical_stitcher.py - 1D 垂直归一化互相关超长图无缝拼接引擎
利用滚屏文档的纯 Y 轴平移物理特性，以 1 像素精度垂直缝合多帧重叠带
"""

import cv2
import numpy as np

def stitch_vertical_frames(frame_list, search_y_range=(350, 500), search_x_range=(200, 1000)):
    if not frame_list:
        return None
    stitched = frame_list[0].copy()
    h, w, _ = stitched.shape
    y1, y2 = search_y_range
    x1, x2 = search_x_range

    for i in range(len(frame_list) - 1):
        f1 = frame_list[i]
        f2 = frame_list[i + 1]

        strip = f1[y1:y2, x1:x2]
        res = cv2.matchTemplate(f2[:, x1:x2], strip, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        if max_val > 0.8:
            dy = y1 - max_loc[1]
            if dy > 5:
                stitched = np.vstack([stitched, f2[h - dy:]])
        else:
            # 降级步长
            stitched = np.vstack([stitched, f2[h - 220:]])

    return stitched
