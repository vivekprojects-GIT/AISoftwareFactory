-- Add read-only role for analysts
CREATE ROLE analyst WITH LOGIN PASSWORD 'password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analyst;
GRANT USAGE ON SCHEMA public TO analyst;