# image-2 prompts — 28 frame-by-frame

Read `codex/brief.md` first for the character bibles (Jack the Narrator, Tyler Durden) and the lighting/palette rules. Each prompt below assumes you've internalized those rules; the prompts only call out the per-frame variations.

All frames share these implicit requirements:
- 128×128 pixels, PNG, fully transparent background outside the sprite silhouette
- Pixel-art aesthetic with visible pixel grain; not photoreal, not vector-smooth
- Composition: subject centered, feet anchored at the same y-coordinate across frames within a loop
- No real-actor likenesses — render the character's TRAITS, not a specific person's face

If image-2 produces a frame with the wrong dimensions or an opaque background, downscale/composite to spec before saving. Filenames are strict — match exactly.

---

## Phase 1A — accept_idle (8 frames, Jack the tired Narrator)

**Shared style prompt (paste into all Phase 1A frames)**:

> Pixel-art portrait, 128×128, transparent background. Subject is a tired insomniac office worker in his early 30s, average build with slightly hunched shoulders. Hair: short, mid-brown, neat but limp. Face: dark circles under the eyes, mild stubble, slightly sunken cheeks, mouth in a flat neutral line. Clothes: wrinkled white dress shirt, dark loosened tie hanging 2 inches lower than the collar, dark slacks. Lighting: cool fluorescent office light, slightly green-shifted shadows, low contrast. Desaturated palette — bone white, dusty beige, sage-gray, navy tie, brown hair, plum under-eye shadow. Visible pixel grain. No saturated red/yellow/orange. No glasses unless stated.

**Per-frame additions**:

### `accept_idle_00.png`
> Pose: standing slouched, weight evenly on both feet, arms hanging slightly inward at sides (or right hand loosely holding a beige paper coffee cup with a sip-lid). Eyes half-open and looking forward, mouth a flat line. This is the neutral baseline pose.

### `accept_idle_01.png`
> Same pose as previous frame, beginning a shallow breath in. Shoulders rise by 1 pixel. Eyes unchanged.

### `accept_idle_02.png`
> Peak inhale. Body posture 1 pixel taller than frame 00 but still hunched. Eyes still half-open.

### `accept_idle_03.png`
> Starting to exhale. Shoulders dropping back to baseline. Eyes drooping further — eyelids now at 60% closed.

### `accept_idle_04.png`
> Maximum eye droop — eyelids at 90% closed, this is a fatigue-droop NOT a peaceful blink. Mouth still neutral. Body baseline pose. He looks like he might fall asleep standing up.

