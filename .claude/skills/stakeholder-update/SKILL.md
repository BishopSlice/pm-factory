---
name: stakeholder-update
description: "Writes a short status update for a specific audience from STATE.md: progress, decisions, risks and asks. Maps stakeholders first if needed. Use at any stage when someone needs to be kept in the loop."
metadata:
  stage: communicate
  modes: [new, revamp, feature, fix]
  menu: "Write a stakeholder update"
  recommend-when: "the user mentions an update, a meeting or a stakeholder"
  model: sonnet
  reads: [projects/<name>/STATE.md, TL;DRs of the files it lists]
  writes: [projects/<name>/comms/<date>-update.md]
  extras:
    - label: "Summarize a meeting transcript"
      show-when: "the user shares a transcript or meeting notes"
---

# Stakeholder update

Tell the right person what they need to know, in under a minute of their reading time.

## Steps
1. **Audience.** Who is it for, and what do they care about (outcome, risk, timeline, their team)? If there are several stakeholders, map them first by influence and interest, and pick a format for each. **Checkpoint:** confirm the audience.
2. **Gather** from STATE.md and output TL;DRs only.
3. **Write** in this order: the headline (one line), progress vs plan, decisions made, risks with mitigations, and **asks** (what you need from them, by when).
4. **Trim** to 150 words or fewer for executives, 300 for working teams. Bold the ask.
5. **Save** to `comms/` and log it in STATE.md.

## Optional (one-liners)
- If given a meeting transcript, summarize it: decisions, action items with owners, open questions.

## Done when
- [ ] The headline makes sense on its own
- [ ] Every risk has a mitigation
- [ ] The ask is explicit, with a date
