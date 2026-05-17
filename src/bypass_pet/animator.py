"""Frame loading + idle/transition playback.

FrameSet caches all 28 sprite frames at startup, falling back to obvious
placeholder pixmaps when a real PNG isn't yet on disk. This lets the pet
boot and demonstrate full behavior before Codex has delivered the art.

Animator owns a QTimer and emits frame_changed signals at the right cadence
for either an infinite idle loop or a one-shot transition.
"""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QObject, QTimer, Qt, Signal
from PySide6.QtGui import QColor, QFont, QPainter, QPen, QPixmap

from .config import (
    IDLE_FRAME_COUNT,
    IDLE_FRAME_MS,
    SPRITE_SIZE,
    TRANSITION_FRAME_COUNT,
    TRANSITION_FRAME_MS,
)
from .state import State

# Per-state palette swatches for placeholder rendering. Matches the moods
# from codex/brief.md: cool office green-gray for Jack, warm oxblood for
# Tyler.
_PLACEHOLDER_PALETTE: dict[State, tuple[str, str]] = {
    "accept": ("#7A8475", "#E8E2D5"),  # bg, fg
    "bypass": ("#A11D1D", "#FCD600"),
}


class FrameSet:
    """Loads sprite frames from disk; substitutes placeholders for any missing."""

    def __init__(self, assets_dir: Path) -> None:
        self.assets_dir = assets_dir
        self._cache: dict[str, QPixmap] = {}
        self.missing: list[str] = []
        self._load_all()

    def _load_all(self) -> None:
        for state in ("accept", "bypass"):
            for i in range(IDLE_FRAME_COUNT):
                self._populate(f"{state}_idle_{i:02d}", state, f"{state}\nidle {i}")
            for i in range(TRANSITION_FRAME_COUNT):
                self._populate(
                    f"trans_to_{state}_{i:02d}",
                    state,
                    f"-> {state}\n{i}",
                )

    def _populate(self, key: str, state: State, label: str) -> None:
        path = self.assets_dir / f"{key}.png"
        if path.is_file():
            pix = QPixmap(str(path))
            if not pix.isNull() and pix.width() > 0:
                if pix.width() != SPRITE_SIZE or pix.height() != SPRITE_SIZE:
                    pix = pix.scaled(
                        SPRITE_SIZE,
                        SPRITE_SIZE,
                        Qt.IgnoreAspectRatio,
                        Qt.SmoothTransformation,
                    )
                self._cache[key] = pix
                return
        self.missing.append(key)
        self._cache[key] = self._make_placeholder(state, label)

    @staticmethod
    def _make_placeholder(state: State, label: str) -> QPixmap:
        bg_hex, fg_hex = _PLACEHOLDER_PALETTE[state]
        pix = QPixmap(SPRITE_SIZE, SPRITE_SIZE)
        pix.fill(QColor(bg_hex))
        painter = QPainter(pix)
        painter.setRenderHint(QPainter.Antialiasing, False)
        painter.setPen(QPen(QColor(fg_hex), 2))
        painter.drawRect(2, 2, SPRITE_SIZE - 4, SPRITE_SIZE - 4)
        painter.setFont(QFont("Consolas", 12, QFont.Bold))
        painter.drawText(
            pix.rect().adjusted(6, 6, -6, -6),
            Qt.AlignCenter | Qt.TextWordWrap,
            label,
        )
        painter.end()
        return pix

    def idle(self, state: State, frame: int) -> QPixmap:
        return self._cache[f"{state}_idle_{frame:02d}"]

    def transition(self, target_state: State, frame: int) -> QPixmap:
        return self._cache[f"trans_to_{target_state}_{frame:02d}"]


class Animator(QObject):
    """Drives which frame to show, given the current and target state."""

    frame_changed = Signal(QPixmap)
    transition_finished = Signal(str)  # emits the new state

    def __init__(self, frames: FrameSet, initial_state: State = "accept") -> None:
        super().__init__()
        self.frames = frames
        self.state: State = initial_state
        self.target_state: State = initial_state
        self.mode: str = "idle"  # "idle" or "transition"
        self._idx = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._start_idle()

    @property
    def effective_target(self) -> State:
        """Where the animator will end up — current state, or in-flight target."""
        return self.target_state if self.mode == "transition" else self.state

    def begin_transition(self, target_state: State) -> None:
        if target_state == self.effective_target:
            return  # nothing to do — debounces external watcher events
        self.target_state = target_state
        self.mode = "transition"
        self._idx = 0
        self._timer.start(TRANSITION_FRAME_MS)
        self.frame_changed.emit(self.frames.transition(target_state, 0))

    def _start_idle(self) -> None:
        self.mode = "idle"
        self._idx = 0
        self._timer.start(IDLE_FRAME_MS)
        self.frame_changed.emit(self.frames.idle(self.state, 0))

    def _tick(self) -> None:
        self._idx += 1
        if self.mode == "idle":
            self._idx %= IDLE_FRAME_COUNT
            self.frame_changed.emit(self.frames.idle(self.state, self._idx))
            return
        # transition
        if self._idx >= TRANSITION_FRAME_COUNT:
            self.state = self.target_state
            self._start_idle()
            self.transition_finished.emit(self.state)
            return
        self.frame_changed.emit(self.frames.transition(self.target_state, self._idx))
