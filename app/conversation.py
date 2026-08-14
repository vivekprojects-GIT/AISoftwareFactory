# Conversation model

from pydantic import BaseModel
from typing import List

class Answer(BaseModel):
    question: str
    sql_query: str
    result_count: int

class ConversationCreate(BaseModel):
    id: int
    answers: List[Answer]

class Conversation(BaseModel):
    id: int
    answers: List[Answer]
