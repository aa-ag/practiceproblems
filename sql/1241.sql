SELECT
    DISTINCT a.sub_id post_id,
    (SELECT 
        COUNT(DISTINCT b.sub_id)
        FROM Submissions b 
        WHERE a.sub_id=b.parent_id
    ) number_of_comments
FROM Submissions a
WHERE a.parent_id IS NULL;