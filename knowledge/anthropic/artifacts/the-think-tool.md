# The "think" tool: a mid-loop scratchpad

The "think" tool gives the agent a no-op tool whose only effect is to append a
thought to the log — a designated space to stop and reason *during* response
generation, in the middle of a tool-use chain. It obtains no new information and
changes no state; it just creates room to think.

It is distinct from **extended thinking**, and the distinction defines when each
applies. Extended thinking is reasoning *before* the agent acts — deep up-front
planning, good for coding/math or simple non-sequential tool use. The "think"
tool is reasoning *after* results arrive — it shines when the agent must process
external information it didn't have from the query alone: long chains of complex
tool calls, careful analysis of tool outputs, policy-heavy environments, and
sequential decisions where each step builds on the last and mistakes are costly.
(Anthropic now recommends extended thinking over a dedicated think tool in most
cases, as extended thinking has improved — but the *pattern* and its scoping
remain instructive.)

Two implementation findings:
- **Pair it with prompting, and put the guidance in the system prompt.** The
  unprompted tool helps over baseline, but the large gains came from a system
  prompt giving worked examples of *what to iterate over* inside the think step
  (list applicable rules, check required info collected, verify policy
  compliance). For long/complex guidance, the system prompt beats the tool
  description — it gives broader context to integrate.
- **It's low-risk, not universal.** It adds prompt/output tokens but has minimal
  downside: it does nothing unless the model chooses to use it, and doesn't
  interfere with existing tools. It offers no benefit for non-sequential tool use
  or simple instruction-following — scope it to the costly, policy-heavy, chained
  cases. Its value was established on τ-bench and SWE-bench, not asserted.

## Sources
- `sources/anthropic/engineering/https-www.anthropic.com-engineering-claude-think-tool-962c879d.md` — https://www.anthropic.com/engineering/claude-think-tool
