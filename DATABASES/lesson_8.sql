/* Найти департаменты в которых есть работники, зарабатывающие больше 10 000. В результате 
выборки формируются два поля (department_id и поле со значениями 1 или 0). 
После, выведите количество таких департаментов.
*/
/* USE hr;
SELECT department_id,
CASE
	WHEN salary > 10000 THEN 1
    ELSE 0
END
AS Salary_case
FROM employees

USE hr;
SELECT
SUM(
CASE
	WHEN salary > 10000 THEN 1
    ELSE 0
END
)
AS SUM_Salary_case
FROM employees

USE hr;
SELECT DISTINCT department_id,
CASE
	WHEN salary > 10000 THEN 1
    ELSE 0
END
AS Salary_case
FROM employees
WHERE
(CASE
	WHEN salary > 10000 THEN 1
    ELSE 0
END) = 1
*/

/* SELECT 
COUNT(
 DISTINCT department_id)
/*SUM(
CASE
	WHEN salary > 10000 THEN 1
    ELSE 0
END)
AS SUM_Salary_case */
/* FROM employees
WHERE 
(CASE
	WHEN salary > 10000 THEN 1
    ELSE 0
END) = 1
*/

/* Разделите самолеты на ближне-, средне- и дальнемагистральные. 
Ближнемагистральными будем считать самолеты, дальность полета которых > 1000 км и <= 2500 км. 
Среднемагистральными — с дальностью полета > 2500 км и <= 6000 км. 
Дальнемагистральными — с дальностью полета > 6000 км. 
В выборке должно быть два столбца, где в первом указана модель самолета. 
Во втором, category, — категория, со значениями short-haul, medium-haul, 
long-haul (ближне-, средне- и дальнемагистральные соответственно). 
Каждый самолет точно попадает ровно в одну категорию.
В выборке должны присутствовать два атрибута — model_name, category.
*/
/* USE airport;   -- БД airport
 SHOW tables;   -- таблицы БД airport
 SELECT id, model_name, `range`, production_year, 
 CASE 
    WHEN `range` <= 2500
         THEN "short-haul"
	WHEN `range` > 2500 AND `range` <= 6000
		THEN "medium-haul"
	ELSE "long-haul"
 END AS category
 FROM airliners;
*/
/* Выведите данные о билетах разной ценовой категории. 
Среди билетов экономкласса (Economy) добавьте в выборку билеты с ценой от 10 000 до 11 000 включительно. 
Среди билетов комфорт-класса (PremiumEconomy) — билеты с ценой от 20 000 до 30 000 включительно. 
Среди билетов бизнес-класса (Business) — с ценой строго больше 100 000. 
В решении необходимо использовать оператор CASE.
В выборке должны присутствовать три атрибута — id, service_class, price.
*/ 
/*
use airport;
SELECT id, service_class, price
FROM tickets
WHERE 
CASE service_class
	WHEN 'Economy' THEN price BETWEEN 10000 AND 11000
    WHEN 'PremiumEconomy' THEN price BETWEEN 20000 AND 30000
    WHEN  'Business' THEN price > 100000
END;
*/
/* Руководство авиакомпании снизило цены на билеты рейсов LL4S1G8PQW, 0SE4S0HRRU и JQF04Q8I9G. 
Скидка на билет экономкласса (Economy) составила 15%, на билет бизнес-класса (Business) — 10%, 
а на билет комфорт-класса (PremiumEconomy) — 20%. Определите цену билета в каждом сегменте с учетом скидки.
В выборке должны присутствовать три атрибута — id, trip_id, new_price.
*/
/*
SELECT id, trip_id,
CASE
WHEN service_class = 'Economy' THEN price * 0.85
WHEN service_class = 'PremiumEconomy' THEN price * 0.8
WHEN service_class = 'Business' THEN price * 0.9
END AS new_price
FROM tickets
WHERE trip_id IN ('LL4S1G8PQW', '0SE4S0HRRU', 'JQF04Q8I9G')
*/

/* Вывести сотрудников с job_id ST_CLERK, 
отсортированными по зарплате - от самой большой зарплаты до самой маленькой
*/
/*
USE hr;
SELECT *
FROM employees
WHERE job_id = 'ST_CLERK'
ORDER BY salary DESC;
*/
/* 
Вывести сотрудников, чьи имена начинаются на букву D и отсортировать их в алфавитном порядке по фамилии
*/
/*
USE hr;
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE 'D_%'
ORDER BY last_name
*/
















