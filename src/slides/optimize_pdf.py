"""Losslessly share identical PDF streams after importing many source pages.

Requires qpdf. Images, fonts and vector content keep their original encoded
bytes; this does not downsample or re-encode figures. Only object references
whose complete stream dictionaries and data match are shared.
"""

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile


def deduplicate_pdf(source, destination):
    source, destination = Path(source), Path(destination)
    with tempfile.TemporaryDirectory(dir=destination.parent,
                                     prefix="pdf-resources-") as directory:
        serialized = Path(directory) / "objects.json"
        with (destination.parent / "qpdf.log").open("w") as log:
            subprocess.run([
                "qpdf", "--warning-exit-0", "--json-output=2",
                "--json-stream-data=inline", "--decode-level=none",
                str(source), str(serialized),
            ], stderr=log, check=True)
            with serialized.open() as handle:
                document = json.load(handle)
            objects = document["qpdf"][1]
            streams = {
                key: hashlib.sha256(value["stream"]["data"].encode()).digest()
                for key, value in objects.items()
                if "stream" in value and "data" in value["stream"]
            }
            shared = 0
            while True:
                known, replacements = {}, {}
                for key, digest in streams.items():
                    signature = (digest, json.dumps(
                        objects[key]["stream"]["dict"], sort_keys=True))
                    reference = key.removeprefix("obj:")
                    if signature in known:
                        replacements[reference] = known[signature]
                    else:
                        known[signature] = reference
                if not replacements:
                    break

                def rewrite(value):
                    if isinstance(value, str):
                        return replacements.get(value, value)
                    if isinstance(value, list):
                        return [rewrite(item) for item in value]
                    if isinstance(value, dict):
                        # Stream payloads are base64, never PDF references.
                        return {key: item if key == "data" else rewrite(item)
                                for key, item in value.items()}
                    return value

                for reference in replacements:
                    key = "obj:" + reference
                    del objects[key]
                    del streams[key]
                for key, value in objects.items():
                    objects[key] = rewrite(value)
                shared += len(replacements)
            with serialized.open("w") as handle:
                json.dump(document, handle)
            subprocess.run([
                "qpdf", "--json-input", "--object-streams=generate",
                str(serialized), str(destination),
            ], stderr=log, check=True)
    print(f"Shared {shared} identical PDF streams without re-encoding figures.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    arguments = parser.parse_args()
    deduplicate_pdf(arguments.source, arguments.destination)
