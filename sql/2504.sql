SELECT
    person_id,
    CONCAT(name, '(', profession, ')')
FROM Person
ORDER BY person_id DESC;