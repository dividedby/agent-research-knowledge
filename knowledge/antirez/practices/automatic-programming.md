# Automatic programming, not vibe coding

antirez names his method **automatic programming**: producing software with AI
assistance while remaining the author of its *vision* and design. He draws a hard
line against "vibe coding" — generating software without being part of the
process, where you describe what you want in general terms, accept whatever the
model's first sampled design happens to be, and at most report what doesn't work.

The distinction is not snobbery; it's about *who owns the output*. In automatic
programming the human supplies the multi-level vision — from *what* to build, down
to how a specific function should be written, stepping in to steer whenever
taste demands it. The same model in two different hands produces vastly different
results, so the differentiator is the human's intuition, design judgment, and
continuous steering, not the LLM. His blunt instruction: stop saying "Claude vibe
coded this for me." If you guided the process and understand what is going on,
**it is the software *you* are producing** — your code, your output, be proud of
it.

Why he's entitled to claim it as his own: pre-training data was produced by
humans collectively, so AI-generated code is not appropriated from someone else —
it's "our collective gift," a kind of shared mind that lets individuals build
things they otherwise never could. The corollary that frames everything: **code
is now automatic; vision is not (yet).** Redis itself contained little technical
novelty at its start — basic data structures and networking any competent systems
programmer could write — and became valuable because of its *ideas*. With the
mechanical act of writing code automated, the scarce, non-automatable input is
deciding *what* to do and holding a coherent design vision.

This reframes the goal of skill. Where vibe coding democratizes software for those
who don't know the internals (which antirez is fine with), automatic programming
is for shipping *high-quality* software that strictly follows the producer's
vision — and it is, like good design always was, "not for everybody."

## Sources

- `sources/antirez/blog/http-antirez.com-news-159-045d8a12.md` — origin `http://antirez.com/news/159` (the "automatic programming" vs vibe coding distinction)
- `sources/antirez/blog/http-antirez.com-news-158-8c9ae0e0.md` — origin `http://antirez.com/news/158` (programming changed forever; democratizing code)
- `sources/antirez/blog/http-antirez.com-news-154-a6ca24d9.md` — origin `http://antirez.com/news/154` (coding with LLMs, mid-2025)
- `sources/antirez/blog/http-antirez.com-news-164-5334e7d1.md` — origin `http://antirez.com/news/164` (Redis Array data type, built with automatic programming)
