SELECT
    DATE_FORMAT(order_date, '%Y-%m') month,
    COUNT(DISTINCT customer_id) order_count
FROM Orders
WHERE invoice > 20
GROUP BY month;