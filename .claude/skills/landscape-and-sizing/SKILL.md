---
name: landscape-and-sizing
description: "Sizes the market and scans competitors and alternatives for a brief, with a source and date on every number. Use in Frame before the gate, or when someone asks \"is this big enough?\"."
metadata:
  stage: 0-frame
  modes: [new]
  menu: "Size the market, scan competitors"
  recommend-when: "brief.md exists and landscape.md does not"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/00-frame/brief.md]
  writes: [projects/<name>/00-frame/landscape.md]
  extras:
    - label: "Lean canvas or business model"
      show-when: "the motive is revenue or a startup"
    - label: "SWOT for an exec audience"
      show-when: "the user mentions stakeholders, leadership or a review"
---

# Landscape and sizing

Answer two questions with evidence: Is the space big enough for the goal? What will users compare us to?

## Steps
1. **Pick the right size of "big".** A portfolio project needs reachable users, not a big total market. A business needs a total market (TAM), the share you can serve (SAM) and the share you can win (SOM). **Checkpoint:** confirm which one applies.
2. **Size it two ways.**
   - Top-down: start from a published total and narrow it.
   - Bottom-up: number of users × usage × value.
   Show the math. If the two results differ by more than 3x, say why.
3. **List alternatives,** including "do nothing" and spreadsheets. Up to 6 entries. For each, give who uses it, what it does well and its biggest gap.
4. **Find the opening:** one gap that the brief's direction exploits. If there isn't one, say so plainly.
5. **Cite everything.** Each number and claim gets a source link and a date. Mark any estimate as an estimate.
6. **Write** `00-frame/landscape.md` and update STATE.md.

## Optional (one-liners)
- If the motive is revenue, add a lean canvas.
- If leadership will see it, add a SWOT.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "No real competitors exist" | There's always an alternative, even if it's doing nothing. Name it. |
| "Exact numbers don't matter" | The order of magnitude matters, and it needs a source. |

## Done when
- [ ] Every number has a source and date, or is labeled as an estimate
- [ ] At least 3 alternatives, including "do nothing"
- [ ] One stated opening, or an explicit "no clear opening"
- [ ] STATE.md recommends the Frame gate if the exit checklist is met

## Output format
```
## TL;DR
<5 lines max>

## Size (method, math, sources)
## Alternatives (table)
## The opening
## Sources
```
