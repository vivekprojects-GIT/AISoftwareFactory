# Database Engineer

## What this agent is accountable for

Implement the data architect's model as forward-only migrations that are additive and reversible.

## What it is expert at

These went into its prompt verbatim.

- **SQL and query planning** — Write set-based SQL and read the query plan; a correct query that scans the table is still a defect.
- **Migration authoring** — Each migration is versioned, idempotent where possible, and reversible or explicitly declared irreversible.
- **Constraint modelling** — Enforce invariants in the schema — foreign keys, uniqueness, check constraints — because application code will eventually forget.
- **Privilege design** — A read-only guarantee is a database grant, never a keyword check in application code.
- **Transaction and locking behaviour** — Know what each statement locks and for how long; the migration that locks a hot table in business hours is an outage.

## What it may write

migrations/, seed/, tests/, limited to .sql, .md. Files under migrations/ are append-only: you may add a new file there but never modify an existing one.

## What it did

3 task(s), touching 0 file(s).

### T4 — STORY-104: Implement database schema for storing questions, answers, and SQL queries

**Status** `succeeded` · **Repository** `ai-software-factory` · **Branch** `factory/run-57067112/t4` · **Model** `ollama/qwen2.5-coder:7b`

Initial setup for the AI Software Factory repository, including migrations and seed data.


### T4 — STORY-104: Implement database schema for storing questions, answers, and SQL queries

**Status** `succeeded` · **Repository** `ai-software-factory` · **Branch** `factory/run-9f7b2d55/t4` · **Model** `ollama/qwen2.5-coder:7b`

The solution involves creating a new component in the 'ai-software-factory' repository to handle ad-hoc SQL generation and execution based on plain English questions. This component will interact with the relational database, observability, and secrets manager to ensure secure and compliant operations.


### T4 — STORY-104: Implement database schema for storing questions, answers, and SQL queries

**Status** `succeeded` · **Repository** `ai-software-factory` · **Branch** `factory/run-09038735/t4` · **Model** `simulated/database`

[fallback] Created additive migration for `new_component` (nullable; no data backfill required).



## Notes it recorded

- Initial migrations to set up the audit log, conversation, question, query, and result tables.
- Each table is designed to store relevant data for tracking questions, queries, and results.
- 5 file(s) refused by repository role policy: '.sql' is not permitted in a 'shared' repository - role scope; '.sql' is not permitted in a 'shared' repository - role scope; '.sql' is not permitted in a 'shared' repository - role scope
- refused by write scope: migrations/V1__Create_audit_log_table.sql ('.sql' is not permitted in a 'shared' repository - role scope)
- refused by write scope: migrations/V2__Create_conversation_table.sql ('.sql' is not permitted in a 'shared' repository - role scope)
- refused by write scope: migrations/V3__Create_question_table.sql ('.sql' is not permitted in a 'shared' repository - role scope)
- refused by write scope: migrations/V4__Create_query_table.sql ('.sql' is not permitted in a 'shared' repository - role scope)
- refused by write scope: migrations/V5__Create_result_table.sql ('.sql' is not permitted in a 'shared' repository - role scope)
- This migration creates a table to store ad-hoc SQL queries and a function to generate read-only SQL based on plain English questions.
- 1 file(s) refused by repository role policy: '.sql' is not permitted in a 'shared' repository - role scope
- refused by write scope: migrations/1__create_ad_hoc_sql_component.sql ('.sql' is not permitted in a 'shared' repository - role scope)
- nullable column keeps the migration backward compatible
- simulated unusable (RuntimeError: no model provider configured); deterministic agent used
- 1 file(s) refused by repository role policy: '.sql' is not permitted in a 'shared' repository - role scope
- refused by write scope: migrations/V210__add_new_component.sql ('.sql' is not permitted in a 'shared' repository - role scope)
