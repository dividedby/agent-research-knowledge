# Extending an agent-facing CLI to remote machines: refuse, don't degrade

Once `cvm` ([[agent-facing-cli-as-glossary-surface]]) needs to run from a
machine other than the author's — a remote agent box, not just the author's
laptop — two problems that a single-machine tool can leave implicit become
unavoidable: which capabilities need the author's *physical* machine, and
whether a remote caller's copy of the schema is still current. `cvm` answers
both by **refusing up front**, never by degrading silently or failing mid-work.

## One token, one transport, no in-process shortcut

A **Remote Box** — any machine that isn't the author's — runs `cvm` against
the deployed `apps/remote` API (a Hono app on Vercel) authenticated by an
**API Token**: a bearer credential minted from the local UI, carrying a human
name (which box it's on), a default 90-day expiry, and a revocation the
author can apply at any moment. Only the token's SHA-256 is stored — the
secret is shown once, at mint time, so the copy on the box is the only one
left in existence. It's unscoped in version one: a token grants every
operation the RPC surface exposes, not a subset.

Critically, this is **the same transport the author's own invocations use** —
there is deliberately no in-process fallback that would let the author's
machine take a shortcut a remote box can't. One code path means "does it work
for an agent" and "does it work for the author" can never quietly diverge.
Wiring a new capability into that path is a checked, two-line change: one
`.post` route in `apps/remote/routes/<noun>.ts`, one `rpcMethod` line in the
CLI's RPC layer — the route table, the service signature and the argument
order are each verified by the build, not left to a runtime mismatch.

## Locality is a property of the command, declared and refused up front

A Remote Box reaches every domain noun `cvm` exposes and can read and write
almost everything through it — but three commands need the author's physical
machine and nothing can change that: `cvm file` (needs the Video Files
directory), `cvm course readiness` and `cvm course publish` (need the
finished-videos directory and, for publish, ffmpeg). These are named
**Local-only Commands**, and each refuses *at the front of the command,
before doing any work*, naming exactly what it would have needed. The
author's machine declares itself with an environment variable
(`CVM_LOCAL_MACHINE`); any box that says nothing is treated as remote by
default — the safe direction to fail in.

The refuse-first design is deliberate, not incidental: a refusal is something
an agent can stop on immediately, where a filesystem error partway through a
multi-step write is something it might retry — and retrying a half-finished
`course publish` is exactly the state a Course must never be left in.
Locality isn't inferred from what happens to work at runtime; it's declared
per-command and checked before the command does anything observable.

## A schema mismatch is refused outright, not silently tolerated

Every `cvm` request states its **Schema Version** — the number of Drizzle
migrations the checkout was built against — and the deployed API compares it
against its own. Any difference is refused outright (a distinct exit code,
naming both numbers and telling the caller to pull); an out-of-date box
doesn't get to write against a schema it doesn't understand. Migrations
themselves are additive-only (no dropped or renamed columns without a
two-step release), which is what actually keeps a `cvm` call already in
flight from breaking when a migration lands mid-request — the version gate
only refuses the box's *next* command, it can't undo one already running.

That additive-only rule mattered enough to force a correction to *how*
migrations get applied. The first version had `apps/remote`'s deploy apply
pending migrations automatically — but that ran on **every** Vercel build,
previews included, so an unmerged migration could land on the production
schema on a preview deploy. ADR 0026 moved migration application to a manual
step (`pnpm db:migrate`, run by hand against the direct database connection,
before or as part of deploying `apps/remote`) precisely because the
automatic version created the exact class of risk the Schema Version gate
exists to prevent on the read side.

## Sources

- `sources/mattpocock/course-video-manager/CONTEXT.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CONTEXT.md (revision 2026-08-11, new "Remote access" section: **API Token**, **Remote Box**, **Local-only Command**, **Schema Version**)
- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md (revision 2026-08-11, `cvm` reaches data over HTTP through `apps/remote`, bearer-token auth, one-transport rule, Schema Version refusal, three local-only commands, one-route-one-rpcMethod build check)
- `sources/mattpocock/course-video-manager/README.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/README.md (revision 2026-08-12, ADR 0026: migrations moved from an automatic deploy step to a manual `pnpm db:migrate`, because deploy-time application ran on every Vercel build including previews)
