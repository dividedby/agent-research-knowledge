# Give agents your priorities, not just a task spec

The highest-leverage change to a prompt today is describing your goals and
relative priorities, not just the literal task — because when frontier models
go wrong now, it's rarely confusion about instructions; it's an incorrect
guess about what you actually want.

Early agents needed narrow, literal instructions ("method A exists on class B,
add an equivalent method to classes C through F") because vaguer prompts
triggered outright confusion. That's no longer the dominant failure mode: a
model asked to write code with no context on who'll read it may produce
dense, minified-style output — not because it can't write readably, but
because it assumed it was writing for itself. Telling it the code is for
humans (or letting it infer style from an existing human-authored codebase)
fixes this instantly, because the model already has the judgment; it just
wasn't told which judgment to apply.

The practical move: spend real prompt space on context that isn't in the task
itself — the longer-term goal a short-term task serves, whether it's personal
or work, and explicit *relative* priorities (which of bug-avoidance,
observability, fitting the existing code, and performance you're willing to
trade off — not just a list of things that matter). A model given that
context can surface improvements you wouldn't have specified yourself —
alternatives a literal spec would have foreclosed. Withholding the context and
handing over only a technical spec reproduces the XY problem: you're asking
an expert to execute the narrow fix you assumed you needed instead of telling
it the actual goal, and losing the expert's ability to correct your framing.

## Sources

- `sources/seangoedecke/blog/https-seangoedecke.com-tell-agents-the-why-d7c944fb.md` — origin: https://seangoedecke.com/tell-agents-the-why/
