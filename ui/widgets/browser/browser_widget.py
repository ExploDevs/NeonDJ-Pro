"""
NeonDJ Pro

Browser Widget
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
)

from database.database import Database
from database.track_repository import TrackRepository

from .track_table import TrackTable

from audio.audio_loader import AudioLoader
from audio.analyzer import AudioAnalyzer

class BrowserWidget(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.database = Database()
        self.repository = TrackRepository(
            self.database
        )

        self.loader = AudioLoader()
        self.analyzer = AudioAnalyzer()

        self.table = TrackTable()

        self.search = QLineEdit()
        self.search.textChanged.connect(
            self.filter_tracks
        )
        self.search.setPlaceholderText(
            "Titel oder Artist suchen..."
        )

        self.import_button = QPushButton("➕ Musik importieren")
        self.import_button.clicked.connect(self.import_track)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Bibliothek"))
        layout.addWidget(self.search)
        layout.addWidget(self.import_button)
        layout.addWidget(self.table)

        self.reload()

    def reload(self):

        tracks = self.repository.get_all_tracks()

        self.table.load_tracks(tracks)

    def filter_tracks(self, text: str) -> None:

        text = text.strip()

        if not text:

            self.reload()
            return
        
        tracks = self.repository.search_tracks(text)

        self.table.load_tracks(tracks)

    def import_track(self) -> None:

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Musik auswählen",
            "",
            "Audio (*.mp3 *.wav *.flac *.ogg *.aac *.aiff)"
        )

        if not file_name:
            return
        try:

            metadata = self.loader.load_metadata(file_name)

            analysis = self.analyzer.analyze(file_name)

            self.repository.add_track(
                metadata,
                analysis,
            )

            self.reload()

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Importfehler",
                str(exc),
            )