# Financial Clarity — Video Production Playbook

How our YouTube videos are made, so every future video follows the same process.
Channel: **Financial Clarity** (anonymous brand — never the host's personal name, never "Heimishe Investing Hub" — that's the WhatsApp community only).

## Pipeline

1. **Source material** — research cards/script from the user (WhatsApp "In Plain English" series).
2. **Script pass** — split the script into narration chunks. Before recording, do a **context check**: every number needs a unit and a comparison, every reference must be set up, no dangling jumps. Add short bridging words where context is missing (same voice); never drop the user's lines.
3. **Narration** — TTS voice Helio (avocado_v2:MAI_03), recorded per chunk, then sped to **1.1x** for energy. Total voice ~4–4.5 min for a standard deep-dive.
4. **Edit** — see standards below.
5. **Verify** — frame grabs at ~10 timestamps; check captions sync, sharpness, no repeated clips, end card correct.
6. **Package** — final MP4 + thumbnail + metadata (3 title options, description with chapters + disclosure, hashtags).

## Editing standards (hard rules)

- **Cuts every 1–3 seconds.** Nothing static held longer. Slide/card images only as ≤2s punched-in flashes.
- **NO clip is ever used twice** in one video. Keep a shot log; audit before delivery.
- **Data first**: every major stat in the narration gets an **animated** visualization — draw-on bar charts, count-up numbers, growing lines, vs-comparisons. A data visual at least every 15–20 seconds. Static charts are a failure.
- **Footage variety**: real motion footage across many subjects (stores, trading screens, warehouses, trucks, registers, produce, investors, money). Generic "people shopping" is a minority of shots. One consistent visual world (US footage for US stories — no foreign signage).
- **Pattern interrupt every 30–45s**: full-screen kinetic typography, animated comparison, or animated chart.
- **Hook density**: the first 30 seconds cut the fastest.
- **Faceless-channel grammar** (models: The Plain Bagel, How Money Works, Wall Street Millennial): clean, research-driven, subtle SFX only on the biggest beats (whoosh/pop), no meme clutter.
- **Finish**: unified color grade (contrast ~1.06, saturation ~1.13), one caption style, loudness **−14 LUFS**, 1920×1080.
- **End card**: FINANCIAL CLARITY, ~9s, earnings/next-video hook, subscribe line, and ONLY the generic disclaimer ("Educational only. Not investment advice. Do your own research."). **No position disclosure ever** — the user decided 2026-10-25 he does not disclose whether he owns the stock, in the video or the description, regardless of what the source cards say.

## Thumbnail standards

- Max **3 elements**: face / stake / identifier. One idea, readable at 320×180 (always check phone size).
- If a face is used, it must **react to the subject** — gaze locked on the chart/price, expression caused by it (never a random happy face next to a chart), red chart glow lighting the face binds subject to background.
- Hierarchy by size: the stake (e.g. −60%) biggest, the question headline next (one line across the bottom, as large as fits), the brand identifier (real logo) supporting, never competing.
- Color ownership: green = company logo, red = the drop, yellow = the question headline. Face never covered by graphics.
- Keep key elements out of the bottom-right (timestamp trap). New filename every version (app caches by name).
- CLICKBAIT BUILD METHOD (user-directed 2026-10-27, after flat PIL-graphic thumbnails were rejected as "not clickbait" and the first AI composite as "overlapped, unprofessional"): generate the base with the AI image tool — photorealistic emotional face reacting to a glowing chart/money visual, with the composition LOCKED so one side of the frame is completely empty dark space; composite the text with PIL into that empty zone only. NO overlaps: text never touches the chart, arrow, coins, or face. One dominant number (e.g. "4X"), the ticker as identifier, one short hook line. Soft blurred drop shadows over heavy outlines.

## Shorts standard (user-directed 2026-10-28, after the first SCHD vs VOO Short was rejected as unstimulating)

Shorts are stimulation-first, a different animal from long videos: PEOPLE/faces in the majority of shots (reactions sell; charts alone are banned as the main visual), cuts every 0.7–1.5s, no static hold over 2s, zoom punches, pattern interrupt every ~3s, hook inside the first 1.5s, big kinetic word-by-word captions, SFX hits on cuts and number reveals, energetic music bed. Audit before delivery: % of runtime with people on screen, mean shot length, longest hold.

## Thumbnails — the user's own hand (2026-10-28)

The user may design and set his OWN thumbnail (maximalist AI style: huge face, fire, many elements, fear hook like "NEVER BUY THE WRONG ONE!"). When he sets his own, NEVER replace it — metadata work only. Muse's thumbnails are drafts for his adoption, not defaults to impose.

## Self-critique loop (mandatory, user-directed 2026-10-25)

After any cut is "done," it is NOT delivered. The builder must act as its own hostile critic: review the entire cut, write a critique list (dead spots, irrelevant/weak shots, caption drift vs the script, repetition, black frames, audio issues, anything unprofessional), fix everything, re-render — and repeat for **three full critique-fix cycles**. Delivery reports include all three critique lists and their fixes. Only then does the user see it.

## Lessons learned (paid for in iterations)

- v1 (static slides) was rejected outright — motion and cutting pace are non-negotiable.
- Reusing stock clips is instantly noticed and reads cheap — over-source footage instead.
- Narration must be context-complete; viewers can't see the cards the script came from.
- Never call a video or thumbnail "final" until the user confirms it.
- **Visual relevance gate (added after the v3 Part 1 rejection, 2026-10-25):** every shot must be semantically tied to the exact narration line under it — verified with a shot-by-shot table (timestamp → line → visual → justification) before delivery. No generic/pretty stock, no foreign-looking locations for US stories (an aerial of English-looking towns killed an opening). Black-screen text cards are snappy (~1.5–2s each, big kinetic type); never long dead black holds. Benchmark for openings: the v2 SFM opening the user praised.

## Update 2026-10-25 (user verdict on Part 1 third take)
- Part 1 v3take verdict: "a little bit better... more on track" — the motion-only, kinetic-card direction is RIGHT, but the quality bar is another 5–10x up: denser cuts, punchier graphics, zero calm windows. Direction approved ≠ quality approved.
- AUDIO RULE (new): the sound must be THICKER. Every video gets a background music bed — royalty-free instrumental, energetic, sidechain-ducked well under narration (−18/−20 dB) — plus beat SFX (whooshes/risers on graphic entries, hits on number reveals). Narration clarity stays first; final mix −14 LUFS integrated, true peak ≤ −1 dB. A dry voice-only mix reads thin and is a defect.

- NARRATION SPEED (2026-10-25, supersedes the 1.1x rule): the user found 1.1x too fast — "a trap." Narration now plays at 0.9x (acceptable range 0.85–0.95). ONLY the words slow down; visual cutting stays fast and dense. Expect runtimes ~20% longer than the 1.1x plan.

- CORRECTION (2026-10-25, minutes later): cutting pace MATCHES narration pace. Slowing the words to 0.9x also slows the edit rhythm proportionally (~1.5–3s cuts, events every ~2.5s, max hold ~3.5s). The voice and the cutting breathe together; do not keep visuals at the old frantic pace over a slower voice.

- SPEED SETTLED (2026-10-25, after full-video review): 0.9x was too slow, 1.1x too fast — narration runs at 1.0x, cutting scaled to match.
- OPENING RULE (2026-10-25): the first 25 seconds decide the video. No generic graphics and no boring pictures in the hook — the opening carries the strongest, most specific visuals in the whole piece (real crash/Wall Street motion, kinetic hero type, the animated crash chart early, real store motion). The rest of the 10:26 video was approved as-is ("the rest is good").

- SPEED FINAL (2026-10-25, later same day): the user re-authorized 1.1–1.2x after hearing the full video with the thicker mix — settled at 1.15x, cutting scaled to match. History: 1.1x over the old frantic edit read "a trap"; 0.9x read too slow; with matched cutting + music bed, 1.15x is the standard.

- QUALITY TRAJECTORY (user, 2026-10-25): the SFM full video is "just about good enough to post" — it is the FLOOR, not the ceiling. Every next video must be visibly better than the last; the channel standard ratchets up and up. Never let a later video ship below the previous one's level.

