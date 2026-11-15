# Pipeline — how a video moves (driver doc)

States: idea -> researched -> scripted -> reviewed -> voiced -> built -> audited ->
verdict -> published -> measured. One folder per video under videos/<slug>/, copied
from videos/_template/.

Stage drivers (existing, proven tooling — this repo orchestrates, it does not rewrite):
- Voice: Kokoro venv + chain.py at
  ~/workspace/financial-clarity/voice-tests/2026-11-15/work (am_onyx @ 0.80, long
  takes, post chain per playbook/producer-prompt.md).
- Pace measurement: measure_pace.py in the same folder.
- Edit/graphics: FFmpeg + Remotion builds live with each video's build scripts under
  ~/workspace/financial-clarity/shorts/<slug>/ (the pattern the wow batch used).
- QA: src/qa_gates.py in this repo (loudness, true peak, silence, dimensions,
  duration) + ASR check + framing frames, written into audit.md.
- Upload: YouTube Studio via Muse's browser flow (verify frames from the actual
  file first — hard rule); TikTok cross-posts on the spaced slate.

The Director (Muse) runs the stages, spawns the ten review passes as separate
reviewers, reconciles, and posts the verdict package. Nothing uploads during trial.
