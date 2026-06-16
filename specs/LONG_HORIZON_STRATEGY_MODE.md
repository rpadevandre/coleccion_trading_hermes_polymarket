# AION Long-Horizon Strategy Mode

## Purpose

Andre wants a mode similar to `/goal`, but more strategic: AION should hold a long-term objective, periodically refine strategy, ingest new readings, improve its own skills/specs, and keep momentum without needing the whole context repeated.

This is not a live trading bot. It is a long-running strategy loop.

## Name

`AION_LONG_STRATEGY`

## Behavior

On each cycle, AION should:

1. Read the standing objective.
2. Check current repo artifacts.
3. Inspect new/changed research sources if available.
4. Compare current system against desired architecture.
5. Pick the highest-leverage next improvement.
6. Write a short strategy report.
7. If safe and clearly beneficial, update specs/skills/plans.
8. Never enable live financial execution by itself.

## Standing Objective

Build AION into Andre's repo-first operating agent for:

- Polymarket intelligence,
- paper trading,
- risk-controlled execution architecture,
- business/product synthesis from readings,
- eventual switch-controlled live micro-wallet only after evidence.

## Output Format

Each cycle should produce:

```text
reports/strategy/YYYY-MM-DD_AION_LONG_STRATEGY.md
```

Sections:

- What changed since last cycle
- New useful readings/repos/signals
- Current bottleneck
- Recommended next improvement
- Files updated
- Risks or blockers
- Next cycle focus

## Relationship to Hermes `/goal`

Hermes `/goal` is an interactive/persistent objective mechanism. This repo mode is the artifact-backed version:

- `/goal` = agent runtime objective
- `AION_LONG_STRATEGY` = repo-visible strategy loop + reports + skill updates

## Guardrails

- Do not trade live.
- Do not add secrets.
- Do not modify unrelated repos.
- Do not create noisy cron outputs.
- Do not rewrite strategy every cycle without evidence.
- Preserve paper-first discipline.
