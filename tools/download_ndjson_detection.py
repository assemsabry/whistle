"""Download an NDJSON image detection dataset into YOLO directory format."""

import argparse
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def download_one(item, images_dir, labels_dir):
    name = Path(item["file"]).name
    image_path = images_dir / name
    label_path = labels_dir / f"{Path(name).stem}.txt"
    if not image_path.exists():
        urllib.request.urlretrieve(item["url"], image_path)
    annotations = item.get("annotations", {}).get("boxes", [])
    label_path.write_text("\n".join(" ".join(map(str, box)) for box in annotations) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ndjson", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()
    items = []
    for line in args.ndjson.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row.get("type") == "image" and row.get("url"):
            items.append(row)
    for split in ("train", "valid", "test"):
        (args.output / "images" / split).mkdir(parents=True, exist_ok=True)
        (args.output / "labels" / split).mkdir(parents=True, exist_ok=True)
    futures = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for item in items:
            split = "val" if item.get("split") == "valid" else item.get("split", "train")
            futures.append(pool.submit(download_one, item, args.output / "images" / split, args.output / "labels" / split))
        for index, future in enumerate(as_completed(futures), 1):
            future.result()
            if index % 500 == 0:
                print(f"downloaded {index}/{len(futures)}", flush=True)
    (args.output / "data.yaml").write_text(
        "path: " + str(args.output) + "\ntrain: images/train\nval: images/val\ntest: images/test\n"
        "names:\n  0: player\n  1: goalkeeper\n  2: referee\n  3: football\n  4: other\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
