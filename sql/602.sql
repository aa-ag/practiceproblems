SELECT 
    accepter_id,
    COUNT(*) n
FROM RequestAccepted
GROUP BY accepter_id
UNION
SELECT 
    requester_id,
    COUNT(*) n
FROM RequestAccepted
GROUP BY requester_id;