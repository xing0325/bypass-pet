"""Frame loading + idle/transition playback.

FrameSet caches all sprite frames at startup, falling back to ball-shaped
placeholder pixmaps when a real PNG isn't yet on disk. This lets the pet
boot, look like a floating ball with a state label, and be obviously
toggleable before Codex has delivered the art.

Animator owns a QTimer and emits frame_changed signals at the right cadence
for either an infinite idle loop or a one-shot transition.
"""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QObject, QRect, QTimer, Qt, Signal
from PySide6.QtGui import QColor, QFont, QPainter, QPen, QPixmap

from .config import (
    IDLE_FRAME_COUNT,
    IDLE_FRAME_MS,
    SPRITE_HEIGHT,
    SPRITE_WIDTH,
    TRANSITION_FRAME_COUNT,
    TRANSITION_FRAME_MS,
)
from .state import State

# Per-state palette for placeholder rendering. Mood matches codex/brief.md:
# cool sage-green for Jack ("accept"), warm oxblood-red for Tyler ("bypass").
_PLACEHOLDER_PALETTE: dict[State, tuple[str, str]] = {
    "accept": ("#5b6b5e", "#e8e2d5"),   # bg fill, fg text+border
    "bypass": ("#a11d1d", "#fcd600"),
}


class FrameSet:
    """Loads sprite frames from disk; substitutes ball placeholders for any missing."""

    def __init__(self, assets_dir: Path) -> None:
        self.assets_dir = assets_dir
        self._cache: dict[str, QPixmap] = {}
        self.missing: list[str] = []
        self._load_all()

    def _load_all(self) -> None:
        for state in ("accept", "bypass"):
            for i in range(IDLE_FRAME_COUNT):
                self._populate(f"{state}_idle_{i:02d}", state, "idle", i)
            for i in range(TRANSITION_FRAME_COUNT):
                self._populate(f"trans_to_{state}_{i:02d}", state, "transition", i)

    def _populate(self, key: str, state: State, kind: str, frame_idx: int) -> None:
        path = self.assets_dir / f"{key}.png"
        if path.is_file():
            pix = QPixmap(str(path))
            if not pix.isNull() and pix.width() > 0:
                if pix.width() != SPRITE_WIDTH or pix.height() != SPRITE_HEIGHT:
                    pix = pix.scaled(
                        SPRITE_WIDTH,
                        SPRITE_HEIGHT,
                        Qt.IgnoreAspectRatio,
                        Qt.SmoothTransformation,
                    )
                self._cache[key] = pix
                return
        self.missing.append(key)
        self._cache[key] = self._make_placeholder(kind, state, frame_idx)

    BALL_SIZE = 72   # placeholder ball is smaller than the canvas so it
                     # reads as a small floating sphere with breathing room

    @staticmethod
    def _make_placeholder(kind: str, state: State, frame_idx: int) -> QPixmap:
        pix = QPixmap(SPRITE_WIDTH, SPRITE_HEIGHT)
        pix.fill(Qt.transparent)
        painter = QPainter(pix)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Ball centered horizontally; nudged slightly above vertical center
        # to leave room for the subtitle line beneath it.
        side = FrameSet.BALL_SIZE
        ball_rect = QRect(
            (SPRITE_WIDTH - side) // 2,
            (SPRITE_HEIGHT - side) // 2 - 14,
            side,
            side,
        )

        if kind == "idle":
            bg_hex, fg_hex = _PLACEHOLDER_PALETTE[state]
            bg, fg = QColor(bg_hex), QColor(fg_hex)
            FrameSet._paint_ball(painter, ball_rect, bg, fg)
            FrameSet._paint_main_label(painter, ball_rect, state.upper(), fg)
            subtitle = "审批中" if state == "accept" else "裸奔中"
            FrameSet._paint_subtitle(painter, ball_rect, subtitle, fg)
        else:  # transition
            prev_state: State = "accept" if state == "bypass" else "bypass"
            prev_bg, _ = _PLACEHOLDER_PALETTE[prev_state]
            new_bg_hex, new_fg_hex = _PLACEHOLDER_PALETTE[state]
            new_fg = QColor(new_fg_hex)
            FrameSet._paint_transition_ball(
                painter,
                ball_rect,
                QColor(prev_bg),
                QColor(new_bg_hex),
                new_fg,
                frame_idx,
            )
            FrameSet._paint_main_label(painter, ball_rect, f"→ {state.upper()}", new_fg)

        painter.end()
        return pix

    # ------------------------------------------------------------------ paint helpers

    @staticmethod
    def _paint_ball(painter: QPainter, rect: QRect, fill: QColor, border: QColor) -> None:
        painter.setBrush(fill)
        painter.setPen(QPen(border, 3))
        painter.drawEllipse(rect)

    @staticmethod
    def _paint_transition_ball(
        painter: QPainter,
        rect: QRect,
        prev_fill: QColor,
        new_fill: QColor,
        border: QColor,
        frame_idx: int,
    ) -> None:
        # Left-to-right wipe: progress 0..1 paints the new state's color
        # over the previous state, sweeping from the ball's left edge to
        # its right. Echoes the half-and-half split that the actual Codex
        # transition art uses around frame 5-6.
        progress = frame_idx / max(TRANSITION_FRAME_COUNT - 1, 1)
        wipe_x = rect.left() + int(progress * rect.width())

        painter.setPen(Qt.NoPen)
        painter.setBrush(prev_fill)
        painter.drawEllipse(rect)

        if wipe_x > rect.left():
            painter.save()
            painter.setClipRect(rect.left(), rect.top(), wipe_x - rect.left(), rect.height())
            painter.setBrush(new_fill)
            painter.drawEllipse(rect)
            painter.restore()

        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(border, 3))
        painter.drawEllipse(rect)

    @staticmethod
    def _paint_main_label(painter: QPainter, ball_rect: QRect, text: str, color: QColor) -> None:
        painter.setPen(color)
        painter.setFont(QFont("Segoe UI", 10, QFont.Bold))
        painter.drawText(ball_rect, Qt.AlignCenter, text)

    @staticmethod
    def _paint_subtitle(painter: QPainter, ball_rect: QRect, text: str, color: QColor) -> None:
        painter.setPen(color)
        painter.setFont(QFont("Microsoft YaHei UI", 9, QFont.Bold))
        subtitle_rect = QRect(0, ball_rect.bottom() + 6, SPRITE_WIDTH, 22)
        painter.drawText(subtitle_rect, Qt.AlignHCenter | Qt.AlignTop, text)

    # ------------------------------------------------------------------ lookup

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
        if self._idx >= TRANSITION_FRAME_COUNT:
            self.state = self.target_state
            self._start_idle()
            self.transition_finished.emit(self.state)
            return
        self.frame_changed.emit(self.frames.transition(self.target_state, self._idx))
