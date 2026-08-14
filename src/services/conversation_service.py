#!/usr/bin/env python

from sqlalchemy.orm import Session
from src.repositories.conversation_repository import ConversationRepository
from src.domain.conversation_domain import Question, Answer

class ConversationService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ConversationRepository(db)

    async def ask_question(self, question: str) -> Answer:
        return await self.repository.ask_question(question)

    async def create_conversation(self, question: str) -> Answer:
        return await self.repository.create_conversation(question)

    async def get_conversation(self, conversation_id: int) -> Answer:
        return await self.repository.get_conversation(conversation_id)