# question_service.py

class QuestionService:
    def __init__(self, repository):
        self.repository = repository

    def ask_question(self, question):
        query = self._translate_to_sql(question)
        if self._is_read_only(query):
            result = self.repository.execute_query(query)
            return result, query
        else:
            raise ValueError('Generated SQL is read-only; anything that writes or deletes is refused')

    def _translate_to_sql(self, question):
        # Placeholder for translation logic
        return 'SELECT * FROM data WHERE 1=1'

    def _is_read_only(self, query):
        # Placeholder for read-only check
        return True