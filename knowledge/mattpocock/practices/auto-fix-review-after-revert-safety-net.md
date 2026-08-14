# Auto-fix code-review findings; review the diff after, not each finding before

Asked how to follow up once `/code-review` surfaces findings — reviewers
default to walking through each one individually and deciding whether to act
on it — Matt's answer skips that gate entirely: "IMO I would just
automatically get it to fix anything it finds." The correspondent pushed
back, wanting to stay more in the loop; Matt's response names the actual
safety net: "You still can, you just read the review afterwards. You can
always reverse the commit." Staying in the loop doesn't require blocking on
each finding before a fix lands — the checkpoint just moves from *before*
the fix (a one-by-one approval gate) to *after* it (reading the diff, with
`git revert` as the undo).

## Why after beats before here

A pre-fix, one-by-one gate treats every finding as equally risky and pays its
cost up front on all of them, whether or not anything ends up wrong. A
post-fix review pays that cost only when a genuine mistake justifies backing
it out — cheap, because `/code-review` findings are exactly the kind of
change a single commit can cleanly undo, unlike a deploy or a data migration.
This mirrors the general shape of `/code-review`'s own place in the chain
([[review-skill-two-axis-with-smell-baseline]]): the skill has no convergence
guarantee and is meant to produce a list of leads to act on and stop, not a
loop to run to exhaustion. Auto-fixing a pass's findings and inspecting the
result afterward fits that "act, then stop" posture better than re-litigating
each finding before it's applied.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087858577859871121-b4e285ea.md` — origin: https://x.com/mattpocockuk/status/2087858577859871121
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2087884688857657592-7f7847d2.md` — origin: https://x.com/mattpocockuk/status/2087884688857657592
