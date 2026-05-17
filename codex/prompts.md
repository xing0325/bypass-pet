# image-2 prompts — 28 frame-by-frame

Read `codex/brief.md` first for the character bible and the two style guides. Each prompt below assumes you've internalized those rules; the prompts only call out the per-frame variations.

All frames share these implicit requirements:
- 128×128 pixels, PNG, fully transparent background outside the sprite silhouette
- Subject: **奶龙** — chubby Chinese-cartoon yellow dragon, big head, short limbs, large eyes
- Composition: subject centered, feet at approximately the same y-coordinate across frames in the same loop

If image-2 produces a frame with the wrong dimensions or an opaque background, downscale/composite to spec before saving. Filenames are strict — match exactly.

---

## Phase 1A — accept_idle (8 frames, Van Gogh Starry Night style)

**Shared style prompt (paste into all Phase 1A frames)**:

> Van Gogh *Starry Night* style oil painting. Background: deep cobalt and cerulean blue swirling sky with thick visible impasto brushstrokes, a luminous golden-yellow moon glow at top-right, small bright yellow stars with halo rings, dark cypress-green accents. The entire image rendered with short curved comma-strokes, post-impressionist palette. Subject is rendered IN this style, painted with the same brushstroke language — not pasted on top. The yellow body has visible directional comma-strokes. Imperfect painted outline.

**Per-frame additions**:

### `accept_idle_00.png`
> Subject: 奶龙 (chubby yellow Chinese cartoon dragon, big head, short stubby limbs, large round eyes with white highlights) standing in neutral pose, mouth closed in a soft small smile, body leaning very slightly to its left, eyes open and gentle, looking forward.

### `accept_idle_01.png`
> Same pose as previous frame but inhaling — chest slightly expanded, body 2 pixels taller, mouth still closed, eyes open.

### `accept_idle_02.png`
> Peak inhale — body at tallest, chest puffed, mouth still closed, eyes open, contemplative.

### `accept_idle_03.png`
> Starting to exhale, body relaxing, eyes half-closed (blink in progress, eyelids 50% down), mouth still in small smile.

### `accept_idle_04.png`
> Eyes fully closed (peaceful blink frame), body neutral height, mouth small smile.

### `accept_idle_05.png`
> Eyes 50% open (blink ending), body still relaxed, mouth small smile.

### `accept_idle_06.png`
> Mid-exhale, eyes fully open, body slightly shorter than neutral, looking forward.

