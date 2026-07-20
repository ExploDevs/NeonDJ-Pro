"""
NeonDJ Pro

Track Repository
"""

from __future__ import annotations

from database.database import Database
from audio.metadata import AudioMetadata
from audio.analyzer import AnalysisResult

from pathlib import Path

from audio.track import Track


class TrackRepository:
    """
    Verwaltet alle Track-Datensätze.
    """

    def __init__(self, database: Database) -> None:
        self.database = database

    def add_track(
        self,
        metadata: AudioMetadata,
        analysis: AnalysisResult,
    ) -> None:

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO tracks
            (
                path,
                title,
                artist,
                album,
                duration,
                bpm,
                musical_key,
                sample_rate,
                channels
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(metadata.path),
                metadata.title,
                metadata.artist,
                metadata.album,
                metadata.duration,
                analysis.bpm,
                "",
                metadata.sample_rate,
                metadata.channels,
            ),
        )

        self.database.connection.commit()

    def get_all_tracks(self):

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM tracks
            ORDER BY title
            """
        )

        rows = cursor.fetchall()

        return [
            self._row_to_track(row)
            for row in rows
        ]
    
    def search_tracks(self, text: str):

        cursor = self.database.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM tracks

            WHERE

                title LIKE ?

                OR artist LIKE ?

                OR album LIKE ?

            ORDER BY title
            """,
            (
                f"%{text}%",
                f"%{text}%",
                f"%{text}%"
            )
        )

        rows = cursor.fetchall()

        return [
            self._row_to_track(row)
            for row in rows
        ]
    
    def _row_to_track(self, row) -> Track:
        """
        Wandelt einen SQLite-Datensatz in ein Track-Objekt um.
        """

        return Track(
            path=Path(row["path"]),
            title=row["title"] or "",
            artist=row["artist"] or "",
            album=row["album"] or "",
            duration=float(row["duration"] or 0.0),
            bpm=float(row["bpm"] or 0.0),
            musical_key=row["musical_key"] or "",
            sample_rate=int(row["sample_rate"] or 44100),
            channels=int(row["channels"] or 2),
        )