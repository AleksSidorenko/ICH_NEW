-- SELECT NOW()
# Используя базу данных hr, написать запрос, который отображает сотрудников, нанятых в 2005 году.
# (2-мя запросами используя STR_TO_DATE и даты '01,1,2005' и '01,1,2006' и стандартное условие
-- USE hr;
/*
SELECT first_name, last_name, hire_date FROM employees
WHERE hire_date BETWEEN ('2005-01-01' AND '2005-12-31')

SELECT first_name, last_name, hire_date FROM employees
WHERE hire_date BETWEEN STR_TO_DATE("01,1,2005", "%d,%m,%Y") AND STR_TO_DATE("31,12,2005", "%d,%m,%Y")
*/

# Написать запрос, который отображает среднюю AMT (сумма заказа) в 2022 году (даты между '01.1.2022' и '01,1,2023')
/*
USE shop;
SELECT ROUND(AVG(AMT), 2)
FROM ORDERS
WHERE ODATE >= str_to_date('01.1.2022', "%d.%m.%Y") AND ODATE < str_to_date('01,1,2023', "%d,%m,%Y")
*/

-- SELECT CURDATE()
# Определите количество сотрудников, которых приняли на работу в пятницу
/*
SELECT COUNT(*) FROM employees
WHERE WEEKDAY(hire_date) = 4  # Пятница
-- WHERE DAYOFWEEK(hire_date) = 6   # Пятница
*/

# Испытательный срок после трудоустройства длится три месяца, 
# начиная с календарного месяца после трудоустройства, напишите скрипт, 
# который рассчитывает дату окончания испытательного срока для каждого сотрудника
/*
select first_name, last_name, hire_date, hire_date + interval 3 month as prob_end_date, date_add(hire_date, interval 3 month) as end_date_term
from employees
*/

# Определите месяц, в который чаще всего принимают на работу
/*
SELECT COUNT(*) AS emp_cnt, EXTRACT(MONTH FROM hire_date) -- FROM employees
FROM employees
GROUP BY EXTRACT(MONTH FROM hire_date)
ORDER BY emp_cnt DESC
*/

# Выведите количество заказов по месяцам (номер месяца - количество заказов в этом месяце)
/*
-- USE shop;
select count(*) "количество заказов", extract(month from ODATE) "месяцы" 
from ORDERS 
group by extract(month from ODATE) 
order by extract(month from ODATE);
*/

# Выведите список заказов в марте
/*
SELECT ORDER_ID, MONTHNAME(ODATE)
FROM ORDERS
WHERE MONTHNAME(ODATE) = 'March';
*/

# Выведите список заказов с годом (номер заказа, год)
/*
use shop;
select ORDER_ID, date_format(ODATE, "%Y")
from ORDERS
*/

# Выведите количество заказов по месяцам (название месяца, количество заказов)
/*
SELECT COUNT(ORDER_ID), MONTHNAME(ODATE)
FROM ORDERS
GROUP BY MONTHNAME(ODATE)

SELECT COUNT(ORDER_ID), MONTHNAME(ODATE) AS n_month
FROM ORDERS
GROUP BY n_month
*/
# Определить какие из покупок были совершены в интервале от 10 апреля 2022 до 10 мая 2022 года
# от '10-04/2022' до '10x05x2022

-- SELECT *
-- FROM ORDERS
-- WHERE ODATE >= STR_TO_DATE ('10-04/2022', '%d-%m/%Y') AND ODATE < STR_TO_DATE ('10x05x2022', '%dx%mx%Y')


# Напишите SQL-запрос для вывода покупок, совершенных в июне,  
# укажите количество покупок для каждого продавца. 
# Результат запроса должен содержать идентификатор продавца и количество покупок, сделанных им в июне.
/*
-- USE shop;
SELECT SELL_ID, COUNT(*) as sales_num -- , MONTH(ODATE)
FROM ORDERS
WHERE MONTH(ODATE) = 6
GROUP BY SELL_ID
*/
# Напишите SQL-запрос для вывода средней стоимости покупок, совершенных в марте, 
# и определите, какие продавцы имеют самую высокую и самую низкую среднюю стоимость покупок в этом месяце. 
# Обязательно выведите имя продавца.
/*
SELECT ord.SELL_ID, sel.SNAME, ROUND(AVG(ord.AMT),2) AS avg_amt 
FROM ORDERS ord
LEFT JOIN SELLERS sel ON ord.SELL_ID = sel.SELL_ID
WHERE MONTH (ord.ODATE) = 3
GROUP BY ord.SELL_ID
ORDER BY avg_amt DESC;

SELECT *
FROM 
(
SELECT ord.SELL_ID, sel.SNAME, ROUND(AVG(ord.AMT)) AS avg_amt 
FROM ORDERS ord
LEFT JOIN SELLERS sel ON ord.SELL_ID = sel.SELL_ID
WHERE MONTH (ord.ODATE) = 3
GROUP BY ord.SELL_ID
) t3
WHERE avg_amt IN (
(SELECT MAX(avg_amt) FROM 
(SELECT ROUND(AVG(AMT)) AS avg_amt 
FROM ORDERS 
WHERE MONTH (ODATE) = 3
GROUP BY SELL_ID
) t1
), 
(
SELECT MIN(avg_amt) FROM 
(SELECT ROUND(AVG(AMT)) AS avg_amt 
FROM ORDERS 
WHERE MONTH (ODATE) = 3
GROUP BY SELL_ID
) t2
))
ORDER BY avg_amt DESC
*/

# Напишите SQL-запрос для вывода средней стоимости покупок, совершенных в марте, и 
# определите, какие продавцы имеют самую высокую и самую низкую среднюю стоимость покупок в этом месяце. 
# Обязательно выведите имя продавца.
# Итоговый вывод: вернуть только максимальные и минимальные средние значения продаж, имя и идентификатор продавца.
# Решить задачу с использованием WITH
























