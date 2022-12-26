SELECT
    DISTINCT user_id,
    COUNT(*) followers_count
FROM Followers
GROUP BY user_id;