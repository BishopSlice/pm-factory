---
name: interview
description: "Writes a customer research interview script with no leading questions, then turns each user transcript into notes and updates insights. Use in Discover to talk to real users. Not for job interview prep."
metadata:
  stage: 1-discover
  modes: [new, revamp]
  menu: "Script and summarize interviews"
  recommend-when: "the user can reach real users and 01-discover/insights.md does not exist"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/00-frame/brief.md (new) or projects/<name>/01-discover/current-product.md (revamp)]
  writes: [projects/<name>/01-discover/interview-script.md, projects/<name>/01-discover/interviews/<nn>-<who>.md, projects/<name>/01-discover/insights.md]
  extras: []
---

# Interview

Learn from what people did in the past, not what they say they'd do. Two modes: **script** before the calls, **summarize** after each one.

## Before you start
- Read STATE.md and the brief's TL;DR (new mode). In revamp mode, read current-product.md instead, including its known issues.

## Steps: script
1. **Set 3 learning goals** from the riskiest unknowns in the brief (or current-product.md). **Checkpoint:** the user agrees.
2. **Draft the script** in 4 parts: warm-up (2 min), the last time it happened (story, 15 min), current workaround and cost (10 min), wrap-up and referrals (3 min).
3. **Run the leading-question check.** Rewrite any question that pitches the idea, asks about the future ("would you use...?") or can be answered yes/no.
4. **Write** `interview-script.md`, including who to recruit and how many (5 per segment is a good start).

## Steps: summarize (one transcript at a time)
1. **Extract** the job they were trying to do, the trigger, the current workaround, the pains (with quotes), and any signal of willingness to pay or switch.
2. **Separate facts from opinions.** Past behavior counts as evidence. Compliments and predictions don't.
3. **Write** `interviews/<nn>-<who>.md`. Strip personal details. Use a role, not a name.
4. **Update** `insights.md`: add or strengthen themes, and give each one a count ("4 of 6"), a quote and its file reference. Use "n/a" for Trend if there is only one round of calls.

## Optional (one-liners)
- For a large batch of transcripts, hand them to feedback-mining instead.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Just ask if they'd use it" | People are polite. Past behavior is the only honest signal. |
| "I'll summarize them all at the end" | Memory blends calls together. Summarize each one within a day. |

## Done when
- [ ] The script passes the leading-question check
- [ ] Each transcript has a summary with no personal details
- [ ] insights.md themes have counts and quotes with sources
- [ ] STATE.md is updated

## Output format (insights.md, shared with feedback-mining. If insights.md already exists, add to it in this format)
```
## TL;DR
<5 lines max>

## Themes
| Theme | Count | Trend | Sentiment | Strongest quote | Sources |
## Surprises
## Data caveats (volume, window, spot-check error rate, or interview count)
## Open questions
```
