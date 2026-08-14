-- CR-586: additive, reversible migration
ALTER TABLE credit_decision ADD COLUMN new_component TEXT NULL;
-- rollback: ALTER TABLE credit_decision DROP COLUMN new_component;
