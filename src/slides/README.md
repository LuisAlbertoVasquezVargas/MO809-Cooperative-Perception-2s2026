# Project Presentation

The updated presentation in [`output/final.pdf`](output/final.pdf) is a
**five-minute final presentation with one continuous 29-page sequence**.
The Results section now presents the user's November 5 matched Original/Tree
experiment: method, full n=1–15 runtime/AP table, and the n=15 trade-off.
The tree takes 46.4% less inference time at n=15, with AP drops of 13.98 and
15.08 percentage points. Conditions above five replay the recorded inputs.
The earlier full-test AP benchmark and detection example remain in their
existing sections. An 83-page supporting appendix follows the delivered
sequence, giving 112 PDF pages in total.
The final deck uses a minimal visual style: diagrams, pictograms, and short
labels, with paragraph-heavy explanations removed.
Build with `python src/slides/build.py --deck final` from the repository root.
Edit `source/final/talk/` and `source/final/core/`; the entry point is `source/final.tex`.
See the [presentation guide](source/final/README.md) for the sequence.
The existing filename and build option are retained for the open PDF viewer.

The material below documents the original proposal, which retains its own
entry point, output, and frozen cover.

Nine-slide Beamer proposal for the DiscoNet course project, intended for a
short presentation of about six minutes. It covers the motivation,
LiDAR aggregation, perfect communication assumptions, the three fusion strategies,
DiscoNet, and the experiment. This earlier proposal predates the completed
evaluation now included in the final presentation.

The layout follows the author's research presentation template:
Carlito typography, navy text, blue title banners, cyan accents, and the same
logo placement. Content titles match the current MOVER `ProgressTitle`: regular
Carlito at 22 pt with 26 pt leading, natural character width, and the original
9.97 cm banner and padding. Titles retain their natural character width.
The cover retains its separately approved typography.
The deck uses original DiscoNet paper figures for the dataset,
aggregation, and teacher/student method. Slide 2 uses an AI-generated
LiDAR illustration; slide 3 arranges original point-cloud panels from Figure 2
to show alignment, aggregation, and cropping. Both use ordinary TeX layout.
Slide 4 uses a generated four-part illustration of the communication assumptions,
with native TeX headings and captions. Slide 5 uses a generated comparison of
raw points, learned features, and detection outputs, with native explanations
and vertical dividers. Slide 6 shows all three original vector panels of Figure 1
at a common scale, before the existing method explanation. Slide 8 groups detection quality, the V2X-Sim and OPV2V datasets, and CARLA
simulation in three columns. Figure, font, and logo provenance is recorded in
`source/assets/README.md` and `source/assets/papers/README.md`.

The cover follows the current monthly deck's `MoverGeneralTitle` layout:
centered course heading and a three-line project title including
“under Perfect Communication” in the same bold type, an underlined uppercase presenter
name near the bottom center, the four professor names beneath it, and the
presentation date at the bottom left.
The current professor list is Wellington Lobato, Guilherme Maia,
Allan M. de Souza, and Edmundo Madeira.

**The cover is frozen.** Follow `AGENTS.md`; its reference rendering is
`source/assets/frozen/cover-reference.png`. Slides 2 onward remain editable.

## Slide Sequence

1. Approved cover (frozen).
2. Local vs Cooperative — two colored LiDAR scans align and combine to fill a blind spot.
3. LiDAR View Aggregation — original Figure 2 panels: local views, combined cloud, and ego crop.
4. Perfect Communication — four visual assumptions: synchronization, poses, delay, and delivery.
5. Fusion Strategies — what early, intermediate, and late fusion share and when they combine it.
6. Collaboration Schemes — complete Figure 1: early, intermediate, and the authors' proposed scheme.
7. How DiscoNet Works — vehicles, matrix-valued edge weights, and knowledge distillation.
8. Experiments and Tools — detection quality, datasets (V2X-Sim and OPV2V),
   and simulator (CARLA). Detection metrics use AP @ 0.5 and AP @ 0.7 notation.
9. Thanks! Questions? — MOVER closing style: bold 30 pt Thanks!, regular 22 pt Questions?, and the original spacing.

## Build and Edit

Edit `source/sections/`. Shared metadata is loaded from
`../../config/project.toml`; layout helpers are in `source/structure/style.tex`
and `source/structure/visuals.tex`. The latter is used only by slides 2 onward.
Build from the repository root with Python 3.11+, `latexmk`, and XeLaTeX
(including Beamer, TikZ, and `fontspec`):

```bash
python src/slides/build.py
```

The stable output is `output/slides.pdf`; intermediate files stay in
`output/.build/`. The build uses bundled font files and needs no network access.
If the local TeX installation lacks a prepared XeLaTeX format, the script
generates one in that ignored build directory. No system configuration changes
are required.

References are linked on the slides and match `../../references/references.bib`.
