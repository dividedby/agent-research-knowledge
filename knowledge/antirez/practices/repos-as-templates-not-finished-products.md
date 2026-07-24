# Ship repos as templates, not just finished products

Coding agents didn't just change how antirez writes software — they changed
what a released repository is *for*, because his users now have coding agents
too. When a recipient can ask their own agent to adapt, test, and specialize
your code, a single polished "finished" branch stops being the most useful
thing you can hand them; a 95%-ready, well-exemplified branch they can steer
further themselves is often more valuable than the fully-refined result you'd
eventually ship.

Concretely, this breaks the classic stable/unstable branching model. The old
shape — freeze a branch, squash bugs until reports taper off, cut a release —
assumed the recipient was a passive consumer of the finished artifact. He
gives two examples of why that assumption no longer holds:

- **A near-final feature branch beats waiting for merge.** His in-flight Redis
  PR for sorted-set memory savings will, once merged, help users uniformly —
  but for the subset already paying real cloud-memory costs, having the
  95%-ready branch *today* to test, adapt, and specialize for their own
  workload beats waiting for a fully polished release.
- **An experimental branch lets the community route around uncertainty.**
  When a new model (e.g. Laguna S.1) ships and it's unclear whether it will
  matter next to a faster-moving competitor, publishing it as its own branch
  in DwarfStar — rather than waiting to decide if it's merge-worthy — lets
  people try it and refine it with their own coding agents, so the group
  forms a collective verdict instead of one maintainer gatekeeping it alone.

The consequence: "main and unstable are no longer enough" — a project can
legitimately carry many live experimental branches as first-class parts of
itself, each one a template for a slightly different set of requirements or
hardware, not a queue of things waiting to be judged worthy of `main`. And
because the recipient's agent is now a reader of the repo alongside the
recipient, the documentation has to serve both: it should be written well
enough for coding agents to use it to understand how to change the system,
not only for human comprehension.

## Sources

- `sources/antirez/blog/http-antirez.com-news-170-fb1dbfd3.md` — origin: http://antirez.com/news/170
