WITH RECURSIVE CTE AS(
    SELECT 1 AS Id,MAX(customer_id) AS end_id
    FROM Customers
    UNION ALL
    SELECT Id+1,end_id
    FROM CTE
    WHERE CTE.Id<end_id
)

SELECT Id AS ids FROM CTE
WHERE Id NOT IN (SELECT customer_id from Customers)