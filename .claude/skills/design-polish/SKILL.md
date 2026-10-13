---
name: design-polish
description: "Factory Design step after design-critique: fixes only the accepted P0 and P1 findings in one batch, hardens states, copy and mobile layout, re-checks once and stops. For open-ended UI polish, use impeccable."
metadata:
  stage: 3-design
  modes: [new, revamp, feature, fix]
  menu: "Polish states and edges"
  recommend-when: "critique.md has accepted P0 or P1 findings that are still open"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/03-design/critique.md, projects/<name>/03-design/brief.md]
  writes: [prototype code, projects/<name>/03-design/critique.md]
  extras:
    - label: "Make it bolder / quieter / add motion"
      show-when: "the user says it feels bland, loud or static"
    - label: "Distill (remove anything not needed)"
      show-when: "critique flags clutter"
---

# Design polish

Close the accepted findings, then stop. A bounded pass keeps polish from turning into endless tweaking.

## Steps
1. **List the accepted P0 and P1 findings** from critique.md. Those are the only fixes in scope.
2. **Fix them in one batch,** in priority order. Use tokens only, and don't redesign what wasn't flagged.
3. **Harden** while you're in there: long text, missing data, slow network, double clicks, and a first-time user with no data.
4. **Check the copy:** buttons say what they do, errors say how to fix, and no jargon.
5. **Re-check once** in the browser at phone and desktop widths, in both themes. Mark each finding fixed or not fixed, with a before and after screenshot.
6. **Stop.** Any new issues go to the list for the next round, not this one.
7. **Update** critique.md and STATE.md.

## Optional (one-liners)
- If the user finds it bland, loud or static, adjust boldness or motion within the brief's tone.
- If critique flags clutter, distill: remove anything that doesn't serve the main task.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "While I'm here, let me also redesign X" | Scope creep resets the review. Log it for next round. |
| "One more pass will make it perfect" | Unbounded polish never ships. One re-check, then the gate. |

## Done when
- [ ] Every accepted P0 and P1 finding is marked fixed or explained
- [ ] Before and after screenshots exist
- [ ] STATE.md recommends the Design gate
