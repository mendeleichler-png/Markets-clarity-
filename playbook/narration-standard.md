# Narration Standard — Research, Diagnosis & Spec (2026-10-31)

Owner's verdict that commissioned this: the narration is the channel's "very low
floor" — speed, loudness and pitch wobble unnaturally across a video, and inside
chunks it runs flat; it doesn't flow like a human talking. This document is the
research + measured diagnosis + the fix (Narration Standard v2), with proofs.

Tool that implements it: `~/workspace/financial-clarity/shorts/narration_v2.py`
Proof renders: `~/workspace/financial-clarity/narration-proof/`

---

## PART 1 — RESEARCH (how the best do it)

Web research run 2026-10-31 (sources cited per cluster; vendor claims flagged
as vendor claims). The load-bearing findings:

**1. The top of our niche is human, and that's the benchmark.** ColdFusion's
narration is creator Dagogo Altraide himself, recorded and edited in a DAW
(coldfusion.fandom.com/wiki/Dagogo_Altraide; cold-fusion.co.uk/about).
Khan Academy's voice is Sal Khan. The Plain Bagel is Richard Coffin himself.
No top faceless finance channel is documented using TTS as its primary voice.
Where TTS *is* used successfully in documentary, the pattern is ONE narrator
persona across the whole catalog (SciShow/Half as Interesting style) — the
audience bonds to a consistent voice, wobble included, which is precisely what
chunk-stitching destroys. Implication: (a) consistency of OUR voice matters
more than its raw quality; (b) the true ceiling-breaker is recorded human VO
(owner or a hired narrator) — TTS work is about closing the consistency gap.

**2. Chunking science — our exact failure, documented.**
- Vendor guidance converges: synthesize complete sentences, and inputs under
  ~15 words trigger "neutral, flat default delivery" (Cartesia docs,
  docs.cartesia.ai/build-with-cartesia/sonic-3/ssml; OpenAI community
  measurements: <300-char chunks vary phoneme timing ±20% even across
  IDENTICAL re-reads, openai.com community gpt-4o-mini-tts threads).
- ElevenLabs' own long-form guidance: normalize each segment's loudness
  BEFORE concatenation so concatenation doesn't compound differences, and
  prefer markup-driven pauses over baked-in settings (elevenlabs.io/blog).
  (That is literally Standard v2 step 6 — independent convergence.)
- Community ABX testing on ElevenLabs: ~800+ characters per call reads
  measurably better than short chunks; per-call voice "seeds" (previous
  context) stabilize a series (r/ElevenLabs ABX threads — folklore-grade
  evidence, directionally consistent with the vendor docs).
- ElevenLabs v3 additionally carries context across sequential calls and
  supports explicit `[pause]`/break markup; Multilingual v2 exposes
  stability/similarity/style controls (elevenlabs.io/docs/tts).

**3. Measurable fingerprints of natural narration.**
- Pace: conversational speech 120–150 wpm; brisk documentary 160–185 wpm
  (ColdFusion measured ~185 wpm). Our settled anchor 0.33 s/word = 182 wpm —
  at the brisk documentary edge, keep. Natural readers vary pace ±10–15%
  across a piece BY DESIGN (slow for emphasis) — variance must be *chosen*,
  not random; our gate therefore caps segment pace CV at 6% (tighter than
  human drift, because our drift was noise, not emphasis).
- Pauses: clause commas 100–250 ms; sentence ends 200–500 ms; paragraph
  breaks roughly 2× sentence pauses, 0.7–1.0 s (NASA prosody corpus study,
  ntrs.nasa.gov; ToBI annotation conventions, ling.upenn.edu). Standard v2's
  grammar (internal cap 0.50 s / floor 0.18 s, joins 0.65 s) sits inside these
  ranges.
- Loudness: voice phrases ride ~5 LU of momentary range in natural reads;
  segment-to-segment integrated drift should stay ≤2 LU (EBU R128 practice).
  YouTube delivery: −14 LUFS integrated / −1 dBTP (Google support).

