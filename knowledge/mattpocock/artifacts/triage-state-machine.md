# Triage state machine with role-based transitions

The `triage` skill implements issue workflow as an explicit state machine with two categories of labels: **category roles** (`bug`, `enhancement`) and **state roles** (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). Every triaged issue carries exactly one of each, and state transitions follow defined rules that make the workflow predictable for both humans and agents.

## State transition discipline

Issues move through a deliberate progression: unlabeled → `needs-triage` → (`needs-info` ↔ `needs-triage`) → terminal states (`ready-for-agent`, `ready-for-human`, `wontfix`). The `needs-info` state can return to `needs-triage` when the reporter provides requested details, creating the only bidirectional transition in the machine. All other moves are forward-only.

The maintainer can override any transition, but unusual transitions are flagged for confirmation rather than executed silently — the state machine is a guide with human escape hatches, not a prison.

## Grilling as state refinement

When issues need fleshing out, the triage process invokes a `/grill-with-docs` session before making terminal state decisions. This is the editorial bridge between raw issue reports and the precise specifications that `ready-for-agent` demands — grilling transforms `needs-triage` into either `ready-for-agent` (with an agent brief), `ready-for-human` (with reasoning about why delegation fails), `needs-info` (with specific questions), or `wontfix` (with `.out-of-scope/` documentation).

## Refusal with explanation

Every state transition that fails preconditions posts an explanation comment and moves to the appropriate blocked state rather than proceeding incorrectly. The pattern is "refuse → explain why → guide toward resolution" — never silent failure. This makes the state machine safe for autonomous operation because every dead end is documented and reversible.

## Triage notes template for continuity

The `needs-info` state uses a structured comment template that separates "what we've established so far" from "what we still need from you", ensuring that prior grilling work survives across multiple maintainer sessions. When triage resumes, all resolved questions are visible and won't be re-asked, while outstanding questions remain actionable.

## Domain-specific label naming

While the canonical state vocabulary is `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`, specific repositories can adapt the naming to match their domain language. In `course-video-manager`, the `ready-for-agent` state is spelled **`Sandcastle`** to align with that project's automation framework. The label functions identically — it triggers the same automation and state transitions — but uses vocabulary that resonates with that codebase's context.

This naming flexibility maintains the state machine's discipline while allowing projects to surface their automation in terms users expect. The core workflow remains unchanged; only the presentation adapts to the project's ubiquitous language.

## Sources

- `sources/mattpocock/skills-repo/skills-engineering-triage-SKILL.md-c4a91ff1.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/triage/SKILL.md
- `sources/mattpocock/skills-repo/skills-engineering-triage-AGENT-BRIEF.md-5b16e7c5.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/triage/AGENT-BRIEF.md
- `sources/mattpocock/skills-repo/skills-engineering-triage-OUT-OF-SCOPE.md-a52875a4.md` — origin: https://github.com/mattpocock/skills/blob/e3b90b5238f38cdea5996e16861dcae28ef52eda/skills/engineering/triage/OUT-OF-SCOPE.md
- `sources/mattpocock/course-video-manager/CLAUDE.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/CLAUDE.md