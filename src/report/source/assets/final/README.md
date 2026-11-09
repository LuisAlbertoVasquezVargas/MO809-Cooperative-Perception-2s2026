# Final Report Figure Snapshots

These project figures and numerical examples retain their original artwork
and values. [sources.json](sources.json) records bundled filenames and SHA-256
checksums. Provenance omits machine-specific paths, private repository
identifiers, and transient generation IDs.

| Directory | Content | Role in the report |
| --- | --- | --- |
| `graph/` | Alignment, rotation/translation, pairing, scoring, softmax, weighting, fusion, and the alignment code example | Architecture walkthrough; synthetic explanatory tensors |
| `metrics/` | IoU geometry, confidence values, and the worked AP curve and records | Numerical teaching examples |
| `cameras/` | Six V2X-Sim camera views for the archived scene_5, frame 000066 example | Recorded scene context |
| `convolution/` | Input planes, kernel slices, Conv2D and Conv3D panels, and numerical records | Worked channel and temporal accumulation |

The report also references the versioned figures already under
`src/slides/source/assets/`, including conceptual artwork, architecture
diagrams, and the measured detection/precision–recall/runtime exports.
Those assets are not duplicated here.

The native report diagram in `source/final/figures/tree-topology.tex` uses
the existing saved five-slot preflight edges from the slide assets. Its
node positions are diagrammatic. `conv3d-example.tex` arranges the original
input, kernel, and output panels at their original aspect ratios; no
numerical label or source image is changed.

The Conv2D example uses all-one 2×2 kernels across three channels. The
Conv3D example has temporal slices `[[1,1],[1,1]]` and `[[1,2],[2,0]]`.
The twelve recorded outputs are in
`convolution/conv3d-sliding-v6-calculations.json`; the two output depth
slices are `[[25,27,11],[14,15,5]]` and `[[8,21,24],[4,16,20]]`.

These figures are local build inputs. No model inference, figure-generation
service, raw dataset, or MOVER checkout is required to compile the report.
