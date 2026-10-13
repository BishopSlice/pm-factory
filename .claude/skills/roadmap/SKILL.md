---
name: roadmap
description: "Builds an outcome-based roadmap in now, next and later, where each item names the problem and the metric it should move, not just the feature. Use when planning beyond one cycle or presenting direction."
metadata:
  stage: communicate
  modes: [new, revamp, feature, fix]
  menu: "Build an outcome roadmap"
  recommend-when: "the user asks about what's next beyond the current cycle"
  model: sonnet
  reads: [projects/<name>/STATE.md, optional if they exist: projects/<name>/01-discover/ost.md, projects/<name>/02-define/spec.md (Later list), projects/<name>/05-launch/readout.md, projects/<name>/05-launch/retro.md]
  writes: [projects/<name>/comms/roadmap.md]
  extras: []
---

# Roadmap

Show where we're going and why, without promising dates for things we haven't learned about yet.

## Steps
1. **Gather candidates** from whichever of these exist: the opportunity tree, the readout, the spec's "Later" list and the retro. If none exist yet, ask the user for candidates.
2. **Rewrite each as an outcome:** problem, then the metric it moves, then a candidate solution. Features without an outcome get cut or questioned.
3. **Place each one** in Now (committed, this cycle), Next (likely, needs discovery) or Later (ideas). Confidence drops from left to right.
4. **Check capacity:** does Now fit the available time? **Checkpoint:** the user approves.
5. **Write** `roadmap.md` and log it in STATE.md.

## Done when
- [ ] Every item names its outcome metric
- [ ] Now fits capacity
- [ ] Next and Later have no dates
