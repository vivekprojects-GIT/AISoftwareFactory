# Quality Orchestrator

## What this agent is accountable for

Decide what must be proven for this change and which quality agents run, then consolidate their evidence into one verdict.

## What it is expert at

These went into its prompt verbatim.

- **Risk-based test strategy** — Concentrate testing where failure costs most, rather than spreading it evenly for the sake of a number.
- **Coverage judgement** — Read what the tests actually assert; a covered line with no assertion is decoration.
- **Release-readiness assessment** — Judge on evidence produced by this build, never on a previous run's green.

## What it may write

an artifact only - you write no repository files

## What it did

6 task(s), touching 0 file(s).

### T10 — Quality Orchestrator

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-f381b618/t10` · **Model** `ollama/qwen2.5-coder:7b`

The proposed change aims to improve the efficiency of data retrieval for analysts by allowing them to ask questions in plain English and receive answers along with the generated SQL. The solution will run locally on a developer machine, adhering to strict security and audit requirements.

- AC-1: A question in plain English returns an answer and the SQL that produced it
- AC-2: A generated query that would write or delete data is refused, not executed
- AC-3: A conversation is saved and can be reopened later with its questions and answers

### T10 — Quality Orchestrator

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-b8f8aa4a/t10` · **Model** `ollama/qwen2.5-coder:7b`

The change requires the implementation of a new component to handle ad-hoc SQL generation based on plain English questions, ensuring that generated queries are read-only and secure, and that conversations are saved for future reference.

- AC-1: A question in plain English returns an answer and the SQL that produced it
- AC-2: A generated query that would write or delete data is refused, not executed
- AC-3: A conversation is saved and can be reopened later with its questions and answers

### T10 — Quality Orchestrator

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-069db4c2/t10` · **Model** `ollama/qwen2.5-coder:7b`

The change requires the implementation of a new component to handle ad-hoc SQL generation and execution based on plain English questions. The component must ensure that generated queries are read-only, save conversations for later, and log all interactions.

- AC-1: A question in plain English returns an answer and the SQL that produced it
- AC-2: A generated query that would write or delete data is refused, not executed
- AC-3: A conversation is saved and can be reopened later with its questions and answers

### T15 — Quality Orchestrator

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-57067112/t15` · **Model** `ollama/qwen2.5-coder:7b`

The change requires the implementation of a new component to handle ad-hoc SQL generation and execution based on plain English questions. The component must ensure that generated queries are read-only, save conversations for future reference, and log all interactions.

- AC-1: A question in plain English returns an answer and the SQL that produced it
- AC-2: A generated query that would write or delete data is refused, not executed
- AC-3: A conversation is saved and can be reopened later with its questions and answers

### T15 — Quality Orchestrator

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-9f7b2d55/t15` · **Model** `ollama/qwen2.5-coder:7b`

The change requires the implementation of a new component to handle ad-hoc SQL queries based on plain English questions, ensuring that generated queries are read-only and all interactions are logged.

- AC-1: A question in plain English returns an answer and the SQL that produced it
- AC-2: Generated query that would write or delete data is refused, not executed
- AC-3: A conversation is saved and can be reopened later with its questions and answers

### T15 — Quality Orchestrator

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-09038735/t15` · **Model** `simulated/quality-orchestrator`

Wired cross-repo contract checks between frontend, backend and API.



## Notes it recorded

- simulated unusable (RuntimeError: no model provider configured); deterministic agent used
