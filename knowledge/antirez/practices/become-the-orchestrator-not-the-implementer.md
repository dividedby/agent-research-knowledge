# Become the orchestrator, not the implementer

antirez's framing, drawn from Linus Torvalds's career: done well, automatic
programming means occupying the role of a project *leader* who directs several
parallel contributors, not a lone implementer reviewing every line they
produce. Linus's real feat wasn't kernel-hacking talent — writing a minimal
Unix kernel was within reach of many capable programmers. It was recognizing,
early, that Linux would outgrow what one person could implement or review
line-by-line, and deliberately stepping back from writing code to hold the
design vision and dialogue with subsystem maintainers about *direction*: what
to build, what quality bar, what strategy — intervening to write or rewrite a
subsystem himself only rarely, when it mattered.

When you run coding agents you are structurally in that position already: the
agents are your subsystem maintainers, and — as in
[control-the-ideas-not-the-code](./control-the-ideas-not-the-code.md) — the
value you add is choosing direction and supplying design intuition, not
reading every generated line. What this post adds is the *shape* of that role
and why it beats a human team at the same job: running several agent branches
in parallel gives near-instant feedback with far less context-switching and
none of the interpersonal friction a multi-person team carries — you're
directing one to a few fast "maintainers" instead of many people at human
speed.

The post's sharpest use of the analogy is a rebuttal, not just a metaphor: a
common misreading of "you don't need to review every line anymore" is that
automatic programming must therefore be effortless — "I put the prompt, and
the thing writes" (vibe coding). It isn't. Leading agents well takes the same
trained skill Linus had to grow into: judging which directions to take,
sensing design quality, and giving agents the design hints a good programmer
intuits and a great one precomputes. That leadership skill is learned, not
innate or automatic, which is why "with LLMs, programming is easy for
everybody" doesn't hold — the bottleneck moved from typing code to exercising
this kind of judgment, and judgment doesn't come free just because typing got
cheap.

## Sources

- `sources/antirez/blog/http-antirez.com-news-171-e3f34c1a.md` — origin: http://antirez.com/news/171
