"""
NeonDJ Pro

Browser Controller
"""

from __future__ import annotations

from pathlib import Path

from audio.audio_loader import AudioLoader
from audio.analyzer import AudioAnalyzer
from audio.track import Track

from database.database import Database
from database.track_repository import TrackRepository
from PySide6.QtCore import QObject, Signal

class BrowserController(QObject):

    track_selected = Signal(Track)

    def __init__(self) -> None:

        super().__init__()

        self.database = Database()

        self.repository = TrackRepository(
            self.database
        )

        self.loader = AudioLoader()

        self.analyzer = AudioAnalyzer()

    def import_track(
            self,
            file_path: str | Path,
    ) -> None:
        
        metadata = self.loader.load_metadata(
            file_path
        )

        analysis = self.analyzer.analyze(
            file_path
        )

        self.repository.add_track(
            metadata,
            analysis,
        )

    def get_tracks(self):

        return self.repository.get_all_tracks()
    
    def search(self, text: str):

        return self.repository.search_tracks(text)