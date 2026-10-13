# How we do evals (load only when building or running evals)

## Parts of an eval case
- **Input:** a real example: a ticket, a document, a query.
- **Golden:** the expected output, or a rule for grading it. Verified by a human.
- **Slice tags:** categories (e.g. bug, question, feature request) so you can see where it fails.

## The set
- Start with 30 to 50 cases. Grow it from real failures over time.
- Split: about 80% dev (tune on these) and 20% holdout (never tune on these, check before shipping).
- Use real data. Strip personal details.

## Scoring
- Exact or structured output: compare to the golden in code.
- Open-ended output: an LLM judge with a written rubric (1 to 5 per criterion, with an example for each score). Use a different model from the one being tested where possible.
- Calibrate the judge: grade 10 cases yourself and compare. If you agree on fewer than 8, fix the rubric.
- Run each case more than once if outputs vary. Report pass rate and consistency.

## Improving (hill-climbing)
1. Run the baseline on the dev set.
2. Read the failures like bug reports. Group them by slice.
3. Change **one** thing: prompt, retrieval, tools or model.
4. Re-run the same set and compare.
5. Before shipping, run the holdout once. A big gap between dev and holdout means overfitting.

## In production
- Re-score a sample of live outputs weekly with the same rubric (measure-setup does this).
- Every production failure becomes a new eval case (learn-readout does this).
