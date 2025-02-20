-- SELECT COUNT(*) 
-- FROM hr.employees; -- 107 

-- SELECT COUNT(department_id) 
-- FROM hr.employees; -- 106

-- SELECT COUNT(DISTINCT(department_id)) FROM hr.employees;

-- SELECT NOW(), current_date()

-- SELECT MIN(salary), first_name, last_name FROM hr.employees;  -- ошибка
-- SELECT COUNT(salary), first_name, last_name FROM hr.employees;  -- ошибка
-- SELECT MAX(salary), first_name, last_name FROM hr.employees;  -- ошибка

-- SELECT ROUND(AVG(RATING),2) FROM shop.CUSTOMERS
-- WHERE CUST_ID in (301,302);

-- SELECT ROUND(AVG(RATING),2), SUM(RATING), COUNT(RATING), MIN(RATING)- MAX(RATING)
-- FROM shop.CUSTOMERS
-- WHERE CUST_ID in (301,302);

-- SELECT AVG(price), SUM(price)/COUNT(price) FROM airport.tickets;

-- SELECT * FROM hr.employees
-- WHERE salary = (SELECT MIN(salary) FROM employees)

-- SELECT first_name,last_name,salary 
-- FROM hr.employees
-- WHERE salary = (SELECT MIN(salary) FROM employees)

-- SELECT first_name,last_name,salary 
-- FROM hr.employees
-- WHERE salary = (SELECT MIN(salary) FROM employees) OR salary = (SELECT MAX(salary) FROM employees)

-- Вернуть всех сотрудников, из департаментов, в которых есть зарплаты более 10000.
-- SELECT * FROM employees
-- WHERE salary > 10000

-- SELECT department_id FROM employees
-- WHERE salary > 10000

-- SELECT DISTINCT(department_id) FROM employees
-- WHERE salary > 10000

-- SELECT first_name, last_name, salary, department_id
-- FROM employees 
-- WHERE department_id in (SELECT DISTINCT(department_id) FROM employees
-- WHERE salary > 10000) -- WHERE department_id in (90, 100, 30, 80, 20, 110)

-- Найти имена и фамилии сотрудников с максимальной зарплатой HR.EMPLOYEES:
-- USE hr;
-- SELECT max(salary)
-- FROM employees
-- SELECT first_name, last_name, salary
-- FROM employees
-- WHERE salary = (SELECT max(salary)
-- FROM employees)

-- Найти среднюю зарплату по компании и общее число сотрудников.
-- SELECT round(avg(salary), 2) AS avg_sal, count(employee_id) AS cnt
-- FROM employees

-- Найти сотрудников, у которых зарплата меньше средней зарплаты по компании.
-- SELECT avg(salary)
-- FROM employees
-- SELECT first_name, last_name, salary
-- FROM employees
-- WHERE salary < (SELECT avg(salary)
-- FROM employees) 

-- Найти общее количество департаментов.
-- Найти количество департаментов, в которых никто не работает.
-- SELECT COUNT(emp.department_id)
-- FROM departments AS dep
-- LEFT JOIN employees AS emp ON emp.department_id = dep.department_id
-- WHERE emp.department_id is NULL 

-- Найти среднюю зарплату в департаменте с id 90.
-- Найти самую большую зарплату среди сотрудников, работающих в департаментах с id 70 и 80.
/*
SELECT ROUND(AVG(salary), 2)
FROM employees
WHERE department_id = 90
*/
-- SELECT MAX(salary)
-- FROM employees
-- WHERE department_id IN (70, 80)

-- Найти количество сотрудников из департамента с айди 100, которые зарабатывают более 5000.
-- SELECT COUNT(*)
-- FROM employees
-- WHERE department_id = 100 AND salary > 5000

-- Найти количество сотрудников из департамента с айди 60, 
-- которые зарабатывают больше средней зарплаты по компании.
-- SELECT COUNT(*) FROM employees
-- WHERE department_id = 60 AND salary > (SELECT AVG(salary) FROM employees);

-- Подсчитайте количество людей на каждой позиции (job_id)
-- SELECT job_id, COUNT(*) AS de_emp_amount
-- FROM employees
-- GROUP BY job_id

-- Выведите среднюю (максимальную, минимальную) зарплату по отделу.
-- SELECT AVG(salary), MAX(salary), MIN(salary), department_id
-- FROM employees
-- GROUP BY department_id

-- Выведите количество сотрудников у каждого менеджера.
-- select manager_id,count(*)
-- from employees
-- group by manager_id

-- SELECT department_id, job_id, AVG(salary)
-- FROM employees
-- GROUP BY department_id, job_id























