# conversation_repository.py

import logging
from sqlalchemy.orm import Session
from models.conversation import Conversation
from models.generated_sql import GeneratedSQL

logger = logging.getLogger(__name__)

class ConversationRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_conversation(self, conversation_id: int) -> dict:
        # Logic to fetch conversation from the database
        conversation = self.db_session.query(Conversation).filter_by(id=conversation_id).first()
        if conversation:
            return conversation.to_dict()
        else:
            raise ValueError(f'Conversation with id {conversation_id} not found')

    def ask_question(self, question: str) -> dict:
        # Logic to generate SQL query and answer based on the question
        # Ensure no write or delete operations are performed
        sql_query = self.generate_sql(question)
        if 'DELETE' in sql_query.upper() or 'UPDATE' in sql_query.upper():
            raise ValueError('Generated SQL contains write or delete operations')
        result = self.db_session.execute(sql_query).fetchall()
        return {'sql': sql_query, 'result': [dict(row) for row in result]}

    def log_activity(self, conversation_id: int, question: str, answer: dict, sql_query: str):
        # Logic to log activity in the audit log
        logger.info(f'Conversation ID: {conversation_id}, Question: {question}, Answer: {answer}, SQL Query: {sql_query}')

    def get_generated_sql(self, query_id: int) -> str:
        # Logic to fetch generated SQL query from the database
        sql_query = self.db_session.query(GeneratedSQL).filter_by(id=query_id).first()
        if sql_query:
            return sql_query.query
        else:
            raise ValueError(f'Generated SQL with id {query_id} not found')
