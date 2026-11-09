# Database

Ändere ausschließlich `examples/task_manager/db.py`. Stelle `init_db`, `get_tasks`, `get_task`, `create_task`, `update_task` und `delete_task` bereit. Tests dürfen `DB_PATH` ersetzen; schließe Verbindungen stets und verwende für Schreibvorgänge Transaktionen sowie parametrisierte SQL-Werte. Dynamische Spaltennamen dürfen nur aus einer festen Positivliste stammen. Gib für fehlende Datensätze `None`/`False` zurück; verschleiere Datenbankausnahmen nicht als leere Liste.
