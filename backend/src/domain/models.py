# -*- coding: utf-8 -*-

from typing import List, Any

class QueryResult:
    def __init__(self, query: str, result: List[Any]):
        self.query = query
        self.result = result
