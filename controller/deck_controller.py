"""
NeonDJ Pro

DeckController

Verbindet UI und Audio-Engine.
"""

from audio.transport import DeckTransport
from audio.track import Track


class DeckController:

    def __init__(self) -> None:
        self.transport = DeckTransport()
        self.track: Track | None = None

        self.widget = None

    def play_pause(self) -> None:
        if self.transport.playing:
            self.transport.pause()
        else:
            self.transport.play()

    def stop(self) -> None:
        self.transport.stop()

    @property
    def playing(self) -> bool:
        return self.transport.playing

    @property
    def playhead(self) -> float:
        return self.transport.playhead

    @property
    def bpm(self) -> float:
        return self.transport.bpm

    @bpm.setter
    def bpm(self, value: float) -> None:
        self.transport.bpm = value

    def set_widget(self, widget) -> None:
        """
        Verbindet den Controller mit seinem DeckWidget
        """

        self.widget = widget

    def load_track(self, track: Track) -> None:
        """
        Lädt einen Track in dieses Deck.
        """

        self.track = track

        if self.widget is not None:
            self.widget.load_track(track)