## Shorts cover frame (user correction, 2026-10-28)
- A Short's cover is chosen from a frame — an auto-picked frame "doesn't grab any attention." Choose the cover DELIBERATELY during the build: the most grabbing frame (expressive face + the video's biggest number) exported as a 1080x1920 JPG (short-cover-frame.jpg in the video folder).
- Studio reality (verified 2026-10-28 on this account): the Short edit page has a Thumbnail section; "Select from video" offers only 3 auto-generated frames (no scrubber) — the good frame is usually NOT among them. Use "Upload file" with the exported frame JPG instead; Studio accepts it and labels it "Uploaded thumbnail." Verify on the channel Shorts shelf.

## Graphics standard v2 (user verdict on VOO vs QQQ, 2026-10-28: "the graphics and the video could be much better — they're not so good")
Frame audit confirmed the verdict. Banned from now on:
- NO spec-sheet/infobox cards (label:value rows on dark background) — they read as documents, not graphics.
- NO text-list slides (two-column bullet walls). Lists get narrated over motion footage or become icon/visual rows.
- NO chart floating in a mostly-empty dark frame. Every data graphic FILLS the frame: giant hero number, bars/areas that grow to real scale, glow/gradient/texture, brand color worlds (e.g. green vs blue split), one visual metaphor per graphic.
- Typography: heavy display font for numbers/hooks — never thin default sans for hero text.
- NO generic finance clichés as filler: robot toys, soap bubbles, suit handshakes, random crowds, generic trading-desk wallpaper. Footage must be topic-relevant (products, campuses, stores, real activity) or people reacting.
Every graphic must pass the phone test: at small size it should look like a designed poster, not a screenshot of a spreadsheet.


## Raised Bar — Perfection Standard (user directive, 2026-10-28)

The user raised the channel-wide bar: every video must be "professionally edited to perfection," with clear structure and perfect frame-to-frame flow — "a much higher bar than till now." This supersedes "previous video is the floor" with a stronger rule:

- **Flow audit is mandatory before delivery:** step through every cut boundary. Each cut must be motivated (action, word, beat, or graphic logic). No jarring jumps, dead frames, back-to-back repeated compositions, or caption/graphic collisions at transitions.
- **Structure pass:** the arc must read as one rising line (hook → escalation → payoff). Any sagging or emotionally out-of-order beat gets re-cut.
- **Uniqueness:** favor verified facts/details the audience has NOT heard a hundred times; the rarest sourced details get the graphic/caption emphasis.
- **Critique cycles:** minimum three, plus one dedicated flow/transitions cycle on flagship pieces (series episodes).
- Applies to ALL future videos and Shorts, starting with "They Saw It Coming" Ep. 1 (Jensen Huang).

## Archival Speech Pacing (user directive, 2026-10-28)

For "They Saw It Coming" and any archival-footage content: no long speeches. Archival voices appear only as short killer-line bursts (~2–4s on screen each); narration carries the story, archival audio is spice. If a line needs more time, run it under a cutaway (B-roll/photo/graphic), never hold the talking head. No single visual holds past the ~2s cap. Report longest talking-head hold + longest single-visual hold in delivery audits.

## "They Saw It Coming" Series Rules (user verdict on the Jensen rough cut, 2026-10-28)

The hypercut stimulation template is WRONG for this series. The user rejected the Jensen rough assembly as too fast, unstructured, Musk-heavy, and script-thin. Standing rules for every series episode:

- **Structured narrative pacing:** premium mini-documentary, not dopamine montage. Shots land (2–4s where earned), cuts motivated by narration phrases and story beats, visible chapter logic (founding → death's door → the bet → vindication). Archival SPEECH bites stay short, but the PICTURE may breathe.
- **One visionary only:** the episode's person owns the camera. No co-stars — e.g. no Elon Musk close-ups or name emphasis in the Jensen episode (DGX-1 delivery is Jensen's beat; OpenAI is just the destination). No secondary talking heads.
- **Fact density is the stimulation:** scripts must be rich in verified, rarely-heard details — pull from the research's cut-for-time list before considering any new claim. Every ~5 seconds should teach something.
- These series rules override the generic Shorts stimulation standard where they conflict (mean shot length will be higher on series episodes — intended).

## Production Team Model (user directive, 2026-10-28)

The user directed Muse to operate as a delegating studio, not a solo builder: "set up a team of agents to work for you... you can make this into a huge [operation] and you could delegate," with multiple second opinions as a standing practice. Standing team for series/channel production:

- **Research & Sourcing** — deep verified research + real archival footage hunt (era-verified, source-logged; unverifiable claims dropped and logged).
- **Story Consultant (independent)** — craft research, blunt script critique, beat outline with hook/open-loop/but-therefore audit. Its fixes are a GATE: no episode finalizes without passing story review.
- **Builder/Editor** — assembles to the approved outline; applies playbook standards.
- **Audit** — flow audit, structure pass, fact-check against research.md, pacing numbers reported at delivery.
- Pipeline per episode: research+footage → story outline (consultant-reviewed) → build → audits → user verdict. Next episode's research starts while the current one builds.

## The Improvement Loop (standing system, user directive 2026-10-29)

The channel runs as a permanent, self-improving production system — not one-off videos. Every piece goes around the same loop, and every pass must come out stronger, faster, and more professional than the last:

1. **Research** — deep, tool-verified facts and real archival material only; unverifiable claims are dropped and logged.
2. **Independent consults** — fresh-eyes agents critique story, structure, and psychology before anything is built; their fixes are gates, not suggestions.
3. **Build** — one builder, to the current playbook standard (pace, voice bites, enhanced graphics, captions diff 0, loudness standard).
4. **Audit** — flow audit on every cut, structure pass, technical checks; failures are fixed before delivery, never after.
5. **User verdict** — the only finish line. Every correction becomes a written rule in this playbook the same day.
6. **Feedback** — Studio analytics are read after episodes have had time in the feed (48–72h, then weekly): views, CTR, stayed-to-watch, traffic sources, subscribers. What the data says becomes written lessons here; the next episode inherits them.
7. **Repeat from a higher floor** — the previous video is the minimum standard, never the target.

Tooling mandate (user, 2026-10-29): build whatever tools, agent teams, and pipeline improvements serve this loop long-term; incorporate as many specialist "partners" (research, story, build, audit, analytics) as the work needs.

## COMPOUNDING QUALITY DIRECTIVE (owner, 2026-11-02 — supersedes "good enough")

The owner, 2026-11-02: "I want you to compound the videos — they are not the best quality; they could be much better." Standing consequences:

1. **Quality compounds, it does not plateau.** Every build names, in its brief and its audit, ONE craft dimension it deliberately pushes beyond anything the channel has shipped (hook construction, graphic sophistication, narration delivery, edit rhythm, sound design, moment-getting, story structure) — and the audit's "vs the floor" section must show the improvement with evidence, not adjectives. Rotating the pushed dimension across builds is how the whole craft compounds instead of one axis being polished repeatedly.
2. **The floor rises with every delivery.** The previous video of a series is the minimum; matching it is a failed build. Where a build cannot beat the floor on its pushed dimension, it says so plainly and carries the attempt forward — never quietly ships at par.
3. **Benchmark against the best in the genre, not against ourselves.** Each series keeps studying the top channels in its genre (owner directive 2026-11-01) and imports one concrete technique per cycle into the playbook; self-referential improvement alone plateaus.
4. **No gate is a ceiling.** Passing the prosody/caption/moment gates is the entry ticket, not the quality claim; the claim is the pushed dimension, evidenced.

## DEMO-FLOPS COMPILATIONS — FOOTAGE & LOOP DIRECTIVE (owner, 2026-11-02)

The owner, 2026-11-02: "Make good compilations of tech demos. Interesting stuff. Just best best high quality footage — the footage themselves should be entertaining — and you have a loop, and the narration, everything amazing." Standing consequences for every compilation (and, where they fit, singles):

