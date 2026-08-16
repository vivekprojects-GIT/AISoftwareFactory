# URL Shortener: User Flows and Screens

## Overview

This document specifies the complete user journey for the internal URL shortener, including all states that determine whether the software feels finished or broken: creation flows, loading states, empty states, error recovery, and the list view that shows both shortened links and click metrics.

**Primary user model**: Workforce users authenticated via OIDC. A user has a subject identity and session lifetime.

**Three acceptance criteria define done**:
- AC-1: User pastes long URL, clicks shorten, sees short link appear in list
- AC-2: Visiting short link returns HTTP 307 redirect to original URL
- AC-3: Click count for that link increases by one

This document designs the screens and flows that allow a user to *complete* each criterion.

---

## Screen 1: Authenticated Home / Link List

**Primary action**: "Create new link" (button)

**Entry point**: User lands here after OIDC login, or revisits the app.

### States

#### 1a. Populated list (happy path for a returning user)

**Display**:
- Header: "My shortened links"
- Table with columns:
  - **Short link**: Copyable text field showing code (e.g., `abc1234`). Copy button adjacent.
  - **Target URL**: Scheme and host only (e.g., `https://example.com/<redacted>`), per API_ARCH-9. Hover or click "Show full URL" to reveal in a tooltip or modal.
  - **Created**: Timestamp (ISO 8601, localized to user timezone)
  - **Clicks**: Integer count. Click to drill into audit trail (future enhancement).
  - **Actions**: "Delete" button (soft-delete, per API_ARCH-1)
- Pagination controls (offset-based, per API_ARCH-3): "Previous", "Next", page size selector (1–100, default 20)
- "Create new link" button at top

**Interaction**:
- Clicking "Copy" on the short link copies `https://<internal-domain>/u/abc1234` to clipboard and shows a transient success toast: "Link copied"
- Clicking "Show full URL" reveals the actual target URL in a tooltip (dismiss on click or after 5s)
- Clicking "Delete" triggers a confirmation modal: "Are you sure? This link will no longer redirect."
  - On confirm: DELETE request, link marked soft-deleted, removed from list with transient success toast
  - On cancel: modal closes, list unchanged
- Pagination: Clicking "Next" or selecting a page size triggers a new GET /v1/links request with new offset/limit

#### 1b. Empty state (new user, or user has deleted all links)

**Display**:
- Header: "No links yet"
- Empty state illustration (optional)
- Paragraph: "Create your first shortened link to get started."
- "Create new link" button (primary, filled)

**Interaction**:
- Clicking "Create new link" transitions to Screen 2 (create form)

#### 1c. Loading state (initial page load, pagination request pending)

**Display**:
- Header: "My shortened links" (shown immediately)
- Skeleton loaders for table rows (5–10 placeholder rows)
- Pagination controls disabled
- "Create new link" button shown but disabled

**Behavior**:
- GET /v1/links request is in-flight
- If request takes >1s, skeleton placeholders appear
- On success: Transition to 1a or 1b
- On error: Transition to 1d

#### 1d. Error state (network failure, permission denied, server error)

**Display**:
- Header: "My shortened links"
- Error box (red border, error icon) with:
  - **Message**: Human-readable error text based on HTTP status:
    - 401/403: "You are not authorized to view your links. Please log in again."
    - 500: "Something went wrong. Please try again in a moment."
    - Network timeout: "Connection lost. Check your network and try again."
  - **Retry button**: "Try again" (sends GET /v1/links again)
  - **Optional details**: If the error is transient (network timeout, 5xx), hint: "This sometimes happens. Retrying usually works."
- "Create new link" button shown, enabled (user can still create while list load failed)

**Interaction**:
- Clicking "Try again" re-sends GET /v1/links
- If error persists after 2 retries, show: "This is taking longer than expected. Contact support if it continues."

---

## Screen 2: Create Link Form

**Primary action**: "Shorten" (button)

**Entry point**: User clicks "Create new link" from Screen 1, or navigates directly.

### States

#### 2a. Form, ready to input (happy path)

**Display**:
- Header: "Create a shortened link"
- Form fields:
  - **Paste long URL**: Text input field, placeholder "https://example.com/very/long/path?with=parameters", autofocus
  - Hint text below field: "Paste the full URL you want to shorten."
