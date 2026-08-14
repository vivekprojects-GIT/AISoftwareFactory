# -*- coding: utf-8 -*-

import logging

from ai_software_factory.ai_factory import ask_model
from ai_software_factory.domain.sql_query import validate_sql_query, is_read_only
from ai_software_factory.repositories.conversation_repository import add_question_to_conversation
from ai_software_factory.utils.logging_utils import log_query_execution

logger = logging.getLogger(__name__)

async def ask_question(question: str) -> dict:
    try:
        # Validate the question
        validate_sql_query(question)

        # Check if the query is read-only
        if not is_read_only(question):
            raise ValueError('Generated SQL is read-only; anything that writes or deletes is refused')

        # Generate SQL using AI model
        sql = await ask_model(system='You are an expert in understanding and deconstructing natural language into SQL components.', user=question)

        # Log the query execution
        log_query_execution(sql, question)

        # Add the question to conversation history
        add_question_to_conversation(question, sql)

        return {
            'sql': sql,
            'query': question,
            'status': 'success'
        }
    except Exception as e:
        logger.error(f'Error processing question: {e}', exc_info=True)
        return {
            'error': str(e),
            'status': 'failure'
        }