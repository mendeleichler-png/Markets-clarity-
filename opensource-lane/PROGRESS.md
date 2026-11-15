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

- [x] **Setup** — DONE 16:19 EST: model pulled, `mc-qwen` created,
      smoke test passed
- [x] **Research** — DONE ~16:35 EST (sources.md written; quality
      notes in the log)
- [x] **Script** — DONE ~16:43 EST (draft written; quality notes in
      the log)
- [ ] **Reviews** — in progress (fact pass DONE: PASS — see log;
      clarity pass running)
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
- **2026-11-15 15:02 EST** — Setup is BLOCKED on disk space, and this is
  the real reason behind the afternoon's "stalls." The home directory
  is at its ~118 GB quota ceiling (measured: 118 GB used). Ollama's
  server log shows the model download's writes failing with "disk
  quota exceeded" from 14:45 EST; a direct write probe confirms only
  ~0.3–0.5 GB of space can still be written. The model file is 2.0 GB
  downloaded of 4.68 GB — it needs ~2.7 GB more. The space is held by
  the channel's own video library (~81 GB in the financial-clarity
  folder, ~42 GB of it Shorts), which the lane will not delete on its
  own authority. Everything else is ready: CrewAI + litellm installed,
  the CrewAI startup crash fixed, crew code complete, images verified,
  Kokoro voice and QA gates in place. **To unblock: free ~3 GB anywhere
  in the home directory (owner's call what goes), and the lane resumes
  the download and runs the build with no other changes.**
- **2026-11-15 ~15:35 EST** — Owner approved cleanup; ~10 GB freed
  (home 118 GB → ~108 GB). Writes verified healthy again. Setup is
  UNBLOCKED.
- **2026-11-15 15:40 EST** — A self-retrying pull loop (10 attempts)
  was started against the running Ollama server. Attempts 1–6 failed
  on the manifest fetch alone: 60-second "context deadline exceeded"
  through the throttled egress proxy. Verified by direct probe that
  the registry itself answers in ~1.2 s — the timeouts are
  intermittent proxy behaviour, not a dead registry, and the loop
  absorbs them.
- **2026-11-15 15:43 EST** — Lane handed to a new coordinator to carry
  it through the build.
- **2026-11-15 15:47 EST** — A manifest fetch succeeded and the blob
  download RESUMED in 16 parts from the on-disk partial state (server
  log: "downloading 2bada8a74506 in 16 292 MB part(s)"). Note the
  on-disk part trackers still show the 576 MB verified counter from
  the afternoon's reset; parts are re-fetching over already-allocated
  blocks, so allocated disk bytes will not grow until the download
  passes the ~2.0 GB high-water mark. Monitoring until the model
  registers in the server.
- **2026-11-15 ~16:02 EST** — INTERVENTION (infrastructure): a runtime
  restart killed the Ollama server and the pull loop at 60%
  downloaded (2.8 GB) — the same failure that hit at 14:05. Recovery:
  restarted the server with the lane environment (models dir + port
  11434) and restarted the identical 10-attempt pull loop. The
  download resumed from the on-disk partial at 61% (2.9 GB), still
  ~2.5 MB/s. No data lost beyond the interruption itself.
- **2026-11-15 16:16 EST** — MODEL DOWNLOAD COMPLETE: "PULL OK" in
  the loop log; `qwen2.5:7b-instruct-q4_K_M` registered in the server
  (4,683,087,332 bytes, SHA-256 verified by Ollama).
- **2026-11-15 ~16:19 EST** — `ollama create mc-qwen` succeeded
  (Modelfile: FROM qwen2.5:7b-instruct-q4_K_M, num_ctx 8192). SMOKE
  TEST PASSED: one short generation via the API answered in ~80 s
  including model load. Honest note: the smoke answer itself was
  factually wrong from the model's memory (it called Jerry Selbee a
  football player) — which is exactly why this crew design forbids
  relying on model memory: the Researcher must verify every fact
  from the web and the fact pass holds a veto. **Setup stage DONE.**
- **2026-11-15 ~16:22 EST** — Crew launched (CrewAI, sequential,
  local mc-qwen only). Research ran first: web searches + page
  fetches including the Massachusetts IG coverage.
- **2026-11-15 ~16:35 EST** — RESEARCH DONE. sources.md verdict,
  honestly: the headline facts check out against CBS 60 Minutes
  ($26M gross, $7.75M profit, ~9 years, MI + MA, IG found no
  rule-breaking). But the file also (a) lists those same two money
  figures under UNVERIFIED, contradicting itself, (b) garbles the
  "first test buy" line into "$4.2 million a year" (Boston Globe),
  which is not a real figure from the story, and (c) leaves the
  roll-down cap UNVERIFIED (so per the rules it must be cut from the
  script). Whether the script + veto passes catch (b) is part of
  the test — it is NOT being fixed by hand.
- **2026-11-15 ~16:38 EST** — INTERVENTION (infrastructure): this
  CrewAI version writes output_file paths relative to the process
  cwd even when given an absolute path — sources.md landed in a
  nested mirror tree under the lane folder instead of the package
  folder. Left alone, every later deliverable would land there too,
  and the Producer's reader (which uses the true absolute path for
  script.md) would have failed. Fix: copied sources.md verbatim to
  the real package folder and replaced the nested `home` directory
  with a symlink to /home, so all subsequent crew outputs resolve
  to their real locations. No content was altered.
- **2026-11-15 ~16:43 EST** — SCRIPT DRAFT DONE. Honest quality
  notes: ~110 spoken words (under the 140–165 band), a [HOLD] in
  only one of five segments, and — critically — the garbled sources
  line shipped straight into Segment 4: "Their first small test buy
  returned $4.2 million a year." The roll-down mechanism is
  described without figures, which does follow the UNVERIFIED rule.
- **2026-11-15 ~16:50 EST** — FACT PASS DONE: **VERDICT: PASS — and
  the veto failed its purpose.** The reviewer polished wording
  ("found" → "discovered", "profitable" → "advantageous") and
  explicitly approved the "$4.2 million a year" line as accurate
  because it matches the sources file. It never questioned the
  sources line itself, so the poisoned fact survived the one pass
  designed to kill it. Recorded, not repaired: whether the later
  passes or the reconciler catch it is still part of the test.
