# Prompt templating with a hard data/code boundary

Sandcastle's `promptFile` templates support two interpolation features that look
alike but sit on opposite sides of a trust boundary: `{{KEY}}` argument
substitution (inject a *value*) and `` !`command` `` shell expansion (run a
*command* and splice its stdout). The design's load-bearing rule is that **only
shell blocks written in the raw template by the template author are ever
executed** — any `` !`…` `` pattern that arrives *through* a substituted argument
is treated as inert text. This is what makes it safe to forward arbitrary,
untrusted content (issue titles, PR bodies, docs excerpts) into a prompt via
`promptArgs`.

## Why the naive ordering is a command-injection hole

Substitution and expansion compose in a fixed order: argument substitution runs
first (so `{{KEY}}` placeholders *inside* a shell block are filled before the
block runs — `` !`gh issue view {{ISSUE_NUMBER}} …` `` works). The trap is that
once an argument value is spliced in, a later, position-blind expansion pass
would happily execute any `` !`…` `` the value happened to contain. A caller
piping an issue body through `promptArgs` could thereby trigger arbitrary host
command execution — the changelog records this as a real fixed bug
(`6bc4d74`), not a hypothetical.

## How the boundary is enforced: mark the trusted blocks, strip forgeries

The mechanism is a **provenance marker**, not an escaping pass. Before
substitution, every shell block *in the raw template* is tagged with an internal
`SHELL_BLOCK_MARKER` sentinel; the downstream preprocessor only executes blocks
carrying that mark. Two details make it airtight:

- **Pre-strip the raw input.** Any sentinel already present in the incoming
  template is removed first, so a malicious template can't pre-forge the marker.
- **Sanitize every substituted value.** The same sentinel is stripped from each
  arg value before it is spliced in, so a value can't smuggle the mark in either.

The net effect: the marker can only originate from Sandcastle's own tagging of
author-written blocks. A `` !`rm -rf ~` `` that arrives via an argument has no
marker, was never author-written, and is passed to the agent as literal text.
Code and data are distinguished by *where the token came from*, not by trying to
sanitize the token's contents — the robust shape for an injection defense.

## The same instinct at the inline-prompt seam

The data/code split shows up again one level out: inline `prompt: "…"` strings
skip the whole template pipeline and are delivered verbatim (no `{{KEY}}`, no
`` !`…` ``), and passing `promptArgs` alongside an inline prompt is a hard error
rather than a silent no-op — the harness refuses an ambiguous request instead of
guessing. The substitution feature follows the prompt's *source*
([[thin-fail-fast-harness]]): only `promptFile`-sourced text is template-active, so
forwarded content that happens to contain `{{…}}` or `` !`…` `` can never trip a
scanner it was never meant to reach.

## Sources

- `sources/mattpocock/sandcastle/src-PromptArgumentSubstitution.ts-58c145ee.md` — origin: github.com/mattpocock/sandcastle (src/PromptArgumentSubstitution.ts)
- `sources/mattpocock/sandcastle/CHANGELOG.md.md` — origin: github.com/mattpocock/sandcastle (CHANGELOG.md)
- `sources/mattpocock/sandcastle/README.md.md` — origin: github.com/mattpocock/sandcastle (README.md)
