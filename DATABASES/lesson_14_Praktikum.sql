/*
Подключитесь к базе данных  students. 
Воспользуйтесь командой describe <table_name> чтобы посмотреть свойства таблиц. 
Например, таблицы Students. 
Ответьте на вопрос: каких ограничений ей может не хватать?
*/
USE 111124_Sidorenko;
-- USE students;
-- DESCRIBE Students;

/*
Обычно имя - это first name и last name. 
Создайте у себя на локальном сервере аналогичную таблицу так, 
чтобы в ней было два поля - first_name, last_name вместо name. 
Учтите, что возраст не может быть меньше, например, 16 и больше 60 лет. 
Создавая таблицу students, также учтите и это ограничение.
*/

-- CREATE TABLE new_students(
-- 						id int PRIMARY KEY auto_increment, 
--                         first_name varchar(100) NOT NULL,
--                         last_name varchar(100) NOT NULL,
--                         age int NOT NULL CHECK(age BETWEEN 16 AND 60) # либо CONSTRAINT age_check CHECK(age BETWEEN 16 AND 60) отдельной строкой
--                         
-- SELECT *
-- FROM new_students;
-- SHOW TABLES

-- Добавьте к таблице поле email так, чтобы оно было уникальным.   
-- ALTER TABLE new_students
-- ADD COLUMN email varchar(150) NOT NULL UNIQUE      
-- DESCRIBE new_students;       

-- Попробуйте добавить несколько записей в таблицу так, чтобы уникальность по емейлу была нарушена. 
-- INSERT INTO new_students(first_name, last_name, age, email) VALUES
-- ('Alex', 'Torn', 60, 'abc@gmail.com'),
-- ('Olaf', 'Scholz', 18, 'olafscho@gmail.com');
-- INSERT INTO new_students(first_name, last_name, age, email) VALUES
-- ('John', 'Gandy', 19, 'ab@gmail.com'),
-- ('Olaf', 'Merkel', 59, 'Merkel@gmail.com');
-- SELECT * FROM new_students;

-- Подумайте, какие ограничения на таблицу students также имеют смысл, например, 
-- сочетание имени и фамилии может быть уникальным.
-- ALTER TABLE new_students
-- ADD CONSTRAINT full_name_unique UNIQUE(first_name, last_name);
-- SELECT * FROM new_students;
-- DESCRIBE new_students;
-- SHOW CREATE TABLE new_students;

-- Подключимся к базе hr, создадим частичную копию таблицы employees 
-- с названием new_students: create table new_students 
-- as select employee_id, first_name, last_name, email from employees;
-- CREATE TABLE new_students_2 AS SELECT employee_id, first_name, last_name, email FROM hr.employees;
-- SELECT * FROM new_students_2;

-- Создать таблиwe new_students_3 наполнить данными на основе всей таблицы employees из hr 
-- CREATE TABLE new_students_3 AS SELECT * FROM hr.employees;
-- SELECT * FROM new_students_3;

-- Теперь напишите запрос с union all который выведет имена всех студентов из таблицы 2 и 3
-- SELECT first_name 
-- FROM new_students_2
-- UNION
-- SELECT first_name 
-- FROM new_students_3;

-- Вывести имена, фамилии, email и номер филиала, из которого пришел сотрудник, 
-- там где это возможно.

-- SELECT first_name, last_name, email, NULL AS department_id
-- FROM new_students_2
-- UNION
-- SELECT first_name, last_name, email, department_id
-- FROM new_students_3
-- UNION 
-- SELECT first_name, last_name, email, NULL AS department_id
-- FROM new_students;






