SELECT COUNT(*)
FROM CITY
WHERE POPULATION > 100000;

SELECT SUM(POPULATION)
FROM CITY 
WHERE DISTRICT='California';

SELECT
    ROUND(AVG(POPULATION))
FROM CITY
WHERE DISTRICT = 'California';

SELECT
    ROUND(AVG(POPULATION))
FROM CITY;

SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;

SELECT
    CEIL(AVG(SALARY) - AVG(REPLACE((SALARY), '0', '')))
FROM EMPLOYEES;

SELECT
    (months * salary) earnings,
    COUNT(*) 
FROM Employee 
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;

SELECT
    ROUND(SUM(LAT_N),2),
    ROUND(SUM(LONG_W),2)
FROM STATION;

SELECT
    ROUND(SUM(LAT_N),4)
FROM STATION
WHERE LAT_N > 38.78880
AND LAT_N < 137.2345;

SELECT
    ROUND(MAX(LAT_N),4)
FROM STATION
WHERE LAT_N < 137.2345;

SELECT
    ROUND(LONG_W,4)
WHERE LAT_N < 137.2345;

SELECT
    ROUND(LONG_W,4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1;