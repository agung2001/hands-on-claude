# Rule: Animations & Motion

## Principles
- Motion should feel purposeful — every animation must serve UX (guide attention, show state, add delight).
- Prefer CSS animations over JS-driven ones for performance. Only use JS for scroll-triggered or interactive effects.
- Default easing: `ease-out` for entrances, `ease-in-out` for loops.
- Never animate more than 3 properties on the same element simultaneously.

## Standard Animation Patterns

### Entrance animations
- Elements entering the viewport: `slideUp` (translateY 40px → 0, opacity 0 → 1) over `0.6s–0.8s`.
- Use `opacity: 0` as the initial state, not `display: none`.
- Stagger sibling elements with `animation-delay` increments of `0.1s–0.2s`.

### Scroll-triggered
- Use `IntersectionObserver` with `threshold: 0.1`.
- Apply transition via inline `style` rather than toggling classes for stagger control.

### Looping animations
- Floating elements: `float` keyframe (translateY ±20px) over `6s–9s ease-in-out infinite`.
- Glow pulse: `box-shadow` intensity oscillation over `3s ease-in-out infinite`.
- Shimmer buttons: `background-position` slide over `2.5s linear infinite`.
- Scan lines: translateY across container over `4s linear infinite`.

## Accessibility
- Always respect `prefers-reduced-motion`. Wrap looping/decorative animations in:
  ```css
  @media (prefers-reduced-motion: reduce) {
    * { animation-duration: 0.01ms !important; }
  }
  ```
- Entrance animations are acceptable even with reduced motion preference, but keep them instant (`0.01ms`).

## Performance
- Animate only `transform` and `opacity` — they are GPU-accelerated and do not trigger layout.
- Avoid animating `width`, `height`, `top`, `left`, `margin`, or `padding`.
- Decorative elements (particles, orbs) must have `pointer-events: none`.
