SELECT
    problem_id,
    likes / (likes + dislikes) quality
FROM Problems;