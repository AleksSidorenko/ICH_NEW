USE 111124_Sidorenko;
-- 1. Вывести все заказы, отсортированные по убыванию по стоимости
/*
SELECT *
FROM orders 
ORDER BY order_price DESC
*/
-- 2. Вывести всех заказчиков, у которых почта зарегистриварована на gmail.com
/*
SELECT *
FROM customer
WHERE email LIKE '%gmail.com'
*/
-- 3. Вывести заказы, добавив дополнительный вычисляемый столбец status, 
-- который вычисляется по стоимости заказа и имеет три значения: low, middle, high. 
/*
SELECT *,
CASE
	WHEN order_price > 2000 THEN 'high'
		WHEN order_price < 1000 THEN 'low'
        ELSE 'middle'
        END AS status
FROM orders
*/
-- 4. Вывести заказчиков по дате регистрации.
/*
SELECT *
FROM customer
ORDER BY reg_date;
*/
-- 5. Вывести всех заказчиков из города на ваш выбор. 
/*
SELECT *
FROM customer
WHERE city IN ('London');
*/
-- 6. Написать запрос, который вернет самый часто продаваемый товар. 
/*
SELECT *,
COUNT(description_item) AS 'description_item_count'
FROM orders
GROUP BY (description_item);
*/
-- 7. Вывести список заказов с максимальной скидкой. 
/*
SELECT *,
	CASE 
		WHEN discounter_price < order_price THEN (discounter_price / order_price) * 100
        END AS 'd_price'
FROM orders
ORDER BY d_price DESC LIMIT 1;
*/

-- 8. Ответьте в 1 предложении: как вы определите скидку? 

-- 9. Ответьте в 1 предложении: может ли это быть разница между нормальной ценой и 
-- скидочной ценой? 

-- 10. Написать запрос, который выведет все заказы с дополнительным столбцом процент_скидки, 
-- который содержит разницу в процентах между нормальной и скидочной ценой?
