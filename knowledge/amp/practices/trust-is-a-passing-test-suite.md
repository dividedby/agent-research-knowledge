# Trust is a passing test suite

Agents are most powerful when they can validate their work against reality —
when they have **feedback loops**. State-of-the-art models often write working
code in one try, but on real projects they still need feedback to iterate and
converge on a solution that satisfies all the project's constraints. Only by
running external tools — the type checker, the test suite, the compiler — can the
model learn what it got wrong. "Trust isn't a feeling, it's a passing test
suite."

So don't just ask for the feature. Give a **definition of done**, then engineer
the feedback loop *into the prompt itself*:

- Point at a reference to follow (`Follow the pattern in src/api/messages.ts`).
- Give it a way to check its own work and a stopping condition (`Run the API
  tests after each step. Don't move on until they pass.` / `Use Chrome devtools
  to check dark mode … toggle back to light and check that too.`).
- With a loop wired in, you can step away and let the agent iterate until green.
  The win is not that the model "got smarter" — it's that you built a better
  environment for it to succeed in.

Corollary — **don't take feedback tools away.** Restricting the agent (hiding
files, blocking reads) just makes it look for workarounds (e.g. reading the file
via Bash instead), wasting tokens and giving only a false sense of security.
Letting it run tests and see results is the whole point.

This reframes the human's role: high-level validation and feedback (review the
*results*, craft the vision) while the agent does the work and validates to your
specification. You verify the outcome; the test suite verifies the code.

Not every definition of done is a test suite. For work a type-checker can't
assert — visual, behavioral, "does this actually work end to end" — ask
explicitly for proof in whatever form fits: a screenshot, a table of
before/after screenshots, a demo video, a full matrix of test cases run and
shown, not just claimed. The proof format changes; the principle doesn't — you
still review evidence, not raw diffs, which is what makes it tractable to let an
agent run long and unsupervised (many minutes, hundreds of lines) without
babysitting it.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-permissions-b6eba13f.md` — origin: https://ampcode.com/notes/permissions
- `sources/amp/chronicle/https-ampcode.com-notes-how-to-pair-with-an-agent-450a7fb3.md` — origin: https://ampcode.com/notes/how-to-pair-with-an-agent
- `sources/amp/chronicle/https-ampcode.com-notes-feedback-loopable-a35615e9.md` — origin: https://ampcode.com/notes/feedback-loopable
- `sources/amp/chronicle/https-ampcode.com-notes-what-i-want-to-tell-you-about-orbs-dc428f37.md` — origin: https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs
