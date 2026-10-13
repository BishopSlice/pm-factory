---
name: measure-setup
description: "Sets up how success is measured after launch: a North Star metric, input metrics, health guardrails, a simple dashboard and weekly production evals for AI output. Use in Launch & Learn before or at launch."
metadata:
  stage: 5-launch-learn
  modes: [new, revamp, feature]
  menu: "Set up metrics and live evals"
  recommend-when: "05-launch/metrics.md does not exist"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/02-define/spec.md (metric section), projects/<name>/04-build/test-plan.md, .claude/skills/test-plan/evals.md]
  writes: [projects/<name>/05-launch/metrics.md, instrumentation code]
  extras: []
---

# Measure setup

Decide what to watch before launch, so the readout has real data instead of guesses.

## Steps
1. **North Star:** the one metric that shows users getting value. Start from the spec's outcome metric.
2. **Input metrics,** 2 to 4 levers that drive it (e.g. activation, repeat use, completion rate).
3. **Health guardrails:** things that must not get worse (errors, latency, cost per run, complaints).
4. **AI quality in production:** sample live outputs weekly and score them with the test-plan rubric (see evals.md). Track the pass rate over time.
5. **Instrument:** add event logging for each metric with the simplest tool that fits (logs, a database table, free analytics). Respect the spec's Never list for personal data.
6. **Dashboard:** one view with each metric, its target, its current value and an alert threshold. **Checkpoint:** the user agrees on targets.
7. **Write** `metrics.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Track everything, decide later" | Too much data means no decision. Pick the few that matter. |
| "Evals were done in Build" | Real inputs drift. Production quality must be measured too. |

## Done when
- [ ] North Star, inputs and guardrails have targets
- [ ] Events are logged and visible
- [ ] Weekly production eval sampling is set up
