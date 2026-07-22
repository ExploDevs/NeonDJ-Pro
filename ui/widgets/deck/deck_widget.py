"""
NeonDJ Pro

Deck Widget

Grafische Oberfläche eines DJ-Decks.
Kommuniziert ausschließlich über den DeckController.
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSlider,
)
from PySide6.QtCore import Qt
from PySide6.QtCore import QTimer
from ui.widgets.waveform.waveform_widget import WaveformWidget
import time
from audio.track import Track


class DeckWidget(QWidget):
    """
    Ein vollständiges DJ-Deck (UI Simulation).
    """

    def __init__(
        self, 
        deck_name: str = "Deck",
        controller=None,
        ) -> None:
            super().__init__()

            self.deck_name = deck_name
            self.controller = controller

            self.timer = QTimer()
            self.timer.setInterval(30)  # ~33 FPS UI Update
            self.timer.timeout.connect(self._update_playhead)

            self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        # ---------------- HEADER ----------------
        self.title = QLabel(self.deck_name)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(self.title)

        self.track_info = QLabel("Kein Track geladen")
        self.track_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.track_info)

        # ---------------- STATUS ----------------
        self.status = QLabel("STOPPED")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.setStyleSheet("color: #00E5FF;")
        layout.addWidget(self.status)

        # ---------------- BUTTON ROW ----------------
        btn_row = QHBoxLayout()

        self.play_btn = QPushButton("▶ Play")
        self.play_btn.clicked.connect(self.toggle_play)

        self.cue_btn = QPushButton("Cue")
        self.stop_btn = QPushButton("Stop")

        self.stop_btn.clicked.connect(self.stop)

        btn_row.addWidget(self.play_btn)
        btn_row.addWidget(self.cue_btn)
        btn_row.addWidget(self.stop_btn)

        layout.addLayout(btn_row)

        # ---------------- PITCH ----------------
        self.pitch = QSlider(Qt.Orientation.Horizontal)
        self.pitch.setMinimum(-100)
        self.pitch.setMaximum(100)
        self.pitch.setValue(0)

        layout.addWidget(QLabel("Pitch"))
        layout.addWidget(self.pitch)

        # ---------------- PLACEHOLDER WAVEFORM ----------------
        self.waveform = WaveformWidget()
        self.waveform.setMaximumHeight(120)

        layout.addWidget(self.waveform)

    # ---------------- LOGIC (UI SIMULATION) ----------------

    def toggle_play(self) -> None:
        if self.controller.playing:
            self.controller.pause()
        else:
            self.controller.play()

        if self.controller.playing:
            self.status.setText("PLAYING")
            self.status.setStyleSheet("color: #00E676;")
            self.play_btn.setText("⏸ Pause")

            # Start timing
            self.timer.start()

        else:
            self.status.setText("PAUSED")
            self.status.setStyleSheet("color: #FFC107;")
            self.play_btn.setText("▶ Play")

            self.timer.stop()

    def stop(self) -> None:
        self.controller.stop()

        self.timer.stop()

        self.waveform.set_playhead(0.0)

        self.status.setText("STOPPED")
        self.status.setStyleSheet("color: #FF5252;")

        self.play_btn.setText("▶ Play")

        self.pitch.setValue(0)

    def _update_playhead(self) -> None:
        """
        Aktualisiert die Waveform anhand der Transport-Engine.
        """

        self.waveform.set_playhead(
            self.controller.player.position
        )

    def sync_to(self, master_bpm: float) -> None:
        """
        Synchronisiert dieses Deck auf Master BPM
        """

        pass


    def load_track(self, track: Track) -> None:
        """
        Aktualisiert die Deck-Anzeige.
        """

        self.title.setText(track.title)

        self.track_info.setText(
            f"{track.artist}\n"
            f"{track.bpm:.1f} BPM"
        )