# Junior programmers still need to build things by hand

antirez's "control the ideas, not the code" argument (see
[control-the-ideas-not-the-code](./control-the-ideas-not-the-code.md)) comes
with an explicit carve-out: it's a claim about experienced programmers who
already have a mental model to steer with. He's genuinely unsure it applies to
people who don't have one yet.

The open question he poses: does a junior programmer need to closely read and
understand LLM-generated code the way a senior does? He doubts it — but not
because review is unnecessary for them. His guess is that reviewing an LLM's
output is *not* the right exercise for building the missing fundamentals in
the first place. What he'd recommend instead is the opposite of reviewing
someone else's code: implementing small, real systems from scratch — a toy
interpreter, a small database, a hash table — the kind of exercise that forces
you to build the mental model that lets a senior "control the ideas" later.

The corollary keeps the advice from over-generalizing into gatekeeping: this
is not an argument for busywork. Reviewing generated glue code for a
throwaway client website is exactly the kind of code-reading that's *not*
worth anyone's time, junior or senior — the fundamentals-building exercise
should be a real, self-contained system, not make-work review of disposable
code.

## Sources

- `sources/antirez/blog/http-antirez.com-news-169-b872d6d4.md` — origin: http://antirez.com/news/169
