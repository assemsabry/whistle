"""Small, dependency-free schemas for pipeline interchange."""

from dataclasses import asdict, dataclass
from typing import Any, Dict, Optional, Tuple


@dataclass(frozen=True)
class VideoManifest:
    path: str
    width: Optional[int]
    height: Optional[int]
    fps: Optional[float]
    frame_count: Optional[int]
    duration_ms: Optional[int]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class Detection:
    frame_id: int
    class_name: str
    bbox_xyxy: Tuple[float, float, float, float]
    confidence: float

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        result["bbox_xyxy"] = list(self.bbox_xyxy)
        return result


@dataclass(frozen=True)
class Track:
    track_id: int
    frame_id: int
    role: str
    bbox_xyxy: Tuple[float, float, float, float]
    confidence: float

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        result["bbox_xyxy"] = list(self.bbox_xyxy)
        return result
