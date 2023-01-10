SELECT
    customer_id,
    product_id,
    COUNT(product_id) n
FROM Orders
GROUP BY customer_id, product_id
ORDER BY customer_id ASC;
