# Designing a programming language for agents

Ronacher's bet: rather than the existing code corpus cementing today's languages,
the collapsing cost of code will spawn *new* languages designed around how agents
work. Most languages were designed assuming keystrokes are laborious, so they
traded clarity for brevity (e.g. heavy type inference). Agents invert that
calculus — writing more is cheap, but *understanding* code under review matters
more — so the design targets change. You can now measure language design against
facts: how many edits and iterations an agent needs for common tasks.

What agents need, distilled into design properties:

- **Local reasoning / greppability.** Agents work from a few loaded files with
  no spatial map of the codebase; they find things with grep. So: force
  package-name-prefixed references (Go's `context.Context`, not `Context`),
  enforce a one-to-one declaration→import mapping, and *discourage aliasing,
  barrel files, and free re-exports* — agents will even complain about aliases in
  thinking blocks. This is [[shape-the-codebase-for-local-reasoning]] pushed down
  into the language itself.
- **No LSP-split.** Type inference makes meaning depend on a *running* LSP, but a
  lazy agent — or one reading a doc snippet or a single pulled-down file — won't
  run it. A language whose code is legible *without* an LSP gives one unified way
  of working everywhere.
- **Effect markers via formatting.** His proposed fix for implicit context-flow
  (the time, the DB, rng): a function declares `needs { time, rng }`; if it uses
  an effect without declaring it, a lint warning that *auto-formatting fixes* and
  propagates to callers. Then tests can precisely mock side effects from the
  error messages (worked example: a deterministic `time.fixed(...)` / `rng`
  in a test). This addresses the tension flagged in
  [[shape-the-codebase-for-local-reasoning]].
- **Diff stability & uniform tooling.** Avoid significant whitespace (token
  efficiency is poor; agents skip indentation and lean on a formatter) but also
  avoid run-of-closing-brace tokenizer pitfalls (Lisp paren-counting). Prefer
  syntax needing little reformatting, trailing commas, few multi-line constructs;
  good multi-line string handling (agents edit *inside* embedded code strings
  mistaking them for real code — only Zig solves it well). Forbid import cycles,
  keep clear package layout, cache test results (Go) so the agent knows what to
  rebuild/retest.
- **Fewer macros, determinism-by-default.** Macros existed mostly to write less
  code — less of a concern now — and agents struggle with them (generics/comptime
  fare better, being uniform structure). Most languages make flaky tests *easier*
  than non-flaky ones by encouraging indeterminism and poor mocking; the ideal is
  one command that lints+compiles and tells you pass/fail (no TypeScript-style
  "runs despite type errors" gaslighting), with mechanical fixes for as many lint
  failures as possible.

The throughline: agents like local reasoning, want code that "either runs or
doesn't," and you can now *measure* what works because agents, unlike humans,
don't mind being surveyed. He hopes for outsider-art language designers and a
first-principles, fact-based write-up of good language design — newly tractable
because targeting a narrow "make the agent happy" use case no longer requires
building a vast ecosystem first ([[pick-an-agent-legible-language]]).

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-2-9-a-language-for-agents-a8f6e8b9.md — https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/
