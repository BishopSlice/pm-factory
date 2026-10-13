---
name: factory
description: "PM factory router. Starts or resumes a project, detects its mode and stage, and offers the next steps as a menu. Use when the user types /factory, wants to start or resume a factory project, or asks \"what next?\"."
metadata:
  stage: router
  modes: [new, revamp, feature, fix]
  menu: "Start or resume a project"
  model: sonnet
  reads: [.factory/active, projects/<name>/STATE.md, stages/<current-stage>.md, the next stage's exit checklist when gating]
  writes: [.factory/active, projects/<name>/STATE.md, projects/<name>/01-discover/current-product.md (revamp and feature start), projects/<name>/04-build/ship-packet.md (production URL after Ship)]
---

# Factory router

Find out where a project stands, then offer the right next steps. Never run a stage skill without the user picking it.

## Commands
- `/factory` resumes the active project or starts a new one.
- `/factory new <name>` starts a project.
- `/factory switch <name>` changes the active project.
- `/factory run <skill>` runs one skill on the active project.
- `/factory gate` closes the current stage.
- `/factory skip <stage> because <reason>` jumps ahead and logs the reason.

## Steps
1. **Load the project.** Read `.factory/active`, then `projects/<name>/STATE.md`. Read nothing else yet.
   - No project yet: ask for a short name, create `projects/<name>/`, and copy `templates/STATE.template.md` to `STATE.md`. Write the name to `.factory/active`.
2. **Set the mode** if STATE.md has none. Ask one question with 4 options:
   new product / revamp / new feature / fix or iterate.
   - Mode paths (Go moves along these):
     - new: 0-frame, 1-discover, 2-define, 3-design, 4-build, 5-launch-learn
     - revamp: 1-discover, 2-define, 3-design, 4-build, 5-launch-learn
     - feature: 1-discover (quick assumptions check only, about 15 min), 2-define, 3-design, 4-build, 5-launch-learn
     - fix: 5-launch-learn (learn-readout), 2-define, 3-design (only if the fix changes the UI), 4-build, 5-launch-learn
   - Revamp or feature: write `01-discover/current-product.md` before anything else. Ask, one at a time: what the product does, who uses it, the main metric today, known issues, links to docs or analytics, and the code path. Mark unknowns as unknown. Discover and Define skills read it in place of `00-frame/brief.md`.
3. **Read the stage file** `stages/<current-stage>.md`, and only that one.
4. **Build the menu.**
   - Steps: for each skill listed in the stage file, read only its frontmatter. Keep skills whose `modes` include this mode. Mark the one whose `recommend-when` matches as **(recommended)**.
   - Extras: add any `extras` whose `show-when` matches what you know about the project.
   - When every file in the stage's exit checklist exists, add **"Close this stage (run the gate)"** as the recommended option.
5. **Ask.** Show the menu as numbered options (AskUserQuestion when available). Wait for the user's choice. Never auto-run.
6. **Hand off.** Invoke the chosen skill. When it finishes, return to step 4.

## The gate (`/factory gate`)
1. Check the exit checklist. List anything missing.
2. Read the TL;DR of each output, not the full files.
3. Answer each gate question from the stage file with evidence and a file reference.
4. Give a recommendation and say why in 2 lines or fewer.
5. **The user decides.** Record the decision, date and owner in STATE.md and append it to the log.
   - Go: move to the next stage in this mode's path and update "Files for the next stage".
   - Ship (Build gate only): show the exact production deploy command from ship-packet.md. **Checkpoint:** the user confirms right before it runs. Smoke test the live URL (main path plus one AI path), write the production URL into ship-packet.md and STATE.md, then move to 5-launch-learn. If the smoke test fails, roll back with the packet's steps and record Back.
   - Add guardrail / Block (Build gate only): stay in Build and note what to fix.
   - Narrow: stay, and note the new scope.
   - Back: set the earlier stage and note what to fix.
   - Stop: mark the project parked and ask for a one-line reason. Append it to `learnings/<stage it stopped at>.md`.
   - Pause: keep everything as is, note why and when to resume. Not a verdict on the idea.
   - Iterate (Launch & Learn gate): archive this cycle. Move the stage folders `00-frame/` to `05-launch/` into `cycles/<nn>/`, keeping `STATE.md`, `lessons.md` and `activity.log` in place. Copy the readout's iteration focus into a new `02-define/intake.md`, then set the stage to 2-define.

## Closing a fix
A fix is closed only when both are true: the regression test passes in production, and the metric that broke recovers in the next learn-readout. Then run a 5-minute mini-retro: lessons only, promoted as usual.

## Don't skip steps
| Excuse | Why not |
|---|---|
| "The next step is obvious, just run it" | The user owns the outer loop. Ask. |
| "I'll read the repo to get context" | STATE.md names the files. Reading more wastes tokens and adds noise. |
| "The checklist is close enough, move on" | Gaps found later cost more. Name what's missing and let the user decide. |

## Done when
- [ ] STATE.md shows the mode, stage, next recommended step and the files for the next stage
- [ ] The user picked the step, or made the gate decision, themselves
