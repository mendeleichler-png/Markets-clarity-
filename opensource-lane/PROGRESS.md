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
- [ ] **Reviews** — RUN 2 completed all five (fact PASS, clarity
      FAIL veto, hook & pace PASS, story & visual PASS, taste
      FAIL) then DIED at the Reconciler (see log). RUN 3 launched
      2026-11-15 ~20:02 EST with ~5.7 GB free. RUN 1 record: fact
      PASS (missed a planted error), clarity FAIL, hook & pace FAIL
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
- **2026-11-15 ~17:06 EST** — CLARITY PASS DONE: **VERDICT: FAIL —
  the second veto fired.** Its reasoning is muddled (scrambled line
  numbers, "they" flagged where the names are in the same sentence),
  but a FAIL from a veto-holder obliges the Reconciler to resolve
  it. Its suggested rewrites keep the $4.2M line untouched (not its
  lens).
- **2026-11-15 ~17:01 EST** — INTERVENTION (infrastructure, no
  action needed): the llama-server runner was SIGKILLed (OOM — the
  box has ~8 GB RAM and the model holds ~5.5 GB). Ollama restarted
  the runner automatically within a second and the crew carried on;
  the in-flight generation restarted from scratch, which is part of
  why the next pass ran long.
- **2026-11-15 ~17:47 EST** — HOOK & PACE PASS DONE: **VERDICT:
  FAIL.** This one judged well: the opening line is "neutral," no
  immediate payoff — its rewrite pushes "$26 million… breaking no
  rules" into line 1. The pass took ~45 minutes wall-clock: two
  full 1,100-token generations at the measured ~1.6 tokens/second
  on this shared box, plus the OOM restart. Generation speed is the
  lane's real cost driver.
- **2026-11-15 ~17:53 EST** — INTERVENTION (infrastructure): SECOND
  OOM runner kill; Ollama auto-restarted it again and the crew
  retried the story & visual generation.
- **2026-11-15 ~18:05 EST** — RUN 1 KILLED by a platform service
  restart (the same event killed the coordinator's own shell): the
  crew process and the Ollama server both died mid story-&-visual
  pass. All run-1 outputs were on disk and are preserved verbatim in
  `videos/selbee-lottery/run1/` (sources, draft, 3 reviews).
- **2026-11-15 ~18:10 EST** — RUN 2 LAUNCHED: server restarted with
  the same env (model intact), then the full crew re-run from the
  top, exactly as designed (log `logs/crew-run-2.log`). Run 2
  produces its own sources/draft/reviews; run 1's record stays on
  file for comparison. No hand-edits to any model output in either
  run.
- **2026-11-15 ~18:17 EST** — RUN 2 RESEARCH DONE, and it is CLEAN:
  no $4.2M garble, no self-contradiction; UNVERIFIED holds only the
  test-buy amount and exact years. Same pipeline, different sample —
  run-to-run variance is itself a headline finding of this test.
- **2026-11-15 ~18:23 EST** — RUN 2 SCRIPT DRAFT DONE: every claim
  traces to the run-2 sources (no invented figures anywhere;
  test-buy profit stated without an amount). ~184 spoken words —
  over the 140–165 band; first line is expository, payoff not in
  line 1. Both are review-pass questions now.
- **2026-11-15 ~18:31 EST** — RUN 2 FACT PASS: **VERDICT: PASS** —
  legitimate this time (the draft has no unsupported figures; the
  reviewer's findings are wording pedantry only).
- **2026-11-15 ~18:37 EST** — RUN 2 CLARITY PASS: **VERDICT: FAIL**
  — the veto fired on invented grounds AGAIN (it claims the
  Selbees' names are "not yet spoken" in the line that speaks
  them; its rewrite just reorders the same words). Cross-run
  pattern: the clarity reviewer is a false-positive veto. The
  Reconciler's instructions cover exactly this — rebut it in the
  reconcile log or fix it; watching which.
- **2026-11-15 ~18:46 EST** — RUN 2 HOOK & PACE PASS: **VERDICT:
  PASS** — a weak review (generic "more engaging" notes; missed
  the missing line-1 payoff and the over-length draft entirely).
  One of its rewrites would corrupt a fact ("$7.75 million AFTER
  taxes" — the figure is before taxes); the Reconciler must not
  adopt it. Run 1's sharp FAIL vs run 2's soft PASS on the same
  weakness: variance again.
- **2026-11-15 ~19:00 EST** — RUN 2 STORY & VISUAL PASS:
  **VERDICT: PASS** — usable visual notes (Selbees frame 0,
  records/chart for the proof, document for the verdict), mostly
  matching the fixed asset plan. The pass survived two more OOM
  runner kills mid-generation (auto-restart + crew retry each
  time; the runner has now been killed ~5 times across the day —
  memory on this ~8 GB box is the lane's chronic hazard).
- **2026-11-15 ~19:08 EST** — RUN 2 TASTE & LANGUAGE PASS:
  **VERDICT: FAIL** — cosmetic synonym notes, but its hostile
  pre-mortem lands (generic ending, weak emotional connection).
  ALARM: its line-8 rewrite AGAIN corrupts the tax fact ("kept
  $7.75 million AFTER taxes") — the second reviewer to propose
  exactly that corruption of a verified figure.
- **2026-11-15 ~20:00 EST** — **RUN 2 DIED AT THE RECONCILER.**
  The reconciler's ~4,570-token prompt + long generation is the
  most memory-exposed stage: three attempts were killed
  mid-generation by OOM runner deaths (885, 213, and 306 tokens
  in; nine runner kills logged across the day), the API returned
  500 "unexpected EOF" each time, and CrewAI exhausted the call's
  retries — kickoff raised `openai.InternalServerError` and the
  process exited (traceback: `logs/crew-run-2.log`). All run-2
  outputs are preserved in `videos/selbee-lottery/run2/`. This is
  an infrastructure kill, not a model failure: the model completed
  7 of 10 stages. Memory has since freed to ~5.7 GB available.
- **2026-11-15 ~20:02 EST** — RUN 3 LAUNCHED (full re-run, log
  `logs/crew-run-3.log`) on the improved memory conditions.
- **2026-11-15 ~20:58 EST** — RUN 3 KILLED by a second platform
  service restart ~55 minutes in, before research completed; it
  produced nothing (run-2 files untouched). The restarts are
  recurring roughly every ~2 hours and kill every background
  process on this box. Server restarted again by hand.
- **2026-11-15 ~21:02 EST** — RUN 4 LAUNCHED (log
  `logs/crew-run-4.log`). The pipeline's clean stages took ~62
  minutes in run 2, so a kill-free run can fit inside one
  restart window; the reconciler remains the risk.
