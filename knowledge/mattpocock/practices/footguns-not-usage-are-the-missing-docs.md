# What's missing from library docs is footguns, not usage

The docs an agent needs from a library or framework are not the ones most
projects ship. Usage is already solved: **"Docs are trivial to crawl for
agents, and the repo usually has tons of prior art"** — an agent can reconstruct
correct usage from the docs and the ecosystem's own example code without help.
What's actually scarce is the opposite kind of knowledge: **"a skill on how NOT
to use them. The list of footguns, presented in severity order."**

The reason this has to be authored deliberately rather than left to be
crawled is that footguns aren't discoverable the way usage is — usage is
written down; footguns are learned by getting burned. Matt's own account of
where his footgun knowledge currently comes from makes the cost concrete:
**"Right now, I'm having to shoot myself in the foot before discovering the
rule, then manually writing it into my CODING_STANDARDS.md for my review
agent."** Each footgun is paid for once, painfully, in production, then
hand-encoded so it isn't paid again — a private, incremental version of the
document a framework's own maintainers could ship once for everyone: **"I
would love to have that provided for my via the framework itself."**

The transferable claim: for any tool an agent works through, the reference an
agent needs least is "how it works" and needs most is "what looks fine but
silently produces trouble" — and that document has to be written on purpose,
severity-ordered, because no amount of crawling usage docs or prior art
manufactures it for you.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2082817962965180761-85a7a83c.md` — origin: https://x.com/mattpocockuk/status/2082817962965180761
