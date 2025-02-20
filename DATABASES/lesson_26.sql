# Напишите SQL-запрос для вывода покупок, совершенных во вторник, 
# и предоставьте информацию о каждом заказе, включая сумму, дату, 
# имя покупателя и имя продавца.
-- SELECT * FROM ORDERS;
-- SELECT * FROM CUSTOMERS;
-- SELECT * FROM SELLERS;
/*
SELECT ord.ORDER_ID, ord.AMT, ord.ODATE, cst.CNAME, sel.SNAME, DAYNAME(ord.ODATE)
FROM ORDERS AS ord
LEFT JOIN CUSTOMERS AS cst ON ord.CUST_ID = cst.CUST_ID
LEFT JOIN SELLERS AS sel ON ord.SELL_ID = sel.SELL_ID
WHERE WEEKDAY(ord.ODATE) = 1
*/
# Определить, сколько покупок было совершено в каждый месяц. 
# Отсортировать строки в порядке возрастания количества покупок. 
# Вывести два поля - номер месяца и количество покупок.
/*
SELECT MONTHNAME(ODATE) AS mon, COUNT(SELL_ID) AS cnt_sel
FROM ORDERS
GROUP BY mon
*/
# Вывести сегодняшнюю дату в формате: день недели, число, месяц, год
/*
SELECT DATE_FORMAT(CURDATE(), '%W %d %M %Y');
SELECT DATE_FORMAT(NOW(), '%W, %d-%m-%Y') AS `today`
SELECT DATE_FORMAT('2024-07-01', '%W, %e-%m-%Y') AS `today`
*/
# Вывести на какой день недели приходится 1 января 2024 года. 
# Вывести, на какой день недели приходится число, через 10 дней после.
/*
SELECT DAYNAME('2024-01-01');
SELECT DATE_FORMAT('2024-01-01', '%W');
SELECT DAY('2024-01-01') + 10 DAY;
SELECT DATENAME(DATE_ADD(NOW(), INTERVAL 10))
*/
# Вывести дату, которая будет через 10 дней после последнего дня текущего месяца. 
# Вывести день недели даты из предыдущей задачи.
/*
SELECT DAY(LAST_DAY(NOW())) + 10 DAY

SELECT DATE_ADD(LAST_DAY(NOW()), INTERVAL 10 DAY),
		DAYNAME(DATE_ADD(LAST_DAY(NOW()), INTERVAL 10 DAY));
*/
# Вывести название месяца, который будет через 5 месяцев после текущего.
/*
SELECT MONTH(NOW()) + 5 MONTH
SELECT monthname(LAST_DAY(NOW()) + interval 5 month) AS `month`
*/
# Вывести количество заказов по числам месяца.
/*
SELECT COUNT(ORDER_ID) AS amount, extract(DAY FROM ODATE) AS `day`, DAY(ODATE) AS additional
FROM ORDERS
GROUP BY `day`
*/
# Вывести количество заказов по дням недели.
/*
SELECT COUNT(ORDER_ID), DAYOFWEEK(ODATE), DAYNAME(ODATE)
FROM ORDERS
GROUP BY DAYOFWEEK(ODATE)
*/
# Вывести количество дней, которые работают сотрудники с момента найма.
-- USE hr;
/*
SELECT * FROM employees;
SELECT first_name, last_name, hire_date, DATEDIFF(NOW(), hire_date)
FROM employees
*/
# Вывести количество лет, которые проработал каждый сотрудник.
/*
SELECT first_name, last_name, hire_date, TIMESTAMPDIFF(YEAR, hire_date, CURDATE()) AS cnt_year
FROM employees
*/































ORDER BY cnt_sel