"""Render the frozen Original/Tree CSV as native LaTeX; no inference runs."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rows = list(csv.DictReader((ROOT / "tree-comparison.csv").open()))
assert [int(row["n_model_inputs"]) for row in rows] == list(range(1, 16))

lines = ["% Generated from tree-comparison.csv by generate_table.py.",
         r"\long\def\TreeStudyTableRows{%"]
fields = ["original_median_ms", "tree_median_ms", "original_AP50_percent",
          "tree_AP50_percent", "original_AP70_percent", "tree_AP70_percent"]
for row in rows:
    n = int(row["n_model_inputs"])
    color = ("TreeDistinct" if n <= 5 else "TreeReplay") + ("Light" if n % 2 else "Alt")
    cells = [str(n)] + [f"{float(row[field]):.2f}" for field in fields]
    if n == 15:
        cells = [r"\textbf{" + cell + "}" for cell in cells]
    lines.append(r"\rowcolor{" + color + "}")
    lines.append(" & ".join(cells) + r" \\")
lines.append("}")
(ROOT / "table-rows.tex").write_text("\n".join(lines) + "\n")

last = rows[-1]
reduction = 100 * (1 - float(last["tree_median_ms"]) / float(last["original_median_ms"]))
values = {"TimeReduction": f"{reduction:.1f}"}
for field in fields:
    name = {"original_median_ms": "OriginalTime", "tree_median_ms": "TreeTime",
            "original_AP50_percent": "OriginalAPFifty", "tree_AP50_percent": "TreeAPFifty",
            "original_AP70_percent": "OriginalAPSeventy", "tree_AP70_percent": "TreeAPSeventy"}[field]
    values[name] = f"{float(last[field]):.2f}"
for threshold in ("50", "70"):
    delta = float(last[f"tree_AP{threshold}_percent"]) - float(last[f"original_AP{threshold}_percent"])
    label = "Fifty" if threshold == "50" else "Seventy"
    values[f"AP{label}Delta"] = f"{delta:.2f}"
(ROOT / "summary-values.tex").write_text(
    "% Generated from the n=15 row. AP changes are percentage points.\n"
    + "".join(r"\def\TreeStudy" + name + "{" + value + "}\n" for name, value in values.items())
)

edges = json.loads((ROOT / "preflight.json").read_text())["5"]["tree_undirected_edges"]
assert len(edges) == 4
(ROOT / "topology-example.tex").write_text(
    "% Saved n=5 preflight tree; logical node IDs are shown one-based.\n"
    + "".join(
        r"\draw[{Stealth[length=1.1mm]}-{Stealth[length=1.1mm]},draw=MoverCyan,"
        r"line width=1.0pt,shorten <=4pt,shorten >=4pt] "
        + f"(tree-node-{a+1}) -- (tree-node-{b+1});\n" for a, b in edges
    )
)
