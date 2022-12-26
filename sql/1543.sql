SELECT
    LOWER(TRIM(product_name)) product_name,
    DATE_FORMAT(sale_date,'%Y-%m') sale_date
FROM Sales;