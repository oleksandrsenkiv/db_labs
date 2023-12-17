use mydb_lab4;

DROP PROCEDURE IF EXISTS add_brand;
DELIMITER //
CREATE PROCEDURE add_brand(IN brand_name varchar(45))
BEGIN
	INSERT INTO `mydb_lab4`.`brand`(`brand_name`) values(brand_name);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_into_snacks_has_brand;
DELIMITER //
CREATE PROCEDURE insert_into_snacks_has_brand(IN insert_brand_name VARCHAR(45), IN insert_snack_name VARCHAR(45))
BEGIN
    DECLARE snacks_id INT;
    DECLARE brand_id INT;

    SELECT id INTO snacks_id FROM `mydb_lab4`.`snacks`
    WHERE `snack_name` = insert_snack_name;

    SELECT id INTO brand_id FROM `mydb_lab4`.`brand`
    WHERE `brand_name` = insert_brand_name;

    IF snacks_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'This snack is not exist';
    END IF;

    IF brand_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'This brand is not exist';
    END IF;

    IF snacks_id IS NOT NULL AND brand_id IS NOT NULL THEN
        INSERT INTO `mydb_lab4`.`snacks_has_brand` VALUES (snacks_id, brand_id);
    END IF;

END//
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_noname_snacks;
DELIMITER //
CREATE PROCEDURE insert_noname_snacks()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i < 10 DO
        INSERT INTO `mydb_lab4`.`snacks`(snack_name) VALUES (CONCAT('NONAME', i));
        SET i = i + 1;
    END WHILE;
END//
DELIMITER ;

DROP FUNCTION IF EXISTS find_stats_of_product_loading_func;
DROP PROCEDURE IF EXISTS find_product_loading_stats;

DELIMITER //
	CREATE FUNCTION find_stats_of_product_loading_func(stats_type varchar(3))
		RETURNS INT
        DETERMINISTIC
        BEGIN
			DECLARE result INT;
			IF stats_type = 'Max' THEN
				SELECT MAX(product_loading_count) INTO result FROM product_loading;
            ELSEIF stats_type = 'Min' THEN
				SELECT MIN(product_loading_count) INTO result FROM product_loading;
            ELSEIF stats_type = 'Sum' THEN
				SELECT SUM(product_loading_count) INTO result FROM product_loading;
            ELSEIF stats_type = 'Avg' THEN
				SELECT AVG(product_loading_count) INTO result FROM product_loading;
			ELSE
				SET result = 1;
			END IF ;
            RETURN result;
		END//
	DELIMITER ;

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

DROP PROCEDURE IF EXISTS create_db_from_snacks;

DELIMITER //

CREATE PROCEDURE create_db_from_snacks()
BEGIN
    DECLARE done INT DEFAULT false;
    DECLARE db_name VARCHAR(255);
    DECLARE cur CURSOR FOR SELECT snack_name FROM snacks;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = true;

    OPEN cur;

    myLoop: LOOP
        FETCH cur INTO db_name;
        IF done THEN
            LEAVE myLoop;
        END IF;

        SET @create_db_query = CONCAT('CREATE DATABASE IF NOT EXISTS ', db_name);
        PREPARE query_ FROM @create_db_query;
        EXECUTE query_;
        DEALLOCATE PREPARE query_;

        SET @num_tables = ROUND(RAND() * 9) + 1;
        SET @counter = 1;

        WHILE @counter <= @num_tables DO
            SET @table_name = CONCAT(db_name, '_', @counter);
            SET @create_table_query = CONCAT('CREATE TABLE IF NOT EXISTS ', db_name, '.', @table_name, ' (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))');
            PREPARE query_ FROM @create_table_query;
            EXECUTE query_;
            DEALLOCATE PREPARE query_;
            SET @counter = @counter + 1;
        END WHILE;
    END LOOP;

    CLOSE cur;
END //