# Safe maintenance: propose a plan, never mutate silently

A tool that maintains your agent setup should diagnose, surface a plan, and wait
for your go-ahead before changing anything — even when it's confident, and even
though every change it makes is reversible. Confidence is not the same as
permission.

Why this matters: setups drift silently. Skills you stopped using, a CLAUDE.md
that quietly grew to 10k tokens, hooks that slow every turn, a Claude Code
version three releases behind — none of it announces itself, so you only
notice once something measures it. A maintenance command you can't trust to
run unsupervised on a real project either goes unused or gets rubber-stamped
past its own checks; propose-then-confirm is what lets you actually run it on
a live setup without holding your breath.

Boris shipped **`/checkup`** for exactly this: it inspects the whole Claude
Code install — unused skills, CLAUDE.md bloat, slow hooks, a stale version,
permission-prompt friction (routed into `/fewer-permission-prompts`) — across
seven areas, then surfaces a plan (what's broken, what's unused, what it would
change) and stops. Nothing is modified until you pick an option, and every
change is reversible — the same discipline as reviewing `git diff` before you
commit. Boris ran it against his own setup and it surfaced drift he didn't know
was there.

`/checkup` doesn't replace the underlying habits — it automates them: context
minimalism ([[context-hygiene]]), CLAUDE.md hygiene ([[compounding-memory]]),
and the committed-config surface it's auditing
([[customization-checked-into-git]]). It's the maintenance half of "keep your
setup lean," turned from a habit you have to remember into a command you run.

## Sources

- `sources/cherny/howborisusesclaudecode/https-howborisusesclaudecode.com-a4e56975.md` — origin: https://howborisusesclaudecode.com
