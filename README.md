# bypass-pet

A pixel desktop pet for Windows that toggles Claude Code Desktop's permission bypass mode with a single click.

- **accept mode**: **the Narrator** ("Jack") from *Fight Club* — exhausted office drone in a wrinkled white shirt and loosened tie, dark circles, slouched. Claude is asking permission.
- **bypass mode**: **Tyler Durden** from *Fight Club* — red leather jacket, peroxide hair, smug smirk, cigarette in the corner of his mouth. Claude is running with `--dangerously-skip-permissions`.

Single click on the pet flips the state. The pet syncs from a sentinel file (`~/.claude/hooks/.bypass-on`) so it stays in sync with the existing `bypass.cmd` toggle and PreToolUse hook.

> **Pivoted from 奶龙 to Fight Club on 2026-05-18.** If you find any 奶龙 / dragon references anywhere in this repo, they're stale — ignore them.

---

## Status

| | |
|---|---|
| Design spec | done — see [`docs/superpowers/specs/2026-05-18-fight-club-pet-design.md`](docs/superpowers/specs/2026-05-18-fight-club-pet-design.md) |
| Sprite assets (28 PNGs) | **awaiting Codex** — see [`codex/brief.md`](codex/brief.md) |
| Python source | not yet written |

---

## For Codex

If you're Codex and the human handed you this repo: read [`codex/brief.md`](codex/brief.md), then work through [`codex/prompts.md`](codex/prompts.md) frame by frame. Output goes in `assets/`.

You generate **art only**. Don't write Python.

---

## Repo layout

```
bypass-pet/
├── README.md                                            # you are here
├── codex/
│   ├── brief.md                                         # Codex's task spec (Jack/Tyler bibles, style rules)
│   ├── prompts.md                                       # 28 frame-by-frame image-2 prompts
│   └── style-reference/                                 # reference images (optional, can be empty)
├── assets/                                              # Codex output: 28 PNGs at 128×128
├── docs/
│   └── superpowers/specs/2026-05-18-fight-club-pet-design.md
├── src/                                                 # Python source (later)
└── tests/                                               # tests (later)
```

---

## Why this exists

Claude Code Desktop has [a bug](https://github.com/anthropics/claude-code/issues/29026) where `permissions.allow` and `defaultMode: bypassPermissions` in `settings.json` are ignored. The user worked around it with a `PreToolUse` hook that reads a sentinel file. The pet is a visual indicator + one-click toggle for that sentinel.

The two characters from *Fight Club* (1999) are the same person seen from two sides: a tired conformist who asks permission, and a destructive alter-ego who does what he wants. That contrast maps directly onto the toggle.

---

## License

Personal project, no license declared yet.
