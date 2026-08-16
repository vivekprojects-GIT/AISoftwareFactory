# UX Research — Internal URL Shortener

Owner: UX Researcher
Scope of this directory: user goals, journeys, pain points. Nothing in here specifies
architecture, data model, security controls or API shape — those are settled elsewhere
and are treated here as fixed constraints on the experience.

## Contents

| File | What it answers |
|---|---|
| `personas.md` | Who uses this, what they are trying to get done, what they already have |
| `task-analysis.md` | The goal hierarchy — what a user is accomplishing, not which screens they touch |
| `journeys.md` | End-to-end paths including every error and recovery state |
| `pain-points.md` | Ranked failures, each with severity, evidence label and the fix it implies |
| `traceability.md` | Journey ↔ acceptance criteria map, and what the ACs do not cover |

## Evidence base, stated plainly

No user was interviewed, observed or surveyed for this work. There is no analytics
baseline, because no product exists yet, and there will be no behavioural telemetry
after launch either — the settled privacy position stores a bare click integer and no
per-visit rows, so this team can never answer "where did users drop off" from data.
That is the right privacy call and I am not contesting it, but it has a research
consequence I want on the record: **for the life of this product, qualitative work
(interviews, hallway tests, support chatter) is the only instrument available.**
Planning to "look at the numbers later" is not an option that exists here.

Every statement in these documents therefore carries one of three labels:

- **EVIDENCE** — traceable to something the client actually stated (business intent,
  acceptance criteria, authentication choice, data classification) or to a settled
  project decision whose user-facing consequence is deterministic.
- **INFERENCE** — a conclusion I drew from EVIDENCE by reasoning that I have written
  out, so a reader can disagree with the reasoning rather than with me.
- **ASSUMPTION** — a plausible claim about users with nothing behind it yet. Each one
  names the cheapest way to kill or confirm it.

If you quote this research downstream, carry the label with the claim. A design
argument that cites an ASSUMPTION as if it were EVIDENCE is how teams end up building
confidently for a user who does not exist.

## Validation plan (small, and worth doing before the SPA is built)

1. **Five 20-minute interviews** with people who paste links into team channels daily.
   Target the assumptions marked V1–V6 in `personas.md` and `pain-points.md`.
   Kills or confirms roughly two-thirds of the ASSUMPTION rows.
2. **Artefact review, no humans required.** Pull the last 200 long URLs shared in the
   team's main channels. Measure: how many exceed the 2048-character cap, how many are
   internal hostnames, how many are re-shared more than once. This is a half-day of work
   and converts the most load-bearing assumptions (A-2, A-4) into evidence without
   scheduling anyone.
3. **Paper-prototype the recipient path**, not the creator path. The creator path is
   one field and one button; the recipient path is where the login interlock lives
   (see J-3) and where this product will be judged.

## How to read the journey maps

Each journey states the user's goal in their words, the trigger, the steps, and — the
part that matters — the branches where it goes wrong and what recovery looks like.
A journey map that stops at the happy path is a marketing diagram. Products are judged
in the error states, and this product has four of them that a user will hit in normal
weekly use.
