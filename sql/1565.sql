SELECT
    DATE_FORMAT(order_date, '%Y-%m') month,
    COUNT(DISTINCT customer_id) order_count
FROM Orders
GROUP BY month;