---
name: assumptions-to-experiment
description: "Lists the risky assumptions behind a chosen solution, ranks them by impact and uncertainty, and designs the cheapest real test for the riskiest ones. Use at the end of Discover, or as the 15-minute check in feature mode."
metadata:
  stage: 1-discover
  modes: [new, revamp, feature]
  menu: "Test the riskiest bet"
  recommend-when: "ost.md exists (or mode is feature) and assumptions.md does not"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/01-discover/ost.md (new, revamp), projects/<name>/01-discover/insights.md (new, revamp), projects/<name>/01-discover/current-product.md (revamp, feature)]
  writes: [projects/<name>/01-discover/assumptions.md]
  extras: []
---

# Assumptions to experiment

Find what has to be true for this to work, then test the scariest part cheaply before building.

## Mode switch
| Mode | What changes |
|---|---|
| new | Cover all 4 risk types. Prefer pretotypes (fake door, landing page, concierge, a manual run on real data). |
| revamp | Focus on value and usability for the changes. Tests can use existing users and analytics. |
| feature | Quick version: 3 to 5 assumptions about the feature request, one test. Takes 15 minutes. There is no ost.md or insights.md; use current-product.md and the request. Then the Discover gate sends it to Define. |

## Steps
1. **List assumptions** by risk type:
   - Value: do they want it?
   - Usability: can they use it?
   - Feasibility: can we build it, including data access and AI quality?
   - Viability: does it work for the business or the goal?
   Phrase each one as "We believe..."
2. **Rank** each on impact if wrong and current evidence (1 to 5). Riskiest = high impact, low evidence. Show a 2x2 or a ranked table.
3. **Pick the top 1 to 3.** **Checkpoint:** the user agrees.
4. **Design a test for each:** method, real data or users involved, a pass/fail threshold set **before** running, cost and time.
5. **Run or schedule.** If a test can run now, like a feasibility spike on real data, run it and record the result. Otherwise mark it planned.
6. **Write** `assumptions.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Set the threshold after seeing results" | Then every result looks like a pass. Decide first. |
| "Feasibility is obvious for AI products" | AI quality on real data is the most common surprise. Spike it. |

## Done when
- [ ] Assumptions span all relevant risk types
- [ ] The top assumptions have tests with thresholds set in advance
- [ ] Each test is run (with its result) or planned (with a date)
- [ ] STATE.md is updated

## Output format
```
## TL;DR
<5 lines max>

## Assumptions (ranked table: assumption, type, impact, evidence, risk)
## Tests
| Assumption | Method | Pass if | Cost | Status / result |
```
