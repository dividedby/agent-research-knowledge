# Filesystem-backed session requirement: opaque file transfer over database coupling

Sandcastle only supports resumable sessions for agents whose conversation state is stored as discrete files on disk, not in databases. This architectural constraint prioritizes simplicity and stability over universal compatibility — file transfer is a bounded, well-understood operation, while database serialization couples the harness to private schemas that change between agent versions.

## The database coupling problem

A SQLite-backed agent stores conversation state inside a local database file whose schema is private to the agent, may change between versions, and can hold rows for many sessions in one file. Supporting resume would require Sandcastle to understand the schema, extract session subgraphs, serialize them for transfer, and re-insert them on the sandbox side.

This couples the harness to undocumented storage internals that are outside Sandcastle's control. When the agent updates its schema or changes its session representation, resume support breaks. The complexity grows with each agent provider's unique database design.

## File transfer as the stability boundary

File-based agents (Claude Code, Codex, Pi) persist one self-contained record per session that Sandcastle can copy verbatim and rewrite by line-level transformations (path adjustments, etc.). The session file is an opaque artifact — Sandcastle doesn't parse its internal structure, only transfers it intact.

This boundary keeps session transfer simple and stable. The agent owns its session format completely; Sandcastle owns only the transport mechanism. Schema changes within the session file don't affect the transfer logic because the file remains the unit of transfer.

The public seam has since narrowed to make this even cleaner: the `SessionStore`
factory exports were removed in favour of **pure-string** helpers —
`transferClaudeSession(jsonl, fromCwd, toCwd)` / `transferCodexSession(...)` — that
rewrite a session JSONL's embedded `cwd` paths *without touching the filesystem*.
The actual file I/O (read the sandbox file, write the host file) moves to the call
site. So the transferable-file requirement is now expressed as a pure transform over
a string plus thin path/scan utilities (`claudeHostSessionPath`,
`findClaudeSessionOnHost`, …), with each provider's `AgentSessionStorage`
composing them. The transform is testable in isolation and provider-owned, which is
the whole point: the agent's session format stays the agent's, and the harness's
contact with it is one string-rewrite function per provider.

## Qualification by storage architecture

The requirement is architectural, not technological. Codex uses SQLite as an index over filesystem JSONL files, with the files being the source of truth — this qualifies because the session data exists as transferable files. OpenCode stores sessions primarily in SQLite rows without file backing — this doesn't qualify.

The distinction is whether the complete session state can be captured by copying files, not whether the agent uses databases for any purpose. An agent that keeps session metadata in a database but writes the actual conversation to files can still be supported.

## Resume as optional capability

Agents that don't meet the filesystem requirement remain fully usable, just non-resumable. The provider ships with `captureSessions: false` and no `sessionStorage` implementation, which types `RunResult.resume` as `never` for that provider. This preserves the agent's core functionality while making the limitation explicit.

This graceful degradation means adding a new agent provider doesn't require solving session storage — it can start as a stateless provider and add resumability later if its storage architecture permits.

## Sources

- `sources/mattpocock/sandcastle/docs-adr-0016-resume-requires-filesystem-backed-sessions.md-46d84860.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/docs/adr/0016-resume-requires-filesystem-backed-sessions.md
- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: github.com/mattpocock/sandcastle (CHANGELOG.md)
- `sources/mattpocock/sandcastle/src-AgentProvider.ts-c6a6e278.md` — origin: github.com/mattpocock/sandcastle (src/AgentProvider.ts)