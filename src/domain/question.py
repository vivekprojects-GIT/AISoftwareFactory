#!/usr/bin/env python

class Question:
    def __init__(self, question: str, answer: str, sql_query: str):
        self.question = question
        self.answer = answer
        self.sql_query = sql_query
