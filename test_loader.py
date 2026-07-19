from audio.audio_loader import AudioLoader

loader = AudioLoader()

track = loader.load(r"C:\Users\User\Music\dior-2001.mp3")

print(track.path)
print(track.sample_rate)
print(track.channels)
print(track.duration)
print(track.samples.shape)