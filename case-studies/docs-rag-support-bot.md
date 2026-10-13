# I tested whether docs RAG helps a support bot. Three pre-registered designs said no.

I set out to build a support agent for Next.js that answers developer questions from the official docs. Before writing any product code, the factory's Discover stage made me test the riskiest assumption: that searching the docs makes the answers better. It didn't, and finding that out took one afternoon instead of two weeks of building.

## The setup
Next.js routes questions to GitHub Discussions. Since 2025, 871 of 1,320 Help questions (66%) never got an accepted answer, so the pain is real. I sampled 20 answered questions where the accepted answer was substantive and the docs plausibly covered the topic. The accepted answer, marked by a maintainer or the asker, became the gold.

Every design ran against the same baseline: **closed book**, where the model answers from its own knowledge with no tools. Sonnet wrote the answers. Opus judged each one against the gold, and Sonnet judged it again independently. The two judges agreed on 93 to 95% of verdicts. I wrote the pass rule down before each run, so I couldn't move it afterwards.

## Three designs, three failures
| Design | Closed book | With docs | Pass rule |
|---|---|---|---|
| WebFetch on the live docs site | 12 of 20 | 11 of 20 | Docs at least +3. **Fail** |
| Raw docs files, as they were on the question's date | 13 of 20 | 8 of 20 | Docs at least +3. **Fail** |
| Hybrid: answer, then verify and cite from the docs | 13 of 20 | 12 of 20, citations 9 of 15 supported | No real loss, and 80% of citations supported. **Fail** |

On the 8 questions asked after the model's training cutoff, closed book still won, 7 to 4. So this wasn't memorization. The model is simply good at these questions.

## Why docs made it worse
When told to answer only from the docs, the agent hedged: "I can't confirm that from these docs." The accepted answers solved problems with practical knowledge the docs don't contain, such as where to set environment variables on Vercel, which version to upgrade to, or that a CDN was caching the login page. The hybrid fixed the accuracy loss but not the trust problem. Four in ten of its citations pointed to a related page that didn't say what the answer claimed.

## What I'd tell a team buying a support bot
1. **Measure the floor first.** Run the same questions through the plain model with no retrieval. If you skip this, any RAG setup looks good.
2. **Use real resolved questions as gold, and check the gold.** Only about half of accepted answers made usable gold. A fifth were the asker answering themselves.
3. **Pre-register the pass rule.** I changed the design twice. Writing the rule down first is what kept me from calling a loss a win.
4. **Citations are a feature to measure, not assume.** A cited link that doesn't support the claim is worse than no link.

## Caveats
The sample is small, 20 questions plus 8 after the cutoff. It's one framework, with one agent model and community answers as gold, so this says nothing about products the model has never seen, where docs should matter more. Treat it as a strong signal for well-known developer frameworks, not a law.

*Built with [PM Factory](https://github.com/BishopSlice/pm-factory). The Discover stage's assumptions-to-experiment skill ran these tests.*
