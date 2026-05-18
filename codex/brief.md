# Codex Task Brief — bypass-pet 桌宠素材生成（C 方案：镜子场景，2026-05-18 v2）

You (Codex) are reading this because the human handed you this repo and said "make the art". This is the **second** pass after the first attempt missed on framing.

Your job: generate **28 PNG sprite frames** for a Windows desktop pixel pet. You are NOT writing Python source code — that part is owned by Claude. You only produce image assets.

> **What changed from the previous version** (read this — it answers "why are we redoing it"):
> - **Framing**: previously full-body, which is illegible at sprite scale. **Now: bust / waist-up only**, framed inside a bathroom mirror. We need to see faces and expressions.
> - **Canvas**: previously 128×128 square. **Now: 256×320 portrait** (wider room for the mirror, taller room for the sink at the bottom and smoke trailing off the top).
> - **Setting**: previously two unrelated environments. **Now: one bathroom mirror, two reflections** — same physical space, different person in the glass.
> - **Likenesses**: previously hedged "don't render real actors". **Now drop that hedge.** Make Jack look like Edward Norton (1999, Fight Club era). Make Tyler look like Brad Pitt (1999, Fight Club era). The closer the resemblance, the better. This is a personal-use desktop tool, the human wants it to look like the actual characters they love.
> - **Fourth-wall device**: Tyler's hand and cigarette smoke can break out of the canvas edges. The mirror itself stays inside the canvas; what extends past the canvas is *Tyler reaching toward the viewer* or *his smoke rising up out of frame*.
>
> If you see any leftover references in this repo to 奶龙, full-body composition, 128×128, or "no actor likenesses" — those are stale, ignore them.

---

## 0. The pet, in one sentence

A 256×320 portrait pixel sprite of a bathroom mirror reflection. The reflection shows either **the Narrator ("Jack") from *Fight Club*** — exhausted office drone splashing water on his face — or **Tyler Durden** — smug, peroxide-blonde, leather-jacketed, cigarette in mouth, occasionally reaching out of the mirror toward the viewer. Single-clicking the pet flips between them. The whole thing lives in the corner of a Windows desktop.

## 1. What you generate

**28 PNG files**, all 256×320 (portrait), **transparent background outside the bathroom view's silhouette**, dropped into `assets/`:

| Filename pattern | Count | Style | Animation role |
|---|---|---|---|
| `assets/accept_idle_00.png` … `accept_idle_07.png` | 8 | Jack washing face in mirror | "accept" state idle loop |
| `assets/bypass_idle_00.png` … `bypass_idle_07.png` | 8 | Tyler grinning in mirror | "bypass" state idle loop |
| `assets/trans_to_bypass_00.png` … `trans_to_bypass_05.png` | 6 | Reflection morphing Jack → Tyler | accept → bypass transition |
| `assets/trans_to_accept_00.png` … `trans_to_accept_05.png` | 6 | Reflection morphing Tyler → Jack | bypass → accept transition |

**Filenames are load-bearing.** The Python animator iterates `00..07` (or `00..05`) and will show a placeholder if a frame is missing. Do not invent names; do not zero-pad differently.

### Output requirements (hard rules)

- **Dimensions**: exactly 256 wide × 320 tall pixels (portrait)
- **Format**: PNG with alpha channel
- **Background**: fully transparent outside the bathroom view. The bathroom view doesn't have to fill the whole rectangle — it should fill most of it, but the edges can fade to transparent or have meaningful protrusions (Tyler's hand, smoke) extending into otherwise-empty pixels right up to the canvas edge.
- **Color depth**: 8-bit per channel RGBA
- **No anti-aliasing halos**: edges of solid sprite areas should be clean against transparent
- **No watermarks, signatures, or text outside the sprite's intended composition**
- **Style**: pixel-art aesthetic, but at 256×320 you have room for semi-detailed shading. Aim for "modern pixel illustration" (think *Octopath Traveler*, *Hyper Light Drifter* bust portraits) rather than 8-bit chunky or photoreal.

If image-2 outputs different dimensions, downscale/composite to spec before saving.

## 2. Canvas composition (universal — fixed across all 28 frames)

The same bathroom layout in every frame. Camera does not move. Only the reflection, the lighting, and the action change between frames.

