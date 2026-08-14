# -*- coding: utf-8 -*-

from typing import List, Dict, Any
from fastapi import HTTPException
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.utils.logging import logger
import httpx

OLLAMA_URL = "http://127.0.0.1:11434"
MODEL = "qwen2.5-coder:7b"

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

class SQLService:
    def __init__(self, conversation_repo: ConversationRepository):
        self.conversation_repo = conversation_repo

    async def validate_sql_query(self, sql_query: str) -> None:
        try:
            if "INSERT" in sql_query.upper() or "UPDATE" in sql_query.upper() or "DELETE" in sql_query.upper():
                raise HTTPException(status_code=403, detail="Write operations are not allowed")
        except Exception as e:
            logger.error(f"Error validating SQL query: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def generate_sql_query(self, question: str) -> str:
        try:
            return await ask_model(system="You are an expert in understanding and deconstructing natural language into SQL components.", user=question)
        except Exception as e:
            logger.error(f"Error generating SQL query: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def run_read_only(self, sql_query: str) -> List[Dict[str, Any]]:
        try:
            return await self.conversation_repo.run_read_only(sql_query)
        except Exception as e:
            logger.error(f"Error executing SQL query: {e}")
            raise HTTPException(status_code=500, detail=str(e))