**4. Mastering chain (pro VO practice).** HPF 70–80 Hz → de-ess (5–8 kHz)
BEFORE compression (a compressor accentuates the sibilance it's fed) →
2.5–4:1 compression, 5–8 dB GR on peaks → limiter → loudnorm once at the end.
Music: sidechain duck −6…−12 dB of gain reduction keyed on the voice, bed
additionally low-passed under dialogue; the bed-under-voice distance that
reads "professional" is ~16–20 dB while speaking (Descript/Adobe podcast
guidance; YouTube creator engineering write-ups). Standard v2's chain now
follows this order (de-ess moved ahead of the compressor on this evidence).

**5. TTS engine landscape (prices checked 2026-10-31, official pages).**

| Engine | Prosody controls | Long-form behavior | Cost |
|---|---|---|---|
| ElevenLabs Multilingual v2 | stability ~50, similarity 75%, style 0–20%, speaker boost | vendor: no systemic long-form drift; per-segment loudness normalization recommended | Creator $22/mo (annual; $11 first month) ≈ 100 min v2 |
| ElevenLabs v3 | + `[pause]` tags, cross-call context carryover | best-in-class chunk continuity | same credits, pricier per char |
| ElevenLabs Flash/Turbo | speed 0.7–1.2 numeric | consistent, less expressive | ~½ credit cost (~200 min on Creator) |
| OpenAI gpt-4o-mini-tts | free-text style instructions | ~15% per-call speed variance; 2,000-char cap forces chunking | ~$0.015/min — cheapest direct API |
| Google Gemini 2.5 Flash TTS | style prompts, 24 languages | 32k-token context = true long passes | ~$0.50/$10 per 1M tok — cheapest premium API |
| Cartesia Sonic-3 | SSML breaks in centiseconds, emotion tags | explicit "short input = flat delivery" warning | $5 / 100k chars |
| Our Helio (Meta Shortwave) | speed integer only, non-linear | per-call tempo lottery on long inputs; near-deterministic per (text, speed) | in-environment, $0 marginal |

**Settings cheat-sheet (if/when ElevenLabs is adopted):** Multilingual v2 for
narration (v3 for hero pieces), stability 50, similarity boost 75, style
exaggeration 0–20, speaker boost ON, one voice locked catalog-wide, segments
of 800+ chars, per-segment loudness normalization (already our v2 step 6) and
`[pause]`/break markup at paragraph joins instead of stitched silence.

### Local findings about our own engine (Meta Shortwave TTS, voice Helio
`avocado_v2:MAI_03`) — measured 2026-10-31, test script 170 words / 5 segments

1. **Per-call tempo is text-dependent and (for long inputs) a lottery.**
   - Five different ~35-word chunks at the SAME api speed (135) came back with
     speech pace 0.173–0.268 s/word — a 55% spread.
   - The same 170-word script in ONE call at speeds 100/115/125/135 produced
     total durations of 134.9 / 74.5 / 116.6 / 112.2 s. Long-pass generation is
     NOT a consistency strategy with this engine; speed does not map linearly,
     and re-rolls vary wildly.
   - At a fixed speed, re-rolling the SAME 40-word segment is near-deterministic
     (speed 135: three takes bit-identical duration, 12.77 s; speed 115:
     14.30/15.31/15.12 s). Consequence: a missed take is fixed by CHANGING THE
     SPEED (speed search), not by re-rolling.
2. **The engine's native pause grammar is heavy**: in long passes it inserts
   0.34–0.79 s pauses at nearly every sentence/clause boundary (38–56 pauses,
   17–29 s of silence in a 170-word read). Chunked generation + head/tail
   trimming + butt-joining throws this grammar away at every chunk seam.
3. **Raw chunk loudness is quiet and scattered**: Jensen-long chunks measured
   −29.9 to −25.3 LUFS integrated (4.5 LU range); money-market chunks (post
   speed-135) −21.6 to −18.8 LUFS (2.8 LU range).

