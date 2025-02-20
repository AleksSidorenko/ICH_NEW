# Вывести id, имя, фамилию и департамент сотрудника, 
# который был внесен в таблицу несколько раз по ошибке. 
# (работа с базой данных kad)
-- USE kad;
-- SELECT * FROM employees;
/*
SELECT COUNT(employee_id) AS cnt, employee_id, first_name, last_name, department_id
FROM employees
GROUP BY employee_id
HAVING cnt > 1
*/