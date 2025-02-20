/* use hr;
SELECT first_name, last_name, salary
 ,salary *1.1 as new_salary
FROM employees;
*/
-- Выведите список официальных языков всех стран с процентом их использования. 
-- Объясните результат. 

USE world;
SELECT *
FROM countrylanguage
WHERE isOfficial = 'T';

-- Вернем имена, фамилии и зарплаты сотрудников с job id ST_Clerk 
-- из департаментов 50 80 110 с именем содержащим букву J
USE hr;
SELECT first_name, last_name ,   salary
FROM employees
WHERE job_id = 'ST_Clerk' AND department_id IN (50, 80, 110) AND first_name LIKE '%j%'

-- Вывести все департаменты в названии которых 
-- присутствует IT и они из 1700 локации 
-- или же все остальные департаменты  с локацией 2400

SELECT *
FROM hr.departments
WHERE department_name LIKE '%IT%' AND location_id = 1700 OR location_id = 2400;


