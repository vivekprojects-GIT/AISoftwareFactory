# Who does what

Every agent that worked on **SQL Assistant**, what it is accountable for, and what it
is expert at. Expertise is not decoration: these skills are put into each agent's
prompt verbatim, so what an agent was held to is exactly what you can read here.

| Agent | Accountable for | Expert at | May write | Did |
|---|---|---|---|---|
| **API Architect**<br>`api-architect` | API surface, versioning and compatibility strategy | Resource-oriented design, Contract-first development, Versioning and compatibility, Error taxonomy, Pagination and idempotency | an artifact only - you write no repository files | 6 task(s), 0 file(s) |
| **API Contract Engineer**<br>`api-contract` | OpenAPI/schema, backward compatible | OpenAPI 3.1 authoring, Schema design, Backward compatibility, Contract testing | the api repository, limited to .yaml, .yml, .json, .md. | 3 task(s), 0 file(s) |
| **Backend Engineer**<br>`backend` | Services, business rules and persistence | Python service engineering, Framework fluency (FastAPI), Input validation and injection defence, Error handling, Query efficiency, Test-first implementation | app/, src/, tests/, limited to .py, .md. | 9 task(s), 10 file(s) |
| **Cloud Architect**<br>`cloud-architect` | Provider placement and approved cloud patterns | Managed-service selection, Environment topology, Cost modelling, Local-first deployment, Resilience design | an artifact only - you write no repository files | 6 task(s), 0 file(s) |
| **Data Architect**<br>`data-architect` | Data ownership, model, retention, lineage | Normalised schema design, Indexing strategy, Migration safety, Data lifecycle, Consistency modelling | an artifact only - you write no repository files | 6 task(s), 0 file(s) |
| **Database Engineer**<br>`database` | Schema and forward-only migrations | SQL and query planning, Migration authoring, Constraint modelling, Privilege design, Transaction and locking behaviour | migrations/, seed/, tests/, limited to .sql, .md. Files under migrations/ are append-only: | 3 task(s), 0 file(s) |
| **Frontend Engineer**<br>`frontend` | Components and client integration | React engineering, TypeScript discipline, Asynchronous UI states, Accessibility, Rendering performance, Contract adherence | src/, limited to .ts, .tsx, .css. | 6 task(s), 5 file(s) |
| **Quality Orchestrator**<br>`quality-orchestrator` | Decide the quality strategy and consolidate evidence | Risk-based test strategy, Coverage judgement, Release-readiness assessment | an artifact only - you write no repository files | 6 task(s), 0 file(s) |
| **Scrum Master / Delivery Manager**<br>`scrum-master` | Ticket flow, blockers, dependency release and honest progress | Impediment removal, Critical path tracking, Board hygiene, Load balancing | an artifact only - you write no repository files | 6 task(s), 0 file(s) |
| **Security Architect**<br>`security-architect` | Authentication, PII, encryption, boundaries, compliance | Threat modelling (STRIDE), Authentication and authorisation design, Secrets management, Least privilege, Data protection | an artifact only - you write no repository files | 6 task(s), 0 file(s) |
| **Solution Architect**<br>`solution-architect` | Module structure and architecture decision records | Component decomposition, Integration patterns, Architecture decision records, Trade-off analysis, Diagramming for review | an artifact only - you write no repository files | 6 task(s), 0 file(s) |
| **Spec Compliance Agent**<br>`spec-compliance` | Every acceptance criterion mapped to real evidence | Requirement-to-evidence tracing, Stub and placeholder detection, Fail-closed reporting | nothing - you produce findings, not files | 6 task(s), 0 file(s) |
| **Technical Lead**<br>`technical-lead` | Task decomposition, sequencing and implementation consistency | Implementation sequencing, Interface-first breakdown, Code review judgement, Technical debt management | an artifact only - you write no repository files | 6 task(s), 0 file(s) |
| **Work Planner**<br>`work-planner` | Dependency-aware epics, stories and tasks from the approved architecture | Vertical slicing, Dependency graphing, Definition of done, Skill-based assignment | an artifact only - you write no repository files | 6 task(s), 0 file(s) |

## Roles that did not work on this project

The full organisation exists for every application; only the part a project needs
is activated. These roles were staffed but produced nothing here, which is a
deliberate outcome rather than an omission:

- Accessibility Engineer
- Application Intake
- AppSec Engineer
- Automation Engineer
- Business Analyst
- Business Sponsor
- Change Management
- Data / AI Director
- Data / AI Engineer
- Deployment Agent
- DevOps Engineer
- Domain SME
- E2E Engineer
- Engineering / AI Director
- Engineering Manager
- Feedback / Telemetry Agent
- Forward Deployed Engineer
- Incident Agent
- Infrastructure Engineer
- Integration Engineer
- Observability Agent
- Performance Engineer
- Product Manager
- Portfolio / Program Director
- Qa
- Release Engineer
- Requirements Engineer
- Security Director
- Spec Completeness Validator
- SRE
- UI Designer
- UX Designer
- UX Researcher
