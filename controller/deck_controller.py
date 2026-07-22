"""
NeonDJ Pro

DeckController

Verbindet UI und Audio-Engine.
"""

from audio.track import Track
from audio.audio_engine import AudioEngine


class DeckController:

    def __init__(
        self,
        audio_engine: AudioEngine,
        deck: str,
    ) -> None:
        
        self.audio_engine = audio_engine
        self.deck = deck


        self.track: Track | None = None

        self.widget = None



    @property
    def playing(self) -> bool:
        return self.player.playing
    
    @property
    def player(self):
        """
        Gibt den DeckPlayer dieses Controllers zurück
        """

        if self.deck == "A":
            return self.audio_engine.deck_a
        
        return self.audio_engine.deck_b

    def set_widget(self, widget) -> None:
        """
        Verbindet den Controller mit seinem DeckWidget
        """

        self.widget = widget

    def load_track(self, track: Track) -> None:
        """
        Lädt einen Track in dieses Deck.
        """

        self.track = track

        if self.widget is not None:
            self.widget.load_track(track)

        if self.deck == "A":
            self.audio_engine.load_deck_a(track.path)
        else:
            self.audio_engine.load_deck_b(track.path)

    def play(self) -> None:
        """
        Startet die Wiedergabe dieses Decks
        """

        self.player.play()
        self.audio_engine.start()

    def pause(self) -> None:
        """
        Pausiert die Wiedergabe
        """

        self.player.pause()

    def stop(self) -> None:
        """
        Stoppt die Wiedergabe 
        """

        self.player.stop()