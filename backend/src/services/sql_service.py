# -*- coding: utf-8 -*-

import logging

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ai_software_factory.domain.sql_query import validate_sql_query
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.ai_factory import ask_model, run_read_only

logger = logging.getLogger(__name__)

class SQLService:
    def __init__(self, db: Session = Depends(run_read_only)):
        self.db = db
        self.conversation_repo = ConversationRepository(db)

    async def execute_query(self, query: str) -> dict:
        if not validate_sql_query(query):
            raise HTTPException(status_code=400, detail="Invalid SQL query")
        try:
            result = await ask_model(system="", user=query)
            return {
                "query": query,
                "result": result,
                "sql": query
            }
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")

    async def add_question_to_conversation(self, question: str) -> dict:
        try:
            result = await ask_model(system="", user=question)
            conversation_id = self.conversation_repo.add_question(question, result)
            return {
                "conversation_id": conversation_id,
                "question": question,
                "result": result
            }
        except Exception as e:
            logger.error(f"Error adding question to conversation: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")

    async def get_conversation_history(self, conversation_id: int) -> dict:
        try:
            history = self.conversation_repo.get_conversation_history(conversation_id)
            return {
                "conversation_id": conversation_id,
                "history": history
            }
        except Exception as e:
            logger.error(f"Error getting conversation history: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")