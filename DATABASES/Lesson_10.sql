	/*
    Идентификатор заказчика, имя, фамилию, улицу, почтовый код, город, страна, email, дата регистрации.
    */
    
    USE 111124_Sidorenko;
-- CREATE TABLE customer
--     (id_cust int primary key auto_increment,
--     first_name varchar(100),
--     last_name varchar(100),
--     street varchar(100),
--     zip_code int,
--     city varchar(150),
--     country varchar(150),
--     email varchar(150),
--     reg_date date);
--     
    
    /*
    Идентификатор заказа, Идентификатор заказчика, который создал этот заказ, дата создания заказа, 
    наименование товара (номер айтема), описание товара, ссылка на фотографию, стоимость заказа.
    */
    -- CREATE TABLE orders(
-- 		id int primary key auto_increment,
-- 		customer_id int,
--         order_date date,
--         item_id int,
--         description_item varchar(300),
--         photo_link varchar(400),
--         order_price decimal(10,2),
--         FOREIGN KEY(customer_id) REFERENCES customer(id_cust));
 --   SELECT * 
 --   FROM orders

-- INSERT INTO customer(first_name, last_name, street, zip_code, city, country, email, reg_date) 
-- values
-- ('Alex', 'Bond', 'MainStr', 50626, 'London', 'England', 'alex_hero@an.an', '2024-12-11'),
-- ('Alexei', 'Bondovici', 'MainStr', 50625, 'London', 'England', 'alexei_hero@an.an', '2024-12-11'),
-- ('John', 'Doe', '123 Main St', 12345, 'Springfield', 'USA', 'john.doe@example.com', '2023-04-01'),
-- ('Marina', 'Rai', 'Luci', 26030, 'Kostroma', 'Russia', 'marina.doe@gmail.com', '2024-04-01'),
-- ('Marie', 'Muller', '20 Bemerode St', 30171, 'Hannover', 'German','marie_muller@email.com', '2024-05-18');
 
-- SELECT *
--  FROM customer
/*
INSERT INTO orders(customer_id, order_date, item_id, description_item, photo_link, order_price) 
values
(1, '2024-11-12', 1, 'product_1', 'photo.jpg', 1000.00),
(2, '2024-11-12', 23, 'product_456', 'photo_1.jpg', 2000.00),
(3, '2024-10-12', 5, 'product_290', 'photo_290.jpg', 1500.00),
(4, '2023-11-06', 789, 'product_569', 'photo_372.jpg', 10500.00),
(5, '2022-07-08', 2665, 'product_1245', 'photo_56948.jpg', 8200.00),
(3, '2021-06-10', 2915, 'product_16', 'jfk.com', 850),
(5, '2024-12-01', 1232, 'product_10', 'njfeoj.net', 1200),
(1, '2023-05-19', 1010, 'product_05', 'widwcwek.com', 10),
(3, '2024-01-24', 14, 'product_1', 'jefn.com', 130)
SELECT *
FROM orders 
*/
-- К таблице Customer добавить поле last_modified, которое содержит дату последнего изменения данных заказчика.
/*
ALTER TABLE customer
ADD COLUMN last_modified timestamp default now() on update now()
SELECT *
FROM customer
UPDATE customer
SET city = 'Manchester' 
WHERE first_name = 'Alexei'
*/
-- Добавить к таблице Order поле discounter_price, которое содержит скидочную стоимость заказа. 
-- Обновить значение этого поля для всех заказов на 10% меньше, чем оригинальная стоимость заказа.
/*
ALTER TABLE orders
ADD COLUMN discounter_price numeric(10,2);
UPDATE orders
SET discounter_price = order_price * 0.9;
*/
/*
UPDATE orders
SET discounter_price = order_price * 0.85
WHERE customer_id = 3;
SELECT *
FROM orders
*/
-- Вывести все заказы, отсортированные по убыванию по стоимости

-- SELECT *
-- FROM orders
-- ORDER BY order_price DESC

-- Вывести всех заказчиков, у которых почта зарегистриварована на gmail.com
/*
SELECT *
FROM customer
WHERE email LIKE '%gmail.com'
*/
-- Вывести заказы, добавив дополнительный вычисляемый столбец status, 
-- который вычисляется по стоимости заказа и имеет три значения: low, middle, high.
-- high - больше 2000, middle - от 1000 до 2000 (включительно)
/*
SELECT *,
CASE
	WHEN order_price > 2000 THEN 'high'
		WHEN order_price < 1000 THEN 'low'
        ELSE 'middle'
        END AS status
FROM orders
*/
-- Вывести заказчиков по убыванию рейтинга.(дате регистрации)
/*
SELECT *
FROM customer
ORDER BY reg_date DESC
*/
-- Вывести всех заказчиков из двух городов на ваш выбор.
/*
SELECT *
FROM customer
WHERE city in ('London', 'Manchester')
*/
-- Написать запрос, который вернет id заказчика, сделавшего больше всех заказов.

-- SELECT customer_id, order_date,
-- COUNT(customer_id) AS 'order_count'
-- FROM orders
-- GROUP BY customer_id
-- ORDER BY order_count DESC
-- LIMIT 1;








