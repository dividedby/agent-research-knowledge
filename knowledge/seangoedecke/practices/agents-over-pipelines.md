# Default to agents over pipelines

There are two ways to put an LLM in a program: a **pipeline** (control flow lives
in your code, which calls the model at fixed points) or an **agent** (you hand the
model tools and let it drive the control flow). The choice is the same
library-vs-framework trade-off — a pipeline gives you control at the cost of
boilerplate you must write and maintain; an agent gives you capability for free at
the cost of predictability.

**When in doubt, build the agent.** Goedecke's default is unambiguous, and rests
on a few asymmetries:

- **Agents are smarter.** They can loop, gather more information after thinking,
  and keep going until the model decides it's done. Hard tasks (coding is the
  canonical one) simply cannot be solved by a single-shot pipeline — every
  successful coding product is an agent, not a pipeline.
- **Context-gathering is the hard part, and agents solve it for free.** A pipeline
  must assemble *all* needed context up front because the model runs once; getting
  that right is an unsolved problem (RAG, AST-walking, embeddings — none work as
  well as just letting the agent `grep` and read files like a human would). The
  field went *backwards* from RAG to plain-text search precisely because "find
  what's relevant" is often as hard as solving the task itself.
- **Agents are more future-proof.** Models are now trained specifically to be
  better agents, and agents delegate more to the model — so a new model release
  makes an agentic system *much* better, while it makes a pipeline only a bit
  better. This justifies building an agent for a task that's currently too hard,
  betting the models will be good enough by the time you ship.

Pipelines win only on **predictability**: bounded cost and latency (an agent can
take 1 turn or 100, swinging cost 2x+ on a data change), the ability to mix cheap
and expensive models per stage, and the ability to run in small/local contexts
(agents always ingest more than they need, and each loop turn grows the context).
So reach for a pipeline when you have hard limits on context size, must accurately
cap GPU cost, or must run on local models — otherwise build the agent.

Two common arguments for pipelines don't hold up. **Safety:** workflows control
*budget*, but the act of taking action on model output has the identical
checking problem at the tool-call boundary or the pipeline-stage boundary, and
both designs eat prompt injection from the same untrusted data — you sanitize and
gate actions regardless. **Legibility:** pipelines are slightly more traceable,
but you never truly know why the model responded as it did either way. And note
the migration direction in practice is one-way: projects move pipeline→agent, not
the reverse.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-build-agents-not-pipelines-217ae140.md` — origin: https://seangoedecke.com/build-agents-not-pipelines/
