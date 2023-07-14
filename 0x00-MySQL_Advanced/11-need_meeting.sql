-- No table for a meeting
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE
    score < 80 AND
    (last_meeting = NULL OR
    (DATEDIFF(MONTH, last_meeting, CURDATE()) >= 1));
