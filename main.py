"""
NeonDJ Pro

Programmstart
"""

from ui.application.application import NeonDJApplication
from controller.app_controller import AppController


def main() -> int:
    """
    Einstiegspunkt der Anwendung.
    """

    app = NeonDJApplication([])

    controller = AppController()

    controller.logger.info("Qt Application erfolgreich gestartet.")

    controller.show()


    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())