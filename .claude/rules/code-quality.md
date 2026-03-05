# Rule: Code Quality

## General
- Write the minimum code required to accomplish the task. Do not over-engineer.
- Prefer readability over cleverness. Code in this repo is for learning — clarity matters most.
- Do not add comments to self-evident code. Only comment non-obvious logic.
- Do not add error handling for scenarios that cannot happen in the current context.

## HTML
- Use semantic elements: `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` — not `<div>` for everything.
- Always include `lang` on `<html>` and a meaningful `<title>`.
- `alt` attributes on all `<img>` tags.
- One `<h1>` per page. Heading hierarchy must be logical (h1 → h2 → h3, no skipping).

## CSS / Tailwind
- Use Tailwind utility classes for everything possible before writing custom CSS.
- Custom CSS (`<style>` block) only for things Tailwind cannot express: keyframe animations, pseudo-elements, complex selectors.
- Do not mix Tailwind and inline `style=""` for the same property on the same element.
- Group Tailwind classes in a consistent order: layout → sizing → spacing → typography → color → border → effect → animation.

## JavaScript
- Vanilla JS only unless a framework is explicitly required by the project.
- Use `const` by default, `let` only when reassignment is needed. Never `var`.
- Prefer `addEventListener` over inline `onclick=""` attributes — exceptions allowed for small single-page demos.
- No `console.log` left in committed code.
- Keep script blocks at the bottom of `<body>`, not in `<head>` (unless `defer`/`async` is used).

## Accessibility
- Interactive elements must be keyboard-focusable and have visible focus styles.
- Color contrast: text on background must meet WCAG AA (4.5:1 for normal text, 3:1 for large text).
- Decorative elements (particles, background shapes) must have `aria-hidden="true"` or `pointer-events: none`.
- Buttons must have descriptive text or `aria-label`.

## Performance
- No synchronous blocking scripts in `<head>`.
- Fonts loaded via `<link rel="preconnect">` before the actual font request.
- Images: use appropriate formats and include `width`/`height` attributes to prevent layout shift.
- Animate only `transform` and `opacity` (GPU-accelerated). Never animate layout properties.
