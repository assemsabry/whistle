# Whistle

![Whistle official poster](media/whistle-poster.png)

**Whistle** is developed and owned by [Assem Sabry](https://assem.one/).

Whistle converts football match video into inspectable temporal data: detections, tracks, JSON/CSV files, and annotated video. It does not identify player names, positions, or jersey numbers, and it has no player-rating task.

## Current status

Version `0.0.1` provides:

- Video manifest reading and file validation.
- Stable schemas for frames, detections, and tracks.
- A CLI that accepts MP4 and writes a reproducible JSON manifest.
- Replaceable detector and tracker interfaces without coupling to one library.

No match videos or checkpoints are distributed with this repository. Dataset provenance and licensing must be recorded before adding any data or weights.

## Usage

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
whistle inspect path\to\match.mp4 --output outputs\match
pytest
```

## Product stages

Core, Pitch, Ball, basic Events, and Analytics. Speed and distance are withheld when camera calibration fails or confidence is too low.

## License

Original code is Apache-2.0. Dataset and model-weight licenses are separate and must be reviewed; match videos or derivatives must not be redistributed without permission.
