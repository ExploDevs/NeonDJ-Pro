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

        self.deck = DeckPlayer()

    def load(self, file_path: str | Path) -> None:
        """
        Lädt einen Track in den Speicher.
        """

        self.deck.load(file_path)
        self.sample_rate = self.deck.sample_rate

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

        chunk = self.deck.next_frames(frames)

        outdata[:] = chunk


    def start(self) -> None:

        if self.stream is not None:
            return
        
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