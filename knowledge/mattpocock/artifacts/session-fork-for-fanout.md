# Session fork: a fan-out sibling of resume that isolates only the conversation

Sandcastle's `.resume()` continues an agent's captured session by mutating it
forward — one linear thread. `RunResult.fork(prompt, options?)` is its sibling for
**fan-out**: it also continues from the last captured session and runs exactly one
iteration, but it leaves the parent session JSONL untouched and writes the child
under a fresh session id. The mechanism is the agent CLI's own fork flag —
`claude --resume <id> --fork-session` for Claude Code, `codex exec fork <id>` for
Codex — so a single expensive parent run (read the codebase, build the data model)
becomes the shared starting point for several independent children that each take
the context in a different direction.

## Fork isolates the session, nothing else

The sharp caveat — and the reason this earns its own concept rather than reading as
"resume but parallel" — is that fork isolates *only the agent session JSONL*. It
does **not** isolate the branch, worktree, or sandbox. So safe concurrent fan-out
(`Promise.all([r.fork(a), r.fork(b)])`) is the caller's responsibility: each child
must be handed a distinct branch via `branchStrategy: { type: "branch", branch }`.
The default strategies are explicitly unsafe under concurrency — `head` shares the
host working directory across all children, and `merge-to-head` races `git merge`
against the same HEAD. (Relatedly, the temp-branch name generator gained a random
suffix because its second-granularity timestamp collided whenever two runs started
in the same second.)

This is the thin-harness line again ([[thin-fail-fast-harness]]): the harness
exposes the fan-out primitive and the constraint, and leaves the orchestration
(give each fork its own branch, collect the results) to the consumer. Like
`.resume()`, `fork` is present only on results from providers that supply
`sessionStorage` (Claude Code, Codex) — hence the optional-chaining call — and the
same single-iteration and session-file-must-exist constraints apply.

## Resume and fork inside a warm sandbox amortize container boot across phases

Both primitives later gained a second home: `sandbox.run()` (from
`createSandbox()`) exposes `.resume(prompt, options?)` and `.fork(prompt, options?)`
on its result, continuing the agent session *inside the same long-lived container*.
The payoff is purely operational but sharp — a multi-phase loop (implement → review
→ edit) keeps the container, the worktree, and the on-ready dependencies **warm**
across phases instead of each phase paying container boot. The conversation thread
continues exactly as the top-level `.resume()`/`.fork()` do; what's reused is the
expensive surrounding environment, which the top-level entry points tear down per
run. This rests on a session-capture fix in the same release: bind-mount providers
were silently dropping the handle that the capture gate keys on, so `.resume()`
inside a created sandbox had nothing to resume from; non-bind-mount (isolated,
no-sandbox) providers skip capture and so still have nothing to resume.

## Sources

- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: github.com/mattpocock/sandcastle (CHANGELOG.md)
- `sources/mattpocock/sandcastle/README.md.md` — origin: github.com/mattpocock/sandcastle (README.md)
- `sources/mattpocock/sandcastle/src-createSandbox.ts-9b83cab1.md` — origin: github.com/mattpocock/sandcastle (src/createSandbox.ts)
