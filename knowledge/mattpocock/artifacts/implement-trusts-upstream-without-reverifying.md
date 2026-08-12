# A build-step skill trusts its upstream input completely — and never re-validates it

`implement` is the skill in the main chain (`grill-with-docs → to-spec →
to-tickets → implement → code-review`) that turns an already-decided ticket or
spec into a commit: read it, drive `tdd` at the seams, typecheck, run the
suite once, run `code-review`, commit. Its defining trait is what it refuses
to do — there is no interview, no clarifying round, no proposal of a different
approach. Whatever was settled upstream is the input, and the skill's whole
job is turning that into code. That is what separates it from telling a fresh
agent to "build this", which will happily redesign the work while building it.

## Trusting the input completely means never checking its shape

Because `implement` doesn't re-validate what it's handed, a badly-structured
ticket — one sliced horizontally by layer instead of vertically as a tracer
bullet, or one whose seams were never actually agreed upstream — gets built
exactly as written rather than caught and pushed back. The "pre-agreed seam"
precondition is the sharpest example: `implement` assumes the seams were
settled in the spec, but nothing *inside* implement agrees them — that's
`tdd`'s job, and `tdd` refuses to write a test at an unconfirmed seam. If the
seam was never actually agreed anywhere upstream — no spec, or a spec that
skipped the seam conversation — the precondition simply never fires, and the
run quietly degrades into "just write the code" with no test discipline at
all, and no error surfaces to say so. A downstream skill built to trust its
input can only be as disciplined as the skill that produced that input; it has
no mechanism of its own to detect a malformed one.

## What "done" doesn't include

`implement` ends at the commit. It never touches the originating ticket or
issue — it doesn't close it, doesn't check off acceptance criteria, and
doesn't act on `code-review`'s findings from the pass it just ran internally.
This isn't a tracker-integration bug; it's a scope boundary the skill holds on
every tracker it's been tested against. The practical cost compounds on a
dependency chain specifically: an upstream ticketing skill defines the
frontier of unblocked work as "tickets whose blockers are all closed," so if
nothing ever gets closed after `implement` runs, nothing downstream ever
becomes visibly takeable — the trust boundary between "build the code" and
"update the tracker" has to be closed by the caller, every time.

## The commit-straight-to-branch default has no escape valve, and no support for parallel runs

`implement` commits straight to whatever branch is checked out — it doesn't
create one, doesn't ask, and has no built-in PR mode; overriding either
behaviour means saying so explicitly in the invocation or editing the local
skill copy. More load-bearing: it has no concept of a second `implement`
session running concurrently in the same checkout. Because sessions share one
working directory, one index, and one `HEAD`, running several at once is worse
than merely unsupported — one field report in a single afternoon saw a
`git commit --amend` in one session land on another session's commit, a stash
vanish from `refs/stash`, and commits land on the wrong branch, all from
sessions that had no way to know about each other. Git worktrees are the
community workaround, with the caveat that `refs/stash` is shared *across*
worktrees too, so worktrees alone don't close the gap. A build-step skill that
assumes exclusive ownership of the working tree is a reasonable design — but
only if every caller actually honours that assumption, since nothing in the
skill itself checks or enforces it.

## Sources

- `sources/mattpocock/aihero/https-www.aihero.dev-skills-implement-da314e96.md` — origin: https://www.aihero.dev/skills-implement
