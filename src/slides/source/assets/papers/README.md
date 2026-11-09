# Paper Figure Sources

All figures in this directory come from Yiming Li et al., **Learning Distilled
Collaboration Graph for Multi-Agent Perception**, NeurIPS 2021,
[arXiv:2111.00643v2](https://arxiv.org/abs/2111.00643v2).
Downloaded on October 3, 2026. Original figure credit remains with the authors.
Consuming slides include paper citations and figure numbers, except slide 8,
whose legend was explicitly removed by the user. Its Figure 3(b) attribution
is retained here.
Numbered slide references below describe the original proposal unless the
final presentation is explicitly named.

## Final Presentation: Complete Architecture

`disconet/fig2_overview.pdf` displays the complete original Figure 2 on page 9
of the final presentation, after the collaboration-strategy figure. It is
a crop of PDF page 3 of the original paper, with viewport `111 540 500 721`
in bottom-left-origin PDF big points. The native source legend reads
`Source: Li et al., DiscoNet, Figure 2.`

The PDF keeps the original vector paths and embedded fonts, along with the
paper's point-cloud images. No figure elements are redrawn, recolored or
regenerated. The external paragraph caption and following body text are outside
the crop. The existing `overview.png` remains unchanged for the proposal's
panel crops.

`fig2_overview.provenance.json` records the source-paper checksum, figure
viewport and output checksum. `fig2_overview.extract.tex` reproduces the crop
with pdfLaTeX; define `DiscoNetPaper` as the original paper's path before input.
The bundled PDF is sufficient for ordinary presentation builds.

## Final Presentation: Collaboration Strategy

Page 8 displays the complete unchanged Figure 1(c) from the bundled
`disconet/fig1_ours.pdf`, after the Problem illustration. The vector figure
places the intermediate-collaboration student on the left and the early-
collaboration teacher on the right. The original guidance arrow and the
training-only boundary remain intact. Native labels identify the two roles,
and the source legend reads `Source: Li et al., DiscoNet, Figure 1(c).`

## Original Proposal Figure Inventory

| Asset | Source | Use in the Slides |
| --- | --- | --- |
| `disconet/overview.png` | [Figure 2](https://arxiv.org/html/2111.00643v2/overview.png) | Teacher-input point-cloud panels on slide 3 |
| `disconet/camera.png` | [Figure 3(b)](https://arxiv.org/html/2111.00643v2/camera.png) | CARLA simulation illustration on slide 8 |
| `disconet/pointcloud.png` | [Figure 3(a)](https://arxiv.org/html/2111.00643v2/pointcloud.png) | Retained point-cloud asset; currently not displayed |
| `disconet/fig1_early.svg` | [Figure 1(a)](https://arxiv.org/html/2111.00643v2/fig1_early.svg) | Early-collaboration scheme on slide 6 |
| `disconet/fig1_int.svg` | [Figure 1(b)](https://arxiv.org/html/2111.00643v2/fig1_int.svg) | Intermediate-collaboration scheme on slide 6 |
| `disconet/fig1_ours.svg` | [Figure 1(c)](https://arxiv.org/html/2111.00643v2/fig1_ours.svg) | Teacher/student scheme on slides 6 and 7 |
| `disconet/edge1.png` | [Figure 5(a), lower bound](https://arxiv.org/html/2111.00643v2/edge1.png) | Retained local-perception asset; currently not displayed |
| `disconet/edge2.png` | [Figure 5(b), upper bound](https://arxiv.org/html/2111.00643v2/edge2.png) | Retained early-fusion asset; currently not displayed |
| `disconet/edge3.png` | [Figure 5(c)](https://arxiv.org/html/2111.00643v2/edge3.png) | Retained DiscoNet asset; currently not displayed |

`disconet/sources.json` records versioned URLs and SHA-256 checksums for the
downloaded files. The PNGs and SVG are saved exactly as retrieved.

## Display and Conversion

Slide 3 shows five viewports of the unchanged Figure 2 image (`overview.png`,
2041 × 936 pixels at approximately 72 dpi). Coordinates are in source-image
big points, with the origin at the bottom left:

| Panel | Viewport (left, bottom, right, top) |
| --- | --- |
| Agent 1 | `26 672 171 824` |
| Agent 2 | `185 672 330 824` |
| Agent M | `383 675 527 825` |
| Aggregated cloud | `607 639 891 924` |
| Ego crop | `1047 699 1230 888` |

`../../sections/bev_aggregation.tex` arranges
these viewports with new headings and arrows. Source colors and the red crop
rectangle are preserved. The ellipsis indicates agents omitted from the three
displayed local examples. This is the teacher's raw-point aggregation, before
BEV encoding; it is not the student's learned feature aggregation. No original
image pixels are retouched or regenerated.

Slide 6 displays all three Figure 1 panels at the same height, preserving their
aspect ratios, original order, and relative scale. The subfigure labels are
typeset separately as in the paper: “(a) Early,” “(b) Intermediate,” and “(c) Ours.”
“Ours” refers to the paper's authors. No figure content is redrawn or removed.

`fig1_early.pdf`, `fig1_int.pdf`, and `fig1_ours.pdf` are the vector conversions
used by XeLaTeX. Each was generated from its corresponding SVG with:

```bash
rsvg-convert -f pdf -o fig1_ours.pdf fig1_ours.svg
```

The converted PDFs are bundled alongside the original SVGs, so `rsvg-convert`
is not needed to build the slides. Typography is rendered from the original
SVG; the method labels, arrows, and training-only boundary are retained.

The Figure 5 source panels are retained unchanged for provenance after the
Detection Comparison slide was removed at the user's request on October 6,
2026. They are no longer displayed. Each contains three stacked published
examples; none represents a local experiment.

The paper images illustrate V2X-Sim 1.0. The final presentation separately
reports the user's recorded V2X-Sim 2.0 evaluation with a fixed compatible
DiscoNet checkpoint; it does not relabel these paper figures as V2X-Sim 2.0
results. See the [experiment import](../experiments/w45-2026-11-04/README.md).
