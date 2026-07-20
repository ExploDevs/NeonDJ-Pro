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

from controller.browser_controller import BrowserController

from .track_table import TrackTable

class BrowserWidget(QWidget):

    def __init__(self, controller: BrowserController):
        super().__init__()

        self.controller = controller

        self.table = TrackTable()
        self.table.itemDoubleClicked.connect(
            self._track_double_clicked
        )

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

        tracks = self.controller.get_tracks()

        self.table.load_tracks(tracks)

    def filter_tracks(self, text: str) -> None:

        text = text.strip()

        if not text:

            self.reload()
            return
        
        tracks = self.controller.search(text)

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

            self.controller.import_track(file_name)

            self.reload()

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Importfehler",
                str(exc),
            )

    def _track_double_clicked(self) -> None:
        """
        Wird bei Doppelklick aufgerufen.
        """

        track = self.table.current_track()

        if track is None:
            return
        
        print(track.title)
        
        self.controller.track_selected.emit(track)