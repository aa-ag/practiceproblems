SELECT seller_id
FROM Seller
WHERE seller_id NOT IN (
    SELECT seller_id
    FROM Orders
    WHERE YEAR(sale_date) = '2020');