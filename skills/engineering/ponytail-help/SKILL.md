# Ponytail Help

## Levels

| Level | Shortcut | What it does |
|-------|----------|--------------|
| **Lite** | `Ctrl+Alt+Shift+L` | Build what's asked, name the lazier alternative in one line. |
| **Full** | `Ctrl+Alt+Shift+F` | The ladder enforced: YAGNI → stdlib → native → one line → minimum. Default. |
| **Ultra** | `Ctrl+Alt+Shift+U` | YAGNI extremist. Deletion before addition. Challenges requirements. |
| **Off** | `Ctrl+Alt+Shift+O` | Disable ponytail rules. |

Level sticks until changed or IDE restart.

## Skills

| Skill | Shortcut | What it does |
|-------|----------|--------------|
| **ponytail** | `Ctrl+Alt+Shift+P` | Inject/update ponytail rules into Copilot instructions |
| **ponytail-review** | `Ctrl+Alt+Shift+R` | Over-engineering review of current changes |
| **ponytail-audit** | `Ctrl+Alt+Shift+A` | Whole-repo over-engineering audit |
| **ponytail-debt** | `Ctrl+Alt+Shift+D` | Harvest ponytail: comments into debt ledger |
| **ponytail-gain** | `Ctrl+Alt+Shift+G` | Show measured-impact scoreboard |
| **ponytail-help** | `Ctrl+Alt+Shift+H` | This card |

## How it works

The plugin writes ponytail rules into `.github/copilot-instructions.md`.
GitHub Copilot reads this file as custom instructions for every prompt.
Switching levels auto-updates the file — Copilot picks up the change immediately.

## Deactivate

Tools → Ponytail → Level: Off (or `Ctrl+Alt+Shift+O`)
This clears the ponytail section from copilot-instructions.md.