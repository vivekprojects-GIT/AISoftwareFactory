# Cloud Architect

## What this agent is accountable for

Decide where each workload runs and which approved provider patterns satisfy it, including any cross-cloud edge and its data classification.

## What it is expert at

These went into its prompt verbatim.

- **Managed-service selection** — Prefer the managed service over the self-run one, and say what operational burden that avoids.
- **Environment topology** — Isolate environments by account or project boundary, never by naming convention inside one.
- **Cost modelling** — Estimate the recurring bill at expected load before the design is approved; cost is a design constraint, not a surprise.
- **Local-first deployment** — When the target is local, choose components that genuinely run locally — never a cloud service with a local-sounding name.
- **Resilience design** — Design for the failure of each dependency explicitly: timeout, retry with backoff, and a defined degraded behaviour.

## What it may write

an artifact only - you write no repository files

## What it did

6 task(s), touching 0 file(s).

### T6 — Cloud Architect

**Status** `blocked` · **Repository** `none` · **Branch** `factory/run-f381b618/t6` · **Model** `—`

_no summary_


### T6 — Cloud Architect

**Status** `blocked` · **Repository** `none` · **Branch** `factory/run-b8f8aa4a/t6` · **Model** `—`

_no summary_


### T6 — Cloud Architect

**Status** `blocked` · **Repository** `none` · **Branch** `factory/run-069db4c2/t6` · **Model** `—`

_no summary_


### T11 — Cloud Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-57067112/t11` · **Model** `ollama/qwen2.5-coder:7b`

The task intent is to allow analysts to ask questions in plain English and receive answers along with the SQL that produced them, running locally on a developer machine. The approved specification outlines the requirements, constraints, and decisions for implementing this functionality.

- The requirement specifies that generated SQL should be read-only and any queries that would write or delete data should be refused.

### T11 — Cloud Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-9f7b2d55/t11` · **Model** `ollama/qwen2.5-coder:7b`

The solution involves creating a new component in the 'ai-software-factory' repository to handle ad-hoc SQL generation and execution based on plain English questions. This component will interact with the relational database, observability, and secrets manager to ensure secure and compliant operations.

- The component may not accurately translate all plain English questions to SQL, leading to incorrect results or errors.
- There is a risk of executing write or delete operations if the translation logic fails to enforce read-only constraints.

### T11 — Cloud Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-09038735/t11` · **Model** `simulated/cloud-architect`

Wired cross-repo contract checks between frontend, backend and API.



## Notes it recorded

- simulated unusable (RuntimeError: no model provider configured); deterministic agent used
