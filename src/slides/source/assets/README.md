# Slide Assets

## Final Presentation: Problem Illustration

`illustrations/problem/problem-model-distillation-imagegen-v3.png` is the selected
illustration for final slide 7. It was generated with the built-in `image_gen`
tool, without reference images. It emphasizes a large teacher network guiding a
compact student, with matching target-car symbols for the shared detection task.
The network scale is explicitly conceptual: the actual DiscoNet encoder/decoder
backbone is common to teacher and student, while the teacher has holistic inputs.
The diagram does not establish parameter compression or equal accuracy. The PNG
is copied unchanged; native dimensions and checksum are in the v3 provenance.

The research question, role labels, captions, and dashed training-only
distillation arrow remain native LaTeX in `../final/core/02_problem.tex`.
`illustrations/problem/` also contains the exact prompt, provenance/checksum
record and earlier vector/imagegen versions. The selected v3 prompt uses no
images from slide 5; the earlier v1 illustration and its references are history.

## MOVER Template

The visual layout and four logo files were adapted from the author's
research presentation template on October 3, 2026. The relevant layout
components and logos are bundled locally; private source locations are omitted.
The cover follows `MoverGeneralTitle` in `structure/progress-layout.tex` from
the October 2, 2026 monthly deck, including its centered text, font sizes,
presenter position, and lower-left date. Course metadata replaces the MOVER
meeting title. The professor names beneath the presenter follow the current
course-project roster: Wellington Lobato, Guilherme Maia, Allan M. de Souza,
and Edmundo Madeira. Use this roster for future updates rather than copying
the professor list from the original MOVER template.
The copied files preserve their original names in `logos/`:
`mover_fubep.png`, `unicamp.png`, `ufmg.jpg`, and `eldorado.png`.
These are the user's requested template assets; their ownership is unchanged.

The course deck is self-contained and does not require the MOVER repository
to be present when building. Its main headings are navy, internal labels are
softer blue, and it retains the template's title banners and footer placement.
Content-slide title typography follows the active monthly deck's `ProgressTitle`
in `structure/progress-layout.tex`: regular Carlito at 22 pt, 26 pt leading,
and natural character width. The default banner dimensions, padding, and surrounding
spacing follow `structure/engine.tex`, including the 9.97 cm title banner.
The earlier local 20 pt bold override
has been removed. The frozen cover has its own unchanged font declarations.

## Font

The closing slide follows the research presentation template reviewed
on October 6, 2026: 30/36 pt bold Thanks, 22/27 pt regular Questions?,
0.45 cm extra line spacing, zero node padding, centered at (8 cm, 4.5 cm).
The user's exclamation mark in “Thanks!” is retained. It uses the same bundled
Carlito and shared logos as the cover; the opening cover remains unchanged.

`fonts/` contains Carlito regular, bold, italic, and bold italic from Google
Fonts, with the complete SIL Open Font License in `fonts/OFL.txt`.
`fonts/SOURCE.txt` records the exact upstream revision. XeLaTeX reads these
files directly, so the build does not depend on an OS font installation.

## Paper Figures

`papers/disconet/` contains original figures from the versioned DiscoNet paper:
all three Figure 1 schemes, simulated street scene, combined point clouds,
the Figure 2 overview, and three detection panels. See `papers/README.md` for source URLs, figure
numbers, display crops, and conversion details. These are published examples,
not measurements from the course project.

## Generated LiDAR Illustration

The final presentation documents this asset on appendix pages A80–A83
(PDF pages 109–112): Codex CLI with ChatGPT, simple subscription/install/sign-in
steps, the approved generation prompt from the November 9 test, and
its generated image. The prompt is labeled a tested
reconstruction; exact historical chat wording is unavailable. The original
slide-4 PNG and historical expanded `.prompt.txt` files remain unchanged.
Codex CLI invoked the built-in `image_gen` tool; no unrecorded model version
or generation settings are inferred.

The [November 9 generation archive](illustrations/prompt-trials-2026-11-09/README.md)
contains the selected conversational generation prompt, exact tool submission,
output image, and source hashes used in Appendix E. The original slide-4 image
remains unchanged.

`illustrations/lidar-cooperation-v2.png` is the selected AI-generated educational
illustration, produced with the built-in `image_gen` tool on October 3, 2026.
It corrects the original image's opposing vehicle headings: all vehicles now
travel in the same direction, with A following the truck's rear cargo doors
and B in the adjacent lane. The edit preserves the triptych and LiDAR colors.
The exact edit prompt is `illustrations/lidar-cooperation-v2.prompt.txt`.
The original edit input (`illustrations/lidar-cooperation.png`) and its original
prompt (`illustrations/lidar-cooperation.prompt.txt`) are retained for provenance;
the original image is no longer displayed. The selected PNG is copied unchanged
into this repository; no external file, service, or image generation is required
to build the presentation.