---

## PART 2 — DIAGNOSIS (measured baseline on shipped files)

### Money-market Short (shipped `money-market-short.mp4`, 5 chunks, speed 135 +
one uniform atempo + loudnorm two-pass on the final mix)

| Metric (per chunk) | Mean | SD | Min | Max | Range/CV |
|---|---|---|---|---|---|
| Pace (s/word, final) | 0.303 | 0.031 | 0.269 | 0.354 | **CV 10.3%** |
| Loudness, narration stem (LUFS) | −20.0 | 1.17 | −21.6 | −18.8 | **range 2.8 LU** |
| Loudness, shipped mix (LUFS) | −17.4 | 0.91 | −18.4 | −16.4 | range 2.0 LU |
| F0 median per chunk (Hz) | 102.4 | 4.3 | 98.0 | 108.1 | **10 Hz wander** |
| F0 IQR within chunk (Hz) | 30.6 | 5.3 | 23.5 | 37.6 | — |

The uniform atempo fixed the AVERAGE pace (0.303 ✓) and left every chunk's
individual deviation in place — chunk 2 runs 11% slow, chunk 5 runs 11% fast,
chunk loudness swings 2.8 LU, and the pitch center jumps ~10 Hz between chunks.
That is exactly the wobble the owner hears.

### Jensen long (master, 66 narration chunks, target 0.374 s/word)

| Metric (per chunk) | Mean | SD | Min | Max |
|---|---|---|---|---|
| Raw TTS pace (s/word) | 0.348 | 0.054 | 0.219 | 0.480 |
| **Atempo factor applied** | 0.934 | 0.137 | **0.78** | **1.28** |
| Raw TTS loudness (LUFS) | −27.9 | 0.98 | −29.9 | −25.3 |
| **Loudness as placed (LUFS)** | −27.8 | 0.98 | −30.0 | −25.3 |
| F0 median per chunk (Hz) | 107.0 | 8.1 | **89.4** | **133.3** |

The pitch center of the "same" voice wanders across a 44 Hz range over one
video — the single most damning number in this diagnosis, and the one no
post-hoc pass was ever going to fix.

Two separate sins:
- Pace was FORCED: each chunk time-stretched by a different factor between
  0.78× and 1.28× (WSOLA artifacts scale with the factor — a chunk at 1.28
  sounds processed next to one at 0.85).
- Narration loudness was NEVER normalized — raw chunk loudness (4.6 LU range)
  went to air unchanged (only the archival bites were gain-matched, to a
  reference sampled from 5 narration chunks). The final loudnorm pass can only
  shift the whole mix; it cannot repair internal variance, and chasing it with
  extra passes (money-market needed corrective passes up to −15.1 → −14.0)
  pumps against the limiter.

### Structural defects in the current chain (both formats)

1. **Chunk granularity ~30–40 words with cold starts**: every chunk restarts
   the intonation arc; seams butt-join with ~0 pause, then the next chunk's
   own internal rhythm takes over — the "stitched" feel.
2. **Mixed recipes across builds**: TTS api speed 115 in one build, 135 in
   another, each with a different after-the-fact correction strategy (uniform
   atempo for Shorts; per-chunk forced atempo for longs; corrective loudnorm
   passes when the finish missed −14).
3. **Shorts music is NOT ducked**: the Shorts engine mixes music at a fixed
   `volume=0.22` under narration with `amix normalize=0` — when a quiet chunk
   lands, the music effectively jumps forward; when a loud chunk lands, it
   buries. Perceived loudness wobble is amplified by the bed. (The longs used a
   manual RMS envelope duck, −17 dB under voice — better, but hand-built per
   episode and not a standard.)
