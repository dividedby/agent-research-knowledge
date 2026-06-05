# Short threads, one task each

Keep agent conversations small and single-purpose. A thread should do **one
thing** and carry just enough context to do it — then end. A feature or bugfix
is not one long thread; it's a *cluster* of short threads, each a discrete task,
linked by references.

Why it holds:

- **Agents degrade as context fills.** "Agents get drunk if you feed them too
  many tokens" — past ~100k they start forgetting first-prompt instructions and
  fall into doom loops (fixing the same test over and over). The fix isn't a
  bigger window; even with a million tokens the Amp team wouldn't run a thread
  that long. 200k is plenty *if you use threads*.
- **Long threads also cost more, nonlinearly.** Every token is resent on every
  request, so cost grows with length; some providers surcharge long-context
  requests; and long idle gaps between messages miss the prompt cache — a major
  driver of runaway-thread cost.
- **Short threads == small tasks.** Breaking a big problem into thread-sized
  units *is* the old discipline of breaking work into small tasks, which was
  good practice before agents and still is. Each unit has a well-defined goal you
  can keep track of.

How it shows up in Amp's own workflow:

- Start with one thread for a basic implementation (or a scouting thread to
  gather context if the area is unfamiliar). Each subsequent tweak, refactor, or
  review is a **new** thread — one change per thread.
- Carry context forward by *reference*, not accumulation: mention a prior
  thread's ID/URL (`@@` in the CLI), use handoff/fork commands, or point the
  agent at git state (`git diff`, a specific commit). Avoid piling everything
  into one mega-thread.
- Most beginner trouble with agents traces back to **not starting new threads
  often enough**.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-200k-tokens-is-plenty-4df831c1.md` — origin: https://ampcode.com/notes/200k-tokens-is-plenty
- `sources/amp/chronicle/https-ampcode.com-notes-how-i-use-amp-60b3bca7.md` — origin: https://ampcode.com/notes/how-i-use-amp
