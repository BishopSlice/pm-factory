---
name: feedback-mining
description: "Pulls real feedback from named sources (GitHub, forums, reviews, support exports), clusters it into cited themes with counts and trends, and writes the insights file. Use in Discover when feedback already exists."
metadata:
  stage: 1-discover
  modes: [new, revamp, feature]
  menu: "Mine public or existing feedback"
  recommend-when: "feedback sources exist (public channels or exports) and 01-discover/insights.md does not exist"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/00-frame/brief.md (new) or projects/<name>/01-discover/current-product.md (revamp), feedback sources listed in STATE.md]
  writes: [projects/<name>/01-discover/sources.md, projects/<name>/01-discover/raw/, projects/<name>/01-discover/insights.md]
  extras:
    - label: "Feature request triage (impact, effort, fit)"
      show-when: "mode is feature or revamp and the feedback is mostly requests"
---

# Feedback mining

Turn a pile of real feedback into a short list of themes the PM can trust. Every theme points back to its sources.

## Before you start
- Read STATE.md and the brief's TL;DR (new mode) or current-product.md (revamp or feature mode).
- Check that network access to the sources works. If it's blocked, stop and tell the user what to allow. Never invent or simulate feedback.

## Steps
1. **List the sources** with their access method, time window and expected volume. **Checkpoint:** the user approves the sources and window.
2. **Pull and save** the raw items to `raw/` as JSON or markdown. Keep the URL, date and author role for each item. Record the actual counts in `sources.md`.
3. **Check volume.** If there are too few items to see patterns (under ~30), say so. Suggest widening the window or adding sources, or go back to Frame.
4. **Cluster** the items into themes. Each theme gets a one-line name, a count, a sentiment, the strongest quote and 2 or 3 source links. If insights.md already exists (from interviews), merge into it instead of replacing it.
5. **Find trends** if dates allow: new this period, growing or fading. In revamp or feature mode, compare before and after the last release.
6. **Spot-check** 10 random theme assignments against the raw items. Report the error rate. If more than 2 are wrong, recluster.
7. **Write** `insights.md` and update STATE.md.

## Optional (one-liners)
- In feature or revamp mode with mostly requests: score requests on impact, effort and strategic fit.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "The network is blocked, I'll use sample data" | Fake data gives fake insights. Ask the user to allow access. |
| "Clustering looks right, skip the spot-check" | LLM clusters drift quietly. Ten checks take two minutes. |
| "Theme counts don't matter" | Without counts, the loudest anecdote wins. |

## Done when
- [ ] sources.md shows real counts and the time window
- [ ] Every theme has a count and at least 2 source links
- [ ] Spot-check error rate is reported
- [ ] STATE.md is updated

## Output format (insights.md, shared with interview)
```
## TL;DR
<5 lines max>

## Themes
| Theme | Count | Trend | Sentiment | Strongest quote | Sources |
## Surprises
## Data caveats (volume, window, spot-check error rate, or interview count)
## Open questions
```
