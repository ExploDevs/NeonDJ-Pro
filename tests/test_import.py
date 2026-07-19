from audio.audio_loader import AudioLoader
from audio.analyzer import AudioAnalyzer

from database.database import Database
from database.track_repository import TrackRepository

loader = AudioLoader()
analyzer = AudioAnalyzer()

db = Database()
repository = TrackRepository(db)

path = r"C:\Users\User\Music\dior-2001.mp3"

metadata = loader.load_metadata(path)
analysis = analyzer.analyze(path)

repository.add_track(
    metadata,
    analysis,
)

print("Track erfolgreich importiert.")

tracks = repository.get_all_tracks()

print()

print("=== TRACKS IN DATABASE ===")

for track in tracks:
    print(
        f"{track['title']} | "
        f"{track['artist']} | "
        f"{track['bpm']:.2f} BPM"
    )

db.close()