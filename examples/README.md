# Ausführbares Reader-Paket

Führe alle Befehle im Stammverzeichnis des entpackten Projekts aus. Importiere Module über `examples.*`.

Prompts für das Notensystem sind `prompts/grades-developer.md` und `prompts/grades-qa.md`; `prompts/qa.md` ist ausschließlich für die Website bestimmt. Weise Aufgaben in einer eigenen Übungskopie zu, damit die Referenzversion erhalten bleibt.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python -m examples.pipeline
```

| Kapitel | Einstiegspunkt | Schwerpunkt der Abnahme |
| --- | --- | --- |
| 1 | `calculator.py` | Rechnen, Division durch null, Typen |
| 2 | `grades.py` | Notengrenzen, fehlende Fächer, Ranggleichheit |
| 3 | `../scripts/probe_herdr.py --live` | Shell-Pane starten, lesen, abwarten und aufräumen |
| 4 | `../scripts/team.py` | Gestufte Zuweisungen, eindeutige Aufgaben-IDs, Artefaktabnahme |
| 5 | `prompts/reviewer-a.md`, `reviewer-b.md` | Unabhängige Reviews und Managerentscheidung |
| 6 | `handoff.py` | Dateivorhandensein, Projektumfang, SHA-256 |
| 7 | `task_manager/` | CRUD, Validierung, statische Seiten, Persistenz nach Neustart |
| 8 | `research.py` | Aussagen, Quellen, Zitate, Unsicherheit |
| 9 | `pipeline.py` | Exitcodes, Timeouts, Abnahme und Abbruch bei Fehler |
| 10 | `queue.py` | Deduplizierung, Leases, Wiederaufnahme, Dead Letters, Nebenläufigkeit |

Website starten:

```bash
.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000
```

Öffne unter WSL `http://localhost:8000/` in einem Windows-Browser. Beispieldaten liegen standardmäßig in `examples/data/tasks.db`; automatisierte Tests verwenden ein temporäres Verzeichnis und greifen nicht darauf zu.

Die Hintergrundwarteschlange ist ein begrenztes Beispiel mit reiner Berechnung und ruft kein kostenpflichtiges Modell auf. Tatsächliche Modellzuweisungen sind ausdrücklich in `scripts/team.py` implementiert; installiere und melde dich vorher an der passenden CLI an.
