"""Convert SoccerNet GSR pitch-line annotations to Ultralytics pose labels.

The generated labels contain only pitch geometry. Player identity, team, and
jersey attributes are intentionally ignored.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


LINE_NAMES = [
    "Big rect. left bottom", "Big rect. left main", "Big rect. left top",
    "Big rect. right bottom", "Big rect. right main", "Big rect. right top",
    "Circle central", "Circle left", "Circle right", "Goal left crossbar",
    "Goal left post left", "Goal left post right", "Goal right crossbar",
    "Goal right post left", "Goal right post right", "Middle line",
    "Side line bottom", "Side line left", "Side line right", "Side line top",
    "Small rect. left bottom", "Small rect. left main", "Small rect. left top",
    "Small rect. right bottom", "Small rect. right main", "Small rect. right top",
]

# Keep the pose head compatible with the official 17-keypoint checkpoint.
KEYPOINT_COUNT = 17


def convert(src: Path, yolo_root: Path, out: Path) -> None:
    val_stems = {p.stem for p in (yolo_root / "images" / "val").glob("*.jpg")}
    for split in ("train", "val"):
        (out / "labels" / split).mkdir(parents=True, exist_ok=True)
    for split in ("train", "val"):
        for ann_file in sorted((src / "train").glob("*/Labels-GameState.json")):
            sequence = ann_file.parent.name
            data = json.loads(ann_file.read_text(encoding="utf-8"))
            by_image = {a["image_id"]: a for a in data["annotations"] if a.get("category_id") == 5}
            for image in data["images"]:
                pitch = by_image.get(image["image_id"])
                if not pitch or not pitch.get("lines"):
                    continue
                points: list[tuple[float, float, int]] = []
                for line in LINE_NAMES[:KEYPOINT_COUNT]:
                    samples = pitch["lines"].get(line, [])
                    if samples:
                        chosen = [samples[0], samples[-1]]
                    else:
                        chosen = [{"x": 0.0, "y": 0.0}, {"x": 0.0, "y": 0.0}]
                    for point in chosen[:1]:
                        x = max(0.0, min(1.0, float(point["x"])))
                        y = max(0.0, min(1.0, float(point["y"])))
                        points.append((x, y, 2 if samples else 0))
                xs = [x for x, _, v in points if v]
                ys = [y for _, y, v in points if v]
                if not xs or not ys:
                    continue
                x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
                stem = f"{sequence}_{Path(image['file_name']).stem}"
                target_split = "val" if stem in val_stems else "train"
                label = [0, (x0 + x1) / 2, (y0 + y1) / 2, max(1e-6, x1 - x0), max(1e-6, y1 - y0)]
                for x, y, v in points:
                    label.extend((x, y, v))
                (out / "labels" / target_split / f"{stem}.txt").write_text(
                    " ".join(f"{value:.7f}" if isinstance(value, float) else str(value) for value in label) + "\n",
                    encoding="utf-8",
                )
        (out / f"{split}.txt").write_text(
            "\n".join(str(p.resolve()) for p in sorted((yolo_root / "images" / split).glob("*.jpg"))) + "\n",
            encoding="utf-8",
        )
    (out / "data.yaml").write_text(
        "path: " + str(out.resolve()) + "\n"
        "train: train.txt\nval: val.txt\n"
        f"kpt_shape: [{KEYPOINT_COUNT}, 3]\nnames: [pitch]\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", type=Path, required=True)
    parser.add_argument("--yolo-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    convert(args.src, args.yolo_root, args.out)


if __name__ == "__main__":
    main()
