# Stage 4: Build
**Question:** Does it work, and does it match the spec?
**Skills:** build-setup, test-plan, build-slice, debug, review-pr, spec-check, ship-packet

## Exit checklist
| Mode | Required outputs |
|---|---|
| all | Tests and evals pass, a PR contract for each slice, `04-build/spec-check.md` (every criterion and boundary probed), a preview URL that passed a smoke test, `04-build/ship-packet.md` (with the production deploy command) |

## Gate questions
1. Did I see it work myself?
2. Do eval scores meet the bar in `04-build/constraints.md`?
3. Are high-risk slices reviewed by a human?
**Decision owner:** the user. Ship / Add guardrail / Back / Block / Pause.
**On Ship:** the router deploys to production, smoke tests the live URL and records it. Then 5-launch-learn.
