USE 111124_Sidorenko;

/* 
Создать таблицу goods с полями
id (первичный ключ)
title (cтрока максимум в 30 символов)
quantity (число больше 0)
in_stock (символ (Y/N) 
*/
-- DROP Table goods - удаление таблицы если нужно

-- проверка таблицы, если не существует, то создать, иначе появится ошибка:
-- CREATE TABLE IF NOT EXISTS goods_1(				
-- 					id INT PRIMARY KEY auto_increment, 
-- 					title varchar(30), 
-- 					quantity int CHECK(quantity > 0),
--                  in_stock char(1) CHECK(in_stock in ('Y','N'))
--                     )

-- при повторном создании таблицы - выдаст ошибку, т.к. уже существует
-- CREATE TABLE goods_1(								
-- 						id INT PRIMARY KEY auto_increment, 
-- 						title varchar(30), 
-- 						quantity int CHECK(quantity > 0),
--                  	in_stock char(1) CHECK(in_stock in ('Y','N'))
--                     )

/*
После создания таблицы, попробуйте добавить в нее несколько строчек с данными (минимум 10 строк), 
нарушив указанные вами при создании таблицы ограничения, например, одинаковые id или отрицательное количество, 
а также in_stock со значением ‘yes’. 
Убедитесь, что база данных выдала ошибку при попытке добавить такие строки, прочитайте сообщения об ошибке, 
исправьте ее и повторите попытку.
*/

-- INSERT INTO goods_1(id, title, quantity, in_stock) VALUES
-- (1,'Laptop',29,'Yes'),
-- (2,'Computer','Computer','N'),
-- (3,1234,89,'Y'),         
-- (4,'Mothetop',29,'Yes')

-- ALTER TABLE goods_1
-- MODIFY COLUMN quantity int CHECK(quantity > 0) NOT NULL

-- TRUNCATE TABLE goods_1; -- DELETE FROM goods_1 WHERE 

-- INSERT INTO goods_1 (title, quantity, in_stock) VALUES 
-- ('Laptop', 29,'Y'),
-- ('Computer', 30,'N'),
-- ('Mouse', 89,'Y'),
-- ('Motherboard', 45, 'Y'),
-- ('Fridge', 13, 'N'),
-- ('bike', 5, 'Y'),
-- ('USB flash', 18, 'N'),
-- ('Scooter',  15, 'Y'),
-- ('TV', 25, 'Y'),
-- ('Sweet Roll', 99, 'Y');

/* пример по добавления уникальности и т.д.
alter table new_students
add unique (email);
describe new_students;

show create table new_students;
INSERT INTO new_students(employee_id,first_name,last_name,email) VALUES
(268, 'Alex','KAdetov', 'ABULL');

alter table new_students
drop constraint email;

DELETE FROM new_students WHERE employee_id = 268
*/

/*
Создать таблицу goods_2 с полями:
id (уникальное значение)
title (cтрока максимум 30 символов)
quantity (число больше 0)
price (целое число)
in_stock (символ (Y/N))
*/
-- CREATE TABLE goods_2(
-- 					id int PRIMARY KEY auto_increment,
--                     title varchar(30),
--                     quantity int CHECK(quantity > 0) NOT NULL,
--                     price int,
--                     in_stock char(1) CHECK(in_stock in ('Y', 'N'))
--                     )

/*
Заполните созданную таблицу goods_2 данными, минимум 10 строк.
*/
-- INSERT INTO goods_2 (title, quantity, in_stock, price) VALUES
-- 			('Laptop', 29,'Y', 123),
-- 			('Computer', 30,'N', 548),
-- 			('Mouse', 89,'Y', 56),
-- 			('Motherboard', 45, 'Y', 45558),
-- 			('Fridge', 13, 'N', 456),
-- 			('bike', 5, 'Y', 12),
-- 			('USB flash', 18, 'N', 267),
-- 			('Scooter',  15, 'Y', 64),
-- 			('TV', 25, 'Y', 649),
-- 			('Sweet Roll', 99, 'Y', 235),
--             ('Велосипед', 2, 'Y',12369),
-- 			('Скейт', 4, 'Y', 187),
--             ('Самокат', 2, 'Y', 298),
--             ('Сноуборд', 7, 'N', 357),
--             ('Санки', 1, 'Y', 159),
--             ('Коньки', 3, 'N', 456),
-- 			('Ролики', 5, 'Y', 8502)
-- ;
-- SELECT * FROM goods_2;

-- Вывести все наименования товаров (включая дубли) из двух таблиц
-- SELECT title
-- FROM goods_2
-- UNION ALL SELECT title
-- FROM  goods_1
-- ORDER BY title

-- Объединить данные из двух таблиц, указав price, где это возможно.
-- SELECT id, title, quantity, in_stock, 0 AS price
-- FROM goods_1
-- UNION ALL 
-- SELECT id, title, quantity, in_stock, price
-- FROM goods_2;

-- SELECT id, title, quantity, in_stock, 0 AS price
-- FROM goods_1
-- UNION
-- SELECT id, title, quantity, in_stock, price
-- FROM goods_2;





















