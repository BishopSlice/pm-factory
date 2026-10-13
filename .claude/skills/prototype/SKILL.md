---
name: prototype
description: "Builds a working, clickable UI for the main task path from the design brief and spec, using real data where possible, and runs it locally for review. Use in Design after the brief."
metadata:
  stage: 3-design
  modes: [new, revamp, feature, fix]
  menu: "Build a clickable prototype"
  recommend-when: "03-design/brief.md exists and no prototype is recorded in STATE.md"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/03-design/brief.md, projects/<name>/02-define/spec.md]
  writes: [prototype code at the path named in STATE.md, projects/<name>/03-design/prototype.md]
  extras: []
---

# Prototype

Build the main task path for real, not as a static mockup. A prototype someone can click through beats any description.

## Steps
1. In feature or fix mode, change the existing app (or a branch of it) for the changed screens only.
2. **Pick the stack** from the spec's tech notes. If none is given, use the simplest option that fits: one HTML file for a demo, or the app's real stack if this will become the product. **Checkpoint:** the user confirms the stack and where the code lives.
3. **Wire up the tokens first,** then the layout, then components. Components use tokens only.
4. **Build the main task path** end to end, including every state in the brief. For AI output, connect it to the real model or a recorded real response. Label it if it's recorded.
5. **Use real data.** Pull a small real sample. If that isn't possible yet, use a clearly labeled sample shaped like the real data, and note it as a gap.
6. **Run it** and open it in a browser. Check the main path yourself at phone and desktop widths.
7. **Write** `prototype.md`: how to run it, what's real and what's stubbed, and known gaps. Record the code path in STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "A Figma-style mockup is enough" | Static mockups hide state and flow problems. Clickable surfaces them. |
| "Lorem ipsum for now" | Fake text hides layout breaks. Real data shows them early. |
| "It compiles, so it works" | If you haven't clicked through it, it doesn't work. |

## Done when
- [ ] The main task path works end to end in a browser
- [ ] Every state from the brief can be reached
- [ ] Real versus stubbed data is labeled
- [ ] STATE.md recommends design-critique next

## Output format (prototype.md)
```
## TL;DR
<5 lines max>

## How to run
## Real vs stubbed
## Known gaps
```
