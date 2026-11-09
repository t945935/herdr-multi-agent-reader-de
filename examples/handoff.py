"""Prüft einen expliziten Übergabedatensatz statt einer Textbehauptung des Agenten."""

import argparse
import hashlib
import json
from pathlib import Path


def validate(record, root):
    required = {"task_id", "from", "to", "completed", "next", "artifacts"}
    if not isinstance(record, dict) or not required <= record.keys():
        raise ValueError("Pflichtfelder der Übergabe fehlen")
    if any(not isinstance(record[key], str) or not record[key].strip()
           for key in ["task_id", "from", "to", "completed", "next"]):
        raise ValueError("Textfelder der Übergabe dürfen nicht leer sein")
    if not isinstance(record["artifacts"], list) or not record["artifacts"]:
        raise ValueError("Die Übergabe muss Artefakte enthalten")
    root = Path(root).resolve()
    for artifact in record["artifacts"]:
        if not isinstance(artifact, dict) or set(artifact) != {"path", "sha256"}:
            raise ValueError("Ein Artefakt benötigt Pfad und sha256")
        path = (root / artifact["path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("Der Artefaktpfad muss auf eine Datei im Projekt verweisen")
        if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
            raise ValueError("Der Artefakt-Hash stimmt nicht überein")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(json.loads(args.record.read_text()), args.root)
    print("Übergabe angenommen")
