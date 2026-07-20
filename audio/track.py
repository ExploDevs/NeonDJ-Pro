"""
NeonDJ Pro

Track Model
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Track:
    """
    Repräsentiert einen geladenen Track.
    """

    path: Path

    title: str

    artist: str

    album: str

    duration: float

    bpm: float

    musical_key: str = ""

    sample_rate: int = 44100

    channels: int = 2