4. **Flat within chunks**: short isolated reads give the engine no discourse
   context, so each chunk is read in the same neutral register; there is no
   emphasis direction and no arc. Mitigations available locally are
   punctuation/exclamation shaping in the text itself, longer segments, and
   choosing takes — not a settings dial (this engine exposes only speed).

---

## PART 3 — THE FIX: Narration Standard v2 (implemented in narration_v2.py)

Per script segment (a full thought, ~25–60 words):

1. **Generate** at a fixed api speed (default 115 — measured: gentle native
   tempo, low same-settings variance). One speed per video, always recorded.
2. **Measure** the take: speech seconds (pauses excluded), total seconds,
   integrated LUFS.
3. **Speed-search regeneration**: if the take's implied atempo correction
   exceeds ±7%, regenerate at a steered speed (speed × measured miss, clamped
   100–140), up to 3 attempts; keep the take needing the least correction.
   (Re-rolling the same settings is futile — near-deterministic.)
4. **Pause-shape in the sample domain** (speech samples untouched): head/tail
   trimmed to 0.05 s; internal pauses capped at 0.50 s, floored at 0.18 s.
5. **Bounded atempo**: correct to the video's target pace with atempo clamped
   to [0.90, 1.10]; anything beyond ±7% is flagged in the gate report, never
   silent. The 0.78–1.28 forcing of the longs is banned.
6. **Static per-segment loudness normalization** to −20 LUFS (gain clamp
   ±12 dB) BEFORE assembly. No dynamic normalization on the voice, ever.
7. **Assemble** with an exact 0.65 s join gap between segments.
8. **Master once**: highpass 70 Hz → de-ess notch −2 dB @ 6.5 kHz (Q 1.5) →
   acompressor 2.5:1 (threshold −18 dB, attack 8 ms, release 180 ms, knee 6).
   (Order per Part 1 §4: de-ess before compression.) Final loudnorm
   (I −14, TP −1.5) happens ONCE, on the finished mix.
9. **Music ducking (engine change for Shorts)**: replace the fixed-volume bed
   with sidechain compression keyed on the narration (target: bed sits
   16–20 dB under voice while speaking, recovers in pauses), e.g.
   `sidechaincompress=threshold=0.02:ratio=8:attack=20:release=300` on the bed
   keyed by the narration stem, then amix. Longs keep envelope ducking only if
   it matches the same −16…−20 dB-under-voice target.

### Proof (same 170-word test script, both ways) — see narration-proof/

- OLD (faithful replica of the shipped recipe: chunks @ speed 135, trim, one
  uniform atempo 0.864, concat): 51.4 s.
- NEW (narration_v2, target 0.330 s/word): `proof_new_stem.wav` +
  `proof_new_stem_mastered.wav`, gate JSON alongside.

### Measured proof (identical ruler applied to both stems, per segment)

| Metric | OLD way (proof replica) | NEW way (narration_v2) | Shipped baseline (money-market / Jensen) |
|---|---|---|---|
| Pace CV across segments | **23.8%** | **1.58%** | 10.3% / raw 15.6% |
| Max pace deviation from target | **29.7%** | **3.64%** | ~19% (segments 0.269–0.354 on a 0.303 target) |
| Segment loudness range | 1.74 LU (this draw; shipped draw was 2.8) | **0.01 LU** | 2.8 LU / 4.6 LU |
| Segment loudness SD | 0.63 LU | **0.00 LU** | 1.17 / 0.98 LU |
| Atempo used | one uniform 0.864 (all chunks warped 13.6%) | per-segment 0.90–1.06, speed-searched takes | uniform / per-chunk 0.78–1.28 |
| F0 median spread across segments | — (shipped: 10.1 Hz ≈ 10%) | 12.8% (report-only metric) | ~10% |
| F0 IQR within segment (expressiveness) | — | 23.7–64.0 Hz | 23.5–37.6 Hz |
| Total duration (170 words) | 51.4 s @ forced 0.303 | 58.0 s @ natural 0.325 (target 0.330) | — |

