# audit_logger.py
from ai_software_factory.domain.question import Question
from ai_software_factory.domain.query import Query

class AuditLoggerService:
    def log_question(self, question: Question) -> None:
        # Implement the logic to log the question
        print(f'Question logged: {question.text}')

    def log_query(self, query: Query) -> None:
        # Implement the logic to log the query and its results
        print(f'Query logged: {query.sql}
Results: {query.results}')