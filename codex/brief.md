# Codex Task Brief — bypass-pet 桌宠素材生成

You (Codex) are reading this because the human handed you this repo and said "make the art".

Your job: generate **28 PNG sprite frames** for a Windows desktop pixel pet that toggles between two visual states tied to two characters from David Fincher's *Fight Club* (1999). You are NOT writing Python source code — that part is owned by Claude. You only produce image assets.

Everything you need is in this folder. The full project context lives in `docs/superpowers/specs/` — skim it once, but this brief is the operational instruction.

> **Note**: this project originally used the cartoon character **奶龙** but pivoted to Fight Club on 2026-05-18. If you find any stray 奶龙 / dragon references anywhere in this repo, **ignore them** — they're stale. The repo on GitHub may still have a historical name; that's fine.

---

## 0. The pet, in one sentence

A 128×128 pixel sprite that lives in the corner of a Windows desktop. **Single-clicking** the pet flips it between two characters who share one mind: **the Narrator** (tired insomniac office drone, "accept" state) and **Tyler Durden** (anarchic alter-ego, "bypass" state). The flip mirrors a Claude Code permission-bypass toggle, so the symbolism is **conformist asks-for-permission ↔ nihilist runs-with-scissors**.

If you've never seen Fight Club: it's a 1999 film where a depressed office worker (the Narrator, played by Edward Norton) imagines and increasingly merges with a charismatic anarchist named Tyler Durden (Brad Pitt) until he realizes Tyler is his own dissociated personality. They are visually opposite: the Narrator is exhausted, beige, conformist; Tyler is jacked, red-leather, gleefully destructive. That contrast is what we're animating.

## 1. What you generate

**28 PNG files**, all 128×128, **transparent background (alpha channel)**, dropped into `assets/`:

| Filename pattern | Count | Style | Animation role |
|---|---|---|---|
| `assets/accept_idle_00.png` … `accept_idle_07.png` | 8 | Narrator (Jack) idle | "accept" state idle loop |
| `assets/bypass_idle_00.png` … `bypass_idle_07.png` | 8 | Tyler Durden idle | "bypass" state idle loop |
| `assets/trans_to_bypass_00.png` … `trans_to_bypass_05.png` | 6 | Narrator → Tyler morph | accept → bypass transition |
| `assets/trans_to_accept_00.png` … `trans_to_accept_05.png` | 6 | Tyler → Narrator morph | bypass → accept transition |

**Filenames are load-bearing.** The Python animator will iterate `00..07` (or `00..05`) and crash if a frame is missing. Do not invent names; do not zero-pad differently.

### Output requirements (hard rules)

- **Dimensions**: exactly 128×128 pixels
- **Format**: PNG with alpha channel
- **Background**: fully transparent (alpha 0) outside the sprite's silhouette
- **Color depth**: 8-bit per channel RGBA
- **No anti-aliasing halos**: edge of the sprite must be clean against transparent, not fringed with the source background color
- **No watermarks, signatures, or text outside the sprite's intended composition**
- **Style**: pixel art aesthetic — visible pixel grain at native 128×128, no smooth photoreal rendering. Think "pixel illustration", not "pixel emoji" and not "AAA game render".

If image-2 outputs something larger or with opaque background, downscale/composite to spec before saving.

## 2. The character bible — Narrator ("Jack")

Used for all **accept_idle_*** and the Jack-side of the transitions. The Narrator is unnamed in the film; fans nickname him "Jack" because of the "I am Jack's [organ]" monologue. We'll call him Jack.

Visual DNA:
- **Build**: average height, slightly hunched shoulders, deflated posture, soft (not muscular) frame
- **Hair**: short, mid-brown, neat but slightly limp; not styled, not bedhead — boring corporate
- **Face**: tired eyes with visible dark circles, mild stubble or 5-o'clock shadow, slightly sunken cheeks, mouth in a neutral or slightly downturned line
- **Clothes**: white or pale-blue dress shirt (slightly wrinkled at collar), dark tie loosened by 2 inches, dark slacks, sometimes a beige overcoat or wrinkled blazer
- **Accessory cues** (optional, vary by frame): coffee mug, briefcase handle, a stack of office paper, IKEA catalog
- **Palette**: desaturated IKEA-catalog tones — bone white `#E8E2D5`, dusty beige `#C9B89A`, sage-gray `#7A8475`, navy tie `#1F2A44`, brown hair `#5A4A3A`, dark-circle plum `#3A2D3A`. Avoid any saturated red, yellow, or orange — those are Tyler's.
- **Mood**: insomniac, depressed, conformist, "I haven't slept in three weeks"
- **No**: bandages or fight-club bruises (we want pre-Tyler Jack, the office drone version), no glasses unless you want to add a single subtle pair as flavor

