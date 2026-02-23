DROP TABLE IF EXISTS tickets;

CREATE TABLE tickets (
  ticket_id   INTEGER PRIMARY KEY,
  created_at  TEXT NOT NULL,      -- YYYY-MM-DD
  channel     TEXT NOT NULL,      -- email/chat
  topic       TEXT NOT NULL,      -- refund/shipping/bug/billing
  priority    TEXT NOT NULL,      -- low/medium/high
  status      TEXT NOT NULL,      -- open/pending/closed
  agent       TEXT               -- can be NULL (unassigned)
);

INSERT INTO tickets (ticket_id, created_at, channel, topic, priority, status, agent) VALUES
(1,  '2026-01-02', 'email', 'refund',   'high',   'open',    'maria'),
(2,  '2026-01-03', 'chat',  'shipping', 'medium', 'closed',  'luca'),
(3,  '2026-01-05', 'email', 'bug',      'high',   'open',    NULL),
(4,  '2026-01-07', 'chat',  'billing',  'low',    'pending', 'maria'),
(5,  '2026-01-10', 'email', 'shipping', 'medium', 'open',    'luca'),
(6,  '2026-01-12', 'chat',  'refund',   'high',   'closed',  'anna'),
(7,  '2026-01-15', 'email', 'refund',   'medium', 'open',    'maria'),
(8,  '2026-02-01', 'chat',  'bug',      'high',   'open',    'anna'),
(9,  '2026-02-02', 'email', 'billing',  'low',    'closed',  NULL),
(10, '2026-02-05', 'chat',  'shipping', 'medium', 'pending', 'luca');

-- Quick sanity check: should return 10
SELECT COUNT(*) AS rows_in_tickets FROM tickets;

-- ============================================================
-- 1) GROUP BY: 1 column
-- Task: Count tickets by topic. Output: topic | cnt
-- ============================================================

SELECT
  topic,
  COUNT(*) AS cnt
FROM tickets
GROUP BY topic
ORDER BY cnt DESC, topic ASC;

-- ============================================================
-- 2) GROUP BY: 2 columns
-- Task: Count tickets by (channel, status). Output: channel | status | cnt
-- ============================================================

SELECT
  channel,
  status,
  COUNT(*) AS cnt
FROM tickets
GROUP BY channel, status
ORDER BY channel ASC, cnt DESC, status ASC;

-- ============================================================
-- 3) WHERE + GROUP BY
-- Task: Only January 2026, count by priority. Output: priority | cnt
-- ============================================================

SELECT
  priority,
  COUNT(*) AS cnt
FROM tickets
WHERE created_at >= '2026-01-01'
  AND created_at <  '2026-02-01'
GROUP BY priority
ORDER BY cnt DESC, priority ASC;

-- ============================================================
-- 4) HAVING (filters groups, not rows)
-- Task: Show only topics where COUNT(*) >= 2
-- ============================================================

SELECT
  topic,
  COUNT(*) AS cnt
FROM tickets
GROUP BY topic
HAVING COUNT(*) >= 2
ORDER BY cnt DESC, topic ASC;

-- ============================================================
-- 5) NULL logic: COUNT(*) vs COUNT(column)
-- Task: Compare COUNT(agent) vs COUNT(*) per status
-- Note: COUNT(column) ignores NULL values.
-- ============================================================

SELECT
  status,
  COUNT(*)     AS cnt_all_rows,
  COUNT(agent) AS cnt_with_agent
FROM tickets
GROUP BY status
ORDER BY cnt_all_rows DESC, status ASC;

-- ============================================================
-- Extra queries (3+), useful for "mini-pack" portfolio
-- ============================================================

-- 6) Unassigned tickets by topic (agent IS NULL)
-- Question: Which topics have unassigned tickets and how many?
SELECT
  topic,
  COUNT(*) AS unassigned_cnt
FROM tickets
WHERE agent IS NULL
GROUP BY topic
ORDER BY unassigned_cnt DESC, topic ASC;

-- 7) Tickets per agent per status (only assigned)
-- Question: For each agent, how many tickets in each status?
SELECT
  agent,
  status,
  COUNT(*) AS cnt
FROM tickets
WHERE agent IS NOT NULL
GROUP BY agent, status
ORDER BY agent ASC, cnt DESC, status ASC;

-- 8) Monthly volume by channel
-- Question: How many tickets came from each channel per month?
-- SQLite trick: substr(created_at, 1, 7) gives 'YYYY-MM'
SELECT
  substr(created_at, 1, 7) AS month,
  channel,
  COUNT(*) AS cnt
FROM tickets
GROUP BY month, channel
ORDER BY month ASC, channel ASC;

-- 9) Top topics in January (limit example)
-- Question: In January, which topics are most frequent?
SELECT
  topic,
  COUNT(*) AS cnt
FROM tickets
WHERE created_at >= '2026-01-01'
  AND created_at <  '2026-02-01'
GROUP BY topic
ORDER BY cnt DESC, topic ASC
LIMIT 2;

-- 10) Channels with at least 4 tickets overall (HAVING example)
-- Question: Which channels have volume >= 4?
SELECT
  channel,
  COUNT(*) AS cnt
FROM tickets
GROUP BY channel
HAVING COUNT(*) >= 4
ORDER BY cnt DESC, channel ASC;
