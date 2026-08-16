# URL Shortener: Design Tokens and Component Specifications

## Overview

This document defines the visual language and reusable components for the URL shortener frontend, ensuring consistency across all screens and states defined in `flows.md`.

---

## Color Palette

### Functional Colors

| Token | Value | Usage |
|-------|-------|-------|
| `color-success` | `#10b981` | Success states, checkmarks, positive feedback |
| `color-error` | `#ef4444` | Error states, destructive actions, alerts |
| `color-warning` | `#f59e0b` | Loading hints, secondary warnings |
| `color-info` | `#3b82f6` | Links, info text, secondary actions |
| `color-neutral-50` | `#f9fafb` | Backgrounds, light surfaces |
| `color-neutral-100` | `#f3f4f6` | Subtle backgrounds, disabled states |
| `color-neutral-200` | `#e5e7eb` | Borders, dividers |
| `color-neutral-700` | `#374151` | Body text, primary text |
| `color-neutral-900` | `#111827` | Headings, high-contrast text |

### Semantic Color Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `bg-primary` | `color-neutral-50` | Page background |
| `bg-elevated` | `white` | Cards, modals, input fields |
| `border-default` | `color-neutral-200` | Standard borders |
| `border-error` | `color-error` | Error box borders |
| `border-success` | `color-success` | Success box borders |
| `text-primary` | `color-neutral-900` | Headings, main content |
| `text-secondary` | `color-neutral-700` | Body text, descriptions |
| `text-disabled` | `color-neutral-200` | Disabled inputs, placeholder text |

---

## Typography

### Font Family
- **System stack**: `-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif`
- Rationale: Cross-platform consistency, zero custom font overhead

### Scale

| Token | Font Size | Line Height | Font Weight | Usage |
|-------|-----------|-------------|-------------|-------|
| `type-h1` | 32px | 1.2 | 700 (bold) | Page headings, modal titles |
| `type-h2` | 24px | 1.3 | 600 (semibold) | Section headings |
| `type-h3` | 18px | 1.4 | 600 (semibold) | Subheadings, card titles |
| `type-body-lg` | 16px | 1.5 | 400 (normal) | Body text, input labels |
| `type-body` | 14px | 1.5 | 400 (normal) | Default body text |
| `type-body-sm` | 12px | 1.4 | 400 (normal) | Helper text, hints, timestamps |
| `type-caption` | 11px | 1.3 | 400 (normal) | Very small text, table captions |

---

## Spacing

### Scale (in pixels and REM for CSS)

| Token | Pixels | REM | Usage |
|-------|--------|-----|-------|
| `space-0` | 0 | 0 | No spacing |
| `space-1` | 4px | 0.25rem | Tight spacing (icon + text) |
| `space-2` | 8px | 0.5rem | Input padding, small gaps |
| `space-3` | 12px | 0.75rem | Comfortable padding |
| `space-4` | 16px | 1rem | Standard padding, gaps |
| `space-6` | 24px | 1.5rem | Section spacing |
| `space-8` | 32px | 2rem | Major section spacing |
| `space-12` | 48px | 3rem | Page-level spacing |

---

## Component Library

### Button

**Variants**: Primary (filled), Secondary (outline), Tertiary (text-only), Danger (red)

