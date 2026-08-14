# -*- coding: utf-8 -*-

import httpx
from ai_software_factory.settings import Settings
from ai_software_factory.ai_factory import ask_model, run_read_only
from ai_software_factory.domain.sql_query import validate_sql_query, is_read_only
from ai_software_factory.repositories.conversation_repository import add_question_to_conversation, get_conversation_history
from ai_software_factory.utils.logging import logger

logger = logging.getLogger(__name__)

class SQLService:
    def __init__(self, session: Session):
        self.session = session

    async def ask(self, question: str) -> dict:
        try:
            if is_read_only(question):
                raise ValueError('Generated query would write or delete data and is refused.')

            sql_query = await run_read_only(question)
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