The pet is **Jack**, not a generic businessman and not a buff hero. If your output looks like a corporate stock photo guy with healthy skin, you got it wrong — pull back toward exhausted-pale-thin.

Reference search: <https://www.bing.com/images/search?q=Fight+Club+Edward+Norton+office>

**Pose continuity inside the idle loop**: across the 8 idle frames, Jack's position should stay anchored (same feet-line, same center column). Don't let him drift around the frame.

## 3. The character bible — Tyler Durden

Used for all **bypass_idle_*** and the Tyler-side of the transitions.

Visual DNA:
- **Build**: lean and sculpted (not bodybuilder — wiry, defined), confident upright posture, weight on one hip
- **Hair**: peroxide-blonde tips or fully bleached, slightly disheveled, longer than Jack's — late-90s grunge
- **Face**: sharp jawline, mild stubble, scar across chin (small white slash), smug crooked smirk, eyes that look like they know something you don't
- **Clothes**: signature **red leather jacket** over either a bare chest or a stained ribbed undershirt; sometimes paired with vintage suit pants or jeans. Alternative looks: rubber dish-washing gloves (soap-maker scene), apron, no shirt
- **Accessory cues** (optional, vary by frame): cigarette (lit or unlit), yellow-tinted aviator sunglasses, a bar of pink soap, a lighter
- **Palette**: blood red `#A11D1D`, oxblood `#6B0F0F`, black leather `#0F0F12`, dirty cream `#D4C8A8`, peroxide yellow `#E8D147`, smoke gray `#7A7A7A`, skin warm-tan `#C9A088`. Strict red-black-cream dominance — minimize blue/green.
- **Mood**: charismatic, dangerous, gleeful chaos, "I want you to hit me as hard as you can"
- **No**: full nudity, blood splatter, fight wounds (keep it clean — energy not gore)

Reference search: <https://www.bing.com/images/search?q=Fight+Club+Tyler+Durden+red+leather+jacket>

**Pose continuity**: same as Jack — anchored feet-line, anchored center column across idle frames.

## 4. The two scenes / settings

Don't give either character a literal scenic background. The PNG background is **transparent**. But the lighting / shading / palette of each character should evoke their world:

- **Jack** → cool fluorescent office light, slightly green-shifted shadows, low contrast — the world of cubicles and IKEA catalogs
- **Tyler** → warm tungsten basement light, hard shadows with golden-orange tint, high contrast — the world of the basement bar and the abandoned house on Paper Street

The sprite itself carries this lighting; nothing outside the silhouette is rendered.

## 5. The transitions

Two 6-frame sequences morphing one character into the other. They play in 600 ms.

### `trans_to_bypass_*` (frames 00 → 05): Jack → Tyler

A dissociative split. Jack notices something has changed; Tyler emerges.

- **00**: identical to `accept_idle_00.png` (continuity start)
- **01**: Jack's eyes widen slightly, as if seeing his reflection in a window; faint red glow appears around his silhouette edge
- **02**: Mid-morph — hair beginning to lighten at the tips, jaw beginning to sharpen, dress shirt collar starting to come open, smirk hinting at the corner of the mouth
- **03**: Half-and-half — one side of the face still Jack, the other side becoming Tyler; the dress shirt is half-replaced by red leather creeping in
- **04**: Tyler nearly formed — leather jacket on, hair bleached, smirk landed, posture straightening; only residual traces of dark circles
- **05**: identical to `bypass_idle_00.png` (continuity end)

### `trans_to_accept_*` (frames 00 → 05): Tyler → Jack

The fantasy fades, the office drone returns.

- **00**: identical to `bypass_idle_00.png`
- **01**: Tyler's smirk wavers, sunglasses slip down (or cigarette starts to drop)
- **02**: Leather jacket dissolving at edges, peroxide hair desaturating toward brown
- **03**: Half-and-half — half Tyler, half Jack; tie reappearing, shoulders starting to slump
- **04**: Jack nearly back — dress shirt buttoned, brown hair, dark circles forming under eyes, posture deflating
- **05**: identical to `accept_idle_00.png`

**Critical**: frames `*_00` and `*_05` MUST be pixel-identical to the corresponding idle frames they bookend. The Python animator concatenates them seamlessly — any mismatch will visually pop. Easiest way: copy the existing idle frame for those bookend slots (these are listed as "DO NOT GENERATE" in `prompts.md`).

