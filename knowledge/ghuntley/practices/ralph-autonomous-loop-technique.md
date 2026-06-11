# Ralph autonomous loop technique

Geoff Huntley originated the "Ralph" autonomous loop technique—a fundamental approach to working with coding agents that treats everything as a programmable loop. Rather than building software vertically "brick by brick," Ralph embraces the mindset that computers can be programmed through autonomous loops.

## Core philosophy

Ralph is a monolithic orchestrator pattern where you "allocate the array with the required backing specifications and then give it a goal then looping the goal." It's explicitly designed as a monolithic approach—like a single operating system process that scales vertically—rather than attempting complex multi-agent communication.

"While I was in SFO, everyone seemed to be trying to crack on multi-agent, agent-to-agent communication and multiplexing. At this stage, it's not needed... Ralph is monolithic. Ralph works autonomously in a single repository as a single process that performs one task per loop."

## The loop mindset

"Software is now clay on the pottery wheel and if something isn't right then i just throw it back on the wheel to address items that need resolving."

Key principles:
- Everything becomes a loop rather than linear development
- Watch the loop actively—that's where personal development and learning occurs
- When you see a failure domain, put on your engineering hat and resolve it permanently
- The pattern is generic and can be used for all tasks through context engineering

## Implementation approaches

Ralph can be executed in multiple ways:
- **Manual prompting**: Running the loop manually via prompting
- **Semi-automated**: Automation with pause points requiring CTRL+C to progress
- **Fully automated**: Complete autonomous operation while AFK (Away From Keyboard)

"In practice this means doing the loop manually via prompting or via automation with a pause that involves having to press CTRL+C to progress onto the next task. This is still ralphing as ralph is about getting the most out how the underlying models work through context engineering."

## Ralph in practice: The cursed compiler

Huntley demonstrated Ralph's power by running Claude in a continuous loop for three months with a single prompt: "Hey, can you make me a programming language like Golang but all the lexical keywords are swapped so they're Gen Z slang?"

This resulted in "cursed," a complete programming language with:
- Compiler with interpreted and compiled modes
- LLVM-based binary generation for Mac, Linux, Windows
- Editor extensions for VSCode, Emacs, Vim
- Standard library packages
- Treesitter grammar

"For the last three months, Claude has been running in this loop with a single goal: 'Produce me a Gen-Z compiler, and you can implement anything you like.'"

## Watching and learning from the loop

"It's important to *watch the loop* as that is where your personal development and learning will come from."

The approach emphasizes active observation and intervention:
- Monitor loop execution for failure patterns
- Apply engineering discipline to prevent recurring issues
- Use failures as learning opportunities for system improvement
- Maintain the role of engineer/orchestrator rather than passive observer

## Economic implications

"Software can now be developed cheaper than the wage of a burger flipper at maccas and it can be built autonomously whilst you are AFK."

Ralph enables:
- Development while away from keyboard
- Concurrent work during meetings or other activities
- Dramatic reduction in development costs
- Automation of entire job functions

Sources: [everything is a ralph loop](https://ghuntley.com/loop/) — `sources/ghuntley/blog/https-ghuntley.com-loop-5a016131.md`, [i ran Claude in a loop for three months](https://ghuntley.com/cursed/) — `sources/ghuntley/blog/https-ghuntley.com-cursed-e03af03c.md`