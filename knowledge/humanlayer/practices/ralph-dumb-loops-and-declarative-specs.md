# Ralph: dumb loops work, if the spec is good

The "Ralph Wiggum" technique (Geoff Huntley) is, at its crudest, running an agent in
an infinite shell loop on a fixed prompt:

```
while :; do
   cat PROMPT.md | npx --yes @sourcegraph/amp
done
```

HumanLayer treats it as more than a gag. The core lesson they draw is **"dumb things
can work surprisingly well"** — a hilariously simple loop has shipped real output
(repos overnight, multi-hour standards-based refactors), so don't dismiss the simple
approach before trying it.

But the loop is not the interesting part; the **prompt is.** What separates a Ralph
run that ships from one that produces slop is the quality of `PROMPT.md`, and the
recurring principle is **declarative specifications over imperative instructions** —
describe the desired end-state and standards, not a step-by-step script. "If the
specs are bad, the results will be meh." This is the same leverage point as
*review-research-and-plans-not-code*: the spec is upstream of all the generated code,
so that's where quality is decided.

Two supporting practices fall out of running a context-bound model in a loop:

- **Context-carving over endless looping** — the loop only helps if each iteration
  starts from well-managed context, not an ever-growing window (cf.
  *frequent-intentional-compaction* and *context-is-the-only-lever*).
- **Manageable changesets over massive refactors** — keep each pass small enough to
  stay inside the model's reliable zone (cf. *small-focused-agents*).

So Ralph isn't a counterexample to HumanLayer's context discipline — it's the same
discipline with the orchestration stripped down to a `while` loop, which works
precisely *because* the spec is good and the changesets stay small.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-brief-history-of-ralph-59b22ba6.md`
  — origin: https://www.humanlayer.dev/blog/brief-history-of-ralph
