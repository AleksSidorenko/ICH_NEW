-- Добавить в таблицу расписание на неделю (5 дней) для нескольких преподавателей и предметов: программирование, 
-- математика, литература, по 2 пары в день
USE 111124_Sidorenko;

-- CREATE TABLE schedule(
-- 		id int PRIMARY KEY auto_increment,
-- 		title_lesson varchar(100),
--         teacher_name varchar(100),
--         date_lesson date,
-- 		number_lesson int CHECK(number_lesson between 1 and 3));

-- INSERT INTO schedule(title_lesson, teacher_name, date_lesson, number_lesson) values
-- ('программирование', 'Teacher_1', '2024-12-9', 1),
-- ('математика', 'Teacher_2', '2024-12-9', 2),
-- ('программирование', 'Semenov A.', '2024-12-10', 2),
-- ('математика', 'Hailova S.', '2024-12-10', 1),
-- ('программирование', 'Teacher1', '2024-12-11', 1),
-- ('литература', 'Teacher3', '2024-12-11', 2),
-- ('программирование', 'Teacher1', '2024-12-12', 1),
-- ('литература', 'Teacher2', '2024-12-12', 2),
-- ('математика', 'Teacher_3', '2024-12-13', 1),
-- ('Программирование', 'Иван Иванов', '2024-12-13', 2), 
-- ('Математика', 'Марья Ивановна', '2024-12-13', 3)


-- Добавить к таблице столбец “время начала” типа строка
-- ALTER TABLE schedule 
-- ADD start_time varchar(10);

-- Установить значение “9:30” для всех первых пар в расписании
-- UPDATE schedule
-- SET start_time = '9:30'
-- WHERE number_lesson = 1;


-- Установить значение “11:00” для всех вторых пар в расписании
-- UPDATE schedule
-- SET start_time = '11:00'
-- WHERE number_lesson = 2;

-- Поменять тип поля “время начала” на типа time
-- ALTER TABLE schedule
-- MODIFY start_time TIME; 

-- Вывести содержимое таблицы, отсортированное по дате в порядке убывания возрастания
-- SELECT *
-- FROM schedule
-- ORDER BY date_lesson DESC

-- Поменять все значения “Литература” на “Физкультура”.
-- update schedule
-- set title_lesson = 'Физкультура'
-- where title_lesson = 'литература'

-- update schedule
-- set title_lesson = 'матан'
-- where lower(title_lesson) = 'математика';

-- update schedule
-- set title_lesson = 'математика'
-- where title_lesson = 'матан';
-- SELECT *
-- FROM schedule 

-- SELECT COUNT(*) FROM employees  -- возвращает количество строк
-- WHERE department_id = 50 ;