### `accept_idle_07.png`
> Almost back to neutral, body leaning very slightly to its right (mirror of frame 00's lean), eyes open. This frame should loop seamlessly back to frame 00.

---

## Phase 1B — bypass_idle (8 frames, Russian Constructivism style)

**Shared style prompt (paste into all Phase 1B frames)**:

> Russian Constructivism propaganda poster style, El Lissitzky and Rodchenko aesthetic. Background: bold geometric blocks of pure revolutionary red `#D60E1E`, deep black `#0F0F12`, pure yellow `#FCD600`, and off-white `#E8E5D8` — no other colors permitted. Sharp diagonal composition, hard edges, no gradients, no anti-aliasing on the blocks. Stencil/sans-serif Cyrillic-flavored block letterforms can appear as background design fragments. Subject is rendered with the same hard-edged geometric block treatment — yellow body in same `#FCD600` as background blocks, bold flat outline.

**Per-frame additions**:

### `bypass_idle_00.png`
> Subject: 奶龙 (chubby yellow dragon) holding a stylized megaphone in its right stubby hand pointing up-right at 45°. Mouth half-open mid-shout. Left fist starting to rise to chest level. Standing on a diagonal red block. Background: bold black + yellow geometric blocks behind.

### `bypass_idle_01.png`
> Same character, mouth opens wider, left fist rising to shoulder height. Megaphone still raised. Background blocks slightly shifted (a yellow diagonal sliver enters from the right).

### `bypass_idle_02.png`
> Mouth at maximum width, left fist at chest height pulled back, megaphone raised, head slightly forward. Background blocks darker on right side.

### `bypass_idle_03.png`
> Peak shout — head tilted slightly back, mouth fully open showing teeth/inside-mouth in `#D60E1E` red, left fist at face height in a strong pump, megaphone aimed up. Maximum action energy.

### `bypass_idle_04.png`
> Easing from peak — mouth still wide but lowering, head returning forward, fist still raised but slightly relaxing.

### `bypass_idle_05.png`
> Mouth partially closing, fist dropping toward chest. Body starting to reset.

### `bypass_idle_06.png`
> Smirk/sneer mid-frame — mouth small but cocky, fist near chest, megaphone slightly lowered. Smug interlude.

### `bypass_idle_07.png`
> Almost back to start pose — mouth half-open ready to shout again, fist low, megaphone half-raised. This frame should loop seamlessly back to frame 00.

---

## Phase 2A — trans_to_bypass (6 frames, cross-fade from A to B)

This sequence breaks the Van Gogh world and bursts into the Constructivism world. Plays in 600 ms.

### `trans_to_bypass_00.png`
> **DO NOT GENERATE — copy `accept_idle_00.png` verbatim.** Continuity start.

### `trans_to_bypass_01.png`
> Van Gogh starry-night sky as in `accept_idle_00`, but thin glass-like cracks (white-and-cobalt jagged lines) appear across the sky background. The 奶龙 still in soft-smile pose, eyes wider with surprise. Style is still 95% Van Gogh.

### `trans_to_bypass_02.png`
> Cracks widen into visible fissures. Sky behind the pet beginning to fragment into shards. The pet's mouth starting to open. Van Gogh swirls partially visible but interrupted by sharp angular gaps.

### `trans_to_bypass_03.png`
> Shards of starry sky flying outward from the center. Red and yellow Constructivism geometric blocks erupting from the cracks behind/beside the pet. The pet's mouth is opening mid-laugh, eyes shifting from soft to wild. The style is hybrid — half painted strokes, half hard-edged blocks.

### `trans_to_bypass_04.png`
> Starry-night fragments mostly gone. Red, black, yellow blocks now fill 80% of the frame. A megaphone materializes in the pet's right hand (drawn with some lingering painted edges that are sharpening into hard outlines). Pet's expression is now nearly the Constructivism shout pose.

### `trans_to_bypass_05.png`
> **DO NOT GENERATE — copy `bypass_idle_00.png` verbatim.** Continuity end.

---

## Phase 2B — trans_to_accept (6 frames, cross-fade from B to A)

This sequence softens the propaganda poster back into a painting. Plays in 600 ms.

### `trans_to_accept_00.png`
> **DO NOT GENERATE — copy `bypass_idle_00.png` verbatim.** Continuity start.

### `trans_to_accept_01.png`
> Constructivism scene as in `bypass_idle_00`, but the hard edges of the geometric blocks begin to soften — edges slightly painterly. The megaphone starts to dissolve at its tip into faint brushstrokes. The pet's shouting mouth is closing slightly.

### `trans_to_accept_02.png`
> Geometric blocks dissolving into curved comma-shaped brushstrokes around the edges. Red is shifting toward warmer painted-red tones. Pet's expression is calming.

### `trans_to_accept_03.png`
> Brushstrokes coalescing into a swirling sky pattern in the background. The remaining red blocks are now small painterly fragments. Megaphone almost gone. Yellow background block softening to a yellow Van Gogh moon glow forming.

### `trans_to_accept_04.png`
> Starry sky 80% formed, just a few painted-red flecks left as residue. Pet's expression mostly calm, eyes returning to soft Van Gogh state. Style is 90% Van Gogh.

### `trans_to_accept_05.png`
> **DO NOT GENERATE — copy `accept_idle_00.png` verbatim.** Continuity end.

---

## Output checklist

After generating, verify in `assets/`:

```
accept_idle_00.png  accept_idle_01.png  accept_idle_02.png  accept_idle_03.png
accept_idle_04.png  accept_idle_05.png  accept_idle_06.png  accept_idle_07.png
bypass_idle_00.png  bypass_idle_01.png  bypass_idle_02.png  bypass_idle_03.png
bypass_idle_04.png  bypass_idle_05.png  bypass_idle_06.png  bypass_idle_07.png
trans_to_bypass_00.png  trans_to_bypass_01.png  trans_to_bypass_02.png
trans_to_bypass_03.png  trans_to_bypass_04.png  trans_to_bypass_05.png
trans_to_accept_00.png  trans_to_accept_01.png  trans_to_accept_02.png
trans_to_accept_03.png  trans_to_accept_04.png  trans_to_accept_05.png
```

28 files total. Each 128×128 PNG with alpha channel. The four `_00` and `_05` bookend frames in the transitions are byte-identical copies of the corresponding idle frame.
