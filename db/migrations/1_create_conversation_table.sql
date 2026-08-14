CREATE TABLE conversation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE question (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER,
    text TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (conversation_id) REFERENCES conversation(id)
);

CREATE TABLE answer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER,
    sql_query TEXT NOT NULL,
    result_count INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES question(id)
);