1. **Footage quality is a gate, not a preference.** Source the cleanest, highest-resolution copy that exists for every moment; log each clip's source quality (resolution, watermark/clean status) in research-check.md. A watermarked or muddy re-upload is used only when no cleaner copy exists, and that is disclosed in the audit.
2. **The footage itself must be entertaining.** Selection favors moments that are inherently watchable — the room's reaction, the presenter's save, the presenter's face — over merely-documentary seconds. A beat whose best available footage is dull fails selection, however famous the flop.
3. **Loop structure.** Compilations are built to loop: the outro hands back to the opening (final line/frame mirrors or calls back the first moment) so a Shorts rewatch feels seamless; the audit verifies the loop join (last frame → first frame, last line → first line).
4. **Narration stays at the top standard** — Prosody Gate v2.1 with the word-level curve; "amazing" is measured, not asserted.

## THE NAME RULE (owner catch, 2026-10-29)
The subject's FULL NAME is spoken in the narration within the first lines after the cold open — every episode, Shorts and longs. §9's "identification-before-information" failed in practice because it meant a human fact, not the name: both the Musk Ep.2 build and the Jensen definitive shipped with narration that only ever said "he" (98s of Musk without one spoken "Elon Musk"; the Jensen definitive names NVIDIA but never Jensen Huang). A feed viewer who doesn't recognize the face or voice must still hear who this is. Title/cover/metadata naming does NOT satisfy this rule — the video itself names its subject, out loud, early.

## PACE RECALIBRATION (owner verdicts, 2026-10-29)
The slow series default (~0.365–0.373s/word) overshot: the owner judged BOTH the Musk Ep.2 narration and the Jensen definitive's narration "too slow." Working anchor is now ~0.33s/word (narration ~10% faster than the overshoot), bites always at natural speed. The earlier "considerably slower" correction was directionally right against the v2 hypercut (0.303 with dense cutting) — the settled zone is between the two: measured, per-episode, and always subordinate to the owner's ear at the verdict gate.

