# question_manager.py
from typing import List, Dict
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.domain.question import Question
from ai_software_factory.services.audit_logger import AuditLogger
from ai_software_factory.services.sql_generator import SQLGenerator

class QuestionManagerService:
    def __init__(self, conversation_repo: ConversationRepository, audit_logger: AuditLogger, sql_generator: SQLGenerator):
        self.conversation_repo = conversation_repo
        self.audit_logger = audit_logger
        self.sql_generator = sql_generator

    def ask_question(self, question: Question) -> None:
        query = self.sql_generator.generate_query(question)
        if not query.is_read_only():
            raise ValueError("Generated SQL is not read-only")
        result = self.conversation_repo.save_question_and_query(question, query)
        self.audit_logger.log_question(question, query, result)

    def get_conversation_history(self) -> List[Dict]:
        return self.conversation_repo.get_conversation_history()