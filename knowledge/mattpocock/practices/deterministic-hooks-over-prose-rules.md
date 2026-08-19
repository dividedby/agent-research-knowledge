# Deterministic hooks over prose rules

When you want an agent to *always* do X or *never* do Y, Matt's rule is: if the
constraint can be enforced mechanically, don't write it as prose in `CLAUDE.md` —
make it a hook. A prose rule ("use pnpm not npm", "don't `git push`") only
*reduces* the probability of the wrong behaviour; it never prevents it, and it
spends scarce instruction budget (see `claude-md-is-an-instruction-budget`) on a
guarantee it can't actually make. A `PreToolUse` hook makes the wrong command
*impossible* and costs zero budget.

## How the guardrail works

The hook is deterministic code wired into `.claude/settings.json` with a `Bash`
matcher. It receives the proposed command as JSON on stdin, greps it against
forbidden patterns, and **exits 2 to block** — which returns the error message
straight to the agent, who reads it and retries correctly ("Blocked: use pnpm
instead of npm"). It's a hard guardrail, not a suggestion buried in prose, so the
agent can't talk its way around it. Matt's `git-guardrails` skill ships exactly
this for destructive git (`push`, `reset --hard`, `clean -f`, `branch -D`,
`checkout .`), framed as "safe by default" rather than "never allow" — you
whitelist what your workflow genuinely needs.

## Why this matters most for autonomous work

The driving case is AFK/Ralph in a Docker sandbox. A sandbox isolates *where*
commands run (it can't reach your home dir or SSH keys) but doesn't restrict
*what* runs — and your git history lives inside the mounted project folder, so a
single `git reset --hard` can still wipe weeks of work while you're away. The hook
fills exactly that gap: deterministic protection for the commands the sandbox
can't reason about, on an agent no human is watching. Matt also notes the agent
can *write its own* hooks — point it at the `CLAUDE.md`, have it extract only the
deterministically-enforceable instructions (CLI preferences, banned commands) and
translate them into hook scripts, confirming before it does.

This is the same instinct as the pre-commit feedback loop (see
`feedback-loop-is-the-work`): for anything that should be guaranteed rather than
merely encouraged, prefer an automated, deterministic gate over trusting the
model's judgement.

## The pattern generalizes past `PreToolUse`

The guardrail doesn't have to live in `.claude/settings.json` — any deterministic
gate that fires before the wrong thing lands does the same job. Matt's
`course-video-manager` `CODING_STANDARDS.md` states an ESM convention in prose
("use `import.meta.dirname`/`import.meta.filename`, never the CJS
`__dirname`/`__filename`") and then backs it with a `check:no-dirname` pre-commit
hook that scans staged files for the banned globals. The prose still carries the
*why*; the hook is what makes the *never* actually true, at the point (commit,
not just tool-call) where this particular mistake is cheapest to catch. A coding
standard that only lives in a doc an agent might not reread is exactly the kind
of rule this pattern converts into something that can't drift.

## Scoped to narrow, mechanical checks — not a whole workflow's lifecycle

The rule above is about individual, checkable constraints (a banned command, a
banned global), not licence to encode an entire process as a hook chain.
Pitched on a hook layer that would enforce a skill workflow's full lifecycle as
a state machine — "ticket active → red observed → green observed → suite
passed → reviewed → committed → ticket reconciled" — Matt rejects the shape
outright: "sounds extremely invasive and likely a bit rubbish." The two ideas
aren't in tension: a `PreToolUse` hook blocking `git push --force` is a single
deterministic fact about one command, cheap to write and impossible to argue
with; a hook that tracks and gates a multi-step process state is reimplementing
what the skill's own prose already coordinates, at a layer that can't see the
judgement calls (is this test suite actually the relevant one? does this
commit close the ticket?) a skill can reason about. The line is narrow,
verifiable facts versus process orchestration — hooks earn their keep on the
former and get invasive and brittle on the latter.

## Endorsement signal: a general hierarchy for eliminating corrections

Matt amplified a practitioner (@poteto) stating the same instinct as a general
rule, not specific to hooks: "every time you intervene and correct your agent,
you should think about how to eliminate it entirely" — and ranks the fixes in
order of value: (1) categorically eliminate the problem through better
architecture or choice of data structures, (2) turn it into a lint rule or
test so CI catches it, (3) turn it into a skill or rule, (4) have humans
review the code to catch it ("ngmi"). This is a repost, not Matt's own words —
attribute the hierarchy to @poteto — but it generalizes exactly the shape this
doc argues for one specific case: a `PreToolUse` hook is rung (2)'s
deterministic-CI-gate move applied to a command instead of a code pattern, and
the hierarchy's ordering makes explicit what this doc leaves implicit —
prose-rule steering (rung 3) is only reached for *after* ruling out a
structural fix, and manual human review (rung 4) is the fallback of last
resort, not a first line of defense.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-how-to-use-claude-code-hooks-to-enforce-c827626c.md` — origin: https://www.aihero.dev/how-to-use-claude-code-hooks-to-enforce-the-right-cli
- `sources/mattpocock/aihero/https-www.aihero.dev-this-hook-stops-claude-code-running-dan-bcfc7d9c.md` — origin: https://www.aihero.dev/this-hook-stops-claude-code-running-dangerous-git-commands
- `sources/mattpocock/course-video-manager/.sandcastle-CODING_STANDARDS.md-7b893b74.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/.sandcastle/CODING_STANDARDS.md
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2088353393664205241-a2aa2e0e.md` — origin: https://x.com/mattpocockuk/status/2088353393664205241
- `sources/mattpocock/twitter/https-x.com-poteto-status-2089067865098113024-1e62ec24.md` — origin: https://x.com/poteto/status/2089067865098113024
