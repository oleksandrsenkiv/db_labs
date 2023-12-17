
DELIMITER //
	CREATE PROCEDURE find_product_loading_stats(IN stats_type VARCHAR(3))
    BEGIN
		DECLARE result INT;
        SET result = find_stats_of_product_loading_func(stats_type);
        IF result IS NOT NULL THEN
			SELECT(CONCAT(stats_type, 'of product loading count: ', result)) AS Result;
		ELSE
			SELECT 'Choose correct statistic type' as Result;
		END IF;
    END//
DELIMITER ;

DROP TRIGGER IF EXISTS before_update_trigger;
DELIMITER //
CREATE TRIGGER before_update_trigger
BEFORE UPDATE ON vm_menu
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You can`t change values in this table';
END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS before_delete_trigger;
DELIMITER //
CREATE TRIGGER before_delete_trigger
BEFORE DELETE ON vending_machine
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You can`t delete values in this table';
END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS before_insert_trigger;
DELIMITER //
CREATE TRIGGER before_insert_trigger
BEFORE INSERT ON technician
FOR EACH ROW
BEGIN
    IF NEW.technician NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid value for the technician';
    END IF;
END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS before_insert_vending_machine;

DELIMITER //

CREATE TRIGGER before_insert_vending_machine
BEFORE INSERT ON `mydb_lab4`.`vending_machine`
FOR EACH ROW
BEGIN
    DECLARE gps_count INT;
    SELECT COUNT(*) INTO gps_count FROM `mydb_lab4`.`gps` WHERE `id` = NEW.`gps_id`;

    IF gps_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'GPS NOT FOUND';
    END IF;
END//

DELIMITER ;