---
name: design-critique
description: "Reviews a running prototype with two independent reviewers (design and technical), then merges their findings into ranked P0 to P3 fixes. Use in Design after a prototype exists."
metadata:
  stage: 3-design
  modes: [new, revamp, feature, fix]
  menu: "Critique with two reviewers"
  recommend-when: "a prototype exists and 03-design/critique.md does not"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/03-design/brief.md, projects/<name>/03-design/prototype.md, checklist.md (this folder)]
  writes: [projects/<name>/03-design/critique.md]
  extras:
    - label: "Run impeccable's automated audit"
      show-when: "the impeccable plugin is installed"
---

# Design critique

Two reviewers who don't see each other's notes catch more than one. Review the running app, not just the code.

## Steps
1. **Start the prototype** and open it in a browser. Take screenshots of each screen at phone and desktop widths, in light and dark mode.
2. **Reviewer A, design** (a subagent on Sonnet). It gets the brief, the screenshots and sections 1 to 4 of `checklist.md`, and walks the main task path as a first-time user.
3. **Reviewer B, technical** (a separate subagent on Sonnet). It gets the running app and section 5 of `checklist.md`: accessibility, responsiveness and console errors.
4. **Merge** (this skill, on Opus). Dedupe the findings, then rank them:
   - **P0:** blocks the main task or breaks trust
   - **P1:** causes confusion or errors
   - **P2:** polish
   - **P3:** nice to have
   Each finding gets the screen, the checklist ID and a suggested fix.
5. **Check the brief:** does the result match the tone, states and AI states? Note any drift.
6. **Present P0 and P1.** **Checkpoint:** the user accepts, defers or rejects each one.
7. **Write** `critique.md` and update STATE.md.

## Optional (one-liners)
- If the impeccable plugin is installed, run its audit and merge its findings as reviewer C.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "One reviewer is enough" | Reviewers anchor on what they notice first. Two independent passes cover more. |
| "Review the code, skip the browser" | Users never see the code. Many problems only show when it runs. |

## Done when
- [ ] Both reviewers ran independently on the live prototype
- [ ] Findings are ranked P0 to P3 with checklist IDs
- [ ] The user decided on every P0 and P1
- [ ] STATE.md recommends design-polish (or the Design gate if there are no accepted P0 or P1 items)

## Output format
```
## TL;DR
<5 lines max>

## Findings (table: ID, priority, screen, checklist ref, issue, fix, decision)
## Brief drift
## Screenshots reviewed
```
