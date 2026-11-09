# QA: Notensystem

Lies die Schnittstelle von `examples/grades.py` und die bestehenden Bewertungsfälle in `tests/test_contracts.py`. Prüfe den Notenvertrag unabhängig. Ändere keinen Code, lösche keine Tests, lies nicht die Selbsteinschätzung des Developers und starte keine weiteren Agenten.

Du darfst ausschließlich `tests/test_grades_review.py` ergänzen oder ändern; schreibe den Bericht nach `reports/grade-qa.md`. Prüfe Fächer, Grenzen 0/100/60, Boolean/NaN/Zeichenkette, leere Daten, Namen, Gleichstand 1/1/3, ungerundete Präzision und Unveränderlichkeit der Eingabe.

Verwende pytest. Decken bestehende Tests einen Fall ausreichend ab, nenne dein Kriterium und ergänze nur wertvolle fehlende Abdeckung; dupliziere keinen identischen Test. Prüfe weder FastAPI noch SQLite oder Website-CRUD – diese Aufgabe betrifft das Notensystem.

Führe Tests aus und bewahre echten Befehl, Exitcode, Befunde und nicht ausgeführte Prüfungen auf. Verwende `task_id` und `completion_path` des Managers im Empfangsdatensatz und nenne die neu erstellten Berichts- und Testdateien unter `artifacts`.
