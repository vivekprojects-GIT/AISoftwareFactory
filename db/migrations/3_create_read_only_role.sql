CREATE ROLE read_only;
GRANT SELECT ON conversation TO read_only;
GRANT SELECT ON question TO read_only;
GRANT SELECT ON answer TO read_only;