# How far you step back from the code is a contextual judgement, not an identity

"Should developers still look at the code?" is becoming one of the most divisive
questions in agentic development, and people are answering it as a *personality
trait* — declaring themselves AI-sceptic Real Developers who check every diff, or
agentic-maximalists directing fleets from on high and pitying the manual-edit
luddites. Both camps mistake a contextual judgement for a moral position.

The better framing isn't binary (look / don't look, hand-edit / only direct).
It's a dial: **how close should the code be, how easy to access, how often do you
expect to edit by hand** — and the right setting moves with the situation, not
with what you believe about AI. The factors that set the dial:

- **Domain and language.** Natural language is a poor medium for designing easing
  curves and aesthetic feel — front-end/CSS work often needs a hand on the code,
  while pass/fail CLI tooling is easy to validate at a distance. Model competence
  also varies wildly by language (React/Tailwind far better than Rust/Haskell).
- **Feedback loops and definitions of success.** The more an agent can validate
  its own work — run tests, open a browser, screenshot, click around — the
  further you can step back. Loop-until-green tooling leans into this; it breaks
  down for fuzzy, taste-driven work an agent can't "see."
- **Risk tolerance.** A broken blog image is recoverable; a drug-dosage or
  money-moving bug is not. Consequences scale fast, and regulated/compliance
  contexts *require* humans who read and verify the code.
- **Greenfield vs. brownfield.** Fresh projects tolerate agent-made architectural
  decisions (cheap to throw out); existing codebases with years of implicit
  conventions need tight supervision or agents contradict the three other ways
  the codebase already solves the same problem.
- **Number of collaborators.** Solo, you can YOLO. On a team you must agree on
  standards and agent rules (AGENTS.md, MCPs, commands, skills), and a sane review
  pipeline — or you arrive to find one agent renamed the schema while another
  refactored the API.
- **Experience level.** Seniors prompt, debug, and set guardrails better because
  they carry a catalogue of failures ("that's a memory leak," "that'll deadlock
  under load"); newer developers more easily prompt a house of cards that passes
  tests and falls over in production.

The trajectory: today, code-must-be-close for most serious professional work; but
the dial shifts toward code-at-a-distance as **harnesses mature** — and the
infrastructure matters far more than model improvement. Validation loops, tests,
and specialised subagents for security, debugging, and code quality are what make
hands-off feasible (e.g. agentic CI/CD workflows that fire a security-review,
accessibility-audit, and docs-updater agent on every commit). Safe guards and
quality gates, not raw model capability, are what let you step back.

## Sources

- `sources/maggieappleton/blog/https-maggieappleton.com-gastown-31a465e3.md` — origin: https://maggieappleton.com/gastown/
