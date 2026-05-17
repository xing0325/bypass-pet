# Codex Task Brief — nailong-pet 桌宠素材生成

You (Codex) are reading this because the human handed you this repo and said "make the art".

Your job: generate **28 PNG sprite frames** for a Windows desktop pixel pet that toggles between two visual states. You are NOT writing Python source code — that part is owned by Claude. You only produce image assets.

Everything you need to do is in this folder. The full project context is in `docs/superpowers/specs/2026-05-17-nailong-pet-design.md` — skim it once for context but don't get lost; this brief is the operational instruction.

---

## 0. The pet, in one sentence

A 128×128 pixel sprite of **奶龙** (a chubby yellow Chinese cartoon dragon meme), rendered in two opposing art styles that flip when the user clicks the pet on their desktop. The flip mirrors a "Claude Code permission bypass mode" toggle, so the symbolism is meditation ↔ revolution.

## 1. What you generate

**28 PNG files**, all 128×128, **transparent background (alpha channel)**, dropped into `assets/`:

| Filename pattern | Count | Style | Animation role |
|---|---|---|---|
| `assets/accept_idle_00.png` … `accept_idle_07.png` | 8 | Van Gogh *Starry Night* | Idle loop, "accept" state |
| `assets/bypass_idle_00.png` … `bypass_idle_07.png` | 8 | Russian Constructivism | Idle loop, "bypass" state |
| `assets/trans_to_bypass_00.png` … `trans_to_bypass_05.png` | 6 | Cross-fade from A to B | accept → bypass transition |
| `assets/trans_to_accept_00.png` … `trans_to_accept_05.png` | 6 | Cross-fade from B to A | bypass → accept transition |

**Filenames are load-bearing.** The Python animator code will iterate `00..07` (or `00..05`) and crash if a frame is missing. Do not invent names; do not zero-pad differently.

### Output requirements (hard rules)

- **Dimensions**: exactly 128×128 pixels
- **Format**: PNG with alpha channel
- **Background**: fully transparent (alpha 0) outside the sprite's silhouette
- **Color depth**: 8-bit per channel RGBA
- **No anti-aliasing-induced halos**: the alpha edge should be clean against transparent, not fringed with the source background color
- **No watermarks, signatures, or text outside the sprite's intended composition**

If image-2 outputs something larger or with opaque background, downscale/composite to spec before saving.

## 2. The character bible — 奶龙

This MUST stay consistent across all 28 frames. Reference search: <https://www.bing.com/images/search?q=%E5%A5%B6%E9%BE%99>

Visual DNA:
- **Color**: milky/golden yellow body (around `#FCD94B`–`#F8C82E`), darker yellow shading
- **Body**: chubby/spherical, body is bigger than legs, tubby silhouette
- **Head**: very large head-to-body ratio (head ≈ 60% of total height)
- **Limbs**: short stubby arms and legs
- **Tail**: small, sometimes hidden
- **Eyes**: large, expressive, dark dots with white highlights
- **Mouth**: can stretch from a small smile to an enormous open laugh
- **Outline**: thin dark outline (not absent, but not heavy black manga lines either)

The pet is **奶龙**, not a generic yellow dragon and not a real dinosaur. If your output looks like a Pokemon or a generic SD anime mascot, you got it wrong — pull back toward the round dumpy Chinese cartoon proportions.

**Pose continuity inside an idle loop**: across the 8 idle frames, the pet's position on the canvas should stay anchored (same feet-line, same center column). Don't let it drift around the frame.

## 3. Style guide A — "accept" idle (Van Gogh Starry Night)

Reference: Vincent van Gogh, *The Starry Night* (1889). Search: <https://www.bing.com/images/search?q=van+gogh+starry+night>

