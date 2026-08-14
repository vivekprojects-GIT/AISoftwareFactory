# Quality evidence

Every gate that ran, and what it found. A build is only as trustworthy as this
table: a gate that never ran proves nothing, and is listed as such.

| Run | Gate | Result | Criterion | Detail |
|---|---|---|---|---|
| RUN-B8F8AA4A | build_static | passed | — | {'checks': ['syntax', 'undefined-references', 'unused-imports', 'stub-detection', 'import- |
| RUN-B8F8AA4A | unit | skipped | — | {'suites': [], 'test_artifacts': ['tests/generated/CR-586_AC-2_security.test.md', 'tests/g |
| RUN-B8F8AA4A | contract | passed | — | {'breaking_changes': [], 'conformance': {'executed': False, 'reason': 'no contract/service |
| RUN-B8F8AA4A | integration | passed | — | {'participating_agents': ['api-architect', 'cloud-architect', 'data-architect', 'frontend' |
| RUN-B8F8AA4A | ui_e2e | passed | — | {'flows': ['login', 'review-decision', 'approve']} |
| RUN-B8F8AA4A | security | passed | — | {'secrets': [], 'prohibited_capabilities': [], 'new_dependency_signals': 0, 'checks': ['SA |
| RUN-B8F8AA4A | infrastructure | passed | — | {'policy_as_code': 'opa', 'changed': False} |
| RUN-B8F8AA4A | spec_compliance | passed | — | {'covered': ['AC-1', 'AC-2', 'AC-3'], 'uncovered': [], 'total': 3, 'reasons': {}, 'criteri |
| RUN-B8F8AA4A | performance | skipped | — | {'harness': None, 'criteria_awaiting_measurement': [], 'note': 'no load-test harness is in |
| RUN-B8F8AA4A | governance | passed | — | {'resolved_capabilities': ['design-system', 'local-model-runtime', 'observability', 'relat |
| RUN-B8F8AA4A | integration | passed | AC-1 | {'statement': 'A question in plain English returns an answer and the SQL that produced it' |
| RUN-B8F8AA4A | security | passed | AC-2 | {'statement': 'A generated query that would write or delete data is refused, not executed' |
| RUN-B8F8AA4A | unit | passed | AC-3 | {'statement': 'A conversation is saved and can be reopened later with its questions and an |
| RUN-57067112 | build_static | failed | — | {'checks': ['syntax', 'undefined-references', 'unused-imports', 'stub-detection', 'import- |
| RUN-57067112 | unit | skipped | — | {'suites': [], 'test_artifacts': ['tests/generated/CR-586_AC-2_security.test.md', 'tests/g |
| RUN-57067112 | contract | passed | — | {'breaking_changes': [], 'conformance': {'executed': False, 'reason': 'no contract/service |
| RUN-57067112 | integration | passed | — | {'participating_agents': ['api-architect', 'api-contract', 'backend', 'cloud-architect', ' |
| RUN-57067112 | ui_e2e | passed | — | {'flows': ['login', 'review-decision', 'approve']} |
| RUN-57067112 | security | passed | — | {'secrets': [], 'prohibited_capabilities': [], 'new_dependency_signals': 0, 'checks': ['SA |
| RUN-57067112 | infrastructure | passed | — | {'policy_as_code': 'opa', 'changed': False} |
| RUN-57067112 | spec_compliance | passed | — | {'covered': ['AC-1', 'AC-2', 'AC-3'], 'uncovered': [], 'total': 3, 'reasons': {}, 'criteri |
| RUN-57067112 | performance | skipped | — | {'harness': None, 'criteria_awaiting_measurement': [], 'note': 'no load-test harness is in |
| RUN-57067112 | governance | passed | — | {'resolved_capabilities': ['design-system', 'local-model-runtime', 'observability', 'relat |
| RUN-57067112 | integration | passed | AC-1 | {'statement': 'A question in plain English returns an answer and the SQL that produced it' |
| RUN-57067112 | security | passed | AC-2 | {'statement': 'A generated query that would write or delete data is refused, not executed' |
| RUN-57067112 | unit | passed | AC-3 | {'statement': 'A conversation is saved and can be reopened later with its questions and an |
| RUN-09038735 | build_static | passed | — | {'checks': ['syntax', 'undefined-references', 'unused-imports', 'stub-detection', 'import- |
| RUN-09038735 | unit | skipped | — | {'suites': [], 'test_artifacts': ['src/test/generated/NewComponentTest.md', 'tests/generat |
| RUN-09038735 | contract | passed | — | {'breaking_changes': [], 'conformance': {'executed': False, 'reason': 'no contract/service |
| RUN-09038735 | integration | passed | — | {'participating_agents': ['api-architect', 'api-contract', 'backend', 'cloud-architect', ' |
| RUN-09038735 | ui_e2e | passed | — | {'flows': ['login', 'review-decision', 'approve']} |
| RUN-09038735 | security | passed | — | {'secrets': [], 'prohibited_capabilities': [], 'new_dependency_signals': 0, 'checks': ['SA |
| RUN-09038735 | infrastructure | passed | — | {'policy_as_code': 'opa', 'changed': False} |
| RUN-09038735 | spec_compliance | passed | — | {'covered': ['AC-1', 'AC-2', 'AC-3'], 'uncovered': [], 'total': 3, 'reasons': {}, 'criteri |
| RUN-09038735 | performance | skipped | — | {'harness': None, 'criteria_awaiting_measurement': [], 'note': 'no load-test harness is in |
| RUN-09038735 | governance | passed | — | {'resolved_capabilities': ['design-system', 'local-model-runtime', 'observability', 'relat |
| RUN-09038735 | integration | passed | AC-1 | {'statement': 'A question in plain English returns an answer and the SQL that produced it' |
| RUN-09038735 | security | passed | AC-2 | {'statement': 'A generated query that would write or delete data is refused, not executed' |
| RUN-09038735 | unit | passed | AC-3 | {'statement': 'A conversation is saved and can be reopened later with its questions and an |
