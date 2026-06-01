# agent-research-knowledge

A **public, read-only mirror** of the synthesized `knowledge/` layer from the
private `dividedby/agent-research` knowledge base.

- **Derived, never authoritative.** This tree is pushed verbatim from
  agent-research's `synthesize` workflow (commit-if-changed). Do not edit here —
  changes are overwritten on the next sync.
- **Only `knowledge/` is mirrored.** The raw `sources/` layer (captured tweets,
  article text, repo snapshots) never leaves the private repo.
- **Why this exists.** It gives downstream consumers a credential-free way to read
  the distilled knowledge — a transport/visibility change authorized by
  agent-research ADR 0019 (2026-05-31 amendment), not a curated bundle.

Consumers shallow-clone this repo and read `knowledge/<subject>/...`.
