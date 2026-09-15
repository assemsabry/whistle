"""Convert SoccerNet GSR annotations to a detection-only YOLO dataset.

Identity, team, and jersey attributes are intentionally discarded.
"""

import argparse
import json
import os
import random
from pathlib import Path


CLASSES = {1: 0, 2: 1, 3: 2, 4: 3, 7: 4}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    sequences = sorted(p for p in args.root.iterdir() if (p / "Labels-GameState.json").exists())
    rng = random.Random(args.seed)
    rng.shuffle(sequences)
    val_count = max(1, round(len(sequences) * args.val_ratio))
    val_sequences = set(sequences[:val_count])
    for split in ("train", "val"):
        (args.output / "images" / split).mkdir(parents=True, exist_ok=True)
        (args.output / "labels" / split).mkdir(parents=True, exist_ok=True)
    total = 0
    for sequence in sequences:
        split = "val" if sequence in val_sequences else "train"
        data = json.loads((sequence / "Labels-GameState.json").read_text(encoding="utf-8"))
        images = {item["image_id"]: item for item in data["images"]}
        grouped = {}
        for annotation in data["annotations"]:
            grouped.setdefault(annotation["image_id"], []).append(annotation)
        for image_id, image in images.items():
            source = sequence / data["info"]["im_dir"] / image["file_name"]
            destination_name = f"{sequence.name}_{image['file_name']}"
            destination = args.output / "images" / split / destination_name
            if not destination.exists():
                os.link(source, destination)
            lines = []
            for annotation in grouped.get(image_id, []):
                category = CLASSES.get(annotation["category_id"])
                box = annotation.get("bbox_image")
                if category is None or not box:
                    continue
                x, y, w, h = box["x"], box["y"], box["w"], box["h"]
                width, height = image["width"], image["height"]
                lines.append(f"{category} {(x + w / 2) / width:.8f} {(y + h / 2) / height:.8f} {w / width:.8f} {h / height:.8f}")
            (args.output / "labels" / split / f"{Path(destination_name).stem}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
            total += 1
    (args.output / "data.yaml").write_text(
        f"path: {args.output}\ntrain: images/train\nval: images/val\n"
        "names:\n  0: player\n  1: goalkeeper\n  2: referee\n  3: football\n  4: other\n",
        encoding="utf-8",
    )
    print(f"converted {total} frames from {len(sequences)} sequences")


if __name__ == "__main__":
    main()
