# Whistle Architecture

Whistle is a modular post-match football video analysis system owned and developed by Assem Sabry. It does not identify player names, positions, or jersey numbers, and it has no player-rating task.

```text
MP4
 |
 v
Video Ingest + Shot Segmentation
 | frames, timestamps, shot_id
 v
Whistle Detector (YOLO26x pretrained -> football fine-tune)
| player / referee / football boxes + confidence
 v
Whistle Tracker (motion + appearance, ByteTrack adapter)
 | stable track_id + trajectories
+-----------------------+
 |
 v
Pitch Calibration
(segmentation/keypoints + homography + gates)
 | XY metres
 v
Ball State + Possession (football detector + motion filter + temporal probability)
             |
             v
Events (rules first, temporal model second)
             |
             v
Analytics (deterministic metrics + uncertainty propagation)
             |
             v
MP4 overlay + JSON + CSV + Parquet + 2D pitch map + report
```

## Model contracts

| Module | Input | Output | First training target |
| --- | --- | --- | --- |
| Detector | RGB frames/crops | boxes, class, confidence | player, referee, football |
| Tracker | detections + frame timestamps | track IDs and trajectories | HOTA/IDF1 stability |
| Pitch | frames + pitch landmarks | camera state, homography, XY metres | JaC@5 and reprojection error |
| Ball/Possession | football detections + tracks | ball state, owner probability | ball recall and possession F1 |
| Events | tracks, ball state, temporal windows | event type, actors, time, confidence | event mAP/F1 |
| Analytics | trusted state/events | distance, speed, KPIs | deterministic regression tests |
| Quality gates | calibration + track coverage | valid/invalid metric flags | false-metric rate |

## 48-hour execution target

The 48-hour target is a reproducible baseline: environment, data schemas, YOLO26 detector fine-tuning on an available licensed/public sample, tracker integration, visualizer, metrics, and one end-to-end MP4 run. A production-quality Whistle still depends on licensed match data, annotation volume, and validation that cannot honestly be guaranteed before those inputs exist.

## Ownership

Project name: **Whistle**  
Developer and owner: **Assem Sabry**  
Website: https://assem.one/
