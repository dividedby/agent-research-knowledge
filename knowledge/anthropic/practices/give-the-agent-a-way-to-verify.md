# Give the agent a way to verify its own work

An agent stops when the work *looks* done. Absent a check it can run, "looks
done" is the only signal it has — and the human becomes the verification loop,
catching every mistake by hand. Hand the agent something that returns a
machine-readable pass/fail and the loop closes on its own: the agent does the
work, runs the check, reads the result, and iterates until the check passes.

The check is anything producing a signal the agent can read back in the
conversation: a test suite, a build exit code, a linter, a script that diffs
output against a fixture, a browser screenshot compared against a design. The
prompting move is to bake the criterion into the request ("write `validateEmail`;
example cases: `user@example.com` true, `invalid` false; run the tests after")
rather than leaving the goal implicit. For UI, point the agent at the visual:
have it screenshot the result and list the differences from the target.

Verification scales up to unattended runs through the harness, not just the
prompt. A `/goal` condition re-checked by a separate evaluator after every turn
(if Claude stalls without resolving it, Claude Code eventually stops the run
with the goal still unmet, rather than looping forever); a Stop hook that runs
the check as a deterministic gate and blocks the turn from ending until it
passes (Claude Code overrides such a hook and ends the turn after 8 consecutive
blocks, so the gate can't wedge a run forever either); a second-opinion
subagent that tries to refute the result. The `/goal` and Stop-hook forms are
specifically what let an *unattended* run finish correctly without you. Whatever
the form, have the agent **show evidence** rather than assert success — the test
output, the command and what it returned, a screenshot — since reviewing evidence
is faster than re-running the check yourself and works for sessions you weren't
watching. And it must be **end-to-end**:  agents tend to mark a feature done after
unit tests or `curl` checks pass while the feature is broken from a user's
perspective — giving the agent browser-automation tools to exercise the running
app the way a human would dramatically improves real correctness.

The deepest version of this principle is the **near-perfect verifier**. An agent
left to run autonomously will solve *whatever the verifier actually measures*, so
a weak or gameable check means it confidently solves the wrong problem — and "it
is easy to see tests pass and assume the job is done, when this is rarely the
case." In the autonomous C-compiler build, most engineering effort went not into
the agent but into the test harness: high-quality compiler suites, CI that blocks
regressions, and (when the kernel itself was one indivisible task) GCC as a
known-good oracle to localize which files were broken. The verifier *is* the
work.

The inverse is a named failure pattern — **the trust-then-verify gap**: the agent
produces a plausible-looking implementation that doesn't handle the edge cases,
and absent a check it ships. The rule that falls out: if you can't verify it,
don't ship it.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-code-best-practic-4d249e2a.md` — https://www.anthropic.com/engineering/claude-code-best-practices
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-effective-harnesses-for--c2414e3a.md` — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-building-c-compiler-c62e49f2.md` — https://www.anthropic.com/engineering/building-c-compiler
- `sources/anthropic/best-practices/https-code.claude.com-docs-en-best-practices-fb8dc53b.md` — https://code.claude.com/docs/en/best-practices
