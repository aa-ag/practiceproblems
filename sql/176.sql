SELECT 
RANK() OVER(ORDER BY salary) place,
salary # SecondHighestSalary
FROM Employee
ORDER BY salary DESC;