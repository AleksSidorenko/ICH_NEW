-- Создать таблицу Students2Courses
-- id - целое число первичный ключ автоинкремент
-- student_id - целое число
-- course_id - целое число
USE 111124_Sidorenko;
-- CREATE TABLE students2courses
-- (id int PRIMARY KEY auto_increment,
-- student_id int,
-- course_id int)
-- SELECT *
-- FROM students2courses

-- Добавить 6 записей в таблицу Students
-- Анатолий 29
-- Олег 25
-- Семен 27
-- Олеся 28
-- Ольга 31
-- Иван 22
-- INSERT INTO students(name, age)
-- VALUES ('Анатолий', 29),
-- 		('Олег', 25),
-- 		('Семен', 27),
-- 		('Олеся', 28),
-- 		('Ольга', 31),
-- 		('Иван', 22);
-- SELECT *
-- FROM students

-- Добавить 6 записей в таблицу Teachers
-- Петр 39
-- Максим 35
-- Антон 37
-- Всеволод 38
-- Егор 41
-- Светлана 32
-- INSERT INTO teachers(name, age)
-- VALUES ('Петр', 39),
-- 		('Максим', 35),
-- 		('Антон', 37),
-- 		('Всеволод', 38),
-- 		('Егор', 41),
-- 		('Светлана', 32);
-- SELECT *
-- FROM teachers

-- Добавить 4 записей в таблицу Competencies
-- Математика 
-- Информатика
-- Программирование
-- Графика
-- INSERT INTO competencies(title)
-- VALUES ('Математика'),
-- 		('Информатика'),
-- 		('Программирование'),
-- 		('Графика');
-- SELECT *
-- FROM competencies

-- Добавьте 6 записей в таблицу Teachers2Competencies
-- 1 1
-- 2 1
-- 2 3
-- 3 2
-- 4 1
-- 5 3
-- INSERT INTO teachers2competencies(teacher_id, competencies_id)
--  VALUES
--  (1,1), 
--  (2,1), 
--  (2,3), 
--  (3,2), 
--  (4,1), 
--  (5,3);
-- SELECT * FROM teachers2competencies

-- Добавьте 5 записей в таблицу Courses
-- 1 Алгебра логики 2
-- 2 Математическая статистика 3
-- 4 Высшая математика 5
-- 5 Javascript 1
-- 5 Базовый Python 1

-- INSERT INTO courses(teacher_id, title, headman_id)
-- VALUES
-- (1, 'Алгебра логики', 2)
-- ,(2, 'Математическая статистика', 3)
-- ,(4, 'Высшая математика', 5)
-- ,(5, 'Javascript', 1)
-- ,(5, 'Базовый Python', 1);
-- SELECT * FROM courses

-- Добавьте 5 записей в таблицу Students2Courses
-- 1 1
-- 2 1
-- 3 2
-- 3 3
-- 4 5
-- INSERT INTO students2courses(student_id, course_id)
-- VALUES
-- (1, 1)
-- ,(2, 1)
-- ,(3, 2)
-- ,(3, 3)
-- ,(4, 5);



-- SELECT * FROM students2courses;
-- SELECT * FROM courses;
-- SELECT * FROM students2courses;

-- SELECT name, title FROM students
-- LEFT JOIN students2courses ON students2courses.student_id = students.id
-- LEFT JOIN courses ON students2courses.course_id = courses.id
























