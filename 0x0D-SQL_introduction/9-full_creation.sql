-- Create a table second_table in the database and add multiple rows
-- second_table description: id INT, name VARCHAR(256), score INT
-- The database name will be passed as an argument to the mysql command
CREATE TABLE IF NOT EXISTS `second_table` (id INT, name VARCHAR(256), score INT);
INSERT INTO `second_table` (`id`, `name`, `score`) 
VALUES 
    (1, "John", 10), 
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
