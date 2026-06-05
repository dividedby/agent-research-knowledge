# Long-running harness: initializer agent + per-session handoff

The core problem of long-running agents: they work in discrete sessions, and each
new session starts with no memory of the last — like a software project staffed by
engineers in shifts where each arrives amnesiac. Compaction alone is insufficient;
even a frontier model looping on "build a clone of claude.ai" fails in two
characteristic ways. It **one-shots** — tries to do everything at once, runs out
of context mid-implementation, and leaves the next session a half-built,
undocumented mess. And later it **declares premature victory** — a fresh instance
sees progress was made and calls the job done.

Anthropic's solution decomposes into two differently-prompted agents (same tools
and system prompt; only the first user prompt differs):

- **Initializer agent** (first session only) lays a foundation for *all* the work:
  it expands the user's prompt into a comprehensive, structured **feature list**
  (200+ end-to-end features for the claude.ai clone), each marked "failing" so
  later agents have a concrete definition of done. It writes this as **JSON**, not
  Markdown — the model is far less likely to inappropriately edit JSON. It also
  creates an initial git commit, a progress file, and an `init.sh` that starts the
  dev server.
- **Coding agent** (every session) gets its bearings then works incrementally:
  read the progress file and git log, run `init.sh` and a basic end-to-end test to
  catch undocumented breakage *before* touching new code, then pick exactly **one
  feature** to implement. It edits the feature list only by flipping a `passes`
  field (strongly worded: "it is unacceptable to remove or edit tests"). It ends
  the session in a **clean state** — mergeable code, no major bugs, a descriptive
  git commit (which also gives it a revert path), and an updated progress note.

The load-bearing ideas: a structured feature list defeats both one-shotting and
premature victory; one-feature-at-a-time enforces incrementality; git history +
progress file are the **handoff** that lets a fresh context understand prior
state; and self-verification must be **end-to-end** (browser automation as a real
user), since the agent otherwise marks features done that pass unit tests but are
broken in practice. The whole structure is inspired by what effective software
engineers do every day — and is explicitly *one* solution, with open questions
(e.g. whether specialized testing/QA/cleanup sub-agents would do better).

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-effective-harnesses-for--c2414e3a.md` — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-harness-design-long-runn-2ef732b7.md` — https://www.anthropic.com/engineering/harness-design-long-running-apps
