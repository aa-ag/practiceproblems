SELECT
    d.name Department,
    e.name Employee,
    e.salary Salary
FROM Department d
JOIN Employee e
ON d.id=e.departmentId
WHERE (d.id,e.salary) IN (
    SELECT departmentId, MAX(salary) m
    FROM Employee
    GROUP BY departmentId
);