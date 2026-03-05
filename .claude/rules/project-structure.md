# Rule: Project Structure

## Repository Layout

```
hands-on-claude/
├── .claude/
│   ├── CLAUDE.md          # Project-level Claude instructions
│   └── rules/             # Granular rule files (this directory)
├── <project-name>/        # Subdirectory for multi-file projects
│   ├── index.html
│   └── ...
├── <experiment>.html      # Single-file experiments live at root
└── README.md              # Always present, always up to date
```

## Adding a New Project

1. **Single-file experiment** → place directly at repo root as `<descriptive-name>.html`.
2. **Multi-file project** → create a subdirectory: `<project-name>/index.html`.
3. **Always update `README.md`** to add an entry for the new project with a one-line description.
4. **Never nest** more than two levels deep without a strong reason.

## File Naming
- Use `kebab-case` for all file and directory names.
- HTML files: `index.html` inside a folder, or `<topic>.html` at root.
- Assets: place in `<project>/assets/` — separate `images/`, `fonts/`, `icons/` subdirectories as needed.

## What NOT to Add
- `node_modules/` — no local installs unless a project explicitly requires a build step.
- `.env` files — never commit secrets or API keys.
- Auto-generated build output (`dist/`, `out/`, `.next/`) — add to `.gitignore` if they appear.
- Duplicate or backup files (`index-old.html`, `index-copy.html`).

## .gitignore Baseline
If a `.gitignore` is ever needed, include at minimum:
```
node_modules/
.env
.env.local
dist/
.DS_Store
```
