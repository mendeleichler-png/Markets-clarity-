# BLUEPRINT — The markets clarity Shorts Producer Agent

**What this is:** the full design for a specialized AI agent whose only job is producing
markets clarity Shorts to the channel standard — research, script, voice, edit, audit,
verdict, publish, measure. It packages the pipeline Muse already runs in-house into one
persistent, portable specialist the owner can direct from his phone.

**Status:** design document, 2026-11-15. No spend, no new accounts, no build started.
Owner decisions are marked ◆ throughout.

---

## 1. Purpose and scope

- **In scope:** 35–55s vertical Shorts (1080×1920) for markets clarity (YouTube
  @marketsclarity, TikTok @markets.clarity): money stories — founders, fortunes, rogue
  traders, demo flops, market history. Series: money stories, "They Saw It Coming,"
  demo flops.
- **Out of scope (v1):** long-form video, the sleep channel, Daily Rot, thumbnails as a
  standalone service (cover frames are part of the Shorts package), ad buying, community
  management.
- **The agent is a producer, not a chatbot.** It runs a fixed pipeline with artifacts at
  every stage. Anything outside the pipeline is a conversation with Muse, not the agent.

## 2. Non-negotiable rules (baked into the agent, not re-briefed per video)

1. **Anonymity:** never the owner's personal name anywhere; never "Heimishe Investing
   Hub"; the brand is only "markets clarity." No position disclosure; the only disclaimer
   is the generic educational one (demo flops: none).
2. **Edit, don't generate.** Real footage only for real moments. Generation is B-roll /
   stylized reenactment only, never passed off as the real event. Never synthesize a real
   person's voice; real archival voice bites (2–4s) are mixed in where they exist.
3. **Facts are sacred.** Every claim traces to a dated primary source in the video's
   source file. Unverifiable = cut. "Reported" is labeled reported.
4. **The Script Standard governs every script** (triple hook, scene-before-claim,
   3-Second Stranger Test, 5th-grade readability, 4-beat structure, ten-pass review with
   fact and clarity vetoes). Full text: `script-standard-2026-11-15.md`.
5. **No publish without the owner's verdict** while the agent is on trial. After a
   sustained pass streak, the owner may ◆ promote it to the standing post-when-done rule
   that Tab-supplied videos already have.
6. **No spend, no signups, no account changes** without owner approval. API keys and
   credentials live in the vault, never in the repo, chat, or Notion.

## 3. Architecture — five layers

```
        OWNER (phone: Slack / chat)
          │  topics, verdicts, approvals
          ▼
┌─────────────────────────────────────────────────┐
│ 1. DIRECTOR — orchestrator model                │
│    plans, scripts, routes jobs, reconciles      │
│    reviews, assembles the delivery package      │
└──────┬───────────────┬───────────────┬──────────┘
       │ reads/writes  │ calls         │ posts/asks
       ▼               ▼               ▼
┌────────────┐  ┌──────────────┐  ┌────────────────┐
│ 2. MEMORY  │  │ 3. TOOLBOX   │  │ 4. CONNECTORS  │
│ GitHub repo│  │ research,    │  │ Notion board,  │
│ (rules,    │  │ footage,     │  │ Slack control  │
│ prompts,   │  │ voice, edit, │  │ room, Drive,   │
│ code) +    │  │ graphics, QA │  │ YouTube/TikTok │
│ Notion     │  │              │  │                │
└────────────┘  └──────────────┘  └────────────────┘
       ▲               │
       └───── 5. GATES ┘
   automated checks on every artifact +
   owner verdict + analytics fed back
   into topic selection
```

### Layer 1 — Director (orchestrator + model routing)

One strong reasoning model runs the pipeline and owns the final package. It delegates to
specialist models by job — diversity is a feature (the ten review passes must not all be
the same model agreeing with itself):

| Job | Model class | Why |
|---|---|---|
| Direction, reconciliation, final edit decisions | Frontier reasoning model | Judgment calls live here |
| Research synthesis | Frontier model w/ web search | Source discipline |
| Script draft | Frontier model | Story craft |
| Review passes 1–10 | Rotating mix (different vendors where available) | Independent lenses; fact + clarity passes get the most literal models |
| Captions/QA checks | Small/fast models + deterministic tools | Cheap, repeatable |
| Graphics generation (B-roll only) | Video/image models (Higgsfield, open models) | Quarantined from "real moment" footage |

Model versions are **pinned** in config; an upgrade is a deliberate change with a
regression test on one known script, never a silent drift.

### Layer 2 — Memory (GitHub + Notion)

**GitHub repo `markets-clarity-producer`** — the agent's brain on disk:

