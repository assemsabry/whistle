# Training

Training is reproducible from the scripts and configurations in this repository. Large datasets and checkpoints are not stored in Git.

## Pipeline

1. Download an approved dataset with a documented revision.
2. Verify checksums and upstream license terms.
3. Convert annotations with the tools in `tools/`.
4. Train the detector and save checkpoints outside the repository.
5. Validate on a held-out split.
6. Train and validate tracking, pitch, ball, and event components.
7. Run the end-to-end quality gates before release.

## Reproducibility requirements

Record the commit, dataset revision, configuration, dependency lock, random seed, hardware, and evaluation results for every release candidate.
