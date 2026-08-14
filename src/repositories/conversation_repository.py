# conversation_repository.py
from typing import List, Dict
from ai_software_factory.domain.question import Question
from ai_software_factory.domain.query import Query

class ConversationRepository:
    def save_question(self, question: Question) -> None:
        # Implement the logic to save the question
        pass

    def save_query(self, query: Query) -> None:
        # Implement the logic to save the query and its results
        pass

    def get_conversation_history(self) -> List[Dict]:
        # Implement the logic to retrieve the conversation history
        pass
