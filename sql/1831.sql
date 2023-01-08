SELECT
    transaction_id,
    DATE(day),
    amount
FROM Transactions
ORDER BY transaction_id ASC;