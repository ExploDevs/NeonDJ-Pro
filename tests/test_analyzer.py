from audio.analyzer import AudioAnalyzer

analyzer = AudioAnalyzer()

result = analyzer.analyze(
    r"C:\Users\User\Music\dior-2001.mp3"
)

print("=== ANALYSIS ===")
print("BPM:", result.bpm)
print("Dauer:", result.duration)
print("Waveform:", result.waveform_preview.shape)