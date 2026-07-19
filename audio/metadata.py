"""
NeonDJ Pro

Audio-Metadaten
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class AudioMetadata:
    """
    Enthält Metadaten eines Audiotracks.
    """

    path: Path

    title: str
    artist: str
    album: str

    duration: float

    sample_rate: int

    channels: int

    file_size: int

    extension: str