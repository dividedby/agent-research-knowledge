# A read-only CLI can teach the domain glossary through its `--help` text

`course-video-manager` ships `cvm`, a read-only CLI (`app/cli/`) that exposes
the project's domain data to agents by **reusing the existing read-operation
services** rather than standing up a parallel query layer. The interesting
design choice isn't the CLI itself — it's what the `--help` text is for: it's
written in the same ubiquitous-language terms as [[shared-language-as-agent-fuel]]'s
`CONTEXT.md`, so running `cvm --help` (or a subcommand's `--help`) teaches an
agent the project's vocabulary the same way reading `CONTEXT.md` would, but
reachable from inside a tool invocation instead of a file read.

## The cost: a second copy of the glossary, kept in sync by hand

This surface is explicitly **not** generated from `CONTEXT.md` — the project's
own instructions say to "keep the cvm help text and `CONTEXT.md` in sync
manually," updating the noun/verb help in `app/cli/commands/*.ts` and the root
help in `app/cli/index.ts` whenever domain vocabulary or entity fields change
in the glossary. That's a deliberate trade-off: a single source of truth
(`CONTEXT.md`) would need either a generator or a runtime read, and the project
instead accepts a manual-sync obligation on two artifacts that must stay
worded the same way. The payoff is that the vocabulary shows up natively in a
CLI's help output — the format an agent already parses when it runs
`--help` to learn an unfamiliar tool — rather than requiring a separate file
read to pick up the domain's nouns and verbs.

## The general shape

Where the domain glossary lives in `CONTEXT.md` for an agent editing code, a
project can additionally surface the *same* vocabulary through any tool
surface an agent queries at runtime — here, a CLI's `--help`. The generalizable
move is picking a glossary-consumption point that matches how the agent
already interacts with the tool, and then explicitly naming the sync
obligation this creates (rather than letting the two copies drift silently).

## Writes are added one noun at a time, and land immediately

A later revision starts turning `cvm` from read-only into "read-mostly": one
noun (`segment`) gains write verbs (`add`/`update`/`move`/`delete`) that author
a Video's Segment plan by reusing the existing write service, while every
other noun stays read-only — "more nouns may gain writes over time" frames
this as a deliberate, incremental rollout rather than a one-shot flip. The
writes themselves are **immediate**: no confirmation prompt, no dry-run mode.
That follows from what the CLI is *for* — an agent invoking a command has
already decided to act, and a tool built to be driven by an agent has no
human on the other end of an interactive "are you sure?" to answer, so the
only real safety lever is which nouns get write verbs at all, not a runtime
guard on each call. The glossary obligation from above carries over
unchanged: the new verbs' `--help` text still has to track `CONTEXT.md` by
hand.

The write-capable noun itself isn't pinned to a name, either: the very next
revision renames it from `segment` to `beat` (`beat add/update/move/delete`),
in lockstep with the same domain-vocabulary rename in `CONTEXT.md`
([[enforced-vocabulary-as-agent-alignment]]). Nothing about the write
mechanics changes — same four verbs, same immediate-write posture, same
manual-sync obligation — only the noun the CLI exposes. Because the CLI's
help text is defined as tracking `CONTEXT.md` by hand rather than generated
from it, a rename in the domain glossary has to be replayed as a matching
edit in `app/cli/commands/*.ts`, the same manual-sync cost paid every time
the two artifacts drift, not a one-off migration.

## Sources

- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md (revision 2026-06-30)
- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md (revision 2026-07-02)
- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md (revision 2026-07-07)
