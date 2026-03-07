-- Lesson 3.3 (SQLite): INNER JOIN / LEFT JOIN + keys + duplicates pitfalls

-- ============================================================
-- 0) SETUP (run once)
-- ============================================================

DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY,
  full_name   TEXT NOT NULL,
  country     TEXT NOT NULL
);

CREATE TABLE orders (
  order_id    INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  order_total REAL NOT NULL,
  created_at  TEXT NOT NULL
);

CREATE TABLE tickets (
  ticket_id   INTEGER PRIMARY KEY,
  created_at  TEXT NOT NULL,
  channel     TEXT NOT NULL,
  topic       TEXT NOT NULL,
  priority    TEXT NOT NULL,
  status      TEXT NOT NULL,
  agent       TEXT,
  customer_id INTEGER,
  order_id    INTEGER
);

INSERT INTO customers (customer_id, full_name, country) VALUES
(1, 'Maria Rossi', 'IT'),
(2, 'Luca Bianchi', 'IT'),
(3, 'Anna Smith', 'US');

INSERT INTO orders (order_id, customer_id, order_total, created_at) VALUES
(101, 1, 120.50, '2026-01-02'),
(102, 1,  35.00, '2026-01-18'),
(103, 2, 250.00, '2026-02-03');

INSERT INTO tickets (ticket_id, created_at, channel, topic, priority, status, agent, customer_id, order_id) VALUES
(1,  '2026-01-02', 'email', 'refund',   'high',   'open',    'maria', 1, 101),
(2,  '2026-01-03', 'chat',  'shipping', 'medium', 'closed',  'luca',  2, 103),
(3,  '2026-01-05', 'email', 'bug',      'high',   'open',    NULL,    1, NULL),
(4,  '2026-01-07', 'chat',  'billing',  'low',    'pending', 'maria', NULL, NULL),
(5,  '2026-01-10', 'email', 'shipping', 'medium', 'open',    'luca',  2, NULL),
(6,  '2026-01-12', 'chat',  'refund',   'high',   'closed',  'anna',  3, NULL),
(7,  '2026-01-15', 'email', 'refund',   'medium', 'open',    'maria', 1, 102),
(8,  '2026-02-01', 'chat',  'bug',      'high',   'open',    'anna',  3, NULL),
(9,  '2026-02-02', 'email', 'billing',  'low',    'closed',  NULL,    99, NULL),
(10, '2026-02-05', 'chat',  'shipping', 'medium', 'pending', 'luca',  2, NULL);

-- sanity checks (expected: 3, 3, 10)
SELECT COUNT(*) AS customers_cnt FROM customers;  -- 3
SELECT COUNT(*) AS orders_cnt    FROM orders;     -- 3
SELECT COUNT(*) AS tickets_cnt   FROM tickets;    -- 10


-- ============================================================
-- 1) TASK 1 — INNER JOIN (tickets + customer name/country)
-- Only rows where customer exists in customers
-- ============================================================

SELECT
  t.ticket_id,
  t.status,
  c.full_name,
  c.country
FROM tickets t
INNER JOIN customers c
  ON t.customer_id = c.customer_id
ORDER BY t.ticket_id;

-- Expected (8 rows): ticket_id present = 1,2,3,5,6,7,8,10
-- Missing: 4 (customer_id NULL), 9 (customer_id 99 not found)
-- Sample rows (exact):
-- 1 | open    | Maria Rossi  | IT
-- 2 | closed  | Luca Bianchi | IT
-- 3 | open    | Maria Rossi  | IT
-- 5 | open    | Luca Bianchi | IT
-- 6 | closed  | Anna Smith   | US
-- 7 | open    | Maria Rossi  | IT
-- 8 | open    | Anna Smith   | US
-- 10| pending | Luca Bianchi | IT


-- ============================================================
-- 2) TASK 2 — LEFT JOIN (show ALL tickets + customer name if exists)
-- ============================================================

SELECT
  t.ticket_id,
  t.status,
  t.customer_id,
  c.full_name
FROM tickets t
LEFT JOIN customers c
  ON t.customer_id = c.customer_id
ORDER BY t.ticket_id;

-- Expected (10 rows):
-- ticket 4 => customer_id NULL, full_name NULL
-- ticket 9 => customer_id 99,   full_name NULL
-- all other tickets have full_name filled


-- ============================================================
-- 3) TASK 3 — Metric after JOIN: tickets count by customer country
-- Shows NULL country bucket for tickets without a matched customer
-- ============================================================

SELECT
  c.country,
  COUNT(*) AS tickets_cnt
FROM tickets t
LEFT JOIN customers c
  ON t.customer_id = c.customer_id
GROUP BY c.country
ORDER BY tickets_cnt DESC;

-- Expected groups (3 rows total):
-- IT   | 6   (tickets: 1,2,3,5,7,10)
-- NULL | 2   (tickets: 4 (no customer), 9 (bad customer_id=99))
-- US   | 2   (tickets: 6,8)


-- ============================================================
-- 4) TASK 4 — Join tickets to orders to bring order_total
-- ============================================================

SELECT
  t.ticket_id,
  t.topic,
  t.order_id,
  o.order_total
FROM tickets t
LEFT JOIN orders o
  ON t.order_id = o.order_id
ORDER BY t.ticket_id;

-- Expected:
-- ticket 1 => order_id 101, order_total 120.50
-- ticket 2 => order_id 103, order_total 250.00
-- ticket 7 => order_id 102, order_total  35.00
-- all other tickets => order_id NULL, order_total NULL


-- ============================================================
-- 5) TASK 5 — The classic trap:
-- LEFT JOIN + WHERE on right table column turns into "accidental INNER"
-- ============================================================

-- 5a) Trap version (drops rows where c is NULL)
SELECT COUNT(*) AS rows_after_join
FROM tickets t
LEFT JOIN customers c ON t.customer_id = c.customer_id
WHERE c.country = 'IT';

-- Expected: 6 rows (only matched IT customers)

-- 5b) Fixed version (keeps tickets with no matched customer too)
SELECT COUNT(*) AS rows_after_join
FROM tickets t
LEFT JOIN customers c ON t.customer_id = c.customer_id
WHERE c.country = 'IT' OR c.country IS NULL;

-- Expected: 8 rows (IT matched 6 + NULL-country 2). US excluded.
