---
name: red-team
description: "Attacks a spec before it gets built: steelmans it, finds the load-bearing assumptions and failure modes (including AI-specific risks), and sorts them into tigers, paper tigers and elephants. Use in Define after spec."
metadata:
  stage: 2-define
  modes: [new, revamp, feature, fix]
  menu: "Attack the spec"
  recommend-when: "spec.md exists and redteam.md does not (in fix mode, only if the fix changes agent behavior)"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/02-define/spec.md, projects/<name>/01-discover/assumptions.md]
  writes: [projects/<name>/02-define/redteam.md, projects/<name>/02-define/spec.md]
  extras: []
---

# Red team

Find what kills this before reality does. Be fair first, then be hard.

## Steps
1. **Steelman.** In 3 lines, state why this spec could succeed.
2. **Find the load-bearing assumptions:** the ones where, if wrong, the whole thing fails.
3. **Attack** from each angle that applies:
   - Users: wrong segment, no real pain, won't change habits
   - Data: access, quality, volume, terms of use, staleness
   - AI behavior: hallucination, prompt injection from inputs, drift, cost per run, latency, unfair or biased outputs
   - Ops: who fixes it when it breaks, monitoring
   - Scope: hidden complexity in "simple" criteria
4. **Imagine it failed** six months from now. Write the 3 most likely reasons.
5. **Sort** every risk:
   - **Tiger:** real, and will hurt
   - **Paper tiger:** looks scary, but isn't
   - **Elephant:** obvious, and nobody is talking about it
6. **For each tiger and elephant,** give the cheapest mitigation: a criterion, a boundary, an eval seed or a test. **Checkpoint:** the user accepts, mitigates or rejects each one.
7. **Apply** the accepted mitigations to spec.md, then write `redteam.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "The spec is solid, skip it" | That's when it matters most. Overconfidence is the elephant. |
| "List every possible risk" | A long list hides the tigers. Sort, then act on the few that matter. |

## Done when
- [ ] Every tiger and elephant is mitigated in spec.md or explicitly accepted by the user
- [ ] AI-specific risks were considered (or marked not applicable)
- [ ] STATE.md recommends tasks next

## Output format
```
## TL;DR
<5 lines max>

## Steelman
## Risks (table: risk, angle, type, mitigation, decision)
## Pre-mortem: top 3 failure reasons
## Changes made to spec.md
```
