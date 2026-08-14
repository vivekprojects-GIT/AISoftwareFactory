import unittest
from sqlalchemy.orm import Session
from db.models.conversation import Conversation
from db.repositories.conversation_repository import add_question_to_conversation, get_conversation_history

class TestConversation(unittest.TestCase):
    def test_add_question_to_conversation(self, db: Session):
        question = 'What is the average salary of employees in department 10?'
        answer = 'SELECT AVG(salary) FROM employees WHERE department_id = 10;'
        sql_query = 'SELECT AVG(salary) FROM employees WHERE department_id = 10;'
        add_question_to_conversation(db, question, answer, sql_query)
        conversation = db.query(Conversation).filter_by(question=question).first()
        self.assertIsNotNone(conversation)
        self.assertEqual(conversation.question, question)
        self.assertEqual(conversation.answer, answer)
        self.assertEqual(conversation.sql_query, sql_query)

    def test_get_conversation_history(self, db: Session):
        question = 'What is the average salary of employees in department 10?'
        answer = 'SELECT AVG(salary) FROM employees WHERE department_id = 10;'
        sql_query = 'SELECT AVG(salary) FROM employees WHERE department_id = 10;'
        add_question_to_conversation(db, question, answer, sql_query)
        history = get_conversation_history(db)
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].question, question)
        self.assertEqual(history[0].answer, answer)
        self.assertEqual(history[0].sql_query, sql_query)