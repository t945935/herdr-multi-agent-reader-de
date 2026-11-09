# Developer: Notenvertrag

Lies zuerst die Bewertungsfälle in `examples/grades.py` und `tests/test_contracts.py`. Ändere ausschließlich `examples/grades.py`; ändere keine bestehenden Tests oder Website-Dateien und starte keine weiteren Agenten.

Vertrag: exakt drei Fächer – Deutsch, Geschichte und Mathematik. Noten sind endliche `int`-/`float`-Werte; weise Boolean-Werte, Zeichenketten, fehlende oder zusätzliche Fächer und Werte außerhalb von 0–100 zurück. Ein Durchschnitt von 60 gilt in diesem Programmbeispiel als bestanden. Eine leere Schülerliste ergibt eine leere Liste. Sortiere nach ungerundeter Gesamtpunktzahl mit Wettbewerbsrangfolge und behalte bei Gleichstand die Eingabereihenfolge bei; ändere die Eingabe nicht.

Behalte die Schnittstellen `calculate_total`, `calculate_average`, `get_grade` und `rank_students` bei. Prüfe den Vertrag und korrigiere nur, wenn nötig. Ist er bereits erfüllt, bewahre die Implementierung und berichte deine Prüfungen, statt nur für einen Diff umzuschreiben.

Führe `.venv/bin/python -m pytest -q tests/test_contracts.py -k 'ranking or scores'` aus. Dokumentiere tatsächlichen Befehl, Exitcode, geänderte Dateien und ungelöste Punkte in `reports/grade-developer.md`. Verwende die vom Manager ergänzten Werte `task_id` und `completion_path` für den Abschlussdatensatz.
