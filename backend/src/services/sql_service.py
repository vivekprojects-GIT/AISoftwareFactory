# -*- coding: utf-8 -*-

from ai_software_factory.ai_factory import ask_model, run_read_only
from ai_software_factory.domain.models import QueryResult
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.utils.logger import logger

class SQLService:
    def __init__(self, conversation_repo: ConversationRepository):
        self.conversation_repo = conversation_repo

    async def ask_question(self, question: str) -> QueryResult:
        try:
            sql_query = await self.generate_sql_query(question)
            result = await run_read_only(sql_query)
            return QueryResult(query=sql_query, result=result)
        except Exception as e:
            logger.error(f'Error processing query: {e}', extra={'question': question})
            raise

    async def generate_sql_query(self, question: str) -> str:
        try:
            sql_query = await ask_model(system='You are an expert in understanding and deconstructing natural language into SQL components.', user=question)
            if not self.is_read_only(sql_query):
                raise ValueError('Generated query would write or delete data')
            return sql_query
        except Exception as e:
            logger.error(f'Error generating SQL query: {e}', extra={'question': question})
            raise

    def is_read_only(self, sql_query: str) -> bool:
        # Check if the generated SQL query is read-only
        return 'INSERT INTO' not in sql_query and 'UPDATE' not in sql_query and 'DELETE FROM' not in sql_query