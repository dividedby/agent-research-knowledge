# Steer with a large context and a braindump

The single highest-leverage input antirez gives a model is **context** — and not
just code, but his own thinking dumped into the window. When the goal is to reason
about implementing or fixing something, he loads extensively: papers, large parts
(ideally all) of the target codebase, and a brain dump of his understanding of
what should be done. The braindump deliberately includes:

- **bad solutions that look good**, and *why* they're suboptimal,
- **promising solutions**, even half-formed — the model can often run with a hint
  the human hasn't fully elaborated,
- **clear goals**: the invariants required, and even the *style* the code should
  have.

For technologies the model can't know (a brand-new Redis data type, say), he drops
the README into context so the model can use it at expert level immediately —
"with such a trivial trick, the LLM can use vector sets at expert level." This is
the practical move behind "always provide your agents with design hints and
extensive documentation," and an agent can gather that documentation itself in a
prior session.

The guiding heuristic for *what* to provide is **"think in terms of what a human
would need"** — give the agent the documentation, the test vectors, the design
rationale a new human collaborator would require — plus a few LLM-specific
allowances (it forgets after context compaction; it needs to continuously verify
it's on the right track).

A complementary discipline: **control what the model sees.** In his 2025
hand-in-the-loop period he refused editor-integrated agents and RAG specifically
because they show the model only *part* of the code/context, which "destroys LLM
performance" — he moved code by hand from terminal to the frontier model's web UI
to stay in the loop and guarantee he followed every step. His later embrace of
Claude Code/Codex relaxes the *mechanism* (he now lets agents run), but the
underlying principle is unchanged: the human curates a large, deliberately-shaped
context rather than letting a tool silently decide what the model sees. He also
treats model choice as part of steering — running two frontier models against each
other (Gemini 2.5 Pro, Claude Opus, later GPT-5.x/Codex for systems work) to widen
his own understanding of the design space through their back-and-forth.

## Sources

- `sources/antirez/blog/http-antirez.com-news-154-a6ca24d9.md` — origin `http://antirez.com/news/154` ("provide large context", "use the right LLMs", stay-in-the-loop)
- `sources/antirez/blog/http-antirez.com-news-160-3eec660b.md` — origin `http://antirez.com/news/160` (Z80 experiment: "always provide design hints and extensive documentation"; "what a human would need")
- `sources/antirez/blog/http-antirez.com-news-164-5334e7d1.md` — origin `http://antirez.com/news/164` (pairing on the spec via back-and-forth; switching models for systems work)
