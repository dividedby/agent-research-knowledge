# The markdown driver file: rules + WIP log

When antirez runs an agent unattended on a real project, the load-bearing artifact
is a single **markdown file** that drives the session. It is not the spec (which
carries the design); it is the *operating manual* the agent reads, follows, and
keeps updating. Its structure recurs across his projects and is worth copying.

A driver file pairs two parts:

**1. The rules block** — how to do the work, as standing constraints. From the
Z80/Spectrum build, verbatim in spirit:

- *Provenance:* "Accessing the internet is prohibited, but you can use the spec
  and test vectors in `./z80-specs`." (Clean-room: information sources are fenced.)
- *Quality:* "Code should be simple and clean, never over-complicate things";
  "very well commented — understandable even by people not versed in the
  internals."
- *Cadence:* "Each solid progress should be committed to git"; "before committing,
  test that what you produced is high quality and works"; "write a detailed test
  suite as you add features, re-execute it at every major change."
- *Autonomy:* "Never stop for prompting, the user is away from the keyboard."

**2. The work-in-progress log** — the file instructs the agent to *maintain a log
inside the same file*: "create a WIP log where you note what you already did and
what is missing; always update this log." And critically: **"Read this file again
after each context compaction."** This is the explicit countermeasure to the
agent's forgetting across compactions — the durable state of the task lives in the
file, not only in the window, and the agent is told to re-anchor on it.

The same artifact shape generalizes to other roles. His **QA driver file** (see
practices/agentic-qa-gate) is the same pattern aimed at testing: standing context
at the top (SSH endpoints, keys, paths), the agent told to diff against the last
release first, then a checklist of outcome-level checks. In both cases the file is
deliberately *thin on rote instruction and rich on standing context and rules*,
letting the agent figure out specifics (the speed baseline, the implementation)
itself.

Design principle behind the whole artifact: **"think in terms of what a human
would need,"** plus a few LLM-specific additions — the compaction re-read, the
no-stop-for-prompting autonomy clause, and the continuous self-verification
cadence. A separate session can even *generate* the supporting documentation the
driver file points to (the agent fetches and distills docs into markdown, which is
then committed and fed to a fresh implementation session).

## Sources

- `sources/antirez/blog/http-antirez.com-news-160-3eec660b.md` — origin `http://antirez.com/news/160` (the Z80 markdown rules file: rules block, WIP log, "read this file again after each context compaction", "never stop for prompting")
- `sources/antirez/blog/http-antirez.com-news-168-81001b41.md` — origin `http://antirez.com/news/168` (the QA-engineer markdown file: standing context, diff-against-last-release, outcome-level checklist)
