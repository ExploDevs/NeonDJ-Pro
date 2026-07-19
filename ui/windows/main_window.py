"""
NeonDJ Pro
Hauptfenster (DJ Layout)
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy
)

from PySide6.QtCore import Qt

from ui.widgets.panel import Panel
from config.constants import APP_NAME
from ui.widgets.deck.deck_widget import DeckWidget


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self._setup_ui()

    def _setup_ui(self) -> None:

        self.setWindowTitle(APP_NAME)
        self.resize(1600, 900)

        # Root Widget
        root = QWidget()
        self.setCentralWidget(root)

        main_layout = QVBoxLayout(root)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(8)

        # ---------------- TOP BAR ----------------
        top_bar = Panel("TopBar")
        top_bar.setFixedHeight(60)

        top_label = QLabel("NEONDJ PRO - MIX CONSOLE")
        top_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        top_bar_layout = QVBoxLayout(top_bar)
        top_bar_layout.addWidget(top_label)

        # ---------------- CENTER AREA ----------------
        center_layout = QHBoxLayout()
        center_layout.setSpacing(8)

        # Browser
        browser = Panel("Browser")
        browser.setMinimumWidth(300)

        # Deck A
        self.deck_a = DeckWidget("Deck A")
        self.deck_a.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        deck_a_label = QLabel("DECK A")
        deck_a_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        deck_a_layout = QVBoxLayout(self.deck_a)
        deck_a_layout.addWidget(deck_a_label)

        # Deck B
        self.deck_b = DeckWidget("Deck B")
        self.deck_b.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        deck_b_label = QLabel("DECK B")
        deck_b_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        deck_b_layout = QVBoxLayout(self.deck_b)
        deck_b_layout.addWidget(deck_b_label)

        center_layout.addWidget(browser)
        center_layout.addWidget(self.deck_a)
        center_layout.addWidget(self.deck_b)

        # ---------------- BOTTOM AREA ----------------
        bottom = Panel("Mixer / Playlist")
        bottom.setFixedHeight(160)

        bottom_label = QLabel("MIXER AREA")
        bottom_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bottom_layout = QVBoxLayout(bottom)
        bottom_layout.addWidget(bottom_label)

        # ---------------- ADD TO ROOT ----------------
        main_layout.addWidget(top_bar)
        main_layout.addLayout(center_layout)
        main_layout.addWidget(bottom)