# Final Project Presentation

The November 5 MO809 presentation combines the earlier MOVER benchmark with
**the November 5 matched Original/Tree experiment**. The Results section contains the
method comparison, the complete runtime/AP table for n=1–15, and the measured
trade-off at n=15. The delivered talk keeps its **29 pages**, order, and
**November 5, 2026** cover date. A separately numbered **83-page appendix**
follows the original closing slide for the professor's hand-in copy, giving
**112 PDF pages** in total. The five-minute delivery uses brief explanations
of the visual slides; the appendix is supporting material.

Build `../final.tex` with `--deck final`. The stable
[PDF path](../../output/final.pdf) lets the existing viewer refresh. The approved
final cover retains its wording, typography, spacing and lower-left date.
The original proposal in `../main.tex`, including its frozen cover, is unchanged.
No separate speaker-note files are generated.

## Presentation Order

| Pages | Content |
| --- | --- |
| 1–2 | Approved final cover and agenda |
| 3–5 | Motivation, cooperative perception, fusion strategies |
| 6–9 | Problem, teacher/student illustration, original strategy and architecture figures |
| 10–13 | Project objective, accuracy/scaling proposal and individual/cooperative detection example |
| 14–20 | Development overview, method and architecture walkthrough |
| 21–24 | Evaluation: assumptions, actual setup and AP results |
| 25–29 | Results: divider, Original/Tree method, full n=1–15 table, trade-off and closing |
| 30–112 (A1–A83) | Appendix: contents, technical detail, evaluation, numerical examples, complete experiments report, and image-generation example |

## Hand-In Appendix

The appendix includes **all 53 weekly technical slides** and **all 20 pages**
of the DiscoNet experiments report opened for review. The technical source
material uses six navigation pages: an appendix cover, linked contents, and
four section dividers. The final image-generation example adds four more pages.
Weekly task,
progress, and planning pages are excluded at the user's request. The weekly
cover, agenda, section covers, and closing add no technical content and are
replaced by the MO809 presentation and appendix navigation. Detailed variants
of topics summarized in the talk are deliberately retained in full.

| Appendix Pages | Content |
| --- | --- |
| A1–A2 | Appendix cover and linked contents |
| A3–A26 | Voxelization, reusable blocks and code, encoder, DiscoGraph alignment/scoring/weights/fusion, and decoder |
| A27–A37 | IoU, thresholds, confidence, precision/recall/AP, dataset counts, camera views, setup, full-test results, and runtime plot |
| A38–A58 | Complete Conv2D/Conv3D numerical walkthrough, including every sliding-window example |
| A59–A79 | Full 20-page recorded-experiments report, including losses, protocol, runtime n=1–20 and Original/Tree n=1–15 results |
| A80–A83 | Slide 4 image-generation example: Codex CLI access, simple steps, generation prompt, and result |

Local PDF snapshots preserve selectable text, original plots, figures, code,
credits, and resolution; imported pages are not rasterized or redrawn. Only
their visible page counters are adapted for the appendix. The main talk
continues to show a total of 29, and appendix counters run from A1 to A83
(the cover itself has no visible counter). PDF bookmarks and the contents
provide section and source-page navigation. No training or inference is rerun.

The [coverage map](../assets/appendix/coverage.md) accounts for every source
page and records each exclusion. [Source snapshots and hashes](../assets/appendix/README.md)
make the build independent of the MOVER checkout. After intentionally editing
the source-page manifest, regenerate the versioned TeX and coverage map with:

```bash
python src/slides/source/final/appendix/generate.py
```

