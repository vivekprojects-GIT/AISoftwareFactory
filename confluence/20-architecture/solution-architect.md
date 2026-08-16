# Solution Architect

_design · task T1 · run RUN-9C44C548 · model `anthropic/claude-opus-5+claude-sonnet-5+claude-haiku-4-5-20251001`_

## What this role decided

I mapped the approved spec onto the single shared repository as four top-level directories — apps/api (FastAPI, layered: routes → services → domain → repositories → db), apps/web (React 19 + TS), contracts (OpenAPI 3.1 as the frozen boundary between them), and deploy/ci — and fixed the eight structural decisions the implementers cannot make locally. The load-bearing ones: (1) short codes are 7-char CSPRNG base62 with a unique index and bounded retry, not sequential ids, because sequential codes make every team member's confidential URLs enumerable; (2) the click counter is a single atomic `UPDATE ... SET clicks = clicks + 1 RETURNING target_url` committed before the response, so AC-2 and AC-3 are one transaction and unit-testable without new infrastructure; (3) the redirect returns 307 with `Cache-Control: no-store`, because a 301 would be cached by the browser and AC-3 would silently stop incrementing after the first visit; (4) authentication is a BFF-style HttpOnly session cookie issued by the API after the OIDC code exchange rather than bearer-only, because a browser navigating to /r/{code} cannot carry an Authorization header and the data is classified confidential, so the redirect route must be authenticated like every other route. Ownership is carried as the OIDC `sub` on each link row, which is what makes 'their list' in AC-1 enforceable at the repository layer rather than in the UI. Costs are named per ADR; the one I want confirmed before build is that short links are team-authenticated, not anonymously shareable.

## Decisions

