# Git-backed memory turns a forgetful agent into one that stops repeating itself

A coding agent's biggest limitation often isn't capability — it's that every
session starts from zero. Durable, git-backed memory of past
mistakes-and-fixes is what turns a capable-but-forgetful agent into one that
stops re-discovering the same pitfall every time it's encountered, no matter
how many times a human already corrected it in an earlier session: without
persisted memory, the correction never compounds.

`pi-self-learning` (a memory extension for mariozechner's `pi` harness,
built by Matteo Collina) implements this as a three-tier compaction rather
than one flat, ever-growing log: after each completed agent task it extracts
what went wrong and how it was fixed into a dated daily markdown file, rolls
those into monthly summaries, and promotes only the top-ranked, most
frequent-and-recent lessons into a small always-loaded core file
(`core/CORE.md`). That tiering is what keeps the memory actually injected
into every turn small even as the underlying history keeps growing — the
agent doesn't have to read its entire past to benefit from it. The whole
memory folder is its own git repository, so the learning history is
versioned and auditable like any other artifact, not a black box. How much
that memory visibly steers the agent is itself configurable per session or
branch (inject only the ranked core, add recent monthly summaries, or make
consulting memory strict/advisory/off) — the design treats "how much should
memory be trusted right now" as a dial, not a fixed default.

## Sources

- `sources/collina/newsletter/https-adventures.nodeland.dev-archive-your-coding-agent-keep-ade1c144.md` — origin: https://adventures.nodeland.dev/archive/your-coding-agent-keeps-making-the-same-mistakes/