The final image-generation section uses the approved conversational generation prompt
from the [November 9 reconstruction test](../assets/illustrations/prompt-trials-2026-11-09/README.md).
It names Codex CLI with ChatGPT, gives the subscription/install/sign-in steps,
and shows the exact tested generation prompt and its generated image.
The displayed prompt is labeled a tested reconstruction; the original
chat wording remains unavailable. Its native text is included from the trial's
generated TeX file. The original slide-4
image and historical expanded tool prompts remain unchanged. The access guidance links to the
[official CLI documentation](https://learn.chatgpt.com/docs/codex/cli) and
[subscription information](https://learn.chatgpt.com/docs/pricing), checked on
November 8, 2026. No additional generation is required to build the slides.

The new Appendix E is **Image Generation Example**. The former weekly research
context remains excluded.

The recorded detection example follows the proposal on page 13. Development
covers the method, preprocessing, encoder, DiscoGraph and decoder. Evaluation
retains the existing full-test benchmark. Results replaces the earlier future
plans and old runtime summary with the user's completed November 5 tree
ablation. Pages 1–24 retain their content and order. The agenda and section
covers keep their approved visual style.

## Completed Results and Their Scope

### Detection Benchmark

The prepared **V2X-Sim 2.0 Test split without a roadside unit** contains 10
scenes, 1,000 synchronized frames and 4,000 active vehicle views. There are
300 frames with three vehicles, 400 with four and 300 with five. One fixed
pretrained epoch-100 DiscoNet student is evaluated in FP32 with information
sharing disabled and enabled. Own scan only uses the same student weights;
it is not a separately trained local-only baseline. No new training or
inference was performed to import these results.

| Condition | AP@0.5 (%) | AP@0.7 (%) |
| --- | --- | --- |
| Own scan only | 49.10 | 43.05 |
| Cooperative perception | 70.41 | 64.82 |
| Gain, percentage points | 21.31 | 21.77 |

The precision/recall curves are unchanged vector exports from the recorded
evaluation. These V2X-Sim 2.0 results are not claimed as an exact replication
of the original paper's V2X-Sim 1.0 scores. Early fusion has not been measured
in this imported comparison.

Page 13 shows `scene_5`, raw frame `000066`, ego vehicle 1, with five
participants. Its 17 reference cars, 11 own-scan predictions and 17 cooperative
predictions are example counts, not AP or a claim of perfect matching. This
example is separate from the 1,000-frame test benchmark. The car icon indicates
orientation; the plotted points and boxes come from recorded data/predictions.

### November 5: Original vs. Tree

The new Results section uses the completed run
`tree-comparison-20261105T140612Z` from the MOVER DiscoNet experiments
subproject. It matches **30 ego-1 views** from scenes 9, 97 and 98, with three
timing trials, 90 timing samples per method/count, and 427 reference cars.
Both methods use the unchanged epoch-100 checkpoint in FP32 on the RTX 5060 Ti.
This is a matched subset ablation, separate from the 1,000-frame benchmark
shown earlier.

The original model evaluates n² fine-resolution pairs. The tree variant pools
features to 4×4, scores all n² coarse pairs, averages the two directional edge
scores, and uses descending Kruskal selection to build a maximum spanning
tree. Original 32×32 scoring/warping is applied to both directions of its n−1
edges plus n self pairs: **3n−2 fine pairs**. The slide-26 tree uses the saved
n=5 preflight topology, with one-based logical labels and self links omitted.
Slide 26 calls these directed edges; the counts include self-loops, which are
omitted from the drawing. Only fine-pair work becomes linear; coarse scoring remains quadratic.
There is one fusion round, so a receiver uses its immediate tree neighbors.

| At n=15 | Original | Tree | Change |
| --- | --- | --- | --- |
| Median full-group inference | 185.05 ms | 99.25 ms | 46.4% less time |
| AP@0.5 | 74.46% | 60.48% | −13.98 percentage points |
| AP@0.7 | 67.53% | 52.45% | −15.08 percentage points |

Page 27 contains all fifteen rows from the provided report, including both
AP thresholds. Blue rows use distinct recorded inputs (n≤5); green rows replay
five scans and their poses into additional model slots (n>5). AP uses the same
ego's original labels, counted once per frame. The replay conditions measure
that workload, not perception from extra independently recorded vehicles.
For n=1 and n=2, both methods produce identical graphs and predictions; their
small timing differences are measurement variation.

Timing includes the encoder, coarse scoring, CPU Kruskal selection, fine fusion,
decoder and heads for the full n-slot group. Inputs are already on the GPU;
input transfer, reads/packing, warmups, model loading, box decoding/NMS and AP
scoring are excluded. AP uses confidence >0.7 and rotated NMS IoU 0.01.
The import does not rerun inference or training. All 2,700 saved timing samples
were checked against their medians; CSV AP values match the saved metrics.

The older synthetic-feature protocol, future baseline comparison and n=1–20
runtime-only sources remain inactive files. The original complete-graph
proposal on page 12 retains its n(n−1) peer-pair count and quadratic-work label.
Main-talk content badges retain 29 as their total; appendix badges use A1–A83.

## Build and Edit

From the repository root:

```bash
python src/slides/build.py --deck final
```

The LaTeX executables must be on `PATH`. The [build guide](../../../../docs/REPRODUCIBILITY.md) lists the required packages.

The build uses Python 3.11+, `latexmk`, pdfLaTeX, Beamer, TikZ/PGF, `booktabs`
and Carlito. Intermediates stay in `src/slides/output/.build/final/`.
Presentation sources/assets are local; building does not read MOVER slide
sources. The default build still builds the original proposal with XeLaTeX.
The workstation's missing Carlito package is installed in the ignored local
`.cache/texmf` tree; `TEXMFHOME` selects it without changing the system fonts.
When `qpdf` is available, the build shares byte-identical PDF streams to reduce
repeated image/font resources. Encoded image data and vector content are not
resampled or re-encoded. This optimization uses only standard Python and qpdf;
without qpdf, the same presentation is produced as a larger PDF.

- `../final.tex`: the main-talk order, followed by the separately numbered appendix.
- `appendix/`: appendix navigation, generated source-page includes, and the coverage generator.
- `../assets/appendix/`: frozen weekly and experiments-report PDFs, source hashes, and page-by-page coverage.
- `talk/`: earlier setup, full-test results and detection example.
- `results/`: the active November 5 method comparison, complete table and trade-off.
- `core/`: approved motivation, paper strategy and earlier project slides.
- `architecture/`: detailed architecture walkthrough.
- `sections/`: evaluation support and inactive earlier drafts.
- `structure/`: final-only metadata, template, layout and counters.
- `../assets/experiments/w45-2026-11-04/`: earlier imported evidence.
- `../assets/experiments/tree-2026-11-05/`: today’s matched records, raw timings and generated native table.

Use English, Title Case titles, large visuals and short native labels. Preserve
the approved cover, original paper figures, source-credit style and logo
positions. Do not replace measured curves/detections with generated images.
Visible sources identify the recorded evaluation, paper or illustration;
detailed MOVER provenance stays in repository documentation.

## Template and Asset Provenance

The visual engine was adapted from MOVER's weekly Beamer template on November
3, 2026: Carlito, navy text, blue banners, cyan counters and four logo positions.
The original section dividers remain active. Shared styles and the frozen
original proposal cover are untouched.

The unchanged paper Figure 1(c) is on page 8; the complete vector Figure 2
crop follows on page 9. Both retain explicit source credits.
The teacher/student illustration, objective icons and development illustrations
remain explanatory AI artwork in the main sequence. Network size is a teaching
metaphor, not a measured parameter comparison; the paper uses a common
teacher/student backbone. Slide 23 uses editable hardware and software tables
matching the user's reference, with values from the recorded benchmark setup.

Architecture snapshots, including the owner's uncommitted worktree figures,
retain their attribution. See [architecture provenance](../assets/architecture/README.md),
[paper figures](../assets/papers/README.md), and [general assets](../assets/README.md).
The November 4 import has an
[asset guide](../assets/experiments/w45-2026-11-04/README.md) and
[checksum manifest](../assets/experiments/w45-2026-11-04/import-manifest.json).
The November 5 records have their own [asset guide](../assets/experiments/tree-2026-11-05/README.md)
and [import manifest](../assets/experiments/tree-2026-11-05/import-manifest.json).
No original MOVER files are modified or required to build the slides.
