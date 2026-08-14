# -*- coding: utf-8 -*-

import logging
from time import time

from sqlalchemy.orm import Session

from ai_software_factory.ai_factory import run_read_only
from ai_software_factory.domain.sql_query import is_read_only
from ai_software_factory.repositories.conversation_repository import add_question_to_conversation
from ai_software_factory.utils.logging import logger

logger = logging.getLogger(__name__)

class SQLService:
    def __init__(self, session: Session):
        self.session = session

    async def ask(self, question: str) -> dict:
        try:
            if is_read_only(question):
                raise ValueError('Generated query would write or delete data and is refused.')

            start_time = time()
            sql_query = await run_read_only(question)
            elapsed_ms = int((time() - start_time) * 1000)
            result = await self.session.execute(sql_query)
            rows = result.scalars().all()
            add_question_to_conversation(self.session, question, sql_query, len(rows))

            logger.info('query executed', extra={'rows': len(rows), 'ms': elapsed_ms})

            return {
                'sql_query': str(sql_query),
                'result': rows,
            }
        except Exception as e:
            logger.error(f'Error processing question: {e}', exc_info=True)
            raise ValueError('An error occurred while processing the question.') from e