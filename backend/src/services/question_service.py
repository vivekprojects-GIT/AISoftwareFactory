# -*- coding: utf-8 -*-

from typing import List, Dict, Any
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ai_software_factory.domain.models import QueryResult
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.services.sql_service import validate_sql_query, generate_sql_query
from ai_software_factory.services.conversation_service import create_conversation, add_question_to_conversation, get_conversation_history
from ai_software_factory.utils.logging import logger


class QuestionService:
    def __init__(self, conversation_repo: ConversationRepository):
        self.conversation_repo = conversation_repo

    async def ask_question(self, question: str) -> Dict[str, Any]:
        try:
            # Validate the input question
            if not question.strip():
                raise HTTPException(status_code=400, detail="Question cannot be empty")

            # Generate SQL query using a hypothetical model service (e.g., Ollama)
            sql_query = await generate_sql_query(question)

            # Validate the generated SQL query
            validate_sql_query(sql_query)

            # Execute the read-only query and get results
            result = await run_read_only(sql_query)

            # Create a new conversation or add to an existing one
            conversation_id = create_conversation(question, sql_query)
            add_question_to_conversation(conversation_id, question, sql_query, result)

            return {
                "conversation_id": conversation_id,
                "question": question,
                "sql_query": sql_query,
                "result": result,
            }
        except Exception as e:
            logger.error(f"Error processing question: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def get_conversation_history(self, conversation_id: str) -> List[Dict[str, Any]]:
        try:
            return await get_conversation_history(conversation_id)
        except Exception as e:
            logger.error(f"Error retrieving conversation history: {e}")
            raise HTTPException(status_code=500, detail=str(e))