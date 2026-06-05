# Make it feedback-loopable

A design discipline for shaping an *environment* so an agent can validate its own
work. The digital world is built for humans — pixels, buttons, dynamic
animations, visual dev tools (Chrome inspector, React devtools) — none of which
an agent can use without torturous workarounds. Agents want **text** (and, in a
pinch, an image). Making a problem "feedback-loopable" means turning it into a
format the agent can perceive and giving it that data as fast as possible. It is
*not* about controlling what the agent sees or feeding it answers — it's about
setting up the environment and getting out of the way.

The three moves (from debugging a dynamic physics simulation an agent couldn't
"see"):

- **Build a playground.** An environment both human and agent can poke, stretch,
  and break to find edges in a controlled way. Turn the un-seeable into the
  seeable: the moving animation was repackaged as a *static* simulation the agent
  could screenshot and reason about, with fixes carrying back to the live system.
- **Set up experiments.** Make state reproducible and shareable. Encoding the
  simulation's starting state in **URL query parameters** (`?vx=-6.31&vy=4.91`)
  gave deterministic, linkable experiments: the human messes around to find a
  bug, then hands the exact state to the agent. Crucially the agent must be able
  to *explore* states independently, not just replay the human's.
- **Make the inner loop fast.** Screenshots are good for end-to-end validation
  but slow and not the agent's favorite data. Convert to text: let the agent add
  logs freely (agents are excellent debuggers) and query the console; better,
  build a **headless CLI** that runs the system and emits a data representation
  (`physics-cli.ts --vx=-7.71 --vy=2.13 --frames=50`). Low-friction headless
  runs let the agent try many varied experiments quickly.

A telling signal of fit: the agent **evolves its own feedback format.** Nobody
told it what data the CLI should emit; it decided, and changed it as needed —
adding a per-frame position `delta` that immediately exposed the bug (edge
collision absorbing horizontal momentum). Once the loop exists, the agent shapes
it.

The division of labor this creates: the human reviews *results* and crafts the
vision; the agent does the work and validates to spec — collaboration, not
abandonment. Real-world equivalents follow the same recipe: the Amp team's
`widget` CLI renders any TUI widget headlessly (widget tree or ASCII, with
state-over-time), unwieldy for a human but *lovely* for the agent, and wrapped in
a skill so the agent reaches it through the bash tool. Even pure screenshot
loops count — a UI storybook the agent opens and screenshots to confirm a change
(or, more usefully, to *see its own errors* and retry until it works).

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-feedback-loopable-a35615e9.md` — origin: https://ampcode.com/notes/feedback-loopable
- `sources/amp/chronicle/https-ampcode.com-notes-how-i-use-amp-60b3bca7.md` — origin: https://ampcode.com/notes/how-i-use-amp
- `sources/amp/chronicle/https-ampcode.com-notes-mainframe-magic-ff27eb54.md` — origin: https://ampcode.com/notes/mainframe-magic
