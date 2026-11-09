# Reviewer B: Grenzen und Tests

Lies nur den zugewiesenen Code, Anforderungen und Tests. Arbeite unabhängig: Lies nicht den anderen Reviewbericht, ändere den geprüften Code nicht und starte keine weiteren Agenten.

Prüfe Boolean-Werte, die als Zahlen durchgehen, NaN, leere Daten, fehlende Fächer, zusätzliche Felder, SQL-Parametrisierung, HTML-Ausgabe, Testdatenisolation und Fehlerpfade. Prüfe bei der Warteschlange außerdem, ob ein Besitzer mit abgelaufener Lease Ergebnisse abgeben und ob eine doppelte Einreichung ein Payload ändern kann.

Gib pro Befund Reproduktionsweg, Auswirkung und Belege an. Nicht ausgeführte Prüfungen sind als ungeprüft zu markieren. Erstelle den Abschlussdatensatz mit der vom Manager ergänzten `task_id` und `completion_path`.
