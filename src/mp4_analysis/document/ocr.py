"""
document/ocr.py - 文本去重与字符级处理
实现真正的编辑距离对比，移除 `'第'` 与 `len < 2` 粗暴黑名单，保护芯片关键单字符
"""

from typing import List, Dict, Any

def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def string_similarity(s1: str, s2: str) -> float:
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0
    dist = levenshtein_distance(s1, s2)
    return 1.0 - (dist / max_len)

class StreamTextDeduplicator:
    def __init__(self, window_size: int = 35, similarity_threshold: float = 0.85):
        self.window_size = window_size
        self.similarity_threshold = similarity_threshold
        self.history = []

    def is_duplicate(self, text_line: str) -> bool:
        clean = text_line.strip()
        # 【P0 修复】绝不删除 '第'、'0'、'1'、'A' 等单字符，仅过滤空行
        if not clean:
            return True

        # 与滑窗内的历史行比较
        recent_window = self.history[-self.window_size:]
        for prev in recent_window:
            if clean == prev:
                return True
            # 编辑距离判定
            if len(clean) >= 4 and len(prev) >= 4:
                sim = string_similarity(clean, prev)
                if sim >= self.similarity_threshold:
                    return True
            # 包含判定
            if len(clean) >= 8 and (clean in prev or prev in clean):
                return True

        self.history.append(clean)
        return False
