"""
NeonDJ Pro

BeatClock

Verwaltet die musikalische Zeitbasis eines Decks.
"""

from __future__ import annotations

import time

class BeatClock:
    """
    Berechnet Beat- und Wiedergabeposition anhand der BPM
    """

    def __init__(self, bpm: float = 128.0) -> None:

        self._bpm = bpm

        self._running = False

        self._start_time = 0.0

        self._pause_offset = 0.0

    @property
    def bpm(self) -> float:
        return self._bpm
    
    @bpm.setter
    def bpm(self, value: float) -> None:

        self._bpm = max(20.0, min(400.0, value))

    def play(self) -> None:

        if self._running:
            return
        
        self._start_time = time.perf_counter() - self._pause_offset

        self._running = True

    def pause(self) -> None:

        if not self._running:
            return
        
        self._pause_offset = time.perf_counter() - self._start_time

        self._running = False

    def stop(self) -> None:

        self._running = False

        self._pause_offset = 0.0

        self._start_time = 0.0

    @property
    def elapsed_seconds(self) -> float:

        if self._running:
            return time.perf_counter() - self._start_time
        
        return self._pause_offset
    
    @property
    def current_beat(self) -> float:

        return self.elapsed_seconds * (self._bpm / 60.0)
    
    @property
    def playhead(self) -> float:
        """
        0.0 - 1.0
        """

        return (self.current_beat % 32.0) / 32.0
    
    @property
    def running(self) -> bool:
        return self._running
        