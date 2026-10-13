---
name: launch-plan
description: "Plans a launch on free channels: positioning, one core message, where the target users already are, release notes and a launch-day checklist. Use in Launch & Learn after the product ships."
metadata:
  stage: 5-launch-learn
  modes: [new, revamp, feature]
  menu: "Plan the launch"
  recommend-when: "the Build gate verdict is Ship (production URL in ship-packet.md) and 05-launch/plan.md does not exist"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/04-build/ship-packet.md, projects/<name>/02-define/spec.md (PM layer), optional if they exist: 00-frame/brief.md, 00-frame/landscape.md, 01-discover/segments.md, 01-discover/current-product.md]
  writes: [projects/<name>/05-launch/plan.md]
  extras:
    - label: "Product name ideas"
      show-when: "the product has no final name"
    - label: "Pricing check"
      show-when: "the product will charge money"
---

# Launch plan

Get the product in front of the people it was built for, using channels they already use.

## Mode switch
| Mode | What changes |
|---|---|
| new | Full plan |
| revamp | Lead with what changed and why. Plan how to tell existing users. |
| feature | Release notes plus in-product announcement. One or two channels. |

## Steps
1. **Positioning in one line:** for <segment>, <product> is the <category> that <key benefit>, unlike <alternative>. Use the vision line and landscape if they exist (new mode). Otherwise use the spec's problem and user, and current-product.md.
2. **One core message** and 3 proof points, each backed by evidence from the ship packet (eval score, demo, real output).
3. **Channels:** where the primary segment (from segments.md, or the spec's user if there is none) already is (communities, forums, GitHub, newsletters, your network). Pick 2 or 3. For each, give the format, timing and owner. **Checkpoint:** the user picks the channels.
4. **Assets:** a demo (gif or video), a short post per channel, release notes, and a README or landing section.
5. **Launch-day checklist:** monitoring on, a feedback route ready, a way to answer questions within hours.
6. **Write** `plan.md` and update STATE.md.

## Optional (one-liners)
- If there's no final name, brainstorm 5 names with reasons.
- If it will charge money, check pricing against alternatives and willingness to pay.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "Post everywhere" | Spread thin gets ignored. Go deep where your users are. |
| "Good products sell themselves" | Nobody finds a product with no launch. |

## Done when
- [ ] Positioning and message are backed by evidence
- [ ] 2 or 3 channels with ready assets
- [ ] The launch-day checklist is complete
