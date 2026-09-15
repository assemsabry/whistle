"""Command line entry point for the first Whistle pipeline."""

import argparse
import json
from pathlib import Path
from typing import List, Optional

from whistle.video.inspect import inspect_video


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="whistle")
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect", help="inspect a video and write a manifest")
    inspect.add_argument("path", type=Path)
    inspect.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    if args.command == "inspect":
        manifest = inspect_video(args.path)
        args.output.mkdir(parents=True, exist_ok=True)
        destination = args.output / "video_manifest.json"
        destination.write_text(json.dumps(manifest.to_dict(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(destination)
        return 0
    return 2
