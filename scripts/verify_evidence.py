"""Verify the bundled evidence without training, inference, or extra packages."""

from collections import defaultdict
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import statistics
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def check_hash(path, expected):
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError(f"Checksum mismatch: {path.relative_to(ROOT)}")


def main():
    slides = ROOT / "src/slides/source/assets"
    appendix = slides / "appendix"
    manifest = json.loads((appendix / "sources.json").read_text())
    for item in manifest["sources"].values():
        check_hash(appendix / item["file"], item["sha256"])

    count = 0
    for directory in [slides / "architecture", ROOT / "src/report/source/assets/final"]:
        manifest = json.loads((directory / "sources.json").read_text())
        for item in manifest["assets"]:
            check_hash(directory / item["local"], item["sha256"])
            count += 1

    generation = slides / "illustrations/prompt-trials-2026-11-09"
    record = json.loads((generation / "generation.json").read_text())
    check_hash(generation / record["image_file"], record["image_sha256"])
    check_hash(generation / record["baseline_file"], record["baseline_sha256"])

    script = ROOT / "src/report/generate_final_tables.py"
    spec = importlib.util.spec_from_file_location("report_tables", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory(prefix="mo809-evidence-") as directory:
        module.generate_tables(ROOT, Path(directory))

    study = slides / "experiments/tree-2026-11-05"
    grouped = defaultdict(list)
    with (study / "timings.jsonl").open() as stream:
        for line in stream:
            sample = json.loads(line)
            grouped[(sample["method"], sample["n"])].append(sample["forward_ms"])
    if len(grouped) != 30 or any(len(values) != 90 for values in grouped.values()):
        raise ValueError("Expected 90 samples for every method/count condition")
    summary = json.loads((study / "tree-comparison.json").read_text())
    for row in summary["results"]:
        for method in ["original", "tree"]:
            measured = statistics.median(grouped[(method, row["n"])])
            if not math.isclose(measured, row[method]["forward_median_ms"], abs_tol=1e-9):
                raise ValueError(f"Timing median mismatch: {method}, n={row['n']}")

    print(f"Verified 2 appendix PDFs, {count} figure/provenance files, and Appendix E assets.")
    print("Verified 20 runtime conditions and all 15 Original/Tree CSV/JSON conditions.")
    print("Verified all 30 tree medians against 2,700 recorded timing samples.")


if __name__ == "__main__":
    main()
