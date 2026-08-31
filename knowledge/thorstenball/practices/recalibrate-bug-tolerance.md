# Recalibrate how many bugs you tolerate now that agents fix them fast

Every codebase already runs at some non-zero, non-infinite bug tolerance — true
zero costs more than it buys, too many kills the product — but that number
tends to freeze in place for years because nothing forces a re-check. Agents
change the correct answer, not by moving the acceptable-defect line but by
cutting the cost of the other side of the equation: bugs are faster to find and
fix, investigations run asynchronously and in parallel, you can debug areas of
the codebase you'd never otherwise have touched, and you can throw an unbounded
number of agents at the same bug at once.

Ball's framing for why this demands a deliberate reset, not a gradual drift:
imagine a genie handed you, back in 2018, a team of ten tireless world-class
debugging specialists working in parallel, free of charge — you wouldn't keep
shipping at the old cadence "to be safe," you'd recalibrate what "fast" even
means, because a bug making it to production no longer means "it sits there
until someone gets around to it," it means "it's fixed before most users ever
notice." The old choice was binary — go slow and ship nothing broken, or go
fast and reckless — and the right target now is neither: it's finding the point
where speed and defects balance given that a shipped bug's *lifetime* has
shrunk, not the point where defects are avoided altogether. Keeping the old,
frozen bug-tolerance number means throttling velocity against a risk that no
longer costs what it used to.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-97-082d4c51.md` — *Joy & Curiosity #97* opening essay: "How many bugs are you willing to tolerate in your codebase?" — the genie framing, recalibrating speed vs. defects now that agents shorten bug lifetime (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-97)
