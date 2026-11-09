# Herdr-Begleitpaket für Lesende

Ressourcenversion: 1.0.0

Dieses öffentliche Begleitpaket enthält ausführbare Beispiele, Tests, Rollenprompts und kurze Anleitungen zu *Zuverlässige Multi-Agenten-Workflows mit Herdr*. Der kostenpflichtige Buchtext ist nicht enthalten.

## Installieren und testen

Verwende Python 3.12 im Stammverzeichnis des Repositorys:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
```

Erwartetes Ergebnis: 42 Tests bestanden. Das Projekt begleitet die Beispiele des Buchs; eine pauschale Open-Source-Lizenz wird nicht erteilt.

Passende Release für Buchausgabe 1.0: [v1.0.0](https://github.com/t945935/herdr-multi-agent-reader-de/releases/tag/v1.0.0). Lade [herdr-multi-agent-reader-de.zip](https://github.com/t945935/herdr-multi-agent-reader-de/releases/download/v1.0.0/herdr-multi-agent-reader-de.zip) und [SHA256SUMS.txt](https://github.com/t945935/herdr-multi-agent-reader-de/releases/download/v1.0.0/SHA256SUMS.txt) herunter. Fehler meldest du unter [GitHub Issues](https://github.com/t945935/herdr-multi-agent-reader-de/issues).

Die Kapitelzuordnung, den Website-Start und Übungshinweise findest du in [`examples/README.md`](examples/README.md), die Releasehistorie in [`CHANGELOG.md`](CHANGELOG.md).
