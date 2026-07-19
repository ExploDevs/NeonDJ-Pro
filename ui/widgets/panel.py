"""
NeonDJ Pro
Basis Panel Widget
"""

from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt


class Panel(QFrame):
    """
    Wiederverwendbares UI-Panel mit Grundstyling.
    """

    def __init__(self, title: str = "") -> None:
        super().__init__()

        self.title = title

        self._setup()

    def _setup(self) -> None:
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            QFrame {
                background-color: #1E1E22;
                border: 1px solid #2A2A30;
                border-radius: 10px;
            }
        """)