# Вывести текущую дату и время.
/*
SELECT CURDATE(), CURTIME();
SELECT DATE_FORMAT(NOW(), '%W %M %Y %k:%i:%s');
SELECT NOW();
SELECT CURRENT_TIMESTAMP();
*/
# Вывести текущий год и месяц
/*
SELECT YEAR(CURDATE()), MONTHNAME(CURDATE());
SELECT YEAR(CURDATE()), MONTH(CURDATE());
SELECT DATE_FORMAT(CURDATE(), '%Y %M');
SELECT EXTRACT(YEAR FROM CURDATE()), MONTHNAME(CURDATE());
*/
# Вывести текущее время
/*
SELECT CURTIME();
SELECT CURRENT_TIME();
*/
# Вывести название текущего дня недели
/*
SELECT DATE_FORMAT(CURDATE(), '%a');
SELECT DATE_FORMAT(CURDATE(), '%W');
SELECT DAYOFWEEK(CURDATE()) + 10 DAY;
*/
# Вывести номер текущего месяца
/*
SELECT MONTH(CURDATE());
SELECT DATE_FORMAT(CURDATE(), '%m');
SELECT EXTRACT(MONTH FROM CURDATE());
*/
# Вывести номер дня в дате “2020-03-18”
/*
SELECT DAY('2020-03-18');
SELECT DAYOFMONTH('2020-03-18');
SELECT EXTRACT(DAY FROM '2020-03-18');
*/
# Подключиться к базе данных shop (которая находится на удаленном сервере).
-- USE shop;
# Определить какие из покупок были совершены апреле (4-й месяц)
/*
SELECT ORDER_ID, ODATE FROM ORDERS
WHERE MONTH(ODATE) = 4
*/
# Определить количество покупок в 2022-м году
/*
SELECT COUNT(ORDER_ID) AS cnt_2022
FROM ORDERS
WHERE extract(YEAR from ODATE) = '2022' 

-- WHERE ODATE BETWEEN '2022-01-01' AND '2022-12-31'
-- WHERE ODATE > '2021-12-31' AND ODATE < '2023-01-01'
-- WHERE ODATE >= STR_TO_DATE('2022-01-01', '%Y-%m-%d') AND ODATE <= STR_TO_DATE('2022-12-31', '%Y-%m-%d')
*/
# Определить, сколько покупок было совершено в каждый день. 
# Отсортировать строки в порядке возрастания количества покупок. 
# Вывести два поля - дату и количество покупок
/*
SELECT ODATE, COUNT(ODATE) AS cnt_sell
FROM ORDERS
GROUP BY ODATE
ORDER BY cnt_sell, ODATE
*/
# Определить среднюю стоимость покупок в апреле
/*
SELECT ROUND(AVG(AMT), 2) AS avg_amt, MONTHNAME(ODATE) AS name_month
FROM ORDERS
WHERE MONTH(ODATE) = 4
*/