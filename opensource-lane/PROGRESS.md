# Open-Source Lane — Live Progress

An open-source agent crew is building one markets clarity Short on its own,
to be judged blind against the main pipeline's Batch 1. Same playbook, same
tools (Kokoro voice, FFmpeg, QA gates) — the only variable is the agent/model
layer: a local open-weight model instead of the main line.

All times America/New_York. This page is updated at every stage change.

## The assignment

- **Video:** the Selbee lottery story — Jerry & Marge Selbee, the retired
  Michigan couple who found the Winfall roll-down flaw and won ~$26M gross
  (~$7.75M profit before taxes) over ~9 years across Michigan and
  Massachusetts. State investigators concluded no rules were broken.
- **Key sources the crew must verify itself:** CBS 60 Minutes and the
  Massachusetts Inspector General's report.
- **Deliverable:** 1080×1920 Short (35–55s) + cover + metadata + measured
  audit, packaged to the same standard as the main line. No uploading —
  the owner judges the package first.

## The lane

- **Framework:** CrewAI 1.15.41 (Python venv inside the lane folder)
- **Model:** Qwen2.5-7B-Instruct, Q4_K_M quantization (~4.68 GB), served
  locally by Ollama 0.40.16 — no API keys, no cloud models
- **Hardware:** shared VM, ~8 GB RAM, ~1.5 shared vCPUs. Local inference is
  slow; that is expected and part of the comparison.

## Stage checklist

- [ ] **Setup** — in progress (details below)
- [ ] **Research** — pending
- [ ] **Script** — pending
- [ ] **Reviews** — pending (10-pass protocol; fact pass and clarity pass run
      as separate veto-holding steps)
- [ ] **Voice** — pending (Kokoro am_onyx @ 0.80, same as main line)
- [ ] **Edit** — pending (FFmpeg assembly, captions, framing audit)
- [ ] **Gates** — pending (qa_gates.py: loudness, envelope, pace, ASR match)
- [ ] **Package** — pending

## Log

- **2026-11-15 12:38 EST** — Lane approved by owner as an A/B against Batch 1.
- **2026-11-15 ~13:00 EST** — Crew code written (research / script / review /
  reconcile / produce / package agents, all driven by the producer-agent
  playbook and prompts). Image assets gathered and verified: two CBS
  60 Minutes stills of the Selbees plus two Wikimedia B-roll images, sources
  logged.
- **2026-11-15 ~13:20 EST** — Ollama 0.40.16 installed (user-space,
  CPU-only: the full package's GPU libraries exceeded this machine's disk
  quota, so only the CPU runtime was extracted — 77 MB). Server running.
- **2026-11-15 13:36 EST** — Model download in progress (318 MB of
  ~4,680 MB; speed varies with the shared machine — Batch 1 builds are
  running in parallel). CrewAI installed; one dependency (litellm) was
  missing from its default install and is being added now. Setup stage
  stays open until the model is pulled and a smoke test passes.
- **2026-11-15 13:52 EST** — Lane handed to a fresh coordinator; the full
  state was re-verified on disk (crew code, image assets, venv all intact).
- **2026-11-15 13:58 EST** — CrewAI blocker found and fixed: this host's
  NO_PROXY setting contains bracketed IPv6 entries that crash CrewAI's
  LLM client ("Invalid port") before any model call can happen. The
  lane's crew script now sanitizes that setting at startup. litellm
  1.109.1 finished installing. Model download ~40% — the shared
  connection runs ~1.3 MB/s, so roughly 35–40 more minutes. Setup stays
  open until the model lands and a smoke test passes.
- **2026-11-15 14:05 EST** — Stall, logged honestly: the host machine
  restarted and killed both the Ollama server and the download at 35%
  (1.6 GB of 4.7 GB). Both were restarted and the download resumed from
  the partial file — nothing lost but time (~40 min at current speed).
