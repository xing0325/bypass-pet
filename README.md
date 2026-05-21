# bypass-pet

A pixel desktop pet for Windows that toggles Claude Code Desktop's permission bypass mode with a single click.

- **accept mode**: **the Narrator ("Jack")** from *Fight Club* — exhausted office drone splashing cold water on his face in a bathroom mirror. Claude is asking permission.
- **bypass mode**: **Tyler Durden** — in the same mirror, peroxide-blonde, red leather jacket, cigarette in the mouth, sometimes reaching his hand out of the mirror toward the viewer. Claude is running with `--dangerously-skip-permissions`.

Single click on the pet flips the state. The pet syncs from a sentinel file (`~/.claude/hooks/.bypass-on`) so it stays in sync with the existing `bypass.cmd` toggle and PreToolUse hook.

> **Heads up**: the pet is the visual layer; the actual auto-approve mechanism lives in the [**claude-bypass-hook**](https://github.com/xing0325/claude-bypass-hook) repo. Install that first (`powershell scripts\install.ps1` in that repo) — without the hook, this pet is just a colored ball that clicks do nothing useful with.

> **History**: this project pivoted three times. (1) 奶龙 (2026-05-17), (2) Fight Club full-body @ 128×128 (2026-05-18 morning), (3) Fight Club mirror scene @ 256×320 / 28 frames (2026-05-18 afternoon, see PR #2 + branch `codex/generate-mirror-sprite-assets`), **(4) current: Fight Club mirror @ 192×240 / 144 frames @ 12 FPS idle / 20 FPS transition (2026-05-19)**. The v3 (PR #2) art is preserved on its branch as a reference for character + scene continuity but is not directly used. If you find any reference to 奶龙 / full-body / 128 / 256×320 / 28-frame in this repo, treat as stale.

---

## Status

| | |
|---|---|
| Design spec | done — see [`docs/superpowers/specs/2026-05-18-fight-club-pet-design.md`](docs/superpowers/specs/2026-05-18-fight-club-pet-design.md) |
| Sprite assets (144 PNGs at 192×240) | **awaiting Codex (v3)** — see [`codex/brief.md`](codex/brief.md). v2 reference art is on branch `codex/generate-mirror-sprite-assets`. |
| Python source | done — runs with placeholder squares until Codex delivers art |

---

## For Codex

If you're Codex and the human handed you this repo: read [`codex/brief.md`](codex/brief.md), then work through [`codex/prompts.md`](codex/prompts.md) frame by frame. Output goes in `assets/`.

You generate **art only**. Don't write Python.

This is the **second pass**. The first attempt was full-body, which didn't read at sprite scale. The current design is a bathroom-mirror scene with bust framing at 256×320.

---

## Run it (placeholder version, while waiting for art)

```powershell
cd C:\Users\david\nailong-pet
.\.venv\Scripts\Activate.ps1
python -m bypass_pet
```

Pet appears in the bottom-right corner of the primary screen. Left-click to toggle. Right-click for menu. Drag to move.

---

## Repo layout

```
bypass-pet/
├── README.md                                            # you are here
├── pyproject.toml                                       # PySide6 dep + entry point
├── src/bypass_pet/                                      # Python source
│   ├── __main__.py
│   ├── app.py                                           # QApplication + sentinel watcher
│   ├── pet_window.py                                    # transparent frameless window
│   ├── animator.py                                      # frame loader + idle/transition timer
│   ├── state.py                                         # sentinel-file read/write
│   └── config.py                                        # paths, sizes, timing
├── codex/
│   ├── brief.md                                         # Codex's task spec
│   ├── prompts.md                                       # 28 frame-by-frame image-2 prompts
│   └── style-reference/                                 # reference images (optional)
├── assets/                                              # Codex output: 28 PNGs at 256×320
├── docs/
│   └── superpowers/specs/2026-05-18-fight-club-pet-design.md
└── tests/
    └── test_state.py
```

---

## Future

A second skin showing the **same window** with Jack inside leaning against the sill (rainy day) and Tyler leaning OUT of the window smoking (city night) is on the post-MVP wishlist. The current code hardcodes a single asset path; future work would refactor `assets/` to `assets/skin-mirror/` + `assets/skin-window/` and add a "switch skin" menu item.

---

## License

Personal project, no license declared yet.
