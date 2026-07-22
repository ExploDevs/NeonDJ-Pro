from audio.audio_engine import AudioEngine

engine = AudioEngine()

engine.load(
    r"C:\Users\User\Music\dior-2001.mp3"
)

engine.deck.play()

engine.start()

print("Song läuft...")

input("ENTER zum Stoppen")

engine.stop()