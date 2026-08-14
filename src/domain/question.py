# question.py

class Question:
    def __init__(self, id, text, answer, sql_query):
        self.id = id
        self.text = text
        self.answer = answer
        self.sql_query = sql_query