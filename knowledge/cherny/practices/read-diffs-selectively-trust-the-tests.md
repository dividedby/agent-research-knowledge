# Read diffs selectively; trust the tests for the rest

Once the agent writes the code, the reviewer's job shifts from *reading* to
*choosing what to read* — and the choice is a judgment call, not a default. Cherny's
rule: he opens a diff only when it's **touching critical code, or code that's
important to get right**. "I read diffs when it's touching critical code, or code
that's important to get right. I don't write the code." Everything else, he lets
pass on the strength of its verification.

The tool changed to match the habit. `/diff` used to be a one-shot list you closed
after reading; it's now a **persistent, scrollable panel** beside the conversation
that updates live as Claude writes — so reading a diff no longer means switching
windows and losing your place. It's a different job from `/focus`, which suppresses
the inline file-write diffs that otherwise fill the transcript as Claude works;
`/diff` gives you somewhere *to* read changes, `/focus` stops them from appearing
unasked.

The load-bearing example is Claude Code's own terminal-rendering layer. Ink (the
React-for-terminals library that draws the whole interface) has been rewritten by
Claude multiple times — and Cherny, the person who built Claude Code, says "I don't
actually know how this impl works — we treat it as a black box with a ton of
property-based tests and benchmarks. Claude maintains it for us." Property-based
tests assert rules that must hold across many generated inputs rather than a
person's hand-picked cases, so they specify a component's *behavior* without
anyone needing to read its *implementation*.

The transferable rule: **you can hand over a component once its tests specify it
well enough that you never need to read the code** — the tests become the contract,
and writing (and trusting) those tests is the part of the job that doesn't go away.
This is the review-side counterpart to [[verification-is-the-number-one-tip]]
(which is about giving the *agent* a feedback loop so it self-corrects); this is
about what lets the *human* stop reading — a property-based or generated-input test
suite is a stronger trust signal than a person re-reading the diff.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
