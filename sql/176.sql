SELECT salary SecondHighestSalary 
FROM (SELECT 
RANK() OVER(ORDER BY salary) place,
salary
FROM Employee) a
WHERE place = 2;