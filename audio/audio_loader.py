"""
NeonDJ Pro

AudioLoader

Lädt Audiodateien und stellt deren Rohdaten
für Analyse und Wiedergabe bereit.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mutagen import File

import soundfile as sf
import numpy as np
from audio.metadata import AudioMetadata


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
    
    def load_metadata(self, file_path: str | Path) -> AudioMetadata:
        """
        Liest grundlegende Metadaten einer Audiodatei
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)
        
        info = sf.info(path)

        audio = File(path, easy=True)

        title = path.stem
        artist = ""
        album = ""

        if audio is not None:

            if "title" in audio:
                title = audio["title"][0]

            if "artist" in audio:
                artist = audio["artist"][0]

            if "album" in audio:
                album = audio["album"][0]

        return AudioMetadata(
            path=path,
            title=title,
            artist=artist,
            album=album,
            duration=info.duration,
            sample_rate=info.samplerate,
            channels=info.channels,
            file_size=path.stat().st_size,
            extension=path.suffix.lower(),
        )