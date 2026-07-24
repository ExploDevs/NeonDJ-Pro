"""
Test für den WaveformGenerator.
"""

from audio.audio_loader import AudioLoader
from audio.waveform import WaveformGenerator

loader = AudioLoader()

track = loader.load(
    r"C:\Users\User\Music\dior-2001.mp3"
)

generator = WaveformGenerator()

waveform = generator.generate(
    track.samples,
    width=1000,
)

print("Anzahl Punkte:", len(waveform))
print("Minimum:", waveform.min())
print("Maximum:", waveform.max())
print("Erste 10 Werte:")
print(waveform[:10])