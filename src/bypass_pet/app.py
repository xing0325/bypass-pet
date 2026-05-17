"""Application entry point: wire QApplication, the pet window, and the sentinel watcher."""

from __future__ import annotations

import sys

from PySide6.QtCore import QFileSystemWatcher
from PySide6.QtWidgets import QApplication

from .animator import Animator, FrameSet
from .config import ASSETS_DIR, SENTINEL_PATH, state_dir
from .pet_window import PetWindow, PositionStore
from .state import SentinelState


def run() -> int:
    app = QApplication.instance() or QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    sentinel = SentinelState(SENTINEL_PATH)
    initial_state = sentinel.current()

    frames = FrameSet(ASSETS_DIR)
    if frames.missing:
        print(
            f"[bypass-pet] {len(frames.missing)} sprite frames missing — "
            f"showing placeholders. Run Codex to populate assets/.",
            file=sys.stderr,
        )

    animator = Animator(frames, initial_state=initial_state)

    position_store = PositionStore(state_dir() / "state.json")

    window = PetWindow(sentinel, animator, position_store)
    window.show()

    # Watch the sentinel's parent directory so we sync to external toggles
    # (the bypass.cmd script, or the desktop shortcut). Watching the file
    # itself loses the watch when the file is deleted.
    SENTINEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    watcher = QFileSystemWatcher([str(SENTINEL_PATH.parent)])

    def on_dir_changed(_path: str) -> None:
        new_state = sentinel.current()
        if new_state == animator.effective_target:
            return
        animator.begin_transition(new_state)
        window._update_tooltip()  # noqa: SLF001 — intentional internal call

    watcher.directoryChanged.connect(on_dir_changed)

    return app.exec()
