/* Сформировать поле SALARY_GROUP которое принимает
a. значение 1, если зп сотрудника больше 10000
b. значение 0, если зп сотрудника меньше 10000

SELECT salary,
CASE
WHEN salary > 10000 THEN 1 
ELSE 0
END AS SALARY_GROUP
FROM hr.employees;
*/
/* Оператор distinct 
SELECT * FROM employees;
SELECT DISTINCT first_name
  FROM employees;
*/
/* Найти сумму зарплат тех сотрудников, которые зарабатывают больше 10000. Решите задачу через CASE
SELECT salary,
SUM(
	CASE
		WHEN salary < 10000 THEN 0
        ELSE salary
	END) AS new_salary
FROM hr.employees;
*/
/* SELECT department_id,
CASE
	WHEN department_id = 60 THEN salary
    WHEN department_id = 90 THEN salary
    WHEN department_id = 100 THEN salary
    ELSE 0
END
AS Salary_case
FROM employees

USE hr;
SELECT department_id,

CASE
	WHEN department_id = 60 THEN salary
    WHEN department_id = 90 THEN salary
    WHEN department_id = 100 THEN salary
    ELSE null
END
AS SUM_Salary_case
FROM employees

SELECT department_id,
avg(IF(department_id = 60, salary, null))
FROM employees
CASE department_id
	WHEN 60 THEN salary
    WHEN 90 THEN salary
    WHEN 100 THEN salary
    ELSE null
END
AS Salary_case
FROM employees
WHERE
(CASE department_id
	WHEN 60 THEN salary
    WHEN 90 THEN salary
    WHEN 100 THEN salary
    ELSE null
END) = salary

SELECT
  department_id,
  CASE
    WHEN salary > 10000 THEN 1
    ELSE 0
  END AS salary_case
FROM employees;
SELECT SUM(
    CASE
      WHEN salary > 10000 THEN 1
      ELSE 0
    END
  ) AS sum_of_ones
FROM employees;
*/
-- Найти все имеющиеся job_id
-- 2. Найти job_id у которых нет COMMISSION_PCT или зп меньше 3000
/* SELECT job_id, salary,commission_pct,
IF(commission_pct is null OR salary < 3000, job_id, null)
FROM hr.employees

SELECT department_id, salary
     FROM employees
     WHERE department_id in (60, 90, 110)
-- Посмотрите на таблицу jobs. Напишите запрос, который возвращает job_id и max_salary. 
-- Отсортируйте выборку по убыванию - максимальные зарплаты выводятся первыми.
SELECT job_id, max_salary
FROM hr.jobs
ORDER BY max_salary DESC
*/
/*
-- Добавьте в выборке дополнительный столбец rank, который имеет два значения: 
-- high и low и вычисляется по правилам high>10000, low <=10000.
-- Отсортируйте выборку по возрастанию этого нового поля rank.
-- Напишите этот запрос с использованием условного оператора case/when/end и IF.
SELECT max_salary,
-- IF(max_salary>10000, 'high', 'low') AS 'rank'
CASE
	WHEN max_salary > 10000 THEN 'high'
    ELSE 'low'
END AS 'rank'
FROM hr.jobs
ORDER BY max_salary
*/
SELECT *
from hr.employees
WHERE department_id IN (60, 90, 110)
ORDER BY last_name;
-- Разделите города на 3 категории по населению: меньше 100000 - under populated, более 100000, 
-- но менее 1000000 - averagely populated, 
-- и более миллиона - millionaire. Напишите запрос, который выводит названия города и категорию по населенности.
SELECT Population,
CASE
	WHEN Population < 100000 THEN 'under populated'
    WHEN Population <= 1000000 THEN 'averagely populated'
    ELSE 'millionaire'
END AS new_popul, Name
FROM world.city
ORDER BY Population DESC
-- Выведите список городов Индии так, чтобы название страны рядом с названием города,
-- было по-русски
SELECT Continent, Population,
sum(
	CASE
		WHEN Continent IN ('Asia') THEN Population
	END) AS sum_pop
FROM world.country
WHERE Continent LIKE 'Asia';
-- Выведите список городов Индии и Германии: названия города, название страны
-- так, чтобы название страны было на русском.
SELECT Name,
CASE
	WHEN Name = 'Germany' THEN 1
END
FROM world.country;




     
     
