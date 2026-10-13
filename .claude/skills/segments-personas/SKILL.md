---
name: segments-personas
description: "Groups users into segments by the job they are trying to do, using only evidence from insights, and writes up to 3 personas. Use in Discover after insights exist."
metadata:
  stage: 1-discover
  modes: [new, revamp]
  menu: "Find segments and personas"
  recommend-when: "01-discover/insights.md exists and segments.md does not"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/01-discover/insights.md, projects/<name>/00-frame/brief.md (new) or projects/<name>/01-discover/current-product.md (revamp)]
  writes: [projects/<name>/01-discover/segments.md]
  extras:
    - label: "Customer journey map"
      show-when: "the problem spans several steps or touchpoints"
---

# Segments and personas

Decide who we serve first. Segments come from behavior and jobs, not demographics.

## Steps
1. **List candidate segments** from insights.md. Split by job, context or level of pain, not by age or title. 3 to 5 segments.
2. **Score each one** on pain (from evidence counts), reachability and fit with the brief. Show the table with evidence references.
3. **Pick a primary segment.** **Checkpoint:** the user confirms it.
4. **Write up to 3 personas** for the top segments. Each persona gets a job to be done, a trigger, a current workaround, the top 3 pains and a quote. Every field cites an insight.
5. **Write** `segments.md` and update STATE.md.

## Optional (one-liners)
- If the problem spans several steps, add a journey map (stages, actions, pains, opportunities).

## Don't skip steps
| Excuse | Why not |
|---|---|
| "I know who the users are" | Then the evidence will confirm it quickly. If it doesn't, you've learned something. |
| "Add a fun persona backstory" | Fiction hides gaps. Only cite evidence. |

## Done when
- [ ] Every persona field traces to insights.md
- [ ] The primary segment was chosen by the user
- [ ] STATE.md is updated

## Output format
```
## TL;DR
<5 lines max>

## Segments (table with scores and evidence)
## Primary segment and why
## Personas
```
