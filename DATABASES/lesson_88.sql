-- USE 111124_Sidorenko;
-- DROP TABLE goods;
/*
CREATE TABLE goods(
		id int PRIMARY KEY,
		title varchar(255),
		quantity integer CHECK(quantity between 0 and 10));
SHOW CREATE TABLE goods -- показать скрипт создания таблицы
'CREATE TABLE `goods` (
  `id` int NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `goods_chk_1` CHECK ((`quantity` between 0 and 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
*/
/*
INSERT INTO goods (id, title, quantity) values
(1, 'TV', 8),
(2, 'Table', 5), 
(3, 'Lamp', 2),
(4,'bycicle', 5),  
(5,'ski', 2), 
(6,'boat', 1);

*/


/* ALTER TABLE goods
ADD COLUMN price int DEFAULT 0;

*/
/*
ALTER TABLE goods
MODIFY COLUMN price numeric(8, 2); # numeric полностью эквивалентно decimal

*/

-- DESCRIBE goods
/*
UPDATE goods
SET price = NULL;
*/
/*
ALTER TABLE goods
RENAME COLUMN price TO item_price;
*/
/*
ALTER TABLE goods
DROP COLUMN item_price;
*/
-- SELECT *
-- FROM goods;
/*
CREATE TABLE schedule(
		id int PRIMARY KEY auto_increment,
		title_lesson varchar(100),
        teacher_name varchar(100),
        date_lesson date,
		number_lesson int CHECK(number_lesson between 1 and 3));

SELECT *
FROM schedule;
*/




