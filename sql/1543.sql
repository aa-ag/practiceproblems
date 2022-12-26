SELECT
    product_name,
    sale_date,
    COUNT(*) total
FROM (SELECT
    LOWER(TRIM(product_name)) product_name,
    DATE_FORMAT(sale_date,'%Y-%m') sale_date
FROM Sales) a
GROUP BY product_name,sale_date
ORDER BY product_name ASC,sale_date ASC;