- **Short code** (optional, read-only display): Initially empty. After successful shorten, shows the generated code (e.g., `abc1234`). If user wants a custom code, this is future scope (not in AC).
- **Actions**:
  - "Shorten" button (primary, filled) – disabled until input is non-empty
  - "Cancel" button (tertiary) – closes form, returns to Screen 1 without creating

**Interaction**:
- User pastes URL into field (keyboard input or paste from clipboard)
- Input validates on blur: Check if it's a valid URL (scheme required, per API_ARCH-5). If invalid, show inline error below field: "Invalid URL format. Include the scheme (https://...)." Button remains disabled.
- If valid, "Shorten" button becomes enabled
- Clicking "Shorten" triggers POST /v1/links and transitions to 2b
- Clicking "Cancel" closes the form and returns to Screen 1 with all fields cleared

#### 2b. Shortening in progress (loading state)

**Display**:
- Header: "Create a shortened link"
- Form fields as in 2a, but:
  - Input field disabled (grayed out, no further edits)
  - "Shorten" button replaced with spinner + text: "Shortening..."
  - "Cancel" button disabled

**Behavior**:
- POST /v1/links request is in-flight
- If request takes >2s, show a hint below the spinner: "This is taking a moment..."
- On success: Transition to 2c
- On error: Transition to 2d

#### 2c. Success: Short link created (happy path, AC-1 complete)

**Display**:
- Header: "Link created!"
- Success box (green border, checkmark icon) with:
  - **Message**: "Your short link is ready."
  - **Short code display**: Highlighted text showing the code (e.g., `abc1234`) in a copyable field
  - **Full short URL**: `https://<internal-domain>/u/abc1234` (also copyable)
  - **Copy button**: Copies the full short URL to clipboard, shows transient toast: "Link copied"
  - **Go to list button**: Returns to Screen 1; the new link is now visible at the top of the list

**Interaction**:
- Clicking "Copy" copies the full short URL to clipboard
- Clicking "Go to list" closes the form and refreshes Screen 1 (user sees new link)
- After 3 seconds, auto-dismiss the success state and return to Screen 1

#### 2d. Error state (invalid URL, policy violation, network failure)

**Display**:
- Header: "Create a shortened link"
- Error box (red border, error icon) with:
  - **Message**: Based on error code (from API_ARCH-5):
    - `INVALID_URL` (422): "The URL format is invalid. Check that it starts with https:// or http://."
    - `URL_POLICY_VIOLATION` (422): "This URL is not allowed. Check with your team admin if you think this is a mistake."
    - Network timeout / 5xx: "Connection lost or server error. Please try again."
  - **Retry button**: "Try again" (re-sends POST /v1/links with same URL)
  - **Clear button**: "Clear form" (resets input to empty, returns to 2a)
- Input field shown with the URL that failed (so user can edit if needed)
- "Shorten" button re-enabled

**Interaction**:
- User can click "Clear form" and start over (transition to 2a)
- User can edit the input field and click "Shorten" again
- Clicking "Try again" re-sends the same request

---

## Screen 3: Click Metrics / Audit Trail (Future Enhancement)

**Note**: This screen is not required by AC-1, AC-2, AC-3, but the data structure supports it (per API_ARCH-10). Design is deferred pending clarification of what "click count" user actions mean. For now, the "Clicks" column in Screen 1 displays a number only.

**Future interaction**: Clicking on a click count in Screen 1 would drill into:
- A modal or separate screen showing:
  - Total clicks for that link
  - Time-series chart of clicks over days/weeks (if audit events are retained)
  - List of audit events (if per-visit rows are enabled, currently forbidden by SEC-7)

---

## Flow Diagrams

### Happy Path: Create and View

```
Screen 1 (List, empty or populated)
  ↓ [Click "Create new link"]
Screen 2a (Form, ready)
  ↓ [User pastes URL, clicks "Shorten"]
Screen 2b (Loading)
  ↓ [POST /v1/links succeeds]
Screen 2c (Success)
  ↓ [Click "Go to list"] or [Auto-dismiss after 3s]
Screen 1 (List, now populated with new link)
```

### Error Recovery: Invalid URL

```
Screen 2a (Form, ready)
  ↓ [User pastes invalid URL, clicks "Shorten"]
Screen 2b (Loading)
  ↓ [POST /v1/links fails with INVALID_URL]
Screen 2d (Error)
  ↓ [Click "Clear form"]
Screen 2a (Form, ready, input cleared)
```

