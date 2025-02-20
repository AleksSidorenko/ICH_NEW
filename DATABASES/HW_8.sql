# 1. Подключитесь к базе данных Students (которая находится на удаленном сервере). 
-- USE students;

# 2. Найдите самого старшего студента
/*
SELECT * FROM Students;
SELECT name, age FROM Students
WHERE age = (SELECT MAX(age) FROM Students)
*/
# 3. Найдите самого старшего преподавателя
/*
SELECT * FROM Teachers;
SELECT name, age FROM Teachers
WHERE age = (SELECT MAX(age) FROM Teachers)
*/
# 4. Выведите список преподавателей с количеством компетенций у каждого
/*
SELECT * FROM Competencies;
SELECT * FROM Teachers;
SELECT * FROM Teachers2Competencies;

SELECT t.name AS name_teacher, COUNT(com.title) AS count_com FROM Teachers AS t
LEFT JOIN Teachers2Competencies AS t2c ON t2c.teacher_id = t.id
LEFT JOIN Competencies AS com ON com.id = t2c.competencies_id
GROUP BY name_teacher
*/
# 5. Выведите список курсов с количеством студентов в каждом
/*
SELECT * FROM Courses;
SELECT * FROM Students2Courses;

SELECT crs.title, SUM(s2c.student_id) AS cnt_std FROM Courses AS crs
LEFT JOIN Students2Courses AS s2c ON crs.id = s2c.course_id
GROUP BY crs.title
*/
# 6. Выведите список студентов, с количеством курсов, посещаемых каждым студентом. 
/*
SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Students2Courses;

SELECT std.name, COUNT(s2c.course_id) AS cnt_crs FROM Students2Courses AS s2c
RIGHT JOIN Students AS std ON std.id = s2c.student_id
GROUP BY std.name
*/
