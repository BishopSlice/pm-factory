## TL;DR
- Before framing a product around a third-party tool, confirm the tool is still active and supported.

## Lessons
- 2026-10-11, gemini-voc: The project was framed around Gemini CLI, which had been discontinued. It was caught during idea-refine, after the interview. **Rule:** interview-me asks "Is the product or data source still live and maintained?" as part of the constraints question, and landscape-and-sizing checks the last release and activity date.
- 2026-10-11, adk-voc: The gate offered Go/Narrow/Stop only, and "pause for now" was recorded as Stop. **Rule:** every gate offers Pause, which is not a verdict on the idea. Stop asks for a reason.
- 2026-10-13, nextjs-triage: A docs-RAG support agent was framed before checking what the model already knew. Discover's closed-book baseline beat three pre-registered RAG designs (12 vs 11, 13 vs 8, 13 vs 12). **Rule:** before choosing a retrieval-based direction, idea-refine measures closed-book performance on about 20 real items.
- 2026-10-13, nextjs-triage: The reframe into an eval kit overlapped existing frameworks (claude-api build-eval and hillclimb, promptfoo, Langfuse). **Rule:** landscape-and-sizing checks for first-party and open-source tools that already do the core job before a direction is picked, not after.
