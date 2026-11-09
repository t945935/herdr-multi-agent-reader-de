# Backend

Ändere ausschließlich `examples/task_manager/main.py`. Initialisiere Tabellen über FastAPIs Lifespan; unbekannte Felder und implizite Typumwandlungen müssen abgelehnt werden. Erfolgreiches POST: 201; PATCH: 200; DELETE: 204; fehlender Datensatz: 404; ungültige Eingabe: 422. Ausgelassene PATCH-Felder behalten ihre Werte; explizites `null` wird abgelehnt; die Beschreibung darf geleert werden. Ändere keine Dateien der Rolle Database.
