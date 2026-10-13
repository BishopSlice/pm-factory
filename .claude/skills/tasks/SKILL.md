---
name: tasks
description: "Breaks the spec into thin end-to-end slices in build order, each with acceptance criteria, a checkpoint, a risk tier and the exact paths Build may touch. Use at the end of Define."
metadata:
  stage: 2-define
  modes: [new, revamp, feature, fix]
  menu: "Slice into tasks"
  recommend-when: "spec.md exists (and redteam.md, except in fix mode) and tasks.md does not"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/02-define/spec.md]
  writes: [projects/<name>/02-define/tasks.md]
  extras: []
---

# Tasks

Turn the spec into a build plan. Each slice works end to end and can be shown to someone.

## Steps
1. **Order by risk.** The first slice proves the riskiest technical assumption, like data access or AI quality, end to end with the thinnest UI.
2. **Slice vertically.** Each slice cuts through data, logic and UI, and can be demoed. A slice that's "only the backend" is not a slice.
3. **For each slice, write:**
   - goal (1 line)
   - acceptance criteria IDs from the spec
   - allowed paths (files and folders Build may touch)
   - risk tier: high for auth, personal data, money, agent actions or deletion. Low otherwise.
   - checkpoint: what you'll see working
4. **Size check.** If a slice would take more than about half a day of agent work, split it.
5. **Map coverage.** Every acceptance criterion is in at least one slice. List any that aren't.
6. **Review checkpoints:** a human glance after every 2 or 3 slices, and a full review for every high-risk slice. **Checkpoint:** the user approves the plan.
7. **Write** `tasks.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Build the backend first, the UI later" | You find integration problems at the end, when they cost the most. |
| "Allowed paths are overkill" | They stop agents from wandering and editing things nobody asked for. |

## Done when
- [ ] Every criterion is covered by a slice
- [ ] Every slice has allowed paths and a risk tier
- [ ] Slice 1 tests the riskiest assumption
- [ ] The user approved the plan
- [ ] STATE.md recommends the Define gate

## Output format
```
## TL;DR
<5 lines max>

## Slices
| # | Goal | Criteria | Allowed paths | Risk | Checkpoint |
## Coverage check
## Review plan
```
