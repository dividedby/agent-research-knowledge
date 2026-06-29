# Display: a swappable rendering backend, with line vs. chunk as a first-class split

Sandcastle's orchestrator never touches a terminal directly. All run output —
status lines, spinners, tool calls, the agent's own prose — goes through a single
tagged service, `Display`, whose `DisplayService` interface (`intro`, `status`,
`spinner`, `summary`, `taskLog`, `text`, `textChunk`, `toolCall`) is implemented
by three interchangeable Effect layers chosen at the seam, not in the call site:

- **`ClackDisplay`** — the interactive TTY: spinners, styled notes, stepped tool
  calls via `@clack/prompts`.
- **`FileDisplay`** — appends a plain-text transcript to a log file (each run
  delimited by an ISO timestamp), for AFK / headless runs with no terminal.
- **`SilentDisplay`** — records every call as a structured `DisplayEntry` into a
  `Ref` array instead of emitting anything, so tests assert *what was displayed*
  as data rather than scraping stdout.

The orchestrator just `yield* Display` and calls `display.status(...)`; which
backend renders is a layer decision. This is the same own-the-interface stance as
the rest of the harness ([[thin-fail-fast-harness]]): the rendering target is a
provided capability, not a hardcoded `console.log`.

## Streamed prose needs a different primitive than logged lines

The interface deliberately splits `text` (a message that *is* a line) from
`textChunk` (a raw streaming fragment with **no implied line break**). Token-by-
token agent output arrives as fragments that must flow together as contiguous
prose; if each chunk were a line, the transcript would be one word per line. So
the orchestrator routes buffered agent deltas through `display.textChunk`, while
structured events (status, tool calls, summaries) stay line-oriented.

That split forces the backend to track cursor state. `FileDisplay` keeps a
`midLine` flag: `appendRaw` (chunk) leaves it set when a fragment lacks a trailing
newline, and every line-oriented entry consults it to emit a leading `\n` first —
so a tool call or status line never lands glued to the tail of half-streamed
prose. The orchestrator cooperates from its side: it wraps deltas in a
`TextDeltaBuffer` and **flushes the buffer before emitting a tool call**, so the
partial line is committed before the next structured entry. Readable interleaving
of free-form stream and structured log is a property the *harness* engineers, not
something the display layer gets for free.

The same agent deltas are also forwarded to an `AgentStreamEmitter` (typed
`text` / `toolCall` / `raw` events), so a structured consumer can subscribe to the
run independently of whichever human-facing Display backend is mounted — display
and machine-readable stream are separate sinks fed from one parse loop.

## Sources

- `sources/mattpocock/sandcastle/src-Display.ts-18d4835a.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/src/Display.ts
- `sources/mattpocock/sandcastle/src-Orchestrator.ts-686b2711.md` — origin: https://github.com/mattpocock/sandcastle/blob/8da999eca700c0f1f8478b29d571b769ec1f0179/src/Orchestrator.ts
