SELECT
    DISTINCT id,
    COUNT(DISTINCT friend) friend_count
FROM
    (SELECT 
        requester_id AS id,
        accepter_id AS friend
    FROM RequestAccepted
    UNION
    SELECT 
        accepter_id AS id,
        requester_id  AS friend
    FROM RequestAccepted) t
GROUP BY id;