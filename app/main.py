#!/usr/bin/env python

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.services.conversation_service import ConversationService
from src.repositories.conversation_repository import ConversationRepository
from src.domain.conversation_domain import Question, Answer

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post('/ask', response_model=Answer)
async def ask_question(question_request: QuestionRequest, db: Session = Depends(ConversationService.get_db)):
    conversation_service = ConversationService(db)
    answer = await conversation_service.ask_question(question_request.question)
    return Answer(answer=answer.sql_query, result=answer.result)

@app.post('/conversations', response_model=Answer)
async def create_conversation(conversation_request: QuestionRequest, db: Session = Depends(ConversationService.get_db)):
    conversation_service = ConversationService(db)
    answer = await conversation_service.create_conversation(question_request.question)
    return Answer(answer=answer.sql_query, result=answer.result)

@app.get('/conversations/{conversation_id}', response_model=Answer)
async def get_conversation(conversation_id: int, db: Session = Depends(ConversationService.get_db)):
    conversation_service = ConversationService(db)
    answer = await conversation_service.get_conversation(conversation_id)
    return Answer(answer=answer.sql_query, result=answer.result)