**Primary Button**
- Background: `color-info` (#3b82f6)
- Text: white
- Padding: `space-2` (vertical) × `space-4` (horizontal)
- Border radius: 6px
- Font weight: 600
- Disabled state: Background `color-neutral-100`, text `text-disabled`, cursor not-allowed
- Hover: Background darkens to #2563eb
- Focus: Border 2px solid `color-info`, outline offset 2px
- Active/pressed: Background further darkens to #1d4ed8

**Secondary Button**
- Border: 2px solid `color-info`
- Background: transparent
- Text: `color-info`
- Padding: `space-2` (vertical) × `space-4` (horizontal)
- Border radius: 6px
- Disabled: Border `color-neutral-100`, text `text-disabled`
- Hover: Background `color-neutral-50`

**Tertiary Button** (for cancel, close)
- Background: transparent
- Text: `color-neutral-700`
- Padding: `space-2` (vertical) × `space-3` (horizontal)
- Border radius: 4px
- Disabled: Text `text-disabled`
- Hover: Background `color-neutral-50`

**Danger Button** (for delete, destructive actions)
- Background: `color-error` (#ef4444)
- Text: white
- Padding: `space-2` × `space-4`
- Border radius: 6px
- Hover: Darken to #dc2626
- Requires explicit confirmation modal

### Input Text Field

- Background: `bg-elevated` (white)
- Border: 1px solid `border-default`
- Border radius: 6px
- Padding: `space-3` (vertical) × `space-4` (horizontal)
- Font size: `type-body`
- Focus state: Border 2px solid `color-info`, outline none
- Error state: Border 2px solid `color-error`, text `color-error` for validation message
- Disabled state: Background `color-neutral-100`, text `text-disabled`, cursor not-allowed
- Placeholder: Text `text-disabled`, font style normal (not italic)

### Label

- Font size: `type-body-lg`
- Font weight: 600
- Color: `text-primary`
- Margin bottom: `space-2`
- Associated with input via `for` attribute

### Helper / Hint Text

- Font size: `type-body-sm`
- Color: `text-secondary`
- Margin top: `space-1`
- Margin bottom: `space-3` (below input)

### Error Message (Inline)

- Font size: `type-body-sm`
- Color: `color-error`
- Margin top: `space-1`
- Icon: Error glyph (⚠) or circle-exclamation, `space-1` before text
- Announced to screen readers via ARIA `aria-invalid="true"` on input

### Alert / Message Box

**Success Alert** (green)
- Background: `color-success` with 10% opacity (e.g., `rgba(16, 185, 129, 0.1)`)
- Border: 2px solid `color-success`
- Border radius: 8px
- Padding: `space-4`
- Icon: Checkmark (✓) in `color-success`, `space-2` before text
- Text: `type-body`, `text-primary`

**Error Alert** (red)
- Background: `color-error` with 10% opacity
- Border: 2px solid `color-error`
- Border radius: 8px
- Padding: `space-4`
- Icon: Alert (⚠) in `color-error`, `space-2` before text
- Text: `type-body`, `text-primary`

**Info Alert** (blue)
- Background: `color-info` with 10% opacity
- Border: 2px solid `color-info`
- Border radius: 8px
- Padding: `space-4`
- Icon: Info circle (ⓘ) in `color-info`, `space-2` before text
- Text: `type-body`, `text-primary`

### Toast Notification (Transient)

- Background: `color-neutral-900` (dark gray)
- Text: white
- Border radius: 8px
- Padding: `space-3` × `space-4`
- Font size: `type-body`
- Position: Fixed, bottom-right corner, 16px offset from edges
- Duration: Auto-dismiss after 3 seconds
- Animation: Fade in (100ms), fade out (200ms)
- Z-index: 9999 (above all other content)
- Optionally include a close button (×) for manual dismiss

### Modal / Dialog

- Backdrop: Semi-transparent black (`rgba(0, 0, 0, 0.5)`)
- Content background: `bg-elevated`
- Border radius: 12px
- Padding: `space-6`
- Shadow: `0 20px 25px -5px rgba(0, 0, 0, 0.1)` (elevation 3)
- Max width: 500px on desktop, 90vw on mobile
- Title: `type-h2`, `text-primary`
- Body text: `type-body`, `text-secondary`
- Actions (buttons): Right-aligned, gap `space-3` between buttons
- Close button (×): Top-right corner, semi-transparent, full opacity on hover
- Keyboard: Escape key closes modal, Tab cycles through focusable elements

### Table

- Background: `bg-elevated`
- Border: 1px solid `border-default`
- Border radius: 8px
- Cell padding: `space-3` (vertical) × `space-4` (horizontal)

**Header row**
- Background: `color-neutral-50`
- Text: `type-body-lg`, font weight 600, `text-primary`
- Border bottom: 2px solid `border-default`

**Body rows**
- Text: `type-body`, `text-secondary`
- Border bottom: 1px solid `border-default`
- Hover state: Background `color-neutral-50` (light highlight)

**Footer / Pagination**
- Background: `color-neutral-50`
- Border top: 2px solid `border-default`
- Controls (buttons, dropdown): Aligned right, gap `space-4`

### Skeleton Loader

- Background: `color-neutral-100`
- Animation: Shimmer effect (left-to-right gradient wave, 1.5s loop)
- Height: Match the replaced element (e.g., text skeleton is 16px tall for body text)
- Border radius: Match the replaced element (4px for text, 6px for input)
- Margin bottom: Match gap that would appear between rows

### Copy Button / Icon

- Icon: Document + stack (📋) or similar
- Background: Transparent on hover → `color-neutral-100`
- Color: `color-info`
- Size: 16–20px
- Padding: `space-2`
- Border radius: 4px
- Cursor: pointer
- On click: Trigger `navigator.clipboard.writeText()`, show toast "Link copied"
- Tooltip on hover: "Copy to clipboard"

### Copyable Text Field

- Layout: Input field + copy button adjacent
- Input: Read-only (no editing), select all on focus
- Button: Right-aligned, inside the field (pseudo-element or flex layout)
- Text: Monospace font (e.g., `'SF Mono', 'Monaco', 'Monaco', monospace`) for URL display
- Font size: `type-body-sm` for long URLs

### Spinner / Loading Indicator

- Icon: Rotating circular progress indicator
- Color: `color-info`
- Size: 20px × 20px (small), 32px × 32px (large)
- Animation: 360° rotation, 1s per cycle, linear
- Adjacent text: "Shortening...", "Loading...", etc., `space-2` to the right

### Disclosure / Expandable Section

- Trigger: Button or clickable text, right-aligned chevron icon (▼ or ▶)
- Trigger text: `type-body`, `color-info` underline on hover
- Content: Revealed below trigger, animated slide-down (200ms ease)
- Content background: Slightly different (e.g., `color-neutral-50`)
- Content padding: `space-4`
- Border: Optional 1px `border-default` around content

---

## Layout Patterns

### Page Layout

- Max width: 1200px on desktop
- Padding: `space-6` on desktop, `space-4` on tablet, `space-4` on mobile
- Header: Sticky, background `bg-elevated`, shadow, padding `space-4`
- Main content: Below header, gap `space-6` to footer
- Footer: Optional, background `color-neutral-50`, padding `space-4`, text-align center

### Form Layout

- Direction: Vertical (stacked)
- Gap between fields: `space-6`
- Label above input
- Helper/error text below input
- Action buttons: Aligned left or full-width on mobile, right-aligned on desktop
- Gap between buttons: `space-3`

### Card Layout

- Background: `bg-elevated`
- Border: 1px solid `border-default`
- Border radius: 8px
- Padding: `space-4` to `space-6`
- Shadow: Optional, `0 1px 3px rgba(0, 0, 0, 0.1)`
- Gap between cards: `space-4`

---

## Responsive Breakpoints

| Breakpoint | Width | Usage |
|---|---|---|
| Mobile (small) | 0–639px | Portrait phones, narrow screens |
| Mobile (large) | 640–767px | Landscape phones, wide mobile |
| Tablet | 768–1023px | iPad, small tablets |
| Desktop | 1024px+ | Laptops, large displays |

### Responsive Rules

- **Mobile**: Single column, full-width inputs, stacked buttons, no table (convert to cards)
- **Tablet**: Two columns where appropriate, narrower padding, tables with horizontal scroll if needed
- **Desktop**: Multi-column layouts, full tables, side-by-side buttons

---

## Accessibility Requirements

### Color Contrast
- All text must meet WCAG AA standards (4.5:1 for normal text, 3:1 for large text)
- Error/success states must not rely on color alone; include icons and text

### Focus Indicators
- All interactive elements must have visible focus outline (2px border or 2px shadow)
- Focus outline color: `color-info` or high-contrast alternative
- Focus outline offset: 2px (gap between element and outline)

### Keyboard Navigation
- All buttons, links, and inputs must be keyboard-accessible
- Tab order must follow visual left-to-right, top-to-bottom flow
- Form inputs must have associated labels (via `<label for="...">`)
- Modal dialog must trap focus (Tab cycles within modal, Escape closes)

### Screen Reader Support
- Buttons: Descriptive text ("Create new link" not "Click here")
- Icons without text: Include `aria-label` (e.g., `<button aria-label="Copy to clipboard">📋</button>`)
- Error messages: Linked to input via `aria-describedby`
- Loading state: Announce "Loading" via `aria-live="polite"`
- Spinners: Include text label, not icon-only
- Alerts: Use `aria-role="alert"` for error/success boxes

### Reduced Motion
- Users with `prefers-reduced-motion` should see minimal animation
- Disable shimmer animation on skeleton loaders
- Disable transitions on modals, toasts, and dropdowns
- Keep essential feedback (color change, text update) but remove motion

---

## Animation Timing

- **Fast**: 100ms (button hover, focus outline)
- **Normal**: 200ms (modal slide, dropdown expand, toast fade)
- **Slow**: 500ms (page transition, skeleton shimmer loop)
- **Very slow**: 1000ms+ (loading spinner rotation, chart animation)

All animations use `ease-in-out` or `ease` easing function for smoothness.

---

## Dark Mode (Future)

When dark mode is added, define corresponding tokens:
- `color-neutral-50` → `#111827` (invert)
- `color-neutral-900` → `#f9fafb` (invert)
- Functional colors remain consistent
- Test contrast ratios in dark mode

---

## Implementation Checklist

- [ ] All components meet WCAG AA contrast and keyboard accessibility
- [ ] Responsive design tested at all breakpoints
- [ ] Focus indicators visible on all interactive elements
- [ ] Loading, error, and empty states match design tokens
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Tooltips and helper text use consistent font sizes and colors
- [ ] Modal backdrop and focus trap work correctly
- [ ] Toast notifications auto-dismiss and are dismissible
- [ ] Copy buttons use correct icon and trigger clipboard API
- [ ] Table pagination controls are keyboard-accessible
