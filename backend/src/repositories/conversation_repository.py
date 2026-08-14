# -*- coding: utf-8 -*-

from ai_software_factory.domain.models import Conversation, QueryResult
from ai_software_factory.services.sql_service import run_read_only
from sqlalchemy.orm import Session
from typing import List
import httpx
import logging

OLLAMA_URL = "http://127.0.0.1:11434"
MODEL = "qwen2.5-coder:7b"
logger = logging.getLogger(__name__)

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

class ConversationRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_conversation(self, conversation: Conversation) -> None:
        self.session.add(conversation)
        self.session.commit()

    async def add_question_to_conversation(self, conversation_id: int, question: str) -> QueryResult:
        try:
            sql_query = await ask_model(system="", user=question)
            result = await run_read_only(self.session, sql_query, {})
            query_result = QueryResult(sql_query=sql_query, result=result)
            conversation = self.session.query(Conversation).filter_by(id=conversation_id).first()
            if conversation:
                conversation.history.append(query_result)
                self.session.commit()
                return query_result
        except Exception as e:
            logger.error(f"Error adding question to conversation: {e}")
            raise

    def get_conversation_history(self, conversation_id: int) -> List[QueryResult]:
        conversation = self.session.query(Conversation).filter_by(id=conversation_id).first()
        if conversation:
            return conversation.history
        else:
            return []