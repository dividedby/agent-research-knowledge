# Split the interface: a CLI for the agent, a live-reloading view for the human

For non-coding work, Matt reports converging repeatedly on the same shape: a
**CLI exposed to an agent like Claude Code for edits**, paired with a
**custom live-reloading interface for viewing**. The agent gets full
programmatic control over everything through the CLI; the human gets to watch
and review in whatever presentation is most comfortable, decoupled from
whatever shape the agent's edits take on disk. He's using the pattern for
course creation now and reports it "rocks." This generalizes
`agent-facing-cli-as-glossary-surface`'s read-only CLI idea into a full write
interface, deliberately split from the human's read interface rather than
sharing one surface for both.

## Closing the loop: pointing the agent at what the human sees

The split creates an obvious gap: if a human spots something worth fixing in
the live view, how do they communicate *which* thing to the agent, which
never sees the rendered view directly? Matt's answer is a **"copy link"**
control in the live view that copies a URI identifying the exact thing being
looked at — that URI is what gets pasted into the agent's prompt. This is the
same instinct as passing a file path or line reference to an agent, adapted
for a rendering surface that has no filesystem location of its own: the live
view manufactures an addressable identifier so the human's pointing gesture
survives the handoff to the CLI-driven agent.

## Sources

- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080277204970143986-87fdfd02.md` — origin: https://x.com/mattpocockuk/status/2080277204970143986
- `sources/mattpocock/twitter/https-x.com-mattpocockuk-status-2080290080543895635-b07b3928.md` — origin: https://x.com/mattpocockuk/status/2080290080543895635