What "Van Gogh starry night style" means here:
- **Background**: a deep cobalt + cerulean blue night sky filled with thick swirling impasto brushstrokes; a large luminous yellow moon/sun glow; small bright yellow stars with halo rings
- **Brushstroke language**: every shape — sky, body outline, internal shading — rendered with short curved comma-strokes, visible directional texture
- **Palette**: deep navy `#1B2A55`, cerulean `#3A6CB3`, golden yellow `#F8D147`, pale cream `#F1E9D2`, cypress dark green `#1A4D3A` (for accents), off-white `#E8E6DF`
- **No**: smooth gradients, photoreal lighting, modern flat vector

How 奶龙 inhabits this style:
- The pet's yellow body becomes a Van Gogh-yellow with comma-strokes visible across its skin
- Outline is painted, slightly imperfect, with brush-stroke variation
- The pet sits in the centerstage of the swirling sky — it IS the painting subject, not pasted on top
- Mood: contemplative, mystical, gently dreamy (peaceful counterpoint to bypass)

**Symbolism**: this is the "thinking, asking for permission" state. The pet is calm, eyes soft, mouth small or closed. Even when it blinks/breathes, the energy stays meditative.

## 4. Style guide B — "bypass" idle (Russian Constructivism)

Reference: El Lissitzky, *Beat the Whites with the Red Wedge* (1919); Alexander Rodchenko propaganda posters. Search: <https://www.bing.com/images/search?q=El+Lissitzky+constructivism+poster>

What "Russian Constructivism style" means here:
- **Background**: bold geometric blocks of pure red, black, yellow, off-white; diagonal composition; sharp triangles and rectangles; sometimes large solid letterforms or stylized rays
- **Palette (strict)**: revolutionary red `#D60E1E`, deep black `#0F0F12`, pure yellow `#FCD600`, off-white `#E8E5D8`. Avoid blue, purple, green, pink — break the color rule and the style breaks.
- **Composition**: dynamic diagonals, asymmetric balance, propaganda-poster energy
- **Typography (optional)**: stencil/sans-serif Cyrillic-flavored block letters can appear as background design elements (e.g. fragments of "НА!"); do not write actual words in any natural language
- **No**: gradients, soft shadows, anti-aliasing on the geometric blocks. Hard edges only.

How 奶龙 inhabits this style:
- The pet is **holding a megaphone** in one stubby hand (megaphone is a constructivism trope — Mayakovsky/Rodchenko energy)
- Mouth wide open mid-shout/laugh — channel the "大笑奶龙" meme energy
- One fist often raised
- The pet is rendered with the same hard-edged geometric block treatment as the background — its outline is bold and flat, its yellow body is the same `#FCD600` as the background yellow blocks
- Mood: agitated, exuberant, revolutionary, slightly unhinged (this is the "I'll execute anything" state)

**Symbolism**: this is the "running with permission off" state. The pet is shouting, gesturing, full action. Visual energy is loud.

## 5. The transitions

Two 6-frame sequences that morph the canvas content between style A and style B. They play in 600 ms.

### `trans_to_bypass_*` (frames 00 → 05): accept → bypass

A cathartic break. The Van Gogh world fractures and the Constructivism world bursts through.

- **00**: identical to `accept_idle_00.png` (continuity start)
- **01**: thin glass-like cracks appear across the starry sky background
- **02**: cracks widen; the swirling sky begins to fragment into shards; the pet's expression starts shifting (mouth beginning to open)
- **03**: shards of starry sky flying outward; red and yellow geometric blocks erupting from the cracks; pet's mouth opens mid-laugh
- **04**: starry-night fragments mostly gone; red/black/yellow blocks fill 80% of the frame; megaphone materializes in the pet's hand
- **05**: identical to `bypass_idle_00.png` (continuity end)

### `trans_to_accept_*` (frames 00 → 05): bypass → accept

A calming dissolve. The propaganda poster softens back into a painting.

- **00**: identical to `bypass_idle_00.png`
- **01**: hard edges of constructivism blocks begin to soften; megaphone starts to dematerialize
- **02**: geometric blocks dissolving into curved brushstrokes
- **03**: brushstrokes coalescing into a swirling sky pattern; red fading toward navy
- **04**: starry sky 80% formed; pet's expression calming
- **05**: identical to `accept_idle_00.png`

