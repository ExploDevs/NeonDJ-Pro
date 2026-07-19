from audio.audio_loader import AudioLoader

loader = AudioLoader()

metadata = loader.load_metadata("C:/Users/User/Music/dior-2001.mp3")

print("Titel:", metadata.title)
print("Dauer:", metadata.duration)
print("Samplerate:", metadata.sample_rate)
print("Kanäle:", metadata.channels)
print("Dateigröße:", metadata.file_size)
print("Endung:", metadata.extension)