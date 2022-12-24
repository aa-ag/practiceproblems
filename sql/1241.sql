-- 1241. Number of Comments per Post
SELECT a.sub_id post_id,
(SELECT COUNT(DISTINCT(b.sub_id)) FROM Submissions b WHERE b.parent_id=a.sub_id) number_of_comments
FROM Submissions a
WHERE a.parent_id IS NULL
GROUP BY a.sub_id
ORDER BY post_id ASC;