```
+-------------------------------+ <- canvas top edge (y=0)
|     (ceiling, dark)           |
| ~~~  fluorescent strip ~~~~~~ | <- thin reflected light line at top of mirror
| +-------------------------+   |
| |                         |   | <- thin metal mirror frame (1-2 px)
| |   [ R E F L E C T I O N ]|   | <- reflection of Jack or Tyler, bust-up
| |   bust + head visible    |   |
| |   shoulders + arms        |   |
| |                         |   |
| | * hairline crack top-right corner of mirror (Tyler's earlier work)
| +-------------------------+   | <- mirror frame bottom
|   |____________________|      | <- sink edge (curved porcelain)
| [toothbrush]    [soap]        | <- small props at canvas bottom
+-------------------------------+ <- canvas bottom edge (y=320)
```

- The mirror should occupy roughly **canvas pixels x=20..236 / y=30..240** (a ~216×210 rectangle, off-center toward top)
- The sink edge takes the bottom ~80 px
- Top ~30 px is ceiling / fluorescent strip glare
- Mirror frame is a thin off-white-cream or chrome rectangle, with a **hairline crack** in the upper-right corner (referring to Tyler having punched the mirror in some prior scene — adds character)
- Below the mirror (above the sink): faucet rim, a glass tumbler with a toothbrush, a bar of pink soap, a wadded paper tissue. Keep these tiny and to the corners — they're context flavor, not focal.

The transparent background means: outside the bathroom view (the rounded corners of the canvas / the gaps around the protruding fourth-wall elements) should be fully transparent so the desktop shows through. You can soften the very outermost edges with subtle vignetting if you want, but the basic shape is a "bathroom view" rectangle inset slightly from the canvas edges.

## 3. The character bible — Jack (the Narrator)

Used for all **accept_idle_*** and the Jack-side of the transitions.

Visual DNA (aim for Edward Norton, 1999, Fight Club):
- **Build**: thin, slightly hunched, soft (not muscular)
- **Hair**: short, mid-brown, neat but slightly limp; flat parted-side; not styled
- **Face**: tired/sunken; visible **dark circles** under the eyes (key feature — make them obvious); mild stubble; pale skin with cool undertones; slim straight nose; thin lips in a neutral or slightly downturned line
- **Clothes**: rumpled **white dress shirt** with collar slightly askew, dark loose tie hanging 2 inches lower than collar (visible at chest); sometimes a wrinkled blazer or wrinkled khaki overcoat
- **Posture in mirror**: slumped shoulders, head sometimes hanging
- **Accessory cues** (vary by frame): coffee mug, hands cupped catching water, hands at face, hands gripping sink edge below mirror
- **Palette**: bone-white shirt `#E8E2D5`, navy tie `#1F2A44`, mid-brown hair `#5A4A3A`, pale skin `#D4B8A8`, plum under-eye shadow `#3A2D3A`, sage-gray background tones `#7A8475`
- **Lighting**: cool fluorescent overhead, slightly green-shifted shadows, low contrast — make the whole bathroom feel like a 90s public restroom under bad bulbs
- **Mood**: insomniac, defeated, going-through-the-motions

## 4. The character bible — Tyler Durden

Used for all **bypass_idle_*** and the Tyler-side of the transitions.

Visual DNA (aim for Brad Pitt, 1999, Fight Club):
- **Build**: lean and **sculpted** (not bodybuilder — wiry, defined chest if jacket open), confident upright posture
- **Hair**: **peroxide-bleached blonde**, longer than Jack's, slightly disheveled, with darker roots showing; late-90s grunge cut
- **Face**: **sharp angular jawline**, mild stubble, **small white scar** across the chin (slight diagonal slash, ~5 px long), prominent cheekbones, smug crooked smirk on the right side of the mouth, hooded eyes with a knowing glint, slight smile-lines at the corners of the eyes when grinning
- **Clothes**: signature **red leather jacket** open over a stained cream ribbed undershirt (or bare-chested if you want — visible sculpted upper chest is fine, no nipples necessary because of the framing); sometimes adds a thin chain necklace or fingerless gloves
- **Posture in mirror**: shoulders back, weight on one hip, head slightly tilted in a "you see me?" challenge
- **Accessory cues** (vary by frame): unlit or lit cigarette in mouth corner, cigarette held between index/middle fingers, lighter, hand reaching out
- **Palette**: blood-red leather `#A11D1D`, oxblood shadows `#6B0F0F`, black `#0F0F12`, dirty cream undershirt `#D4C8A8`, peroxide-yellow hair `#E8D147`, warm-tan skin `#C9A088`, smoky gray `#7A7A7A` for smoke
- **Lighting**: the same bathroom but the **bulb has somehow changed** — warm tungsten with hard shadows and golden-orange tint, high contrast. As if Tyler swapped the fluorescent for a warm bulb. The crack in the mirror glints with this warmer light.
- **Mood**: charismatic, dangerous, gleeful chaos

