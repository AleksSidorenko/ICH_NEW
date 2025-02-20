-- create database 111124_Sidorenko; -- Создание таблицы
/* 
1. Создайте таблицу goods_имя с 4 полями (id, title, price, quantity).
2. Добавьте в таблицу goods 4 товара
3. Поменяйте цену велосипеда на 10000
4. Создать представление, которое выводит только те товары, которые стоят меньше 10000
*/
USE 111124_Sidorenko;
/* CREATE TABLE goods(  -- создали БД
				id int,
                title varchar(255),
                price decimal(10,2),
                quantity int);
*/
/*
SELECT *
FROM goods;
*/
-- SHOW TABLES; -- список всех таблиц которые у нас присутствуют
/*
INSERT INTO goods(id, title, price, quantity) values
(1, "bycikle", 6000, 50),
(2, "TVset", 20000, 40),
(3, "Laptop", 15000, 60),
(4, "Computer", 4000, 20);
*/
-- SELECT *
-- FROM goods;
-- SHOW TABLES; -- список всех таблиц которые у нас присутствуют

-- UPDATE goods set price = 10000
-- WHERE title = "bycikle"

-- CREATE VIEW goods_exp AS
-- SELECT *
-- FROM goods
-- WHERE price >= 10000;

-- SELECT *
-- FROM goods_exp
-- RENAME TABLE table_v TO view_of_goods;

-- DELETE FROM goods
-- SELECT *
-- FROM goods








			



                
                
                
                
                