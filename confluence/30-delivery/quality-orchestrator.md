# Quality Orchestrator

_assure · task T15 · run RUN-17EA8460 · model `ollama/qwen2.5-coder:7b`_

## What this role decided

The change requires proving that the new component for handling natural language to SQL generation meets the acceptance criteria, specifically AC-1, AC-2, and AC-3.

## Decisions

- Run integration tests for AC-1 to ensure the system returns an answer and the correct SQL query based on a plain English question.
- Run security tests for AC-2 to ensure that any queries attempting to write or delete data are refused.
- Run unit tests for AC-3 to verify that conversations can be saved and reopened.

## Findings

- AC-1: The system must return an answer and the SQL query generated based on a plain English question. This will be verified through integration testing with various questions and checking if the output is as expected.
- AC-2: The system must refuse and not execute any queries that would write or delete data. This will be tested by attempting to run such queries and verifying that they are rejected.
- AC-3: Conversations must be saved and can be reopened later with their questions and answers. This will be verified through unit testing the conversation repository functions.

## Open questions

- What specific questions should be used in the integration tests to cover various scenarios?
- How will the security tests be designed to ensure all potential write/delete queries are covered?
- What is the format of the conversation data that needs to be saved and how will it be verified upon reopening?

---

_Written by the agent that made these decisions, when it made them._
