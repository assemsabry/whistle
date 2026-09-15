# Contributing to Whistle

Thank you for contributing to Whistle. The project is maintained by Assem Sabry and welcomes focused, reproducible improvements.

## Development setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev,video]"
pytest
```

## Contribution rules

- Keep all public documentation and code comments in English.
- Do not add player names, positions, jersey numbers, identity recognition, or player-rating features.
- Do not commit raw match footage, credentials, tokens, or generated checkpoints.
- Record every external dataset, model, and dependency in `docs/data.md` and `docs/licensing.md`.
- Add tests for behavior changes.
- Keep pull requests small, focused, and reproducible.

## Pull requests

Describe the problem, the change, the test command, and any dataset or model impact. A maintainer must review license and provenance changes before merge.
