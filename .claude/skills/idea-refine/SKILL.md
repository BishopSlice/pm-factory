---
name: idea-refine
description: "Turns a stated intent into a sharp problem brief with one chosen direction, a success metric and a vision line. Use in Frame after interview-me, or when an idea needs sharpening."
metadata:
  stage: 0-frame
  modes: [new]
  menu: "Sharpen the idea"
  recommend-when: "intent.md exists and brief.md does not"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/00-frame/intent.md]
  writes: [projects/<name>/00-frame/brief.md]
  extras:
    - label: "Value proposition lens (who, before, how, after, alternatives)"
      show-when: "the user is unsure why someone would switch"
---

# Idea refine

Widen first, then narrow. End with one direction you can test.

## Steps
1. **Restate the problem** in one sentence from the user's side. **Checkpoint:** the user agrees.
2. **Widen.** Give 5 or 6 distinct directions, each a different bet: a different user, a different job, or a different mechanism. Include one boring option and one bold one. Two lines each.
3. **Narrow.** Score each direction on pain, reach, feasibility with the stated constraints, and fit with the motive (1 to 5 each). Show the table.
4. **Pick.** Recommend one and say why. **Checkpoint:** the user picks, which may be a different one.
5. **Define success.** One measurable metric with a target and a timeframe, plus one leading signal you can see within 2 weeks.
6. **Write the vision line:** "For <user> who <problem>, <product> <does what>, unlike <alternative>."
7. **Write** `00-frame/brief.md` and update STATE.md.

## Optional (one-liners)
- If the user is unsure why someone would switch, add a value proposition: who, before, how, after, alternatives.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "We already know the direction" | Seeing alternatives is how you check it's the best one. It takes 2 minutes. |
| "Success is hard to measure, skip it" | Without a metric, the gate has nothing to judge. Pick a proxy. |

## Done when
- [ ] The brief has a problem, a user, a chosen direction with its rejected alternatives, a metric, a 2-week signal and a vision line
- [ ] The user picked the direction
- [ ] STATE.md recommends landscape-and-sizing next

## Output format
```
## TL;DR
<5 lines max>

## Problem
## Target user
## Direction chosen (and why)
## Directions rejected (one line each)
## Success metric and 2-week signal
## Vision line
```
