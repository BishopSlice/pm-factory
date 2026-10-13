---
name: define-intake
description: "Starts Define by checking which inputs exist for this mode, summarizing them in one place, and asking only for what is missing. Use at the start of Define in any mode."
metadata:
  stage: 2-define
  modes: [new, revamp, feature, fix]
  menu: "Check inputs and fill gaps"
  recommend-when: "02-define/intake.md does not exist, or mode is fix and STATE.md does not log define-intake for this cycle"
  model: sonnet
  reads: [projects/<name>/STATE.md, files listed under "Files for the next stage", projects/<name>/01-discover/current-product.md (revamp, feature), projects/<name>/02-define/intake.md (fix, written by learn-readout)]
  writes: [projects/<name>/02-define/intake.md]
  extras: []
---

# Define intake

Give the spec one clean input file, so spec never has to hunt through earlier stages.

## Mode switch
| Mode | Needs |
|---|---|
| new, revamp | Problem, user, metric, target opportunity, chosen solution, test results |
| feature | The existing product's context, the feature request, its user, a quick assumption check |
| fix | What broke, evidence (logs, readout, reports), the expected behavior. learn-readout already wrote intake.md: check it against this row and fill gaps. Don't start over. |

## Steps
1. **Read** STATE.md, then only the TL;DRs of the files it lists.
2. **Fill the needs table** for this mode. Each row is found (with a file reference) or missing.
3. **Ask for missing items** one at a time, with suggested answers. In feature or fix mode, ask for paths to the existing product's docs or code if they're needed.
4. **Write** `intake.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Spec can read everything itself" | That burns tokens and mixes stale context in. One intake file is cheaper and clearer. |

## Done when
- [ ] Every need is found or answered
- [ ] intake.md is under one page
- [ ] STATE.md recommends spec next

## Output format
```
## TL;DR
<5 lines max>

## Needs (table: need, answer, source)
## Constraints carried forward
## Open risks from Discover
```
