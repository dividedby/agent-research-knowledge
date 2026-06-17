# Shift as much work onto agents as possible — without going too far

The core skill of working with 2026-era coding agents, per Goedecke, is to **move
the maximum amount of work onto agents that you can while still catching their
mistakes** — and most people miss the balance in one of two directions.
Under-utilizers won't let agents investigate bugs or test their own changes, or
won't throw enough small tasks at them. Over-utilizers let agents write the
communications that should be hand-written, or trust them with sweeping changes
that need careful human review.

What changed between 2025 and 2026 is that agents recover from their own mistakes,
so the supervision style flips. Early agents had to be **line-edited as they went**
— you watched the thought process and stepped in to correct. Current agents move
too fast for that and recover most errors themselves, so the discipline is now a
single **editing pass at the end**: start every change by handing the problem to
an agent, then review once. This is what lets him say "yes" to far more low-risk
work than he used to defer or decline.

Where the work goes:

- **Every code change** starts as an agent attempt. Reject fast — a ~30-second snap
  judgement ("eh, not what I was thinking") kills most attempts; only on a
  plausible one does he do a real review. Hard tasks routinely cost five or six
  rejected attempts before one is good enough, or he falls back to doing it by hand.
- **Every bug** gets thrown at a fresh agent session first; agents correctly
  diagnose ~80% of issues alone. But human expertise still wins the hard ones — a
  tricky bug took 14 agent sessions, and he counts it as *his* find because his own
  narrowing of the search space between sessions is what made session #14's problem
  easy. Run your own reproduction and feed disconfirming hints ("no, your theory
  can't be right because of X") in parallel.
- **Testing and setup** are pushed onto agents wholesale: ask the agent to test the
  change and read its log; let it write unit tests unprompted; treat test code as
  cheap and review it with a more generous eye than production code. Annoying local
  config wrangling (a broken nvm, etc.) replaces Googling — the agent runs the
  diagnostic commands itself.

What stays human: **public communication** (PR descriptions, ADRs, issues, Slack)
is hand-written, both because the model over-communicates and buries the core idea,
and because writing it yourself *signals* to reviewers that a human has actually
read the diff — the exception is a trivial two-line PR. **UI work** is not handed
to agents, which aren't sensitive to look-and-feel. And nothing ships that he
hasn't carefully reviewed.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-how-i-use-llms-in-2026-45e571f6.md` — origin: https://seangoedecke.com/how-i-use-llms-in-2026/
