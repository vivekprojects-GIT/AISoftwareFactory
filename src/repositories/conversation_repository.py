#!/usr/bin/env python

from sqlalchemy.orm import Session
from src.domain.question import Question

class ConversationRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_conversation(self, question: Question):
        # Placeholder for actual logic to save conversation to the database
        pass
