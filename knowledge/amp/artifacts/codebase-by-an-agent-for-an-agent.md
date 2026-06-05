# A codebase by an agent, for an agent

Counterintuitive design lesson: a codebase the agent can navigate *fast* is one
where it chose the names, file layout, and structure — not one where the human
imposed their taste. Let the agent decide naming and organization, and it builds
something it is then exceptionally good at working in.

The mechanism: when an agent reaches for a name or a file location, its "hand is
guided by training data" — it picks the *statistically most probable* choice. If
a human overrides that ("I know better — rename `present()` to `swapScreens()`"),
the agent later reaches for the probable name, fails to find it, spins its
wheels, runs extra loops, burns tokens, and eventually rediscovers the function
under the human's idiosyncratic name. You've forced it to recall what *past-you*
would have called things instead of what *past-it* would have — and it can't read
your mind, only its weights.

Take your hands off the wheel and the opposite happens. Amp's TUI framework (a
TypeScript port of a Zig library) is ~90% agent-written; once the author stopped
correcting names and layout, the agent "went faster and for longer," chose names
and structures the human wouldn't have, used unusual OOP/generics patterns — and
became *strikingly* good at using the result. It can extend an undocumented
framework that doesn't fit in one context window: add scrollbars to a modal, work
the animation subsystem, fix a missing event handler on the fly.

Why it works, conceptually: the agent recognizes *concepts* through syntax. This
framework has a Flutter-shaped API (Widgets, StatefulWidgets, Intents, Bindings);
the model has enough Flutter in its weights to see those concepts even across
Dart → Zig → TypeScript. A codebase left in the agent's preferred shape sits at
an equilibrium between *what the human wants*, *what the concepts require*, and
*what the model judges most likely* — so the agent never has to second-guess what
something is called or why it works the way it does.

The practical rule: stop telling the agent how to name things or where to put
them. The satisfaction of a "nice-looking" codebase by *your* taste is real but
costs agent throughput; the most probable layout is the one the agent navigates
best.

## Sources

- `sources/amp/chronicle/https-ampcode.com-notes-by-an-agent-for-an-agent-734cc269.md` — origin: https://ampcode.com/notes/by-an-agent-for-an-agent