```
playbook/        VIDEO_PLAYBOOK.md, script-standard, voice spec, producer prompt
prompts/         one file per pipeline stage (research, script, each review pass, audit)
config/          models.yaml (pinned versions + routing), gates.yaml (thresholds), slate.yaml
src/             pipeline code (fetch, voice, edit, graphics, qa, package)
videos/          one folder per video: sources.md, script.md, reviews/, shotlog.md,
                 audit.md, metadata.md, renders/
templates/       description, pinned comment, audit skeletons
```

**Notion workspace** — the owner's window into the agent (no code required):

- **Slate** (database): topic, story, moment, share trigger, status, owner decision
- **Scripts**: one page per script with the ten pass verdicts summarized
- **Published**: link, date, stayed %, views, subs — the feedback record
- Rule: Notion mirrors state; GitHub is the source of truth. The agent writes both.

### Layer 3 — Toolbox (mostly open source)

| Stage | Tool | Job | Cost |
|---|---|---|---|
| Research | Web search + fetch; SEC EDGAR; court/official sources | Build `sources.md` with dated citations | $0 |
| Footage | Pexels/Pixabay APIs; archival downloads (yt-dlp); Wikimedia; company IR/newsroom pages | Real clips per the shot list; every clip logged with source + license note | $0 (optional paid stock ◆) |
| Face/subject tracking | OpenCV / MediaPipe face detection | Auto-crop suggestions that keep the subject centered (the framing rule) | $0 |
| Voice | **Kokoro-82M, `am_onyx`, speed 0.80**, long takes (no chunk stitching) | Narration at the channel standard | $0 |
| Voice post-chain | FFmpeg + SoX-style chain: per-segment loudness norm → de-ess → compression (envelope p95−p50 target 3.2–4.9 dB) → light saturation → sidechain-ducked bed → loudnorm | The measured channel sound | $0 |
| Captions | faster-whisper (word timestamps) | Kinetic word-by-word captions + the ASR-vs-script check | $0 |
| Edit | FFmpeg (programmatic assembly from a shot list) | Cuts every 0.7–1.5s, punch-ins, pattern interrupts, loop ending | $0 |
| Graphics | Remotion (React-based programmatic video) | Count-ups, draw-on charts, split screens, hero numbers — full-bleed, no word cards | $0 |
| B-roll generation (optional) | Higgsfield or open video models | Stylized reenactment/B-roll only, flagged in the shot log as generated | ◆ plan/API |
| QA | ffprobe, loudness analysis, ASR diff, frame sampler | The gate measurements in §5 | $0 |

### Layer 4 — Connectors

- **GitHub:** code, prompts, playbook, per-video artifacts. Every change is a commit —
  the agent's work is auditable and reversible.
- **Notion:** slate + scripts + published record (owner-facing mirror).
- **Slack (control room):** channels `#mc-slate` (topic pitches), `#mc-drafts`
  (finished packages posted for verdict), `#mc-alerts` (gate failures, blockers).
  Owner reacts ✅ = approved, replies with fixes otherwise. This is how the owner runs
  the agent from his phone.
- **Google Drive:** large asset handoff (footage in, renders out) when files exceed
  chat/Slack limits.
- **YouTube:** upload via Studio/API with metadata package; **TikTok:** cross-post on
  the spaced slate (2–3/day, strongest first). Publishing credentials stay in the vault;
  during trial the agent prepares everything and the owner (or Muse) executes the post.

### Layer 5 — Gates

**Automated gates (a build that fails any gate does not reach the owner):**

| Gate | Threshold (from the channel standard) |
|---|---|
| Loudness | −14 LUFS ±0.5, true peak ≤ −1 dB |
| Voice envelope | p95−p50 between 3.2–4.9 dB (dynamics, not flatness) |
| Speech over bed | 8–13 dB |
| Dead air | no silent gap ≥ 0.4s |
| Pace | mean 0.30–0.36 s/word; variation present (metronome = defect) |
| Captions | ASR transcript matches script ≥ 99% |
| Hook audio | first 0.3s hot (no fade-in) |
| Framing | one frame pulled per shot; subject centered/verified |
| Shot discipline | no clip used twice; cuts in the 0.7–1.5s band |
| Facts | every script claim maps to a line in `sources.md` |

**Human gates:** the ten-pass script reconciliation (fact + clarity vetoes), and the
owner's ear/eye verdict on the finished package.

**Feedback gate:** 48h after publish, the agent pulls views, stayed %, AVD, and subs
into Notion's Published table and writes a 3-line read: what the stayed rate says, what
it means for the next topic. Stayed % is the channel's ceiling law — topic selection is
re-ranked by it, not by taste.

## 4. The pipeline (state machine per video)

`idea → researched → scripted → reviewed → voiced → built → audited → verdict → published → measured`

