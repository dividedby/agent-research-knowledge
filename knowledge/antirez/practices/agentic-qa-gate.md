# Agentic QA as a release gate

antirez uses coding agents not only to *write* software but as a standing **QA
engineer** that runs the manual, integration, and exploratory testing that human
teams structurally skip. The observation motivating it: covering every line of
code does not cover every *state*; integration tests are hard (timing, setup,
outputs only a human can eyeball); and manual QA passes are expensive, so they get
done rarely or never. LLM agents can close that gap on top of the existing test
suite.

The mechanism is a **markdown file that casts the agent as a QA engineer.** It is
deliberately spare in fixed instructions and rich in standing context:

- The agent is told to first **diff against the last released version** — inspect
  the new commits, identify what they could affect, and specialize the QA pass to
  hunt for regressions those changes might introduce.
- It's given a checklist of things to verify, written as outcomes, not procedures:
  e.g. "check distributed inference works across MacBook A and B, output coherent,
  across all GGUF files"; "make sure this release has no speed regression."
- Crucially, **moving targets are left to the agent.** He does *not* tell it the
  previous expected speed — that changes every release — the agent figures out the
  baseline itself. Integration setup (SSH endpoints, keys, paths) sits at the top
  of the file; the agent does the rest.

He pushes it past pass/fail into the "psychological side of software quality":
asking the agent to flag new features that look surprising, under-documented, or
sloppy from a user's point of view, or to build a realistic application against a
new data type, stand up replication and persistence, and simulate days of
multi-user load looking for anything odd. All things that *needed* to be done by
hand and mostly weren't.

The strategic point: automatic programming trades some code quality for speed, and
**automatic QA is the compensating control** — it can raise the quality bar for
releases precisely in the dimensions that high-speed AI-written code tends to
erode.

## Sources

- `sources/antirez/blog/http-antirez.com-news-168-81001b41.md` — origin `http://antirez.com/news/168` (using an AI agent as a QA engineer: DwarfStar release QA, Redis Arrays load simulation, diff-against-last-release scoping)
