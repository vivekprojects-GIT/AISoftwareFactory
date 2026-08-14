# -*- coding: utf-8 -*-

from typing import List, Dict, Any
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ai_software_factory.domain.models import QueryResult
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.services.sql_service import validate_sql_query, generate_sql_query
from ai_software_factory.services.conversation_service import create_conversation, add_question_to_conversation, get_conversation_history
from ai_software_factory.utils.logging import logger


class SQLService:
    def __init__(self, conversation_repo: ConversationRepository):
        self.conversation_repo = conversation_repo

    async def validate_sql_query(self, sql_query: str) -> None:
        try:
            # Implement validation logic here (e.g., check for write operations)
            if "INSERT" in sql_query.upper() or "UPDATE" in sql_query.upper() or "DELETE" in sql_query.upper():
                raise HTTPException(status_code=403, detail="Write operations are not allowed")
        except Exception as e:
            logger.error(f"Error validating SQL query: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def generate_sql_query(self, question: str) -> str:
        try:
            # Implement logic to generate SQL query using a hypothetical model service (e.g., Ollama)
            return await ask_model(system="You are an expert in understanding and deconstructing natural language into SQL components.", user=question)
        except Exception as e:
            logger.error(f"Error generating SQL query: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def run_read_only(self, sql_query: str) -> List[Dict[str, Any]]:
        try:
            # Implement logic to execute the read-only query and return results
            # This is a placeholder for actual database execution logic
            return []  # Replace with actual implementation
        except Exception as e:
            logger.error(f"Error executing SQL query: {e}")
            raise HTTPException(status_code=500, detail=str(e))