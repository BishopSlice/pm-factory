---
name: opportunity-solution-tree
description: "Maps the success metric to user opportunities (problems) and candidate solutions, then picks one opportunity to pursue. Use in Discover once insights exist, to choose what to solve."
metadata:
  stage: 1-discover
  modes: [new, revamp]
  menu: "Map outcome to opportunities"
  recommend-when: "insights.md exists and ost.md does not"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/00-frame/brief.md (new) or projects/<name>/01-discover/current-product.md (revamp), projects/<name>/01-discover/insights.md, projects/<name>/01-discover/segments.md]
  writes: [projects/<name>/01-discover/ost.md]
  extras: []
---

# Opportunity solution tree

Connect the metric we want to move to the user problems that move it, and only then to solutions.

## Before you start
- In revamp mode there is no brief. Take the outcome from current-product.md (main metric today), or ask for it.

## Steps
1. **Set the outcome** at the top: the success metric from the brief (or current-product.md in revamp).
2. **List opportunities** as user problems or needs, in the user's words, each backed by an insight. Group them into parent and child where that helps. 4 to 8 at the top level.
3. **Size each opportunity** by evidence count, pain and the primary segment's fit.
4. **Pick one target opportunity.** **Checkpoint:** the user picks.
5. **Brainstorm 3 or more solutions** for the target only, from PM, design and engineering angles. Include one that isn't software.
6. **Write** `ost.md` with a text tree and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "We already have the solution" | Then compare it against two others. If it wins, you'll know why. |
| "Work on all the opportunities" | Spreading thin ships nothing. Pick one, learn, then move on. |

## Done when
- [ ] Every opportunity cites evidence
- [ ] One target opportunity was chosen by the user
- [ ] At least 3 distinct solutions for the target
- [ ] STATE.md is updated

## Output format
```
## TL;DR
<5 lines max>

## Tree
Outcome: <metric>
├─ Opportunity A (evidence: n) ★ target
│  ├─ Solution 1
│  ├─ Solution 2
│  └─ Solution 3
└─ Opportunity B (evidence: n)
## Why this target
```
