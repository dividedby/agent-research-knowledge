# A session has a trajectory, and so does the codebase it edits

An agent's behavior across a session isn't independent turn to turn — it has a
**trajectory**: habits it picks up early tend to persist. If it verifies a
change by cURL once, it will likely reach for cURL again on the next request in
the same session, whether or not that's still the right check. Matt picks the
term up from Dex Horthy (in an interview with Gergely Orosz) and extends it
with his own case: a personal podcast he generates from his own feed, whose
script has every past episode's transcript available as retained state.
Because that state persists across runs, the generator has picked up its own
recurring catchphrases and a bad habit — over-focusing on meaningless
engagement metrics ("wow, 400 bookmarks on this post!"). The podcast, in his
words, "is on a bad trajectory."

## Why this generalizes past one session

The scarier extension is that codebases have trajectories too. A codebase is
stateful — it accumulates whatever agents leave behind across sessions
(comments, patterns, conventions, code shape) — so it has a trajectory the
same way a single conversation does, and "most trend down": left unmanaged, a
codebase run through repeated agent sessions drifts the same way an
unmanaged conversation does, just on a longer timescale and less reversibly,
because the drift lives in committed files, not a discardable context window.

## The fix is steering plus environment, not more of the same session

Matt's stated fix has two parts, matched to the two places trajectory lives:
within one session, clearing context is sometimes the only way to break a
mid-session habit once it's set (see [[keep-the-agent-in-the-smart-zone]]);
for the codebase itself, "the only way to fix a bad trajectory is with better
steering, and by changing the environment the agent works in" — not just
re-prompting, but altering the constraints (hooks, deep-module boundaries,
feedback loops) that shape what the agent does by default.

## Ralph loops externalize trajectory, they don't remove it

Responding directly to Horthy's point that "loops, esp ralph style fresh
context loops, move all trajectory concerns from the context window into the
codebase and otherwise externalized context," Matt agrees and sharpens it:
"Exactly, they don't remove them." Fresh-context-per-iteration loops (see
[[autonomous-loops-ralph]]) don't eliminate trajectory as a concern — they
relocate where it accumulates, from the ephemeral, clearable context window
into durable, git-tracked state (the progress file, the codebase itself).
That's a trade, not a fix: it buys a context window that never picks up a bad
in-session habit, at the cost of needing the same steering discipline
(feedback loops, explicit scope, deep-module design) applied to the artifacts
the loop leaves behind — because that's now where the trajectory lives.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085063640470974489-48a041f3.md` — origin: https://x.com/mattpocockuk/status/2085063640470974489
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085064031203708952-e18ccebb.md` — origin: https://x.com/mattpocockuk/status/2085064031203708952
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2085085591067132382-4da27709.md` — origin: https://x.com/mattpocockuk/status/2085085591067132382
