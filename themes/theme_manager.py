"""
Theme Manager
"""

from themes import colors


class ThemeManager:

    def stylesheet(self):

        return f"""

        QWidget {{

            background:{colors.BACKGROUND};

            color:{colors.TEXT};

            font-size:10pt;

        }}

        QPushButton {{

            background:{colors.PURPLE};

            border:none;

            border-radius:12px;

            padding:8px;

            color:white;

        }}

        QPushButton:hover {{

            background:{colors.BLUE};

        }}

        """