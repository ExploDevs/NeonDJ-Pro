"""
NeonDJ Pro
Application Entry Point
"""

import sys

from PySide6.QtWidgets import QApplication

from controller.app_controller import AppController


def main() -> int:

    app = QApplication(sys.argv)

    controller = AppController()

    return controller.run(app)


if __name__ == "__main__":
    raise SystemExit(main())