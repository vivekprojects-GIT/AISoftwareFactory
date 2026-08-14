# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

def validate_sql_query(user_question: str) -> bool:
    try:
        # Validate the SQL query
        pass
    except Exception as e:
        logger.error(f'Error validating SQL query: {e}', extra={'user_question': user_question})
        raise

def is_read_only(sql_query: str) -> bool:
    try:
        # Check if the query is read-only
        pass
    except Exception as e:
        logger.error(f'Error checking if query is read-only: {e}', extra={'sql_query': sql_query})
        raise
