# API Architect

_design · task T4 · run RUN-B93F03BB · model `ollama/qwen2.5-coder:7b`_

## What this role decided

The API surface will include endpoints for asking questions, retrieving conversation history, and managing conversations. Versioning will be done through URL path prefixes, with each version being additive. Error semantics will follow a consistent taxonomy, and pagination will be implemented for collections. Idempotency will be ensured for mutating operations, and compatibility will be maintained through additive changes only.

## Decisions

- Resources: The API will include endpoints for asking questions, retrieving conversation history, and managing conversations.
- Versioning strategy: Versioning will be done through URL path prefixes, with each version being additive.
- Error semantics: Error responses will follow a consistent taxonomy, including status codes, stable machine codes, and actionable messages.
- Pagination: Every collection will paginate, and every mutating call will be safe to retry.
- Idempotency: Every mutating call will be safe to retry, ensuring idempotency.
- Compatibility policy: Compatibility will be maintained through additive changes only, with removing or narrowing a field being a new version.

## Findings

- The project already decided to use Docker Compose with a named volume for the SQLite file and to use ChromaDB for vector storage.
- The project has already decided to use the local model server (Ollama) for natural-language work and the standard library logger for structured logging.
- The project has already decided to use SQLAlchemy for interacting with the SQL database.

---

_Written by the agent that made these decisions, when it made them._
