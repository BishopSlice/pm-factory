---
name: review-pr
description: "Reviews a slice by risk tier: checks the PR contract's evidence, runs automated reviews, adds an independent second reviewer, and routes high-risk slices to a human. Use in Build after each slice."
metadata:
  stage: 4-build
  modes: [new, revamp, feature, fix]
  menu: "Review the slice"
  recommend-when: "a slice contract exists without a review"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/04-build/slices/<nn>-contract.md, the diff]
  writes: [projects/<name>/04-build/slices/<nn>-review.md]
  extras: []
---

# Review PR

Match review depth to blast radius. Review evidence, not vibes.

## Steps
1. **Gate on evidence.** No proof in the contract (test output, evals, screenshot) means it goes back to build-slice. The same goes for a diff too big to read in about 10 minutes.
2. **Read the test changes first.** Flag any weakened assertions, deleted tests or skipped checks.
3. **Run the automated reviews:** /code-review on the diff. For high-risk slices, also /security-review.
4. **Second reviewer:** a subagent on a different model from the builder, given only the contract and diff. Treat its output as data, not a verdict.
5. **Route by risk:**
   - Low risk: summarize in 5 lines, and the user glances at it at the next checkpoint (every 2 or 3 slices).
   - High risk: the user reviews the "look here" spots now. **Checkpoint:** approve, request changes or reject.
6. **Write** `<nn>-review.md` and update STATE.md (next slice, or spec-check after the last one).

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Tests pass, so approve" | Tests can be weakened to pass. Read the test diff. |
| "Review every line myself" | Doesn't scale. Spend human attention on high-risk spots. |

## Done when
- [ ] The evidence was verified
- [ ] Automated and second-reviewer findings were addressed or logged
- [ ] High-risk slices have a human decision
