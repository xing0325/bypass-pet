# nailong-pet

A pixel desktop pet for Windows that toggles Claude Code Desktop's permission bypass mode with a single click.

- **accept mode**: 梵高《星月夜》风格奶龙 — calm, breathing, blinking. Claude is asking permission.
- **bypass mode**: 苏联构成主义风格奶龙 — shouting through a megaphone, fist pumping. Claude is running with `--dangerously-skip-permissions`.

Single click on the pet flips the state. The pet syncs from a sentinel file (`~/.claude/hooks/.bypass-on`) so it stays in sync with the existing `bypass.cmd` toggle and PreToolUse hook.

---

## Status

| | |
|---|---|
| Design spec | done — see [`docs/superpowers/specs/2026-05-17-nailong-pet-design.md`](docs/superpowers/specs/2026-05-17-nailong-pet-design.md) |
| Sprite assets (28 PNGs) | **awaiting Codex** — see `codex/brief.md` |
| Python source | not yet written |

---

## For Codex

If you're Codex and the human handed you this repo: read [`codex/brief.md`](codex/brief.md), then work through [`codex/prompts.md`](codex/prompts.md) frame by frame. Output goes in `assets/`.

You generate **art only**. Don't write Python.

---

## Repo layout

```
nailong-pet/
├── README.md                                            # you are here
├── codex/
│   ├── brief.md                                         # Codex's task spec
│   ├── prompts.md                                       # 28 frame-by-frame image-2 prompts
│   └── style-reference/                                 # reference images (optional, can be empty)
├── assets/                                              # Codex output: 28 PNGs at 128×128
├── docs/
│   └── superpowers/specs/2026-05-17-nailong-pet-design.md
├── src/                                                 # Python source (later)
└── tests/                                               # tests (later)
```

---

## Why this exists

Claude Code Desktop has [a bug](https://github.com/anthropics/claude-code/issues/29026) where `permissions.allow` and `defaultMode: bypassPermissions` in `settings.json` are ignored. The user worked around it with a `PreToolUse` hook that reads a sentinel file. The pet is a visual indicator + one-click toggle for that sentinel.

The character is **奶龙** (a viral Chinese cartoon dragon). The two-state design (meditation ↔ revolution) mirrors the seriousness of letting an AI execute commands without asking.

---

## License

Personal project, no license declared yet.