Notes on honesty:
- The NEW way's within-segment pitch movement (F0 IQR) is LARGER than the
  shipped baseline's — the longer, speed-searched takes breathe more. The
  cross-segment F0 *center* still wanders ~10–13% — that is the engine's
  per-call register and normalization cannot fix it; the gate therefore treats
  F0 spread as a report metric with an 18% hard ceiling, not a tight pass/fail.
- Two of five proof segments needed the atempo hard bound (0.90) even after
  speed search bottomed out — flagged in the gate JSON, final pace still
  landed within 3.6%. Stubborn texts exist; the system's job is to bound and
  disclose, which the old system's never did.
- Listening files: `narration-proof/proof_OLD_way.mp3` and
  `proof_NEW_way.mp3` — same script, same final master chain, level-matched.
  Only the narration stage differs.

---

## PART 4 — THE PROSODY GATE (mandatory in every build's audit.md from
2026-10-31; thresholds derived from the baseline vs proof measurements)

Every future build runs narration through `narration_v2.py`, saves the emitted
`<stem>.gate.json` in its build directory, and copies these lines into
audit.md. A build that fails the gate is re-voiced, not shipped.

| # | Check | Pass threshold | Baseline (shipped) | Proof (v2) |
|---|---|---|---|---|
| G1 | Per-segment pace CV | ≤ 6% | 10.3% Short / 15.6% long (raw) | 1.58% |
| G2 | Max per-segment pace deviation from target | ≤ 8% | ~19–30% | 3.64% |
| G3 | Per-segment loudness range (post-normalization, pre-mix) | ≤ 2.0 LU (SD ≤ 0.8) | 2.8 LU / 4.6 LU | 0.01 LU |
| G4 | Atempo per segment | all within [0.90, 1.10]; segments beyond ±7% flagged by name with speed-search log | 0.78–1.28 unflagged | 0.90–1.06, 2 flagged |
| G5 | F0 median spread across segments | ≤ 18% (report the number always) | ~10% | 12.8% |
| G6 | Pause grammar in final stem | joins = 0.65 s; no internal pause > 0.90 s; no segment head/tail silence > 0.10 s | ~0 s joins, untrimmed heads | by construction + verified |
| G7 | Final mix loudness | I = −14 ± 0.5 LUFS, TP ≤ −1.0 dB, achieved in ONE loudnorm pass (a corrective second pass = gate note explaining why) | corrective passes needed | one pass |
| G8 | Recipe discipline | one api speed strategy per video (v2 speed-search log), voice + target pace recorded in audit.md | speeds 115 vs 135 across builds, unrecorded strategy | logged in gate JSON |

Plus the standing rules the gate enforces structurally: no dynamic
normalization on the voice; no per-chunk atempo outside [0.90, 1.10]; music
sidechain-ducked (Shorts engine patched 2026-10-31) or envelope-ducked to
16–20 dB under voice (longs); narration segments are full thoughts
(~25–60 words), never sentence fragments.

## Paid options (owner decisions — nothing purchased)

Our production volume is ~15 min of narration/week ≈ 60 min/month.

1. **ElevenLabs Creator — $22/mo billed annually ($11 first month)** —
   ~100 min/month of Multilingual v2 (or ~200 min of Flash). This is the
   single biggest prosody jump per dollar: real stability/style controls,
   emphasis markup, cross-call context on v3, and it removes the tempo
   lottery entirely (numeric speed control, deterministic-ish reads). Fits
   our volume with headroom. elevenlabs.io/pricing (checked 2026-10-31).
2. **Zero-commitment trial route: Voler.ai pass-through at $0.09/min** —
   ~$1 buys ~11 min of ElevenLabs/Google voices to A/B against Helio before
   any subscription decision. Third-party pipe; fine for a test, not a
   foundation.
3. **Cheapest direct APIs if price is the binding constraint:** OpenAI
   gpt-4o-mini-tts (~$0.015/min, steerable but chunky and tempo-variable) and
   Google Gemini 2.5 Flash TTS (32k context, true long passes). Both are API
   integrations, not drop-ins for the current CLI.
