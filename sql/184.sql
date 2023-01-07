SELECT departmentId, MAX(salary) m
FROM Employee
GROUP BY departmentId;