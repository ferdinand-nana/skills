# Ponytail Debt

Every deliberate ponytail shortcut is marked with a `ponytail:` comment naming
its ceiling and upgrade path. This collects them into one ledger so a deferral
can't quietly become permanent.

## Scan

Grep the repo for comment markers, skipping node_modules, .git, and build output:
`grep -rnE '(#|//) ?ponytail:' .`

Each hit is one ledger row.

## Output

One row per marker, grouped by file:
`<file>:<line> — <what was simplified>. ceiling: <the limit named>. upgrade: <the trigger to revisit>.`

Flag any `ponytail:` comment that names no upgrade path or trigger with a
`no-trigger` tag — those rot silently.

End with `<N> markers, <M> with no trigger.`
Nothing found: `No ponytail: debt. Clean ledger.`

## Boundaries

Reads and reports only, changes nothing. One-shot.