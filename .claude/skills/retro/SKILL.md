---
name: retro
description: "Runs a short retro on a finished cycle: what to keep, what to change, and which lessons get promoted from the project's lessons.md to the shared learnings folder. Use at the end of Launch & Learn."
metadata:
  stage: 5-launch-learn
  modes: [new, revamp, feature]
  menu: "Retro and ratchet"
  recommend-when: "readout.md exists and retro.md does not"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/05-launch/readout.md, projects/<name>/lessons.md, projects/<name>/activity.log]
  writes: [projects/<name>/05-launch/retro.md, learnings/<stage>.md, projects/<name>/lessons.md (removes promoted or outdated lines)]
  extras: []
---

# Retro

Turn this cycle's experience into rules that make the next one faster.

## Steps
1. **Timeline:** use STATE.md and activity.log to list the stages, the time each took and any gate decisions that sent work back.
2. **Keep / change / try:** 3 items each, with evidence.
3. **Review lessons.md.** For each lesson, decide:
   - project-only: keep it here
   - every project: promote it to `learnings/<stage>.md`
   - outdated: delete it
4. **Check the factory itself.** Did a skill step get skipped, cause confusion or prove unnecessary? Note proposed skill edits. Don't make them here.
5. **Where it goes.** Personal projects promote to `learnings/`. Work projects promote to that employer's own learnings folder, never the shared one. **Checkpoint:** the user approves the promotions.
6. **Write** `retro.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "It went fine, skip the retro" | Then the next project repeats the same friction. 15 minutes. |
| "Promote every lesson" | A long learnings file gets ignored. Only promote what applies broadly. |

## Done when
- [ ] Keep / change / try is written
- [ ] Each lesson is kept, promoted or deleted
- [ ] Proposed factory edits are listed
