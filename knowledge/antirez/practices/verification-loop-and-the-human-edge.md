# Verify everything; the human keeps the creative edge

antirez treats the LLM as a fast, erudite, but limited partner — and organizes his
practice around two facts about it: it is excellent at *blending and recalling*,
and weak at *novel reasoning*. The operating rule that falls out: **only use the
model where you can verify its output**, and never outsource the genuinely
creative leap.

**Verify, don't trust.** His recurring pattern is "I have a problem, I need to
quickly know something that *I can verify* if the LLM is feeding me nonsense." He
copy-pastes API shapes into the model, gets code, and tests in the REPL that the
tensors really have the dimensions he needs. He uses frontier models routinely for
free, fast **code review** — catching bugs he introduced before they ever reach a
user — precisely because a review is something he can check. The verification loop
is also what makes agents trustworthy on tedious work: he had Claude Code iterate
until it could reproduce a transient, timing-related Redis test failure, inspect
process state, and fix it — work he could confirm because the test either flakes
or it doesn't.

**The human supplies the out-of-the-box leap.** In a detailed account of designing
a fast reciprocal-link check for Redis Vector Sets, Gemini 2.5 Pro could only
offer the textbook answer (sort pointers, binary-search); it was *antirez* who
proposed the XOR accumulator and then the seeded murmur-128 hash scheme. The model
was invaluable as a "smart duck" — verifying his ideas, doing the collision
analysis, sharpening the design — but "the creativity of humans still has an edge,
we are capable of really thinking out of the box, envisioning strange and
imprecise solutions that can work better." The division of labor: the human
escapes local minima and invents; the model knows more facts than any human and
checks the work.

**Know the boundary.** For disposable, textually-representable, high-level code
(throwaway scripts, glue, data-munging in Python) he lets the model write
everything — the effort-to-benefit ratio of doing it himself is bad, and he can
verify the result trivially. For deep system programming, when he was already an
expert, LLMs were long "only a more convenient form of documentation": they failed
disastrously the moment subtle reasoning was required (a bloom filter with
correctly decorrelated hashes; reverse-engineering a GGUF quant encoding). The
model is a "stupid savant" — vast knowledge, shallow reasoning — so route work to
it accordingly. (Frontier models later closed much of this gap for systems work,
which is exactly why he tests "what agents can do" periodically and switches when
they genuinely surpass him — but the verify-where-you-can rule is invariant.)

## Sources

- `sources/antirez/blog/http-antirez.com-news-140-a4888026.md` — origin `http://antirez.com/news/140` ("LLMs and programming in the first days of 2024": verify-or-nonsense, disposable programs, the system-programming failures, stupid-savant framing)
- `sources/antirez/blog/http-antirez.com-news-153-b041a882.md` — origin `http://antirez.com/news/153` (the reciprocal-link design story: human creative edge, the LLM as "smart duck")
- `sources/antirez/blog/http-antirez.com-news-148-7aa62477.md` — origin `http://antirez.com/news/148` (routine practical help: code review, understanding papers, "free and fast code review")
- `sources/antirez/blog/http-antirez.com-news-158-8c9ae0e0.md` — origin `http://antirez.com/news/158` (Claude Code iterating to reproduce and fix a transient Redis test failure)
