SELECT 
    c.company_code, 
    c.founder, 
    COUNT(DISTINCT e.lead_manager_code),
    COUNT(DISTINCT e.senior_manager_code),
    COUNT(DISTINCT e.manager_code),
    COUNT(DISTINCT e.employee_code)
FROM Company c
JOIN Employee e
ON c.company_code=e.company_code
GROUP BY c.company_code,c.founder
ORDER BY c.company_code;

/* Write a query to output the names 
of students whose best friends got offered a higher salary than them.*/
SELECT s.name, f.ID, p.Salary
FROM Students s
JOIN Friends f 
ON s.ID==f.Friend_ID
JOIN Packages p
JOIN f.ID==p.ID;