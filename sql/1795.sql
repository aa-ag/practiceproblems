SELECT
    product_id,'store_1' AS store,store1 AS price FROM Products WHERE store1
IS NOT NULL
UNION
SELECT
    product_id,'store_2' AS store,store2 AS price FROM Products WHERE store2
IS NOT NULL
UNION
SELECT
    product_id,'store_3' AS store,store3 AS price FROM Products WHERE store3
IS NOT NULL
GROUP BY 1,2;