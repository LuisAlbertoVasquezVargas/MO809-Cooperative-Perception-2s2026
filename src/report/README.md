# Written Proposal and Final Report

The original proposal remains in `output/report.pdf`. The separate English
final report is in [`output/final-report.pdf`](output/final-report.pdf), based
on the MO809 final presentation and its technical appendices. Its cover retains
the explicitly labeled presentation date, November 5, 2026.

The final report explains DiscoNet's architecture and assumptions, the full-test
own-scan/cooperative benchmark, fixed-checkpoint losses and a detection example,
the n=1–20 runtime-only workload, and the matched n=1–15 Original/Tree ablation.
It includes all runtime and tree-table rows, measured vector figures, references,
and implementation detail. The underlying reproducibility records remain in
the repository's [evidence guide](../../docs/EVIDENCE.md). It distinguishes the
4,000-view full-test AP from the 30-ego-view ablation, and identifies replayed
inputs above five slots. No inference or training is run by a document build.

The illustrated report reuses the project's occlusion and communication
artwork, fusion comparison, preprocessing illustrations, encoder/decoder
diagrams, and the complete alignment-to-fusion sequence. It also includes
worked IoU/confidence/AP examples, six synchronized camera views, the saved
five-slot tree, and a numerical Conv2D/Conv3D walkthrough. A linked list of
figures helps navigate the visual material. The two-line cover title uses
one bold font throughout; the presentation date and black contents are retained.
The cover and inner title page are separate from the abstract. Front matter
uses Roman page numbers and the main text uses Arabic page numbers. Blank
reverse pages allow the main text, technical appendix, and references to
start on right-hand pages when printed on both sides.
The cover uses the original [UNICAMP and IC logo files](source/assets/branding/)
from the author's EQM document.

All eleven tables use the shared style in
[`source/final/tables.tex`](source/final/tables.tex): sans serif text, navy
headers, alternating pale rows, and full-width layouts. Summary rows use a
subtle teal fill. The runtime and Original/Tree tables use tighter row spacing
and retain their recorded-input/replay boundary. Their values still come
directly from the same versioned records.

Additional figures from the existing MOVER project are frozen under
[`source/assets/final/`](source/assets/final/README.md), with exact original
paths and SHA-256 checksums in `sources.json`. Figures already bundled with
the slides are reused directly. No external checkout is required to build
the report, and no new images or experimental measurements are generated.

Build the final report from the repository root:

```bash
python src/report/build.py --document final
```

The LaTeX executables must be on `PATH`; see [the build guide](../../docs/REPRODUCIBILITY.md) for the required packages.

The default command, `python src/report/build.py`, still builds the original
proposal to `output/report.pdf`. The final report uses `source/final.tex` and
`source/final/`; its intermediates are isolated in `output/.build/final/`.
Both use the shared metadata and bibliography. The final report adds official
dataset documentation and one project-repository citation through
`source/final/evidence.bib`. Individual data and provenance files remain
supporting materials indexed in the evidence guide.

`generate_final_tables.py` reads the versioned JSON/CSV files under
`src/slides/source/assets/experiments/` at each final-report build. It checks
the full-test frame/view counts and all fifteen Original/Tree CSV conditions
against the saved JSON, then generates tables and headline metrics in the
ignored build directory. Tables and narrative metric macros therefore use the
same recorded values. Figures reference the versioned slide assets directly;
no original MOVER checkout or running preview service is needed.

Requirements: Python 3.11+, `latexmk`, pdfLaTeX, BibTeX, Latin Modern,
`microtype`, `amsmath`, `booktabs`, `tabularx`, `colortbl`, `listings`, `caption`, `placeins`, and
TikZ. When `qpdf` is available, the final export also normalizes imported
PDF figure dictionaries while preserving encoded image/vector streams.
No third-party Python
package is needed. Sources, metrics, and figure attribution remain editable.

## Original Proposal

The proposal planned a comparison using pretrained models under perfect
spatial and temporal alignment. The completed report distinguishes that plan
from the available measurements: early fusion was not evaluated, own scan
only uses the same DiscoNet weights, and the sparse-tree experiment is an
inference-only ablation.

- Shared metadata: `../../config/project.toml`.
- Entry point: `source/main.tex`.
- Content: `source/sections/`; figures: `source/assets/`.
- Shared bibliography: `../../references/references.bib`.
- Build from the repository root: `python src/report/build.py`.
- Read the generated document at `output/report.pdf`.

The bibliography contains the selected NeurIPS 2021 paper and supporting
references for V2X-Sim and OPV2V. Dataset and checkpoint versions must be matched
before executing the comparison.
