# Rule: UI & Design

## Theme
- Always use dark theme as the default. Background base color: `#0A0A0F`.
- Primary accent color is Claude orange: `#D97757`. Use it for highlights, CTAs, and interactive elements.
- Surface colors: `#12121A` (surface), `#1A1A26` (card), `#2A2A3E` (border).
- Muted text: `#6B7280`. Never use pure white for body copy — use `#E5E7EB` or Tailwind `text-gray-200`.

## Typography
- Headings: `font-extrabold` or `font-bold`, tight tracking (`tracking-tight`).
- Code/terminal text: `JetBrains Mono` or `font-mono`.
- Body: `Inter` at `text-base` or `text-lg` with `leading-relaxed`.

## Layout
- Max content width: `max-w-7xl` for full sections, `max-w-5xl` for centered content, `max-w-3xl` for focused CTAs.
- Section vertical padding: `py-24` minimum, `py-32` preferred.
- Use CSS Grid and Flexbox — no floats or legacy layout methods.
- Always mobile-first: design for small screen first, then add `md:` and `lg:` breakpoints.

## Components
- Cards: rounded-2xl, `border border-claude-border`, `bg-claude-card`, hover lift with `transition-transform`.
- Buttons: primary uses the shimmer animation; secondary uses border + hover color shift.
- Inputs/terminals: `font-mono`, dark background, subtle border, optional scan-line overlay.
