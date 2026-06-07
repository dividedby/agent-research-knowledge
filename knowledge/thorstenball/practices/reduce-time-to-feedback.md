# Reduce the time to feedback

If building new software is learning, the single most important thing you can do
is **shrink the time between "let me try something" and getting your ass whooped
by reality.** Ball's framing: every new build has a `...` gap between the confident
"yes, let me build it" and the humbled "oh, I see." You can't eliminate the gap
(you can't define what you want until you've learned it), but you *can* compress
it — and that compression is the highest-leverage move in the whole process.

The discipline is to constantly ask: **how can I get feedback on what I'm building
as soon as possible?** "Feedback" is meant in the widest sense — from CI on main,
from colleagues, from users, from *yourself* once you actually use the thing.
Concrete cheap probes he lists, instead of disappearing for four weeks: build a
one-hour prototype; write a 30-minute spec; ship one small slice per day so each
day hits reality; cut scope to *only* the parts you're unsure about (don't build
5 logins when you need to learn 1); fake a demo video; write the launch post; write
the example code that'd go in the README and check if the API feels right before
building the SDK. Pick several and combine them.

Following the "feedback as soon as possible" question also tells you *how* to chop
and ship work. You won't get useful feedback from an obviously-buggy MVP (you'll
get bug reports, not signal), from something that takes 8 hurdles to test, or from
a branch held three weeks (merge 27 commits, CI blows up, now you have 27 suspects
instead of 1). And it tells you *what* feedback you can get cheaply: want feedback
on a skateboard's design? show the deck. Want feedback on how it *feels*? you need
the wheels on.

In the agent era this sharpens into a corollary Ball calls being "a very narrow
bottleneck": when an agent can produce code in seconds, the human's job collapses
to steering and verifying, and the existing tool flow (ticket → agent → PR →
review → merge) was built on the now-false assumption that code is slow and
expensive to write. The constraint moves off code generation and onto getting
feedback fast.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-building-software-is--caff9672.md` — *Building Software Is Learning* (origin https://registerspill.thorstenball.com/p/building-software-is-learning)
- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-74-7737f51c.md` — *Joy & Curiosity #74* intro: "I am a very, very narrow bottleneck now"; tooling built for slow-and-expensive code will collapse (origin https://registerspill.thorstenball.com/p/joy-and-curiosity-74)
