SELECT
    contest_id,
    COUNT(*) n
FROM Register
GROUP BY contest_id
ORDER BY n DESC;