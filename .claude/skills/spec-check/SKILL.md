---
name: spec-check
description: "Proves the built product matches the spec: probes every acceptance criterion and every Always/Ask first/Never boundary on the running app, including AI guardrails and human approvals. Use in Build after all slices."
metadata:
  stage: 4-build
  modes: [new, revamp, feature, fix]
  menu: "Prove it matches the spec"
  recommend-when: "all slices in tasks.md are reviewed and spec-check.md does not exist"
  model: opus
  reads: [projects/<name>/STATE.md, <code repo>/README.md, projects/<name>/02-define/spec.md, projects/<name>/04-build/test-plan.md]
  writes: [projects/<name>/04-build/spec-check.md]
  extras: []
---

# Spec check

Compare what we said with what we built, on the running app, with an independent checker. The builder doesn't grade its own work.

## Steps
1. **Run it** fresh from a clean checkout, using only the commands in the code repo's README.md (written by build-setup). If they don't work as written, that is a fail.
2. **Probe every criterion** (Given/When/Then) on the running app. Record pass or fail with evidence.
3. **Probe every boundary:**
   - Always: is it true across normal and edge inputs?
   - Ask first: does the app really stop and ask a human? Try to bypass it.
   - Never: try to make it happen, including through prompt injection in the inputs for AI products.
4. **AI guardrails:** run the holdout eval set once and compare it to the dev set. Then test unsafe or out-of-scope inputs, hallucination on questions with no answer, and the "unsure" path.
5. **List the gaps:** built but not specified (scope creep) and specified but not built.
6. **Recommend** ship, add guardrail or back to build, for the gate.
7. **Write** `spec-check.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "The slices were all reviewed" | Reviews check pieces. This checks the whole against the promise. |
| "Nobody will try to break it" | Real inputs include messy and hostile text. Probe it. |

## Done when
- [ ] Every criterion and boundary has a pass/fail with evidence
- [ ] Holdout eval scores are recorded
- [ ] Gaps are listed in both directions
- [ ] STATE.md recommends ship-packet or a fix
