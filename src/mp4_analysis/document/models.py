"""
document/models.py - Document IR (统一中间表示层)
提供标准化数据模型，彻底解耦输入视频、OCR引擎与输出格式
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import json

@dataclass
class BoundingBox:
    xmin: float
    ymin: float
    xmax: float
    ymax: float

@dataclass
class Provenance:
    start_time: float
    end_time: float
    frame_indices: List[int] = field(default_factory=list)

@dataclass
class DocumentElement:
    id: str
    type: str  # text, heading, table, figure, code
    bbox: Optional[BoundingBox] = None
    provenance: Optional[Provenance] = None
    confidence: float = 1.0
    content: Any = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class DocumentPage:
    page_index: int
    elements: List[DocumentElement] = field(default_factory=list)
    image_path: Optional[str] = None
    provenance: Optional[Provenance] = None

@dataclass
class DocumentIR:
    doc_id: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    pages: List[DocumentPage] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        def _serialize(obj):
            if hasattr(obj, "__dict__"):
                return {k: _serialize(v) for k, v in obj.__dict__.items()}
            elif isinstance(obj, list):
                return [_serialize(item) for item in obj]
            elif isinstance(obj, dict):
                return {k: _serialize(v) for k, v in obj.items()}
            return obj
        return _serialize(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)
