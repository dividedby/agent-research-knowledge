# Context Compression and Handoff Mechanics

Matt developed the `/handoff` skill to split concerns across independent agent sessions while preserving relevant context. This technique enables focused work sessions without losing critical information, addressing the context window smart zone limitations.

## The Smart Zone Problem

Context windows have smart zones (~120k tokens) and dumb zones. Early in the context window, agents perform much better because attention relationships aren't strained. As conversations develop, responses gradually get dumber due to diffuse attention across too many tokens.

This creates a practical limit: despite advertised massive context windows, only about 120k tokens are available for truly smart work.

## Handoff vs Compact

**`/compact`** summarizes large conversations to move from dumb zone back to smart zone, useful for long-running single-threaded work like debugging. Creates layers of previous conversations like sediment.

**`/handoff`** takes specific slices of context relevant to different work and creates independent sessions. Enables splitting concerns without losing focus on either task.

The handoff approach allows: extending current session would dilute context working on two things simultaneously, while handoff keeps each session pure and focused on one concern.

## Handoff Document Structure

The skill compresses current session context into markdown documents containing:

**Purpose of next session** — Clear description of what the new session will accomplish  
**Relevant context** — Only information needed for the specific handoff task  
**Suggested skills** — Recommended skills to invoke in the next session  
**Pointers to artifacts** — References to existing files rather than duplicated content  

Documents are saved to the OS temporary directory as disposable working documents, not permanent documentation.

## Common Usage Patterns

**Out-of-scope discovery** — During feature work, notice refactoring opportunity. Handoff the refactor to separate session, keep current work pure.

**Prototype handoff** — During grilling sessions, identify things that need prototyping. Hand off to prototype session, compress learnings back to parent session.

**Cross-tool workflow** — Pass handoff documents between different AI coding tools (Claude Code → Copilot CLI → Codex) for tool-specific advantages.

## Design Principles

**Tool portability** — Use markdown format instead of native agent features for cross-agent compatibility  
**Avoid duplication** — Reference existing artifacts rather than copying content to prevent bloat  
**Redact sensitive information** — Strip out API keys, passwords, or PII from handoff documents  
**Disposable documents** — Save to temporary directories, not permanent project documentation  
**Purpose-tailored content** — Include only context relevant to the next session's specific goals  

## DIY Sub-Agent Pattern

Handoff creates a DIY sub-agent pattern: use a full context window for exploration, compress learnings into a handoff document, and pass insights back to the parent session. This enables complex exploration without bloating the main session's context.

## Sources

- /home/runner/work/agent-research/agent-research/sources/mattpocock/aihero/https-www.aihero.dev-skills-handoff-2afa3dc0.md