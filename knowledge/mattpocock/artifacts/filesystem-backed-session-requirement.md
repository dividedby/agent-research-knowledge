# Filesystem-backed session requirement: opaque file transfer over database coupling

Sandcastle only supports resumable sessions for agents whose conversation state is stored as discrete files on disk, not in databases. This architectural constraint prioritizes simplicity and stability over universal compatibility — file transfer is a bounded, well-understood operation, while database serialization couples the harness to private schemas that change between agent versions.

## The database coupling problem

A SQLite-backed agent stores conversation state inside a local database file whose schema is private to the agent, may change between versions, and can hold rows for many sessions in one file. Supporting resume would require Sandcastle to understand the schema, extract session subgraphs, serialize them for transfer, and re-insert them on the sandbox side.

This couples the harness to undocumented storage internals that are outside Sandcastle's control. When the agent updates its schema or changes its session representation, resume support breaks. The complexity grows with each agent provider's unique database design.

## File transfer as the stability boundary

File-based agents (Claude Code, Codex, Pi) persist one self-contained record per session that Sandcastle can copy verbatim and rewrite by line-level transformations (path adjustments, etc.). The session file is an opaque artifact — Sandcastle doesn't parse its internal structure, only transfers it intact.

This boundary keeps session transfer simple and stable. The agent owns its session format completely; Sandcastle owns only the transport mechanism. Schema changes within the session file don't affect the transfer logic because the file remains the unit of transfer.

## Qualification by storage architecture

The requirement is architectural, not technological. Codex uses SQLite as an index over filesystem JSONL files, with the files being the source of truth — this qualifies because the session data exists as transferable files. OpenCode stores sessions primarily in SQLite rows without file backing — this doesn't qualify.

The distinction is whether the complete session state can be captured by copying files, not whether the agent uses databases for any purpose. An agent that keeps session metadata in a database but writes the actual conversation to files can still be supported.

## Resume as optional capability

Agents that don't meet the filesystem requirement remain fully usable, just non-resumable. The provider ships with `captureSessions: false` and no `sessionStorage` implementation, which types `RunResult.resume` as `never` for that provider. This preserves the agent's core functionality while making the limitation explicit.

This graceful degradation means adding a new agent provider doesn't require solving session storage — it can start as a stateless provider and add resumability later if its storage architecture permits.

## Sources

- `sources/mattpocock/sandcastle/docs-adr-0016-resume-requires-filesystem-backed-sessions.md-46d84860.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0016-resume-requires-filesystem-backed-sessions.md