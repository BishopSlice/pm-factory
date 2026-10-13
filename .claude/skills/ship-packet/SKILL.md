---
name: ship-packet
description: "Deploys to preview or staging and bundles the evidence for the Build gate: tests, evals, reviews, spec-check, known issues, cost per run and rollback steps. Production waits for the Ship decision. Use at the end of Build."
metadata:
  stage: 4-build
  modes: [new, revamp, feature, fix]
  menu: "Deploy with evidence"
  recommend-when: "spec-check.md exists with no failing criteria"
  model: sonnet
  reads: [projects/<name>/STATE.md, TL;DRs of projects/<name>/04-build/*.md and projects/<name>/04-build/slices/*.md]
  writes: [projects/<name>/04-build/ship-packet.md, preview URL]
  extras: []
---

# Ship packet

Put it on a preview URL, and leave a one-page record that proves it works and explains how to undo it. Production deploy happens only after the user says Ship at the Build gate (the factory router does it).

## Steps
1. **Pre-flight:** all checks green, no secrets in code, environment variables set and documented.
2. **Deploy to preview or staging** with the stack's normal method (e.g. a Vercel preview, a staging branch, or a dry run of a scheduled job). Never deploy to production here. Write the exact production deploy command into the packet.
3. **Smoke test** the preview URL: the main task path plus one AI path. Capture evidence.
4. **Basic monitoring:** error logging is on, and there's a way to see usage and cost per run.
5. **Write the packet** and update STATE.md (Build gate next).

## Don't skip steps
| Excuse | Why not |
|---|---|
| "It worked locally" | Deployed environments differ: env vars, data, limits. Smoke test the preview. |
| "Rollback won't be needed" | It's needed exactly when you didn't plan for it. Write the steps. |

## Done when
- [ ] The preview URL passed a smoke test
- [ ] The production deploy command is written down
- [ ] The packet links all evidence
- [ ] Rollback steps exist

## Output format
```
## TL;DR
<5 lines max>

## Preview URL and version
## Production deploy command
## Production URL (filled in by the router after Ship)
## Evidence (tests, evals vs threshold, reviews, spec-check)
## Known issues and accepted risks
## Cost per run and monitoring
## Rollback steps
```
