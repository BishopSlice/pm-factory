---
name: build-slice
description: "Builds one slice from tasks.md: tests first, only inside the slice's allowed paths, with every check run, ending in a PR contract with evidence. Use in Build for each slice."
metadata:
  stage: 4-build
  modes: [new, revamp, feature, fix]
  menu: "Build the next slice"
  recommend-when: "test-plan.md exists and tasks.md has an unfinished slice"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/02-define/tasks.md (the current slice only), projects/<name>/04-build/test-plan.md, projects/<name>/lessons.md]
  writes: [code inside the slice's allowed paths, projects/<name>/04-build/slices/<nn>-contract.md, projects/<name>/04-build/test-plan.md (Baseline section, slice 1 only)]
  extras: []
---

# Build slice

One thin slice, built properly, with proof. Then stop.

## Steps
1. **Load the slice:** its goal, criteria, allowed paths and risk tier. Read lessons.md. Make a branch for the slice.
2. **Write failing tests first** for the slice's criteria (and evals if it touches AI behavior). Confirm they fail for the right reason.
3. **Build in small steps.** After each step, run the checks. Commit when they pass. Touch only the allowed paths. If you need another path, stop and ask.
4. **Run everything:** typecheck, lint, all tests, the relevant evals. On slice 1, run the full eval set and record the scores as the baseline in test-plan.md. On later slices, compare evals to that baseline.
5. **Run it.** Use the feature yourself in the browser or CLI and capture a screenshot or output.
6. **Clean up** with /simplify on the changed files.
7. **Write the PR contract** at `slices/<nn>-contract.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "I'll write tests after" | Tests written after tend to test what was built, not what was asked. |
| "Quick fix in a file outside the slice" | Unasked changes are where surprises come from. Ask first. |
| "Checks are slow, skip them once" | Skipped once becomes skipped always. Run them. |

## Done when
- [ ] Tests and checks pass. Slice 1: the baseline is recorded. Later slices: evals are at or above baseline
- [ ] Only allowed paths were changed
- [ ] The PR contract has real evidence
- [ ] STATE.md recommends review-pr

## PR contract format
```
## Intent (1-2 sentences)
## Criteria covered (IDs)
## Proof (test output, eval scores vs baseline, screenshot)
## Risk tier and why
## What AI wrote vs what a human wrote
## Look here (1-2 spots for human review)
## Decisions and rejected alternatives
```
