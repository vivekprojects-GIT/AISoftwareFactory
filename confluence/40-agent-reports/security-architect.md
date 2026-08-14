# Security Architect

## What this agent is accountable for

Decide the security posture before anything is built: authentication, authorisation model, PII handling, encryption in transit and at rest, network boundaries, secret management and the compliance obligations that apply.

## What it is expert at

These went into its prompt verbatim.

- **Threat modelling (STRIDE)** — Walk every trust boundary and data flow systematically; threats are found by method, not by intuition.
- **Authentication and authorisation design** — Specify how identity is proven and how each decision is enforced server-side; a client-side check is not authorisation.
- **Secrets management** — Secrets come from a managed store at runtime — never a repository, an image layer, or a build argument.
- **Least privilege** — Every principal gets the narrowest grant that works, and the grant is written down as part of the design.
- **Data protection** — Decide encryption in transit and at rest, key ownership and rotation before storage exists, not after.

## What it may write

an artifact only - you write no repository files

## What it did

6 task(s), touching 0 file(s).

### T3 — Security Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-f381b618/t3` · **Model** `ollama/qwen2.5-coder:7b`

The task requires a local solution for analysts to ask questions in plain English and receive answers along with the generated SQL, while ensuring that write or delete operations are refused. The solution must adhere to security best practices, including encryption, access controls, and audit logging.

- The requirement specifies that the system should run locally on a developer machine, which limits the scope of potential security risks compared to a cloud-based solution.

### T3 — Security Architect

**Status** `blocked` · **Repository** `none` · **Branch** `factory/run-b8f8aa4a/t3` · **Model** `—`

_no summary_


### T3 — Security Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-069db4c2/t3` · **Model** `ollama/qwen2.5-coder:7b`

The task requires a local development environment where analysts can ask questions in plain English and receive answers along with the generated SQL. The system must ensure that no write or delete operations are performed, and all queries are logged for audit purposes.

- The requirement specifies that generated SQL is read-only, which means any query that writes or deletes data should be refused.

### T8 — Security Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-57067112/t8` · **Model** `ollama/qwen2.5-coder:7b`

The solution involves creating a new component within the 'ai-software-factory' repository to handle ad-hoc SQL generation and execution based on plain English questions. This component will interact with the local relational database, ensure read-only operations, log all queries and results, and save conversations for future reference.

- The component may not accurately interpret complex or ambiguous questions, leading to incorrect SQL queries.
- There is a risk of security vulnerabilities if the component does not properly validate input or handle exceptions.

### T8 — Security Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-9f7b2d55/t8` · **Model** `ollama/qwen2.5-coder:7b`

The solution involves creating a new component in the 'ai-software-factory' repository to handle ad-hoc SQL generation and execution based on plain English questions. This component will interact with the relational database, observability, and secrets manager to ensure secure and compliant operations.

- The component may not accurately translate all plain English questions to SQL, leading to incorrect results or errors.
- There is a risk of executing write or delete operations if the translation logic fails to enforce read-only constraints.

### T8 — Security Architect

**Status** `succeeded` · **Repository** `none` · **Branch** `factory/run-09038735/t8` · **Model** `simulated/security-architect`

Wired cross-repo contract checks between frontend, backend and API.



## Notes it recorded

- simulated unusable (RuntimeError: no model provider configured); deterministic agent used
