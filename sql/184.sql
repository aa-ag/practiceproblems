SELECT d.name, e.name, e.salary
FROM Department d
JOIN Employee e
ON d.id=e.departmentId
WHERE (d.id,e.salary) IN (
    SELECT departmentId, MAX(salary) m
    FROM Employee
    GROUP BY departmentId
);