-- Выведите 10 стран с наиболее высокой продолжительностью жизни
-- USE world;
-- SELECT Name, LifeExpectancy
-- FROM country
-- ORDER BY LifeExpectancy DESC
-- LIMIT 10
######################
-- Выведите список стран с названиями столиц в каждой
-- SELECT country.Name, city.Name
-- FROM country
-- LEFT JOIN city ON country.Capital = city.ID
#######################
-- Выведите количество стран с республиканской формой правление (Republic)
-- SELECT * FROM country;
-- SELECT Name, COUNT(GovernmentForm)
-- FROM country
-- WHERE GovernmentForm = 'Republic'
-- GROUP BY Name
####################
-- Выведите все формы правление с количеством стран, в которых она присутствует. 
-- Какая самая популярная форма правления?
-- SELECT GovernmentForm, COUNT(Code) 
-- FROM country
-- GROUP BY GovernmentForm
-- ORDER BY COUNT(Code) DESC;
###################
-- Выведите список городов, где население больше (меньше) среднего населения по все городам.
-- select avg(Population)
-- from city;

-- select `Name`, Population
-- from city
-- where Population > (select avg(Population) from city); # (select avg(Population) from city) = '350468.2236'
##################
-- Вывести среднюю, максимальную и минимальную зарплату 
-- и количество подчиненных менеджеров в департаментах 50, 60, 80. 
-- Результат должен показывать количество сотрудников по убыванию. 
-- Если одинаковое количество сотрудников, то по убыванию средней зарплаты.
-- USE hr;
-- SELECT manager_id, AVG(salary), MIN(salary), MAX(salary), COUNT(employee_id)
-- FROM employees
-- WHERE department_id IN (50, 60, 80)
-- GROUP BY manager_id
-- ORDER BY COUNT(employee_id) DESC, AVG(salary) DESC
######################
-- Округлить значения, там где это возможно. 
-- Вывести имена и фамилии, менеджеров. 
-- Сравнить их зарплату со средней зарплатой подчиненных.
-- SELECT ROUND(AVG(emp.salary), 2) AS avg_sal, MAX(emp.salary) AS 'MAX', MIN(emp.salary) AS 'MIN', 
--        COUNT(emp.employee_id) AS 'Number of \nemploees', 
-- 		  emp.manager_id, man.salary, 
--         ROUND(man.salary / AVG(emp.salary) * 100, 2) AS '% from avg_sal', 
--         man.first_name, man.last_name FROM employees AS emp
-- 	LEFT JOIN employees AS man ON emp.manager_id = man.employee_id
-- WHERE emp.department_id IN (50, 60, 80)
-- GROUP BY emp.manager_id
-- ORDER BY COUNT(emp.employee_id) DESC, AVG(emp.salary) DESC;
####################
-- Вывести названия департаментов, в которых работают указанные менеджеры.
-- SELECT ROUND(AVG(emp.salary), 2) AS avg_sal, MAX(emp.salary) AS 'MAX', MIN(emp.salary) AS 'MIN', COUNT(emp.employee_id) AS 'Number of \nemploees', 
-- 		emp.manager_id, man.salary, 
--         ROUND(man.salary / AVG(emp.salary) * 100, 2) AS '% from avg_sal', 
--         man.first_name, man.last_name, dep.department_name
--         FROM employees AS emp
-- 	LEFT JOIN employees AS man ON emp.manager_id = man.employee_id
--     LEFT JOIN departments AS dep ON dep.department_id = man.department_id
-- WHERE emp.department_id IN (50, 60, 80)
-- GROUP BY emp.manager_id
-- ORDER BY COUNT(emp.employee_id) DESC, AVG(emp.salary) DESC;
####################
-- Подсчитать количество менеджеров в каждом департаменте
-- SELECT COUNT(DISTINCT manager_id), department_id 
-- FROM employees
-- GROUP BY department_id
###########################
-- Подключитесь к базе данных hr 
-- Выведите одним запросом общее количество департаментов (отделов) в базе, 
-- кол департаментов где есть сотрудники и кол департаментов 
-- где нет сотрудников (на выходе три столбца и одна строчка)
-- COUNT(DISTINCT IF(emp.employee_id IS NULL,  dept.department_id, null)) 'no employees',
-- COUNT(DISTINCT dep.department_id) AS amount - COUNT(DISTINCT emp.department_id) AS dep_with_emp
--
-- SELECT * 
-- FROM employees;
-- SELECT *
-- FROM departments;

-- SELECT COUNT(DISTINCT dep.department_id) AS amount, COUNT(DISTINCT emp.department_id) AS dep_with_emp, 
-- 	   COUNT(DISTINCT dep.department_id) - COUNT(DISTINCT emp.department_id) AS 'No employees'
-- 	  -- COUNT(DISTINCT IF(emp.employee_id IS NULL,  dep.department_id, null)) AS 'no employees'
-- FROM departments AS dep
-- LEFT JOIN employees AS emp ON emp.department_id = dep.department_id

























