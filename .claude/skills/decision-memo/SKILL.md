---
name: decision-memo
description: "Records an important decision: context, options considered, the choice, why, and what evidence would change our mind. Use at any stage for decisions that are costly to reverse or likely to be questioned later."
metadata:
  stage: communicate
  modes: [new, revamp, feature, fix]
  menu: "Write a decision memo"
  recommend-when: "a gate decision or architecture choice was just made"
  model: opus
  reads: [projects/<name>/STATE.md, the files relevant to the decision]
  writes: [projects/<name>/comms/decisions/<nn>-<slug>.md]
  extras: []
---

# Decision memo

Future you, and your stakeholders, will ask "why did we do this?" Answer it once, now.

## Steps
1. **Frame the decision** as a question, with its deadline and owner.
2. **Context:** the facts and constraints, with file references.
3. **Options:** at least 2, including "do nothing". For each, give the pros, cons, cost and reversibility.
4. **Decision and why,** in 3 lines. **Checkpoint:** the user confirms this is the decision.
5. **What would change our mind:** the specific evidence that would trigger a revisit.
6. **Save** the memo and log it in STATE.md.

## Done when
- [ ] At least 2 real options were compared
- [ ] Revisit triggers are specific and observable
