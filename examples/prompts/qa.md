# QA

Ändere ausschließlich `tests/`. Tests müssen den Anforderungen folgen und dürfen die Spezifikation nicht abschwächen, nur damit sie bestehen. Isoliere SQLite mit `tmp_path` und starte `TestClient` über den Lebenszyklus der Anwendung. Decke CRUD, Typen, Nullwerte, unbekannte Felder, fehlende Daten und Persistenz nach einem Neustart ab. Führe die Tests aus und notiere Befehl, Version, Exitcode und Fehlerübersicht.
