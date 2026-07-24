"""
NeonDJ Pro

Waveform Generator

Erzeugt eine vereinfachte Waveform aus Audiodaten.
"""

from __future__ import annotations

import numpy as np

class WaveformGenerator:
    """
    Erzeugt eine zeichenbare Waveform
    """

    def generate(
        self,
        samples: np.ndarray,
        width: int,
    ) -> np.ndarray:
        """
        Erzeugt eine vereinfachte Waveform.

        Aktuell nur Platzhalter
        """

        if len(samples) == 0:
            return np.zeros(width, dtype=np.float32)

        # Stereo -> Mono
        if samples.ndim == 2:
            samples = np.mean(samples, axis=1)

        block_size = max(1, len(samples) // width)

        peaks = []

        for i in range(width):

            start = i * block_size
            end = start + block_size

            block = samples[start:end]

            if len(block) == 0:
                peaks.append(0.0)
            else:
                peaks.append(np.max(np.abs(block)))

        return np.asarray(peaks, dtype=np.float32)