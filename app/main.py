# AISoftwareFactory

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

class Question(BaseModel):
    text: str

class Answer(BaseModel):
    question: str
    sql_query: str
    result_count: int

@app.post('/ask', response_model=Answer)
def ask_question(question: Question, db: Session = Depends(get_db)):
    try:
        # Translate plain English question to SQL query
        sql_query = translate_to_sql(question.text)
        if is_write_or_delete_query(sql_query):
            raise HTTPException(status_code=403, detail='Generated query that would write or delete data is refused')
        result_count = execute_read_only_query(db, sql_query)
        return Answer(question=question.text, sql_query=sql_query, result_count=result_count)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/conversation/{id}', response_model=List[Answer])
def get_conversation(id: int, db: Session = Depends(get_db)):
    try:
        conversation = db.query(Conversation).filter(Conversation.id == id).first()
        if not conversation:
            raise HTTPException(status_code=404, detail='Conversation not found')
        return conversation.answers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/conversation', response_model=Conversation)
def create_conversation(conversation: ConversationCreate, db: Session = Depends(get_db)):
    try:
        new_conversation = Conversation(id=conversation.id, answers=conversation.answers)
        db.add(new_conversation)
        db.commit()
        db.refresh(new_conversation)
        return new_conversation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Helper functions

def translate_to_sql(question: str) -> str:
    # Implement translation logic here
    pass

def is_write_or_delete_query(sql_query: str) -> bool:
    # Check if query writes or deletes data
    return False

def execute_read_only_query(db: Session, sql_query: str) -> int:
    # Execute read-only query and return result count
    return 0