# Hand-In Appendix Sources

Frozen copies of the two supporting documents reviewed with the user:

- `weekly.pdf`: the 69-page MOVER weekly deck dated November 4, 2026.
- `disconet-experiments.pdf`: the complete 20-page DiscoNet experiments report,
  exported on November 5, 2026.

[sources.json](sources.json) records bundled filenames, SHA-256 hashes, page
titles, page selections, and exclusion reasons. [coverage.md](coverage.md)
maps every imported source page to its page in the MO809 PDF. All 53 weekly
technical pages and all 20 report pages are included. The sixteen excluded weekly
pages are navigation, covers, the closing, and the four task/progress/planning
pages removed at the user's request.
Where the main talk summarizes a topic, its full-detail source remains in the
appendix.

The snapshot import changes no source document or experiment record. PDF pages
are embedded directly, preserving vector content, selectable text, figures,
code, and source credits. Only visible pagination is replaced: weekly counters
become appendix counters, and report footer numbers become source-page labels.
The original talk keeps its 29-page counter and November 5 presentation date.

The appendix's linked contents and PDF bookmarks group the material into
Architecture and Implementation, Evaluation and Reproduction, Conv2D and
Conv3D, and Complete Experiment Record. A final native LaTeX section, Image
Generation Example, names Codex CLI with ChatGPT and shows access instructions,
simple steps, the approved tested generation prompt, and its generated
image from the November 9 trial. The displayed prompt is
labeled a tested reconstruction; exact historical wording is unavailable.
The original slide-4 illustration and complete historical tool prompts remain
unchanged. The build reuses assets under `illustrations/` and performs no new
generation or image editing.
The removed weekly task/progress/planning section remains excluded. These PDFs
are local build inputs, so neither the MOVER checkout nor its services are
needed to rebuild the final presentation.

Regenerate the versioned page includes and coverage guide after intentionally
editing the manifest:

```bash
python src/slides/source/final/appendix/generate.py
```

The generator checks both snapshot hashes and complete, nonoverlapping source
coverage. The normal `python src/slides/build.py --deck final` command then
builds the main talk and appendix together, with no new Python dependencies.

This is an import of existing material, not a new evaluation. Full-test AP,
single-frame examples, n=1–20 replay-workload runtime, and the matched n=1–15
Original/Tree ablation retain their original scopes and caveats. No inference,
training, or metric calculation is rerun by the appendix build.