### Pagination on List

```
Screen 1a (List, populated, page 1)
  ↓ [Click "Next" or change page size]
Screen 1c (List, loading)
  ↓ [GET /v1/links?offset=20&limit=20 succeeds]
Screen 1a (List, page 2)
```

---

## State Transition Matrix

| Current State | User Action / Event | Next State | Backend Request | Result Display |
|---|---|---|---|---|
| 1a (List populated) | Click "Create new link" | 2a | None | Form appears |
| 1a (List populated) | Pagination: Click "Next" | 1c | GET /v1/links | Skeleton loaders |
| 1b (List empty) | Click "Create new link" | 2a | None | Form appears |
| 1c (Loading) | Request succeeds | 1a or 1b | GET /v1/links | List populated or empty |
| 1c (Loading) | Request fails | 1d | GET /v1/links | Error box + retry |
| 1d (Error) | Click "Try again" | 1c | GET /v1/links | Skeleton loaders |
| 2a (Form ready) | User pastes URL | 2a | None | Inline validation |
| 2a (Form ready) | Click "Shorten" with valid URL | 2b | POST /v1/links | Spinner + disabled form |
| 2a (Form ready) | Click "Cancel" | 1a | None | Form closes, return to list |
| 2b (Loading) | Request succeeds | 2c | POST /v1/links | Success box + short link |
| 2b (Loading) | Request fails | 2d | POST /v1/links | Error box + retry |
| 2c (Success) | Auto-dismiss timer fires | 1a | GET /v1/links | List refresh, new link visible |
| 2c (Success) | Click "Go to list" | 1a | GET /v1/links | List refresh, new link visible |
| 2d (Error) | Click "Clear form" | 2a | None | Input cleared, form reset |
| 2d (Error) | Click "Try again" | 2b | POST /v1/links | Spinner |
| 1a (List) | Click "Delete" on a link | Modal | None | Confirmation prompt |
| Modal | Click "Confirm delete" | Modal → 1a or 1b | DELETE /v1/links/{code} | Link removed, success toast |
| Modal | Click "Cancel delete" | 1a | None | Modal closes |

---

## Accessibility and Progressive Disclosure

### Keyboard Navigation
- All buttons are keyboard-accessible (Tab, Enter)
- Form inputs support standard text editing (Ctrl+A, Ctrl+V, etc.)
- Error messages are announced to screen readers (ARIA live region)
- Links in the "Copy" action show focus outline

### Progressive Disclosure
- **Novice user**: Sees form with one input field (paste URL) and one button (Shorten). Hint text explains what to do.
- **Returning user**: Sees list with short link (copyable), target URL (redacted by default, revealed on click), and click count. No overwhelming detail.
- **Power user / audit**: Click on a link's "Clicks" count to drill into audit trail (future). Pagination controls support offset/limit parameters.

### Empty and Loading States
- **Empty state** (1b) prevents confusion: User understands they have no links yet, not that the app is broken.
- **Loading state** (1c, 2b) shows progress: Skeleton placeholders give feedback that the request is in-flight, not frozen.
- **Error state** (1d, 2d) is actionable: Specific error message + retry button, so user is not stranded.

---

## Acceptance Criteria Completion Map

### AC-1: User pastes long URL, clicks shorten, sees short link appear in list

**Flow**: User starts at Screen 1 → clicks "Create new link" (2a) → pastes URL → clicks "Shorten" (2b loads) → POST /v1/links succeeds → (2c success, auto-dismiss or click "Go to list") → Screen 1 refreshes → new link visible at top of list.

**Screens involved**: 1, 2a, 2b, 2c

**Visible result**: Short link appears in the table on Screen 1 with code, target URL (redacted), creation timestamp, and click count (0).

### AC-2: Visiting short link returns HTTP 307 redirect

**Flow**: User clicks "Copy" on the short link in Screen 1 (or pastes the URL from 2c success message) → clicks or navigates to `https://<domain>/u/abc1234` → Browser receives GET /u/{code} → Backend returns 307 Temporary Redirect with Location header → Browser follows redirect to original URL.

**Screens involved**: This is a backend contract (API_ARCH-6), not a user-facing screen. Frontend displays the short link; clicking it delegates to the browser.

**Visible result**: User's browser navigates to the original long URL without the user seeing an intermediate page.

