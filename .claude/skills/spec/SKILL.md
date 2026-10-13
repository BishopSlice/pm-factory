---
name: spec
description: "Writes a two-layer spec: a PM layer (problem, scope, metric) and a machine layer (Given/When/Then acceptance criteria, Always/Ask first/Never boundaries, eval seeds). Use in Define after intake."
metadata:
  stage: 2-define
  modes: [new, revamp, feature, fix]
  menu: "Write the spec"
  recommend-when: "intake.md exists and spec.md does not"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/02-define/intake.md]
  writes: [projects/<name>/02-define/spec.md]
  extras:
    - label: "OKRs for the success metrics"
      show-when: "the user mentions team goals or a work context"
    - label: "Loop add-on (schedule, sources, checker, memory)"
      show-when: "the product runs on a schedule or in a loop"
---

# Spec

One document that both a stakeholder and a coding agent can act on. If a criterion can't be tested, it isn't done yet.

## Mode switch
| Mode | Scope of the spec |
|---|---|
| new | Full spec |
| revamp | Full spec plus a keep / change / remove table for the existing product |
| feature | Delta only: what changes, what must not break |
| fix | Short: steps to reproduce, expected result, actual result, a regression test, and the boundary for the fix |

## Steps
1. **PM layer.** Problem, user, outcome metric with a target, scope (in and out), and **Not doing**. **Checkpoint:** the user agrees on scope.
2. **Cut to the smallest version** that moves the metric. Move everything else to "Later" with one line each.
3. **Acceptance criteria.** For each requirement, write Given / When / Then. Each criterion must be checkable by a test or an eval.
4. **Boundaries** in 3 tiers:
   - **Always:** things the system must always do
   - **Ask first:** actions that need human approval
   - **Never:** forbidden actions. Include secrets, personal data and destructive actions.
5. **Eval seeds.** For every criterion involving AI output, write 2 or 3 example inputs with the expected output or a grading rule. Use real data examples where possible. These become the goldens in Build's test-plan.
6. **Tech notes.** Stack, data sources and access method, and known constraints. Keep these short, since the details go in Build.
7. **Write** `spec.md` and update STATE.md.

## Optional (one-liners)
- In a work context, express the metrics as OKRs.
- For loop or scheduled products, add: schedule, sources, maker and checker roles, the checker's pass rules, memory (what carries over between runs) and the stop condition.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "The criteria are obvious" | Agents build exactly what's written. Unwritten means unbuilt or built wrong. |
| "Evals can come later" | Without seeds now, Build tests whatever is easy, not what matters. |
| "No Never list needed for a small app" | Agents with tools can delete, leak or spam. One line of Never is cheap insurance. |

## Done when
- [ ] Every requirement has at least one testable Given/When/Then
- [ ] Always / Ask first / Never are filled in
- [ ] Every AI behavior has eval seeds
- [ ] Not doing and Later lists exist
- [ ] STATE.md recommends red-team next (or tasks in fix mode)

## Output format
```
## TL;DR
<5 lines max>

# PM layer
## Problem and user
## Outcome metric and target
## Scope / Not doing / Later

# Machine layer
## Acceptance criteria (ID, Given, When, Then)
## Boundaries (Always / Ask first / Never)
## Eval seeds (criterion ID, input, expected or grading rule)
## Tech notes
## Loop add-on (if used)
```
