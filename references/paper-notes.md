# Paper selection and reproduction notes

Selected paper: **Learning Distilled Collaboration Graph for Multi-Agent
Perception (DiscoNet)**, NeurIPS 2021, by Yiming Li, Shunli Ren, Pengxiang Wu,
Siheng Chen, Chen Feng, and Wenjun Zhang. The citation and shared metadata are
recorded in `references.bib` and `../config/project.toml`.

## Selection criteria

The user selected DiscoNet and confirmed that pretrained models are acceptable.
The course project is a simple method study and evaluation. Baseline models may
be trained when needed to reproduce the reference comparisons; developing new
methods is outside the scope. Any baseline training must use the training split,
keeping the evaluation scenes held out.

## Method and assumptions

Section 2 describes spatially weighted cooperation between vehicles and
knowledge distillation from an early-fusion teacher. Only the student is needed
at inference. Use synchronized observations, accurate poses, and communication
without delay or packet loss. All agents can be evaluated on one computer.

## Reproduction contract

Compare DiscoNet, no cooperation, and early fusion on the same small,
fixed set of held-out V2X-Sim scenes. Report AP at IoU 0.5 and 0.7 and example
detections. Prefer pretrained checkpoints; train baselines if needed. First
verify compatible checkpoints, dataset release, and execution
on the desktop RTX 5060 Ti (16 GB VRAM, 16 GB system RAM).

The original paper uses V2X-Sim 1.0; current CoPerception supports 2.0.
The exact release, checkpoints, and subset remain to be selected and recorded.
Subset results or results on another release are not an exact reproduction of
the original benchmark. No experiments have been run.

## Evidence and provenance

- [Primary paper](https://arxiv.org/abs/2111.00643), verified 2026-10-03.
- [Official implementation](https://github.com/ai4ce/DiscoNet).
- [CoPerception dataset documentation](https://coperception.readthedocs.io/en/latest/datasets/v2x_sim/).

Record code and checkpoint revisions, licenses, and dataset provenance before
executing the experiment. Keep published and locally measured results separate.
