-- Calculate average score
DROP PROCEDURE IF NOT EXISTS;
DELIMIT $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT AVG(score) FROM corrections WHERE user_id = corrections.user_id);
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END
$$
DELIMIT ;
