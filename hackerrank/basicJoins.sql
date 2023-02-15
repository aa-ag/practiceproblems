SELECT
    SUM(ci.POPULATION)
FROM CITY ci
JOIN COUNTRY co
ON ci.CountryCode=co.Code
WHERE co.CONTINENT='Asia';


SELECT
    ci.NAME
FROM CITY ci
JOIN COUNTRY co
ON ci.COUNTRYCODE=co.CODE
WHERE CONTINENT = 'Africa';

SELECT
    co.CONTINENT,
    FLOOR(AVG(ci.Population))
FROM COUNTRY co
JOIN CITY ci
ON ci.COUNTRYCODE=co.CODE
GROUP BY co.CONTINENT;

SELECT s.hacker_id,h.name
FROM Submissions s
JOIN Hackers h
ON s.hacker_id=h.hacker_id
JOIN Challenges c
ON c.challenge_id=s.challenge_id
JOIN Difficulty d
ON d.difficulty_level=c.difficulty_level
WHERE s.score=d.score
GROUP BY s.hacker_id, h.name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;