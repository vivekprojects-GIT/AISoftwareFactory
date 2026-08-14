INSERT INTO question (conversation_id, text) VALUES (1, 'What is the average salary?');
SELECT * FROM question WHERE conversation_id = 1 AND text = 'What is the average salary?';