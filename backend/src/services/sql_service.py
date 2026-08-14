# -*- coding: utf-8 -*-

import httpx
from ai_software_factory.ai_factory import ask_model, run_read_only
from ai_software_factory.domain.sql_query import validate_sql_query, is_read_only
from ai_software_factory.repositories.conversation_repository import add_question_to_conversation
from ai_software_factory.domain.models import QueryResult
import logging

logger = logging.getLogger(__name__)

class SQLService:
    def __init__(self, session: httpx.Client):
        self.session = session

    async def execute_query(self, user_question: str) -> QueryResult:
        try:
            # Validate the query
            if not validate_sql_query(user_question):
                raise ValueError('Invalid SQL query')

            # Check if the query is read-only
            if not is_read_only(user_question):
                raise PermissionError('Write queries are not allowed')

            # Execute the query using a local model server
            sql_query = await ask_model(system='You are an expert in understanding and deconstructing natural language into SQL components.', user=user_question)

            # Log the conversation history
            add_question_to_conversation(user_question, sql_query)

            # Run the read-only query using a local model server
            result = await run_read_only(sql_query)

            return QueryResult(query=sql_query, result=result)
        except Exception as e:
            logger.error(f'Error executing query: {e}', extra={'user_question': user_question})
            raise
