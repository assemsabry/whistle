# Training

Training is reproducible from the scripts and configurations in this repository. Large datasets and checkpoints are not stored in Git.

## Pipeline

1. Download an approved dataset with a documented revision.
2. Verify checksums and upstream license terms.
3. Convert annotations with the tools in `tools/`.
4. Train the detector and save checkpoints outside the repository.
5. Convert SoccerNet GSR pitch-line annotations with `tools/convert_gsr_pitch_pose.py`.
6. Train and validate pitch calibration on a held-out split.
7. Evaluate anonymous tracking, ball state, and basic event components.
8. Run the end-to-end quality gates before release.

## Reproducibility requirements

Record the commit, dataset revision, configuration, dependency lock, random seed, hardware, and evaluation results for every release candidate.
