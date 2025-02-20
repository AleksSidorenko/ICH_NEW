# выведите номера отделов и количество сотрудников в каждом отделе, 
# где сотрудников больше 10
-- USE hr;
-- SELECT * FROM employees;
-- SELECT * FROM departments;
/*
SELECT department_id, COUNT(employee_id) AS cnt
FROM employees
GROUP BY department_id
HAVING cnt > 10
*/
/*
SELECT dep.department_name, COUNT(emp.employee_id) AS cnt
FROM employees AS emp
LEFT JOIN departments AS dep ON dep.department_id = emp.department_id
GROUP BY emp.department_id
HAVING cnt > 10
*/
/* Оптимизация - вложенный запрос
SELECT dep.department_name, cnt
FROM 
(SELECT department_id, COUNT(employee_id) AS cnt
FROM employees 
GROUP BY department_id 
HAVING cnt > 10) AS emp
LEFT JOIN departments AS dep ON dep.department_id = emp.department_id
*/
# Вывести количество сотрудников, получающих зарплату более 5000, в департаментах, где сотрудников больше 8.
/*
SELECT COUNT(employee_id) AS cnt, department_id
FROM employees
WHERE salary > 5000
GROUP BY department_id
HAVING cnt > 8
*/
# найти максимальную зарплату в каждом департаменте. Вывести department_id и max_salary.
/*
SELECT department_id, MAX(salary) AS max_salary
FROM employees
GROUP BY department_id;
*/
# Найти сотрудников, у которых наибольшая зарплата в их департаменте.
/*
SELECT first_name, last_name, emp.department_id, emp.salary
FROM (SELECT department_id, MAX(salary) AS max_salary
FROM employees
GROUP BY department_id
) AS new_emp
INNER JOIN employees AS emp ON emp.department_id = new_emp.department_id AND new_emp.max_salary = emp.salary
ORDER BY salary DESC
*/
# Найти департамент (или департаменты) с наибольшим кол-вом сотрудников. 
# (вывести все имеющиеся данные об этих департаментах).
/*
SELECT emp.department_id, dep.department_name, dep.manager_id, dep.location_id, COUNT(emp.employee_id) AS cnt
FROM employees AS emp
INNER JOIN departments AS dep ON dep.department_id = emp.department_id
GROUP BY department_id
ORDER BY cnt DESC
*/
/*
SELECT COUNT(emp.employee_id) AS cnt
FROM employees AS emp
GROUP BY department_id;

SELECT dep.department_name, MAX(cnt)
FROM (SELECT COUNT(emp.employee_id) AS cnt
FROM employees AS emp
GROUP BY department_id) AS new_emp;

SELECT department_id
FROM employees AS emp
GROUP BY department_id
HAVING COUNT(employee_id) = (SELECT MAX(cnt)
FROM (SELECT COUNT(employee_id) AS cnt
FROM employees AS emp
GROUP BY department_id) AS new_emp)
*/
/*
select count(employee_id) -- * from departments;
from employees
group by department_id; 

select max(mux_num)
from (select count(employee_id) as mux_num
from employees
group by department_id) as t1;

select max(mux_num)
from (select count(employee_id) as mux_num
from employees
group by department_id) as t1;

select department_id
from employees
group by department_id
having count(employee_id) = (select max(mux_num)
from (select count(employee_id) as mux_num
from employees
group by department_id) as t1);

select *
from departments
where department_id in (select department_id
from employees
group by department_id
having count(employee_id) = (select max(mux_num)
from (select count(employee_id) as mux_num
from employees
group by department_id) as t1))
*/
/*
SELECT dep.*, emp_amount
FROM departments AS dep
JOIN (
    SELECT department_id, COUNT(*) AS emp_amount
    FROM employees
    GROUP BY department_id
) AS emp_counts 
ON dep.department_id = emp_counts.department_id
WHERE emp_counts.emp_amount = (
    SELECT MAX(emp_count) 
    FROM (
        SELECT COUNT(*) AS emp_count 
        FROM employees 
        GROUP BY department_id
    ) AS max_emp
);
*/
# Выведите название отделов с кол-вом сотрудников больше среднего.
/*
select department_name
from departments;

select count(employee_id)
from employees
group by department_id;

select avg(workers)
from (select count(employee_id) as workers
from employees
group by department_id) as t1;

select department_id
from employees
group by department_id
having count(employee_id) >= (select avg(workers)
from (select count(employee_id) as workers
from employees
group by department_id) as t1);

select department_name
from departments
where department_id in(select department_id
from employees
group by department_id
having count(employee_id) >= (select avg(workers)
from (select count(employee_id) as workers
from employees
group by department_id) as t1));
*/
-- USE shop;
# напишите SQL-запрос для определения города с наибольшим числом клиентов 
# в базе данных. 
# Выведите название города и общее количество клиентов в этом городе, 
# при условии, что в городе проживает более одного клиента.
-- SELECT * FROM CUSTOMERS;
/*
SELECT CITY, COUNT(CUST_ID) AS cnt
FROM CUSTOMERS
GROUP BY CITY
HAVING cnt > 1;
*/
# Вывести самое большое число клиентов в городе
/*
SELECT MAX(cnt)
FROM (SELECT CITY, COUNT(CUST_ID) AS cnt
FROM CUSTOMERS
GROUP BY CITY
HAVING cnt > 1) AS cnt_max;
*/
# Вывести все города, в которых 2 клиента.
/*
select count(cust_id), CITY
from CUSTOMERS
group by CITY
having count(cust_id) = (select max(cus)
	from (select count(cust_id) as cus, CITY
		from CUSTOMERS
		group by CITY
		having count(cust_id) > 1) t1);
*/
# вывести всех сотрудников, из департаментов, 
# в которых есть хотя бы один сотрудник с зарплатой 12000 и более.
-- USE hr;
-- SELECT * FROM employees;
/*
SELECT DISTINCT department_id
FROM employees
WHERE salary >= 12000;

SELECT first_name, last_name, department_id, salary
FROM employees
WHERE department_id IN (SELECT DISTINCT department_id
FROM employees
WHERE salary >= 12000)
*/













