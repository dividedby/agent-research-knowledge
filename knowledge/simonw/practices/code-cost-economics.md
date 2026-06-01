# Code Cost Economics

Simon Willison argues that understanding the new economics of code generation is the biggest challenge in adopting agentic engineering practices.

## The Fundamental Shift

**Writing code is cheap now.** Code has always been expensive - producing a few hundred lines of clean, tested code takes most developers a full day or more. Engineering habits at macro and micro levels are built around this constraint.

### Macro Level Changes
- Extensive time spent designing, estimating, and planning projects to ensure expensive coding time is used efficiently
- Product features evaluated based on value provided *in exchange for development time*
- Features need to earn development costs many times over to be worthwhile

### Micro Level Changes  
- Hundreds of daily decisions based on available time and anticipated tradeoffs
- Questions like: Should I refactor for elegance if it adds an hour? Write documentation? Test edge cases? Build debug interfaces?

Coding agents dramatically drop the cost of typing code, disrupting existing intuitions about which trade-offs make sense. Parallel agents make evaluation even harder since one human can implement, refactor, test, and document code simultaneously across multiple places.

## Good Code Still Has Costs

Delivering new code has dropped to almost free, but delivering *good* code remains significantly more expensive. Good code means:

- **Works correctly**: Does what it's meant to do, without bugs
- **Verifiable**: We know it works through confirmation steps  
- **Solves right problem**: Addresses actual requirements
- **Handles errors gracefully**: Covers more than just happy path with informative error messages
- **Simple and minimal**: Does only what's needed in maintainable way
- **Protected by tests**: Works now and guards against future regressions
- **Appropriately documented**: Reflects current state, updates with changes
- **Affords future changes**: Maintains YAGNI while not making future changes unnecessarily hard
- **Quality attributes**: Accessibility, testability, reliability, security, maintainability, observability, scalability, usability as appropriate

Coding agent tools can help with most of this, but substantial burden remains on the developer to ensure produced code meets quality standards for the project.

## Building New Habits

The challenge is developing new personal and organizational habits responding to agentic engineering affordances and opportunities. These best practices are still being figured out across the industry.

Current recommendation: Second guess instincts. When instinct says "don't build that, it's not worth the time," fire off a prompt anyway in an asynchronous agent session where the worst outcome is checking ten minutes later to find it wasn't worth the tokens.

*Sources: [Writing code is cheap now](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)*