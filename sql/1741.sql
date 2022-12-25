SELECT
    emp_id,
    event_day,
    out_time - in_time daily_balance
FROM Employees;