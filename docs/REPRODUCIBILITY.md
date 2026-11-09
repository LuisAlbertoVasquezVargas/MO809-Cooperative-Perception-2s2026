# Document builds and evidence checks

## Requirements

- Python 3.11 or later; the build and verification scripts use the standard library.
- A LaTeX distribution with `latexmk`, pdfLaTeX, BibTeX, Beamer, PGF/TikZ,
  Latin Modern, Carlito, `microtype`, `amsmath`, `booktabs`, `array`,
  `longtable`, `tabularx`, `colortbl`, `caption`, `placeins`, and `listings`.
- `qpdf` for PDF normalization and lossless sharing of repeated slide resources.
- XeLaTeX and `fontspec` only if rebuilding the earlier proposal slides.

The LaTeX executables must be on `PATH`. All project figures, citations,
fonts used by the proposal, and experiment snapshots are bundled locally.

## Check the evidence

```bash
python scripts/verify_evidence.py
```

This checks the two frozen appendix PDFs, architecture assets, report figure
snapshots, selected Appendix E image, all twenty runtime conditions, all
fifteen Original/Tree conditions, and the medians of all 2,700 raw tree timings.
It performs no model execution or detection postprocessing.

## Build the final report

```bash
python src/report/build.py --document final
```

Output: `src/report/output/final-report.pdf`.

The generator reads the saved JSON/CSV records, checks their agreement, and
produces the report tables and metric macros. Imported PDF figures are
normalized through `qpdf` without resampling their images. The report keeps
the presentation date November 5, 2026, its unified two-line title, and the
shared modern table style.

## Build the final presentation

```bash
python src/slides/source/final/appendix/generate.py
python src/slides/build.py --deck final
```

Output: `src/slides/output/final.pdf`.

The delivered sequence remains 29 slides. Its 83 appendix pages preserve
the detailed technical material and the single-prompt image-generation
example, giving 112 pages in total. Appendix regeneration validates the
frozen source hashes and complete technical-page coverage.

Build intermediates stay under each `output/.build/` directory and are ignored.
The ordinary commands without `--document final` / `--deck final` still build
the earlier proposal documents.

## Experiment records

The [evidence index](EVIDENCE.md) provides the dataset units, protocol files,
and source records for every result. Full-test AP pools all active vehicle
views; the tree comparison evaluates the fixed ego-view cohort. Workloads
above five slots replay recorded inputs.

The archived records identify the epoch-100 checkpoint and reference
implementation commit. Raw datasets, checkpoints, and the original model
prediction archives belong to the experiment environment; this deliverable
contains the document sources and recorded evidence used by the report.
The authors' [CoPerception project](https://github.com/coperception/coperception)
and [data documentation](https://coperception.readthedocs.io/en/latest/datasets/v2x_sim/)
provide the upstream implementation and data-preparation instructions.
