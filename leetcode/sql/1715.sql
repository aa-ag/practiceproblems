SELECT 
    SUM(b.apple_count) + COALESCE(SUM(c.apple_count),0) AS apple_count,
    SUM(b.orange_count) + COALESCE(SUM(c.orange_count),0) AS orange_count
FROM Boxes b
LEFT JOIN Chests c
USING(chest_id);