# -*- coding: utf-8 -*-

from typing import List, Dict, Any
from fastapi import HTTPException
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.utils.logging import logger
import httpx
from sqlalchemy import text
from sqlalchemy.orm import Session
import os

OLLAMA_URL = "http://127.0.0.1:11434"
MODEL = "qwen2.5-coder:7b"

Settings = type("Settings", (), {
    "database_url": os.getenv("DATABASE_URL", "sqlite:///./app.db")
})

async def ask_model(system: str, user: str) -> str:
    response = httpx.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": MODEL,
            "stream": False,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        },
        timeout=120.0,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]

async def run_read_only(db: Session, sql: str, params: dict) -> list[dict]:
    rows = db.execute(text(sql), params).mappings().all()
    return [dict(r) for r in rows]

class ConversationService:
    def __init__(self, conversation_repo: ConversationRepository):
        self.conversation_repo = conversation_repo

    async def create_conversation(self, question: str, sql_query: str) -> str:
        try:
            if "INSERT" in sql_query.upper() or "DELETE" in sql_query.upper():
                raise HTTPException(status_code=403, detail="Refused to execute write query")

            result = await ask_model(system="", user=question)
            conversation_id = self.conversation_repo.create_conversation(question, sql_query, result)
            logger.info("query executed", extra={"rows": len(result), "ms": 0})
            return conversation_id
        except Exception as e:
            logger.error(f"Error creating conversation: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def add_question_to_conversation(self, conversation_id: str, question: str, sql_query: str, result: List[Dict[str, Any]]) -> None:
        try:
            if "INSERT" in sql_query.upper() or "DELETE" in sql_query.upper():
                raise HTTPException(status_code=403, detail="Refused to execute write query")

            self.conversation_repo.add_question_to_conversation(conversation_id, question, sql_query, result)
            logger.info("query executed", extra={"rows": len(result), "ms": 0})
        except Exception as e:
            logger.error(f"Error adding question to conversation: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def get_conversation_history(self, conversation_id: str) -> List[Dict[str, Any]]:
        try:
            return self.conversation_repo.get_conversation_history(conversation_id)
        except Exception as e:
            logger.error(f"Error retrieving conversation history: {e}")
            raise HTTPException(status_code=500, detail=str(e))