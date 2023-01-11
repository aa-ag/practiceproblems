SELECT customer_id FROM Visits
WHERE visit_id NOT IN 
(SELECT
    distinct visit_id 
FROM Transactions);