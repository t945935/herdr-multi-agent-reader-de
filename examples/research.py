"""Belegzuordnung prüfen und einen nachvollziehbaren Recherchebericht erzeugen."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data):
    if not isinstance(data, dict) or not data.get("question"):
        raise ValueError("Eine Forschungsfrage ist erforderlich")
    sources = data.get("sources", [])
    if not isinstance(sources, list) or not sources:
        raise ValueError("Quellen sind erforderlich")
    by_id = {}
    for source in sources:
        if not {"id", "url", "title", "accessed", "kind"} <= source.keys():
            raise ValueError("Unvollständige Quelle")
        parsed = urlparse(source["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Die Quellen-URL muss HTTP(S) verwenden")
        if source["id"] in by_id:
            raise ValueError("Quellen-ID doppelt vorhanden")
        by_id[source["id"]] = source
    claims = data.get("claims", [])
    if not claims:
        raise ValueError("Aussagen sind erforderlich")
    for claim in claims:
        if not claim.get("text") or claim.get("status") not in {"supported", "uncertain", "conflict"}:
            raise ValueError("Ungültige Aussage")
        evidence = claim.get("evidence", [])
        if claim["status"] == "supported" and not evidence:
            raise ValueError("Gestützte Aussagen benötigen Belege")
        for item in evidence:
            if item.get("source") not in by_id or not item.get("quote"):
                raise ValueError("Ein Beleg benötigt eine bekannte Quelle und ein Zitat")
    return by_id


def render(data):
    sources = validate(data)
    lines = ["# " + data["question"], "", "## Befunde und Belege", ""]
    for claim in data["claims"]:
        status_label = {"supported": "gestützt", "uncertain": "unsicher", "conflict": "widersprüchlich"}[claim["status"]]
        lines.extend([f"### {claim['text']}", "", "Status: " + status_label, ""])
        for evidence in claim.get("evidence", []):
            source = sources[evidence["source"]]
            lines.extend([f"> {evidence['quote']}", "", f"Quelle: [{source['title']}]({source['url']})", ""])
    lines.extend(["## Quellen", ""])
    for source in sources.values():
        kind = {"official": "offiziell"}.get(source["kind"], source["kind"])
        lines.append(f"- {source['id']}: [{source['title']}]({source['url']}); {kind}; abgerufen am {source['accessed']}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = render(json.loads(args.input.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report)
    print(args.output)
