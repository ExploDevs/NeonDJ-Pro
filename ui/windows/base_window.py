"""
NeonDJ Pro

Basisklasse für alle Fenster der Anwendung.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QStatusBar

from config.constants import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)


class BaseWindow(QMainWindow):
    """
    Gemeinsame Basisklasse aller Fenster.
    """

    def __init__(self) -> None:
        super().__init__()

        self._setup_window()
        self._create_statusbar()

    def _setup_window(self) -> None:
        """Grundkonfiguration des Fensters."""

        self.setWindowTitle(APP_NAME)

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setMinimumSize(1280, 720)

        self._center()

    def _create_statusbar(self) -> None:
        """Erstellt die Statusleiste."""

        status = QStatusBar(self)

        status.showMessage("Bereit")

        self.setStatusBar(status)

    def _center(self) -> None:
        """Fenster auf dem Hauptbildschirm zentrieren."""

        screen = QGuiApplication.primaryScreen()

        if screen is None:
            return

        geometry = screen.availableGeometry()

        frame = self.frameGeometry()

        frame.moveCenter(geometry.center())

        self.move(frame.topLeft())