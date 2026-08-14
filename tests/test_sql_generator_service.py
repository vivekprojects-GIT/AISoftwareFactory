# test_sql_generator_service.py
import pytest
from ai_software_factory.services.sql_generator_service import SQLGeneratorService
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.domain.question import Question
from ai_software_factory.domain.query import Query

@pytest.fixture
def sql_generator_service():
    conversation_repo = ConversationRepository()
    audit_logger = AuditLoggerService()
    return SQLGeneratorService(conversation_repo, audit_logger)

def test_generate_query(sql_generator_service):
    question = Question(text="SELECT * FROM users")
    query = sql_generator_service.generate_query(question)
    assert isinstance(query, Query)

def test_execute_query(sql_generator_service):
    question = Question(text="SELECT * FROM users")
    query = sql_generator_service.generate_query(question)
    results = sql_generator_service.execute_query(query)
    assert isinstance(results, list)
