---
name: test-plan
description: "Turns the spec's acceptance criteria and eval seeds into a test plan plus an eval set (goldens, slices, holdout, judge rubric) and a runnable eval harness. Use in Build before writing feature code."
metadata:
  stage: 4-build
  modes: [new, revamp, feature, fix]
  menu: "Plan tests and evals"
  recommend-when: "constraints.md exists and 04-build/test-plan.md does not"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/02-define/spec.md, projects/<name>/04-build/constraints.md, evals.md (this folder)]
  writes: [projects/<name>/04-build/test-plan.md, <code repo>/evals/]
  extras: []
---

# Test plan

Decide what "working" means in numbers before building. Regular code gets tests. AI behavior gets evals.

## Steps
1. **Sort the criteria.** For each acceptance criterion, decide: unit test, integration test, eval (AI output) or manual check. Map every criterion to at least one.
2. **Plan the tests:** happy path, edge cases (empty, huge, malformed, slow) and the regression test for fix mode. List them by criterion ID.
3. **Build the eval set** for AI behavior. Follow `evals.md`:
   - goldens from the eval seeds plus real data
   - slices by category
   - a holdout set you never tune on
   - a judge rubric for open-ended output
4. **Set thresholds** from constraints.md. **Checkpoint:** the user agrees on the goldens and thresholds.
5. **Harness.** Write one command that runs the whole eval set and prints scores per slice tag. It can fail for now, since no feature code exists yet. Leave a "Baseline" section in test-plan.md marked pending. build-slice records the baseline at the end of slice 1.
6. **Write** `test-plan.md` and the eval files, then update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "The AI output looks good when I try it" | A few tries hide failure rates. Evals give a number you can improve. |
| "Make up the goldens" | Invented goldens test the model's imagination. Use real cases. |
| "Tune on all the data" | Then the score lies. Keep a holdout. |

## Done when
- [ ] Every criterion maps to a test, an eval or a manual check
- [ ] Evals have goldens, slices, a holdout and a rubric
- [ ] Thresholds were agreed with the user
- [ ] The eval command runs, and the Baseline section is marked pending
- [ ] STATE.md recommends build-slice next
