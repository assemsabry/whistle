"""Video inspection with an optional OpenCV dependency."""

from pathlib import Path
from typing import Union

from whistle.core.schemas import VideoManifest


def inspect_video(path: Union[str, Path]) -> VideoManifest:
    video_path = Path(path).expanduser().resolve()
    if not video_path.is_file():
        raise FileNotFoundError(f"Video not found: {video_path}")

    try:
        import cv2
    except ImportError:
        return VideoManifest(str(video_path), None, None, None, None, None)

    capture = cv2.VideoCapture(str(video_path))
    try:
        if not capture.isOpened():
            raise ValueError(f"Could not open video: {video_path}")
        fps = float(capture.get(cv2.CAP_PROP_FPS)) or None
        frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT)) or None
        duration_ms = int(frames * 1000 / fps) if fps and frames else None
        return VideoManifest(
            str(video_path),
            int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) or None,
            int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) or None,
            fps,
            frames,
            duration_ms,
        )
    finally:
        capture.release()
