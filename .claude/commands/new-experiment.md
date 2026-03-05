Create a new experiment for this hands-on-claude repo.

## Steps

1. Ask the user: "What is this experiment about? Give a short description."
2. Derive a kebab-case filename from the description (e.g. `particle-clock.html`).
3. Confirm the filename with the user before creating anything.
4. Create the file at the repo root as `<kebab-name>.html` (single-file experiment) or as `<kebab-name>/index.html` (multi-file project — only if the user says it needs multiple files).
5. Scaffold the file using the project's standard boilerplate:
   - `<!DOCTYPE html>` with `lang="en"` and a meaningful `<title>`
   - Tailwind CSS via CDN (`<script src="https://cdn.tailwindcss.com"></script>`)
   - Inter font via Google Fonts preconnect
   - Dark theme base: `bg-[#0A0A0F] text-gray-200 min-h-screen`
   - Tailwind `extend` config block with the project's custom colors (`claude-orange: #D97757`, `claude-surface: #12121A`, `claude-card: #1A1A26`, `claude-border: #2A2A3E`)
   - Empty `<style>` block for keyframe animations only
   - Semantic HTML structure: `<header>`, `<main>`, `<footer>`
   - Empty `<script>` block at the bottom of `<body>`
   - `prefers-reduced-motion` media query stub in the `<style>` block
6. Add the experiment to `README.md` under `## Projects` with a one-line description and the file path.
7. Do NOT commit — remind the user to run `/commit` when ready.
