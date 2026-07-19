"""
NeonDJ Pro

Track Repository
"""

from __future__ import annotations

from database.database import Database
from audio.metadata import AudioMetadata
from audio.analyzer import AnalysisResult


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

        return cursor.fetchall()