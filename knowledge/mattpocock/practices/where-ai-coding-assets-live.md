# Not every AI coding asset belongs in git

Working with an agent generates a class of intermediate assets — **PRDs, research
files, decision maps, implementation plans** — and Matt's open position is that
most of them *don't belong checked into the repo's git history*. They are
scaffolding for a change, not the change; committing them clutters the tree with
process artefacts that outlive their usefulness and that the next reader has to
wade past to find the code.

Where they go instead is unsettled, but his current split is concrete:

- **PRDs and implementation plans → GitHub issues.** The issue tracker is the
  natural home for a spec or a plan: it is durable, linkable, and already the seam
  his skills hand work across (`to-prd → to-issues`), so the plan lives beside the
  work it describes without polluting the source tree.
- **Research files → still unresolved.** He checks these into git today only
  because he has nowhere better to put them; he is openly considering an
  **external knowledge base** instead, and notes that parking research in a
  GitHub issue is "a bit awkward." He has held this idea for months without
  building it — uncertain whether no one has tried it because it is good, or
  because it sucks.

The unifying instinct is the same one behind treating the agent as an amnesiac and
keeping `CLAUDE.md` to a tight budget: be deliberate about *which* durable surface
each kind of generated artefact lands on, rather than defaulting everything into
the repo. A related preference falls out of it — for most workflows Matt keeps the
agent's "brain" / knowledge store **stateless**, rather than building a persistent
personal memory the agent carries between tasks.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069698109492343101-6d683ee8.md` — origin: https://x.com/mattpocockuk/status/2069698109492343101
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069698238685294858-6c3f48d8.md` — origin: https://x.com/mattpocockuk/status/2069698238685294858
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069698455195263459-5c40425e.md` — origin: https://x.com/mattpocockuk/status/2069698455195263459
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069728413896585249-6c940188.md` — origin: https://x.com/mattpocockuk/status/2069728413896585249
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2069741439349633054-d92739c9.md` — origin: https://x.com/mattpocockuk/status/2069741439349633054
