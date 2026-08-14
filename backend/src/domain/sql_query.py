# -*- coding: utf-8 -*-

from typing import Optional

class SQLQuery:
    def __init__(self, query: str):
        self.query = query

    def is_read_only(self) -> bool:
        # Implement logic to check if the SQL query is read-only
        return True  # Placeholder implementation
