import sqlite3
from pathlib import Path

class SQLiteManager:
    def __init__(self, db_path="database.db"):
        self.db_path = Path(db_path)
        self.conn = self._connect()
        self._create_tables()

    def get_conn(self):
        # SQLite connections are not thread-safe by default
        return sqlite3.connect(str(self.db_path), check_same_thread=False)

    def _connect(self):
        if not self.db_path.parent.exists():
            self.db_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.db_path.exists():
            conn = sqlite3.connect(str(self.db_path))
            conn.close()

        return sqlite3.connect(str(self.db_path), check_same_thread=False)

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def _create_tables(self):
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS api_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key VARCHAR,
                user_id INTEGER,

                FOREIGN KEY (user_id) REFERENCES users(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            )
            """
        )

        self.conn.commit()
