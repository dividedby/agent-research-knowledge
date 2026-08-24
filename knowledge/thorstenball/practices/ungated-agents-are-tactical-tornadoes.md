# Ungated agents are the ultimate tactical tornadoes

An unsupervised agent risks becoming what Ousterhout called a "tactical
tornado" — a contributor who churns out plenty of *working* code that doesn't
fit cleanly into the existing system, leaving the team to clean up the
resulting complexity debt. Ball, reading Russ Cox's "People of ACM" interview
(which cites Ousterhout's term), draws the direct line to agents: "If we
aren't careful managers, AI agents can easily become the ultimate tactical
tornadoes."

The failure mode isn't that the generated code is broken — each piece can pass
review in isolation. It's that raw output volume reads as productivity to a
manager who isn't watching for *fit*, while the integration and complexity
debt lands on whoever inherits the system. Agents make the classic
tactical-tornado risk worse than a fast human ever could, because they churn
at higher volume, faster, with no fatigue to slow the pace down — so unmanaged
output can pile up debt quicker than a team notices.

The hedge is the same one the review/verification discipline in this corpus
already argues for: someone still has to act as the careful manager, judging
whether agent output *fits* the system and doesn't box in future changes — not
just whether each diff works on its own terms.

## Sources

- `sources/thorstenball/blog/https-registerspill.thorstenball.com-p-joy-and-curiosity-96-414473f3.md` — *Joy & Curiosity #96*: quoting Russ Cox's "People of ACM" interview citing Ousterhout's "tactical tornado" term, applied to ungated AI agents (origin: https://registerspill.thorstenball.com/p/joy-and-curiosity-96)