## 5. The fourth-wall device

This is the signature visual move. Use it in `bypass_idle_06.png` and any frame where Tyler is in command:

- Tyler can **reach his hand out of the mirror** toward the viewer. His arm extends past the mirror frame, past the sink, and **out past the canvas's right edge** (clipping cleanly at x=256). The hand is the closest object to camera — slightly larger than perspective-realism would dictate, palm or finger extended.
- **Cigarette smoke** trails up from his cigarette and **out past the canvas's top edge** (clipping cleanly at y=0). Smoke is a few small wispy gray pixel clusters.
- Optionally his red leather jacket sleeve can also overflow the mirror's frame in some frames.

Jack never breaks the fourth wall. He stays politely inside the mirror.

## 6. Idle animation choreography

### `accept_idle_00..07` — Jack washes his face (2 s loop)

Camera is fixed on the bathroom mirror. Jack is reflected; the actual Jack's hands occasionally appear at the bottom of the mirror as he splashes water.

| Frame | Action |
|---|---|
| 00 | Jack stands at the sink, both hands on sink rim (faintly visible at very bottom of mirror), head bowed slightly, looking down — reflection shows top of his head + slumped shoulders + back of neck |
| 01 | Jack raises his head, eyes meeting his own gaze in the mirror — tired, blank |
| 02 | Eyes start to close (blink frame, eyelids 50% down) |
| 03 | Eyes fully closed (full blink) |
| 04 | Eyes 50% open again (blink ending) |
| 05 | Jack's cupped hands rise into the bottom of the mirror with water in them |
| 06 | Hands at face splashing water — water droplets visible flying outward; some droplets cling to mirror surface |
| 07 | Hands drop back below mirror, water dripping from chin — loop back to 00 |

Throughout: cool fluorescent light. Bone-white shirt, dark tie visible from chest up. Dark circles emphasized.

### `bypass_idle_00..07` — Tyler grins and smokes in the mirror (2 s loop)

Camera fixed. The reflection now shows Tyler — same posture-region but radically different person.

| Frame | Action |
|---|---|
| 00 | Tyler in mirror, smug crooked smirk, unlit cigarette in left corner of mouth, hands at his sides, weight on right hip, looking slightly off-camera toward viewer's left |
| 01 | Head tilts 2 px to his right, smirk widens |
| 02 | Brings cigarette to mouth properly (hand visible at right side of frame) and lights it — small orange spark at lighter? Cigarette tip starts to glow |
| 03 | Takes a drag — cigarette tip glowing hot orange-red (2-3 px bright orange dot), eyes squint, chest expands |
| 04 | Exhales — gray-white smoke billows in front of his face and rises up, **the topmost wisp exits the canvas top edge** |
| 05 | Smoke clearing, smirk returns to maximum |
| 06 | **Reaches his right hand TOWARD viewer** — hand extends past mirror frame, past sink, **clips out past canvas right edge**. Smug grin held. This is the signature 4th-wall frame. |
| 07 | Hand retreats back into mirror, cigarette settles in mouth corner, back to base pose — loop back to 00 |

Throughout: warm tungsten / oxblood light, red jacket dominant, scar visible on chin.

## 7. Transition choreography

### `trans_to_bypass_*` (Jack → Tyler in the mirror, 6 frames, 600 ms)

The reflection morphs while Jack reacts.

- **00**: identical to `accept_idle_00.png` (Jack at sink, head down). **DO NOT GENERATE — copy from `accept_idle_00.png`.**
- **01**: Jack jerks his head UP. His reflected eyes widen — he sees something wrong. Lighting still cool. Hair still brown.
- **02**: The reflection starts to diverge. Hair lightens at the tips (peroxide creeping in). Jawline sharpens by 1-2 px. The mirror's lighting starts warming up — shadows shift from green-gray toward warm-orange.
- **03**: Half-and-half (vertical split). Left half of the reflection still Jack (brown hair, dress shirt, tired). Right half is becoming Tyler (peroxide on right side of head, leather jacket creeping onto right shoulder, smirk emerging on right side of mouth). The whole bathroom lighting is mid-shift.
- **04**: Tyler nearly formed. Hair fully peroxide. Red leather jacket on. Smirk in place. Cigarette not yet lit. Lighting fully warm. Only residual Jack-tired-eyes still slightly visible.
- **05**: identical to `bypass_idle_00.png`. **DO NOT GENERATE — copy from `bypass_idle_00.png`.**

