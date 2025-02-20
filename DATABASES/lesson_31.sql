-- USE shop;

# Вывести средний рейтинг клиентов по городам: для каждого города вывести средний рейтинг клиентов.

-- SELECT * FROM CUSTOMERS;
/*
SELECT *, ROUND(AVG(RATING) OVER(PARTITION BY CITY)) AS avg_rate 
FROM CUSTOMERS;
ODER:
SELECT CITY, ROUND(AVG(RATING)) AS avg_rate 
FROM CUSTOMERS
GROUP BY CITY;

SELECT * 
FROM CUSTOMERS AS cus
LEFT JOIN (SELECT CITY, ROUND(AVG(RATING)) AS avg_rate 
FROM CUSTOMERS
GROUP BY CITY) AS avg_r ON cus.CITY = avg_r.CITY
*/

# Вывести информацию о каждом заказе и максимальную сумму заказа в том же месяце для каждой строки.
-- SELECT * FROM ORDERS;
/*
SELECT *, MAX(AMT) OVER(PARTITION BY MONTH(ODATE))
FROM ORDERS
*/

# Для более полного понимания практической значимости прошлого запроса, 
# добавим подсчет относительного вклада каждого заказа в max объем продажи месяца.
/*
SELECT *, MAX(AMT) OVER(PARTITION BY MONTH(ODATE)),
		  ROUND((AMT / MAX(AMT) OVER(PARTITION BY MONTH(ODATE)))* 100, 2) AS "%"
FROM ORDERS
*/

# Вывести список продавцов с указанием общей суммы их продаж. 
# Отсортировать продавцов по убыванию суммы продаж.
-- SELECT * FROM SELLERS;
/*
select s.SELL_ID, s.SNAME, o.AMT,
if (sum(o.AMT) over(partition by s.SELL_ID) is null, 0, sum(o.AMT) over(partition by s.SELL_ID)) sellers_sum
from SELLERS s left join ORDERS o on s.SELL_ID = o.SELL_ID
order by sellers_sum desc;


select s.SELL_ID, s.SNAME, o.AMT,
coalesce(sum(o.AMT) over(partition by s.SELL_ID), 0) sellers_sum # делает из null другое значение
from SELLERS s left join ORDERS o on s.SELL_ID = o.SELL_ID
order by sellers_sum desc;

select s.SELL_ID, s.SNAME, o.AMT,
ifnull(sum(o.AMT) over(partition by s.SELL_ID), 0) sellers_sum
from SELLERS s left join ORDERS o on s.SELL_ID = o.SELL_ID
order by sellers_sum desc;
*/

# Вывести топ-2 продавцов с самой высокой средней суммой заказа.
/*
SELECT t1.SNAME, AVG(t2.AMT)
FROM SELLERS t1
LEFT JOIN  ORDERS t2 ON t2.SELL_ID = t1.SELL_ID
GROUP BY t1.SELL_ID
ORDER BY AVG(t2.AMT) DESC
LIMIT 2;

SELECT t1.SNAME, AVG(t2.AMT) OVER (PARTITION BY t1.SELL_ID) as average_order, AMT
FROM SELLERS t1
LEFT JOIN  ORDERS t2 ON t2.SELL_ID = t1.SELL_ID
ORDER BY average_order DESC
*/

# произведите ранжирование департаментов по средней зарплате.
-- USE hr;

-- SELECT * FROM employees;
-- SELECT * FROM departments;
/*
SELECT department_id, ROUND(AVG(salary)) AS avg_sal, DENSE_RANK() OVER(ORDER BY AVG(salary) DESC) AS rang_sel
FROM employees
GROUP BY department_id
ORDER BY department_id
*/

# Выведите топ 3 департамента по уровню средней зарплаты:
/*
SELECT *
FROM (SELECT department_id, ROUND(AVG(salary)) avg_sel, DENSE_RANK()OVER(ORDER BY AVG(salary) DESC) as rank_sel
FROM employees
GROUP BY department_id) t1
WHERE rank_sel <= 3;
*/
# Вывести всех покупателей, которые имеют 2 место в рейтинге по значению рейтинга.
-- USE shop;
/*
SELECT * FROM 
(SELECT CNAME, RATING, DENSE_RANK() OVER(ORDER BY RATING DESC) AS rang
FROM CUSTOMERS) AS t
WHERE rang = 2
*/

# Выведите второго по зарплате сотрудника в каждом департаменте.
-- USE hr;

SELECT department_id,  first_name, last_name, salary, 
        DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS sal_rang,
        RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS sal_rang
FROM employees;

SELECT *
FROM 
(SELECT department_id,  first_name, last_name, salary, 
        DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS sal_rang
FROM employees) AS t
WHERE sal_rang = 2;

SELECT t1.*, department_name
FROM    (SELECT department_id, first_name, last_name, salary, 
        DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS sal_rang
        FROM hr.employees) AS t1
    LEFT JOIN hr.departments AS dep ON dep.department_id = t1.department_id
WHERE sal_rang = 2;









































