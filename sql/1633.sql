SELECT
    contest_id,
    COUNT(*) percentage
FROM Register
GROUP BY contest_id
ORDER BY contest_id ASC;