SELECT
    person_id,
    CONCAT(name, '(', SUBSTRING(profession, 1, 1), ')')
FROM Person
ORDER BY person_id DESC;