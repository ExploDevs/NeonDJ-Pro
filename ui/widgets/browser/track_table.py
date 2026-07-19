"""
NeonDJ Pro

Track Table
"""

from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
)

from PySide6.QtCore import Qt


class TrackTable(QTableWidget):

    def __init__(self) -> None:
        super().__init__()

        self.setColumnCount(5)

        self.setHorizontalHeaderLabels(
            [
                "Titel",
                "Artist",
                "Album",
                "BPM",
                "Dauer",
            ]
        )

        self.setSortingEnabled(True)

        self.setAlternatingRowColors(True)

        self.verticalHeader().hide()

        self.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.horizontalHeader().setStretchLastSection(True)

    def load_tracks(self, tracks) -> None:

        self.setRowCount(len(tracks))

        for row, track in enumerate(tracks):

            self.setItem(
                row,
                0,
                QTableWidgetItem(track["title"] or "")
            )

            self.setItem(
                row,
                1,
                QTableWidgetItem(track["artist"] or "")
            )

            self.setItem(
                row,
                2,
                QTableWidgetItem(track["album"] or "")
            )

            bpm = ""

            if track["bpm"]:
                bpm = f"{track['bpm']:.1f}"

            self.setItem(
                row,
                3,
                QTableWidgetItem(bpm)
            )

            duration = ""

            if track["duration"]:

                minutes = int(track["duration"] // 60)
                seconds = int(track["duration"] % 60)

                duration = f"{minutes}:{seconds:02}"

            self.setItem(
                row,
                4,
                QTableWidgetItem(duration)
            )