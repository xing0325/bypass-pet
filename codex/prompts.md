# image-2 prompts — 28 frame-by-frame (C / mirror-scene, v2)

Read `codex/brief.md` first for the character bibles (Jack the Narrator, Tyler Durden), the canvas composition (bathroom mirror + sink), and the fourth-wall device. Each prompt below assumes you've internalized those; the prompts only call out the per-frame variations.

**Universal requirements** (don't restate them in every prompt — keep them as context for image-2):
- **256 wide × 320 tall pixels**, PNG, transparent background outside the bathroom view
- **Pixel-art aesthetic** with modern semi-detailed shading (think *Octopath Traveler* / *Hyper Light Drifter* bust portrait), not 8-bit chunky, not photoreal
- **Camera fixed**: same bathroom mirror centered in canvas, same sink edge at bottom, same toothbrush + soap props at bottom corners, same hairline crack in upper-right corner of the mirror
- **Likeness target**: make the reflection look like the actual actor (Edward Norton for Jack, Brad Pitt for Tyler) at Fight Club (1999) era
- **Lighting changes between states**: Jack frames = cool green-shifted fluorescent / Tyler frames = warm orange tungsten

If image-2 produces a frame with the wrong dimensions or an opaque background, downscale/composite to spec before saving. Filenames are strict.

---

## Phase 1A — accept_idle (8 frames, Jack washes his face)

**Shared style prompt for Phase 1A**:

> Pixel-art bathroom-mirror scene, 256×320 portrait, transparent background outside the bathroom view. The viewer sees a bathroom mirror (thin metal frame, hairline crack in upper-right corner) reflecting a man, with the porcelain sink edge visible at the bottom of the canvas and a toothbrush in a glass + a bar of pink soap as small details in the bottom corners. The reflected man is the Narrator from *Fight Club* (1999), Edward Norton: thin, slightly hunched, short mid-brown hair parted to the side, pale skin with prominent dark circles under tired eyes, mild stubble, wearing a rumpled white dress shirt with a dark loose tie hanging 2 inches lower than the collar. Cool fluorescent overhead lighting, slightly green-shifted shadows, low contrast — 90s public-restroom mood. Modern pixel-illustration style, visible pixel grain but with semi-detailed shading and color depth.

**Per-frame variations**:

### `accept_idle_00.png`
> Pose: Jack stands at the sink, both hands gripping the sink rim (just visible at the very bottom of the mirror as the tops of his hands and forearms). Head bowed slightly, looking down at the running water — in the mirror we see the top of his head and his slumped shoulders. Reflection mostly shows the slope of his head and back of his neck.

### `accept_idle_01.png`
> Pose: Jack has just raised his head and is now looking directly at his own reflection. Eyes meet his own gaze — tired, blank, no expression. Shoulders still slumped. Hands no longer on sink rim (now hanging at his sides, below mirror).

### `accept_idle_02.png`
> Same composition as frame 01 but eyes 50% closed (starting to blink).

### `accept_idle_03.png`
> Eyes fully closed (mid-blink). Mouth still neutral.

### `accept_idle_04.png`
> Eyes 50% open again (blink ending).

### `accept_idle_05.png`
> Jack's cupped hands rise into view at the bottom of the mirror, holding a small pool of water. He's about to splash his face. Head bowed slightly toward his hands. Eyes still tired.

### `accept_idle_06.png`
> Mid-splash: Jack has thrown the water at his face. Small water droplets visible flying outward from his face; a few droplets cling to the mirror surface itself. Eyes shut tight against the water. Hands open against face.

### `accept_idle_07.png`
> Hands dropping back below the mirror. Water dripping from his chin (small droplets falling). Eyes still half-closed, returning to neutral. This frame should loop seamlessly back to frame 00.

---

## Phase 1B — bypass_idle (8 frames, Tyler grins and smokes)

**Shared style prompt for Phase 1B**:

> Pixel-art bathroom-mirror scene, 256×320 portrait, transparent background outside the bathroom view. Same bathroom as before (mirror with hairline crack upper-right, sink edge at bottom, toothbrush + soap details). The reflection now shows Tyler Durden from *Fight Club* (1999), Brad Pitt: lean and sculpted (visible chiseled chest if jacket open), confident upright posture with weight on his right hip, peroxide-bleached blonde hair (longer than the Narrator's, slightly disheveled, dark roots showing), sharp angular jawline, mild stubble, a small white diagonal scar across the chin, prominent cheekbones, smug crooked smirk on the right side of his mouth, hooded knowing eyes. Wearing his signature open red leather jacket over a stained cream ribbed undershirt. Lighting has shifted to warm orange tungsten — hard shadows with golden tint, high contrast. The crack in the mirror catches the warm light. A cigarette in the corner of his mouth.

**Per-frame variations**:

### `bypass_idle_00.png`
> Pose: Tyler stands in the mirror, hands at his sides, weight on right hip, smug crooked smirk, unlit cigarette in the LEFT corner of his mouth (his left = viewer's right because mirror), looking slightly off-camera toward viewer's left, eyes hooded. Base swagger pose.

### `bypass_idle_01.png`
> Same pose but head tilts 2 px to his right (viewer's left). Smirk widens by 1 pixel.

### `bypass_idle_02.png`
> Tyler raises his right hand to the cigarette, holding a small zippo lighter. Tiny orange spark visible at the cigarette tip — he's just lit it. Eyes squinted slightly.

### `bypass_idle_03.png`
> Tyler takes a drag — cigarette tip glowing hot orange-red (2-3 px bright orange dot at the cigarette's tip), eyes squinted with the inhale, chest expanded by 1-2 px. Hand still near mouth.

### `bypass_idle_04.png`
> Tyler exhales — a billow of gray-white smoke in front of his face. The smoke rises and the topmost wisp EXTENDS ABOVE THE MIRROR FRAME and the topmost few pixels of smoke EXIT THE CANVAS TOP EDGE at y=0 (clipped clean). Eyes hooded looking up slightly.

### `bypass_idle_05.png`
> Smoke clearing, just a few residual wisps. Smirk returns to maximum width. Right hand back at side. Cigarette held between index and middle fingers near chest.

### `bypass_idle_06.png`
> **The signature 4th-wall frame.** Tyler reaches his right hand TOWARD THE VIEWER. The arm extends past the mirror's right edge, past the sink, and his hand and forearm CLIP CLEANLY OUT THE CANVAS RIGHT EDGE at x=256. The hand is closer to camera, slightly larger than perspective realism would dictate — palm open or fingers extended in a "come here" / "you see me?" gesture. His face still in the mirror, smug. Cigarette in mouth corner.

### `bypass_idle_07.png`
> Hand retreats back into the mirror, returning to base swagger pose. Cigarette settled in mouth corner again. Smirk reset to base. Should loop seamlessly back to frame 00.

---

## Phase 2A — trans_to_bypass (Jack → Tyler in mirror, 6 frames, 600 ms)

### `trans_to_bypass_00.png`
> **DO NOT GENERATE — copy `accept_idle_00.png` verbatim.** Continuity start.

### `trans_to_bypass_01.png`
> Jack at the sink as in frame 00, but he has just jerked his head UP. His reflected eyes are wide — he sees something wrong. Lighting still cool fluorescent. Hair still brown. Dress shirt still on. Posture frozen mid-startle.

### `trans_to_bypass_02.png`
> The reflection diverges from Jack's body. The reflected hair begins lightening at the tips — peroxide creeping in. Reflected jawline sharpening by 1-2 pixels. Bathroom lighting mid-shift: shadows transitioning from green-gray toward warm orange. The crack in the mirror glints more.

### `trans_to_bypass_03.png`
> Half-and-half reflection (vertical split). Left half of the reflected face still Jack's (brown hair, white shirt collar visible, tired eye). Right half is Tyler's (peroxide hair, red leather sleeve, sharp jaw, smirk emerging at the corner of the mouth). Lighting is half cool / half warm in a soft gradient down the middle. Jack's actual body (still visible at sink rim) hasn't changed yet — he's about to realize.

### `trans_to_bypass_04.png`
> Reflection is nearly fully Tyler: hair fully peroxide, red leather jacket on, smirk landed, lighting fully warm tungsten. Cigarette not yet in mouth. Only the tiniest residue of Jack's tired-eye darkness still slightly visible. The mirror has fully "swapped" who's in it.

### `trans_to_bypass_05.png`
> **DO NOT GENERATE — copy `bypass_idle_00.png` verbatim.** Continuity end.

---

## Phase 2B — trans_to_accept (Tyler → Jack in mirror, 6 frames, 600 ms)

### `trans_to_accept_00.png`
> **DO NOT GENERATE — copy `bypass_idle_00.png` verbatim.** Continuity start.

### `trans_to_accept_01.png`
> Tyler in the mirror as in frame 00, but his smug smirk wavers — mouth shape less confident, eyes losing their hooded knowing quality. The cigarette in his mouth corner has gone OUT (no glow). Slight cool-gray edge starting to creep into the lighting at the edges of the bathroom.

### `trans_to_accept_02.png`
> Leather jacket starts to dissolve at its edges (sleeve outlines softening with pixel-level dithering). Peroxide hair desaturating toward darker brown roots. Posture shoulders dropping by 1-2 px. Cigarette gone from mouth.

### `trans_to_accept_03.png`
> Half-and-half reflection (vertical split). Right half still Tyler (red leather right sleeve, peroxide right side of head, sharp jaw on right). Left half becoming Jack (white dress shirt left sleeve emerging, brown hair on left side, dark circle reappearing under the left eye, softer jaw). Lighting in mid-transition.

### `trans_to_accept_04.png`
> Reflection is nearly fully Jack: dress shirt fully on with loose tie, brown hair restored, dark circles forming under both eyes, posture slumped, mouth in neutral tired line. Only a faint residual peroxide tint at the very tips of his hair. Lighting fully cooled to fluorescent green-gray.

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

28 files total. Each **256 × 320** PNG with alpha channel. The four `_00` and `_05` bookend frames in the transitions are byte-identical copies of the corresponding idle frame.
