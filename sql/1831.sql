SELECT
    DATE(day) transaction_date,
    MAX(amount)
FROM Transactions
GROUP BY transaction_date