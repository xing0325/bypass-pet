# Codex Task Brief — bypass-pet 桌宠素材生成（v3 · 2026-05-19）

You (Codex) are reading this because the human handed you this repo for the **third pass** of sprite generation.

Your job: generate **144 PNG sprite frames** for a Windows desktop pixel pet. You are NOT writing Python source code — that's owned by Claude. You only produce image assets.

---

## 🚨 What changed from v2 (READ THIS FIRST)

You already did a v2 pass on branch [`codex/generate-mirror-sprite-assets`](../../tree/codex/generate-mirror-sprite-assets) and the **character design + bathroom layout + lighting from that pass are excellent — keep them**. What changed:

| | v2 (PR #2) | **v3 (this brief)** |
|---|---|---|
| Canvas | 256 × 320 | **192 × 240** (smaller; doesn't crowd the desktop) |
| accept_idle frames | 8 @ 250 ms = 2 s loop | **60 @ 83 ms = 5 s loop** (smoother, more natural breathing rhythm) |
| bypass_idle frames | 8 @ 250 ms = 2 s loop | **60 @ 83 ms = 5 s loop** |
| trans_to_bypass | 6 @ 100 ms = 0.6 s | **12 @ 50 ms = 0.6 s** (same duration, double FPS, smoother morph) |
| trans_to_accept | 6 @ 100 ms = 0.6 s | **12 @ 50 ms = 0.6 s** |
| Total frames | 28 | **144** |

**Why the human asked for this**: v2's 4-FPS idle loop felt twitchy at 2 s. 12 FPS over 5 s feels alive, not frantic. The canvas was also a touch too big.

**You are not starting from scratch.** v2's character design is canonical — go look at `codex/generate-mirror-sprite-assets` branch for the 28 reference PNGs. Use them as **character + scene + lighting references** when generating v3. Only the framing and motion choreography expand; the look of Jack, the look of Tyler, the bathroom layout, the lighting palette stay the same.

---

## 0. The pet, in one sentence

A 192×240 portrait pixel sprite of a bathroom mirror reflection. The reflection shows either **the Narrator ("Jack") from *Fight Club*** — exhausted office drone going through a slow blink-and-splash routine — or **Tyler Durden** — peroxide-blonde, leather-jacketed, smug, with a 5-second cycle of lighting / smoking / smirking / reaching out of the mirror toward the viewer. Single-clicking the pet flips between them via a 0.6 s morph.

## 1. What you generate

**144 PNG files**, all 192×240, **transparent background outside the bathroom view's silhouette**, dropped into `assets/`:

| Filename pattern | Count | Style | Animation role |
|---|---|---|---|
| `assets/accept_idle_00.png` … `accept_idle_59.png` | 60 | Jack washing face in mirror | "accept" state idle loop (5 s) |
| `assets/bypass_idle_00.png` … `bypass_idle_59.png` | 60 | Tyler grinning + smoking in mirror | "bypass" state idle loop (5 s) |
| `assets/trans_to_bypass_00.png` … `trans_to_bypass_11.png` | 12 | Reflection morphing Jack → Tyler | accept → bypass transition (0.6 s) |
| `assets/trans_to_accept_00.png` … `trans_to_accept_11.png` | 12 | Reflection morphing Tyler → Jack | bypass → accept transition (0.6 s) |

**Filenames are load-bearing.** The Python animator iterates `00..59` (or `00..11`) and shows placeholder squares for any frame it can't find. Don't invent names; don't zero-pad differently.

### Output requirements (hard rules)

- **Dimensions**: exactly **192 wide × 240 tall** pixels (portrait)
- **Format**: PNG with alpha channel (RGBA 8-bit)
- **Background**: fully transparent outside the bathroom view's silhouette
- **No watermarks, signatures, or stray text**
- **Style**: pixel-art with semi-detailed shading (modern pixel illustration, like *Octopath* / *Hyper Light Drifter* bust portraits)
- **Bookend frames** (`trans_to_bypass_00`, `trans_to_bypass_11`, `trans_to_accept_00`, `trans_to_accept_11`) MUST be byte-identical copies of the corresponding idle frame they bookend (see Section 5). Just `cp` them.

## 2. Character + scene reference

**Go look at the v2 branch first.** It has 28 PNGs that establish:
- What Jack looks like (Edward Norton 1999 Fight-Club Narrator: thin, slightly hunched, brown hair parted to the side, pale skin, prominent dark circles, mild stubble, white dress shirt with loose dark tie)
- What Tyler looks like (Brad Pitt 1999 Fight-Club Tyler Durden: lean and sculpted, peroxide-bleached blonde hair, sharp jaw with small chin scar, red leather jacket over cream undershirt, cigarette in mouth corner, smug crooked smirk)
- Bathroom layout (centered mirror with thin metal frame and **hairline crack in upper-right corner**, sink edge at bottom with toothbrush in glass + bar of pink soap + crumpled tissue, fluorescent light strip at top)
- Lighting (cool green-shifted fluorescent for Jack frames; warm tungsten orange for Tyler frames)

Keep all of that **byte-identical** in feel. At 192×240, the same elements appear slightly smaller per pixel — your art needs to scale gracefully.

**Likenesses**: the v2 brief tried to point image-2 at Edward Norton and Brad Pitt by name, but image-2 refused. You worked around it with feature descriptions (jawline, hair, wardrobe, posture, scar). Use the same workaround for v3 — keep the rewritten descriptors, not the actor names.

## 3. The fourth-wall device (still required)

In at least one bypass_idle frame, Tyler's **hand reaches out of the mirror** and extends past the canvas's right edge (clipped at x=192). In another bypass_idle frame, **cigarette smoke** trails up and exits the canvas's top edge (clipped at y=0). v2 nailed these in `bypass_idle_06` (hand) and `bypass_idle_04` (smoke); in v3 the timing is different (60-frame loop), but the device must persist — see Section 4 for where to place it in the new timeline.

Jack never breaks the fourth wall.

## 4. Idle choreography (60 frames @ 12 FPS = 5 s loop)

For each idle loop, generate **10 keyframes** with full detail (every 6th frame), then fill in the 5 in-between frames per gap with small pose interpolations. The result is a smooth 12-FPS loop.

You do not have to literally tween in image-2 — each frame is still a fresh image-2 generation. The "keyframe + tween" structure just tells you what to prompt: keyframe prompts go heavy on the new pose, tween prompts say "almost identical to neighbor frame, slight pose shift only." See `codex/prompts.md` for the exact per-frame text.

### accept_idle timeline (Jack)

| Frame range | Time | Beat |
|---|---|---|
| 00-05 | 0.0-0.5 s | Rest pose: head bowed at sink, hands on rim |
| 06-11 | 0.5-1.0 s | Head slowly rises |
| 12-17 | 1.0-1.5 s | Held stare into own reflection (only micro-shifts) |
| 18-23 | 1.5-2.0 s | Slow blink: eyelids descending |
| 24-29 | 2.0-2.5 s | Eyes fully closed (frames 24-26), then reopening (27-29) |
| 30-35 | 2.5-3.0 s | Cupped hands rise into the mirror frame, water held in palms |
| 36-41 | 3.0-3.5 s | Hands at face, water splashing (visible droplets flying) |
| 42-47 | 3.5-4.0 s | Hands hold against face, water dripping from chin |
| 48-53 | 4.0-4.5 s | Hands drop back below mirror, water still dripping |
| 54-59 | 4.5-5.0 s | Return to rest pose, seamless loop to frame 00 |

### bypass_idle timeline (Tyler)

| Frame range | Time | Beat |
|---|---|---|
| 00-05 | 0.0-0.5 s | Base swagger pose: smug smirk, unlit cigarette in mouth corner |
| 06-11 | 0.5-1.0 s | Head tilts to his right, smirk widens |
| 12-17 | 1.0-1.5 s | Cigarette to mouth, lighter spark, tip starts to glow |
| 18-23 | 1.5-2.0 s | Drag: cigarette glows hot orange-red, eyes squint, chest expands |
| 24-29 | 2.0-2.5 s | **Exhale: smoke billows in front of face, topmost wisp exits canvas TOP edge (4th wall)** |
| 30-35 | 2.5-3.0 s | Smoke clearing, smirk returns to max |
| 36-41 | 3.0-3.5 s | Hand begins reaching out toward viewer |
| 42-47 | 3.5-4.0 s | **Hand fully extended OUT past canvas RIGHT edge (4th wall money frame)**, smug grin held |
| 48-53 | 4.0-4.5 s | Hand retreats back into mirror |
| 54-59 | 4.5-5.0 s | Return to base pose, seamless loop to frame 00 |

## 5. Transition choreography (12 frames @ 20 FPS = 0.6 s)

Transitions are deliberately kept tight (0.6 s) so state-change doesn't feel sluggish. With 12 frames you get a smooth morph.

### trans_to_bypass (Jack → Tyler)

| Frame | Beat |
|---|---|
| 00 | **COPY accept_idle_00 verbatim** (bookend) |
| 01-02 | Jack jerks head up, eyes wide, faint red glow at silhouette edge |
| 03-04 | Hair tips starting to bleach, jaw sharpening, dress shirt collar opening, smirk hinting |
| 05-06 | Half-half vertical split: left side Jack, right side Tyler emerging |
| 07-08 | Mostly Tyler, red leather jacket on, smirk in place, lighting fully warm |
| 09-10 | Tyler fully formed, only residual Jack-tired-eye darkness |
| 11 | **COPY bypass_idle_00 verbatim** (bookend) |

### trans_to_accept (Tyler → Jack)

| Frame | Beat |
|---|---|
| 00 | **COPY bypass_idle_00 verbatim** (bookend) |
| 01-02 | Smirk wavers, cigarette goes out |
| 03-04 | Leather jacket dissolving at edges, peroxide hair desaturating |
| 05-06 | Half-half vertical split: right side Tyler, left side Jack emerging |
| 07-08 | Mostly Jack, dress shirt back on, brown hair, dark circles forming |
| 09-10 | Jack fully back, only residual peroxide tint at hair tips, lighting cooled |
| 11 | **COPY accept_idle_00 verbatim** (bookend) |

## 6. Working order

The recommended batches:

1. **Phase 1A — Jack keyframes** (10 PNGs): `accept_idle_00, 06, 12, 18, 24, 30, 36, 42, 48, 54` — locks the choreography for Jack
2. **Phase 1B — Tyler keyframes** (10 PNGs): `bypass_idle_00, 06, 12, 18, 24, 30, 36, 42, 48, 54` — locks Tyler choreography (and the 2 fourth-wall moments at 24-29 and 42-47 land here)
3. **Phase 2A — Jack tweens** (50 PNGs): all the other `accept_idle_*` frames
4. **Phase 2B — Tyler tweens** (50 PNGs): all the other `bypass_idle_*` frames
5. **Phase 3 — Transitions** (24 PNGs): `trans_to_bypass_01..10` + `trans_to_accept_01..10` (frames 00 and 11 are file copies)

Deliver Phase 1 (20 keyframes) first; the human can sanity-check and ping any redos before you commit to the 124 follow-up frames.

## 7. Iteration protocol

If the human asks for a redo on a frame:
- Keep the rest of the set; only re-generate the named frame(s)
- Maintain pose continuity with neighboring frames in the same loop
- Don't change the character bibles mid-project
- If a filename collides with an existing file, overwrite without asking

## 8. Quality bar (self-check before declaring done)

- [ ] All **144** files present in `assets/`, exactly named per spec
- [ ] All **192 × 240** PNG with alpha
- [ ] Bathroom layout consistent across all 144 frames (mirror centered + hairline crack + sink edge + toothbrush + soap)
- [ ] Jack frames cool fluorescent; Tyler frames warm tungsten
- [ ] Jack readably similar to v2's Jack (don't drift into a new face)
- [ ] Tyler readably similar to v2's Tyler (don't drift)
- [ ] Tyler's hand breaks canvas right edge somewhere in frames 36-47 of bypass_idle
- [ ] Tyler's smoke breaks canvas top edge somewhere in frames 24-29 of bypass_idle
- [ ] accept_idle_00 and accept_idle_59 close enough to loop seamlessly
- [ ] bypass_idle_00 and bypass_idle_59 close enough to loop seamlessly
- [ ] Transition bookend frames byte-identical to their idle counterparts (just `cp`)
- [ ] Pixel-art aesthetic preserved; not photoreal, not 8-bit chunky

## 9. Content notes

- Actor-likeness target is encouraged via descriptive features. v2 already learned that image-2 refuses direct actor names — use the visual-feature workaround.
- Cigarettes are fine and core to Tyler
- Bare chest under open jacket is fine
- No blood / gore / fight wounds / nudity below the waist

## 10. When you're done

Commit on a fresh branch and open a PR. Pattern:

```
git checkout -b codex/v3-mirror-144-frames
git add assets/
git commit -m "feat(assets): generate 144-frame v3 sprite sheet @ 192x240 (Jack/Tyler)"
git push -u origin codex/v3-mirror-144-frames
gh pr create --draft --title "[codex] v3 generate 144-frame mirror sprite sheet @ 192x240" --body "..."
```

Reference your earlier v2 PR (`#2`) as superseded. In the PR body, describe:
- Any judgment calls on choreography or tween interpolation
- Frames you're least confident about
- Whether you delivered all 144 or just Phase 1 for review first

The human will open `preview.html` from the repo root to flip through your output frame-by-frame and decide.

See `codex/prompts.md` for the per-frame image-2 prompt for each of the 144 frames.
