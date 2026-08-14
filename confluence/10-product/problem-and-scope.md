# Problem and scope

## What was asked for

The business wants an ad-hoc SQL assistant that analysts can interact with through a chat interface in plain English, receive answers and see the generated SQL, and have conversations saved. The system must be local to developer machines and should not perform any data writing or deletion.

## What was explicitly excluded

_Nothing was recorded as out of scope._

## Technology chosen

Every choice below came from the governed catalogue; nothing was invented for this
project.

- **cloud**: local
- **backend_language**: python
- **backend_framework**: fastapi
- **database**: postgres
- **runtime**: managed-paas
- **api_style**: rest
- **observability**: otel
- **frontend_framework**: react
- **auth**: rbac
- **ci**: github-actions

## Deployment

Target: **local**
