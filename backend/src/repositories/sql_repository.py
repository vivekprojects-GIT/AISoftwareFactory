# -*- coding: utf-8 -*-

from sqlalchemy import text

from sqlalchemy.orm import Session


def execute_query(db: Session, sql: str) -> list:
    result = db.execute(text(sql)).fetchall()
    return result


def validate_sql_query(sql: str) -> bool:
    # Add logic to validate the SQL query
    return True  # Placeholder for validation logic
