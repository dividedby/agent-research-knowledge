# Control what agents *do* with a deterministic box outside the agent

Brooker's safety/control posture: the flexibility that makes an agent valuable is
exactly what makes its behaviour impossible to bound from the inside, so control
must live in a strong, deterministic layer *outside* the agent — "the box."

## Do, not think

Riffing on Simon Willison's definition ("an AI agent runs models and tools in a
loop to achieve a goal"), Brooker narrows the focus to what agents *do* — their
side effects (writing files, calling services, making payments, starting a 3D
print), not their inference. Doing inference doesn't *do* anything; "without the
*do*, the *think* seems less important." Agents *do* things via tools (MCP, skills,
powers); controlling the *do* is the safety problem.

## Why outside the agent

The defining property of the box is **outside the agent**. Alignment, careful
prompting, steering, and context management are real and valuable — but for
*liveness* (success rate, cost), not *safety*. They're insufficient for safety
**for the same reason we build agents at all**: agents are flexible, adaptive,
creative problem solvers, and you cannot get strong guarantees about what a
creative thing will *do* by trying to constrain what it can *think*. In-agent
safety runs straight into this trade-off; an external, deterministic layer
sidesteps it.

The second payoff is crisp reasoning. If the box deterministically enforces "a
refund can only be ≤ the original price" and "one refund per order," you can
reason exactly about maximum refund exposure **regardless of the prompt-injection
attack of the week**. No errant prompt, context, or memory can bypass a control
at the edge of the box.

## What the box is

For cloud agents: a secure, isolated runtime (e.g. AgentCore Runtime) gives each
session a place to run its loop and execute generated code; a **gateway** (e.g.
AgentCore Gateway) is *the singular hole in the box* — the only place tools are
exposed and policy is enforced. The runtime's network controls stop the agent
sending packets anywhere else (old-school network security), so the gateway
can't be bypassed. Note the distinction from ordinary authorization: typical
authz governs *what an actor can do with a tool*; the gateway's first control is
*which tools exist at all*.

Because today's authz can't express or compose the constraints we want, a
**policy layer** sits at the gateway. AgentCore Policy uses the Cedar policy
language for fine-grained deterministic control, with natural-language policy
authoring on top (built on research converting human intent to policy) so people
don't have to learn Cedar.

## The real danger is the apprentice, not the spy

The most common failure isn't the adversary (prompt injection, hallucination) —
it's Goethe's *Sorcerer's Apprentice*. Agents are **persistent problem solvers**;
that persistence is the whole point (if a fixed workflow could solve it, you'd
use the cheaper, faster workflow). But a persistent solver, like the enchanted
broom, keeps fetching water until it floods the house. Policy layers and
structured steering (AgentCore Policy, Strands Steering) exist to make the agent
*stop when the basin is full* — and this matters **more** as models get more
capable and run longer, even with no adversary and no hallucination in sight.

## Sources

- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-01-12-agent-box.html-9060ee29.md` — origin: https://brooker.co.za/blog/2026/01/12/agent-box.html
- `sources/marcbrooker/blog/http-brooker.co.za-blog-2026-03-18-apprentice.html-89fb3199.md` — origin: https://brooker.co.za/blog/2026/03/18/apprentice.html
