"""
Hauptcontroller
"""

from config.settings import Settings
from utils.logger import create_logger
from themes.theme_manager import ThemeManager
from ui.windows.main_window import MainWindow

class AppController:

    def __init__(self):
        
        self.settings = Settings()
        self.logger = create_logger()
        self.theme = ThemeManager()

        self.main_window = MainWindow()

        self.logger.info("NeonDJ Pro gestartet")

    def show(self) -> None:
        self.main_window.show()