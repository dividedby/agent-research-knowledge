# Anti-Patterns to Avoid

Simon Willison identifies behaviors that are anti-patterns in agentic engineering - things that undermine effective collaboration and quality code delivery.

## Inflicting Unreviewed Code on Collaborators

The most common and deeply frustrating anti-pattern: **Don't file pull requests with code you haven't reviewed yourself**.

### The Problem

Opening PRs with hundreds or thousands of lines of agent-produced code without personal review delegates the actual work to other people. Collaborators could have prompted an agent themselves - what value are you providing?

### Professional Standards

If you put code up for review, you need confidence it's ready for other people's time. The initial review pass is your responsibility, not something to farm out to others.

## Characteristics of Good Agentic PRs

A good agentic engineering pull request has:

- **Functional code**: The code works, and you are confident it works. Your job is to deliver code that works.
- **Manageable scope**: Small enough to review efficiently without excessive cognitive load. Several small PRs beats one big one.
- **Context and explanation**: Higher level goals the change serves. Link to relevant issues or specifications.
- **Validated descriptions**: Agents write convincing PR descriptions, but you must review these too. It's rude to expect others to read text you haven't validated yourself.

## Evidence of Due Diligence

Given how easy it is to dump unreviewed code on people, include evidence you've invested the work:

- Notes on manual testing performed
- Comments on specific implementation choices  
- Screenshots and video of features working
- Demonstrations that reviewer time won't be wasted

This demonstrates respect for collaborators' time and professional engineering standards.

*Sources: [Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)*