#!/usr/bin/env python

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.services.question_service import QuestionService
from src.repositories.conversation_repository import ConversationRepository
from src.domain.question import Question
from src.infra.database import get_db

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post('/ask', response_model=Question)
async def ask_question(question_request: QuestionRequest, db: Session = Depends(get_db)):
    question_service = QuestionService(db)
    conversation_repository = ConversationRepository(db)
    try:
        result = await question_service.process_question(question_request.question)
        conversation_repository.save_conversation(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
