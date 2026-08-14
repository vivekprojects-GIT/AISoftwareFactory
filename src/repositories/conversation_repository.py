# conversation_repository.py
from typing import List, Dict
from ai_software_factory.domain.question import Question
from ai_software_factory.domain.query import Query
from ai_software_factory.services.audit_logger import AuditLogger
from ai_software_factory.services.sql_generator import SQLGenerator

class ConversationRepository:
    def save_question(self, question: Question) -> None:
        sql = SQLGenerator.generate_read_only_sql(question)
        AuditLogger.log_question(question)
        # Implement the logic to save the question and its generated SQL

    def save_query(self, query: Query) -> None:
        if not SQLGenerator.is_safe(query):
            raise ValueError("Generated query would write or delete data")
        AuditLogger.log_query(query)
        # Implement the logic to save the query and its results

    def get_conversation_history(self) -> List[Dict]:
        # Implement the logic to retrieve the conversation history
        return []