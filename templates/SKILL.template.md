---
name: <kebab-case-name>
description: "<What it does in one sentence>. Use when <trigger situations>. <Under 250 characters. This line costs tokens in every message, so keep it tight. Quote it, since colons break YAML.>"
metadata:
  stage: <0-frame | 1-discover | 2-define | 3-design | 4-build | 5-launch-learn | communicate>
  modes: [new, revamp, feature, fix]   # which entry modes use this skill
  menu: "<Short label the router shows, e.g. 'Mine public feedback'>"
  recommend-when: "<One rule, e.g. 'STATE.md has no 01-discover/feedback.md and public feedback exists'>"
  model: <haiku | sonnet | opus>
  reads: [<project>/STATE.md, <exact input paths>]
  writes: [<exact output paths>]
  extras:   # optional one-liners the router may show under "Extras"
    - label: "<e.g. Add a SWOT>"
      show-when: "<e.g. user mentions stakeholders or an exec review>"
---

# <Skill name>

<One sentence: the job this skill does and why it matters.>

## Before you start
- Read `STATE.md` first. Then read only the files listed in `reads`.
- If an input is missing, ask for it or run in "<fallback>" mode. Never search the repo.
- Check `lessons.md` and `learnings/` for rules that apply to this stage.

## Mode switch
| Mode | What changes |
|---|---|
| new | <...> |
| revamp | <...> |
| feature | <...> |
| fix | <...> |
<Delete rows for modes this skill doesn't support.>

## Steps
1. <Verb-first step.> **Checkpoint:** <what the user confirms before moving on>
2. <...>
3. <...>
Keep it to 7 steps or fewer. Each step is an action, not an essay.

## Optional (one-liners)
- <e.g. "If stakeholders expect it, add a SWOT.">

## Don't skip steps
| Excuse | Why not |
|---|---|
| "<e.g. The idea is obvious, skip research>" | <e.g. Obvious ideas are where wrong assumptions hide.> |

## Done when (evidence)
- [ ] <A concrete, checkable outcome, e.g. "Every claim links to a source">
- [ ] Output starts with a TL;DR of 5 lines or fewer
- [ ] `STATE.md` is updated: stage, files written, next recommended step

## Output format
Write to `<path>`:
```
## TL;DR
<5 lines max>

## <Sections...>
```
