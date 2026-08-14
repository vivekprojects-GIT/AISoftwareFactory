# -*- coding: utf-8 -*-

import httpx

from ai_software_factory.domain.models import QueryResult
import logging

logger = logging.getLogger(__name__)

class ConversationRepository:
    def __init__(self, session: httpx.Client):
        self.session = session

    async def add_question_to_conversation(self, user_question: str, sql_query: str) -> None:
        try:
            # Log the conversation history
            logger.info(f'User question: {user_question}, SQL query: {sql_query}')
        except Exception as e:
            logger.error(f'Error adding question to conversation: {e}', extra={'user_question': user_question, 'sql_query': sql_query})

    async def get_conversation_history(self) -> list[QueryResult]:
        try:
            # Retrieve the conversation history from the database
            pass
        except Exception as e:
            logger.error(f'Error retrieving conversation history: {e}')
            raise
