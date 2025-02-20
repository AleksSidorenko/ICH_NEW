-- Вывести имя и фамилию и название департамента только тех сотрудников, которые работают в IT, Treasury или IT Support.
-- USE hr;
-- SELECT first_name, last_name, department_name
-- FROM departments AS a_dep
-- INNER JOIN employees AS a_emp ON a_dep.department_id = a_emp.department_id AND department_name IN ('IT', 'Treasury', 'IT Support');

-- Вывести имя и фамилию сотрудника и имя и фамилию его менеджера.

-- SELECT emp.first_name, emp.last_name, manager.first_name, manager.last_name 
-- FROM employees AS emp
-- INNER JOIN employees AS manager ON emp.manager_id = manager.employee_id*/
-- USE hr;
-- SELECT *
-- FROM employees AS emp
-- INNER JOIN employees AS manager ON emp.manager_id = manager.employee_id
-- ORDER BY emp.employee_id;

-- Вывести job_id тех сотрудников, которые зарабатывают больше своего менеджера.
-- SELECT DISTINCT a_emp.job_id
-- FROM employees AS a_emp
-- INNER JOIN employees AS a_manager ON a_emp.manager_id = a_manager.employee_id AND a_emp.salary > a_manager.salary;

-- Используя данные из схемы HR выведите имя и фамилию сотрудника и название его департамента (hr.departments)
-- SELECT first_name, last_name, department_name
-- FROM employees AS a_emp
-- LEFT JOIN departments AS a_dep ON a_emp.department_id = a_dep.department_id

