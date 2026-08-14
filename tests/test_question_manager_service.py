# test_question_manager_service.py
import pytest
from ai_software_factory.services.question_manager_service import QuestionManagerService
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.domain.question import Question
from ai_software_factory.services.audit_logger import AuditLoggerService

@pytest.fixture
def question_manager_service():
    conversation_repo = ConversationRepository()
    audit_logger = AuditLoggerService()
    return QuestionManagerService(conversation_repo, audit_logger)

def test_ask_question(question_manager_service):
    question = Question(text="SELECT * FROM users")
    response = question_manager_service.ask_question(question)
    assert isinstance(response, dict)
    assert 'sql' in response

def test_get_conversation_history(question_manager_service):
    conversation_history = question_manager_service.get_conversation_history()
    assert isinstance(conversation_history, list)