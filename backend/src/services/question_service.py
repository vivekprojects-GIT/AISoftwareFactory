# -*- coding: utf-8 -*-

from typing import List, Dict, Any
from fastapi import HTTPException
from ai_software_factory.repositories.conversation_repository import ConversationRepository
from ai_software_factory.services.sql_service import validate_sql_query, generate_sql_query
from ai_software_factory.services.conversation_service import create_conversation, add_question_to_conversation, get_conversation_history
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

async def run_read_only(sql: str, params: dict) -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": MODEL,
                "stream": False,
                "messages": [
                    {"role": "system", "content": "You are a SQL query generator."},
                    {"role": "user", "content": sql},
                ],
            },
            timeout=120.0,
        )
    response.raise_for_status()
    return response.json()["message"]["content"]

class QuestionService:
    def __init__(self, conversation_repo: ConversationRepository):
        self.conversation_repo = conversation_repo

    async def ask_question(self, question: str) -> Dict[str, Any]:
        try:
            # Validate the input question
            if not question.strip():
                raise HTTPException(status_code=400, detail="Question cannot be empty")

            # Generate SQL query using a hypothetical model service (e.g., Ollama)
            sql_query = await ask_model(system="You are a SQL query generator.", user=question)

            # Validate the generated SQL query
            validate_sql_query(sql_query)

            # Execute the read-only query and get results
            result = await run_read_only(sql_query, {})

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