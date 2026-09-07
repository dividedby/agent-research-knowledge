# Lights-off autonomy drowns in slop; the fix is to read code again

Running an agent loop fully unattended for long enough eventually produces unmaintainable
slop, even when the tests keep passing and the tasks keep completing — those counters
don't track whether the code stays easy to change (cf.
*software-factory-metrics-miss-maintainability*). HumanLayer ran a "lights-off" factory
this way for five months before the accumulated output caught up with them and they
reset their own advice.

The correction wasn't more process layered on top; it was reinstating the human step
they'd stripped out — read the code, not just the plan — paired with two other
adjustments: seek leverage (spend attention where it compounds, not everywhere) and
decompose broad "skills" into narrower "workflows." This is the same team that argues
elsewhere for reviewing research and plans instead of code (*review-research-and-
plans-not-code*) and for trusting a good spec in a dumb loop (*ralph-dumb-loops-and-
declarative-specs*) — the correction shows neither substitutes indefinitely for
periodically checking the actual code once a loop has been running unattended long
enough.

## Sources

- `sources/humanlayer/blog/https-www.humanlayer.dev-blog-humanlayer-resources-56fd92bf.md`
  — origin: https://www.humanlayer.dev/blog/humanlayer-resources
