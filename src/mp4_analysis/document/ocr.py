"""
document/ocr.py - 文本去重与字符级处理
无可靠来源定位时保留全部非空文本；相似度仅供诊断，不作为删除依据。
"""

from collections import deque
from typing import Optional

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
    """Deduplicate only identical observations of a proven identical source.

    ``source_key`` must identify the same physical document region/cell after
    registration, including the segment/document identity. Never derive it from
    text alone or a repeated screen coordinate. Without this evidence, repeated
    text is retained. This intentionally prefers visible duplicates over loss.

    ``similarity_threshold`` remains accepted for constructor compatibility;
    fuzzy similarity is no longer allowed to delete technical content.
    """

    def __init__(self, window_size: int = 35, similarity_threshold: float = 0.85):
        if window_size < 1:
            raise ValueError("window_size must be positive")
        self.window_size = window_size
        self.similarity_threshold = similarity_threshold
        self.history = deque(maxlen=window_size)

    def is_duplicate(self, text_line: str, *, source_key: Optional[str] = None) -> bool:
        if not isinstance(text_line, str):
            raise TypeError("text_line must be a string")
        if not text_line.strip():
            return True
        if source_key is None:
            return False
        if not isinstance(source_key, str) or not source_key.strip():
            raise ValueError("source_key must be a non-empty string or None")

        # Keep raw whitespace: indentation can be semantically significant.
        observation = (source_key, text_line)
        if observation in self.history:
            return True
        self.history.append(observation)
        return False