## Lessons from the benchmark test cut (owner-shared, 2026-10-29)
- SIGNATURE-LINE HUNT: before declaring a subject's famous line "narration-only," search their long-form podcast/interview appearances for the line IN THEIR OWN VOICE. Case: Jensen's "thirty days from going out of business" motto — our sourced pool had no clip and we concluded none existed; it exists in JRE #2422 (Dec 2025), along with "We would have vaporized instantly" (the 1997 payroll story). The long build now uses his voice for the motto.
- SOURCE LINES ON GRAPHICS: the test cut burns a small attribution line (source + date) into its data graphics (JRE #2422; CNBC; WSJ; NVIDIA press release). It reads as credibility, costs nothing — adopt for data graphics where a source is not already on screen.
- ONE-QUESTION REFRAIN: the test cut asks its open-loop question verbatim twice (open + ~60% reframe before the payoff). Worked as a retention refrain; keep our re-hooks varied in wording EXCEPT when a single question is the episode's spine — then a verbatim refrain is allowed once.

## NARRATION STANDARD v2 (owner verdict + overhaul, 2026-10-31)

Owner's verdict on the shipped catalog: the narration is the "very low floor" — speed, loudness and pitch wobble unnaturally across each video and it runs flat inside chunks; it doesn't flow like a human talking. Measured diagnosis (full research + data: `~/workspace/financial-clarity/narration-standard.md`):

- Shipped Short (money-market): per-chunk pace CV **10.3%**, chunk loudness range **2.8 LU**, F0 center wandering ~10 Hz chunk to chunk. One uniform atempo fixed only the average.
- Jensen long: raw chunk pace 0.219–0.480 s/word was FORCED to target with per-chunk atempo **0.78–1.28**, and narration loudness was never normalized (4.6 LU range went to air). Both practices are **banned**.
- Engine facts (measured): our TTS is near-deterministic per (text, speed) — re-rolling a miss is futile, steer the speed instead; long single-pass generation is a tempo lottery (74–135 s for the same 170 words) — banned as a consistency strategy; the Shorts music bed was fixed-volume, unducked — now sidechain-ducked (engine patched 2026-10-31).

THE STANDARD — all narration is produced by `~/workspace/financial-clarity/shorts/narration_v2.py`:
1. Segments are full thoughts (~25–60 words), generated at a fixed starting api speed (115) with **speed-search regeneration**: a take needing >±7% pace correction is regenerated at a steered speed (≤3 attempts, best take kept).
2. **Pause shaping in the sample domain** (speech untouched): head/tail 0.05 s; internal pauses capped 0.50 s / floored 0.18 s; segment joins exactly 0.65 s. **Decay-preserving (2026-11-02, G9 fix):** the −40 dB pause detector only *segments* pauses — cut points are extended into each pause until the envelope falls below −58 dBFS sustained, so the previous word's decay and the next word's soft onset are kept as real audio; splices to silence carry micro-fades (4 ms; 25 ms when a take ends abruptly). The pre-fix shaper replaced whole detected pauses with zeros and amputated audible word-final decay at ~2/3 of boundaries.
3. **Atempo bounded [0.90, 1.10]**; anything beyond ±7% is flagged by segment name in the gate report. Never force.
4. **Static per-segment loudness normalization to −20 LUFS before assembly.** No dynamic normalization on the voice, ever. Loudnorm happens once, on the final mix (I −14, TP ≤ −1).
5. **Master chain (once)**: highpass 70 Hz → de-ess −2 dB @ 6.5 kHz → compressor 2.5:1 (−18 dB threshold). Music sidechain-ducked to sit ~16–20 dB under the voice while it speaks.

PROSODY GATE — mandatory in every build's audit.md (the tool emits `<stem>.gate.json`; copy it in). A failed gate means re-voice, never ship:
- G1 per-segment pace CV ≤ 6% · G2 max pace deviation from target ≤ 8% · G3 segment loudness range ≤ 2.0 LU (SD ≤ 0.8) · G4 every atempo within [0.90, 1.10], >±7% flagged by name · G5 F0-median spread ≤ 18% (always reported) · G6 pause grammar verified in the final stem (joins 0.65 s, no internal pause > 0.90 s, no head/tail silence > 0.10 s) · G7 final mix −14 ± 0.5 LUFS in ONE loudnorm pass (a corrective pass = gate failure note) · G8 voice, target pace and speed-search log recorded.
- **G9 TAIL INTEGRITY (2026-11-02, owner ear catch — see the v2.2 section below):** every build must (a) measure segment-final decay on the shipped stem — for every boundary (joins AND internal pauses), the RMS of the final 30 ms before the boundary silence vs the segment's last-word peak; PASS = no boundary with final-30 ms RMS above **−35 dBFS** and the median at or below **−45 dBFS** (pre-fix catalog: median ≈ −29 dBFS, 100% of boundaries above −35); the engine's gate json pre-computes `g9_splice_max_db` (must be ≤ −50) and `g9_tail_final30_max_db` (must be ≤ −40) per narration — copy them in; (b) ASR-verify the FINAL WORD of every segment against the script on the shipped stem (whisper at 16 kHz; the word must transcribe completely, not a truncated near-miss like "offered"→"off"); (c) report both in audit.md. A failed G9 means re-shape/re-voice, never ship.
- Proof on file (`narration-proof/`): same 170-word script both ways — pace CV 23.8% → **1.58%**, max pace deviation 29.7% → **3.64%**, segment loudness range 1.74–2.8 LU → **0.01 LU**. Listening files: `proof_OLD_way.mp3` vs `proof_NEW_way.mp3`.
- Honest ceiling: Helio exposes only voice + a non-linear speed integer — no SSML, no emphasis or stability controls. v2 guarantees consistency, not new acting range. The documented step-change is ElevenLabs Creator ($22/mo annual, ~100 min v2 — see narration-standard.md Part 1/Paid options) or recorded human VO; either is an owner decision. The gate machinery is engine-agnostic and carries over.

## Longs Pace Standard v2 (owner verdict, 2026-10-31 — supersedes the "premium mini-documentary" drift for longs)

The owner, on the shipped Jensen and Bezos longs: "really not professional — too slow, nothing happening, just a slow AI voice telling a story with a picture in the background; not stimulating for people whose brains are on the web." Measurement backs him. Shipped-file scene detection (threshold 0.35) on the Jensen long: **41 shots in 667s = 3.7 cuts/min, mean shot 16.3s, median 9.0s** — and frame-difference checks prove the worst windows are truly near-static: the cold open holds essentially one frame from 0:03–0:39 (mean abs diff 1.2–1.7), and the concept chapter opens on a ~46s zoom-only hold. Build-plan data for the Musk long: 93 visual beats / 623s = 9.0 beats/min, mean beat 6.7s, with single unbroken visuals of 25.9s (Ch. 6 ledger bite) and 22.5s (Ch. 8 JRE bite). Bezos plan: ~7.9 beats/min, with 34.7s (Ch. 2 Academy carry) and 32.6s (Ch. 7 Princeton payoff) single-item spans. Reference class (researched 2026-10-31): a 4,412-scene production sample of long-form faceless videos (OverseerOS) has median scene 3.62s (≈16 changes/min; openings 3.20s); talking-head/vlog norms run 10–30 cuts/min (CutScore); fast documentary channels (Magnates Media class) cut at ~2–4s. Our longs shipped at roughly half to a quarter of the reference cadence. The story rules were never the problem — the frame went to sleep inside good stories.

**Reconciliation with the series rules:** the Structured Narrative Pacing rule still governs the STORY — chapters, motivated beats, fact density, one visionary. This standard governs the FRAME inside that story. The story may breathe; the frame may not. We do not shred narration into jump cuts and we do not cut against meaning: we add visual events *inside* long narration spans (sub-shot cutaways, graphic state builds, punch-ins, splits) so a 15-second sentence no longer means a 15-second picture. Where the Archival Speech Pacing section's "~2s no-hold cap" conflicts with this section for LONGS, this section governs (the 2s cap stands for Shorts).

### Numeric rules — every long must pass all of them

1. **Cadence floor:** ≥11 visual changes/min across the whole video (target 13–16). Mean shot ≤5.5s, median shot ≤4.5s, measured on the shipped file (scene detection + shot log), not the plan.
2. **Hold caps:** no static or near-static frame — photo, treated still, freeze, or talking head — held longer than **6s** without a visual event (hard cut, ≥115% punch-in, overlay/graphic state change, split). Absolute cap **8s**, allowed only for a chart the viewer must read, and the chart must still be building or annotated during it.
3. **30-second rule:** no 30s window may contain fewer than 5 visual events. (The Jensen long's first minutes fail this repeatedly — most 30s windows in 0:00–2:30 contain ≤2 shots.)
4. **Talking heads:** archival speech stays in ~2–4s on-camera bursts (standing rule). Any voice carry longer than ~5s runs under cutaways that change every ≤5s; the speaker's face may return for the closing line only. On-camera talking-head share ≤25% of runtime.
5. **Stills/photos:** never bare. Every still gets a move (≥8% scale travel or a pan) AND, if on screen >4s, a mid-hold event (super landing, highlight, split, or cut).
6. **Graphics cadence:** a designed graphic, super, or chart state change at least every **20s** (the Bezos long shipped at ~35s — too sparse). Data graphics animate in states; a finished static graphic may not sit unchanged >5s.
7. **First 30 seconds (fastest window):** median shot ≤3.2s, no single visual >5s, and the hook picture is the strongest MOTION asset in the piece — never a treated still or a stage wide-shot. (Jensen's cold open — one near-static frame for ~35s — is the named failure this rule exists to prevent.)
8. **Minutes 1–3:** a re-hook visual set-piece (chapter turn, split-world, full-screen graphic, natural-sound moment) lands by 2:30–3:00 at the latest. Every chapter boundary is marked by a visual event, never a quiet cut.
9. **Pattern interrupts:** at least one every 45–60s (full-screen graphic, split, music change, natural sound, kinetic type) — inside chapters, not only at their edges.
10. **Bite staging:** long verified voice carries (the SES-10 ledger class, the Princeton payoff class) are staged as *voice under building graphics/footage*, with the face bookending the passage — never as one unbroken on-camera hold, however good the audio is.

### PACE GATE — mandatory in every long's audit file (measured on the shipped file)

- [ ] Shots/min, mean shot, median shot (scene detection, threshold stated)
- [ ] Longest near-static hold + its timestamp (frame-difference verified, not just scene detection — gradual montages hide from scene scores)
- [ ] Worst 30s window: fewest visual events + its timestamp
- [ ] First-30s: median shot, longest single visual
- [ ] Talking-head on-camera seconds / % of runtime
- [ ] Longest gap between graphic/super/state changes
- [ ] Chapter-by-chapter beat table (beats, mean, longest) from the shot log
- Any FAIL = the video does not ship. The gate numbers are reported at delivery alongside the existing audit items.

## Demo-flops series rules (owner verdict, 2026-11-01)
- NO education/investment-advice disclaimer in demo-flop videos — not spoken, not on screen, not in the description. These are tech-history videos; the disclaimer is channel practice for finance-advice content only.
- ORIENTATION INTRO, every episode: the opening seconds must tell a cold viewer what they are about to see and what they are looking at (event, product, stakes) BEFORE the fail moment plays. Owner's catch on the Face ID cut: the unlock footage played and "you don't know what you're seeing." A cold viewer must never wonder what event they're watching.
- The owner's eye is the final gate on this series: his "can be redone 10x better" verdict on the first three cuts sent all of them back for a raise-the-bar revision pass (intro rebuild + disclaimer removal), 2026-11-01.

## Consistency + external-review rule (owner directive, 2026-11-01)
- ONE locked professional structure for every video, applied identically across all series: orientation intro → paced story beats (Pace Standard) → narration per Narration Standard v2 + Prosody Gate → Graphics Standard v2 → sound design → full verification. Editing, cutting, visuals, voice, narration, storytelling — no per-video improvisation of the structure; quality compounds because the structure is fixed and only the content changes.
- EXTERNAL AI REVIEW OF THE FINISHED CUT: before any video is delivered to the owner or uploaded, the finished cut must be shown to at least two external AIs (free no-login surfaces) for critique — using the best representation the surface accepts (the file itself where possible, otherwise contact-sheet frames + narration audio/transcript + shot list + gate metrics). Their verdicts are logged in the package's consult-log.md; material findings are fixed or consciously waived in the audit with a reason. External opinions are critique, never authority — verified facts still come from the research packages.

## Creative license + benchmarking (owner directive, 2026-11-01, refines the rule above)
- The locked structure is the FLOOR, not the ceiling. Muse has standing creative authority to change the structure, editing approach, or format whenever a change makes the video better — "it doesn't have to be the exact structure I give you." Deviations that win become the new standard; the playbook updates to match what worked.
- BENCHMARK STUDY is part of every flagship build: before finalizing, study the best YouTube channels in the video's genre (for demo-flops: top tech-fail/compilation and high-retention Shorts channels), extract concrete techniques (hook mechanics, pattern interrupts, caption craft, sound design, punch-ins, retention editing), apply what fits, and log what was borrowed and from whom in the consult log.
- Demo-flops formats are OPEN: singles, compilations, rankings, timelines — "all types." Format follows whatever serves the material and retention best.

## Prosody Gate v2.1 — the ear correction (owner verdict, 2026-11-01)
The owner rejected the revised Cybertruck cut BY EAR ("the voice changes from slower to fast") although its segment-average gate passed at CV 1.29%. Lesson, standing: segment-average pace is NECESSARY, NOT SUFFICIENT. Every narration sign-off now also requires (1) a WORD-LEVEL pace curve (ASR word timestamps; per-phrase pace vs the stem median; swings fixed by take selection or re-voice, not by post-hoc stretching), and (2) external review that includes the actual AUDIO wherever a surface accepts it — a text/frames-only review structurally cannot hear pace and must never be reported as a listening review. The owner's ear remains the final calibration; a gate pass the ear fails is a failed gate, and the failure gets diagnosed at word level, not argued with.

## Prosody Gate v2.2 — the tail-integrity correction (owner verdict, 2026-11-02)
The owner, listening to the shipped catalog: "words keep on getting cut off — by the end you can't hear it; it doesn't sound like a clear soundtrack." He was right, and the segment-average gate could not see it. Forensics on 7 shipped masters (full report: `~/workspace/financial-clarity/audio-tail-audit-2026-11-02.md`): the v2 pause shaper defined "silence" as 10 ms windows under −40 dBFS and replaced every detected pause region with digital zeros. Word-final decays (vowel tails, fricative/plosive endings) spend 0.05–0.29 s between −40 and −55 dBFS, so they were classified as silence and deleted: on shipped stems the median boundary was cut while the voice was still at **−29 dBFS** (final-30 ms RMS), worst −19.7, and **100% of measured boundaries (74/74 on part-b-penalty) were cut above −35 dBFS**. ASR proof: whisper hears the script's final word in the raw TTS take but not in the shipped segment in **9 of 24** sampled segments — always the final consonant/syllable eaten ("offered"→"off", "entirely"→"entire", "doesn't"→"does", "floor"→"law", "month"→"moment"). A secondary engine bug compounded it: empty bookend speech segments made head/tail pauses classify as "internal," so segment tails carried up to 0.50 s of zeros instead of the intended 0.05 s. NOT causes (measured and cleared): atempo (applied after shaping; cannot restore deleted audio), per-segment loudnorm (static gain), the master chain, and the mix's apad/`-t VDUR` (every sampled master is longer than its stem — the final word is never cut by video duration).
FIX (in `narration_v2.py`, 2026-11-02): decay-preserving pause shaping — cut points extended into each pause until the envelope falls below **−58 dBFS sustained 30 ms**, scanning the run's whole decay region so a fricative tail hiding behind a closure dip survives ("next." → /kst/); onset pre-roll symmetric; 4 ms micro-fades at splices (25 ms adaptive when a take ends abruptly); head/tail classification fixed. Proof (part-b-penalty narration regenerated in scratch, nothing shipped touched): splice levels worst **−59.5 dBFS** (engine log, all 58 splices), stem boundaries above −35 dBFS **74/74 → 0/54**, median boundary final-30 ms **−28.1 → −50.2 dBFS**, ASR final words **3/6 mangled → 6/6 complete**. Standing gate: **G9** (above). Segment-average pace was necessary, not sufficient — now the END of every word is gated too. The owner's ear remains the final calibration.

## ⭐ TAB STANDARD — narration gate v3 (owner ultimatum, 2026-11-08)
Owner: in-house voiceovers are "terrible compared to Tab — a million times better"; in-house must reach his level or the channel runs on Tab's videos only. Measured comparison of 5 Tab masters vs 4 in-house mixes + their Helio stems (full data + diagnosis: `narration-proof/tab-standard-2026-11-08.md`, tool `narration-proof/tabstd_measure.py`). Headline findings: overall pace is NOT the gap (≈0.35 s/word both). The gap is architecture: **(1)** Tab's pauses sit over a bed only ~9.7 dB under his voice — ours sit over near-silence at ~16.6 dB (the old "music 16–20 dB under" rule specified the losing number); **(2)** Tab's word loudness SD is 2.0–2.2 dB, ours 2.6–4.2 dB — per-segment static normalization leaves word-to-word wobble inside segments; **(3)** Tab speaks in 7–10-word bursts with holds up to 3.1 s, our scripts run 12–16-word clause chains and the engine quantizes joins to exactly 0.65 s with a 0.90 s pause cap that makes his signature hold illegal; **(4)** Gate v2.2 graded the wrong axis — rent-vs-buy shipped at pace CV 0.17% (a metronome) while Tab runs 13–29% phrase-pace variation and the owner called his 16.1% Costco read "very very good."
**Standing rules:** Gate v2.2 **G1 and G6 are superseded**; G7 (loudness) and G9 (tail integrity) retained. No in-house build is shown to the owner unless the shipped stem + mix pass **TS1–TS8**: TS1 phrase pace 0.31–0.37 spw with 5 s-window CV **10–25%** (floor and ceiling) · TS2 ASR breath groups ≤ 11 words mean, none > 20 · TS3 pauses ≥ 0.5 s ≥ 40% of pauses, scripted `[HOLD]` beats 0.9–1.5 s land, no two consecutive joins equal · TS4 word-RMS SD ≤ 2.5 dB (bounded ±2 dB word-levelling pass, N2) · TS5 mean declination ≤ −1.0 st/s, within-segment F0 range ≥ 7 st · TS6 final-mix speech−bed 8–13 dB, no dead-air gap ≥ 0.4 s · TS7 stem voiced share ≥ 47% · TS8 = G7 + G9. **Scripts** are written to the standard before voicing: ≤ 10-word breath groups, payload word at line end, figures on their own beat, `[HOLD]`/`[PRESS]`/`[LAND]` annotated. Path: fix script + mix architecture on Helio first (free), then a gated ElevenLabs Brian A/B (needs Creator plan — owner money decision; 66 free credits left, free tier is non-commercial).

## Feedback record — 2026-11-02 tail-integrity forensics (owner ear catch)
- OWNER REPORT (2026-11-02 ~19:56 EST): in many videos, narration words get cut off at the end; the soundtrack doesn't sound clean. Directed: keep quality at "perfect perfection," show finished videos fully to outside people/consultant AIs.
- FINDING: confirmed and measured — pause-shaper tail amputation (see v2.2 section above). Present in every sampled build (6 finance Shorts + Compilation #4): 49–71% of raw-take boundaries discarded a run whose peak was above −38 dBFS with ≥0.08 s of audible decay; shipped-stem boundary cuts at median −29 dBFS. The defect is in the shared engine, so it is catalog-wide for everything built on narration_v2 since 2026-10-31, not per-video.
- EXTERNAL AUDIO REVIEW: still no outside AI has heard our audio. Routes tried 2026-11-02 (log: `~/workspace/financial-clarity/audio-review/consult-log-2026-11-02.md`): Pollinations audio chat API — 401 (key now required); llm7 — model unavailable, no audio route; HuggingFace router — 401 (token required); Claude — no audio upload exists; ChatGPT — audio attach is paid-plan only. Google Gemini's app accepts audio uploads (≤10 min free tier) but only through the interactive browser, which the forensic agent cannot operate — the extracted soundtrack (`audio-review/part-b-penalty-full.mp3`) is staged for a parent-run browser session. Text/frames reviews remain what they are: not listening reviews, never reported as such.

## Effort + structure refinement (owner directive, 2026-11-01 01:19)
- The formulaic HOOK/PREAMBLE is LIFTED. Do not force a hook structure. Open on the strongest moment; orientation is still required but delivered FAST, inside the opening action (super + narration over the fail footage), not as a separate preamble. External-AI structural critique is presumptively right — override it only for verified facts or research locks, never for habit or formula.
- NON-NEGOTIABLE: real research. Verified facts from primary sources are the one place no shortcut is ever taken; structure, editing, and style all flex around the research, never the reverse.
- PRODUCTION: use the best available technology and studio-grade options at every step — graphics, editing, rendering, transitions/flows. Effort per video is the standard: "work and work" — a video that took the tremendous-effort path and lost to a check gets another loop, not a shrug.

## Framing rule — subject placement in vertical cuts (owner catch, 2026-11-01)
Owner, watching Face ID: "their faces are like in the side, phones in the side — what you see in the final is very cut narrow." Standing rule for ALL vertical (9:16) work using landscape/archival footage: fixed center crops are BANNED as the default. Reframe subject-aware: track the subject (face, product) and keep it in the central zone of the vertical frame, moving the crop window to follow it; never ship a shot with a face clipped at the frame edge or a product half-amputated. Where no crop can hold the subject properly, compose instead — footage in a designed window over a branded background — rather than forcing a bad crop. Audit addition: pull a frame from every shot and verify subject placement explicitly (face whole and in-frame, product whole), listed in the audit; a framing failure is a build failure.

## Feedback record — 2026-11-01 traction check (jensen-traction-check-48h)
- YOUTUBE DISTRIBUTION LESSON (measured, Studio read Nov 1, 9:28–9:41 AM EST): channel at 26 subs (27 → 26 vs Oct 29), 222 views/28d, realtime 92 views/48h (up from 65). NO video is being feed-pushed yet: every video sits at 1–18 views with 1 unique viewer on the deep-checked set. The definitive Jensen (8 views) and the survival cut (5) both show **0% Shorts-feed traffic** — their views came via channel pages/search/other features (our own network) — so the definitive-vs-survival hook comparison is INCONCLUSIVE by distribution, not by content: an A/B hook question is untestable until a cut actually gets feed impressions, and hook debates should not be re-litigated on own-network views. Stayed-to-watch of 100% on 2 engaged views and AVDs like 39:44 on a 79s Short are loop artifacts — never quote them; the 70%/60% playbook thresholds can only be judged after a video passes a few hundred feed views. Musk Ep.2 is the relative bright spot on BOTH platforms (YouTube: 18 views, only key test with real feed share at 27.8%, 88.9% stayed on the largest engaged sample of 8; TikTok: 111 views, only video over 100) — famous-name + bet-everything founder stories are the best-tested format so far. Oct 30 batch: Gates/Karp/Bezos Short tie at 11 views; nothing broke out. (Full snapshot: ~/workspace/goals/they-saw-it-coming-founder-series/hidden_files/analytics-2026-11-01.md.)
- TIKTOK FLOOD LESSON (measured, TikTok Studio owner view, Nov 1 ~09:00 EST): @markets.clarity stands at 0 followers, 3 total likes (2 are the owner's own → 1 organic), ~206–223 total views. ONLY the first 3 videos posted on Oct 30 ever received views (survival cut 31, Jensen definitive 64, Musk 111 — Musk still the account's strongest). The other 16 videos — including everything posted later on Oct 30, both Oct 31 posts, and the Nov 1 IRMAA post — sit at exactly 0 views. A 0-view video was never test-pushed; it is UNTESTED, not rejected, and its numbers must never be read as a per-video verdict. Flooding a day-old zero-follower account with 16 videos in a few hours stalled distribution at the account level. Standing rule CONFIRMED by data: YouTube uploads immediate; TikTok cross-posts spaced 2–3/day, strongest first; never re-flood. (Snapshot: ~/workspace/goals/they-saw-it-coming-founder-series/hidden_files/analytics-2026-11-01.md — note the YouTube half of that check is marked unmeasured there; its Studio reports never reached the run, and the YouTube verdict carries to the Monday weekly loop.)

## Feedback record — 2026-11-02 weekly loop (channel-feedback-loop-weekly)
- SUBSCRIBER + REALTIME BREAK (measured, Studio read Nov 2, 10:42–11:02 AM EST; 28d window Oct 5–Nov 1): subscribers **26 → 31** (+5 since Nov 1, +4 in the 28d window), 28d views 222 → **320**, watch 20.1h → **29.9h**, realtime **92 → 223 views/48h**. First real movement since launch — but it is ONE video, not a channel-wide lift (see next lesson). Do not read this as the catalog working.
- MUSK LONG IS THE PROOF AND THE WARNING (measured): the Musk long re-cut "The Rocket Everyone Threw Away" (7DAR3YehprE, live Nov 1) is the channel's biggest long by an order of magnitude — **44 views since published, 4.1K impressions, traffic 70.5% Suggested** — the pace re-cut standard CAN get Suggested distribution. Its CTR is **0.3–0.4%** (Nov 1 funnel: 3.5K impressions → 12 views from impressions). Channel long-form CTR is **0.6%** overall vs Burry long's **9.1%** (on only 88 impressions) and Bezos/Jensen longs at 2.6–3.3%. LESSON FOR NEXT BUILDS: for longs, title + thumbnail CTR is now the #1 measured bottleneck — YouTube is offering our longs in Suggested and viewers are not clicking. Next long ships only with a CTR-first package: title/thumbnail tested against the Burry long's 9.1% pattern (specific name + concrete stake), not against our own recent covers. Impressions without CTR do not compound.
- SHORTS STILL NOT FEED-DISTRIBUTED (measured): Shorts feed is only **27.1%** of 28d Shorts traffic (other features 28.3%, search 14.6%); individually, Compilation #1, Bard, Social Security earnings-test and the Nov 2 Catch-Up Short all show **0% feed**. Stayed-to-watch channel-wide 75.2% (vs 77.1% Nov 1) on 88 engaged views — still too small to judge hooks. The Nov 2 batch of 12 Shorts sits at 2–7 views each, all own-network/search. LESSON: distribution, not hook quality, remains the Shorts bottleneck; do not re-litigate hooks/titles on 0%-feed videos.
- DEMO-FLOP COMPILATION GROWS VIA SEARCH, NOT FEED (measured): Compilation #1 "5 Tech Demos That Failed in Front of Everyone" **5 → 16 views** (top Short in realtime 48h), stayed **66.7% on 8 engaged** — the largest new engaged sample — with traffic search 37.5% / other 31.3% / feed 0%. Face ID 6 → 10 views, stayed 75%. Cybertruck Short is the weak signal: stayed **33.3% / swiped 66.7%** (engaged 1, tiny — directional only). LESSON: demo-flop compilations are currently the best Shorts bet and are searchable evergreen topics; keep making them (per the 2026-11-02 compilations directive), title them for search phrasing viewers would type, and do not judge the Cybertruck single by this sample alone.
- FOUNDER SHORTS STALLED (measured): Bezos Short flat at 11, Dell 4, Ellison 4, Jobs 2, IRMAA flat at 2, Jensen long flat at 3, Bezos long flat at 4; Karp 11 → 12 and Gates ~10 → 11 are trickle only. LESSON: the Oct 30 founder batch has exhausted its own-network audience; new founder episodes need a distribution lever (compilation/search-led entry or a long that earns Suggested), not just another upload into the same pool.
- (Full snapshot: ~/workspace/goals/they-saw-it-coming-founder-series/hidden_files/analytics-2026-11-02.md. Caveats carried forward: per-video subscribers gained = "—" everywhere, retention reports unpopulated on Nov 1–2 videos, Shorts AVDs are loop artifacts, and Studio's Content vs Analytics counts disagree on several older Shorts.)

## THE MOMENT RULE (owner catch, 2026-11-01)
In demo-flops — and any fail/reveal/event content — the ACTUAL MOMENT of the event must be on screen: the ball hitting the glass, the crack forming, the error appearing. Showing the wind-up and then the aftermath is a defect, however good the rest is; the moment is the product. Every build's audit must include a moment table: each claimed event beat, the timestamp of its actual moment on screen, frame-verified. (Owner caught the Cybertruck cut showing before/after of the SECOND break but not its impact; the upload was stopped and the beat re-edited.)

## ⭐ THUMBNAIL RULE — GEMINI ALWAYS (owner, restated 2026-11-02 21:23 EST)
Every thumbnail/cover for every video on this channel is generated with GEMINI — the owner rates it the best thumbnail maker. This covers Shorts covers, long-video thumbnails, rebuilds, and The Close daily episodes. Engine-rendered cover frames are a fallback only when Gemini is unreachable, and that must be disclosed in the audit. The owner's OWN thumbnails are never replaced (SCHD vs VOO long = his; Musk long variant B = his pick). Judge at phone size (320px); face never covered by text/graphics.

## ⭐ FRAME-0 RULE (owner, 2026-11-02 ~21:38 EST — channel-wide, all Shorts, both platforms)
Frame 0 is the swipe-stopper: the FIRST frame of every Short must be a designed, graphic-rich hook frame — the day's/topic's defining visual + big number or image + (for dated content) the date — never a plain title card or a bare talking/background frame. "It looks so boring no one would click; people just swipe." The frame-0 frame is audited in every build (pulled and eyeballed at phone size) and doubles as the cover wherever the platform takes the first frame. Applies to TikTok exactly as to YouTube.

## ⭐ TRIPLE HOOK RULE (owner, 2026-11-06 ~03:17 EST — channel-wide, all Shorts, both platforms)
Owner: "Use a triple hook... swipe hook, all the hooks." Every Short opens with THREE hook layers stacked inside the first ~2 seconds, all hitting at once so the video survives the feed swipe test:
1. **VISUAL hook** — the Frame-0 designed swipe-stopper (rule above): the defining visual + big number/image on frame 0.
2. **SPOKEN hook** — the first narration line IS the hook: the specific dollar / loss / contradiction lands immediately, no warm-up, no preamble.
3. **TEXT hook** — big kinetic on-screen text reinforcing the spoken hook in the same first seconds.
All three layers must be the video's genuine strongest moment/number — stacking real hooks, never manufactured gimmicks (the "do not force a hook" rule still stands). AUDIT GATE: every build's audit verifies all three layers present and landing within the first 2 seconds of the shipped file; a build missing a layer fails.

## THUMBNAIL TOOL UPDATE (owner, 2026-11-02 ~22:22 EST)
Owner: "if you can find a different tool that you can use use it." Muse's own image generator is now a fully authorized thumbnail route, EQUAL to Gemini — use whichever produces the best result and is reachable; a blocked tool never blocks a thumbnail again. Proven 2026-11-02: the generator produced The Close Ep.1 thumbnail ("BEAT EARNINGS... STILL FELL!") with perfect text rendering, applied the same night. Gemini remains welcome when its sign-in works. The owner's own thumbnails are still never replaced.

## STIMULATION + NARRATION-PERFECTION STANDARD (owner, 2026-11-02 ~22:48 EST)
Owner, after watching recent videos: "we shouldn't have too much empty spaces in videos — things should constantly happen, should be like rewarding dopamine videos to look at" and "make sure the words… the talking is perfect, the narration is perfect."
- NO DEAD SPACE, channel-wide (all series, all Shorts): something new on screen every ~1–3s — a cut, a graphic event, a number landing, a footage move. No static holds, no narration over emptiness, no silent gaps except a deliberate designed beat (e.g. Galaxy Fold's 1s of true silence before a verdict — intentional, audited, rare).
- Every audit includes a dead-space scan (visual AND audio) alongside the pace/static checks; a video with empty stretches fails.
- NARRATION PERFECTION IS A SHIP GATE, not a preference: fixed engine + Prosody Gate v2.2 incl. G9 (no cut-off words — splice and ASR final-word proof on the shipped file) + word-level pace curve. A gate pass the owner's ear fails is a failed gate.
- VOLUME STRATEGY (owner decision): more high-quality videos = more discovery chances; volume WITH the quality gates held, never volume instead of them.


## ⭐ VIRAL STANDARD (owner directive 2026-11-03 ~00:51 EST, from the commissioned virality research — full report: ~/workspace/research_notes/viral-finance-shorts-brainrot-research-20261103-0551/report.md)

Owner: "stay within the niche but I want real brain rot content that the audience is hungry for. Virality." Research verdict: virality = retention architecture, not topic. Standing rules for all new Shorts builds until superseded:

1. **LENGTH: default 35–55 seconds.** Evidence: quso.ai (108,138 matured Shorts) median views 901 (11–20s) → 188 (46–60s) → 51 (90s+). Our historical 60–100s band is the hardest on the platform. 60s+ ONLY for countdowns/battles/compilations with re-hooks ≤15s apart.
2. **HOOK: a specific dollar / loss / contradiction on frame 1, spoken + on screen within the first 2 seconds.** Benchmarks: viewed-vs-swiped-away 70–90% = strong distribution, <60% = collapse; ~half of all leavers leave within 3s; a first-2s hook retains ~+19%.
3. **RETENTION ARCHITECTURE:** visual reset every 2–4s; a new open loop BEFORE each beat resolves; payoffs stacked, biggest last; ending designed to loop into frame 0 (loop join verified in audit, as compilations already do).
4. **BRAIN ROT = "RELEVANT SLUDGE":** a live chart/race/counter running under the whole video as the constant stimulation layer — never unrelated gameplay footage. Stimulation density serves the content, not noise on top of it.
5. **CAPTIONS: word-by-word, 1–3 words on screen, bold condensed, numbers highlighted in a second color** (viral spec; replaces phrase captions on viral-format builds).
6. **PROVEN FORMATS (rotate):** mistakes/rules countdowns · "what $X becomes" growth races · stock/fund battles · earnings verdicts · fine-print loopholes. Every build names its format and its pushed dimension (Compounding Directive still applies).
7. **MONETIZATION FENCE:** YouTube's July 2025 "inauthentic content" policy — mass-produced interchangeable templated AI content is YPP-ineligible, judged channel-wide. Differentiation per video (original research, unique structure/graphics) is a monetization requirement, not taste.
8. First builds under this standard (2026-11-03): The $10,000 Race (VOO vs QQQ) · 5 IRS Numbers countdown · The Cost of Waiting (three-age race).

## MOMENT-FIRST PRIORITY (owner verdict, 2026-11-03 ~02:38 EST)
The Houses explainer verdict: "not a bad video but it's not something that goes viral viral viral." Standing priority: MOMENT-FIRST content leads the pipeline — real footage, real faces, can't-look-away seconds (demo-flop compilations, founder archival moments). Proof point on this channel: the Musk 1998 moment video (19K TikTok views) vs every explainer. Explainers continue as the steady base (comments/saves engine); the biggest production swings go to moments. Followed immediately by: "now we can focus on high high high high quality viral videos" + "post it when it's done" — the standing upload-on-verified-delivery rule reaffirmed.

## CONTINUOUS SELF-IMPROVEMENT RESEARCH (owner directive, 2026-11-03 ~02:50 EST)
"I need you to become better and better. I need you to consistently research yourself how to become better, what are the best tools you can use... quicker, better, more professional, better audio. Always think about it." Standing practice: a recurring frontier-research pass on (1) audio quality (the known low floor — engines, voices, settings, mastering), (2) production speed/tooling, (3) craft techniques from the best channels — findings land as adopt/test/ignore verdicts with sources; measured A/B tests for anything that would replace a settled choice (e.g., the Helio v2 decision is re-openable only with new measured evidence). First pass: research/audio-tools-frontier-2026-11-03.md.

## FRONTIER RESEARCH — ROUND 1 FINDINGS (2026-11-03)
Report: ~/workspace/financial-clarity/research/audio-tools-frontier-2026-11-03.md. (1) ElevenLabs now has a generation-time speed setting (0.7–1.2) — the 2026-11-01 pace blocker is mathematically fixable for Brian/George; Test A (free, within remaining credits) commissioned 2026-11-03 to measure it; adoption still requires the owner's ear. (2) Cartesia Sonic = candidate #2 (speed 0.6–1.5, $5/mo) — needs an owner account step. (3) ADOPTED for iteration renders: critique cycles run on the 540×960 render and/or libx264 preset veryfast (≈2.5× fps at SSIM parity, +1–2 CRF); MASTER encodes keep the quality settings. (4) Dead platforms, do not revisit: OpenAI TTS (shuts down 2027-01-06), PlayHT (shut down). Mastering chain: not the bottleneck; Auphonic finishing pass is testable only with silence-cutting disabled (G9 lesson).

## Feedback record — 2026-11-09 weekly loop (channel-feedback-loop-weekly)
- BREAKOUT REGIME CHANGE (measured, Studio read Nov 9, 10:43–11:04 AM EST; 28d window Oct 12–Nov 8): subscribers **31 → 46** (+15 in a week, +21 in 28d), 28d views 320 → **3,388** (10.6x), watch 29.9h → **60.5h**, realtime **223 → 2,413 views/48h**. Shorts feed share **27.1% → 73.4%** — the channel has moved from own-network/search distribution to real feed distribution for the first time. Do not compare retention percentages across the regime change without the sample note below.
- STAYED-TO-WATCH IS NOW MEASURABLE — AND IT IS 59.6% (measured): channel Shorts stayed **59.6% / swiped 40.4%** on **1,700 engaged views** (Nov 2: 75.2% on 88 engaged — that figure was a small-sample artifact and is retired as a benchmark). 59.6% sits just under the Viral Standard's <60% collapse line and well under the 70%+ strong-distribution band. LESSON FOR NEXT BUILDS: now that the feed tests at scale, retention — not distribution — is the Shorts bottleneck. The next lever is the first-2s hold and mid-video drop-off on feed traffic specifically, judged only on videos with 100+ engaged views.
- TESLA/MUSK LANE + JENSEN EMAIL = THE PROVEN FEED FORMULA (measured): the four breakouts are "They Paid $250,000 for a Car They Never Got" (Roadster, 933, feed 97.4%, stayed 56.9%), "Tesla's Ending the Cybertruck?" (~950, feed 95.0%, stayed **65.0%**, +1 sub), "The White House Tesla Showroom" (419, feed 95.0%), and "Nvidia's CEO Sent This Email..." (346, feed 96.8%, stayed 62.7%, +1 sub) — plus its sibling "Monday 9:30 AM" email Short (227, feed 95.2%, stayed **68.6%**, best measured). Top 4 = ~74% of all channel views. LESSON: famous-name + concrete-money-contradiction + a real moment/document (an email, a showroom, a paid-for car never delivered) at **0:39–0:50** is the best-tested feed format the channel has ever had. Weight the Tesla/Musk lane and the founder-email/document angle first in topic selection; the appeal bar and moment-first priority are now data-backed, not just owner-called.
- LENGTH LESSON CONFIRMED BY OUR OWN DATA (measured): every breakout is 0:39–0:50. The Oct 30 founder originals at 1:23–1:33 (Gates 20, Karp 15, Bezos 6, Dell 6, Jobs 2) and the entire Nov 2 retirement batch at 1:24–1:50 (20 Shorts, all still 0–4 views after a week) never earned a feed test at scale. This matches the Viral Standard's 35–55s default exactly. LESSON: keep new Shorts at 35–55s as the default; treat 60s+ as the exception that must justify itself (compilation/countdown with re-hooks), and do not read the long-batch zeroes as topic verdicts — they are length-plus-distribution untested, the same trap as the TikTok flood zeroes.
- FEED PUSH ≠ RETENTION — WHITE HOUSE WARNING (measured): "The White House Tesla Showroom" got the same 95.0% feed push as the other breakouts but held only **41.7%** stayed (vs Cybertruck-ending 65.0%, Monday email 68.6%). Same lane, same distribution, ~23-point retention gap. LESSON: a Tesla/Musk topic buys the feed test; the hold is earned inside the video. When a feed-pushed Short stalls under ~50% stayed on 100+ engaged, diagnose the opening seconds and first payoff timing before blaming the topic — and do not clone a weak-hold breakout's structure just because its topic worked.
- LONGS DID NOT FOLLOW THE SHORTS — CTR LESSON HARDENS (measured): longs are 193 views (5.3% of channel) on 5.5K impressions at **0.8% CTR** (Nov 2: 0.6%). Musk long 44 → **76 views** but CTR still **0.3–0.4%** on 4.5K impressions, and its traffic is now Advertising 44.7% / Suggested 42.1% — impressions are being bought/shown, not clicked organically at rate. Every new long is flat: SBF 2, Tech Flops 3, Cockroaches 5, Nvidia Memo 2, Debt long 2 (CTR 0%, though AVD 4:06 on 2 views is encouraging directionally). Burry long remains the CTR benchmark at **8.7%** (105 impressions, Search 60%) and Windows 98 long grew 7 → 34 via Search (67.7%) at 2.6% CTR. LESSON FOR NEXT BUILDS: unchanged from Nov 2 and now stronger — no new long ships without a CTR-first package benchmarked against the Burry pattern (specific name + concrete searchable stake), and Shorts success must not be read as long-form demand. The Shorts→long cross-link (debt pair) is live but at 2 views it is untested, not failed.
- SEARCH STILL WORKS AS THE SECOND ENGINE (measured): "Then He Said BUY" reached 83 views with **Search 84.3% / Feed 7.2%** (+1 sub) — the inverse of the breakouts — and Roaring Kitty (23) and Hwang (14) trickle at Search 100%. Windows 98 long's growth was also search-led. LESSON: keep one search-phrased title in each batch (the exact phrase a viewer types after a news moment) alongside the feed-first titles; search-led Shorts convert subscribers at the same +1 rate as feed breakouts on 10x fewer views.
- DEMO-FLOPS / FOUNDER ORIGINALS STALLED (measured): Compilation #1 flat 16 → 15 (realtime 0), Face ID 10 → 11, founder originals flat (see Length lesson). The Nov 2 read that compilations grow via search as evergreen did not continue — feed moment-Shorts have displaced them as the growth engine. LESSON: do not prioritise another compilation or another 90s founder cut on the strength of the old data; if a compilation returns, it returns at feed length with a moment-first cold open, or not at all.
- CONCENTRATION RISK (measured): 122 live videos, ~74% of views in 4. Volume alone did not lift the median video (median live Short is still ~5 views). LESSON: the volume thesis holds only as a search for the breakout format — now that a format is identified (see Tesla/email lesson), the next cycle should iterate tightly on that format (same length, same premise shape, new moments) rather than spreading across retirement explainers, CLOSE recaps, and long-tail topics that have never earned a feed test.
- (Full snapshot: ~/workspace/goals/they-saw-it-coming-founder-series/hidden_files/analytics-2026-11-09.md. Caveats carried forward: Studio surfaces disagree by window — Cybertruck 801/914/957 by surface is the largest spread; per-video subscribers are mostly "—" with only +4 attributed of +21; retention is still pending for Nov 7–9 videos beyond the stayed figures above; McDonald's/AMC AVDs in Overview are loop artifacts, single-source.)


---

## 2026-11-14 — Owner verdict on the first in-house build + the method rethink (appended, standing rules above unchanged)

- **Verdict (owner, ~21:25 EST):** the in-house Jensen resignation Short (v1, live:
  youtube.com/shorts/nE4pyWOQ4iI) "doesn't come close to Tab… everything, it's just
  flat." His diagnosis: Muse is "not using the right methods to build it" and must
  "rethink the whole way… use different tools, different methods." The TS gates passing
  is not quality; the gates measure narration uniformity, and uniformity is part of
  what read as flat.
- **Process (owner, ~21:27 EST, same night — this REVERSES the verdict-before-upload
  idea floated minutes earlier):** "Just keep on building and post. I won't be
  available for the next time, so don't keep asking waiting for my approval. Just try
  to fix it on yourself… try with new ways to build high level — high level shorts,
  high level longs, upload them, keep on doing it." Standing order: autonomous
  build-and-post for in-house Shorts AND longs under the rethought methods; no
  approval waits; his verdicts on posted work become written corrections here.
- **The rethink:** full teardown + proposal in `method-rethink-2026-11-14.md`.
  Headline rules adopted (v3 pipeline):
  1. **Frame-0 gate:** frame 0 is the finished hook poster (full-bleed, big type,
     furniture) and the audio starts hot (first-0.3s RMS ≥ median word level). No
     black fade-ins, no windowed photos on black.
  2. **Rhythm gate (EDL-first):** every edit is planned as a written EDL from a
     moment map; shot lengths must show contrast — min ≤0.6s, max ≥2.8s, CV ≥0.45.
     A uniform 0.8–2.0s band is a fail. Synthetic moves (zoom/punch) only where a
     static shot needs one and it means something — never as wallpaper.
  3. **Poster graphics, not slides:** Anton/Archivo Black, textured saturated fields,
     pill tags, arrows, source strip + channel bug as furniture; data drawn as
     pictures. Matplotlib/DejaVu card rendering is retired.
  4. **Caption grammar:** 2–3-word chunks, big stroked condensed type, active phrase
     in a highlight pill, timed from word timestamps. Clause-length plain subtitles
     are retired.
  5. **Sound signature:** SFX budget ≤8 placed events per Short; bed chosen by
     spectrum (real low end); glue to Tab's envelope (onsets ≤22/10s, p95−p50
     ≤6.5 dB); TS1–TS8 + G7/G9 retained.
  6. **Voice:** Helio v2 + TS architecture stays until the free fixes are proven;
     ElevenLabs is the measured alternative and any spend on it is the owner's call.
