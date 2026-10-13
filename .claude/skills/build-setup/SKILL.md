---
name: build-setup
description: "Prepares a repo for agent-built code: a short project CLAUDE.md, a README with run and test commands, the quality bar as checks, blocked commands and a lessons file. Use once at the start of Build."
metadata:
  stage: 4-build
  modes: [new, revamp, feature, fix]
  menu: "Set rules and quality bar"
  recommend-when: "04-build/constraints.md does not exist"
  model: sonnet
  reads: [projects/<name>/STATE.md, projects/<name>/02-define/spec.md (tech notes and boundaries), projects/<name>/02-define/tasks.md]
  writes: [<code repo>/CLAUDE.md, <code repo>/README.md, projects/<name>/04-build/constraints.md, projects/<name>/lessons.md]
  extras: []
---

# Build setup

Agents follow the rules they can see and the checks that stop them. Set both up before the first line of code.

## Mode switch
| Mode | What changes |
|---|---|
| new | Create everything |
| revamp, feature, fix | Read the existing repo's CLAUDE.md and checks first. Add to them, don't replace them. |

## Steps
1. **Code location.** Confirm where the code lives (a new repo or a folder) and record it in STATE.md. **Checkpoint:** the user confirms.
2. **Write the code repo's CLAUDE.md**, 30 lines or fewer, like a pilot's checklist:
   - the commands to install, run, test and lint, with full flags
   - the folder structure in 5 lines
   - one real code-style example
   - the spec's Always / Ask first / Never rules, copied over
3. **Write or update the code repo's README.md** with how to install, run and test from a clean checkout. spec-check uses only these commands, so keep them exact.
4. **Set the quality bar** in `constraints.md`: which checks must pass (typecheck, lint, tests, evals), the minimum eval scores (from the spec's outcome targets and eval seeds, agreed with the user), and what counts as high risk.
5. **Make checks automatic** where the stack allows: a test script, and a pre-commit or CI step. Block destructive commands (force push, deleting data, pushing to main) in the project's Claude settings.
6. **Start** `lessons.md` empty, with a header. Every real failure adds one line here (the ratchet).
7. Update STATE.md.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "A long CLAUDE.md is more helpful" | Long instructions get ignored. Short, and every line earned. |
| "We'll add checks later" | Agents lower the bar quietly unless a check stops them. |

## Done when
- [ ] The code repo's CLAUDE.md has run and test commands and the boundaries
- [ ] README.md has install, run and test commands that work from a clean checkout
- [ ] constraints.md lists the required checks and eval thresholds
- [ ] Destructive commands are blocked
- [ ] STATE.md recommends test-plan next
