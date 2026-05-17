"""Sentinel-file state model.

The Claude Code PreToolUse hook reads a sentinel file:
its presence means "bypass on", its absence means "accept (defer)".

This module owns reading and writing that file. The pet's UI never
touches the path directly — it goes through SentinelState.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

State = Literal["accept", "bypass"]


class SentinelState:
    def __init__(self, sentinel_path: Path) -> None:
        self.path = sentinel_path

    def current(self) -> State:
        return "bypass" if self.path.exists() else "accept"

    def toggle(self) -> State:
        if self.path.exists():
            self.path.unlink()
            return "accept"
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch()
        return "bypass"

    def set(self, state: State) -> State:
        if state == "bypass":
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.touch(exist_ok=True)
        elif state == "accept":
            self.path.unlink(missing_ok=True)
        else:
            raise ValueError(f"unknown state: {state!r}")
        return state
