USE 111124_Sidorenko;
-- Вывести список заказов с максимальной скидкой. 
/*
SELECT *, order_price - discounter_price AS 'discount'
FROM orders
WHERE order_price - discounter_price = (SELECT MAX(order_price - discounter_price) AS 'discount'
FROM orders);
-- SELECT MAX(order_price - discounter_price) AS 'discount'
-- FROM orders;
*/

-- Ответьте в 1 предложении: как вы определите скидку? 

-- Ответьте в 1 предложении: может ли это быть разница между нормальной ценой и скидочной ценой?

-- Написать запрос, который выведет все заказы с дополнительным столбцом процент_скидки, 
-- который содержит разницу в процентах между нормальной и скидочной ценой?
/*
SELECT *,
(order_price -  discounter_price)/order_price * 100 AS `%`
FROM orders
WHERE (order_price -  discounter_price)/order_price * 100 = (SELECT
MAX((order_price -  discounter_price)/order_price )* 100 AS `%`
FROM orders);
*/
-- Создать таблицу Students с полями:
-- id - целое число первичный ключ автоинкремент
-- name - строка 128 не null
-- age - целое число
/*
CREATE TABLE students
(id int primary key auto_increment,
name varchar(128) not null,
age int);
-- SELECT *
-- FROM students
*/
-- Создать таблицу Teachers с полями:
-- id - целое число первичный ключ автоинкремент
-- name - строка 128 не null
-- age - целое число
/*
CREATE TABLE teachers(
				id int PRIMARY KEY auto_increment,
                `name` varchar(128) NOT NULL,
                age int);
-- SELECT *
-- FROM teachers;
*/

-- Создать таблицу Competencies с полями:
-- id - целое число первичный ключ автоинкремент
-- title - строка 128 не null
/*
CREATE TABLE competencies(
	id int PRIMARY KEY auto_increment,
    title varchar(128) not null);
-- SELECT *
-- FROM competencies
*/
-- Создать таблицу Teachers2Competencies с полями:
-- teacher_id - целое число
-- competencies_id - целое число
/*
CREATE TABLE teachers2competencies(
teacher_id int,
competencies_id int,
PRIMARY KEY (teacher_id, competencies_id),
FOREIGN KEY (teacher_id) REFERENCES teachers(id),
FOREIGN KEY (competencies_id) REFERENCES competencies(id)
)
*/
-- Создать таблицу Courses
-- id - целое число первичный ключ автоинкремент
-- teacher_id - целое число
-- title строка - 128 не null
-- headman_id - целое число
/*
CREATE TABLE courses (
id int primary key auto_increment,
teacher_id int,
title varchar(128) NOT NULL,
headman_id int
);
*/