**Critical**: frames `*_00` and `*_05` MUST be pixel-identical to the corresponding idle frames they bookend. The Python animator concatenates them seamlessly — any mismatch will visually pop. Easiest way: copy the existing idle frame for those bookend slots.

## 6. The idle animations, choreographed

### `accept_idle_00..07` — Van Gogh breathing (2 s loop)

The pet breathes gently and blinks once per loop.

| Frame | Pose |
|---|---|
| 00 | neutral, eyes open, looking forward, slight lean left |
| 01 | inhaling, chest slightly expanded, eyes open |
| 02 | peak inhale, body slightly taller |
| 03 | starting to exhale, eyes half-closed (blink frame 1) |
| 04 | eyes fully closed (blink frame 2) |
| 05 | eyes opening (blink frame 3) |
| 06 | mid-exhale, eyes open |
| 07 | almost back to neutral, slight lean right |

The Van Gogh swirls behind the pet should also subtly shift — the sky in 00 and 04 can be in slightly different stroke positions to give the background life.

### `bypass_idle_00..07` — Constructivism shout cycle (2 s loop)

The pet shouts through a megaphone, fist pumping.

| Frame | Pose |
|---|---|
| 00 | megaphone raised, mouth half-open, fist starting to rise |
| 01 | mouth opens wider, fist higher |
| 02 | mouth at max, fist at chest height |
| 03 | peak shout — head tilted slightly back, mouth fully open, fist at face height |
| 04 | beginning to ease, mouth wide but lowering, fist still raised |
| 05 | mouth closing partway, fist dropping |
| 06 | smirk/sneer mid-frame, fist near chest |
| 07 | resetting to start, mouth half-open, fist down — loops back to 00 |

The background constructivism blocks can pulse subtly — e.g. a yellow diagonal block can shift position slightly across frames to add motion energy.

## 7. Working order (recommended)

If you want to deliver in batches for review:

- **Phase 1 (16 frames)**: all idle frames (`accept_idle_*` and `bypass_idle_*`). Lets the human check that both styles land before you commit to transitions.
- **Phase 2 (12 frames)**: both transition sequences.

Bookend frames in Phase 2 (`trans_to_bypass_00`, `trans_to_bypass_05`, `trans_to_accept_00`, `trans_to_accept_05`) are byte-identical copies of existing idle frames — just `cp` them, don't re-generate.

## 8. Iteration protocol

If the human asks for a redo on a frame:
- Keep the rest of the set, only re-generate the named frame(s)
- Maintain pose continuity with neighboring frames in the same loop
- Don't change the character bible mid-project

If a frame's filename collides with an existing file, overwrite without asking.

## 9. Quality bar (self-check before declaring done)

- [ ] All 28 files present in `assets/`, exactly named per spec
- [ ] All 128×128 PNG with alpha
- [ ] Character is recognizably 奶龙 (chubby yellow round body, big head, short limbs)
- [ ] Style A frames feel like a Van Gogh painting (visible impasto strokes, swirling sky, dreamy)
- [ ] Style B frames feel like a Lissitzky poster (hard edges, red/black/yellow only, megaphone, agitated)
- [ ] Idle loops are choreographically coherent (00 and 07 close enough to loop seamlessly)
- [ ] Transition bookend frames match their idle counterparts
- [ ] No anti-aliasing halos, no watermarks, no extraneous text

## 10. When you're done

Commit the 28 PNGs in a single commit:
```
git add assets/
git commit -m "feat(assets): generate 28-frame sprite sheet"
git push
```

Then write a one-paragraph PR description summarizing what you generated and any judgment calls you made. The human will run the desktop pet against your output and ping you for any frames that don't read right.

See `codex/prompts.md` for the specific image-2 prompt for each of the 28 frames.