- **One repository, four top-level directories: apps/api, apps/web, contracts, deploy (+ .github/workflows). No shared Python/TS package is created at this size.** — The client explicitly chose 'one repository, directories inside it'. Boundaries follow ownership and change axis: the API and the SPA release together but are built, tested and containerised independently, so they are siblings rather than nested. A shared library is deferred because there is exactly one consumer of each side today, and an unused abstraction layer is pure carrying cost.
- **apps/api is layered strictly: api/routes (HTTP only) → services (use cases) → domain (pure rules: code generation, URL policy) → repositories (SQL) → db (SQLAlchemy models, Alembic). Routes never touch a session or ORM model; domain modules import nothing from db or fastapi.** — The three acceptance criteria are behavioural rules (uniqueness, ownership filtering, exact +1) whose evidence rule is 'unit'. Keeping those rules in service/domain modules with no HTTP or DB import makes them testable in-process without a running app or database, which is the cheapest possible path to the required evidence.
- **Short codes are 7 characters of base62 drawn from `secrets.choice`, stored in a UNIQUE column; on insert conflict the service regenerates and retries up to 5 times, then returns 503.** — Data classification is confidential. A code space of 62^7 (~3.5e12) makes guessing impractical and, unlike a sequence, prevents any user from walking neighbouring codes to read colleagues' links. Uniqueness is enforced by the database constraint rather than a read-then-write check, so it holds under concurrent inserts. Cost: a code carries no ordering information and the retry path needs a test double to exercise.
- **Resolve-and-count is one statement: `UPDATE links SET clicks = clicks + 1 WHERE code = :code RETURNING target_url`, committed before the 307 is written. Zero rows affected → 404. A failed commit → 500, not a silent redirect.** — AC-2 and AC-3 are a single observable event, so they belong in a single transaction; the atomic increment is correct under concurrency without row locks held across application code. Making the increment non-optional means the count in the list view (AC-1/AC-3) can never drift below reality, which is the property the user actually checks. Cost: every read is a write — no read-only replica path, and a very hot link serialises on one row.
- **The redirect responds 307 Temporary Redirect with `Cache-Control: no-store` and `Referrer-Policy: no-referrer`. Only `http`/`https` absolute targets are accepted at creation.** — 301 is cacheable and browsers honour it aggressively, so the second and later visits would never reach the service and AC-3 would appear to fail while looking like a caching mystery. 307 plus no-store guarantees every visit is counted. Restricting schemes at creation time prevents the redirect endpoint from becoming a launcher for `javascript:` or `data:` URLs. Cost: no CDN offload for redirects, which is acceptable for internal team volume.
- **Authentication is OIDC authorization-code + PKCE handled by the API as a BFF: /auth/login and /auth/callback exchange the code server-side and issue a signed HttpOnly, Secure, SameSite=Lax session cookie. Every route including GET /r/{code} requires that cookie; unauthenticated navigation to a short link is 302'd into the login flow and returned to the link afterwards. ID tokens are validated against cached JWKS; `sub` is the link owner key.** — A browser navigating to a short link cannot attach an Authorization header, so a bearer-only design would force the redirect route to be public — unacceptable for confidential data, since the code alone would grant read access to anyone. SameSite=Lax still permits top-level navigation from mail and chat clients, which is how short links are actually used. Keeping tokens out of JavaScript also removes XSS token theft from the threat model. Cost: the SPA and API must be served on the same registrable domain, and the redirect path now has a login dependency.
- **Single aggregate, single table `links` (id, code UNIQUE, target_url, owner_subject, clicks NOT NULL DEFAULT 0, created_at), indexed on (owner_subject, created_at DESC). Schema changes only via Alembic migrations in apps/api/app/db/migrations. No cache tier.** — All three criteria touch one entity; splitting it would create joins with no owning reason to change separately. The composite index serves the only list query ('my links, newest first') directly. Postgres alone meets the latency need at team scale, and the atomic-increment decision in ADR-4 would make a read-through cache immediately stale anyway.
- **contracts/openapi.yaml is generated from the FastAPI app and committed; CI fails if the committed contract drifts from the code. apps/web consumes a generated typed client from that file and hand-writes no request/response types.** — It makes the API/SPA boundary a reviewable artifact rather than tribal knowledge, and a drift check in CI is the cheapest guard against the SPA and API disagreeing about the shape of a link. Cost: contributors must regenerate the file, which will annoy people until it is a make target.
- **URL acceptance policy lives in apps/api/app/domain/url_policy.py as a pure function: require absolute http/https, normalise (strip fragment, lowercase host), cap length at 2048, and reject targets resolving to the service's own host or to private/loopback/link-local address literals.** — The create endpoint accepts a user-supplied URL that the service will later hand to a browser, so it is an open-redirect and internal-network-probing surface. Putting the rule in one pure domain function means it is unit-testable and cannot be bypassed by a future second entry point. This is a real check, not a named guard: the rejection list is explicit and enforced at creation time before persistence.

## Components

- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****
- ****

## Risks

- ADR-6 makes short links team-only: a link pasted into a channel forces a login round trip and will not open for anyone outside the IdP. That is the safe reading of 'confidential' but it is an access-control expectation I inferred, not one the client stated — confirm before build, because reversing it later changes the redirect route's contract.
- The cookie decision requires the SPA and API on one registrable domain; a split-domain deployment silently breaks authentication on the redirect path and would push the team back toward a public redirect endpoint.
- ADR-4 turns every redirect into a write. A single very popular link serialises on one row, and there is no read replica or cache path available given the counting requirement — acceptable at team scale, revisit if redirect volume grows.
- No per-click history is stored (counter only), so questions like 'when was this clicked' or 'by whom' cannot be answered later without a migration and backfill gap.
- Codes are unguessable but not revocable in this scope: there is no delete/expire endpoint, so a mistakenly shortened confidential URL cannot be withdrawn. Worth a follow-up ticket.
- The bounded collision retry (5 attempts) returning 503 is a path that will effectively never fire in production and can therefore rot untested — it must be covered by an injected-collision unit test, not left to chance.
- Session-cookie POSTs need CSRF protection (SameSite=Lax plus an origin check on /api writes); if the implementer treats SameSite as sufficient on its own, the create endpoint is exposed to cross-site form posts.
- Assumed AWS realisation is managed PostgreSQL plus the already-approved Kubernetes runtime; no new AWS service is introduced by this plan, and any move to DynamoDB, ElastiCache or a queue would invalidate ADR-4/ADR-7 and require re-approval.

---

_Written by the agent that made these decisions, when it made them._
