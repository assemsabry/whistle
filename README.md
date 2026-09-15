# Whistle

![Whistle official poster](media/whistle-poster.png)

**Whistle** is developed and owned by [Assem Sabry](https://assem.one/).

Whistle converts football match video into inspectable temporal data: detections, tracks, JSON/CSV files, and annotated video. It does not identify player names, positions, or jersey numbers, and it has no player-rating task.

The GitHub repository is the complete source repository for Whistle. The companion [Hugging Face repository](https://huggingface.co/assemsabry/whistle) is reserved for released model weights and their minimal model card only.

## Current status

Version `0.0.1` provides:

- Video manifest reading and file validation.
- Stable schemas for frames, detections, and tracks.
- A CLI that accepts MP4 and writes a reproducible JSON manifest.
- Replaceable detector and tracker interfaces without coupling to one library.

No match videos or checkpoints are distributed with this repository. Dataset provenance and licensing must be recorded before adding any data or weights. Released weights are published separately in the Hugging Face repository.

## Usage

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
whistle inspect path\to\match.mp4 --output outputs\match
pytest
```

## Documentation

- [Documentation index](docs/README.md)
- [Architecture](docs/architecture.md)
- [Training](docs/training.md)
- [Inference](docs/inference.md)
- [Data and provenance](docs/data.md)
- [Licensing](docs/licensing.md)
- [Model card](docs/model-card.md)
- [Release process](docs/release.md)

## Repository layout

```text
configs/       Versioned experiment configurations
docs/          Technical documentation and provenance
examples/      Reproducible usage examples
media/         Official project media
scripts/       Operational and release helpers
tests/         Automated tests
tools/         Dataset conversion and download tooling
whistle/       Python package and public CLI
```

## Product stages

Core, Pitch, Ball, basic Events, and Analytics. Speed and distance are withheld when camera calibration fails or confidence is too low.

## License

The intended license for original Whistle code is MIT, subject to the dependency and dataset audit in [Licensing and Data Provenance](docs/licensing.md). Dataset and model-weight licenses remain separate; match videos or derivatives must not be redistributed without permission.
