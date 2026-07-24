# Two solid examples let an agent extrapolate the third automatically

A codebase can be built to bootstrap its own future implementation work: once
it contains two well-built examples of a pattern, a strong coding agent can
infer the pattern well enough to implement a third instance of it with little
to no steering. antirez's evidence from DwarfStar (his local-inference
engine): once the engine supported two models well enough, a third could be
"implemented in an almost automatic way, using the existing code base as a
guardrail for coding agents in order to guide the implementation." The same
held for tensor-parallel graph execution across backend/model pairs — DwarfStar
can't be exhaustively tested across every GPU, model, and execution mode
combination, but two solid examples of one execution pattern are enough for an
agent to generalize the rest.

The concrete before/after is stark: implementing earlier models (DS4, GLM5.2)
cost him "a lot of steering, reading the model card and the details of the
implementation of the attention of those models" — because the codebase didn't
yet have a strong exemplar to extrapolate from. Once it did, a new model
implementation was written in about two hours, automatically, by a frontier
model that "found a lot of good examples inside the existing source code."

The design implication runs opposite to "cover the whole feature matrix
yourself": a project doesn't need to work out of the box for every
configuration if it supports a couple of cases *very well* — the well-built
examples become rails a coding agent can follow to cover the remaining cases,
including cases the maintainer never personally implements. This reframes what
"good code" is for in an agent-adjacent codebase: exemplar quality on a few
cases is worth more than defensive coverage of all of them, because the
exemplars are the guardrail the next agent-driven implementation steers by.

## Sources

- `sources/antirez/blog/http-antirez.com-news-170-fb1dbfd3.md` — origin: http://antirez.com/news/170
