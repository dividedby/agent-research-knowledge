# Pick languages, frameworks, and platforms for agent legibility, not developer ergonomics

Now that agents write and debug most of the code, the criteria for choosing a
language, framework, or platform have flipped: syntax elegance and tool
ergonomics — the things a human developer used to weigh — barely matter
anymore, as long as the agent can produce good results in it. What matters
instead is whether the *system's runtime behavior* is legible to the agent:
performance characteristics, resource usage, failure modes, observability,
debuggability, deployments, rollbacks. If the agent can't see how the thing it
built actually runs, it can't debug or improve it, no matter how capable the
model is.

Ball's own case study is a platform that failed this test: building on
Cloudflare Durable Objects, the agent kept treating it as ordinary Node.js,
didn't know the runtime's actual characteristics, and couldn't inspect what
was happening — there are no logs telling you when your code gets evicted or
resumed. A platform that's opaque to introspection is opaque to the agent
twice over: it can't discover the behavior from docs it wasn't trained deeply
on, and it can't discover it empirically either, because the feedback loop
(logs, traces) doesn't exist. The lesson generalizes past Durable Objects: any
tool or platform you adopt should let the agent find out, from the codebase
and its own feedback loop, how the thing runs and how to see that — not rely
on the human already knowing.

The reframe behind this: switching from writing code yourself to directing an
agent that writes it is like switching from driving a car to controlling it
remotely — you stop caring about heated seats and AC (ergonomics you'd
personally feel) and start caring about how fast it brakes (properties that
determine whether the remote operator can actually control the outcome).
Shared abstractions (frameworks) still earn their keep in this world, but for
a different reason than before: not because they save typing (that cost is
heading to zero anyway) but because they hand you a pre-decided way to do
auth, hit a database, or separate dev from prod — one less thing you have to
think about, independent of who's typing.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-101-6013f6b9.md` — *Joy & Curiosity #101* opening essay on languages/frameworks after DHH's "Rails is over" keynote: syntax/ergonomics no longer the deciding factor, what will matter is legibility to the agent (performance, failure modes, observability, debuggability, deploys, rollbacks), the Cloudflare Durable Objects logging/eviction disaster, the driving-vs-remote-control car analogy, and why shared abstractions still matter (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-101)
