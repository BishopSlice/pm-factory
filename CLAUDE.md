# PM Factory

## What this is
A set of Claude Code skills that take a product from a vague idea to a shipped, measured release. Work moves through six stages (Frame, Discover, Define, Design, Build, Launch & Learn). Each stage writes artifacts and ends at a human gate.

## Layout
- `.claude/skills/`: the factory skills. `factory` is the router; the rest are stage steps.
- `stages/`: one file per stage with its skills, exit checklist and gate questions.
- `templates/`: STATE.md and skill templates. `learnings/`: lessons promoted from past projects.
- `projects/<name>/`: one folder per project, with STATE.md as the handoff file (not in git).

## How to work
- Always sound human. Never use em dashes. Prefer short, crisp sentences over prose.
- Discuss the plan before executing anything big. The user owns every gate decision.
- Read only the files STATE.md names for the next stage.

## Token habits
- Use Haiku/Sonnet subagents for reading and summarizing. Save Opus for judgment calls.
- Read excerpts, not whole repos. Summarize into files so we don't re-read.
