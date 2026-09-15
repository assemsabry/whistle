# Quickstart

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev,video]"
```

## Inspect a video

```powershell
whistle inspect path\to\match.mp4 --output outputs\match
```

## Run tests

```powershell
pytest
```

The source repository contains the software and reproducibility tooling. Model checkpoints are published separately in the [Whistle Hugging Face repository](https://huggingface.co/assemsabry/whistle).
