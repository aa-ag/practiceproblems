SELECT
    from_id person1,
    to_id person2,
    COUNT(*) call_count
FROM Calls
GROUP BY from_id;