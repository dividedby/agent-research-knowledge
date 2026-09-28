# Gate deploys by branch pattern; let the platform's own skip logic decide the rest

When a deploy platform already knows how to skip work it doesn't need to do,
building a custom script to make that decision is redundant risk, not extra
control. `course-video-manager`'s Vercel setup — one project per deployable
directory, each with its own Root Directory — relies entirely on Vercel's
**built-in unaffected-project skipping** to decide *what* to deploy, and
deliberately configures **no Ignored Build Step**: `turbo-ignore` (the
Turborepo-native way to write one) is deprecated, and the platform's native
skip doesn't consume a concurrent build slot the way a custom step's own build
invocation would. If a custom check is ever needed later, the documented
fallback is `turbo query affected` — read the answer, don't reimplement the
question.

## `git.deploymentEnabled` decides *when*, as a separate axis from *what*

A later addition gates *which branches deploy at all*: `apps/remote/vercel.json`
sets `git.deploymentEnabled` to `{ "**": false, "main": true }`, so a push to
any branch other than `main` builds nothing — no Preview Deployment gets
created for an open PR. Production still deploys on every merge to `main`,
because a branch matching two rules in the map deploys if *either* is `true`.
This matters specifically in a repo where most PRs are agent-opened (see
[[label-driven-agent-ci-pipeline]]): without the gate, every agent-authored
branch would spend a Preview Deployment build, whether or not anyone was going
to look at it.

The glob is `**`, deliberately not `*` — `*` doesn't match a slash, so a
branch like `feat/thing` would still fall through and deploy. This is stated
as **the supported way to do per-branch control**: Vercel's dashboard has no
equivalent toggle, and the repo takes no Ignored Build Step to fake it.

## The general shape

Two separate deploy questions — *should this push build at all* and *is this
build's output actually new* — get two separate platform-native answers rather
than one bespoke script trying to hold both: a declarative branch-pattern map
answers the first, and the platform's own dependency-graph skip logic answers
the second. Reaching for a custom Ignored Build Step collapses both into one
place a human has to keep correct by hand; using the platform's two purpose-
built mechanisms means the correctness burden stays where the platform itself
already carries it.

## Sources

- `sources/mattpocock/course-video-manager/README.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/README.md (revision 2026-08-11, "Deploys": one Vercel project per deployable directory, built-in unaffected-project skipping, no Ignored Build Step because `turbo-ignore` is deprecated and native skipping doesn't consume a concurrent build slot, `turbo query affected` as the documented fallback)
- `sources/mattpocock/course-video-manager/README.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/README.md (revision 2026-09-26, "Only `main` deploys": `apps/remote/vercel.json`'s `git.deploymentEnabled` map, the `**` vs `*` glob distinction, no Preview Deployment for an open PR)