### `accept_idle_05.png`
> Eyes opening back to half-open. Head tilted 2 pixels to his left (the viewer's right). Mouth neutral.

### `accept_idle_06.png`
> Small yawn — mouth open 3-4 pixels wide showing a dark oval of mouth interior. Eyes squinting (eyelids 70% closed). Head tilted back by 1 pixel.

### `accept_idle_07.png`
> Yawn ending — mouth closing, almost back to neutral line. Eyes returning to half-open. Body returning to frame-00 pose. This frame should loop seamlessly back to frame 00.

---

## Phase 1B — bypass_idle (8 frames, Tyler Durden)

**Shared style prompt (paste into all Phase 1B frames)**:

> Pixel-art portrait, 128×128, transparent background. Subject is a charismatic anarchist anti-hero in his early 30s with a lean wiry sculpted build, confident upright posture, weight on his right hip. Hair: peroxide-bleached blonde, longer than corporate, slightly disheveled, late-90s grunge. Face: sharp jawline, mild stubble, small white scar across the chin, smug crooked smirk, hooded knowing eyes. Clothes: red leather jacket open over a stained cream ribbed undershirt (or bare chest with sculpted abs, your choice — pick one and stay consistent across the 8 frames). Dark vintage suit pants or black jeans. Lighting: warm tungsten basement light, hard shadows with golden-orange tint, high contrast. Palette: blood red leather, oxblood shadows, black, dirty cream, peroxide yellow hair, warm-tan skin. Strict red-black-cream dominance. Visible pixel grain. A cigarette protrudes from the corner of his mouth in most frames.

**Per-frame additions**:

### `bypass_idle_00.png`
> Pose: standing with weight on right hip, left hand in jacket pocket (or thumb hooked through belt loop), right hand at his side. Smug crooked smirk on the right side of his mouth. Unlit cigarette in the left corner of his mouth. Looking slightly off-camera toward the viewer's left, eyes hooded. This is the neutral swagger pose.

### `bypass_idle_01.png`
> Same pose, head tilts 2 pixels to his right (viewer's left), smirk widens by 1 pixel.

### `bypass_idle_02.png`
> Taking a drag on the cigarette — cigarette tip glows hot orange-red (a 2-pixel bright orange dot). Eyes squint slightly with the inhale. Chest expands by 1 pixel.

### `bypass_idle_03.png`
> Head tilts back by 2 pixels as he exhales. Mouth opens slightly. Eyes hooded, looking up. Chest still expanded.

### `bypass_idle_04.png`
> Small puff of light gray smoke visible in front of his face (an irregular 3-pixel-wide cloud above the mouth). Head back to baseline. Smirk returning. Cigarette settled in mouth corner again.

### `bypass_idle_05.png`
> Smug grin at maximum width. Right hand has come up to mid-chest level, holding the cigarette between index and middle fingers (cigarette now out of mouth in this frame). Eyes locked on viewer.

### `bypass_idle_06.png`
> Small chuckle — chest puffs out by 1 extra pixel, head shake by 1 pixel to his left. Cigarette held at chest. A faint smile-line crease at the corner of his eye.

### `bypass_idle_07.png`
> Back to baseline pose, cigarette returned to mouth corner, hand back at side, smug smirk reset. This frame should loop seamlessly back to frame 00.

---

## Phase 2A — trans_to_bypass (6 frames, Jack → Tyler morph)

This sequence is a dissociative split. Plays in 600 ms.

### `trans_to_bypass_00.png`
> **DO NOT GENERATE — copy `accept_idle_00.png` verbatim.** Continuity start.

### `trans_to_bypass_01.png`
> Same composition as Jack idle pose but Jack's eyes widen slightly (eyelids open to 80%), as if he's just caught his reflection in a window. A faint blood-red glow halos the silhouette edge — only 1-2 pixels of red along his outline. Office lighting still cool overall.

### `trans_to_bypass_02.png`
> Mid-morph. Hair: brown roots with the tips beginning to lighten to peroxide-yellow (yellow ends, brown middle). Jawline sharpening — face shape narrowing by 1-2 pixels. Dress shirt collar coming undone — top button gone, collar splaying open. A hint of smirk emerging at the right corner of the mouth. Lighting warming up — shadows shifting from green-gray toward warm-tan.

### `trans_to_bypass_03.png`
> Half-and-half split, vertically. Left half of the body still Jack (white dress shirt, brown hair, dark circles). Right half is becoming Tyler — red leather sleeve materialized over the right shoulder and arm, right side of the hair fully peroxide, right side of the face sharp-jawed and smirking. Eyes asymmetric — left eye still tired, right eye knowing.

### `trans_to_bypass_04.png`
> Tyler nearly formed. Red leather jacket fully on, hair fully peroxide-blonde, smirk landed, posture straightened. Only residual traces of Jack's dark circles still visible under the eyes. Cigarette not yet in mouth. Lighting warm tungsten.

### `trans_to_bypass_05.png`
> **DO NOT GENERATE — copy `bypass_idle_00.png` verbatim.** Continuity end.

---

## Phase 2B — trans_to_accept (6 frames, Tyler → Jack morph)

The fantasy fades, the drone returns. Plays in 600 ms.

### `trans_to_accept_00.png`
> **DO NOT GENERATE — copy `bypass_idle_00.png` verbatim.** Continuity start.

### `trans_to_accept_01.png`
> Tyler pose, but the smirk wavers — mouth shape less confident, eyes losing their hooded knowing quality. The cigarette in the mouth corner has gone out (no glow). Faint cool-gray edge starting at the silhouette outline.

### `trans_to_accept_02.png`
> Leather jacket dissolving at the edges — sleeves and lapels showing pixel-level erosion / dithering as if turning to dust. Hair desaturating — peroxide yellow shifting toward darker brown at the roots. Posture starting to deflate — shoulders dropping by 1 pixel.

### `trans_to_accept_03.png`
> Half-and-half. Right half of body still Tyler (red leather sleeve, peroxide right side of hair, smirk on right side). Left half is becoming Jack — white dress shirt sleeve, brown left side of hair, slumped shoulder, dark circle reappearing under the left eye.

### `trans_to_accept_04.png`
> Jack nearly back. Dress shirt fully on with loosened tie, brown hair restored, dark circles forming under both eyes, posture deflated. Only residual peroxide tint at the very tips of the hair. Lighting cooled to office-fluorescent green-gray.

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
