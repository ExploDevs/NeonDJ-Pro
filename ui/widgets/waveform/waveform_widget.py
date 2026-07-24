"""
NeonDJ Pro
Waveform Widget (UI Layer)

Visuelle Darstellung einer DJ-Waveform.
Später gekoppelt mit Audioanalyse.
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QRectF

from audio.waveform import WaveformGenerator


class WaveformWidget(QWidget):
    """
    Zeichnet eine simulierte Waveform.
    (Phase 1: Dummy-Daten, später echte Audio-Daten)
    """

    def __init__(self) -> None:
        super().__init__()

        self.setMinimumHeight(120)
        self.setAttribute(Qt.WidgetAttribute.WA_OpaquePaintEvent)

        # waveform data (später Audio FFT)
        self.generator = WaveformGenerator()

        self.samples = []

        self.playhead = 0.3  # 0.0 - 1.0 (Position im Track)

    # ----------------------------
    # DATA
    # ----------------------------

    def _generate_dummy_waveform(self) -> list[float]:
        """
        Erstellt künstliche Waveform-Daten.
        Später ersetzt durch librosa FFT Analyse.
        """
        import random

        return [random.uniform(0.1, 1.0) for _ in range(200)]

    # ----------------------------
    # PAINT EVENT
    # ----------------------------

    def paintEvent(self, event) -> None:
        painter = QPainter(self)

        rect = self.rect()

        # Background
        painter.fillRect(rect, QColor("#1E1E22"))

        # Waveform color
        pen = QPen(QColor("#00E5FF"))
        pen.setWidth(2)
        painter.setPen(pen)

        width = rect.width()
        height = rect.height()

        mid_y = height / 2

        if len(self.samples) == 0:
            return

        step = width / len(self.samples)

        # Draw waveform bars
        for i, value in enumerate(self.samples):

            x = i * step

            bar_height = value * (height / 2)

            painter.drawLine(
                int(x),
                int(mid_y - bar_height),
                int(x),
                int(mid_y + bar_height),
            )

        # Playhead line
        play_x = width * self.playhead

        play_pen = QPen(QColor("#FF5252"))
        play_pen.setWidth(2)
        painter.setPen(play_pen)

        painter.drawLine(
            int(play_x),
            0,
            int(play_x),
            height
        )

    # ----------------------------
    # PUBLIC API
    # ----------------------------

    def set_playhead(self, position: float) -> None:
        """
        Setzt Abspielposition (0.0 - 1.0)
        """
        self.playhead = max(0.0, min(1.0, position))
        self.update()

    def set_audio(self, samples) -> None:
        """
        Erzeugt aus Audiodateien eine Waveform.
        """

        self.samples = self.generator.generate(
            samples,
            width=500,
        )

        self.update()