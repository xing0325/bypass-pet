"""Paths, sizes, and tunable constants for bypass-pet."""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent  # bypass-pet/
ASSETS_DIR = REPO_ROOT / "assets"

SENTINEL_PATH = Path.home() / ".claude" / "hooks" / ".bypass-on"


def state_dir() -> Path:
    base = os.environ.get("LOCALAPPDATA")
    if base:
        return Path(base) / "bypass-pet"
    return Path.home() / "AppData" / "Local" / "bypass-pet"


SPRITE_SIZE = 128
IDLE_FRAME_COUNT = 8
TRANSITION_FRAME_COUNT = 6
IDLE_FRAME_MS = 250
TRANSITION_FRAME_MS = 100
DRAG_THRESHOLD_PX = 6

# Distance from the screen's available-geometry edges when placing the pet
# for the first time (or after "reset position"). Available geometry already
# excludes the taskbar.
DEFAULT_MARGIN_RIGHT = 24
DEFAULT_MARGIN_BOTTOM = 12

TOOLTIP_ACCEPT = "ACCEPT · Jack · 正常审批"
TOOLTIP_BYPASS = "BYPASS · Tyler · 全自动放权"
