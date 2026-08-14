-- This migration will be used to reject write queries
CREATE VIEW read_only_queries AS SELECT * FROM sql_query WHERE is_read_only = TRUE;
-- Rollback: DROP VIEW IF EXISTS read_only_queries;