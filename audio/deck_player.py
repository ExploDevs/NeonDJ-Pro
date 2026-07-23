"""
NeonDJ Pro

DeckPlayer

Verwaltet die Wiedergabe eines Decks.
"""

from __future__ import annotations

import numpy as np

from pathlib import Path
import soundfile as sf

class DeckPlayer:

    def __init__(self) -> None:

        self.samples: np.ndarray | None = None

        self.sample_rate = 44100

        self.position = 0.0

        self.playing = False

        self.gain = 1.0

        self.pitch = 1.0

    def load(
        self,
        file_path: str | Path,
    ) -> None:
        """
        Lädt einen Track in den Player.
        """

        self.samples, self.sample_rate = sf.read(
            file_path,
            dtype='float32',
            always_2d=True,
        )

        print(f"Loaded {file_path}")
        print(f"Sample rate: {self.sample_rate}")

        self.position = 0

    def play(self) -> None:
        self.playing = True

    def pause(self) -> None:
        self.playing = False

    def stop(self) -> None:
        self.playing = False
        self.position = 0

    def next_frames(
        self,
        frames: int,
    ) -> np.ndarray:
        """
        Liefert die nächsten Audioblöcke.
        """

        if (
            not self.playing
            or self.samples is None
        ):
            return np.zeros((frames, 2), dtype=np.float32)
        
        indices = (
            self.position
            + np.arange(frames) * self.pitch
        )

        indices = indices.astype(np.int64)


        if indices[-1] >= len(self.samples):

            result = np.zeros((frames, 2), dtype=np.float32)

            valid = indices < len(self.samples)

            result[valid] = self.samples[indices[valid]]

            self.stop()

            return result
        
        chunk = self.samples[indices]

        self.position += frames * self.pitch

        return chunk
    
    @property
    def length(self) -> int:
        """
        Gesamte Anzahl der Samples
        """
        if self.samples is None:
            return 0
        
        return len(self.samples)
    
    @property
    def progress(self) -> float:
        """
        Wiedergabefortschritt zwischen 0.0 und 1.0
        """

        if self.length == 0:
            return 0.0
        
        return self.position / self.length
    
    @property
    def current_time(self) -> float:
        """
        Aktuelle Wiedergabe in Sekunden
        """
        return self.position / self.sample_rate
    
    @property
    def duration(self) -> float:
        """
        Gesamtdauer des Tracks in Sekunden
        """
        if self.samples is None:
            return 0.0
        
        return len(self.samples) / self.sample_rate
    
    def set_pitch(self, pitch: float) -> None:
        """
        Setzt den Pitch-Faktor.
        1.0 = Originalgeschwindigkeit
        """

        self.pitch = pitch

    def get_pitch(self) -> float:
        return self.pitch