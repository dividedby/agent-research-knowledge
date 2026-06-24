# The harness-level loop: who decides when work is done

There are two loops in agentic coding. The **agent loop** is the familiar one
inside every coding agent — call a tool, read the result, edit, run tests, and
eventually say "done." The **harness-level loop** sits *outside* that: when the
model stops, a harness decides whether that was actually the end, and if not it
continues the session, injects a new message, restarts with modified context, or
hands the task to another machine. Work is put on a queue, a machine picks it up,
attempts it, and the harness keeps it alive past the point the model would have
called itself finished. This loop isn't new (Claude Code had versions from the
start), but it is the pattern increasingly being built on top of agents — Pi
included — and Ronacher thinks about it more than he wants to admit.

His position is split by what the loop produces:

- **Where loops already work astonishingly well: disposable or transformable
  output.** Porting (Bun Zig→Rust, his own MiniJinja→Go), performance
  exploration (try, benchmark, discard, keep searching), security scanning, and
  almost any *research* that surfaces findings without committing lasting code.
  What these share: they either **transform code that already exists** or produce
  **artifacts with no long shelf life** (proofs of concept, ideas, findings,
  mechanical translations). The harness doesn't need an objective binary measure
  of success — it just needs *some* signal useful enough to drive another
  iteration, and that signal can come from an LLM-as-judge as readily as a test.
  Ronacher loves loops that take the boring experiment-and-measure parts out of
  his day.

- **Where he resists: lasting code he wants to comprehend.** Hands-off harnesses
  amplify the model's worst instinct — see a local failure, add a local defense
  ([[make-the-bad-state-impossible]]). Each iteration adds another small defense,
  so the system slowly becomes *less* understandable while *appearing* more
  robust; the more hands-off you are, the more this happens, and it teaches
  juniors bad practices they can convincingly defend. A 30-minute uninterrupted
  run produces worse code than the more human-in-the-loop process of last autumn.

The metaphor he reaches for is **software moving from a deterministic machine to
an organism**: a codebase produced, reviewed, patched, and kept alive by loops
becomes something you *treat, monitor, and stabilize* but no longer *comprehend*
— diagnosed like a patient rather than read like a machine. The deeper cost is a
new kind of dependency: such a codebase **assumes machine participation as part
of its maintenance model**, so losing access to the same class of models (cost,
trade restrictions, or just atrophied human understanding) leaves you unable to
maintain your own software.

Crucially, opting out fully may not be possible. **If attackers and AI bug-report
floods loop against your software (curl's "summer of bliss"), defenders must
eventually loop too** just to triage and reproduce; competitively, small teams
that orchestrate machines well will out-build others on raw speed. So the
question isn't *whether* we loop — clearly we will — but how, in a future of
loops, we avoid abdicating judgment: keep a responsible human able to supervise,
jolt the human back into the loop, make loop changes legible long-term, and
re-architect code to retain sanity. This is the harness-design stakes behind
[[you-are-the-bottleneck]] and the structural reason the
[[slop-loops-and-agent-psychosis]] failure mode matters at scale.

## Sources
- `sources/ronacher/blog/https-lucumr.pocoo.org-2026-6-23-the-coming-loop-387584b7.md` — origin: https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
