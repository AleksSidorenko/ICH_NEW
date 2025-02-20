
-- 1. Подключиться к базе данных world (которая находится на удаленном сервере). 
-- USE world;

-- 2. Посмотреть на таблицы city, country из базы world. 
-- В каждой таблице есть поле название (Name) и население (Population). 
-- Поле Name в одной таблице означает название города, а в другой - название страны. 
-- Написать запрос с помощью UNION, который выводит список названий всех городов и стран с их населением. 
-- Итоговая выборка должна содержать два столбца: Name, Population. 

-- SELECT Name, Population FROM city;
-- UNION
-- SELECT Name, Population FROM country;

-- 3. Посмотреть на таблицы в базе world и объяснить ограничения нескольких столбцов - ответить 1 предложением.

-- 1. PRIMARY KEY - первичный ключ: значение поля уникальное и NOT NULL 
-- 2. NOT NULL DEFAULT - значение поля: по-умолчанию не может быть NULL 
-- 3. DEFAULT NULL - значение поля: по-умолчанию NULL
-- 4. UNIQUE - значение поля уникальное
-- 5. CHECK - значение поля соответствует условию

-- 4. Далее работаем на локальном сервере. Создать новую таблицу citizen, 
-- которая содержит следующие поля: уникальное автоинкрементное, номер соц страхования, имя, фамилию и емейл.

-- USE 111124_Sidorenko;
-- CREATE TABLE citizen(
-- 					id int PRIMARY KEY auto_increment,
--                     soc_sec_num int,
--                     first_name varchar(100),
--                     last_name varchar(100),
--                     email varchar(150)
--                     )
-- SELECT * FROM citizen;
-- 5. На вашем локальном сервере в любой базе создать таблицу без ограничений (любую, можно взять с урока).
-- CREATE TABLE goods_3(								
-- 					id INT, 
-- 					first_name varchar(100),
--                     last_name varchar(100)
--                      )
-- SELECT * FROM goods_3
-- 6. Добавить в таблицу 5 значений. Добавить 3 человека с одинаковыми именами и 2 человека без lastname

-- INSERT INTO goods_3 VALUES
-- (1, 'Alex', ''),
-- (2, 'Olaf', 'Scholz'),
-- (3, 'Matthias', ''),
-- (4, 'Olaf', 'Merkel'),
-- (5, 'Olaf', 'Makron');
-- DESCRIBE goods_3;
-- 7. Использовать оператор alter table … modify , чтобы добавить ограничение not null на поле firstname и lastname. 

-- ALTER TABLE goods_3
-- MODIFY COLUMN first_name varchar(100) NOT NULL,
-- MODIFY COLUMN last_name varchar(100) NOT NULL;

-- 8. Добавить ограничение unique для пары firstname\lastname. 

-- ALTER Table goods_3
-- ADD UNIQUE (first_name,last_name);

-- 9. Удалить таблицу из базы и пересоздать ее, модифицировав запрос create table так, 
--    чтобы он учитывал ограничения (см примеры из класса).

-- DROP TABLE goods_3;  
-- CREATE TABLE goods_3(								
-- 					id INT PRIMARY KEY auto_increment, 
-- 					first_name varchar(100) UNIQUE NOT NULL,
--                     last_name varchar(100) UNIQUE NOT NULL
--                      )
-- DESCRIBE goods_3;
-- 10. Добавить правильные и неправильные данные (нарушающие и не нарушающие ограничения). 

-- INSERT INTO goods_3(first_name, last_name) VALUES
-- ('Alex', 'Torn'),
-- ('Olaf', 'Scholz'),
-- ('Matthias', 'Dorry'),
-- ('Angela', 'Merkel'),
-- ('Emanuel', 'Makron');
-- SELECT * FROM goods_3

-- INSERT INTO goods_3(id, first_name, last_name) VALUES
-- (1, 'Alex', ``),
-- ('Olaf', 12345),
-- ('', '1'),
-- ('Olaf', 'Scholz'),
-- ('Olaf', 'Merkel');





