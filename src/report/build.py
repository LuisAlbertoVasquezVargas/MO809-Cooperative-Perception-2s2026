"""Build the original proposal or the final report using shared metadata."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tomllib

from generate_final_tables import generate_tables


def latex_escape(value):
    replacements = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
                    "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{",
                    "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(replacements.get(char, char) for char in value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--document", choices=("proposal", "final"), default="proposal")
    args = parser.parse_args()
    project = Path(__file__).resolve().parent
    root = project.parents[1]
    if not shutil.which("latexmk"):
        raise SystemExit("Install latexmk and a LaTeX distribution before building.")
    config = tomllib.loads((root / "config/project.toml").read_text())
    metadata = config["project"]
    build = project / "output/.build"
    if args.document == "final":
        build /= "final"
    build.mkdir(parents=True, exist_ok=True)
    fields = {"ProjectTitle": metadata["title"], "ProjectCourse": metadata["course"],
              "ProjectAuthor": metadata["author"] or "Author to be confirmed"}
    if args.document == "final":
        fields["FinalPresentationDate"] = config["deadlines"]["presentation"]
        generate_tables(root, build)
    (build / "metadata.generated.tex").write_text("".join(
        "\\newcommand{\\" + key + "}{" + latex_escape(value) + "}\n"
        for key, value in fields.items()))
    environment = os.environ.copy()
    environment["TEXINPUTS"] = str(build) + os.pathsep + environment.get("TEXINPUTS", "")
    environment["TEXMFVAR"] = str(build / "texmf-var")
    environment["BIBINPUTS"] = os.pathsep.join([
        str(project / "source"), str(root / "references"), environment.get("BIBINPUTS", "")])
    entrypoint = "final.tex" if args.document == "final" else "main.tex"
    subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                    "-outdir=" + str(build), entrypoint],
                   cwd=project / "source", env=environment, check=True)
    output = project / "output" / ("final-report.pdf" if args.document == "final" else "report.pdf")
    built_pdf = build / Path(entrypoint).with_suffix(".pdf")
    if args.document == "final" and shutil.which("qpdf"):
        # Normalize imported PDF dictionaries, including repeated page-group
        # entries from figure exports, while preserving encoded figure streams.
        normalized = build / "final.normalized.pdf"
        subprocess.run(["qpdf", "--warning-exit-0", "--compress-streams=y",
                        "--decode-level=none",
                        "--object-streams=generate", str(built_pdf), str(normalized)],
                       check=True)
        shutil.copy2(normalized, output)
    else:
        shutil.copy2(built_pdf, output)
    print(output)


if __name__ == "__main__":
    main()
