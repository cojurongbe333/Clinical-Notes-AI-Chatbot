
-- SQL schema for summarization logs
CREATE TABLE summary_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    timestamp DATETIME,
    department TEXT,
    note_type TEXT,
    note_word_count INTEGER,
    summary_word_count INTEGER,
    question TEXT,
    answer_tokens INTEGER,
    response_latency_sec REAL
);
