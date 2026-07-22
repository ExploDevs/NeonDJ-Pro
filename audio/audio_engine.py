"""
NeonDJ Pro

Audio Engine
"""

from __future__ import annotations

from pathlib import Path

#import numpy as np
import sounddevice as sd
#import soundfile as sf

from audio.deck_player import DeckPlayer


class AudioEngine:
    """
    Verwaltet den Audio-Output.
    """

    def __init__(self) -> None:

        self.sample_rate = 44100
        self.block_size = 512

        self.stream: sd.OutputStream | None = None

        self.deck_a = DeckPlayer()
        self.deck_b = DeckPlayer()

    def load_deck_a(self, file_path: str | Path) -> None:
        self.deck_a.load(file_path)
        self.sample_rate = self.deck_a.sample_rate

    def load_deck_b(self, file_path: str | Path) -> None:
        self.deck_b.load(file_path)

        if self.deck_a.samples is None:
            self.sample_rate = self.deck_b.sample_rate

    def _audio_callback(
        self,
        outdata,
        frames,
        time,
        status,
    ) -> None:
        """
        Wird von der Soundkarte aufgerufen.
        """

        if status:
            print(status)

        chunk_a = self.deck_a.next_frames(frames)
        chunk_b = self.deck_b.next_frames(frames)

        mixed = (chunk_a + chunk_b) * 0.5

        outdata[:] = mixed


    def start(self) -> None:

        if self.stream is not None:
            return
        
        print("Engine sample_rate:", self.sample_rate)
        print("Deck A sample_rate:", self.deck_a.sample_rate)
        print("Deck B sample_rate:", self.deck_b.sample_rate)
        
        self.stream = sd.OutputStream(
            samplerate=self.sample_rate,
            channels=2,
            blocksize=self.block_size,
            callback=self._audio_callback,
        )

        self.stream.start()

    def stop(self) -> None:

        if self.stream is None:
            return
        
        self.stream.stop()
        self.stream.close()

        self.stream = None