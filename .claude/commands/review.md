Review the current experiment or changed file(s) against all project rules and report any issues.

## Steps

1. Identify the file(s) to review:
   - If the user names a file, read that file.
   - Otherwise, run `git diff --name-only HEAD` to find recently changed files and read each one.

2. Check each file against the following rule categories. For each violation found, note the file, line (if applicable), rule broken, and a fix suggestion.

### HTML rules
- `<html lang="...">` present, meaningful `<title>`
- Semantic elements used (`<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`) — not `<div>` for everything
- Only one `<h1>` per page; heading hierarchy is logical (no skipping levels)
- All `<img>` tags have `alt` attributes
- No synchronous blocking scripts in `<head>`

### CSS / Tailwind rules
- Tailwind utility classes used for all styling; custom `<style>` only for keyframes, pseudo-elements, or complex selectors
- No mixing Tailwind classes and inline `style=""` for the same property on the same element
- Dark theme base colors respected: background `#0A0A0F`, surface `#12121A`, card `#1A1A26`, border `#2A2A3E`
- Muted text uses `#6B7280` or `text-gray-200` — no pure white (`#FFFFFF`) for body copy

### JavaScript rules
- `const` used by default; `let` only where reassignment is needed; no `var`
- No `console.log` left in code
- `<script>` block is at the bottom of `<body>`
- `addEventListener` preferred over inline `onclick=""` (exceptions allowed for small demos)

### Animation rules
- Only `transform` and `opacity` animated (no `width`, `height`, `top`, `left`, `margin`, `padding`)
- `prefers-reduced-motion` respected (looping/decorative animations wrapped)
- Decorative elements have `pointer-events: none`
- Entrance animation pattern: `opacity 0 → 1` + `translateY 40px → 0` over `0.6s–0.8s ease-out`

### Accessibility rules
- Interactive elements keyboard-focusable with visible focus styles
- Decorative elements have `aria-hidden="true"`
- Buttons have descriptive text or `aria-label`
- Color contrast meets WCAG AA

### Project structure rules
- File named in `kebab-case`
- `README.md` updated with an entry for this experiment

3. Output a structured report:
   - **Pass** — if a category has no issues
   - **Issues** — list each violation with a fix suggestion

4. After the report, ask: "Would you like me to fix any of these issues?"
