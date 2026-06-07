# Building software is learning

Ball's keystone principle for working with agents: **building something new is an
act of learning, not of execution.** When there's no spec — when you don't yet
fully know how the thing is supposed to behave — you only discover what you're
actually building *by* building it. You will bump into "that's not what I meant,"
"now that I'm working on it I'm not sure," and "now that I use it, I don't like
it." There is *no way* to avoid this, because the only way to avoid it would be
to fully specify the thing up front, and fully specifying what you want *is*
programming. (His shorthand for the alternative: go type "waterfall software"
into Google.)

This is the frame everything else hangs off. It explains *why* an agent's speed
isn't an unalloyed good: an agent will happily pick an answer to a question you
didn't know you were asking — which array should be `Client[]` vs. a single
`client: Client`, whether multiple clients can connect at once — and just write
the code, **without telling you it made the choice.** When the goal is to learn
(so you can make better engineering and product tradeoffs), that silent
resolution is the cost. So the boundary is: if you're *not* building something
new, or don't need to understand how it works, or already hold a good mental
model — let the agent rip; most software development is *not* building something
new. But where you need to learn, you have to stay in the loop, because the
learning is the point.

The meta-skill that survives the churn is exactly this learning ability, not the
prompt tricks. Ball reflects that "don't make mistakes" is a prayer, "you are a
senior engineer" is obsolete, and even manual context management is fading — but
what he actually got better at over two years is **chopping problems into
agent-sized tasks and sequencing them, spotting the pitfalls that wouldn't be
pitfalls for a human, and knowing what's "poison" in a codebase.** In the most
general sense: he learned how to work *with* an intelligence. If prompt-engineering
tricks are punch cards, that's learning about computation.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-building-software-is--caff9672.md` — *Building Software Is Learning* (origin https://registerspill.thorstenball.com/p/building-software-is-learning)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-76-cf332424.md` — *Joy & Curiosity #76* intro: writing code by hand to learn what new software should do (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-76)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-82-9bedf3cd.md` — *Joy & Curiosity #82* intro: the durable meta-skills vs. punch-card prompt tricks; "this is what software development is: learning" (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-82)