4. **The benchmark option (not TTS at all):** recorded human VO — the owner
   narrating, or a hired narrator. Every top channel in our niche does this.
   Highest ceiling, highest ongoing effort. Stated for completeness; the
   channel's anonymous-brand model works with a hired voice too.

Recommendation: run the $1 Voler A/B first; if it clearly beats the v2 Helio
proof (it should on expressiveness), move to ElevenLabs Creator and re-lock
the catalog voice. Standard v2's measurement/gate machinery carries over
unchanged — it is engine-agnostic.

## Honest ceiling of the current tooling

Helio (Meta Shortwave) exposes exactly two controls: voice choice and a speed
integer whose effect is non-linear and text-dependent. There is no SSML, no
pause markup, no emphasis control, no stability/style dial. Everything in
Standard v2 is therefore measurement and selection around a black box: we can
guarantee consistency (pace, loudness, pauses, mastering) but we cannot give
the voice new acting range — within-chunk expressiveness improves only via
longer segments and text shaping. A step-change in raw expressiveness requires
an ElevenLabs-class engine (see Paid options) or recorded human VO. That is
the honest ceiling, stated once, here.

---

## ADDENDUM 2026-10-31 (night) — ElevenLabs A/B test: route verification,
CORRECTION, and prepared test (owner approved "~$1, no commitment")

**CORRECTION to Paid Options #2 above: the "Voler.ai pass-through at
$0.09/min" does not exist.** voler.ai was fetched in full on 2026-10-31: it
is an Italian AI *consultancy* for small businesses in Verona (LINO'S & CO
SRL) — no TTS product, no credit system, no ElevenLabs or Google voices, no
per-minute pricing. No equivalent "Voler" TTS service exists in search
either. The $0.09/min citation was wrong and must not be relied on; the
cheapest legitimate no-commitment route to ElevenLabs voices is the
**ElevenLabs Free tier itself: $0, 10,000 credits/month (≈10 min of
Multilingual v2), no credit card required** (verified against
elevenlabs.io/pricing via multiple October-2026 sources). Other
pass-throughs were checked and all stop at an account/payment line:
Puter.js "free unlimited ElevenLabs" (tested directly from this machine —
returns "Unauthorized" without a signed-in Puter account; user-pays model),
OpenRouter (account + prepaid top-up above the $1 approval), WaveSpeedAI /
fal / Replicate (account + balance). The ElevenLabs homepage demo
(~500 chars, playback only, no download) cannot produce measurable clips.

**Result of the approved test run: NO clips rendered, $0 spent, nothing
subscribed, no accounts created.** Every route requires one owner identity
step this run was barred from taking (creating an account in the owner's
name). The test is fully prepared in `narration-proof/elevenlabs-test/`:

- `TEST-PLAN.md` — route evidence, voices, settings, credit math, exact
  owner step.
- `render.py` — one-command render once `ELEVENLABS_API_KEY` exists:
  3 voices × (5 proof segments + IRMAA s01–s04 excerpt as one call),
  ≈5,650 of the free tier's 10,000 credits.
- `measure.py` — applies the identical gate ruler (imports narration_v2.py
  helpers): pace CV, max pace deviation vs 0.33 s/word, raw LUFS range,
  F0 median spread, per voice, vs the Helio v2 proof baseline
  (CV 1.58%, max dev 3.64%, F0 spread 12.8%).
- Voices selected (ElevenLabs default/premade, IDs verified): **George**
  `JBFqnCBsd6RMkjVDRZzb` (British, warm), **Brian** `nPczCjzI2devNBz1zQrb`
  (American, deep), **Adam** `pNInz6obpgDQGcFmaJgB` (American, deep);
  settings on every call: Multilingual v2, stability 50, similarity 75,
  style 15%, speaker boost ON.
