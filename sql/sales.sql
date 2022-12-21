-- 1069. Product Sales Analysis II
SELECT p.product_id,SUM(s.quantity) total_quantity
FROM Product p
JOIN Sales s
ON p.product_id=s.product_id
GROUP BY p.product_id;

SELECT product_id, sum(quantity) as total_quantity
FROM sales
GROUP BY product_id