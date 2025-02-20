# получить репорт по department_id с минимальной и максимальной зарплатой, 
# с ранней и поздней датой прихода на работу и с количествов сотрудников. 
# Сорировать по количеству сотрудников (по убыванию).

SELECT * FROM departments;
SELECT * FROM employees;
/*
SELECT department_id, COUNT(employee_id) AS cnt, 
MIN(hire_date)AS min_date, MAX(hire_date) AS max_date, MIN(salary) AS min_sal, 
MAX(salary) AS max_sal
FROM employees
GROUP BY department_id
ORDER BY cnt DESC
*/

# Сколько сотрудников которые работают в одном и тоже отделе и получают одинаковую зарплату?
/*
SELECT department_id, salary, COUNT(employee_id) AS cnt
FROM employees
GROUP BY department_id, salary
HAVING cnt > 1
ORDER BY cnt DESC, department_id
*/

# Получить количество департаментов в котором есть сотрудники
/*
SELECT COUNT(DISTINCT department_id)
FROM employees;
# ODER
SELECT COUNT(department_id)
FROM employees
WHERE department_id IS NOT NULL
GROUP BY department_id
*/

# Получить количество сотрудников с одинаковым количеством букв в имени. 
# При этом показать только тех у кого длина имени больше 5 и 
# количество сотрудников с таким именем больше 10. 
# Сортировать по длине имени
/*
SELECT first_name, COUNT(employee_id), length(first_name)
FROM employees;

SELECT length(first_name) AS l_cli, COUNT(employee_id) AS cnt
FROM employees
GROUP BY l_cli
HAVING l_cli > 5 AND cnt > 10
ORDER BY l_cli;
# Optimisiren
SELECT length(first_name) AS l_cli, COUNT(employee_id) AS cnt
FROM employees
WHERE l_cli > 5
GROUP BY l_cli
HAVING cnt > 10
ORDER BY l_cli
*/





