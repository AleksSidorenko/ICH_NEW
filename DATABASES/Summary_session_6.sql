-- Вывести имя, фамилию, название департамента и название должности сотрудника.
-- USE hr;
-- SELECT * FROM employees;
-- SELECT * FROM departments;
-- SELECT * FROM jobs;
-- SELECT a_emp.first_name, a_emp.last_name, a_job.job_title, a_dep.department_name
-- FROM employees AS a_emp
-- LEFT JOIN departments AS a_dep ON a_dep.department_id = a_emp.department_id
-- LEFT JOIN jobs AS a_job ON a_job.job_id = a_emp.job_id

-- Выведите имена покупателей, которые совершили покупку на сумму больше 1000 условных единиц. 
-- В выборке должно присутствовать два атрибута — cname, amt.
-- USE shop;
-- SELECT * FROM CUSTOMERS;
-- SELECT * FROM ORDERS;
-- SELECT * FROM SELLERS;
-- SELECT CNAME, AMT
-- FROM CUSTOMERS AS a_cus
-- INNER JOIN ORDERS AS a_ord ON a_ord.CUST_ID = a_cus.CUST_ID AND a_ord.AMT > 1000

-- Выведите имена покупателей, которые сделали заказ.
-- Предусмотрите в выборке также имена продавцов.
-- Примечание: покупатели и продавцы должны быть из разных городов.
-- В выборке должно присутствовать два атрибута — cname, sname.
-- SELECT a_cus.cname, a_sel.sname
-- FROM customers AS a_cus
-- INNER JOIN orders AS a_ord ON a_cus.cust_id = a_ord.cust_id
-- LEFT JOIN sellers AS a_sel ON a_sel.sell_id = a_ord.sell_id  
-- WHERE a_cus.city != a_sel.city

-- select cus.cname, sel.sname
-- from CUSTOMERS as cus
-- INNER JOIN ORDERS as ord on ord.cust_id = cus.cust_id
-- LEFT JOIN SELLERS as sel on sel.sell_id = ord.sell_id
-- WHERE cus.city != sel.city

-- Для каждого сотрудника выведите разницу между комиссионными его босса и его собственными. 
-- Если у сотрудника босса нет, выведите NULL.
-- Вывести : sname, difference.
-- SELECT sel.SNAME, sel.BOSS_ID, a_sel.COMM - sel.COMM
-- FROM SELLERS AS sel
-- LEFT JOIN SELLERS AS a_sel ON sel.BOSS_ID = a_sel.SELL_ID;

-- Выведите список студентов с курсом, на который каждый записан (результат содержит имя студента - name и course_id).
-- USE uni;
-- SELECT t1.name, t3.course_id, t2.title
-- FROM Students t1
-- INNER JOIN Students2Courses t3 ON t3.student_id = t1.id
-- INNER JOIN Courses t2 ON t3.course_id = t2.id

-- Выведите список студентов, который не записаны на какой-либо курс.
-- SELECT t1.name, t3.course_id
-- FROM Students t1
-- LEFT JOIN Students2Courses t3 ON t3.student_id = t1.id
-- WHERE t3.course_id IS NULL

-- Выведите список преподавателей с компетенциями (имя преподавателя, competencies_id)
-- Измените предыдущий запрос так, чтобы вместо competencies_id было название компетенции.
-- SELECT t1.name, t2.competencies_id, t3.title
-- FROM Teachers t1
-- INNER JOIN Teachers2Competencies t2 ON t2.teacher_id = t1.id
-- INNER JOIN Competencies t3 ON t2.competencies_id = t3.id;





