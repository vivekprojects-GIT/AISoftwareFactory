# query.py
from pydantic import BaseModel

class Query(BaseModel):
    sql: str
    results: List[Dict]

    class Config:
        orm_mode = True
