---
name: design-brief
description: "Sets the look, feel and screen list for a product before any UI is built: users, tone, references, design tokens and the states every screen needs. Use at the start of Design."
metadata:
  stage: 3-design
  modes: [new, revamp, feature, fix]
  menu: "Set the look and feel"
  recommend-when: "03-design/brief.md does not exist"
  model: opus
  reads: [projects/<name>/STATE.md, projects/<name>/02-define/spec.md]
  writes: [projects/<name>/03-design/brief.md]
  extras:
    - label: "Derive tokens from a reference image"
      show-when: "the user shares a screenshot or image they like"
---

# Design brief

Decide what it should feel like and what screens exist, so the prototype doesn't default to generic AI-looking UI.

## Mode switch
| Mode | What changes |
|---|---|
| new | Full brief and new tokens |
| revamp | Audit the current UI first: what to keep, change or remove. Keep tokens that work. |
| feature, fix | Reuse the existing tokens. Brief only the new or changed screens. Fix mode reaches Design only if the fix changes the UI. |

## Steps
1. **Users and context.** Who uses it, where (desk, phone, terminal), how often, and in what mood. Pull this from the spec.
2. **Tone in 3 words,** plus one product they'd recognize as a reference and one thing to avoid. **Checkpoint:** the user agrees.
3. **Screen list.** Map every acceptance criterion to a screen or flow. Name the main task path in 3 to 5 steps.
4. **States per screen:** empty, loading, error, success and partial data.
5. **AI states** (if the product has AI output): streaming with Stop, editable draft, sources shown, "the agent is unsure", approval needed (from the spec's Ask first list) and failure with retry.
6. **Tokens:** colors (light and dark), type scale, spacing and radius as named variables. No hard-coded values in components.
7. **Write** `brief.md` and update STATE.md.

## Optional (one-liners)
- If the user shares a reference image, derive tokens from it.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Just make it look clean" | "Clean" produces the same template every time. Name the tone. |
| "States can come later" | Empty and error states are most of what users see in v1. |

## Done when
- [ ] Every acceptance criterion maps to a screen
- [ ] Every screen lists its states (and AI states where relevant)
- [ ] Tokens are defined for both themes
- [ ] STATE.md recommends prototype next

## Output format
```
## TL;DR
<5 lines max>

## Users and context
## Tone, reference, avoid
## Screens and main task path
## States (table: screen, empty, loading, error, success, AI states)
## Tokens
```
