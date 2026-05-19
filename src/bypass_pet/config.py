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


SPRITE_WIDTH = 192
SPRITE_HEIGHT = 240
IDLE_FRAME_COUNT = 60         # 12 fps × 5 s = 60 frames
TRANSITION_FRAME_COUNT = 12   # 20 fps × 0.6 s = 12 frames
IDLE_FRAME_MS = 83            # 1000 / 12 ≈ 83
TRANSITION_FRAME_MS = 50      # 1000 / 20 = 50
DRAG_THRESHOLD_PX = 6

# Distance from the screen's available-geometry edges when placing the pet
# for the first time (or after "reset position"). Available geometry already
# excludes the taskbar.
DEFAULT_MARGIN_RIGHT = 24
DEFAULT_MARGIN_BOTTOM = 12

TOOLTIP_ACCEPT = "ACCEPT · Jack · 正常审批"
TOOLTIP_BYPASS = "BYPASS · Tyler · 全自动放权"
