-- 1241. Number of Comments per Post
SELECT
    sub_id post_id,
    parent_id number_of_comments
FROM Submissions
WHERE parent_id IS NULL;