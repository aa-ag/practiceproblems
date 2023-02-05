-- 1069. Product Sales Analysis II
SELECT p.product_id,SUM(s.quantity) total_quantity
FROM Product p
JOIN Sales s
ON p.product_id=s.product_id
GROUP BY p.product_id;

SELECT product_id, sum(quantity) as total_quantity
FROM sales
GROUP BY product_id

-- 1211. Queries Quality and Percentage
SELECT
    query_name,
    ROUND(SUM((rating / position)) / COUNT(query_name),2) quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(query_name) * 100,2) poor_query_percentage
FROM Queries
GROUP BY query_name;