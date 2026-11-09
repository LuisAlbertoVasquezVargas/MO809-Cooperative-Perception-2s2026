# Evidence and reference index

The report's project-owned citations point to this repository at **v1.0.0**.
The links below identify the corresponding records within the archive.

## Experiments

| Evidence | Archived records | Evaluation unit |
| --- | --- | --- |
| Full-test detection | [Benchmark JSON](../src/slides/source/assets/experiments/w45-2026-11-04/full-test-v2-no-rsu-2026-11-03.json), [precision–recall figure](../src/slides/source/assets/experiments/w45-2026-11-04/results-plots-v1.pdf) | 1,000 synchronized frames, 4,000 active vehicle views; fixed checkpoint, sharing off/on |
| Fixed-checkpoint losses | [Loss JSON](../src/slides/source/assets/experiments/w45-2026-11-04/test-loss-v2-no-rsu-2026-11-03.json) | Original five-slot normalization; classification, localization, and total loss |
| Runtime-only scaling | [Summary CSV](../src/slides/source/assets/experiments/w45-2026-11-04/runtime-workload-summary.csv), [scope](../src/slides/source/assets/experiments/w45-2026-11-04/runtime-workload-scope.json), [source record](../src/slides/source/assets/experiments/w45-2026-11-04/runtime-workload-source.json) | 30 frames, 1–20 slots, 90 timings per condition; no AP |
| Original/Tree ablation | [CSV](../src/slides/source/assets/experiments/tree-2026-11-05/tree-comparison.csv), [JSON](../src/slides/source/assets/experiments/tree-2026-11-05/tree-comparison.json), [protocol](../src/slides/source/assets/experiments/tree-2026-11-05/specification.json), [cohort](../src/slides/source/assets/experiments/tree-2026-11-05/cohort.json) | 30 ego-1 views, 427 reference cars, 1–15 slots |
| Raw tree timings | [2,700 timing samples](../src/slides/source/assets/experiments/tree-2026-11-05/timings.jsonl), [run metrics](../src/slides/source/assets/experiments/tree-2026-11-05/run-metrics.json) | 90 samples per method/count; recorded medians are independently checkable |
| Detection example | [Figure](../src/slides/source/assets/experiments/w45-2026-11-04/example-detections-v1.pdf), [provenance](../src/slides/source/assets/experiments/w45-2026-11-04/qualitative-examples-v1.json), [camera images](../src/report/source/assets/final/cameras/) | `scene_5`, raw frame `000066`, ego vehicle 1 |

Above five model slots, scans and poses repeat. The full-test benchmark,
runtime sweep, and tree ablation remain separate evidence sets.

## Figures and technical material

| Material | Location |
| --- | --- |
| Encoder, decoder, and preprocessing figures | [Architecture assets](../src/slides/source/assets/architecture/), [source/hash manifest](../src/slides/source/assets/architecture/sources.json) |
| Full alignment-to-fusion sequence | [Report graph figures](../src/report/source/assets/final/graph/) |
| IoU, confidence, and AP worked examples | [Metric records and figures](../src/report/source/assets/final/metrics/) |
| Numerical Conv2D/Conv3D walkthrough | [Convolution panels and arithmetic](../src/report/source/assets/final/convolution/) |
| Additional report figure sources | [38-file source/hash manifest](../src/report/source/assets/final/sources.json) |
| Presentation appendix inputs | [Frozen weekly PDF](../src/slides/source/assets/appendix/weekly.pdf), [experiment report PDF](../src/slides/source/assets/appendix/disconet-experiments.pdf), [page coverage](../src/slides/source/assets/appendix/coverage.md) |
| Image-generation example in Appendix E | [Selected prompt, generated image, and provenance](../src/slides/source/assets/illustrations/prompt-trials-2026-11-09/) |

Provenance retains bundled filenames, checksums, public attribution, and
technical evidence. Machine-specific paths, private source-repository
identifiers, and transient generation IDs are omitted. Current citations use
the bundled snapshots. Predictions, measured plots, and numerical results
are unchanged.

## Verify the archive

```bash
python scripts/verify_evidence.py
sha256sum -c SHA256SUMS
```

The first command checks figure/snapshot hashes, CSV/JSON consistency, and all
30 tree timing medians. The second checks the distributed final PDFs. A
document rebuild may change PDF metadata, so check the published PDF hashes
before replacing them with locally rebuilt files.
