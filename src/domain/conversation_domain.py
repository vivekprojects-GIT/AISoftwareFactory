#!/usr/bin/env python

from pydantic import BaseModel

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    sql_query: str
    result: any