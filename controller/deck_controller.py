"""
NeonDJ Pro

DeckController

Verbindet UI und Audio-Engine.
"""

from audio.transport import DeckTransport


class DeckController:

    def __init__(self) -> None:
        self.transport = DeckTransport()

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