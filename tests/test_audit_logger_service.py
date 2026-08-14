# test_audit_logger_service.py
import pytest
from ai_software_factory.services.audit_logger_service import AuditLoggerService
from ai_software_factory.domain.question import Question
from ai_software_factory.domain.query import Query

@pytest.fixture
def audit_logger_service():
    return AuditLoggerService()

def test_log_question(audit_logger_service):
    question = Question(text="SELECT * FROM users")
    audit_logger_service.log_question(question)

def test_log_query(audit_logger_service):
    query = Query(sql="SELECT * FROM users", results=[{}])
    audit_logger_service.log_query(query)
