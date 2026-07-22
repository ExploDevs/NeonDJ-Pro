"""
NeonDJ Pro

Application Controller
"""

from PySide6.QtWidgets import QApplication

from controller.browser_controller import BrowserController
from controller.deck_controller import DeckController

from audio.audio_engine import AudioEngine

from ui.widgets.browser.browser_widget import BrowserWidget
from ui.windows.main_window import MainWindow

from utils.logger import create_logger


class AppController:
    """
    Zentrale Anwendung.
    Verwaltet alle Controller und verbindet sie mit der Oberfläche.
    """

    def __init__(self) -> None:

        self.logger = create_logger()

        #
        # Audio
        #
        self.audio_engine = AudioEngine()

        #
        # Controller
        #
        self.browser_controller = BrowserController()

        self.deck_a_controller = DeckController(
            self.audio_engine,
            "A",
        )

        self.deck_b_controller = DeckController(
            self.audio_engine,
            "B",
        )

        #
        # Widgets
        #
        self.browser_widget = BrowserWidget(
            self.browser_controller
        )

        #
        # Main Window
        #
        self.main_window = MainWindow(
            self.browser_widget,
            self.deck_a_controller,
            self.deck_b_controller,
        )

        #
        # Decks mit ihren Widgets verbinden
        #
        self.deck_a_controller.set_widget(
            self.main_window.deck_a
        )

        self.deck_b_controller.set_widget(
            self.main_window.deck_b
        )

        #
        # Browser -> Deck A
        #
        self.browser_controller.track_selected.connect(
            self.deck_a_controller.load_track
        )

    def run(self, app: QApplication) -> int:

        self.logger.info("Qt Application erfolgreich gestartet.")

        self.main_window.show()

        return app.exec()