SELECT
    event_day,
    emp_id,
    SUM(out_time - in_time) daily_balance
FROM Employees
GROUP BY emp_id,event_day;