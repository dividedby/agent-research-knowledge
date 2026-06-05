# Make the bad state impossible, not handled

The single most reliable way LLM-authored code grows needless complexity:
**models see a local failure and try to locally defend against it.** Tell a
clanker "this malformed session log crashes the reader" and it will add a
tolerant reader, then a fallback, then a migration, then debug output, then
tests for all of it — none necessarily wrong in isolation, but the wrong move
for the system. The model assumes no invariant exists and bends the system to
swallow malformedness, blowing up complexity in the process.

Ronacher's maintainer-side rule, reinforced by working on Pi's code: **almost
always the correct fix is not to handle the bad state but to make it
impossible.** This matters most for persisted, long-lived data — Pi's session
logs are opened, branched, compacted, exported, shared, and analyzed, so the
goal is to *never write bad data*, not to read every flavor of bad data back.
A permissive reader is the trap; the invariant is the fix.

Because models default to local defense, the maintainer's job becomes
**repeatedly pulling the conversation back to the global invariant** — laborious
work that's harder than it should be, since cheap local workarounds are exactly
what the machine reaches for. The same instinct extends past a single codebase:
when an upstream gateway misbehaves, the right answer is often to make the
*upstream* behave correctly so everyone benefits, not to paper over it locally.
Mario's refusal to let Pi paper over every misconfigured gateway is the
discipline being preserved. Letting the agent roam free without this pressure is
how you accumulate a codebase of isolated local defenses against every possible
misbehavior.

This is the global-invariant counterpart to the structural rules in
[[shape-the-codebase-for-local-reasoning]], and a concrete instance of why
[[agent-as-collaborator-you-stay-accountable]] — the judgement about *where* a
fix belongs is exactly the part you can't cede.

## Sources
- /home/runner/work/agent-research/agent-research/sources/ronacher/blog/https-lucumr.pocoo.org-2026-5-24-pi-oss-0c3d1fdf.md — https://lucumr.pocoo.org/2026/5/24/pi-oss/
