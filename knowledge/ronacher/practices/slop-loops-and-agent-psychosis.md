# The slop loop: agent addiction and the cost of turning off your brain

Ronacher's hype-free counterweight to his own enthusiasm: agents are a huge
productivity boost *and* "massive slop machines if you turn off your brain and
let go completely." Both are true at once. The failure mode he names is a
dopamine loop — the build-build-build high that decouples output from any
external reality check.

The mechanics of how it goes wrong:

- **A parasocial dependence.** He compares memory-equipped agents to His Dark
  Materials dæmons: companions we lean on for validation, painful to be
  separated from. But it's a pseudo-collaboration — entirely driven by you, the
  AI just along for the ride, easily steered to reinforce your own impulses.
- **Building is now cheap; *using and polishing* is not.** "You can just do
  things" — but just because you can, you might not want to. He built piles of
  tools in a sleepless two-month binge that he never actually used.
- **No reality check until an outsider looks.** Inside a hyped-up circle (Discord/X
  builder cults), people ram the agent down the narrowest path toward an
  ill-defined goal with no concern for codebase health, generate "documentation"
  that is itself slop to regain false confidence, and reinforce each other. It
  looks amazing until someone pokes under the hood. (His pointed example: Steve
  Yegge's Beads / Gas Town — 240k lines to manage markdown files, abysmal
  quality, near-impossible to uninstall — as "the complete celebration of slop
  loops.")
- **Brutal review asymmetry.** A PR takes a minute to generate and an hour to
  honestly review. Shipping unreviewed AI code to a maintainer disregards their
  time — and the author, told by their dæmon that it was good, is genuinely
  confused by the rejection.
- **Token economics.** Hands-off "let it run wild" patterns burn tokens at
  staggering rates; Ralph-style restart-from-scratch loops are especially
  wasteful because they forfeit cache reuse. A well-prepared, well-tooled session
  is dramatically cheaper (the MiniJinja→Go port took only 2.2M tokens). And
  current pricing is "almost certainly subsidized" — these patterns may not stay
  viable.

The discipline that keeps delegation ([[yolo-mode-delegate-and-wait]]) from
becoming psychosis is the same accountability line from
[[agent-as-collaborator-you-stay-accountable]]: provide the context, make the
tradeoffs, use your knowledge, and honestly review. Watching someone run their
tenth parallel agent at 3am claiming peak productivity, Ronacher doesn't see
productivity — and wonders how often that someone is himself. The proposed exit
is better tooling for *signaling quality and making AI involvement visible*:
some projects now want the prompts rather than (or alongside) the code, trusting
their own agent run over an opaque human-submitted one.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-1-18-agent-psychosis-5dd86afc.md — https://lucumr.pocoo.org/2026/1/18/agent-psychosis/
