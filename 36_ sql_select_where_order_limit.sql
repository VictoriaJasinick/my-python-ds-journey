-- 30_sql_01_tickets_schema_selects.sql
-- Improved SQL schema (types + constraints) + basic query practice.
-- Notes:
-- - created_at stored as TEXT in ISO-8601 format 'YYYY-MM-DD' (SQLite best practice for dates)
-- - added NOT NULL, CHECK constraints, and sensible defaults

DROP TABLE IF EXISTS tickets;

CREATE TABLE tickets (
  ticket_id INTEGER PRIMARY KEY,
  created_at TEXT NOT NULL
    CHECK (created_at GLOB '[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]'),
  channel TEXT NOT NULL
    CHECK (channel IN ('email', 'chat', 'phone')),
  priority TEXT NOT NULL
    CHECK (priority IN ('low', 'medium', 'high')),
  status TEXT NOT NULL DEFAULT 'open'
    CHECK (status IN ('open', 'closed', 'pending')),
  user_id INTEGER NOT NULL CHECK (user_id > 0),
  subject TEXT NOT NULL CHECK (length(subject) > 0),
  response_time_min INTEGER NOT NULL CHECK (response_time_min >= 0)
);

INSERT INTO tickets (ticket_id, created_at, channel, priority, status, user_id, subject, response_time_min)
VALUES
  (101, '2026-01-10', 'email', 'high',   'open',   1, 'refund request', 180),
  (102, '2026-01-11', 'chat',  'low',    'closed', 2, 'password reset', 15),
  (103, '2026-01-12', 'email', 'medium', 'open',   3, 'delivery delay', 90);

-- Task 1: Show ticket_id, subject, status for all tickets
SELECT ticket_id, subject, status
FROM tickets;

-- Task 2: Show all open tickets
SELECT *
FROM tickets
WHERE status = 'open';

-- Task 3: Show tickets where channel is 'email' AND priority is 'high'
SELECT *
FROM tickets
WHERE channel = 'email' AND priority = 'high';

-- Task 4: Show tickets with response_time_min > 60, sorted by response_time_min DESC
SELECT *
FROM tickets
WHERE response_time_min > 60
ORDER BY response_time_min DESC;

-- Task 5: Show tickets where subject contains the word 'refund'
SELECT *
FROM tickets
WHERE subject LIKE '%refund%';

-- Task 6: Show 3 newest tickets (by created_at)
SELECT *
FROM tickets
ORDER BY created_at DESC
LIMIT 3;
