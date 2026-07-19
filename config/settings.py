"""
Zentrale Einstellungen
"""

import json
from pathlib import Path

from config.constants import ROOT_DIR

CONFIG_FILE = ROOT_DIR / "config" / "config.json"

class Settings:

    def __init__(self):

        self.data = {}

        self.load()

    def load(self):

        if CONFIG_FILE.exists():

            with open(CONFIG_FILE, "r", encoding="utf-8") as file:

                self.data = json.load(file)

        else:

            self.data = {

                "theme": "neon",

                "language": "de",

                "sample_rate": 48000,

                "buffer_size": 512,

                "master_volume": 0.8
            }

            self.save()

    def save(self):

        with open(CONFIG_FILE, "w", encoding="utf-8") as file:

            json.dump(
                self.data,
                file,
                indent=4
            )

    def get(self, key):

        return self.data.get(key)
    
    def set(self, key, value):

        self.data[key] = value

        self.save()