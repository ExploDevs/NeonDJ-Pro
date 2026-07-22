"""
NeonDJ Pro

Audio Engine
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sounddevice as sd
import soundfile as sf


class AudioEngine:
    """
    Verwaltet den Audio-Output.
    """

    def __init__(self) -> None:

        self.sample_rate = 44100
        self.block_size = 512

        self.stream: sd.OutputStream | None = None

        self.samples: np.ndarray | None = None
        self.position = 0

    def load(self, file_path: str | Path) -> None:
        """
        Lädt einen Track in den Speicher.
        """

        self.samples, self.sample_rate = sf.read(
            file_path,
            dtype='float32',
            always_2d=True,
        )

        self.position = 0

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

        if self.samples is None:
            outdata.fill(0)
            return
        
        end = self.position + frames

        chunk = self.samples[self.position:end]

        if len(chunk) < frames:

            outdata.fill(0)

            outdata[:len(chunk)] = chunk

            self.position = 0

            return
        
        outdata[:] = chunk

        self.position = end

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