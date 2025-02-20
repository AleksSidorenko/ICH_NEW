# Напишите SQL-запрос для вывода средней стоимости покупок, совершенных в марте, 
# и определите, какие продавцы имеют самую высокую и самую низкую среднюю стоимость покупок в этом месяце. 
# Обязательно выведите имя продавца.
# Итоговый вывод: вернуть только максимальные и минимальные средние значения продаж, имя и идентификатор продавца.
# Решить задачу с использованием WITH
/*
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
*/

/*
WITH avg_sales as (SELECT ord.SELL_ID, sel.SNAME, ROUND(AVG(ord.AMT)) AS avg_amt 
FROM ORDERS ord
LEFT JOIN SELLERS sel ON ord.SELL_ID = sel.SELL_ID
WHERE MONTH (ord.ODATE) = 3
GROUP BY ord.SELL_ID)

SELECT * FROM 
avg_sales
WHERE avg_amt in ((SELECT max(avg_amt) from avg_sales), (SELECT min(avg_amt) from avg_sales))
order by avg_amt DESC;
*/

# Вывести департаменты и количество сотрудников, работающих в них и нанятых в декабре
/*
-- USE hr;
SELECT dep.department_name, COUNT(emp.employee_id)
FROM employees AS emp
LEFT JOIN departments AS dep ON dep.department_id = emp.department_id
WHERE MONTH(hire_date) = 12
GROUP BY emp.department_id
*/

# В каких городах работают сотрудники, нанятые в марте.
-- SELECT * FROM employees;
-- SELECT * FROM locations;
-- SELECT * FROM departments;
/*
SELECT DISTINCT(loc.city) -- или с GROUP BY вместо DISTINCT
FROM locations AS loc
LEFT JOIN departments AS dep ON dep.location_id = loc.location_id
LEFT JOIN employees AS emp ON emp.department_id = dep.department_id
WHERE MONTH(emp.hire_date) = 3
*/
# '2003-07-03'
-- SELECT FLOOR(DATEDIFF(CURDATE(), '2003-07-03') / 365);
/*
SELECT 
CASE 
	WHEN MONTH(CURDATE()) < MONTH('2003-07-03') THEN YEAR(NOW())-1 - YEAR('2003-07-03')
    WHEN MONTH(CURDATE()) > MONTH('2003-07-03') THEN YEAR(NOW()) - YEAR('2003-07-03')
    WHEN MONTH(CURDATE()) = MONTH('2003-07-03') AND DAY(CURDATE()) < DAY('2003-07-03') THEN YEAR(NOW())-1 - YEAR('2003-07-03')
    ELSE YEAR(NOW()) - YEAR('2003-07-03')
END AS x;
*/
/*
select 
    year(curdate()) - year('2003-07-03') - 
    (date_format(curdate(), '%m%d') < date_format('2003-07-03', '%m%d')) as age;
*/
























