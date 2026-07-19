"""
NeonDJ Pro
Application-Klasse

Diese Klasse erweitert QApplication und verwaltet
globale Einstellungen der Anwendung.
"""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from config.constants import (
    APP_NAME,
    APP_VERSION,
    ORGANIZATION,
)


class NeonDJApplication(QApplication):
    """
    Zentrale QApplication.

    Hier landen später:
    - Theme
    - Übersetzungen
    - Splash Screen
    - Fonts
    - Ressourcen
    """

    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)

        self.setApplicationName(APP_NAME)
        self.setApplicationVersion(APP_VERSION)
        self.setOrganizationName(ORGANIZATION)

        # verhindert unnötiges Beenden bei späteren Hilfsfenstern
        self.setQuitOnLastWindowClosed(True)

    def run(self) -> int:
        """
        Startet den Qt-Eventloop.
        """
        return self.exec()