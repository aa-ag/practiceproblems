WITH cte as (
    SELECT customer_id,
    product_id,
    RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(product_id) DESC) as o_rank
    FROM Orders
    GROUP BY customer_id, product_id
)