### AC-3: Click count increases by one

**Flow**: AC-2 completes (user visits short link) → Backend records the click (increments counter in `clicks` table, per DATA-9) → When user returns to Screen 1 and views the list, the "Clicks" column shows the incremented count.

**Screens involved**: 1a (list, populated)

**Visible result**: "Clicks" column in the table increments by 1 each time the link is visited. User can refresh Screen 1 to see the updated count.

---

## Design Decisions and Rationale

### Why inline validation on URL input (Screen 2a)?
Client feedback and AC-1 imply users should get quick feedback on whether their URL is valid *before* they click Shorten. Inline validation (on blur or as-you-type with debounce) prevents wasted network requests and keeps the user in control.

### Why show redacted target URL by default (Screen 1a)?
Per API_ARCH-9, target URLs are redacted to `scheme://host/<redacted>` before emission. This is a security measure. The full URL is revealed on click to prevent a wall of text on first glance (progressive disclosure).

### Why auto-dismiss the success state (Screen 2c) after 3 seconds?
Users often expect a brief confirmation and then return to the main task (viewing their list). Auto-dismiss reduces friction for the happy path without removing the success feedback. Users who want to copy the link before dismissal can do so immediately.

### Why soft-delete only (no permanent delete)?
Per API_ARCH-1, links are soft-deleted (marked as deleted, not removed from DB). This supports audit trails (DATA-8) and allows recovery if needed. Frontend shows the delete as permanent from the user's perspective (link vanishes from list), but backend preserves the data.

### Why paginate the link list?
Per API_ARCH-3, the collection endpoint supports offset-based pagination with limit (1–100). Even a user with 50 links per day × 365 days = 18k links benefits from pagination. Design shows page size selector and Next/Previous buttons to keep navigation simple.

### Why no session timeout warning?
Session and identity are managed by OIDC (ARCH-PLACE-5). Token refresh happens transparently. If a session expires, the backend returns 401, and the frontend (this layer) redirects to login. A session timeout warning is a future enhancement.

---

## Notes for Implementation

### Form Validation
- Client-side: Regex or URL constructor to validate format (scheme required)
- Server-side: POST /v1/links endpoint returns 422 if URL fails policy checks (API_ARCH-5)
- On 422, extract `error_code` field and map to human-readable message per error taxonomy

### Copy to Clipboard
- Use modern `navigator.clipboard.writeText()` API
- Show transient toast: "Link copied" for 2–3 seconds
- Fallback for older browsers: Show a tooltip "Press Ctrl+C to copy" with text pre-selected

### Auto-refresh after create
- After POST /v1/links succeeds, either:
  - User clicks "Go to list" and frontend fetches GET /v1/links, OR
  - 3-second auto-dismiss triggers GET /v1/links
- Ensure the new link appears at the top (sorted by creation time, descending)

### Error Code Mapping
Frontend must map API error codes (from API_ARCH-5) to user-friendly messages:
- `INVALID_URL` → "The URL format is invalid..."
- `URL_POLICY_VIOLATION` → "This URL is not allowed..."
- `LINK_NOT_FOUND` → "That link doesn't exist..." (for future GET /{code})
- `UNAUTHORIZED` (401) → "You are not authorized. Please log in again."
- Generic 5xx → "Something went wrong. Please try again in a moment."

### Loading UX Timing
- Show skeleton loaders after 1 second of wait time (avoid flicker for fast responses)
- Show "taking a moment" hint after 2 seconds
- Show "contact support" message after 3+ failed retries

### Responsive Design
- Mobile (< 640px): Stack form vertically, show short link in a card (not table)
- Tablet (640–1024px): Two-column layout or collapsible columns in table
- Desktop (> 1024px): Full table with all columns visible

---

## Future Enhancements (Out of Scope)

1. **Click analytics drill-down** (Screen 3): Time-series chart of clicks, optional per-hour breakdown
2. **Custom short codes**: Allow user to specify a custom code (if not taken)
3. **Link expiration**: Set a TTL on a link so it auto-deletes after N days
4. **Bulk operations**: Select multiple links and delete/export in one action
5. **Shared links**: Grant other team members access to a link (read-only, or edit permissions)
6. **QR code generation**: Generate a QR code for the short link
7. **Session timeout warning**: Warn user 5 minutes before session expires
8. **Dark mode**: Support system preference or manual toggle
