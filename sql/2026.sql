SELECT
    problem_id,
    likes / (likes + dislikes) quality
FROM Problems
WHERE likes / (likes + dislikes) < 0.6;