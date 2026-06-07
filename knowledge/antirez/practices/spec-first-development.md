# Hand-write the specification first

For serious, high-quality work, antirez does not start by prompting for code — he
starts by writing a **specification document by hand**. On the Redis Array data
type he spent the *entire first month* writing the spec: the rationale for the
type, the C structures, the sparse representation, the exact semantics of the
array cursor. Only then did implementation begin.

The spec plays two roles that pay off across the whole project:

1. **It is what you steer with.** A long, precise design document evolves through
   back-and-forth with the model — "intellectual challenges about what was the
   best design, what was the right compromise, what was too engineered." The
   human's vision gets sharpened by the model before any code exists, and the
   model inherits a fully-formed target instead of guessing.
2. **It is what makes line-by-line review possible.** Because he wrote the spec,
   he can later read every line of the generated implementation and recognize
   inefficiencies or design errors against his own intent. "To write the initial
   huge specification was the key to the successive work, as it was the key to
   review each single line." Without the spec, reviewing AI output is reviewing
   against nothing.

For smaller agent runs the spec is a high-level markdown file of "just English,
high-level ideas about the scope" — what the thing is for, the constraints (e.g.
"must run on an RP2350," "one instruction at a time, not per-clock-step"), and the
desiderata. The point holds at both scales: **the human's durable contribution is
the design document; the code is the cheap, regenerable part.** This is why he
releases automatic-programming output without hesitation — the value he added
lives in the spec and the steering, not in keystrokes.

## Sources

- `sources/antirez/blog/http-antirez.com-news-164-5334e7d1.md` — origin `http://antirez.com/news/164` (Redis Array: a month writing the spec by hand; the spec as the key to line-by-line review)
- `sources/antirez/blog/http-antirez.com-news-160-3eec660b.md` — origin `http://antirez.com/news/160` (Z80: the high-level markdown spec file that opens the project)
