SELECT
    from_id person1,
    to_id person2,
    COUNT(*) call_count,
    SUM(duration) total_duration
FROM Calls
GROUP BY from_id,to_id;