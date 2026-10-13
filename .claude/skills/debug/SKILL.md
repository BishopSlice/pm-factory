---
name: debug
description: "Finds the root cause of a failing test, build, check or code behavior: reproduce, isolate, fix with a regression test, log the lesson. Use while building. For live product problems, use learn-readout."
metadata:
  stage: 4-build
  modes: [new, revamp, feature, fix]
  menu: "Find the root cause"
  recommend-when: "a check, test or eval is failing"
  model: opus
  reads: [projects/<name>/STATE.md, the failing output, projects/<name>/lessons.md]
  writes: [the fix, a regression test, projects/<name>/lessons.md]
  extras: []
---

# Debug

Find why before changing anything. Guessing makes new bugs.

## Steps
1. **Reproduce** it reliably. Write down the exact command and output. If it can't be reproduced, gather more data first.
2. **Check lessons.md.** Has this happened before?
3. **Isolate.** Narrow it down: recent changes (git diff or bisect), inputs and environment. Form one hypothesis at a time and test it.
4. **Name the root cause** in one sentence. **Checkpoint** for high-risk code: the user agrees before the fix.
5. **Write a failing regression test,** then fix. Run all checks.
6. **Ratchet.** Add one line to lessons.md: the symptom, the cause and the rule that prevents it. If it's a rule for every project, flag it for `learnings/`.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Try changes until it passes" | That hides the cause, and it comes back. |
| "Change the test so it passes" | That deletes the alarm, not the fire. Only change a test if the test was wrong, and say so. |

## Done when
- [ ] The root cause is stated
- [ ] A regression test fails before the fix and passes after
- [ ] lessons.md has a new line
