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

        self.position = 0

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
        
        end = self.position + frames

        chunk = self.samples[self.position:end]

        if len(chunk) < frames:

            result = np.zeros((frames, 2), dtype=np.float32)

            result[:len(chunk)] = chunk

            self.stop()

            return result
        
        self.position = end

        return chunk