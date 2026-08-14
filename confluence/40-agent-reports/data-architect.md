# Data Architect

## What this agent is accountable for

Decide data ownership, the logical model, retention, lineage and integration boundaries. The Database Engineer implements what you decide.

## What it is expert at

These went into its prompt verbatim.

- **Normalised schema design** — Model to third normal form first and denormalise only against a measured read pattern.
- **Indexing strategy** — Design indexes from the query plan the application will actually issue; an unindexed foreign key is a future outage.
- **Migration safety** — Migrations are append-only, forward-only and backward-compatible for one release, so a rollback never strands data.
- **Data lifecycle** — Classify, then set retention and deletion; data with no expiry is a liability that grows.
- **Consistency modelling** — Choose transactional boundaries deliberately and state where eventual consistency is acceptable.

## What it may write

an artifact only - you write no repository files

## What it did

6 task(s), touching 0 file(s).

### T4 — Data Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-f381b618/t4` · **Model** `ollama/qwen2.5-coder:7b`

The system will provide a local, developer-friendly interface for analysts to ask questions in plain English and receive answers along with the generated SQL. The solution will include a conversation history feature that allows reopening of past conversations.

- The requirement specifies that the system should run locally on a developer machine, which means we need to ensure that all dependencies are available locally.

### T4 — Data Architect

**Status** `blocked` · **Repository** `none` · **Branch** `factory/run-b8f8aa4a/t4` · **Model** `—`

_no summary_


### T4 — Data Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-069db4c2/t4` · **Model** `ollama/qwen2.5-coder:7b`

The system will be a local, developer-facing tool that translates plain English questions into read-only SQL queries and provides the results along with the generated SQL. The conversation history will be saved for future reference.

- The requirement specifies that the system should run locally on a developer machine, which means it needs to be designed and implemented in a way that does not rely on any external services or cloud resources.

### T9 — Data Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-57067112/t9` · **Model** `ollama/qwen2.5-coder:7b`

The solution involves creating a new component within the 'ai-software-factory' repository to handle ad-hoc SQL generation and execution based on plain English questions. This component will interact with the local relational database, ensure read-only operations, log all queries and results, and save conversations for future reference.

- The component may not accurately interpret complex or ambiguous questions, leading to incorrect SQL queries.
- There is a risk of security vulnerabilities if the component does not properly validate input or handle exceptions.

### T9 — Data Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-9f7b2d55/t9` · **Model** `ollama/qwen2.5-coder:7b`

The solution involves creating a new component in the 'ai-software-factory' repository to handle ad-hoc SQL generation and execution based on plain English questions. This component will interact with the relational database, observability, and secrets manager to ensure secure and compliant operations.

- The component may not accurately translate all plain English questions to SQL, leading to incorrect results or errors.
- There is a risk of executing write or delete operations if the translation logic fails to enforce read-only constraints.

### T9 — Data Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-09038735/t9` · **Model** `simulated/data-architect`

Wired cross-repo contract checks between frontend, backend and API.



## Notes it recorded

- simulated unusable (RuntimeError: no model provider configured); deterministic agent used