| State | Artifact produced | Lives in |
|---|---|---|
| idea | Slate row: person, moment, dollar/contradiction, share trigger | Notion + slate.yaml |
| researched | `sources.md` — every fact w/ dated primary source | videos/<slug>/ |
| scripted | `script.md` — 5 segments, 140–165 words, triple-hook spec, [HOLD] beats | videos/<slug>/ |
| reviewed | 10 pass reports + reconciliation log; vetoes cleared | videos/<slug>/reviews/ |
| voiced | Narration WAV + pace/pause map | videos/<slug>/ |
| built | Draft MP4 from shot list; `shotlog.md` (source + license per clip) | videos/<slug>/ |
| audited | `audit.md` — all gate measurements, framing frames, 3 critique cycles | videos/<slug>/ |
| verdict | Package posted to Slack #mc-drafts: MP4, cover JPG, 3 titles, description + sources, pinned comment | Slack + Drive |
| published | Links recorded; TikTok cross-post scheduled per spacing rule | Notion Published |
| measured | 48h analytics read appended; slate re-ranked | Notion Published |

## 5. Runtime options — where the agent lives

| Option | What it means | Effort | Control | Cost |
|---|---|---|---|---|
| **A. Packaged here (recommended first)** | The pipeline already runs in Muse's environment; Phase 0–2 package it as the repo + Notion + Slack system above, with Muse as the runtime | Days | Highest — owner already works with Muse | $0 new |
| B. Self-hosted sandbox | Same repo deployed to a VPS/sandbox with an open orchestrator (e.g., LangGraph/n8n-style runner); runs without Muse | 1–3 weeks | Full ownership; owner maintains a server | ~$10–40/mo VPS + model API usage ◆ |
| C. Agent platform | Brief a platform agent (Instinct-type) with the producer prompt | Hours | Lowest — their sandbox, their tools, quality varies | Their pricing ◆ |

**Recommendation:** build A now — it is the same agent, on infrastructure that already
works, and the repo makes it portable. If the format proves out and the owner wants it
running independently, the identical repo ports to B with no redesign. C stays a trial
lane (already running with Instinct), not the main line.

## 6. Build phases

- **Phase 0 — Packaging (days).** Create the repo with the layout in §3; move the
  playbook, script standard, voice spec, and prompts in as versioned files; create the
  Notion workspace; create the Slack channels; write `gates.yaml` from §5 thresholds.
  *Deliverable: the agent's brain exists as one repo, readable by the owner in Notion.*
- **Phase 1 — One-command build (days).** Consolidate the existing build scripts into
  the pipeline: script + shot list in → voiced, captioned, graphics-rendered draft out;
  QA gates run automatically and write `audit.md`. *Deliverable: one proof video
  (Leeson/Barings or Kerviel/SocGen) built end-to-end by the packaged system.*
- **Phase 2 — Control room (days).** Slack verdict flow live (package posted, owner
  reacts, agent acts); analytics pull at 48h into Notion; slate re-ranking by stayed %.
  *Deliverable: the owner runs the agent from his phone.*
- **Phase 3 — Portability (optional, ◆ decision).** Containerize; deploy the same repo
  to a self-hosted sandbox; regression-test one known script end-to-end; switch the
  control room over only after the port matches Phase 2 output.

## 7. Costs (all optional items need ◆ approval)

- Open-source stack (Kokoro, Whisper, FFmpeg, Remotion, yt-dlp, OpenCV): **$0**
- Model APIs: the director/reviewer calls — usage-based; a Short's worth of calls is
  small (single-digit dollars at current API prices, estimate, varies by model mix)
- Higgsfield (optional B-roll lane): their plan pricing ◆
- Paid stock footage (optional): per-clip or subscription ◆
- Self-hosting (Phase 3 only): ~$10–40/mo VPS estimate ◆
- GitHub / Notion / Slack: free tiers cover v1

## 8. Risks and honest limits

- **Taste is the ceiling, not the wiring.** The gates guarantee a competent floor; the
  Tab-level bar is beaten through the verdict loop and slate selection, not by adding
  connectors. Expect iteration, measured in videos.
- **Free-voice ceiling.** Kokoro am_onyx is the best free option measured; the owner's
  ear remains the final judge (ElevenLabs stays an owner money decision, currently
  declined).
- **Footage rights.** Archival/news clips are used editorially; the shot log records
  source per clip so any claim is answerable. Paid stock removes doubt where it matters.
- **Platform friction.** TikTok posting and review holds are outside the agent's
  control; the spacing rule and duplicate checks are built into the publish step.
- **Model drift.** Pinned versions + a regression script; no silent upgrades.

## 9. First deliverable

One proof Short through the packaged system — **Nick Leeson / Barings (1995)** or
**Jérôme Kerviel / Société Générale (2008)** — with the full artifact trail (sources,
ten passes, shot log, audit) visible in the repo and the package posted for the owner's
verdict. That single run validates Phases 0–2 before any portability spend.

---

*Companion documents: `instinct-producer-prompt.md` (the agent's standing instructions),
`script-standard-2026-11-15.md`, `VIDEO_PLAYBOOK.md`, `claude-producer-prompt.md`.*
