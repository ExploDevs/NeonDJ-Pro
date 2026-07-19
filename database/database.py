"""
NeonDJ Pro

SQLite Datenbankverwaltung
"""

from __future__ import annotations

import sqlite3
from pathlib import Path


class Database:

    def __init__(self) -> None:

        Path("database").mkdir(exist_ok=True)

        self.connection = sqlite3.connect(
            "database/library.db"
        )

        self.connection.row_factory = sqlite3.Row

        self._create_tables()

    def _create_tables(self) -> None:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tracks
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                path TEXT UNIQUE,

                title TEXT,
                artist TEXT,
                album TEXT,

                duration REAL,

                bpm REAL,

                musical_key TEXT,

                sample_rate INTEGER,

                channels INTEGER,

                play_count INTEGER DEFAULT 0,

                rating INTEGER DEFAULT 0,

                last_played TEXT
            );
            """
        )

        self.connection.commit()

    def close(self) -> None:
        self.connection.close()