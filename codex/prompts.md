# image-2 prompts — 144 frame v3 (mirror scene @ 192×240, 12 FPS idle, 20 FPS transition)

Read `codex/brief.md` first for character bibles + scene + lighting. Each prompt below assumes you've internalized those.

**Universal context for every frame** (don't restate in every prompt — keep it in your image-2 system context):
- **192 × 240 px portrait** PNG with alpha; transparent outside the bathroom view
- Modern pixel-illustration style (semi-detailed shading, not 8-bit chunky, not photoreal)
- Camera fixed: bathroom mirror centered (mirror occupies roughly x=14..178 / y=22..180); sink edge fills bottom ~60 px; thin fluorescent strip glare at top ~22 px; hairline crack in mirror's upper-right corner; toothbrush in glass + pink soap bar + crumpled tissue tucked into bottom corners
- Image-2 will refuse direct actor names → use feature descriptions (jawline, hair, scar, wardrobe, posture); your v2 prompts on `codex/generate-mirror-sprite-assets` branch already worked, reuse that language
- **All sprite frames must scale-down gracefully** from the v2 (256×320) look without losing readability

---

## Frame structure (keyframes + tweens)

For each idle loop you generate **10 keyframes** (every 6th frame) with full pose detail, then **5 tween frames per gap** that interpolate small pose deltas. The tween prompts are brief because they ride on keyframe context.

---

## Phase 1A — accept_idle keyframes (Jack, 10 frames)

**Shared style prompt for Phase 1A** (paste into every Phase 1A frame):

> Pixel-art bathroom-mirror scene, 192×240 portrait, transparent background outside the bathroom view. Subject: a thin slightly hunched man in his early 30s, short mid-brown hair parted to the side, pale skin with prominent dark circles under tired eyes, mild stubble, sunken cheeks, wearing a rumpled white dress shirt with a dark loose tie hanging 2 inches lower than the collar. Cool fluorescent overhead lighting, slightly green-shifted shadows, low contrast — 90s public-restroom mood. Bathroom layout: thin metal mirror frame with hairline crack in upper-right corner, sink edge visible at bottom, toothbrush in glass + bar of pink soap in bottom corners.

### Keyframes

#### `accept_idle_00` — rest pose (loop start)
> Both hands on the sink rim (just visible at the very bottom of the mirror as the tops of his hands). Head bowed, looking down at running water. Reflection shows top of head and slumped shoulders. Mouth neutral, eyes hidden by head bow.

#### `accept_idle_06` — head fully raised
> Head now upright, eyes meeting his own reflection — tired, blank, no expression. Hands no longer on rim (dropped below mirror). Shoulders still slumped.

#### `accept_idle_12` — held stare
> Same as frame 06 but eyes locked on own reflection, holding the stare. Tiny micro-tilt of head (1 px right).

#### `accept_idle_18` — pre-blink
> Eyes 30% closed, beginning to droop. Mouth still neutral.

#### `accept_idle_24` — full blink
> Eyes fully closed. Mouth still neutral. Body held in place.

#### `accept_idle_30` — cupped hands rising
> Cupped hands have just risen into the bottom of the mirror, holding a small pool of water. Head bowed slightly toward hands. Eyes open again but tired.

#### `accept_idle_36` — mid-splash
> Jack throws water at his face. Visible droplets flying outward; a few droplets cling to mirror surface. Eyes shut tight against water. Hands open against face.

#### `accept_idle_42` — hands at face dripping
> Hands held against face. Water dripping from his chin. Eyes still mostly closed.

#### `accept_idle_48` — hands dropping
> Hands dropping back below the mirror. Water still slowly dripping. Eyes half-open, returning to neutral exhausted state.

#### `accept_idle_54` — pre-rest
> Hands back on sink rim. Head beginning to bow again. Eyes nearly closed (just heavy lids). Body resetting toward frame 00.

### Phase 1A tweens (50 frames total — short blocks)

For each frame N between keyframes, generate a near-identical-to-neighbor frame with a 1-2 pixel pose delta. Block instructions:

- **Frames 01-05** (rest hold): nearly identical to frame 00. Micro pose drift only — head tilts 1 px right at frame 02, then 1 px back left at frame 04. Hands stay on rim. Eyes hidden.
- **Frames 07-11** (head rising mid-arc): linear interpolation between frame 06 (head fully raised, eyes open) and frame 12 (held stare). Each frame the head rises slightly more / eyes open a bit more. No big change.
- **Frames 13-17** (held stare with breath): nearly identical to frame 12. Tiny shoulder rise+fall over the 5 frames (subtle breath). Eyes locked.
- **Frames 19-23** (eyelids descending): linear interp between frame 18 (eyelids 30% closed) and frame 24 (fully closed). Each frame 15% more closed.
- **Frames 25-29** (eyelids reopening): linear interp between frame 24 (fully closed) and frame 30 (open with cupped hands rising). Eyelids opening, hands beginning to enter from below in last 2 frames.
- **Frames 31-35** (hands moving to face): interp between frame 30 (cupped hands holding water) and frame 36 (mid-splash). Hands rising toward face, water beginning to release at frame 34-35.
- **Frames 37-41** (splash settling): interp between frame 36 (mid-splash, droplets flying) and frame 42 (hands at face, dripping). Droplets falling, hands settling.
- **Frames 43-47** (face wash dwell): interp between frame 42 and frame 48. Water continuing to drip. Tiny finger movements.
- **Frames 49-53** (returning to rest): interp between frame 48 (hands dropping) and frame 54 (pre-rest). Hands returning to sink rim, head beginning to bow.
- **Frames 55-59** (final settle): interp between frame 54 (pre-rest) and frame 00 (rest). Head bowing further, eyes finishing close, hands settling on rim.

---

## Phase 1B — bypass_idle keyframes (Tyler, 10 frames)

**Shared style prompt for Phase 1B** (paste into every Phase 1B frame):

> Pixel-art bathroom-mirror scene, 192×240 portrait, transparent background outside the bathroom view. Subject: a lean wiry sculpted man in his early 30s with confident upright posture and weight on his right hip, peroxide-bleached blonde hair slightly disheveled with darker roots, longer than corporate, late-90s grunge cut, sharp angular jawline, mild stubble, small white diagonal scar across the chin, prominent cheekbones, smug crooked smirk on the right side of his mouth, hooded knowing eyes. Wearing an open red leather jacket over a stained cream ribbed undershirt. Same bathroom as the Phase 1A frames — same mirror frame with hairline crack in upper-right, same sink + toothbrush + soap details — but the lighting has shifted to warm orange tungsten, hard shadows with golden tint, high contrast. A cigarette in the LEFT corner of his mouth (his left = viewer's right).

### Keyframes

#### `bypass_idle_00` — base swagger (loop start)
> Hands at his sides (left thumb hooked in belt loop). Smug crooked smirk. Unlit cigarette in left corner of mouth. Looking slightly off-camera toward viewer's left, hooded eyes.

#### `bypass_idle_06` — head tilt, smirk widens
> Head tilted 2 px to his right (viewer's left). Smirk widens by 1 px. Otherwise same as frame 00.

#### `bypass_idle_12` — lighting cigarette
> Right hand raised to mouth, holding a small zippo lighter. Tiny orange spark at the cigarette tip — just lit. Eyes slightly squinted.

#### `bypass_idle_18` — drag
> Cigarette tip glowing hot orange-red (2-3 px bright orange dot). Eyes squinted with the inhale. Chest expanded by 1-2 px. Right hand still near mouth.

#### `bypass_idle_24` — exhale (FOURTH WALL: smoke top)
> **Smoke billowing in front of face, the topmost wisp EXITS THE CANVAS TOP EDGE (y=0, clipped clean).** Eyes hooded, looking up. Mouth open slightly to exhale.

#### `bypass_idle_30` — smug grin max
> Smoke mostly cleared, just a faint residual wisp at top. Smirk now at maximum width. Right hand back at side, cigarette returned to mouth corner. Looking back at viewer.

#### `bypass_idle_36` — reaching begins
> Right hand starting to extend forward, breaking the plane of the mirror at the wrist. Hand still mostly within the mirror's frame but visibly emerging.

#### `bypass_idle_42` — **FOURTH WALL: hand out right** (money frame)
> **Right hand fully extended past the mirror's right edge, past the sink, AND CLIPPED OUT THE CANVAS RIGHT EDGE (x=192).** Hand is closer to camera, palm slightly open in a "come here" / "you see me?" gesture. Smug grin held. Cigarette in mouth corner.

#### `bypass_idle_48` — hand retreating
> Hand pulling back toward mirror. Wrist now at the mirror's right edge, fingers still slightly past. Smirk held.

#### `bypass_idle_54` — pre-reset
> Hand returned to inside mirror, settling down to his side. Smirk relaxing slightly toward base pose. Cigarette in mouth corner.

### Phase 1B tweens (50 frames total — short blocks)

- **Frames 01-05** (base hold): nearly identical to frame 00. Head/shoulder 1 px micro shifts. Eyes locked.
- **Frames 07-11** (cigarette lifting): interp between frame 06 (smirk wider, head tilt) and frame 12 (lighter spark). Right hand rising toward mouth, lighter coming up.
- **Frames 13-17** (drag building): interp between frame 12 (just lit) and frame 18 (full drag). Cigarette tip glow brightening, eyes squinting more.
- **Frames 19-23** (exhale beginning): interp between frame 18 (drag) and frame 24 (smoke clearing top). Smoke starting to emerge frame by frame, expanding upward.
- **Frames 25-29** (smoke clearing): interp between frame 24 (smoke at top edge) and frame 30 (smug grin max). Smoke dissipating, smirk re-emerging.
- **Frames 31-35** (pre-reach): interp between frame 30 (smug max) and frame 36 (reaching begins). Right hand starting to lift from side.
- **Frames 37-41** (extending arm): interp between frame 36 (reach starting) and frame 42 (hand fully out canvas right). Arm extending more each frame, hand getting closer to camera, perspective slightly enlarging.
- **Frames 43-47** (hand held out): interp between frame 42 (full extension) and frame 48 (retreat starting). Hand held in space — slight finger flex, slight forearm sway.
- **Frames 49-53** (retracting): interp between frame 48 (wrist at mirror edge) and frame 54 (back at side). Arm retracting smoothly.
- **Frames 55-59** (final settle): interp between frame 54 (pre-reset) and frame 00 (base swagger). Posture settling, smirk returning to base width.

---

## Phase 2 — transition keyframes (24 frames total)

Transitions are short (0.6 s @ 20 FPS = 12 frames) so I'll write each frame as a quasi-keyframe.

### trans_to_bypass (Jack → Tyler, 12 frames)

#### `trans_to_bypass_00`
> **DO NOT GENERATE — copy `accept_idle_00.png` verbatim.** Bookend.

#### `trans_to_bypass_01`
> Same as accept_idle_00 (Jack head bowed at sink), but he has JERKED his head up. Reflected eyes wide — startled. Lighting still cool fluorescent. Hair still brown. Posture frozen mid-startle.

#### `trans_to_bypass_02`
> Same as frame 01 but a faint **blood-red glow** appearing at the silhouette edge of his reflection (1-2 px red along outline).

#### `trans_to_bypass_03`
> Hair tips beginning to lighten to peroxide-yellow (yellow ends, brown middle). Jawline sharpening 1-2 px. Dress shirt collar starting to open. Lighting starting to warm.

#### `trans_to_bypass_04`
> Hair more peroxide (50%). Jaw fully sharp. Smirk hinting at right corner of mouth. Red leather glow at the shoulder edge of the reflection (jacket starting to materialize).

#### `trans_to_bypass_05`
> Half-and-half vertical split. Left half of reflection still Jack (brown hair, white shirt collar, tired left eye). Right half Tyler (peroxide right side, red leather right shoulder/sleeve, sharp jaw, smirk on right side). Lighting half cool / half warm gradient down the middle.

#### `trans_to_bypass_06`
> Split more advanced — Tyler taking over the right 60% of the reflection. Cigarette beginning to materialize in the mouth corner.

#### `trans_to_bypass_07`
> Tyler taking over 80% of the reflection. Only narrow strip of Jack-tired-eye darkness left on the far left. Red leather fully on. Cigarette in mouth.

#### `trans_to_bypass_08`
> Reflection nearly fully Tyler. Hair fully peroxide. Lighting fully warm. Smirk in place. Only tiniest residue of dark circles around eyes.

#### `trans_to_bypass_09`
> Tyler fully formed in the reflection. Posture locked. Smirk at base width. Cigarette unlit in mouth corner.

#### `trans_to_bypass_10`
> Essentially identical to bypass_idle_00 but with the tiniest possible residual cool-light tint at the edges, fading. Functions as the last morph beat before bookend.

#### `trans_to_bypass_11`
> **DO NOT GENERATE — copy `bypass_idle_00.png` verbatim.** Bookend.

### trans_to_accept (Tyler → Jack, 12 frames)

#### `trans_to_accept_00`
> **DO NOT GENERATE — copy `bypass_idle_00.png` verbatim.** Bookend.

#### `trans_to_accept_01`
> Tyler base pose as frame 00, but the smug smirk WAVERS — mouth shape less confident, eyes losing the hooded knowing quality. Cigarette in mouth goes out (no glow). Slight cool-gray creeping in at the silhouette edges.

#### `trans_to_accept_02`
> Smirk continuing to fade toward neutral mouth. A faint cool-gray halo at silhouette edge.

#### `trans_to_accept_03`
> Red leather jacket edges starting to dissolve/dither. Peroxide hair beginning to desaturate toward darker brown roots. Shoulders dropping by 1 px.

#### `trans_to_accept_04`
> Hair 50% reverted to brown. Leather jacket fully softening, white dress shirt collar appearing underneath in faint outline. Lighting starting to cool.

#### `trans_to_accept_05`
> Half-and-half vertical split (reverse of trans_to_bypass_05). Right half still Tyler (red leather right sleeve, peroxide right side, smirk on right). Left half becoming Jack (white dress shirt left sleeve, brown hair on left, dark circle reappearing under left eye, slumped shoulder).

#### `trans_to_accept_06`
> Split more advanced — Jack taking over the left 60%. Loose tie appearing. Posture noticeably slumped.

#### `trans_to_accept_07`
> Jack taking over 80%. Only narrow strip of red leather and peroxide on the far right. Mouth in neutral exhausted line.

#### `trans_to_accept_08`
> Reflection nearly fully Jack. Dress shirt back on with loose tie. Brown hair restored. Dark circles forming under both eyes. Posture slumped.

#### `trans_to_accept_09`
> Jack fully formed in reflection. Only residual peroxide tint at very tips of hair, fading. Lighting fully cool fluorescent.

#### `trans_to_accept_10`
> Essentially identical to accept_idle_00, with the tiniest residual warm-light tint at edges, fading. Last morph beat before bookend.

#### `trans_to_accept_11`
> **DO NOT GENERATE — copy `accept_idle_00.png` verbatim.** Bookend.

---

## Output checklist

After generating, verify `assets/` contains exactly:

```
accept_idle_00.png  ... accept_idle_59.png        (60 files)
bypass_idle_00.png  ... bypass_idle_59.png        (60 files)
trans_to_bypass_00.png ... trans_to_bypass_11.png (12 files)
trans_to_accept_00.png ... trans_to_accept_11.png (12 files)
```

**144 files total. Each 192 × 240 PNG with alpha.** The four `_00` and `_11` bookend frames in transitions are byte-identical copies of the corresponding idle frame.

Run a quick sanity check before opening the PR:

```bash
ls assets/ | wc -l  # must be 144
python -c "from PIL import Image; [print(f, Image.open(f'assets/{f}').size) for f in sorted(__import__('os').listdir('assets'))]" | grep -v "(192, 240)"
# Above must produce no output (every file 192x240)
```
