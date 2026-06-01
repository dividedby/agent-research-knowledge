# Context-efficient backpressure

An agent's chance of success correlates strongly with its ability to **verify its
own work** — typechecks, builds, unit and integration tests, coverage, UI checks.
That verification loop is the backpressure that keeps an agent honest. But naive
verification poisons the very context it's meant to protect: a passing pytest or jest
run can emit 200+ lines to say "everything's fine," and 4,000 lines of passing tests
floods the window and makes the agent lose the thread.

So the rule is **surface only what matters, swallow the rest**: on success print a
single `✓`; on failure dump the full output. The signal the agent needs from a
passing suite is one bit — it passed — and you should spend exactly one bit of
context on it.

A minimal wrapper captures the whole idea:

```bash
run_silent() {
    local description="$1"; local command="$2"
    local tmp_file=$(mktemp)
    if eval "$command" > "$tmp_file" 2>&1; then
        printf "  ✓ %s\n" "$description"; rm -f "$tmp_file"; return 0
    else
        local exit_code=$?
        printf "  ✗ %s\n" "$description"; cat "$tmp_file"; rm -f "$tmp_file"; return $exit_code
    fi
}
```

Refinements all serve the same goal — fail fast so the agent fixes one thing at a
time (`pytest -x`, `jest --bail`, `go test -failfast`), strip generic stack frames
and timing noise, parse out test counts. The deeper move is **determinism over
delegation**: if *you already know* what matters in the output, don't make the model
churn thousands of junk tokens to decide. Format it yourself.

There's a failure mode in the other direction. Recent models, trying to be frugal
with context, over-correct: piping to `/dev/null` on exit code (which can cost *more*
tokens than just showing the relevant lines), or truncating with `... | head -n 50`
which silently drops the failure and forces a full, expensive re-run. The principle
isn't "minimize output" — it's "show exactly the relevant output, deterministically."

Why it's worth the effort: every token spent moves you closer to a clear/compact, and
**human time managing a context-starved agent is far more expensive than the tokens
saved**. A `Stop` hook that runs the verification silently and surfaces only errors
turns backpressure into a deterministic part of the loop rather than something the
agent has to remember to do (see *harness-engineering* and *claude-md-is-not-a-linter*).

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-context-efficient-backpressure-38259122.md`
  — origin: https://www.humanlayer.dev/blog/context-efficient-backpressure
- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-skill-issue-harness-engineerin-313aa20b.md`
  — origin: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