## 6. The idle animations, choreographed

### `accept_idle_00..07` — Jack tired-breathing cycle (2 s loop)

Jack is exhausted. He's not doing anything dramatic; he's just barely keeping it together.

| Frame | Pose |
|---|---|
| 00 | standing slouched, eyes half-open, mouth neutral, hands at sides or one holding a coffee mug |
| 01 | shallow breath in, shoulders rise barely |
| 02 | peak inhale, still hunched, eyes half-open |
| 03 | starting to exhale, eyes drooping further |
| 04 | eye droop maximum — eyes almost closed from fatigue (NOT a peaceful blink — this is a "I haven't slept" droop) |
| 05 | eyes opening back to half-open, head tilts slightly |
| 06 | small yawn — mouth opens slightly, eyes squint |
| 07 | yawn ending, returning to neutral slouch |

Lighting stays in the cool/green office register throughout.

### `bypass_idle_00..07` — Tyler swagger cycle (2 s loop)

Tyler is performing for an audience that doesn't exist. He's smug, kinetic, in command.

| Frame | Pose |
|---|---|
| 00 | weight on one hip, one hand in jacket pocket or at side, smug crooked smirk, cigarette in mouth (unlit or lit) |
| 01 | head tilts slightly to the side, smirk widens by 1 pixel |
| 02 | takes a drag — cigarette tip glows orange-red, eyes squint slightly with the inhale |
| 03 | head tilts back as he exhales, mouth slightly open, eyes hooded |
| 04 | small puff of smoke visible in front of his face (greyish white pixels), smirk returning |
| 05 | smug grin at maximum, hand might come up to remove cigarette or gesture |
| 06 | small chuckle — chest puffs out by 1 pixel, head shake by 1 pixel |
| 07 | back to base pose, cigarette settled in mouth, ready to loop |

Lighting stays in the warm tungsten / oxblood register. The cigarette glow is the only saturated color hit beyond the leather jacket.

## 7. Working order (recommended)

If you want to deliver in batches for review:

- **Phase 1 (16 frames)**: both idle loops (`accept_idle_*` and `bypass_idle_*`). Lets the human verify the character design before you commit to transitions.
- **Phase 2 (12 frames)**: both transition sequences.

Bookend frames in Phase 2 (`trans_to_bypass_00`, `trans_to_bypass_05`, `trans_to_accept_00`, `trans_to_accept_05`) are byte-identical copies of existing idle frames — just `cp` them, don't re-generate.

## 8. Iteration protocol

If the human asks for a redo on a frame:
- Keep the rest of the set; only re-generate the named frame(s)
- Maintain pose continuity with neighboring frames in the same loop
- Don't change the character bible mid-project

If a filename collides with an existing file, overwrite without asking.

## 9. Quality bar (self-check before declaring done)

- [ ] All 28 files present in `assets/`, exactly named per spec
- [ ] All 128×128 PNG with alpha
- [ ] Jack is recognizably exhausted-office-drone (white shirt + tie + dark circles + slouched), not a generic businessman
- [ ] Tyler is recognizably the red-leather-jacket charismatic anarchist (jacket + peroxide + smirk + cigarette), not a generic action hero
- [ ] Jack frames use desaturated cool palette; Tyler frames use warm oxblood/cream palette — the two halves visually disagree
- [ ] Idle loops are choreographically coherent (00 and 07 close enough to loop seamlessly)
- [ ] Transition bookend frames match their idle counterparts byte-for-byte
- [ ] No anti-aliasing halos, no watermarks, no extraneous text
- [ ] Pixel-art aesthetic, not photoreal

## 10. Content guardrails

This is a personal-use desktop toy. Keep the imagery within these limits even if the source material is darker:

- No visible blood, wounds, or gore
- No explicit nudity (bare chest fine, full nudity no)
- Cigarettes are OK (they're load-bearing for Tyler's character); no other drugs depicted
- No real recognizable actor likenesses — describe character TRAITS, not "Brad Pitt's face"; the pixel-art abstraction at 128×128 handles this naturally
- No text from the film's anti-consumerist monologues rendered as readable text in the image (occasional stylized letterforms as composition elements are fine)

## 11. When you're done

Commit the 28 PNGs in a single commit:
```
git add assets/
git commit -m "feat(assets): generate 28-frame Jack/Tyler sprite sheet"
git push
```

Then write a one-paragraph summary describing what you generated and any judgment calls you made. The human will run the desktop pet against your output and ping you for any frames that don't read right.

See `codex/prompts.md` for the specific image-2 prompt for each of the 28 frames.