### `trans_to_accept_*` (Tyler → Jack in the mirror, 6 frames, 600 ms)

The opposite morph. Tyler dissolves, Jack returns.

- **00**: identical to `bypass_idle_00.png`. **DO NOT GENERATE — copy from `bypass_idle_00.png`.**
- **01**: Tyler's smirk wavers — mouth shape less confident. Cigarette goes out (no glow). Slight cool-gray edge creeping into the lighting at the edges.
- **02**: Leather jacket starts to dissolve at the edges — sleeve outlines softening, peroxide fading toward darker root color. Posture shoulders dropping by 1-2 px.
- **03**: Half-and-half (vertical split). Right half of reflection still Tyler (leather sleeve, peroxide right side). Left half becoming Jack (white dress shirt sleeve emerging, brown hair returning, dark circle reappearing under left eye).
- **04**: Jack nearly back. Dress shirt fully on with loose tie. Brown hair restored. Dark circles forming under both eyes. Posture slumped. Only residual peroxide tint at very tips of hair. Lighting cooled to fluorescent green-gray.
- **05**: identical to `accept_idle_00.png`. **DO NOT GENERATE — copy from `accept_idle_00.png`.**

**Critical**: frames `*_00` and `*_05` for both transitions MUST be byte-identical copies of the corresponding idle frame they bookend. The Python animator concatenates them seamlessly — any mismatch will visually pop. Just `cp` the existing PNG.

## 8. Working order (recommended)

If you deliver in batches for review:

- **Phase 1 (16 frames)**: both idle loops (`accept_idle_*` Jack washing face + `bypass_idle_*` Tyler grinning/smoking). Lets the human verify the look and the character bibles land before you commit to the transitions.
- **Phase 2 (12 frames)**: both transition sequences. The 4 bookend frames are file copies.

## 9. Iteration protocol

If the human asks for a redo on a frame:
- Keep the rest of the set; only re-generate the named frame(s)
- Maintain pose continuity with neighboring frames in the same loop
- Don't change the character bible mid-project

If a filename collides with an existing file, overwrite without asking.

## 10. Quality bar (self-check before declaring done)

- [ ] All 28 files present in `assets/`, exactly named per spec
- [ ] All **256 × 320** PNG with alpha
- [ ] Jack is recognizably Edward Norton's Fight-Club Narrator — exhausted, brown-haired, dark-circled, dress shirt, tie
- [ ] Tyler is recognizably Brad Pitt's Tyler Durden — peroxide, scar, smirk, red leather jacket, cigarette
- [ ] Bathroom layout is consistent: mirror centered, sink edge at bottom, toothbrush/soap props, hairline crack in mirror upper-right
- [ ] Jack frames cool fluorescent; Tyler frames warm tungsten
- [ ] Tyler's hand and/or smoke breaks the canvas edge in at least one bypass_idle frame (signature 4th wall move)
- [ ] Idle loops choreographically coherent (00 and 07 close enough to loop seamlessly)
- [ ] Transition bookend frames byte-identical to their idle counterparts
- [ ] Pixel-art aesthetic with semi-detailed shading; not photoreal, not 8-bit chunky

## 11. Content notes (relaxed from v1)

- **Actor likenesses are encouraged** — make Jack look like Edward Norton, make Tyler look like Brad Pitt. Personal-use, no IP concerns to hedge for.
- Cigarettes: fine and core to Tyler's look
- Bare chest under open jacket: fine (no need to render anything explicit, just chiseled chest)
- No visible blood, gore, fight wounds
- No nudity below the waist (we're cropping at chest anyway)

## 12. When you're done

Commit the 28 PNGs in a single commit:
```
git add assets/
git commit -m "feat(assets): generate 28-frame mirror-scene sprite sheet (Jack/Tyler)"
git push
```

Then write a one-paragraph summary describing what you generated, any judgment calls you made on the bathroom layout or character likeness, and any frames you're particularly unsure about. The human runs the desktop pet against your output and pings you for redos.

See `codex/prompts.md` for the specific image-2 prompt for each of the 28 frames.
