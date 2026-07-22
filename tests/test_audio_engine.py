from audio.audio_engine import AudioEngine

engine = AudioEngine()

engine.load_deck_a(
    r"C:\Users\User\Music\dior-2001.mp3"
)

engine.load_deck_b(
    r"C:\Users\User\Music\abracadabra.mp3"
)

engine.deck_a.play()
engine.deck_b.play()

engine.start()

print("Song läuft...")

input("ENTER zum Stoppen")

engine.stop()