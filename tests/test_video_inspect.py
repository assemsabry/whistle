from pathlib import Path

import pytest

from whistle.video.inspect import inspect_video


def test_missing_video_is_explicit(tmp_path: Path):
    with pytest.raises(FileNotFoundError, match="Video not found"):
        inspect_video(tmp_path / "missing.mp4")
