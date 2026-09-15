"""Train the Whistle detector from an Ultralytics YOLO dataset YAML."""

import argparse
from pathlib import Path


def train(data: str, epochs: int, imgsz: int, batch: int, device: str, project: str):
    from ultralytics import YOLO

    model = YOLO("yolo26x.pt")
    return model.train(
        data=data,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        device=device,
        project=project,
        name="whistle-detector-yolo26x",
        pretrained=True,
        amp=True,
        exist_ok=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="configs/detector_yolo26x.yaml")
    parser.add_argument("--epochs", type=int, default=80)
    parser.add_argument("--imgsz", type=int, default=1280)
    parser.add_argument("--batch", type=int, default=-1)
    parser.add_argument("--device", default="0")
    parser.add_argument("--project", default="/mnt/opet-data/whistle/outputs/training")
    args = parser.parse_args()
    Path(args.project).mkdir(parents=True, exist_ok=True)
    train(args.data, args.epochs, args.imgsz, args.batch, args.device, args.project)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
