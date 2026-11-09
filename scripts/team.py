#!/usr/bin/env python3
"""Weist einem gestarteten inaktiven Agenten Arbeit zu und prüft den Aufgabenempfang."""
import argparse
import json
import os
import subprocess
import uuid
from pathlib import Path


def call(*args, timeout=310):
    done = subprocess.run(["herdr", *args], text=True, capture_output=True, timeout=timeout)
    if done.returncode:
        raise RuntimeError(done.stderr or done.stdout)
    return json.loads(done.stdout)["result"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get("HERDR_ENV") != "1":
        raise SystemExit("Führe den Befehl in einem von Herdr verwalteten Terminal aus")
    agent = call("agent", "get", args.target)["agent"]
    if agent["agent_status"] not in {"idle", "done"}:
        raise SystemExit("Der Agent muss vor Aufgabenbeginn inaktiv oder fertig sein")
    path = args.output.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit("Wähle einen neuen Empfangspfad; verwende keinen Pfad einer früheren Aufgabe erneut")
    task_id = uuid.uuid4().hex
    prompt = args.prompt.read_text() + (
        f"\n\nDiese task_id={task_id}\ncompletion_path={path}\n"
        'Erledige die tatsächliche Aufgabe und schreibe anschließend JSON: {"task_id":"die obige Kennung","status":"completed",'
        '"summary":"konkrete Ergebnisse und Prüfungen","artifacts":["tatsächliche Artefaktpfade"]}. '
        "Kannst du die Aufgabe nicht abschließen, verwende status=blocked und erkläre den Grund in summary. Starte keine weiteren Agenten."
    )
    settled = call("agent", "prompt", args.target, prompt, "--wait", "--timeout", "300000")
    state = settled["agent"]["agent_status"]
    if state not in {"idle", "done"} or not path.is_file():
        raise SystemExit("Der Agent hat ohne akzeptierten Empfang beendet; prüfe agent get/read")
    receipt = json.loads(path.read_text())
    if receipt.get("task_id") != task_id or receipt.get("status") != "completed" or not receipt.get("summary"):
        raise SystemExit("Der Empfang bestätigt diese Aufgabe nicht")
    for artifact in receipt.get("artifacts", []):
        candidate = Path(artifact)
        if not candidate.is_absolute():
            candidate = Path.cwd() / candidate
        if not candidate.is_file():
            raise SystemExit(f"Artefakt fehlt: {artifact}")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
