SELECT
    a.company_code company_code,
    a.founder,
    COUNT(a.lead_manager_code),
    COUNT(a.senior_manager_code),
    COUNT(a.employee_code),
FROM (SELECT
        DISTINCT c.company_code,c.founder,l.lead_manager_code,s.senior_manager_code,e.employee_code
    FROM Company c
    JOIN Lead_Manager l
    ON c.company_code=l.company_code
    JOIN Senior_Manager s
    ON c.company_code=s.company_code
    JOIN Employee e
    ON c.company_code=e.company_code
    ORDER BY c.company_code ASC) a
GROUP BY company_code;