from audio.audio_loader import AudioLoader

loader = AudioLoader()

track = loader.load(r"C:\Users\User\Music\dior-2001.mp3")

print("=== AUDIO LOADER ===")
print("Pfad:", track.path)
print("Samplerate:", track.sample_rate)
print("Kanäle:", track.channels)
print("Dauer:", track.duration)
print("Shape:", track.samples.shape)

metadata = loader.load_metadata(track.path)

print("\n=== METADATA ===")
print("Titel:", metadata.title)
print("Dateigröße:", metadata.file_size)
print("Endung:", metadata.extension)