Slide 2 shows two vehicles' LiDAR observations and their combined view. A truck
blocks A's view of another car, while B observes that car from another position.
Cyan and orange points distinguish the two sources. Solid gray scene elements
provide explanatory context; they are not detections. The raster illustration
replaces the previous TikZ ray diagram and is explicitly identified on the slide
as AI-generated. It is not a dataset sample, physically validated scan, measured
result, or an illustration of DiscoNet's exact architecture. It explains
raw-point early fusion; DiscoNet instead shares learned features.
The assumption banner is omitted here; those assumptions remain on slide 4.

## Figure 2 Aggregation Panels

Slide 3 uses original point-cloud panels from Figure 2's teacher-input path.
The full unmodified `papers/disconet/overview.png` is bundled; ordinary TeX
viewports display the individual views, combined cloud, and ego crop.
See `papers/README.md` for provenance and exact coordinates. The slide contains
no AI-generated maps.

## Generated Communication Illustration

`illustrations/perfect-communication.png` is the selected image for slide 4,
generated with the built-in `image_gen` tool on October 3, 2026. The exact prompt
is `illustrations/perfect-communication.prompt.txt`. The four scenes represent
synchronized observations, known positions and headings, zero assumed delay,
and complete packet delivery. They illustrate the project's ideal conditions;
the clocks, poses, and packet graphics are not experimental measurements.

The PNG is copied unchanged into the repository. Headings, short captions, and
the footer are typeset separately in `../sections/communication_settings.tex`.
The previous TikZ car-and-grid drawing is no longer used on this slide.

## Generated Fusion Illustration

`illustrations/fusion-strategies.png` is the slide 5 comparison of early,
intermediate, and late fusion, generated with the built-in `image_gen` tool
on October 3, 2026. The exact prompt is
`illustrations/fusion-strategies.prompt.txt`. The PNG is copied unchanged;
headings, captions, and dividers are native TeX in `../sections/fusion_strategies.tex`.

The three panels illustrate combining raw LiDAR points, learned feature maps,
and detection outputs. Cyan and orange identify two contributing vehicles.
Definitions follow [DiscoNet, Sec. 1](https://arxiv.org/html/2111.00643v2#S1),
also recorded in `../../../../references/references.bib`. The feature activations, channel counts, and bounding boxes
are conceptual, not measurements or an exact implementation. The late-fusion
caption names classes and scores, which are not drawn in the image. The slide
introduces the three general strategies without assigning DiscoNet to one panel;
the following Figure 1 and method slides explain its teacher/student design. The footer is
kept to “AI-generated illustration.” This adds no experiment to the project scope.

## Retained BEV Illustration Draft

`illustrations/disconet-bev-fusion.png` is an unused earlier design, retained
with its prompts. It is no longer displayed on slide 3.
It was generated and refined with the built-in `image_gen` tool on October 3,
2026, guided by [DiscoNet, Sec. 2.1 and Fig. 2](https://arxiv.org/html/2111.00643v2#S2.SS1).
The paper's original Figure 2 was inspected when designing the explanation.
This is an AI-generated schematic, not a copied paper figure or experimental
output. Grid shapes, colors, channel counts, and mask intensities are illustrative.
The learned edge-weight subnetwork is omitted for simplicity.

Exact prompts: `illustrations/disconet-bev-fusion.prompt.txt` and
`illustrations/disconet-bev-fusion-edit.prompt.txt`. The refinement makes the
feature-by-weight multiplication explicit before summation. The selected PNG
is stored unchanged and the build requires no image-generation service.

## Original Vector Illustrations

`diagrams/edge-weights.svg` is an editable schematic for slide 7, exported to
`diagrams/edge-weights.pdf` with `rsvg-convert -f pdf`. It isolates one directed
student edge and associates it with a spatial weight matrix, following
[DiscoNet, Sec. 2.1](https://arxiv.org/html/2111.00643v2#S2.SS1).
The 4 × 4 grid and its intensities are illustrative, not experimental output
or the network's actual resolution. The dashed connector is a callout, not a
communication edge. The full model has bidirectional edges and normalizes
weights across contributing agents at each spatial location. The original
paper figure beside it remains unchanged; Student and Teacher are slide labels.

The experiment overview in `../sections/` uses native text and divider lines
to group detection quality, datasets, and simulators. Its CARLA scene is the
original Figure 3(b) from DiscoNet, not a generated project result. Shared helpers
are in `../structure/visuals.tex`. TikZ also positions the shared MOVER template;
its cover, logos, and headings were not changed for the raster replacement.

## Frozen Cover Reference

`frozen/cover-reference.png` records the user-approved cover at a 1400-pixel
long edge, including “under Perfect Communication” within the main title.
Its balanced lines read “Cooperative Perception” / “with DiscoNet under” /
“Perfect Communication.” Re-render page 1 at the same size to check it after shared changes.
The reference is for verification only and is not embedded in the presentation.
