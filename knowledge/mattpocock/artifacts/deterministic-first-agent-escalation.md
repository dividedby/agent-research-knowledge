# Try the deterministic tool first; call the agent only for the residual, then verify on disk

`update-branch.ts` — the CI step that keeps a stale PR branch current with
`main` — is built as four gates, and only one of them ever calls an LLM:

1. **No-op check.** If `git merge-base HEAD origin/<base>` already equals the
   base SHA, the branch is already current; write "no push needed" and exit
   before touching anything.
2. **Plain deterministic merge.** Run `git merge --no-edit` first. If it's
   clean, done — the agent is never invoked.
3. **Agent, only for the residual.** Only on actual conflicts does an agent get
   called, scoped to just the PR/branch/base context.
4. **Deterministic verification.** The agent's result is checked with the same
   tools that diagnosed the problem, not trusted on its own report.

## Why gate this way

Git's own merge algorithm resolves the overwhelming majority of "branch fell
behind" cases without needing a model at all; calling an agent unconditionally
would spend cost, latency, and a non-zero failure rate on work a decades-old
deterministic tool already does for free. Reserving the agent for the genuinely
hard residual — real textual conflicts — is the same instinct as the pipeline's
other refusal guards in [[label-driven-agent-ci-pipeline]], applied to *when to
invoke the agent at all* rather than *when to refuse a request*.

## Verify on disk, not on the agent's word

The wrapper doesn't stop at parsing the agent's structured `comment` output —
it re-derives success from git state:

- **HEAD must have moved** (`postSha !== preMergeSha`) — an agent that claims
  to have resolved the conflict but produced no commit is a failure, not a
  no-op.
- **No unresolved conflict markers remain** (`git diff --name-only
  --diff-filter=U` must be empty) — an agent that stopped mid-resolution, or
  wrote around a marker instead of removing it, doesn't get to push.

Both checks fail loud (`failure_reason.txt`), independent of whatever the
agent's own extracted output claims. This is
[[structured-output-with-session-retry]]'s "don't trust, verify" instinct
applied one level up: not just schema-validating what the agent *says* it
did, but re-checking what actually changed on disk before acting on it.

## The general shape

Any CI step that *could* be handed straight to an agent benefits from the same
ordering: cheap no-op check → deterministic tool → agent for the residual only
→ deterministic verification of the agent's result. The agent is the most
expensive, slowest, and least certain option in the chain — it belongs last,
not first.

## Sources

- `sources/mattpocock/course-video-manager/.sandcastle-update-branch-update-branch.ts-77ab77d6.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/update-branch/update-branch.ts (revision 2026-07-25)
