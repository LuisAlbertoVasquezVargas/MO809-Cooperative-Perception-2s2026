"""Build the proposal or final presentation using shared project metadata."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tomllib

from optimize_pdf import deduplicate_pdf


def latex_escape(value):
    replacements = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
                    "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{",
                    "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(replacements.get(char, char) for char in value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deck", choices=("proposal", "final"), default="proposal")
    args = parser.parse_args()
    project = Path(__file__).resolve().parent
    root = project.parents[1]
    engine = "pdflatex" if args.deck == "final" else "xelatex"
    if not shutil.which("latexmk") or not shutil.which(engine):
        raise SystemExit(f"Install latexmk and {engine} before building the {args.deck} slides.")
    config = tomllib.loads((root / "config/project.toml").read_text())
    metadata = config["project"]
    build = project / "output/.build"
    if args.deck == "final":
        build /= "final"
    build.mkdir(parents=True, exist_ok=True)
    fields = {"ProjectTitle": metadata["title"], "ProjectCourse": metadata["course"],
              "ProjectAuthor": metadata["author"] or "Author to be confirmed"}
    if args.deck == "final":
        fields["FinalPresentationDate"] = config["deadlines"]["presentation"] or "Date to Be Confirmed"
    (build / "metadata.generated.tex").write_text("".join(
        "\\newcommand{\\" + key + "}{" + latex_escape(value) + "}\n"
        for key, value in fields.items()))
    environment = os.environ.copy()
    environment["TEXMFVAR"] = str(build / "texmf-var")
    environment["TEXINPUTS"] = str(build) + os.pathsep + environment.get("TEXINPUTS", "")
    environment["TEXFORMATS"] = str(build) + os.pathsep + environment.get("TEXFORMATS", "")
    # Some minimal TeX installations include XeTeX without a prepared format.
    # Generate it locally when needed, without changing the system installation.
    if args.deck == "proposal":
        format_lookup = subprocess.run(["kpsewhich", "xelatex.fmt"], env=environment,
                                       capture_output=True, check=False)
        if format_lookup.returncode != 0:
            subprocess.run(["xelatex", "-ini", "-etex", "-jobname=xelatex",
                            "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory=" + str(build), "xelatex.ini"],
                           cwd=project / "source", env=environment, check=True)
    entrypoint = "final.tex" if args.deck == "final" else "main.tex"
    option = "-pdf" if args.deck == "final" else "-xelatex"
    subprocess.run(["latexmk", option, "-interaction=nonstopmode", "-halt-on-error",
                    "-outdir=" + str(build), entrypoint],
                   cwd=project / "source", env=environment, check=True)
    output = project / "output" / ("final.pdf" if args.deck == "final" else "slides.pdf")
    built_pdf = build / Path(entrypoint).with_suffix(".pdf")
    if args.deck == "final" and shutil.which("qpdf"):
        optimized = build / "final.optimized.pdf"
        deduplicate_pdf(built_pdf, optimized)
        shutil.copy2(optimized, output)
    else:
        shutil.copy2(built_pdf, output)
    print(output)


if __name__ == "__main__":
    main()
