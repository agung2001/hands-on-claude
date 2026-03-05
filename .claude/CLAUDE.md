# CLAUDE.md — hands-on-claude

This file gives Claude Code context about this project's purpose, conventions, and preferences.

## Project Purpose

A personal learning repo for exploring **Claude Code** capabilities hands-on.
Each project inside is a small, self-contained experiment — built with Claude Code during learning sessions.

## Project Structure

```
hands-on-claude/
├── .claude/
│   └── CLAUDE.md        # This file
├── index.html           # 01: Claude Code landing page (Tailwind CSS, dark theme)
└── README.md            # Project overview and index
```

New projects may be added as standalone files or subdirectories as learning progresses.

## Conventions

- **No build step** unless explicitly needed — prefer CDN-based setups (Tailwind CDN, etc.) for quick experiments
- **Dark theme** is the default for any UI work in this repo
- **One file per experiment** when possible — keep things self-contained and easy to open directly in a browser
- **README.md** should be kept up to date with a list of all projects and what each demonstrates

## Coding Preferences

- Tailwind CSS via CDN for styling (no PostCSS/build pipeline unless the project requires it)
- Vanilla JS over frameworks for simple UI experiments
- Semantic HTML structure
- Mobile-first responsive design
- Animations via CSS keyframes + Tailwind `animation` config

## Claude Code Behavior

- **Do not auto-commit** — always ask before creating git commits
- **Do not push** to remote without explicit confirmation
- **Prefer editing existing files** over creating new ones unless a new experiment is being added
- Keep new experiments minimal and focused — avoid over-engineering
- Update `README.md` when a new project file is added

## Stack

| Layer   | Tool                        |
|---------|-----------------------------|
| Markup  | HTML5                       |
| Style   | Tailwind CSS (CDN)          |
| Script  | Vanilla JS                  |
| AI Tool | Claude Code (claude-sonnet) |
