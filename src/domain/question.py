# question.py
from pydantic import BaseModel

class Question(BaseModel):
    text: str

    class Config:
        orm_mode = True
