# Rule: Git Workflow

## Core Rules
- **Never auto-commit.** Always ask the user before creating any git commit.
- **Never auto-push.** Pushing to remote requires explicit user confirmation every time.
- **Never force-push** (`--force`) under any circumstances without explicit user instruction.
- **Never skip hooks** (`--no-verify`) unless the user explicitly asks.

## Commit Messages
Follow Conventional Commits format:

```
<type>(<scope>): <short summary>

[optional body]
```

**Types:**
| Type     | When to use                                      |
|----------|--------------------------------------------------|
| `feat`   | Adding a new project or feature                  |
| `fix`    | Fixing a bug or broken layout                    |
| `style`  | CSS/design changes with no logic change          |
| `refactor` | Restructuring without changing behavior        |
| `docs`   | README, CLAUDE.md, or comments only              |
| `chore`  | Tooling, config, `.gitignore`, etc.              |

**Examples:**
```
feat(landing-page): add animated hero section with floating particles
style(landing-page): update color palette to match Claude brand
docs: add project-structure rule to .claude/rules
```

## Branching
- Default work happens on `main` for this learning repo.
- If experimenting with a breaking change, suggest creating a branch: `experiment/<topic>`.
- Branch names: `kebab-case`, descriptive, no more than 5 words.

## What to Stage
- Stage specific files by name — never use `git add .` or `git add -A` blindly.
- Verify with `git diff --staged` before committing.
- Never stage `.env`, secrets, or large binary assets.
