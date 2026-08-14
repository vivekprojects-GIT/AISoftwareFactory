# Spec Compliance Agent

## What this agent is accountable for

Answer the question the tests cannot: did the implementation actually satisfy every approved acceptance criterion, with evidence, and not merely pass its own tests?

## What it is expert at

These went into its prompt verbatim.

- **Requirement-to-evidence tracing** — Match every acceptance criterion to the artefact that proves it, and name the ones with nothing behind them.
- **Stub and placeholder detection** — A function that returns a constant, raises `NotImplementedError`, or is commented as a placeholder does not satisfy anything.
- **Fail-closed reporting** — Unproven is reported as unproven; absence of evidence is never reported as compliance.

## What it may write

nothing - you produce findings, not files

## What it did

6 task(s), touching 0 file(s).

### T11 — Spec Compliance Agent

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-f381b618/t11` · **Model** `ollama/qwen2.5-coder:7b`

The implementation does not satisfy every approved acceptance criterion as it lacks evidence for AC-1 and AC-3, and has a risk of executing write or delete queries.

- {'severity': 'high', 'area': 'AC-1 and AC-3', 'detail': 'The implementation does not provide evidence that a question in plain English returns an answer and the SQL that produced it, nor does it save conversations for later reopening.'}

### T11 — Spec Compliance Agent

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-b8f8aa4a/t11` · **Model** `ollama/qwen2.5-coder:7b`

The implementation does not satisfy every approved acceptance criterion as it lacks evidence for AC-1 and AC-3.

- {'severity': 'medium', 'area': 'User Experience', 'detail': 'The implementation does not provide the functionality for analysts to ask questions in plain English and receive both an answer and the SQL that produced it, as required by AC-1.'}
- {'severity': 'medium', 'area': 'Persistence', 'detail': 'The implementation lacks the capability to save conversations and reopen them later with their questions and answers, as required by AC-3.'}

### T11 — Spec Compliance Agent

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-069db4c2/t11` · **Model** `ollama/qwen2.5-coder:7b`

The implementation does not satisfy every approved acceptance criterion as it lacks evidence for AC-1 and AC-3.

- {'severity': 'medium', 'area': 'Acceptance Criteria Coverage', 'detail': 'AC-1 and AC-3 are not covered by the provided evidence, which means the implementation may not fully satisfy these criteria.'}

### T16 — Spec Compliance Agent

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-57067112/t16` · **Model** `ollama/qwen2.5-coder:7b`

The implementation does not satisfy every approved acceptance criterion as it lacks evidence for AC-1 and AC-3, and there is no evidence that the generated SQL is read-only.

- {'severity': 'medium', 'area': 'Integration', 'detail': 'There is no evidence that a question in plain English returns an answer and the SQL that produced it.'}
- {'severity': 'medium', 'area': 'Unit', 'detail': 'There is no evidence that a conversation is saved and can be reopened later with its questions and answers.'}

### T16 — Spec Compliance Agent

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-9f7b2d55/t16` · **Model** `ollama/qwen2.5-coder:7b`

The implementation does not fully satisfy every approved acceptance criterion as it lacks evidence for AC-3 and does not provide a mechanism to save and reopen conversations.

- {'severity': 'medium', 'area': 'Security', 'detail': 'Generated queries that would write or delete data are not being refused, which could lead to data integrity issues.'}
- {'severity': 'medium', 'area': 'Functionality', 'detail': 'The implementation does not provide a way to save and reopen conversations with questions and answers.'}

### T16 — Spec Compliance Agent

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-09038735/t16` · **Model** `simulated/spec-compliance`

Wired cross-repo contract checks between frontend, backend and API.



## Notes it recorded

- simulated unusable (RuntimeError: no model provider configured); deterministic agent used
