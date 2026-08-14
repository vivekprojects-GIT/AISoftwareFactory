# conversation_service.py

class ConversationService:
    def __init__(self, repository):
        self.repository = repository

    def get_conversation(self, conversation_id):
        return self.repository.get_conversation(conversation_id)

    def ask_question(self, conversation_id, question):
        answer, sql_query = self.repository.ask_question(question)
        self.repository.log_activity(conversation_id, question, answer, sql_query)
        return answer, sql_query

    def get_generated_sql(self, conversation_id, query_id):
        return self.repository.get_generated_sql(query_id)