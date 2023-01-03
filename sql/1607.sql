SELECT seller_id,sale_date
FROM Orders
WHERE YEAR(sale_date) = '2020';