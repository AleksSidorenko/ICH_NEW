-- 1. Подключиться к базе данных hr
USE hr;

-- 2. Вывести список region_id, total_countries, где total_countries - количество стран в таблице. 
--    Подсказка: работаем с таблицей countries, использовать оконную функцию over() и суммировать count(country_id).

SELECT DISTINCT region_id, COUNT(country_id) OVER() AS total_countries
FROM countries;

-- 3. Изменить запрос 2 таким образом, чтобы для каждого region_id выводилось количество стран в этом регионе. 
--    Подсказка: добавить partition by region_id в over().

SELECT DISTINCT region_id, COUNT(country_id) OVER(PARTITION BY region_id) AS total_countries
FROM countries;

-- 4. Работа с таблицей departments. Написать запрос, который выводит location_id, department_name, dept_total, 
--    где dept_total - количество департаментов в location_id.
-- SELECT * FROM departments;

SELECT location_id, department_name, COUNT(department_id) OVER(PARTITION BY location_id) AS dept_total
FROM departments;

-- 5. Изменить запрос 4 таким образом, чтобы выводились названия городов соответствующих location_id. 
-- SELECT * FROM locations;

SELECT dep.location_id, loc.city, dep.department_name, COUNT(dep.department_id) OVER(PARTITION BY dep.location_id) AS dept_total
FROM departments AS dep
LEFT JOIN locations AS loc ON loc.location_id = dep.location_id;

-- 6. Работа с таблицей employees. Вывести manager_id, last_name, total_manager_salary, 
--    где total_manager_salary - общая зарплата подчиненных каждого менеджера (manager_id).
-- SELECT * FROM employees;

SELECT emp.manager_id, emp_dop.last_name, emp.total_manager_salary
FROM (SELECT manager_id, SUM(salary) AS total_manager_salary
FROM employees
GROUP BY manager_id) AS emp
INNER JOIN employees AS emp_dop ON emp.manager_id = emp_dop.employee_id;


