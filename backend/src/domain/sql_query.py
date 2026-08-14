# -*- coding: utf-8 -*-

import httpx
from sqlalchemy.orm import Session
from backend.src.services.sql_service import run_read_only
from backend.src.utils.logger import logger

OLLAMA_URL = "http://127.0.0.1:11434"
MODEL = "qwen2.5-coder:7b"


async def ask_model(system: str, user: str) -> str:
    response = httpx.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": MODEL,
            "stream": False,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        },
        timeout=120.0,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


def is_read_only(db: Session, sql: str) -> bool:
    try:
        run_read_only(db, sql, {})
        return True
    except Exception as e:
        logger.error(f"Query rejected: {e}", extra={"sql": sql})
        return False
