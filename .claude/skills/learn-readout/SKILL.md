---
name: learn-readout
description: "Reads post-launch results against targets, labels them statistical or directional, turns failures into eval cases, and decides iterate, scale or stop. Use when launch data arrives or a live product has a problem (fix mode)."
metadata:
  stage: 5-launch-learn
  modes: [new, revamp, feature, fix]
  menu: "Read the results"
  recommend-when: "metrics.md exists and enough time has passed, or mode is fix"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/05-launch/metrics.md (not in fix mode), live data or the problem report]
  writes: [projects/<name>/05-launch/readout.md, new eval cases in <code repo>/evals/, projects/<name>/02-define/intake.md (fix mode)]
  extras:
    - label: "Write a SQL query for the data"
      show-when: "the data lives in a database"
---

# Learn readout

Say what happened, how sure we are, and what to do next.

## Mode switch
| Mode | What changes |
|---|---|
| new, revamp, feature | Full readout against targets |
| fix | Start here. Describe the problem with evidence, find which metric or users are affected, and write a fix intake for Define. |

## Steps
1. **Pull the data** for each metric in metrics.md: current value vs target vs baseline. In fix mode there may be no metrics.md: start from the problem report and pull only the data that shows the problem (errors, logs, affected users).
2. **Label confidence.** If there's enough data for a significance test (A/B or before/after), run it and report the confidence. Otherwise label it **directional** and say why.
3. **Segment it.** Break results down by user segment or cohort. Look for where the average hides a story.
4. **Mine the failures.** Collect failed AI outputs, errors and complaints. Turn each new failure type into an eval case.
5. **Decide:** iterate (back to Define with a focus), scale (more of the same) or stop. **Checkpoint:** the user decides.
6. **Write** `readout.md`. In fix mode, also write `02-define/intake.md`. Update STATE.md.

## Optional (one-liners)
- If the data is in a database, write the query.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "The number went up, so it worked" | Without confidence or a baseline, that could be noise. Label it. |
| "Failures are edge cases" | Today's edge case is tomorrow's top complaint. Add them to evals. |

## Done when
- [ ] Every metric has a value, target and confidence label
- [ ] New failures were added as eval cases
- [ ] The user made the iterate / scale / stop call