- Test material: the same 170-word proof script (segment-for-segment
  comparable) + a ~169-word excerpt from the real IRMAA Short script
  (single call, to test long-pass prosody on upcoming material).

**The one owner step (≈2 minutes):** sign up FREE at
**https://elevenlabs.io/sign-up** (email or Google, no card, no paid plan),
then dashboard → API Keys → + Create Key, and hand the key to Muse via the
Secure Vault (never chat). Muse then renders and measures the same day.

**Recommendation:** run the test on the free tier at $0 — the approved $1
does not need spending; there is no $1 ElevenLabs product (cheapest paid is
Starter, $6/mo, a subscription, not authorized). Judge the A/B on
expressiveness (owner's ear) + gate numbers. If ElevenLabs wins, published
use requires at least Starter (commercial license; free-tier audio is
non-commercial with attribution — test clips only, never publish them);
Creator ($22/mo billed annually, $11 first month, ~121k credits) remains
the right production tier per the volume math in Paid Options #1. Standard
v2's gate machinery carries over unchanged, as stated above.


---

## Addendum — 2026-11-01: replacement-key re-verification BLOCKED (no renders, 0 credits spent)

The owner replaced the stored key with a brand-new one via the Secure Vault
reconnect on 2026-11-01, and Muse re-verified before rendering, per
protocol. The surrogate path works (requests reach api.elevenlabs.io with
the credential placed in the xi-api-key header), but the NEW key is again a
restricted-permissions key:

- `GET /v1/user/subscription` → 401 `missing_permissions`: "The API key you
  used is missing the permission user_read to execute this operation."
- `GET /v1/voices` → 401 `missing_permissions`: missing permission
  `voices_read`.

Per the stop rule, no TTS probe was made, so the `text_to_speech` scope
status is unconfirmed — but a key missing both read scopes was plainly not
created with the permissions this test needs, and no credits were burned
finding out (0 spent; balance untouched at the free tier's 10,000).

**Owner fix (≈1 minute, dashboard):** ElevenLabs → API Keys → the key →
Permissions: either set the key to unrestricted / all permissions, or
enable at minimum `text_to_speech` (the test itself), plus `voices_read`
and `user_read` (verification reads). Save, then tell Muse — render.py +
measure.py run immediately, no new key and no new vault paste needed if the
same key is edited in place.

**Verdict status:** the A/B still has not run. No per-voice numbers, no
listening files, no adoption recommendation yet — nothing about this
outcome is evidence for or against ElevenLabs. The Helio v2 baseline
(CV 1.58%, max dev 3.64%, F0 spread 12.8%) remains the standing champion by
default only. Licensing note unchanged: free-tier renders are test-only
and non-commercial; publishing requires Starter ($6/mo) at minimum, with
Creator ($22/mo billed annually) the production tier. Nothing was
subscribed, uploaded, or published.

---

## Addendum — 2026-11-01 (later): voice test RAN — verification passed, 18 renders, verdict inside

The owner edited the FIRST key's permissions in the dashboard (restriction
removed / scopes enabled), and the stored credential — whichever of the two
keys it is — now passes verification cleanly:

- `GET /v1/user/subscription` → 200 (tier free, limit 10,000).
- `GET /v1/voices` → 200 (21 premade voices, incl. all three test voices).

The full prepped test then ran in one pass (`render_surrogate.py`, the
surrogate-transport twin of `render.py`; identical texts, segmentation and
settings: Multilingual v2, stability 50, similarity 75, style 15%, speaker
boost ON). 18 renders: 5 proof segments + the IRMAA excerpt, × George /
Brian / Adam. **Credits used: 5,436 of 10,000** (subscription read-back
confirms character_count 5,436; 4,564 remain this cycle). Measured with
`measure.py` — the same narration_v2 ruler as the Helio proof;
`results.json` sits beside the clips in `elevenlabs-test/`.

### Numbers (ElevenLabs = RAW single takes; target pace 0.33 s/word)

| Metric | George | Brian | Adam | Helio v2 proof |
|---|---|---|---|---|
| G1 pace CV | 20.04% | 18.01% | 15.02% | **1.58%** |
| G2 max pace deviation | 40.3% | 36.7% | 39.4% | **3.64%** |
| G3 LUFS range across segments | **0.63 LU** | **0.71 LU** | **0.86 LU** | 0.01 LU |
| G5 F0 median spread | **6.3%** | **10.0%** | 15.7% | 12.8% |
| IRMAA single-call pace | 0.429 spw | 0.425 spw | 0.441 spw | — |
| IRMAA duration (~169 words) | 69.4s | 68.9s | 71.5s | ≈55.8s at target |

**Read the table honestly — two caveats decide what it means:**

1. **Raw vs corrected.** Helio's 1.58% / 3.64% are the output of the v2
   correction pipeline (per-segment speed search + pre-normalization), not
   raw engine consistency; the ElevenLabs figures are uncorrected single
   takes. Raw Helio on shipped files measured CV 10.3–15.6%, so raw-vs-raw
   the ElevenLabs voices sit in the same band on pace — their spread is
   interpretive: every voice slows for the number-dense segments
   (s02/s03 ≈ 0.41–0.46 spw) and runs at ≈0.30 on plain prose. That is the
   human-flow quality the overhaul was commissioned for, and it is also
   precisely what G1/G2 punish. The gate machinery carries over, but on
   Multilingual v2 there is no per-call speed knob to search — pace
   correction would be post-hoc, inside the gate's atempo bounds.
2. **Native loudness is excellent.** 0.63–0.86 LU raw across five separate
   calls beats raw Helio; Helio's 0.01 LU exists only after v2's
   pre-normalization. Absolute level differs by voice (Adam ≈ −17.5 LUFS,
   Brian/George ≈ −23.5 LUFS) and is a non-issue: the existing single
   loudnorm pass absorbs it. George (6.3%) and Brian (10.0%) also beat
   Helio's F0 spread; Adam (15.7%) does not.

**The one genuine adoption blocker is pace on real material.** On the
IRMAA script all three voices deliver ≈0.43 s/word — about 30% slower
than the channel's 0.33 anchor. Assembled as-is, a 55-second Short becomes
≈70 seconds. Closing the gap needs ≈1.3× atempo, outside the gate's
correction bound; the alternatives are shorter segments with re-takes,
text-side pacing, or a deliberate pace re-anchor. That is a pipeline
problem to solve before any published render — not a voice-quality
finding.

### Verdict / recommendation

**Adopt ElevenLabs as the candidate engine — with Brian as the channel
voice, George as alternate — conditional on (a) the owner's ear and
(b) the pace fix. Do not retire Helio v2 yet.**

- **Brian** (`nPczCjzI2devNBz1zQrb`): American deep; best balance —
  mid pace CV, F0 spread 10.0% (better than Helio), tight loudness.
- **George** (`JBFqnCBsd6RMkjVDRZzb`): most stable F0 (6.3%) and the
  tightest loudness (0.63 LU), but British and the widest pace CV.
- **Adam** is out: widest F0 spread (15.7%) and the slowest IRMAA pass.
- Expressiveness — the original complaint ("doesn't flow like a human
  talking") — is the owner's call on the listening files; no meter in
  this addendum settles it. Files: `elevenlabs-test/clips/<voice>_proof_full.mp3`
  (5 segments, 0.65s joins) and `<voice>_irmaa.mp3`, beside the per-segment
  clips and `results.json`.

**Licensing fence, unchanged:** these free-tier renders are test-only,
non-commercial, attribution-required — never publish them. Published use
requires Starter ($6/mo) at minimum; Creator ($22/mo billed annually,
~121k credits ≈ 100+ min/mo) remains the production tier per the volume
math. Nothing was subscribed, uploaded, or published; IRMAA/rollover
files untouched.
