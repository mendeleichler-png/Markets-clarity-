# markets clarity — Shorts Producer Agent

The packaged producer from playbook/blueprint.md (Option A: built here). This repo is
the agent's brain: rules, prompts, config, and one folder per video. The repo copies
under playbook/ are canonical from 2026-11-15; the pre-repo originals remain in
~/workspace/financial-clarity/ as history.

## Layout
- playbook/ — the rules (playbook, script standard, narration standard, producer prompt, blueprint)
- prompts/ — one prompt per pipeline stage, incl. the ten review passes
- config/ — models.yaml (routing + voice), gates.yaml (measured thresholds), slate.yaml
- templates/ — sources/script/shotlog/audit/metadata skeletons
- videos/ — one folder per video (_template/ is the starting skeleton)
- board/ — local mirror of the Notion board + Slack control room until they connect
- src/ — pipeline driver doc + qa_gates.py (measured gate checks)

## Status (2026-11-15)
- Phase 0 packaging: DONE (this repo, local git).
- Connectors: GitHub authorized 2026-11-15 (repo selection pending owner install step);
  Notion CONNECTED 2026-11-15 — the live board is the 'markets clarity — Producer Agent'
  page (Slate + Published databases, seeded); Slack SKIPPED by owner decision 2026-11-15 — the control room is the owner's Muse chat (see board/control-room.md).
  board/ holds the local mirrors the Notion board was seeded from.
- Phase 1: proof video through the packaged system (Leeson/Barings or Kerviel/SocGen).

## Rules that never change
Anonymity (never the owner's name, never "Heimishe Investing Hub"), edit-don't-generate,
facts from dated primary sources, ten-pass script review, measured gates, owner verdict
before anything is called final, no uploads during trial, no spend without approval.
