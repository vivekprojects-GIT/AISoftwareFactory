CREATE TRIGGER add_question_to_conversation
AFTER INSERT ON conversation
BEGIN
    INSERT INTO sql_query (query, is_read_only)
    VALUES ('SELECT * FROM conversation WHERE id = NEW.id', TRUE);
END;
-- Rollback: DROP TRIGGER IF EXISTS add_question_to_conversation;