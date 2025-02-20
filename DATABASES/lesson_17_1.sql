-- Вывести имя, фамилию и город сотрудников, 
-- которые работают в Seattle или Toronto.
-- USE hr;
-- SELECT a_emp.first_name, a_emp.last_name, a_loc.city
-- FROM employees AS a_emp
-- INNER JOIN departments AS a_dep ON a_emp.department_id = a_dep.department_id
-- INNER JOIN locations AS a_loc ON a_loc.location_id = a_dep.location_id AND a_loc.city IN ('Seattle', 'Toronto')
-- Option 1
-- select count(*) -- считает строки
-- from employees
-- where department_id is null
-- Option 2
-- select *
-- from employees
-- left join departments on employees.department_id = departments.department_id
-- where departments.department_id is null;

-- Вывести названия департаментов, в которых никто не работает.
-- SELECT department_name
-- FROM departments AS a_dep
-- LEFT JOIN employees AS a_emp ON a_dep.department_id = a_emp.department_id
-- WHERE a_emp.employee_id is NULL

-- Выведите названия департаментов, в которых менеджеры зарабатывают больше 10000.
-- SELECT department_name, salary
-- FROM employees AS a_emp
-- INNER JOIN departments AS a_dep ON a_dep.manager_id = a_emp.employee_id AND a_emp.salary > 10000

-- Выведите имена всех продавцов. Предусмотрите также в выборке имена их боссов, 
-- сформировав атрибут boss_name. В выборке должно присутствовать два атрибута — sname, boss_name.
-- USE shop;
-- SELECT a_sel.SNAME, a_sel1.SNAME AS 'BOSS'
-- FROM SELLERS AS a_sel
-- LEFT JOIN SELLERS AS a_sel1 ON a_sel.BOSS_ID = a_sel1.SELL_ID

-- Напишите запрос, который вернет выборку full join, используя таблицы CUSTOMERS и ORDERS (по ключу CUST_ID). 
-- В выборке должно присутствовать два атрибута — cname, order_id.
-- SELECT * 
-- FROM CUSTOMERS AS a_cus
-- LEFT JOIN ORDERS AS a_ord ON a_cus.CUST_ID = a_ord.CUST_ID
-- UNION
-- SELECT * 
-- FROM CUSTOMERS AS a_cus
-- RIGHT JOIN ORDERS AS a_ord ON a_cus.CUST_ID = a_ord.CUST_ID;
		   
