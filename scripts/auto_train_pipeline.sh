#!/usr/bin/env bash
set -euo pipefail

# Sequential Whistle training/release queue for the dedicated AWS workspace.
# The orchestrator never embeds credentials and never deletes checkpoints.

ROOT="${WHISTLE_ROOT:-/mnt/opet-data/whistle}"
LOG_DIR="$ROOT/logs"
OUT_DIR="$ROOT/outputs/training"
PITCH_PID="${1:?Pass the active Pitch training PID}"
PIPELINE_LOG="$LOG_DIR/whistle_auto_pipeline.log"

mkdir -p "$LOG_DIR"
exec > >(tee -a "$PIPELINE_LOG") 2>&1

echo "[$(date -Is)] Whistle sequential pipeline started; waiting for Pitch PID $PITCH_PID"
while kill -0 "$PITCH_PID" 2>/dev/null; do
  sleep 60
done

PITCH_RUN="$OUT_DIR/whistle-pitch-yolo26x-pose-b4-v7"
if [[ ! -f "$PITCH_RUN/weights/best.pt" ]]; then
  echo "[$(date -Is)] BLOCKED: Pitch training ended without best.pt"
  exit 2
fi
echo "[$(date -Is)] COMPLETE: Pitch checkpoint found"

# Detector validation is deterministic and can run without new data.
echo "[$(date -Is)] STAGE: detector validation"
"$ROOT/venv/bin/yolo" detect val \
  model="$OUT_DIR/whistle-yolo26x-gsr-batch24/weights/best.pt" \
  data="$ROOT/datasets/soccernet-gsr/yolo/data.yaml" \
  imgsz=1280 batch=20 device=0 \
  project="$OUT_DIR" name=whistle-detector-final-val exist_ok=True

# Tracker integration is an evaluation stage, not a separate neural training job.
if [[ -f "$ROOT/repo/tools/evaluate_tracking.py" ]]; then
  echo "[$(date -Is)] STAGE: tracker evaluation"
  "$ROOT/venv/bin/python" "$ROOT/repo/tools/evaluate_tracking.py" \
    --dataset "$ROOT/datasets/soccernet-gsr" \
    --output "$ROOT/outputs/tracking"
else
  echo "[$(date -Is)] BLOCKED: tracker evaluation tool is not published yet"
fi

# Events require frame-level Action Spotting labels. Do not train on sequence-level
# action metadata because that would produce invalid event supervision.
if [[ -f "$ROOT/datasets/action-spotting/data.yaml" ]]; then
  echo "[$(date -Is)] STAGE: basic events training"
  "$ROOT/venv/bin/python" "$ROOT/repo/tools/train_events.py" \
    --data "$ROOT/datasets/action-spotting/data.yaml" \
    --output "$OUT_DIR/whistle-events"
else
  echo "[$(date -Is)] BLOCKED: frame-level Action Spotting dataset is unavailable"
fi

echo "[$(date -Is)] Whistle sequential pipeline finished"
