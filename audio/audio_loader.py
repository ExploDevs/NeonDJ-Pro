"""
NeonDJ Pro

AudioLoader

Lädt Audiodateien und stellt deren Rohdaten
für Analyse und Wiedergabe bereit.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import soundfile as sf
import numpy as np


SUPPORTED_FORMATS = {
    ".mp3",
    ".wav",
    ".flac",
    ".ogg",
    ".aiff",
    ".aif",
}

@dataclass(slots=True)
class AudioTrack:
    """
    Enthält die geladenen Audiodateien und Basisinformationen
    """

    path: Path
    samples: np.ndarray
    sample_rate: int
    channels: int
    duration: float


class AudioLoader:
    """
    Lädt Audiodateien von der Festplatte
    """

    def load(self, file_path: str | Path) -> AudioTrack:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)
        
        if path.suffix.lower() not in SUPPORTED_FORMATS:
            raise ValueError(
                f"Nicht unterstütztes Audioformat: {path.suffix}"
            )
        
        samples, sample_rate = sf.read(
            path,
            always_2d=True,
            dtype="float32",
        )

        channels = samples.shape[1]

        duration = len(samples) / sample_rate

        return AudioTrack(
            path=path,
            samples=samples,
            sample_rate=sample_rate,
            channels=channels,
            duration=duration,
        )