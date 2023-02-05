SELECT product_id,store,price
FROM Products
UNPIVOT
(
	price
	FOR store in (store1,store2,store3)
) AS T

-- SELECT
--     product_id,'store1' AS store,store1 AS price FROM Products WHERE store1
-- IS NOT NULL
-- UNION
-- SELECT
--     product_id,'store2' AS store,store2 AS price FROM Products WHERE store2
-- IS NOT NULL
-- UNION
-- SELECT
--     product_id,'store3' AS store,store3 AS price FROM Products WHERE store3
-- IS NOT NULL
-- GROUP BY 1,2;