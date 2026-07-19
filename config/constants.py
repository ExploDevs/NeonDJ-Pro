"""
NeonDJ Pro
Globale Konstanten
"""

from pathlib import Path

# ---------------
# Projektpfade
# ---------------

ROOT_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = ROOT_DIR / "assets"
ICONS_DIR = ROOT_DIR / "icons"
THEMES_DIR = ROOT_DIR / "themes"
DOCS_DIR = ROOT_DIR / "docs"
DATABASE_DIR = ROOT_DIR / "database"
LOG_DIR = ROOT_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

# -----------------------------
# Programm
# -----------------------------

APP_NAME = "NeonDJ Pro"

APP_VERSION = "0.1.0"

ORGANIZATION = "ExploDevs"

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

# -----------------------------
# Audio
# -----------------------------

DEFAULT_SAMPLE_RATE = 48000
DEFAULT_BUFFER_SIZE = 512

CHANNELS = 2
