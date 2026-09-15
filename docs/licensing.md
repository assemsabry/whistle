# Licensing and Data Provenance

Whistle's original source code is intended to use the MIT License only after all runtime and training dependencies are compatible with that choice.

## Current audit

- The current YOLO26 training prototype uses the Ultralytics package and checkpoint. Ultralytics publishes its code and models under AGPL-3.0, with an Enterprise option. This prototype must not be presented as an MIT-only derivative until it is replaced by a permissive backend or separately licensed.
- SoccerNet SN-GSR-2024 is published on Hugging Face with a GPL-3.0 dataset license. Whistle may record a download manifest and link to the source, but must not silently relicense or redistribute that dataset as MIT.
- The public soccer-players dataset used for the first smoke training run declares a CC license in its dataset card. Its exact upstream terms and the Roboflow source terms must be retained in the release record.
- RT-DETR's official repository is Apache-2.0 and is the current candidate for an MIT-compatible detector backend, subject to a final audit of its selected checkpoint and dependencies.

## Release policy

Whistle source code, training scripts, configuration, and original utilities can be MIT when the dependency audit passes. External datasets, pretrained checkpoints, and third-party code retain their own licenses. Releases must include a source manifest, checksums, attribution, license text, and redistribution status for every external artifact.
