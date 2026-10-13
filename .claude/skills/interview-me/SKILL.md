---
name: interview-me
description: "Asks the user one question at a time to pin down what they want from a product idea, and writes intent.md. Use at the start of Frame, after /factory sets up a new project. Not for customer or job interviews."
metadata:
  stage: 0-frame
  modes: [new]
  menu: "Pin down what I actually want"
  recommend-when: "projects/<name>/00-frame/intent.md does not exist"
  model: opus
  reads: [projects/<name>/STATE.md, learnings/]
  writes: [projects/<name>/00-frame/intent.md]
  extras: []
---

# Interview me

Get from a vague idea to a clear goal. Ask one question at a time and never more than 8 in total.

## Before you start
- Read STATE.md, then skim the TL;DRs in `learnings/` for anything relevant. Don't read other files.

## Steps
1. **Ask for the idea in one sentence**, plus why they care about it now.
2. **Ask one question per turn.** Prioritize what's still unknown, in this order:
   - Who has the problem? Name a real person or group.
   - What do they do today instead?
   - What would "this worked" look like in 3 months?
   - What can't change: time, money, tools, data, accounts? If the idea depends on a third-party product or data source, confirm it is still live and maintained.
   - What's the real motive? Portfolio, revenue, learning, a work goal?
   Offer 2 to 4 likely answers as options so replying is fast.
3. **Push back once** on any answer that sounds like what they think they should want. Ask: "If nobody else saw this, would you still pick it?"
4. **Play it back** in 5 lines. **Checkpoint:** the user confirms or corrects it.
5. **Write** `00-frame/intent.md` and update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "The idea is clear enough already" | Unstated constraints sink projects later. Two minutes here saves days. |
| "Ask all the questions at once" | A wall of questions gets shallow answers. One at a time goes deeper. |

## Done when
- [ ] The user confirmed the playback
- [ ] intent.md covers who, current workaround, success in 3 months, constraints and motive
- [ ] STATE.md logs this step and recommends idea-refine next

## Output format
```
## TL;DR
<5 lines max>

## Who and problem
## What they do today
## Success in 3 months
## Constraints
## Motive
## Open questions
```
