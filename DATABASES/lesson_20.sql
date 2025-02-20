-- Найти количество сотрудников в каждом департаменте. 
-- Вывести department_id и employees_cnt
-- Найти количество сотрудников в каждом департаменте. 
-- Вывести department_name и employees_cnt (количество сотрудников)
-- USE hr;
-- SELECT department_name, COUNT(employee_id) as employees_cnt
-- FROM employees
-- INNER JOIN departments on employees.department_id = departments.department_id
-- GROUP BY department_name
-- ORDER BY employees_cnt desc
#################
-- Найти количество сотрудников у каждого менеджера. Вывести manager_id и employees_cnt
-- Найти количество сотрудников у каждого менеджера. Вывести first_name,  last_name и employees_cnt
-- SELECT * FROM employees;
-- SELECT manager_id, COUNT(employee_id) AS employees_cnt
-- FROM employees
-- GROUP BY manager_id
################
-- SELECT man.first_name, man.last_name, COUNT(emp.employee_id) AS employees_cnt
-- FROM employees AS emp
-- LEFT JOIN employees AS man ON man.employee_id = emp.manager_id
-- GROUP BY emp.manager_id, man.first_name, man.last_name
################
-- Найти максимальную зарплату в каждом департаменте. Вывести department_id и max_salary
-- SELECT department_id, MAX(salary) AS max_salary
-- FROM employees
-- GROUP BY department_id
-- ORDER BY max_salary DESC
##################
-- Найти количество сотрудников в каждом городе (вывести название города, 
-- и количество сотрудников, которые в нем работают).
-- SELECT * FROM locations;
-- SELECT * FROM employees;
-- SELECT * FROM departments;
-- SELECT loc.city, COUNT(employee_id) AS cnt
-- FROM employees AS emp
-- LEFT JOIN departments AS dep ON dep.department_id = emp.department_id
-- LEFT JOIN locations AS loc ON loc.location_id = dep.location_id
-- GROUP BY loc.city
-- ORDER BY cnt DESC;
####################
-- Выведите 10 городов с наибольшим населением:  название города, страна, население. 
-- Подсказка: использовать join с таблицей country
-- USE world;
-- SELECT * FROM city;
-- SELECT * FROM country;
-- SELECT cit.Name, cnt.Name, cit.Population
-- FROM city AS cit
-- INNER JOIN country AS cnt ON cnt.Code = cit.CountryCode
-- ORDER BY cit.Population DESC
-- LIMIT 10
#######################
-- Выведите название страны и количество городов в ней.
-- SELECT cnt.Name, COUNT(cit.Name) AS cnt_cit
-- FROM country AS cnt
-- LEFT JOIN city AS cit ON cit.CountryCode= cnt.Code
-- GROUP BY cit.CountryCode
-- ORDER BY cnt_cit DESC
##########################
-- Выведите разбивку населения по провинциям Голландии.
-- SELECT SUM(Population), District 
-- FROM city
-- WHERE CountryCode = 'NLD'
-- GROUP BY District
#######################
-- Выведите 10 стран с наиболее высокой продолжительностью жизни
-- SELECT Name, LifeExpectancy
-- FROM country
-- ORDER BY LifeExpectancy DESC
-- LIMIT 10





