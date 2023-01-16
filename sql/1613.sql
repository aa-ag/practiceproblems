WITH RECURSIVE seq AS (
    SELECT 0 AS rng
    UNION ALL SELECT rng + 1
    FROM seq
    WHERE rng < 100
)

SELECT * FROM seq;