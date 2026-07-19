"""
NeonDJ Pro

DeckTransport

Steuert den Wiedergabestatus eines Decks.
"""

from __future__ import annotations

from audio.clock import BeatClock

class DeckTransport:
    """
    Verwaltet den Wiedergabestatus eines Decks
    """

    def __init__(self) -> None:
        
        self.clock = BeatClock()

    @property
    def bpm(self) -> float:
        return self.clock.bpm
    
    @bpm.setter
    def bpm(self, value: float) -> None:
        self.clock.bpm = value

    @property
    def playhead(self) -> float:
        return self.clock.playhead
    
    @property
    def current_beat(self) -> float:
        return self.clock.current_beat
    
    @property
    def playing(self) -> bool:
        return self.clock.running
    
    def play(self) -> None:
        self.clock.play()

    def pause(self) -> None:
        self.clock.pause()
    
    def stop(self) -> None:
        self.clock.stop()