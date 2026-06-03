# Remote Terminal Supervision

Long-running agents need a check-in channel from anywhere, so the move is to expose the agent's terminal to a browser without any SSH setup. VibeTunnel does this with a small native process-management binary that wires a running session to the web: a regular file holds stdout so it's tailable and observable, while a named pipe carries stdin for bidirectional control. The session streams to an Xterm.js front-end over Server-Sent Events.

The transport choice is deliberate. SSE is picked over WebSockets for its simplicity, proxy-friendliness, and built-in reconnect — properties that matter when you're checking in from a flaky phone connection. The cost is the HTTP/1.1 ceiling of six connections per domain, which forces multiplexing many sessions over a shared stream rather than one connection each.

The enabling idea underneath is keeping the *same* session alive in two terminals at once, with resize and scrollback synchronized, so observing remotely doesn't fork the session or disturb the agent. You can watch what the agent is doing and redirect it mid-task from a browser tab on your phone.

This extends [[stay-in-the-loop-active-steering]] across distance: active steering only works if you can see and reach the loop, and a browser terminal makes that possible from anywhere without provisioning access. It complements the dashboard-style visibility of [[agent-status-in-terminal-titles]] — one tells you *what* the fleet is doing, this lets you *intervene*.

## Sources
- /home/runner/work/agent-research/agent-research/sources/steipete/blog/https-steipete.me-posts-2025-vibetunnel-turn-any-browser-int-d1bfe9ac.md — https://steipete.me/posts/2025/vibetunnel-turn-any-browser-into-your-mac-terminal/
