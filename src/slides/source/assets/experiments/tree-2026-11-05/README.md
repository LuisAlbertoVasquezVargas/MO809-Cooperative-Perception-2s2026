# November 5 Matched Original/Tree Experiment

Frozen from the user's MOVER DiscoNet experiments subproject on November 5,
2026. The source report is `single-frame-disconet-report.pdf`, pages 19–20;
page 20 is the table supplied in the conversation. The exact source paths,
run identity, report hash and imported checksums are in
[import-manifest.json](import-manifest.json).

`tree-comparison.json` and `tree-comparison.csv` contain all n=1–15 results.
The corresponding run metrics, specification, cohort, preflight, frame manifest,
precision/recall NPZ and 2,700 raw timing samples are bundled unchanged.
Original prediction archives remain in the owning MOVER run; the bundled
manifest preserves their hashes and references. No MOVER file is modified.

The import verified each source hash, every CSV metric against the JSON, and
all 30 method/count medians from their 90 raw timing samples. The source
exporter also records recomputation of AP from its saved predictions. This
import does not rerun inference, training or postprocessing.

The native table and summary are generated directly from the frozen CSV:

```bash
python src/slides/source/assets/experiments/tree-2026-11-05/generate_table.py
```

`table-rows.tex`, `summary-values.tex` and `topology-example.tex` are bundled
build inputs. The topology is the saved n=5 preflight tree; logical node IDs
are displayed one-based. `generate_table.py` needs only standard Python.
The LaTeX build does not depend on MOVER or on the screenshot/report PDF.

Both methods use the same checkpoint and 30 ego-1 views. There are three
trials, 90 timings per entry and 427 reference cars. n counts model slots;
above five, recorded scans and poses repeat. AP in that region describes the
replay workload, not newly observed vehicles. The n=1 and n=2 graphs and
predictions are identical; timing differences are measurement variation.

The tree reduces full-resolution evaluations from n² to 3n−2; coarse all-pair
scoring remains quadratic. Full-group timing includes selection and excludes
input transfer and postprocessing. At n=15, inference drops from 185.05 to
99.25 ms (46.4%), with AP@0.5 falling 13.98 points and AP@0.7 falling 15.08.
These are matched subset measurements, separate from the earlier full-test AP.

See the [presentation guide](../../../final/README.md) for scope and placement.
