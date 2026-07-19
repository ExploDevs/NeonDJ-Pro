"""
NeonDJ Pro

Audio Analyzer
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import librosa
import numpy as np


@dataclass(slots=True)
class AnalysisResult:
    """
    Ergebnis der Audioanalyse.
    """

    bpm: float
    duration: float
    waveform_preview: np.ndarray


class AudioAnalyzer:
    """
    Analysiert Audiodateien unabhängig vom AudioLoader.
    """

    def analyze(self, file_path: str | Path) -> AnalysisResult:

        path = Path(file_path)

        # Für BPM reicht 22050 Hz vollkommen.
        samples, sample_rate = librosa.load(
            path,
            sr=22050,
            mono=True,
        )

        duration = librosa.get_duration(y=samples, sr=sample_rate)

        tempo, _ = librosa.beat.beat_track(
            y=samples,
            sr=sample_rate,
        )

        tempo = float(np.asarray(tempo).item())

        preview_size = 2000

        indices = np.linspace(
            0,
            len(samples) - 1,
            preview_size,
            dtype=np.int32,
        )

        waveform = samples[indices]

        return AnalysisResult(
            bpm=tempo,
            duration=duration,
            waveform_preview=waveform,
        )