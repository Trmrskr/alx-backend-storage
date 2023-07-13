--Email validation to sent
DELIMITER $$
CREATE TRIGGER `reset_valid_emaili_AUPD`
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email
THEN
    SET NEW.valid_email = 0;
END IF;
END
$$
DELIMITER ;
