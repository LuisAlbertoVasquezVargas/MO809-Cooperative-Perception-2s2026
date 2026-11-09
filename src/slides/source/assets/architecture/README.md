# Architecture Walkthrough Assets

These bundled project assets support the main architecture walkthrough on
PDF pages 14–22 of the final presentation. The build uses local snapshots and
requires no external checkout.

[`sources.json`](sources.json) records bundled filenames and SHA-256 checksums,
plus the code filenames and hashes inspected for the explanations. Private
source locations and transient generation identifiers are omitted.

| Asset | Purpose |
| --- | --- |
| `preprocessing/w44_raw_scan-imagegen-v3.png` | Illustration of one LiDAR scan |
| `preprocessing/w44_occupancy_layers-imagegen-v3.png` | Conceptual binary occupancy and height layers |
| `blocks/unit-2d-cubes-v4.pdf` | Conv2d and the normalization/activation tail |
| `blocks/encoder-stage-cubes-v2.pdf` | Initial/Down, Keep, and optional pointwise 3D unit |
| `encoder/encoder-stage-pipeline-imagegen-v9.png` | Six encoder tensor states and the Stage 3 branch |
| `graph/discograph-three-agents-imagegen-v3.png` | Directed collaboration with three teaching agents |
| `graph/discograph-three-agents-v2-spatial-map.pdf` | Spatial weights for one selected edge |
| `blocks/decoder-stage-cubes-v6.pdf` | Upsampling, skip concatenation, and decoder block |
| `decoder/decoder-stage-pipeline-v6.pdf` | Four decoder stages and their skip inputs |

Useful provenance and available editable SVG sources are preserved.
The encoder's v4 SVG is the numerical/geometry reference used by its v9 redraw;
it is not described as an editable copy of the generated v9 composition.
The selected v9 image is natively 2048 × 768 pixels. Decoder diagrams retain
their imported high-resolution materials and vector lettering.

## Architecture Scope

Shapes on the slides use height × width × channels, omitting batch. The
single-frame occupancy input is 256 × 256 × 13. Encoder Stages 0–4 produce:

| Stage | Output | Routing |
| --- | --- | --- |
| 0 | 256 × 256 × 32 | Saved for the final decoder stage |
| 1 | 128 × 128 × 64 | Saved for decoder Stage 7 |
| 2 | 64 × 64 × 128 | Saved for decoder Stage 6 |
| 3 | 32 × 32 × 256 | Shared and fused by DiscoGraph |
| 4 | 16 × 16 × 512 | Local input to the decoder |

The first decoder stage combines the local Stage 4 output with the fused
Stage 3 map. Subsequent stages use saved Stages 2, 1, and 0. The final decoded
feature map is 256 × 256 × 32; classification and regression heads generate
class scores and box parameters. The heads and routing were checked against
the vendored CoPerception `DiscoNet.py` and `DetModelBase.py` in the experiments
checkout, not inferred solely from the illustration.

The `unit_3d` helper in this reconstruction uses Unflatten → a pointwise Conv3d
→ Flatten with a singleton depth axis. It preserves H/W/C and should not be
presented as evidence of multi-frame temporal aggregation.

The overview and detection-head diagrams are new native TikZ summaries of
these inspected code paths. The selected tensor illustrations are reused
unchanged. No new image generation or diagram-image edits were performed.

## Evidence and Credits

These are AI-assisted teaching illustrations, credited on slides as
“AI generated illustration” or its plural. In particular, the three-agent
attention map contains synthetic, normalized teaching weights, not attention
measured from inference. The preprocessing height-layer image is conceptual,
not a plot of recorded voxel values. Copied JSON provenance files retain the
original history and references to earlier versions; those history files need
not all be present in this selected snapshot.

The architecture slides do not claim a new local training run, complete model
execution, or reproduced benchmark. The final deck's measurement table remains
pending. Sources for the model explanation are Li et al. (2021), Section 2,
and the CoPerception code identified in `sources.json`; the original figure
provenance also records versioned implementation links.
