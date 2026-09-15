# Whistle Data Provenance

This file records external datasets used or staged for Whistle. External data keeps its upstream license; it is not relicensed by the Whistle code license.

| Source | Use | Size/status | License/status |
| --- | --- | --- | --- |
| `sherjahongir/Football-detection` | Large player, goalkeeper, referee, football detection pretraining | 20k images, about 8.6 GB; download staged on AWS | Dataset card declares MIT; verify upstream image provenance before redistribution |
| `SoccerNet/SN-GSR-2024` | Player/ball localization and pitch calibration | 35.1 GB total; train archive downloading on AWS | GPL-3.0; use only under its terms and publish links/checksums rather than silently relicensing |
| `Francesco/soccer-players-5fuqs` | Initial detection smoke baseline | 163 images | Dataset card declares CC; retain upstream attribution and terms |
| `SoccerNet Action Spotting` | Basic event timestamps | Access and redistribution conditions apply | Use only after accepting the source terms; no raw redistribution by default |

## Class policy

Whistle does not identify player names, positions, teams, or jersey numbers. Detection labels are limited to visible entities needed by the pipeline: player, goalkeeper where available, referee, football, and other/unknown where the source includes it.

## Release policy

Every release must include source URLs, revision/date, checksums, label mappings, preprocessing code, and a clear statement of whether the raw files may be redistributed. When redistribution is not permitted, publish the downloader and manifest instead of the raw videos or images.
