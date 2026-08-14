# Architecture overview

Approved by **u.architect**.

## The approved diagram

```mermaid
flowchart TD
    subgraph Trust Boundary
        FE[Frontend]
        BE[Backend]
        API[HTTP API]
    end
    subgraph Data Tier
        DB[PostgreSQL Database]
    end
    FE -->|REST + OpenAPI 3.1| API
    API -->|Role-based access control| BE
    BE -->|SQL Queries| DB
    DB -->|Results| BE
    BE -->|HTTP Response| FE
```

## Decisions behind it

_No architecture decisions were recorded._

## Notes

The SQL Assistant is a full-stack web application that allows users to ask questions in plain English and receive answers along with the generated SQL. The frontend communicates with the backend via an HTTP API, which uses FastAPI and PostgreSQL for data storage. Observability is provided through OpenTelemetry traces and metrics.
