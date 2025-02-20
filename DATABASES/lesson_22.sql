-- Создайте SQL запрос, который позволяет вывести информацию о населении стран 
-- в двух столбцах: 'CountryCode' и 'Население', 
-- где 'Население' представляет собой суммарное количество жителей всех городов 
-- в каждой стране.
-- USE world;
-- SELECT CountryCode, SUM(Population) 
-- FROM city
-- GROUP BY CountryCode
##############
# Отобразите результат аналогично заданию 1, однако вместо 'CountryCode' включите названия стран.
-- select country.Name, SUM(city.Population) as total_pop
-- from city
-- left join country on city.CountryCode = country.Code
-- group by country.Name
-- order by total_pop desc
###############
# Предоставьте список стран, указав количество используемых языков в каждой из них
-- SELECT Name, COUNT(Language) AS cnt_lang
-- FROM country
-- LEFT JOIN countrylanguage AS a_counL ON a_counL.CountryCode = country.Code
-- GROUP BY Name
-- ORDER BY cnt_lang DESC
#####
# Выведите количество сотрудников, работающих в отделах Marketing и IT
-- use hr;
-- select *
-- from employees;
-- select count(employee_id)
-- from departments as dp
-- inner join employees as em on dp.department_id = em.department_id and department_name in ('Marketing', 'IT')
############
# Выведите  количество сотрудников, работающих в отделах Marketing и IT для каждого департамента по отдельности.
-- select *
-- from employees;
-- select department_name, count(employee_id)
-- from departments as dp
-- inner join employees as em on dp.department_id = em.department_id and department_name in ('Marketing', 'IT')
-- GROUP BY department_name
#########
# Посчитайте сумму зарплат всех сотрудников
-- SELECT SUM(salary)
-- FROM employees
############
# Посчитайте сумму зарплат сотрудников, работающих в IT
-- select department_name, SUM(salary) 
-- from  employees as emp
-- Inner join departments as dep on emp.department_id = dep.department_id AND department_name = 'IT';
###########
# Выведите имена студентов и id курса, которые они проходят
-- USE uni;
-- SELECT name, course_id
-- FROM Students AS std
-- INNER JOIN Students2Courses AS std_cour ON std_cour.student_id = std.id
#########
# Измените запрос в задании 1 так, чтобы выводились имена студентов и названия курсов, которые они проходят
-- select s2c.course_id, c.title, st.name from Students st
-- left join Students2Courses s2c on st.id = s2c.student_id
-- left join Courses c on s2c.course_id = c.id
#######
# Изменить запрос в задании 2 так, чтобы выводились дополнительно имена старост для каждого курса.
-- select *
-- from Courses;
-- select s2c.course_id, c.title, st.name , st_name.name from Students st
-- left join Students2Courses s2c on st.id = s2c.student_id
-- left join Courses c on s2c.course_id = c.id
-- left join Students as st_name on c.headman_id = st_name.id
##########
# Вывести имена всех преподавателей с их компетенциями
-- SELECT t.name teacher_name, c.title
-- FROM Teachers `t`
-- LEFT JOIN `Teachers2Competencies` t2c ON t.id = t2c.teacher_id
-- LEFT JOIN `Competencies` `c` ON t2c.competencies_id = c.id;
-- Найти преподавателя, у которого нет компетенций
-- SELECT t.name teacher_name, c.title
-- FROM Teachers `t`
-- LEFT JOIN `Teachers2Competencies` t2c ON t.id = t2c.teacher_id
-- LEFT JOIN `Competencies` `c` ON t2c.competencies_id = c.id
-- WHERE t2c.competencies_id is NULL
##########
# Найти имена студентов, которые не проходят ни один курс
-- select s.`name`
-- from Students as s
-- left join Students2Courses as s2c on s.id = s2c.student_id
-- where s2c.course_id is null;
########
# Найти курсы, которые не посещает ни один студент
-- SELECT * FROM Students;
-- SELECT * FROM Courses;
-- SELECT * FROM Students2Courses; 

-- SELECT Courses.title FROM Students							# Есть лишние проверки.
-- 	RIGHT JOIN Students2Courses AS s2c ON Students.id = s2c.student_id
--     RIGHT JOIN Courses ON Courses.id = s2c.course_id
-- WHERE s2c.course_id IS NULL;

-- SELECT Courses.title FROM Students2Courses AS s2c			# Оптимизированный запрос.
--     RIGHT JOIN Courses ON Courses.id = s2c.course_id
-- WHERE s2c.course_id IS NULL;
###########
# Найти компетенции, которых нет ни у одного преподавателя
-- SELECT *
-- FROM Competencies;
-- SELECT *
-- FROM Teachers2Competencies;

-- SELECT com.title
-- FROM Competencies AS com
-- LEFT JOIN Teachers2Competencies ON com.id = Teachers2Competencies.competencies_id
-- WHERE competencies_id IS NULL
##########
# Отобразить имена студентов и старост, курсов на которых они обучается и имена их преподавателей.
-- SELECT stud.name AS stud_name, stud_2.name AS headm_name, title, teac.name 
-- FROM Students AS stud
-- LEFT JOIN Students2Courses AS s2c ON s2c.student_id = stud.id
-- LEFT JOIN Courses AS cour ON cour.id = s2c.course_id
-- LEFT JOIN Students AS stud_2 ON cour.headman_id = stud_2.id
-- LEFT JOIN Teachers AS teac ON cour.teacher_id = teac.id
###########
# Какой староста курирует больше всех дисциплин?
-- SELECT t1.name, COUNT(t2.id)
-- FROM Students t1
-- INNER JOIN Courses t2 ON t2.headman_id = t1.id
-- GROUP BY headman_id
-- ORDER BY COUNT(t2.id) DESC
-- LIMIT 1
##########
# Вывести преподавателя, который ведет больше всех дисциплин.
-- select t1.name, count(t2.title) as disc
-- from Teachers t1
-- join Courses t2 on t1.id = t2.teacher_id
-- group by teacher_id
-- order by disc DESC 
-- limit 1

















