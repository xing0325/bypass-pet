"""The visible pet window: transparent, frameless, top-most, click+drag."""

from __future__ import annotations

import json
from pathlib import Path

from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import (
    QGuiApplication,
    QMouseEvent,
    QPainter,
    QPixmap,
)
from PySide6.QtWidgets import QApplication, QMenu, QMessageBox, QWidget

from .animator import Animator
from .config import (
    DEFAULT_MARGIN_BOTTOM,
    DEFAULT_MARGIN_RIGHT,
    DRAG_THRESHOLD_PX,
    SPRITE_SIZE,
    TOOLTIP_ACCEPT,
    TOOLTIP_BYPASS,
)
from .state import SentinelState


class PositionStore:
    """Persists the pet's last (x, y) so it returns to where you left it."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> tuple[int, int] | None:
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            return int(data["x"]), int(data["y"])
        except (OSError, ValueError, KeyError):
            return None

    def save(self, xy: tuple[int, int]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps({"x": int(xy[0]), "y": int(xy[1])}),
            encoding="utf-8",
        )


class PetWindow(QWidget):
    def __init__(
        self,
        sentinel: SentinelState,
        animator: Animator,
        position_store: PositionStore,
    ) -> None:
        super().__init__()
        self.sentinel = sentinel
        self.animator = animator
        self.position_store = position_store

        self._pixmap: QPixmap | None = None
        self._press_offset: QPoint | None = None
        self._was_drag = False

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setFixedSize(SPRITE_SIZE, SPRITE_SIZE)
        self.setWindowTitle("bypass-pet")

        self.animator.frame_changed.connect(self._on_frame)
        self.animator.transition_finished.connect(lambda _: self._update_tooltip())

        self._update_tooltip()
        self._place(self.position_store.load())

    # ------------------------------------------------------------------ placement

    def _place(self, saved: tuple[int, int] | None) -> None:
        if saved is not None:
            self.move(*saved)
            return
        self._place_default()

    def _place_default(self) -> None:
        screen = QGuiApplication.primaryScreen().availableGeometry()
        x = screen.right() - SPRITE_SIZE - DEFAULT_MARGIN_RIGHT
        y = screen.bottom() - SPRITE_SIZE - DEFAULT_MARGIN_BOTTOM
        self.move(x, y)

    # ------------------------------------------------------------------ rendering

    def _on_frame(self, pix: QPixmap) -> None:
        self._pixmap = pix
        self.update()

    def paintEvent(self, _event) -> None:
        if self._pixmap is None:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, False)
        painter.drawPixmap(0, 0, self._pixmap)
        painter.end()

    def _update_tooltip(self) -> None:
        if self.sentinel.current() == "bypass":
            self.setToolTip(TOOLTIP_BYPASS)
        else:
            self.setToolTip(TOOLTIP_ACCEPT)

    # ------------------------------------------------------------------ mouse

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self._press_offset = (
                event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )
            self._was_drag = False
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self._press_offset is None:
            return
        new_top_left = event.globalPosition().toPoint() - self._press_offset
        if not self._was_drag:
            delta = new_top_left - self.frameGeometry().topLeft()
            if delta.manhattanLength() > DRAG_THRESHOLD_PX:
                self._was_drag = True
        if self._was_drag:
            self.move(new_top_left)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton and self._press_offset is not None:
            if self._was_drag:
                self.position_store.save((self.x(), self.y()))
            else:
                self._toggle()
        self._press_offset = None
        self._was_drag = False
        super().mouseReleaseEvent(event)

    def _toggle(self) -> None:
        new_state = self.sentinel.toggle()
        self.animator.begin_transition(new_state)
        self._update_tooltip()

    # ------------------------------------------------------------------ menu

    def contextMenuEvent(self, event) -> None:
        menu = QMenu(self)
        act_accept = menu.addAction("强制切到 ACCEPT (Jack)")
        act_bypass = menu.addAction("强制切到 BYPASS (Tyler)")
        menu.addSeparator()
        act_reset = menu.addAction("重置位置（屏右下角）")
        act_about = menu.addAction("关于")
        menu.addSeparator()
        act_quit = menu.addAction("退出")

        chosen = menu.exec(event.globalPos())
        if chosen is None:
            return
        if chosen is act_accept:
            self.sentinel.set("accept")
            self.animator.begin_transition("accept")
            self._update_tooltip()
        elif chosen is act_bypass:
            self.sentinel.set("bypass")
            self.animator.begin_transition("bypass")
            self._update_tooltip()
        elif chosen is act_reset:
            self._place_default()
            self.position_store.save((self.x(), self.y()))
        elif chosen is act_about:
            self._show_about()
        elif chosen is act_quit:
            QApplication.quit()

    def _show_about(self) -> None:
        QMessageBox.information(
            self,
            "bypass-pet",
            "bypass-pet · Fight Club 桌宠\n\n"
            "ACCEPT (Jack) ↔ BYPASS (Tyler)\n"
            "左键单击切换 · 拖动改位置 · 右键看菜单\n\n"
            f"哨兵文件: {self.sentinel.path}\n"
            "Hook 配置: ~/.claude/settings.json",
        )
