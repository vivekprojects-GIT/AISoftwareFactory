# question_repository.py

class QuestionRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def execute_query(self, query):
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result