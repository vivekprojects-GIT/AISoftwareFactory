# -*- coding: utf-8 -*-

from typing import List, Optional

class Conversation:
    def __init__(self, id: int, questions: List[str], answers: List[Optional[str]]):
        self.id = id
        self.questions = questions
        self.answers = answers

class QueryResult:
    def __init__(self, query: str, result: Optional[List[dict]] = None):
        self.query = query
        self.result = result
