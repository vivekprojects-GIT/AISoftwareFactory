# question_service.py

class QuestionService:
    def __init__(self, repository):
        self.repository = repository

    def ask_question(self, question):
        # Implement logic to parse the plain English question and generate SQL
        sql_query = self.generate_sql(question)
        result = self.execute_sql(sql_query)
        return sql_query, result

    def generate_sql(self, question):
        # Placeholder for generating SQL based on plain English question
        return 'SELECT * FROM data WHERE condition = 1'

    def execute_sql(self, sql_query):
        # Placeholder for executing the generated SQL query
        return {'result': 'data'}
