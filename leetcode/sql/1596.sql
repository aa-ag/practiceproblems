WITH cte as (
    SELECT customer_id,
    product_id,
    RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(product_id) DESC) as o_rank
    FROM Orders
    GROUP BY customer_id, product_id
)
SELECT cte.customer_id, p.product_id, p.product_name
FROM cte, Products as p
WHERE cte.product_id=p.product_id AND cte.o_rank=1;