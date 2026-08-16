# Security Architect

_design · task T2 · run RUN-B93F03BB · model `ollama/qwen2.5-coder:7b`_

## What this role decided

The security posture for this application will be designed with authentication, authorisation, PII handling, encryption, network boundaries, secret management, and compliance obligations in mind.

## Decisions

- Authentication: Use OAuth 2.0 for authentication, with a client ID and secret stored in a secrets manager.
- Authorisation: Implement role-based access control (RBAC) with a least privilege model, where each principal gets the narrowest grant that works.
- PII Handling: Implement PII detection and anonymisation using a library like `fides`.
- Encryption: Encrypt data in transit using TLS 1.2 and encrypt data at rest using AES-256-GCM.
- Network Boundaries: Implement network segmentation and firewalls to limit access to the application.
- Secret Management: Use HashiCorp Vault for secrets management, with secrets stored in a managed store at runtime.
- Compliance: Ensure compliance with GDPR and CCPA by implementing data minimisation, access controls, and data protection impact assessments.

## Findings

- The project already decided to use Docker Compose with a named volume for the SQLite file and never bake credentials into the image. This decision is approved by Vivek.
- The project already decided to use ChromaDB for any vector storage or similarity search and SQL for all structured data. This decision is approved by Vivek.

## Open questions

- What specific roles and permissions will be defined for RBAC?
- What specific PII fields will be detected and anonymised?
- What specific data flows will be encrypted in transit and at rest?
- What specific network segmentation and firewall rules will be implemented?
- What specific data minimisation and access control measures will be implemented?
- What specific data protection impact assessments will be conducted?

---

_Written by the agent that made these decisions, when it made them._
