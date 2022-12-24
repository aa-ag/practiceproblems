-- 1241. Number of Comments per Post
SELECT
    DISTINCT sub_id post_id,
    parent_id number_of_comments
FROM Submissions
WHERE parent_id IS NULL
ORDER BY post_id ASC;