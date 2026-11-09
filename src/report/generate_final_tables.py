"""Generate final-report tables directly from the versioned experiment records."""

import csv
import json
import math
from pathlib import Path


def generate_tables(root, output):
    records = Path(root) / "src/slides/source/assets/experiments"
    benchmark = records / "w45-2026-11-04"
    study = records / "tree-2026-11-05"
    full = json.loads((benchmark / "full-test-v2-no-rsu-2026-11-03.json").read_text())
    losses = json.loads((benchmark / "test-loss-v2-no-rsu-2026-11-03.json").read_text())
    runtime = list(csv.DictReader((benchmark / "runtime-workload-summary.csv").read_text().splitlines()))
    tree = list(csv.DictReader((study / "tree-comparison.csv").read_text().splitlines()))
    tree_json = json.loads((study / "tree-comparison.json").read_text())
    if [int(row["n_model_inputs"]) for row in runtime] != list(range(1, 21)):
        raise ValueError("Expected all twenty runtime conditions")
    if [int(row["n_model_inputs"]) for row in tree] != list(range(1, 16)):
        raise ValueError("Expected all fifteen Original/Tree conditions")
    if full["frames"] != 1000 or full["active_vehicle_views"] != 4000:
        raise ValueError("Full-test coverage changed")
    for row, recorded in zip(tree, tree_json["results"], strict=True):
        if int(row["n_model_inputs"]) != recorded["n"]:
            raise ValueError("Tree CSV/JSON conditions disagree")
        for method in ["original", "tree"]:
            expected = {
                f"{method}_median_ms": recorded[method]["forward_median_ms"],
                f"{method}_AP50_percent": recorded[method]["AP"]["iou_0.5"]["ap_percent"],
                f"{method}_AP70_percent": recorded[method]["AP"]["iou_0.7"]["ap_percent"],
            }
            for key, value in expected.items():
                if not math.isclose(float(row[key]), value, abs_tol=1e-9):
                    raise ValueError(f"Tree CSV/JSON mismatch: n={recorded['n']}, {key}")

    def write(name, text):
        (Path(output) / name).write_text("% Generated from versioned experiment records.\n" + text + "\n")

    own = full["metrics"]["official"]["own_scan_only"]
    cooperative = full["metrics"]["official"]["cooperative"]
    table = [r"\begin{ReportTable}{Lrr}", r"\ReportTableHead",
             r"\ReportTH{Condition} & \ReportTH{AP@0.5 (\%)} & \ReportTH{AP@0.7 (\%)} \\"]
    for label, values in [("Own scan only", own), ("Cooperative perception", cooperative)]:
        table.append(f"{label} & {values['iou_0.5']['ap_percent']:.2f} & "
                     f"{values['iou_0.7']['ap_percent']:.2f}" + r" \\")
    gain50 = cooperative["iou_0.5"]["ap_percent"] - own["iou_0.5"]["ap_percent"]
    gain70 = cooperative["iou_0.7"]["ap_percent"] - own["iou_0.7"]["ap_percent"]
    table += [r"\rowcolor{ReportTableSummary}",
              f"\\textbf{{Gain (percentage points)}} & \\textbf{{{gain50:.2f}}} & \\textbf{{{gain70:.2f}}}" + r" \\",
              r"\end{ReportTable}"]
    write("full-test-table.generated.tex", "\n".join(table))

    table = [r"\begin{ReportTable}{Lrrr}", r"\ReportTableHead",
             r"\ReportTH{Condition} & \ReportTH{Classification} & \ReportTH{Localization} & \ReportTH{Total} \\"]
    for label, key in [("Own scan only", "own_scan_only"), ("Cooperative perception", "cooperative")]:
        row = losses["mean_loss"][key]
        table.append(label + " & " + " & ".join(f"{row[k]:,.2f}" for k in
                     ["classification", "localization", "total"]) + r" \\")
    table += [r"\end{ReportTable}"]
    write("loss-table.generated.tex", "\n".join(table))

    table = [r"\begin{ReportTable}[1.10]{rRRRR}", r"\ReportTableHead",
             r"\ReportTH{$n$} & \ReportTH{Recorded inputs} & \ReportTH{Replayed inputs} & \ReportTH{Median (ms)} & \ReportTH{P95 (ms)} \\"]
    for row in runtime:
        if int(row["n_model_inputs"]) == 6:
            table.append(r"\ReportTableDivider")
        table.append(" & ".join([row["n_model_inputs"], row["distinct_recorded_vehicles"],
                                  row["replayed_input_slots"], f"{float(row['forward_median_ms']):.2f}",
                                  f"{float(row['forward_p95_ms']):.2f}"]) + r" \\")
    table += [r"\end{ReportTable}"]
    write("runtime-table.generated.tex", "\n".join(table))

    table = [r"\begin{ReportTable}[1.10]{rRRRRRR}", r"\ReportTableHead",
             r"& \multicolumn{2}{c}{\ReportTH{Median time (ms)}} & \multicolumn{2}{c}{\ReportTH{AP@0.5 (\%)}} & \multicolumn{2}{c}{\ReportTH{AP@0.7 (\%)}} \\",
             r"\ReportTableSubheadRow",
             r"\ReportSubTH{$n$} & \ReportSubTH{Original} & \ReportSubTH{Tree} & \ReportSubTH{Original} & \ReportSubTH{Tree} & \ReportSubTH{Original} & \ReportSubTH{Tree} \\"]
    keys = ["original_median_ms", "tree_median_ms", "original_AP50_percent", "tree_AP50_percent",
            "original_AP70_percent", "tree_AP70_percent"]
    for row in tree:
        if int(row["n_model_inputs"]) == 6:
            table.append(r"\ReportTableDivider")
        table.append(row["n_model_inputs"] + " & " + " & ".join(f"{float(row[k]):.2f}" for k in keys) + r" \\")
    table += [r"\end{ReportTable}"]
    write("tree-table.generated.tex", "\n".join(table))

    last = tree[-1]
    reduction = 100 * (1 - float(last["tree_median_ms"]) / float(last["original_median_ms"]))
    fields = {
        "ReportOwnAPFifty": f"{own['iou_0.5']['ap_percent']:.2f}",
        "ReportOwnAPSeventy": f"{own['iou_0.7']['ap_percent']:.2f}",
        "ReportCoopAPFifty": f"{cooperative['iou_0.5']['ap_percent']:.2f}",
        "ReportCoopAPSeventy": f"{cooperative['iou_0.7']['ap_percent']:.2f}",
        "ReportGainFifty": f"{gain50:.2f}", "ReportGainSeventy": f"{gain70:.2f}",
        "ReportTreeReduction": f"{reduction:.1f}",
        "ReportOriginalTime": f"{float(last['original_median_ms']):.2f}",
        "ReportTreeTime": f"{float(last['tree_median_ms']):.2f}",
        "ReportOriginalAPFifty": f"{float(last['original_AP50_percent']):.2f}",
        "ReportTreeAPFifty": f"{float(last['tree_AP50_percent']):.2f}",
        "ReportOriginalAPSeventy": f"{float(last['original_AP70_percent']):.2f}",
        "ReportTreeAPSeventy": f"{float(last['tree_AP70_percent']):.2f}",
        "ReportTreeDropFifty": f"{float(last['original_AP50_percent'])-float(last['tree_AP50_percent']):.2f}",
        "ReportTreeDropSeventy": f"{float(last['original_AP70_percent'])-float(last['tree_AP70_percent']):.2f}",
        "ReportRuntimeStart": f"{float(runtime[0]['forward_median_ms']):.2f}",
        "ReportRuntimeEnd": f"{float(runtime[-1]['forward_median_ms']):.2f}",
        "ReportRuntimeFactor": f"{float(runtime[-1]['forward_median_ms'])/float(runtime[0]['forward_median_ms']):.1f}",
    }
    write("metrics.generated.tex", "\n".join(
        "\\newcommand{\\" + key + "}{" + value + "}" for key, value in fields.items()))


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    output = root / "src/report/output/.build/final"
    output.mkdir(parents=True, exist_ok=True)
    generate_tables(root, output)
